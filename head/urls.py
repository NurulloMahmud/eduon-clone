from django.urls import path
from django_filters.views import FilterView
from .views import CartAPIView, CourseStarAPIViews, CourseFilterAPIView

urlpatterns = [
    path('cart', CartAPIView.as_view(), name='cart'),
    path('coursestar', CourseStarAPIViews.as_view(), name='course_star'),
    path('filter', CourseFilterAPIView.as_view(), name='filter'),
]

