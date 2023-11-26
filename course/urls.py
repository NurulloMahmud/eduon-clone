from django.urls import path
from .views import UploadCourseAPIView, CourseCommentView, CourseStarAPIView, CourseModulAPIView, \
    ModulLessonAPIView, LessonCommentAPIView, LessonStarAPIView, EditCourseAPIView, SpeakerUploadedCoursesAPIView, \
    UploadWebinarAPIView, UserBalanceAPIView, EnrolledAPIView

urlpatterns = [
    path('course', UploadCourseAPIView.as_view(), name='course'),
    path('course-comment', CourseCommentView.as_view(), name='course_comment'),
    path('course-star', CourseStarAPIView.as_view(), name='course_star'),
    path('course-modul', CourseModulAPIView.as_view(), name='course_modul'),
    path('modul-lesson', ModulLessonAPIView.as_view(), name='modul_lesson'),
    path('lesson-comment', LessonCommentAPIView.as_view(), name='lesson_comment'),
    path('lesson-star', LessonStarAPIView.as_view(), name='lesson_star'),
    path('edit-course/<int:pk>', EditCourseAPIView.as_view(), name='edit_course'),
    path('speaker-courses', SpeakerUploadedCoursesAPIView.as_view(), name='speaker-courses'),
    path('upload-webinar', UploadWebinarAPIView.as_view(), name='upload_webinar'),
    path('user-transaction', UserBalanceAPIView.as_view(), name='user_transaction'),
    path('enrolled', EnrolledAPIView.as_view(), name='enrolled'),
]
