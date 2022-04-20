from django.urls import path
from . import views

urlpatterns = [
    path('ddc-dashboard', views.DashboardView.as_view()),
    path('data-top-up', views.DataTopUp.as_view()),
    path('get-plan', views.GetPlanView.as_view()),
    path('delete-top-up-data', views.delete_user_top_up_data),
]