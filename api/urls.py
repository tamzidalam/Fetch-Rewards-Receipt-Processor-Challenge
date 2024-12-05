from django.urls import path
from .views import home_page, get_points,get_points_by_id,process_reciepts

urlpatterns=[
    path('',home_page,name='home_page'),
    path('receipts/',get_points,name='get_points'),
    path('receipts/<uuid:id>/points', get_points_by_id, name='get_points_by_id'),
    path('receipts/process',process_reciepts,name='process_reciepts')

]