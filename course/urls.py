from django.urls import path
from .views import UploadCourseAPIView, CourseCommentAPIView, CourseStarAPIView, CourseModulAPIView, \
    CourseModulLessonAPIView, LessonCommentAPIView, LessonStarAPIView, EditCourseAPIView, CourseCountAPIView, \
    UploadWebinarAPIView, UserBalanceAPIView, EnrolledAPIView

urlpatterns = [
    path('course', UploadCourseAPIView.as_view(), name='course'),
    path('commentcourse/<int:pk>', CourseCommentAPIView.as_view(), name='comment_course'),
    path('coursestar/<int:pk>', CourseStarAPIView.as_view(), name='course_star'),
    path('coursemodul', CourseModulAPIView.as_view(), name='course_modul'),
    path('coursemodullesson', CourseModulLessonAPIView.as_view(), name='course_modul_lesson'),
    path('lessoncomment/<int:pk>', LessonCommentAPIView.as_view(), name='lesson_comment'),
    path('lessonstar/<int:pk>', LessonStarAPIView.as_view(), name='lesson_star'),
    path('editcourse/<int:pk>', EditCourseAPIView.as_view(), name='edit_course'),
    path('usercoursecount', CourseCountAPIView.as_view(), name='user_course_count'),
    path('uploadwebinar', UploadWebinarAPIView.as_view(), name='upload_webinar'),
    path('usertransaction', UserBalanceAPIView.as_view(), name='user_transaction'),
    path('enrolled', EnrolledAPIView.as_view(), name='enrolled'),
]
