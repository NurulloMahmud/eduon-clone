from django.urls import path
from .views import CartAPIView, CourseStarAPIViews, CourseCommentAPIView, CourseModulAPIView, CourseModulLessonAPIView, \
    UploadWebinarAPIView, LessonStarAPIView, LessonCommentAPIView

urlpatterns = [
    path('cart', CartAPIView.as_view(), name='cart'),
    path('coursestar/<int:pk>', CourseStarAPIViews.as_view(), name='course_star'),
    path('coursecomment/<int:pk>', CourseCommentAPIView.as_view(), name='course_comment'),
    path('coursemodul/<int:pk>', CourseModulAPIView.as_view(), name='course_modul'),
    path('coursemodullesson/<int:pk>', CourseModulLessonAPIView.as_view(), name='course_modul_lesson'),
    path('webinar', UploadWebinarAPIView.as_view(), name='wibenar'),
    path('lessoncomment/<int:pk>', LessonCommentAPIView.as_view(), name='lesson_comment'),
    path('lessonstar/<int:pk>', LessonStarAPIView.as_view(), name='lesson_star'),
]
