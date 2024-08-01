from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import Allowance_app, Allowance_input_app
from .forms import AllowanceForm, SpendingForm
from datetime import date, datetime, timedelta
from django.db.models import Sum, Q
from django.utils.timezone import localdate
from django.contrib import messages 
from django.views.generic.edit import FormView

# Create your views here.
#how can I use ID so i don't have to count the number of current IDs in the database?
#add list of purchases
#change nav bar so it can link to other pages


def allowance_input_view(request):
    form = AllowanceForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AllowanceForm()
        return redirect("/spending")
    context = {'form':form}
    return render(request,"allowance_app/allowance.html", context)

def spending_input_view(request):
    form = SpendingForm(request.POST or None)
    if request.method == "POST":
        form = SpendingForm(request.POST)
        if form.is_valid():
            form.save()

    #total

    if Allowance_input_app.objects.count() == 0:
        earliest_date = localdate()
    else:
        earliest_date = Allowance_app.objects.earliest('date').date

    def sum_numbers(numbers):
        if len(numbers) == 0:
            return 0
        return numbers[0] + sum_numbers(numbers[1:])

    date = earliest_date
    days = localdate() - earliest_date
    dates_in_range = Allowance_app.objects.order_by().values_list('date').distinct()
    dates = [item[0] for item in dates_in_range]
    allowance_total = []

    for i in range(days.days+1):
        if date in dates:
            print(date)
            a = Allowance_app.objects.filter(date = date)[0].allowance_no_debt_spending
        else:
            a = allowance_total[-1]
        allowance_total.append(a)
        date = date + timedelta(days=1)
    
    allowance = sum_numbers(allowance_total)
    spent = Allowance_app.objects.filter(credit=False).aggregate(Sum('price'))['price__sum'] - Allowance_app.objects.filter(credit=True).aggregate(Sum('price'))['price__sum']

    i_can_spend_TOTAL = allowance - spent

    #today only 
    #find the LAST allowance on allowance_input_app for the nearest date but not that date
    if localdate() == earliest_date:
        daily_allowance = Allowance_input_app.objects.filter(date = localdate())[0].allowance_no_debt
    else:
        daily_allowance = Allowance_input_app.objects.filter(~Q(date = localdate())).last().allowance_no_debt
    
    i_can_spend_TODAY = daily_allowance - Allowance_app.objects.filter(date = localdate(), credit=False).aggregate(Sum('price'))['price__sum'] + Allowance_app.objects.filter(date = localdate(), credit=True).aggregate(Sum('price'))['price__sum']  

    pk = Allowance_app.objects.latest('id').id

    if form.is_valid():
        form.save()
        b = Allowance_app.objects.get(id=pk)
        b.allowance_no_debt_spending = daily_allowance
        b.save()
        form = SpendingForm()
    
    context = {'form':form,
                "i_can_spend_today": i_can_spend_TODAY,
                "i_can_spend_total": i_can_spend_TOTAL,
            }
    return render(request,"allowance_app/spending.html", context)


def item_list_view(request):
    queryset=Allowance_app.objects.all() #list of objects

    context = {
        "object_list":queryset,
    }

    return render(request, 'allowance_app/item_list.html', context)

####inputting the allowance

def item_update_view(request, id=id):
    obj=get_object_or_404(Allowance_app, id=id)
    form = AllowanceForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form':form
    }
    return render(request, 'allowance_app/input_item.html', context)
