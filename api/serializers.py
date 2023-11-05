from rest_framework import serializers
from django.contrib.auth import get_user_model
from main.models import (
    Language,
    Level,
    UserAccount,
    Category,
    SubCategory,
    Course,
    CourseComment,
    CourseStar,
    MentorCourse,
    Modul,
    Lesson,
    LessonComment,
    LessonStar,
    Transaction,
    TransactionCourse,
    Enrolled,
    Cart,
)

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class MainCategorySerializer(serializers.ModelSerializer):
    parent = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    def get_parent(self, obj):
        if obj.parent:
            return obj.parent.name
        return None


class SubCategorySerializer(serializers.ModelSerializer):
    head_category = MainCategorySerializer(many=True, read_only=True)

    class Meta:
        model = SubCategory
        fields = '__all__'


