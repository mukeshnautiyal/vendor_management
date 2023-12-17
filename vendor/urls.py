from django.urls import path
#importing tokens 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from vendor.views.vendor import *
from vendor.views.user_signin import LoginView
from vendor.views.purchase_order import *
from vendor.views.performance import *


urlpatterns = [
    path('signin', LoginView.as_view(), name='signin'),

    #Vendors URLs
    path('vendors/create/', CreateVendor.as_view(), name='create_vendor'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('vendors/list', VendorListView.as_view(), name='vendor_list'),
    path('vendors/details/<int:pk>/', DetailView.as_view(), name='vendor_detail'),
    path('vendors/update/<int:pk>/', UpdateView.as_view(), name='vendor_update'),
    path('vendors/delete/<int:pk>/', DeleteView.as_view(), name='vendor_delete'),
    #Performance
    path('vendors/<int:pk>/performance/', VendorPerformance.as_view(), name='user_performance'),

    #Purchase Order URLs
    path('purchase_orders/create/', CreatePurchaseOrders.as_view(), name="create_purchase_order"),
    path('purchase_orders/list', PurposeOrdersListView.as_view(), name='purchase_orders_list'),
    path('purchase_orders/details/<int:pk>/', PurchaseDetailsDetailView.as_view(), name='purchase_orders_detail'),
    path('purchase_orders/delete/<int:pk>/', DeletePurchaseOrder.as_view(), name='purchase_orders_delete'),
    path('purchase_orders/update/<int:pk>/', UpdatePurchaseOrderView.as_view(), name='purchase_orders_update'),
    path('purchase_orders/<int:pk>/acknowledge/', UpdateAcknowledgment.as_view(), name='order_acknowledge'),
]