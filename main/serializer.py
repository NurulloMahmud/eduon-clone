import os
import tempfile

from datetime import timedelta
from rest_framework.serializers import ModelSerializer
from .models import Course, SubCategory, Category, CourseComment, CourseStar, Modul, Lesson, LessonComment, \
    LessonStar, Webinar, Transaction, TransactionCourse, Enrolled, Cart, MentorCourse
from rest_framework import serializers

from moviepy.editor import VideoFileClip


class SubCategorySerializer(ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseCommentForPostSerializer(ModelSerializer):
    class Meta:
        model = CourseComment
        fields = ('id', 'course', 'text', 'date')


class CourseCommentForGetSerializer(ModelSerializer):
    class Meta:
        model = CourseComment
        fields = '__all__'


class CourseStarForPostSerializer(ModelSerializer):
    class Meta:
        model = CourseStar
        fields = ('id','course', 'star')


class CourseStarForGetSerializer(ModelSerializer):
    class Meta:
        model = CourseStar
        fields = '__all__'


class CourseModulSerializer(ModelSerializer):
    class Meta:
        model = Modul
        fields = '__all__'


class CourseModulLessonForGetSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseModulLessonForPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

    def save(self, *args, **kwargs):
        try:
            # Faylning turini tekshirish
            video_file = self.validated_data['video_location'].file

            # Save the file temporarily
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(video_file.read())

            try:
                # Olingan video uzunligini hisoblash
                video_clip = VideoFileClip(temp_file.name)
                length = timedelta(seconds=int(video_clip.duration))
                print(f'Video length: {length}')
                self.validated_data['length'] = length
            finally:
                # Close the file before cleanup
                temp_file.close()

                # Clean up: Delete the temporary file
                os.unlink(temp_file.name)

        except Exception as e:
            # Xatoni qaytarish yoki qanday qilib uni qaytadan ishlab chiqishni hohlash
            print(f"Error calculating video duration: {e}")
            print('xatolik: video turi xato')

        return super().save(*args, **kwargs)


class LessonCommentForPostSerializer(ModelSerializer):
    class Meta:
        model = LessonComment
        fields = ('id', 'text', 'lesson', 'date')


class LessonCommentForGetSerializer(ModelSerializer):
    class Meta:
        model = LessonComment
        fields = '__all__'


class LessonStarForPostSerializer(ModelSerializer):
    class Meta:
        model = LessonStar
        fields = ('id', 'lesson', 'star')


class LessonStarForGetSerializer(ModelSerializer):
    class Meta:
        model = LessonStar
        fields = '__all__'


class UploadWebinarForPostSerializer(ModelSerializer):
    class Meta:
        model = Webinar
        fields = ('id', 'title', 'language', 'trailer', 'thumbnail', 'date', 'start_time', 'price', 'youtube', 'webinar_type', 'description')


class UploadWebinarForGetSerializer(ModelSerializer):
    class Meta:
        model = Webinar
        fields = '__all__'


class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class TransactionCourseSerializer(ModelSerializer):
    class Meta:
        model = TransactionCourse
        fields = '__all__'


class EnrolledSerializer(ModelSerializer):
    class Meta:
        model = Enrolled
        fields = '__all__'


class CartForPostSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'course',)


class CartForGetSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class MentorCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorCourse
        fields = '__all__'
