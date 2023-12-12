from django.db import models
from members.models import Member


defaultMonthlyAmount = 80000
# Create your models here.
class MonthlyReceipt(models.Model):
    member_id = models.ForeignKey(Member, verbose_name="نام عضو", on_delete=models.CASCADE)
    receipt_date = models.DateField()
    monthly_amount = models.FloatField(default=defaultMonthlyAmount)
    installment_amount = models.FloatField(default=0)
    
    def __str__(self):
        receipt_str = f"Name : {self.member_id.member_name}, Monthly amount : {self.monthly_amount}, Installment amount : {self.installment_amount}"
        return receipt_str
    