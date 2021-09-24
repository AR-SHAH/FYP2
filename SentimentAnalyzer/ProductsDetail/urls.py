from django.urls import path
from ProductsDetail import views

urlpatterns = [
    path('', views.listView.as_view())
]
