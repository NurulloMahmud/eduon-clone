from django.contrib import admin
from main.models import (Enrolled, Course, CourseComment, CourseStar, Lesson, LessonComment, LessonStar, Level, Language,
                         MentorCourse, Modul, Category, Transaction, TransactionCourse, SubCategory, Webinar)

# Register your models here.
admin.site.register((Course, CourseComment, CourseStar, Lesson, LessonComment, LessonStar, Level, Modul,
                     MentorCourse, Category, Transaction, TransactionCourse, Enrolled, SubCategory, Language, Webinar))
