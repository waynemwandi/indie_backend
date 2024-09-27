# daraja/views.py
import datetime
import json

import requests
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from daraja.models import Transaction


# 1. Returns message on 127.0.0.1:8000/api/daraja/
def index(request):
    return HttpResponse("Hello, this is the Indie - Daraja integration app!")


# 2. Returns message on localhost:5173
def test_api(request):
    data = {"message": "Hello from Django!", "status": "success"}
    return JsonResponse(data)


# 3. Generate Access Token using Basic Auth
def get_access_token():
    consumer_key = settings.SAFARICOM_CONSUMER_KEY
    consumer_secret = settings.SAFARICOM_CONSUMER_SECRET
    api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    try:
        response = requests.get(api_url, auth=(consumer_key, consumer_secret))
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to get access token: {e}")
        return None

    print(f"Response Status Code: {response.status_code}")
    print(f"Response Headers: {response.headers}")
    print(f"Response Content: {response.content.decode()}")

    try:
        json_response = response.json()
        access_token = json_response.get("access_token")
        if access_token:
            print(f"Access Token: {access_token}")  # Debugging output
            return access_token
        else:
            print(f"Access token not found in the response: {json_response}")
            return None
    except json.JSONDecodeError as e:
        print(f"JSON decoding error: {e}")
        print(f"Response content: {response.content.decode()}")
        return None


# 4. Test Access Token Generation
@csrf_exempt
def test_access_token(request):
    access_token = get_access_token()
    if access_token:
        return JsonResponse({"access_token": access_token}, status=200)
    else:
        return JsonResponse({"error": "Failed to generate access token"}, status=500)


# 5. Register URLs
@csrf_exempt
def register_urls(request):
    access_token = get_access_token()
    if not access_token:
        return JsonResponse({"error": "Failed to retrieve access token"}, status=500)

    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": f"Bearer {access_token}"}
    payload = {
        "ShortCode": "600999",  # Replace with dynamic shortcode
        "ResponseType": "Completed",
        "ConfirmationURL": "https://indiearts.art/api/daraja/c2b_confirmation/",
        "ValidationURL": "https://indiearts.art/api/daraja/c2b_validation/",
    }

    print(f"Sending request to {api_url}")
    print(f"Headers: {headers}")
    print(f"Payload: {json.dumps(payload, indent=2)}")

    try:
        response = requests.post(api_url, json=payload, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        response_json = response.json()
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Headers: {response.headers}")
        print(f"Response Content: {response.content.decode()}")
        return JsonResponse(response_json)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        if response:
            print(f"Response Status Code: {response.status_code}")
            print(f"Response Headers: {response.headers}")
            print(f"Response Content: {response.content.decode()}")
        return JsonResponse(
            {"error": "Request to Safaricom API failed", "details": str(e)}, status=500
        )


# 6. Validate C2B transactions
@csrf_exempt
def c2b_validation(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse(
                {"ResultCode": 1, "ResultDesc": "Invalid JSON received"}, status=400
            )

        # Convert TransAmount to string to ensure consistency
        data["TransAmount"] = str(data.get("TransAmount", ""))

        # Simple validation
        if "TransAmount" not in data or float(data["TransAmount"]) <= 0:
            return JsonResponse(
                {"ResultCode": 1, "ResultDesc": "Invalid transaction amount"},
                status=400,
            )

        if "MSISDN" not in data or not data["MSISDN"].isdigit():
            return JsonResponse(
                {"ResultCode": 1, "ResultDesc": "Invalid MSISDN"}, status=400
            )

        # If validation passes
        return JsonResponse({"ResultCode": 0, "ResultDesc": "Accepted"})

    return JsonResponse(
        {"ResultCode": 1, "ResultDesc": "Invalid request method"}, status=400
    )


# 6. Confirm C2B transactions and log in db
@csrf_exempt
def c2b_confirmation(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse(
                {"ResultCode": 1, "ResultDesc": "Invalid JSON received"}, status=400
            )

        # Parse transaction time, use current time if parsing fails
        try:
            trans_time = datetime.datetime.strptime(data["TransTime"], "%Y%m%d%H%M%S")
        except ValueError:
            trans_time = datetime.datetime.now()

        account_details = data["BillRefNumber"].split()
        if len(account_details) != 3:
            account_details = ["Unknown", "Unknown", "Unknown"]

        last_name, house_number, month_paid = account_details

        # Create the transaction record
        transaction = Transaction.objects.create(
            transaction_type=data.get("TransactionType", "Unknown"),
            trans_id=data["TransID"],
            trans_time=trans_time,
            trans_amount=float(data["TransAmount"]),
            business_short_code=data["BusinessShortCode"],
            bill_ref_number=data.get("BillRefNumber", ""),
            msisdn=data["MSISDN"],
            first_name=data.get("FirstName", ""),
            last_name=data.get("LastName", ""),
            month_paid=month_paid,
        )

        # Respond with success message
        return JsonResponse({"ResultCode": 0, "ResultDesc": "Accepted"})

    return JsonResponse(
        {"ResultCode": 1, "ResultDesc": "Invalid request method"}, status=400
    )


# 7. Get Payments/Transaction API
def get_payments(request):
    if request.method == "GET":
        transactions = Transaction.objects.all().values(
            "id", "trans_id", "trans_amount", "msisdn", "trans_time"
        )
        return JsonResponse(list(transactions), safe=False)
    else:
        return JsonResponse({"error": "GET request required"}, status=400)
