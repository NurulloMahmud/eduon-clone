from django.shortcuts import render
from rest_framework.views import APIView

from .models import Course, Category, SubCategory, CourseStar
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView


from .serializer import CategorySerializer, SubCategorySerializer, CourseSerializer, CourseCommentSerializer, \
    CourseModulSerializer, CourseModulLessonSerializer, LessonCommentSerializer, \
    LessonStarSerializer, CourseStarSerializer


class UploadCourseAPIView(APIView):
    permission_classes = ()

    def post(self, request):
        upload_serailized = CourseSerializer(data=request.data)
        if upload_serailized.is_valid(raise_exception=True):
            upload_serailized.save()
            return Response(data={"Success": True, "data": upload_serailized.data}, status=200)
        return Response(status=400)


class CourseCommentAPIView(APIView):
    permission_classes = ()

    def post(self, request):
        comment_serialiser = CourseCommentSerializer(data=request.data)
        if comment_serialiser.is_valid(raise_exception=True):
            comment_serialiser.save()
            return Response(data={'Success':True, 'data': comment_serialiser.data}, status=200)
        return Response(status=400)


class CourseStarAPIView(APIView):
    permission_classes = ()

    def post(self, request):
        course_star_serializer = CourseStarSerializer(data=request.data)
        if course_star_serializer.is_valid(raise_exception=True):
            return Response({'Success': True, "data": course_star_serializer.data}, status=200)
        return Response(status=400)


class CourseModulAPIView(APIView):
    permission_classes = ()

    def post(self, request):
        course_modul = CourseModulSerializer(data=request.data)
        if course_modul.is_valid(raise_exception=True):
            return Response({'Success': True, 'data': course_modul.data}, status=200)
        return Response(status=400)


class CourseModulLessonAPIView(APIView):
    permission_classes = ()

    def post(self, request):
        modul_lesson_serializer = CourseModulLessonSerializer(data=request.data)
        if modul_lesson_serializer.is_valid(raise_exception=True):
            return Response({'Success': True, 'data': modul_lesson_serializer.data}, status=200)
        return Response(status=400)


class LessonCommentAPIView(APIView):
    permission_classes = ()

    def post(self, request):
        lesson_comment_serializer = LessonCommentSerializer(data=request.data)
        if lesson_comment_serializer.is_valid(raise_exception=True):
            return Response({'Success': True, 'data': lesson_comment_serializer.data}, status=200)
        return Response(status=400)


class LessonStarAPIView(APIView):
    permission_classes = ()

    def post(self, request):
        lesson_star_serializer = LessonStarSerializer(data=request.data)
        if lesson_star_serializer.is_valid(raise_exception=True):
            return Response({'Success': True, 'data': lesson_star_serializer.data}, status=200)
        return Response(status=400)

