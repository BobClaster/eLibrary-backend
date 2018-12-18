from django.urls import path
from .views import UserProfileView, ListUserProfileView

urlpatterns = [
    path('', ListUserProfileView.as_view(), name='list_user_profile'),
    path('<slug:student_id>/', UserProfileView.as_view(), name='user_profile'),
]
