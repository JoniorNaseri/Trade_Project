from django.urls import path
from . import views

urlpatterns = [
    path('', views.TradeListView.as_view(), name = "trade_list"),
    path('trade/<pk>/', views.TradeDetailView.as_view(), name = "trade_detail"),
    path('trade-new/', views.TradeCreateView.as_view(), name = "trade_create")
]