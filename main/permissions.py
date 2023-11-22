from rest_framework.permissions import BasePermission

from main.models import MentorCourse


class HasPurchasedCourse(BasePermission):
    message = "You do not have permission to view this course content."

    def has_permission(self, request, view):
        course_id = view.kwargs.get('pk')

        if request.user and request.user.is_authenticated:
            return request.user.purchased_courses.filter(course_id=course_id).exists()

        return False


class IsCourseMentor(BasePermission):
    message = "You do not have permission to modify this course."

    def has_permission(self, request, view):
        course_id = view.kwargs.get('pk')

        if request.user and request.user.is_authenticated:
            return MentorCourse.objects.filter(user=request.user, course_id=course_id).exists()

        return False
