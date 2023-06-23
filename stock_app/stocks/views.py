from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import StockForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Stock

@login_required
def add_stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.user = request.user
            stock.save()
            return redirect('stock_list')
    else:
        form = StockForm()
    return render(request, 'stocks/add_stock.html', {'form': form})

@login_required
def stock_list(request):
    stocks = Stock.objects.filter(user=request.user)
    return render(request, 'stocks/stock_list.html', {'stocks': stocks})
