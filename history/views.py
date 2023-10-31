from typing import Any
from .models import Trade
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class TradeListView(ListView):
    model = Trade
    template_name = 'history/trade_list.html'
    context_object_name = "trades"

    ordering = ['-created_at']
    paginate_by = 10

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Trade.objects.filter(user=self.request.user).order_by('-created_at')
        else:
            return Trade.objects.none()



#    def get_queryset(self):
        queryset = Trade.objects.filter(user=self.request.user)

        trade_result = self.request.GET.get('trade_result')

        if trade_result is None:
            queryset = queryset.all()
        else:
            queryset = queryset.filter(trade_result=trade_result)

        return queryset.order_by('-created_at')
    

class TradeDetailView(DetailView):
    model = Trade
    template_name = 'history/trade_detail.html'

class TradeCreateView(LoginRequiredMixin, CreateView):
    model = Trade
    template_name = 'history/trade_create.html'
    fields = ['chart_day', 'chart_hour', 'chart_close', 'trade_type', 'entry_price', 'stop', 'tp_1', 'tp_2', 'profit_or_loss', 'trade_result', 'explanation']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)