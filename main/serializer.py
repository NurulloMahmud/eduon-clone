from rest_framework.serializers import Serializer, ModelSerializer
from .models import Course, Language, SubCategory, Category, CourseComment, CourseStar, Modul, Lesson, LessonComment, \
    LessonStar, Webinar, Cart
from rest_framework import serializers


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


class CourseCommentSerializer(ModelSerializer):
    class Meta:
        model = CourseComment
        fields = '__all__'


class CourseStarSerializer(ModelSerializer):
    class Meta:
        model = CourseStar
        fields = '__all__'


class CourseModulSerializer(ModelSerializer):
    class Meta:
        model = Modul
        fields = '__all__'


class CourseModulLessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class LessonCommentSerializer(ModelSerializer):
    class Meta:
        model = LessonComment
        fields = '__all__'


class LessonStarSerializer(ModelSerializer):
    class Meta:
        model = LessonStar
        fields = '__all__'


class UploadWebinarSerializer(ModelSerializer):
    class Meta:
        model = Webinar
        fields = '__all__'


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'