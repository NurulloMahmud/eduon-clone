from django.urls import path
from .views import UploadCourseAPIView, CourseCommentAPIView, CourseStarAPIView, CourseModulAPIView, \
    CourseModulLessonAPIView, LessonCommentAPIView

urlpatterns = [
    path('uploadcourse', UploadCourseAPIView.as_view(), name='upload_course'),
    path('commentcourse', CourseCommentAPIView.as_view(), name='comment_course'),
    path('coursestar', CourseStarAPIView.as_view(), name='course_star'),
    path('coursemodul', CourseModulAPIView.as_view(), name='course_modul'),
    path('coursemodullesson', CourseModulLessonAPIView.as_view(), name='course_modul_lesson'),
    path('lessoncomment', LessonCommentAPIView.as_view(), name='lesson_comment'),
]
