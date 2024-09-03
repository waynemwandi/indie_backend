# daraja/views.py
import datetime
import json

from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from daraja.models import Transaction


def index(request):
    return HttpResponse("Hello, this is the Indie - Daraja integration app!")


def test_api(request):
    data = {"message": "Hello from Django!", "status": "success"}
    return JsonResponse(data)


def get_payments(request):
    if request.method == "GET":
        transactions = Transaction.objects.all().values(
            "id", "trans_id", "trans_amount", "msisdn", "trans_time"
        )
        return JsonResponse(list(transactions), safe=False)
    else:
        return JsonResponse({"error": "GET request required"}, status=400)


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
