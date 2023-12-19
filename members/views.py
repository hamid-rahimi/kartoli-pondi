from django.shortcuts import render, redirect
from .models import Member, Family
from django.db.models import Avg,Sum,Min,Max,Count


def dashboard_page(request):
    if not request.user.is_authenticated:
        return redirect('login:login_page')
    # members = Member.objects.all()
    # print(members)
    # list_of_members_capital = list((members.values('member_capital')))
    # sum_of_members_capital = sum(m_capital['member_capital'] for m_capital in list_of_members_capital)
    sum_of_members_capital = Member.objects.aggregate(Sum('member_capital'))['member_capital__sum'] # مجموع کل سرمایه
    print(sum_of_members_capital)
    count_of_members = Member.objects.aggregate(Count('id'))['id__count'] # تعداد کل اعضا
    capital_of_member = Member.objects.get(id=1) # سرمایه هر عضو
    sum_of_members_dept = Member.objects.aggregate(Sum('member_dept'))['member_dept__sum'] # مجموع کل بدهی
    cash_fund = sum_of_members_capital - sum_of_members_dept # موجودی صندوق
    families = list(Member.objects.values('family_id__family_name').order_by('family_id_id').
                   annotate(count_of_family=Count("family_id"),
                            sum_of_capital_family=Sum("member_capital"),
                            sum_of_dept_family=Sum('member_dept')))
    i = 1
    families_added_num = list()
    for family in families:
        temp = dict(num=i)
        temp.update(family)
        families_added_num.append(temp)
        i += 1
        
    print(families)
    print(list(temp))
    # print(count_of_family)
    
    return render(request,"members/dashboard.html", {
        'sum_of_members_capital': sum_of_members_capital,
        'count_of_members': count_of_members,
        'capital_of_member': capital_of_member.member_capital,
        'cash_fund': cash_fund,
        'families': families_added_num,
        })

