from django.urls import path
from .views import AddCartAPIView, CourseStarAPIViews, CourseCommentAPIView, CourseModulAPIView, ModulLessonAPIView, \
    UploadWebinarAPIView, LessonStarAPIView, LessonCommentAPIView, CourseAPIView, GetCartAPIView, CourseSearch, \
    CourseFilterAPIView

urlpatterns = [
    path('cart', AddCartAPIView.as_view(), name='add_cart'),
    path('cart-list', GetCartAPIView.as_view(), name='cart_list'),
    path('course-star/<int:pk>', CourseStarAPIViews.as_view(), name='course_star'),
    path('course-comment/<int:pk>', CourseCommentAPIView.as_view(), name='course_comment'),
    path('course-modul/<int:pk>', CourseModulAPIView.as_view(), name='course_modul'),
    path('modul-lesson/<int:pk>', ModulLessonAPIView.as_view(), name='modul_lesson'),
    path('webinar', UploadWebinarAPIView.as_view(), name='webinar'),
    path('lesson-comment/<int:pk>', LessonCommentAPIView.as_view(), name='lesson_comment'),
    path('lesson-star/<int:pk>', LessonStarAPIView.as_view(), name='lesson_star'),
    path('course-list', CourseAPIView.as_view(), name='course_list'),
    path('search', CourseSearch.as_view(), name='search'),
    path('filter/<int:deg>', CourseFilterAPIView.as_view(), name='filter'),
]
