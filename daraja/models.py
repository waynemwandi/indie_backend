from django.db import models

class Transaction(models.Model):
    transaction_type = models.CharField(max_length=100)
    trans_id = models.CharField(max_length=100, unique=True)
    trans_time = models.DateTimeField()
    trans_amount = models.DecimalField(max_digits=10, decimal_places=2)
    business_short_code = models.CharField(max_length=20)
    bill_ref_number = models.CharField(max_length=100, blank=True, null=True)
    invoice_number = models.CharField(max_length=100, blank=True, null=True)
    third_party_trans_id = models.CharField(max_length=100, blank=True, null=True)
    msisdn = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    month_paid = models.CharField(max_length=20, default="Unknown")
    class Meta:
        db_table = 'transactions'

    def __str__(self):
        return self.trans_id
