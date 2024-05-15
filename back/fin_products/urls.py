from django.contrib import admin
from django.urls import path
from . import views

app_name = "fin_products"
urlpatterns = [
    path('financial_products/', views.financial_products),
    path('deposit_list/', views.deposit_list),
    path('deposit_list/<deposit_code>/', views.deposit_detail),
    path('deposit_list/<deposit_code>/Option_list/', views.depositOption_list),
    path('deposit_list/<deposit_code>/Option_list/<int:depositOption_pk>/', views.depositOption_detail),
    path('saving_list/', views.saving_list),
    path('saving_list/<saving_code>/', views.saving_detail),
    path('saving_list/<saving_code>/Option_list/', views.savingOption_list),
    path('saving_list/<saving_code>/Option_list/<int:savingOption_pk>/', views.savingOption_detail),
    path('loan_list/', views.loan_list),
    path('loan_list/<loan_code>/', views.loan_detail),
    path('loan_list/<loan_code>/Option_list/', views.loanOption_list),
    path('loan_list/<loan_code>/Option_list/<int:loanOption_pk>/', views.loanOption_detail),
    # path('deposit/6months/', views.get_deposits, {'save_trm': '6'}),
    # path('deposit/12months/', views.get_deposits, {'save_trm': '12'}),
    # path('deposit/24months/', views.get_deposits, {'save_trm': '24'}),
    # path('deposit/36months/', views.get_deposits, {'save_trm': '36'}),
    # path('saving/6months/', views.get_savings, {'save_trm': '6'}),
    # path('saving/12months/', views.get_savings, {'save_trm': '12'}),
    # path('saving/24months/', views.get_savings, {'save_trm': '24'}),
    # path('saving/36months/', views.get_savings, {'save_trm': '36'}),
    # path('deposit/-6months/', views.get_reverse_deposits, {'save_trm': '6'}),
    # path('deposit/-12months/', views.get_reverse_deposits, {'save_trm': '12'}),
    # path('deposit/-24months/', views.get_reverse_deposits, {'save_trm': '24'}),
    # path('deposit/-36months/', views.get_reverse_deposits, {'save_trm': '36'}),
    # path('saving/-6months/', views.get_reverse_savings, {'save_trm': '6'}),
    # path('saving/-12months/', views.get_reverse_savings, {'save_trm': '12'}),
    # path('saving/-24months/', views.get_reverse_savings, {'save_trm': '24'}),
    # path('saving/-36months/', views.get_reverse_savings, {'save_trm': '36'}),
]