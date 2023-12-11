from django.db import models


class Family(models.Model):
    family_name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.family_name
    
class Member(models.Model):
    family_id = models.ForeignKey(Family, verbose_name="خانواده", on_delete=models.CASCADE)
    member_name = models.CharField(max_length=250)
    birthdate = models.DateField(blank=True, null=True)
    member_image = models.ImageField(blank=True, null=True)
    member_capital = models.FloatField()
    member_dept = models.FloatField()
    
    def __str__(self):
        member_str = f"Name : {self.family_id.family_name}, {self.member_name} Capital : {self.member_capital}, Dept : {self.member_dept} "
        return member_str
    