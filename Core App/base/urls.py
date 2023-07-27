from .import views
from django.urls import path

urlpatterns = [
    path('',views.StudentAPIView.as_view(),name='home'),
    path('student/<int:id>/',views.StudentAPIView.as_view(),name='home'),
]