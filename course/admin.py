from django.contrib import admin
from main.models import *

# Register your models here.
admin.site.register((Course, CourseComment, CourseStar, Lesson, LessonComment, LessonStar, Level, Modul,
                     MentorCourse, Category, Transaction, TransactionCourse, Enrolled, SubCategory, Language))
