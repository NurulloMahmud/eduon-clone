from django.urls import path
from .views import CartAPIView, CourseStarAPIViews

urlpatterns = [
    path('cart', CartAPIView.as_view(), name='cart'),
    path('coursestar', CourseStarAPIViews.as_view(), name='course_star'),
]