from django.urls import path

from retail.apps import RetailConfig
from retail.views import MemberCreateAPIView, MemberListAPIView, \
    MemberUpdateAPIView, MemberDestroyAPIView, MemberRetrieveAPIView

app_name = RetailConfig.name

urlpatterns = [
    path('create/', MemberCreateAPIView.as_view()),
    path('list/', MemberListAPIView.as_view()),
    path('update/<int:pk>/', MemberUpdateAPIView.as_view()),
    path('delete/<int:pk>/', MemberDestroyAPIView.as_view()),
    path('<int:pk>/', MemberRetrieveAPIView.as_view()),

]