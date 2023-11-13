from django.urls import path
from .views import CourseAPIView, CourseCommentAPIView, CourseStarAPIView, CourseModulAPIView, \
    CourseModulLessonAPIView, LessonCommentAPIView, LessonStarAPIView, EditCourseAPIView, CourseCountAPIView, \
    UploadWebinarAPIView, UserBalanceAPIView, EnrolledAPIView

urlpatterns = [
    path('uploadcourse', CourseAPIView.as_view(), name='upload_course'),
    path('commentcourse', CourseCommentAPIView.as_view(), name='comment_course'),
    path('coursestar', CourseStarAPIView.as_view(), name='course_star'),
    path('coursemodul', CourseModulAPIView.as_view(), name='course_modul'),
    path('coursemodullesson', CourseModulLessonAPIView.as_view(), name='course_modul_lesson'),
    path('lessoncomment', LessonCommentAPIView.as_view(), name='lesson_comment'),
    path('lessonstar', LessonStarAPIView.as_view(), name='lesson_star'),
    path('editcourse/<int:pk>', EditCourseAPIView.as_view(), name='edit_course'),
    path('usercoursecount', CourseCountAPIView.as_view(), name='user_course_count'),
    path('uploadwebinar', UploadWebinarAPIView.as_view(), name='upload_webinar'),
    path('usertransaction', UserBalanceAPIView.as_view(), name='user_transaction'),
    path('enrolled', EnrolledAPIView.as_view(), name='enrolled'),
]
