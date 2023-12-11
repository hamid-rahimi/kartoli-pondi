from django.db import models
from members.models import Member


class Loan(models.Model):
    loan_name = models.CharField(max_length=7)
    loan_amount = models.FloatField()
    loan_interest = models.FloatField(default=0)
    loan_count_installment = models.IntegerField()

    def __str__(self):
        loan_str = f"Amount : {self.loan_amount}, Count Installments : {self.loan_count_installment}"
        return loan_str

class LoanPayment(models.Model):
    loan_id = models.ForeignKey(Loan, verbose_name="کد وام", on_delete=models.CASCADE)
    member_id = models.ForeignKey(Member, verbose_name="عضو", on_delete=models.CASCADE)
    payment_date = models.DateField()
    settling_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        loanPayment_str = f"Member Name : {self.member_id.member_name}, Loan : {self.loan_id.loan_amount}"
        return loanPayment_str
    