from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.OrderCreate, name='OrderCreate'),
    #path('admin/order/<order_id>', views.AdminOrderDetail, name='AdminOrderDetail'),
    url(r'^admin/order/(?P<order_id>\d+)/$', views.AdminOrderDetail, name='AdminOrderDetail'),
    url(r'^admin/order/(?P<order_id>\d+)/pdf/$', views.AdminOrderPDF, name='AdminOrderPDF')
]