from rest_framework import permissions

class IsMentorPermission(permissions.BasePermission):
    message = "Sizda ruhsat yo'q."

    def has_permission(self, request, view):
        # Foydalanuvchi mentor bo'lsa ruhsat berish
        return request.user.is_mentor

class HasBoughtCoursePermission(permissions.BasePermission):
    message = "Siz kursni sotib o'lmagansiz."

    def has_permission(self, request, view):
        # Foydalanuvchi kursni sotib olishgan bo'lsa ruhsat berish
        return request.user.has_bought_course
