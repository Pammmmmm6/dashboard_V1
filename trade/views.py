from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from trade.models import Category, Trade


@login_required
def index(request):
    categories = Category.objects.all()
    trade = Trade.objects.filter(owner=request.user)
    paginator = Paginator(trade, 10)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    context = {
        'trade': trade,
        'page_obj': page_obj,
    }
    return render(request, 'trade/index.html', context)


@login_required
def add_trade(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request, 'trade/add_trade.html', context)

    if request.method == 'POST':
        assets = request.POST['assets']

        if not assets:
            messages.error(request, 'Assets is required')
            return render(request, 'trade/add_trade.html', context)
        date = request.POST['date']
        category = request.POST['category']
        action = request.POST['action']
        status = request.POST['status']
        types = request.POST['types']
        risk = request.POST['risk']
        profit = request.POST['profit']
        balance = request.POST['balance']
        setup = request.POST['setup']

        if not balance:
            messages.error(request, 'Balance is required')
            return render(request, 'trade/add_trade.html', context)

        Trade.objects.create(owner=request.user, assets=assets, date=date,
                             action=action, status=status, types=types,
                             risk=risk, profit=profit, balance=balance, setup=setup, category=category)
        messages.success(request, 'Trade saved successfully')

        return redirect('trade')


def delete_trade(request, id):
    trade = Trade.objects.get(pk=id)
    trade.delete()
    messages.success(request, 'Trade removed')
    return redirect('trade')

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