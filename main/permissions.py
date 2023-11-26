from rest_framework.permissions import BasePermission

from main.models import MentorCourse, Enrolled


class CanModifyOwnCoursesPermission(BasePermission):
    message = "You don't have permission to modify this course."

    def has_object_permission(self, request, view, obj):
        # Foydalanuvchi kursni o'zgartira olishi mumkinmi?
        user = request.user
        return MentorCourse.objects.filter(user=user, course=obj).exists()


class CanAccessPurchasedContentPermission(BasePermission):
    message = "You don't have permission to access this content."

    def has_object_permission(self, request, view, obj):
        # Foydalanuvchi kursni sotib oldimi?
        user = request.user
        course_id = obj.course.id
        return Enrolled.objects.filter(user=user, course_id=course_id).exists()
