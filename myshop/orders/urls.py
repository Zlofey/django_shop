from django.conf.urls import url, include
from django.urls import path
from . import views
from django.contrib.auth.urls import path

app_name = 'orders'

urlpatterns = [
    path('create/', views.OrderCreate, name='OrderCreate'),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('admin/order/<order_id>', views.AdminOrderDetail, name='AdminOrderDetail'),
    url(r'^admin/order/(?P<order_id>\d+)/$', views.AdminOrderDetail, name='AdminOrderDetail'),
    url(r'^admin/order/(?P<order_id>\d+)/pdf/$', views.AdminOrderPDF, name='AdminOrderPDF'),

]