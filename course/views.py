
from main.models import Course, Category, SubCategory, CourseStar
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView
from rest_framework.views import APIView
from main.serializer import CategorySerializer, SubCategorySerializer, CourseSerializer, CourseCommentSerializer, \
    CourseModulSerializer, CourseModulLessonSerializer, LessonCommentSerializer, \
    LessonStarSerializer, CourseStarSerializer


class UploadCourseAPIView(CreateAPIView):
    permission_classes = ()

    def post(self, request):
        upload_serailized = CourseSerializer(data=request.data)
        if upload_serailized.is_valid(raise_exception=True):
            upload_serailized.save()
            return Response(data={"Success": True, "data": upload_serailized.data}, status=200)
        return Response(status=400)


class CourseCommentAPIView(CreateAPIView):
    permission_classes = ()

    def post(self, request):
        comment_serialiser = CourseCommentSerializer(data=request.data)
        if comment_serialiser.is_valid(raise_exception=True):
            comment_serialiser.save()
            return Response(data={'Success': True, 'data': comment_serialiser.data}, status=200)
        return Response(status=400)


class CourseStarAPIView(CreateAPIView):
    permission_classes = ()

    def post(self, request):
        course_star_serializer = CourseStarSerializer(data=request.data)
        if course_star_serializer.is_valid(raise_exception=True):
            course_star_serializer.save()
            return Response({'Success': True, "data": course_star_serializer.data}, status=200)
        return Response(status=400)


class CourseModulAPIView(CreateAPIView):
    permission_classes = ()

    def post(self, request):
        course_modul = CourseModulSerializer(data=request.data)
        if course_modul.is_valid(raise_exception=True):
            course_modul.save()
            return Response({'Success': True, 'data': course_modul.data}, status=200)
        return Response(status=400)


class CourseModulLessonAPIView(CreateAPIView):
    permission_classes = ()

    def post(self, request):
        modul_lesson_serializer = CourseModulLessonSerializer(data=request.data)
        if modul_lesson_serializer.is_valid(raise_exception=True):
            modul_lesson_serializer.save()
            return Response({'Success': True, 'data': modul_lesson_serializer.data}, status=200)
        return Response(status=400)


class LessonCommentAPIView(CreateAPIView):
    permission_classes = ()

    def post(self, request):
        lesson_comment_serializer = LessonCommentSerializer(data=request.data)
        if lesson_comment_serializer.is_valid(raise_exception=True):
            lesson_comment_serializer.save()
            return Response({'Success': True, 'data': lesson_comment_serializer.data}, status=200)
        return Response(status=400)


class LessonStarAPIView(CreateAPIView):
    permission_classes = ()

    def post(self, request):
        lesson_star_serializer = LessonStarSerializer(data=request.data)
        if lesson_star_serializer.is_valid(raise_exception=True):
            lesson_star_serializer.save()
            return Response({'Success': True, 'data': lesson_star_serializer.data}, status=200)
        return Response(status=400)


class EditCourseAPIView(GenericAPIView):
    permission_classes = ()
    serializer_class = CourseSerializer

    def get_object(self, pk):
        return Course.objects.get(pk=pk)

    def put(self, request, pk):
        try:
            course = self.get_object(pk)
            data = CourseSerializer(course, data=request.data)
            data.is_valid(raise_exception=True)
            data.save()
        except Exception as e:
            return Response({'Success': False, 'message': e}, status=400)
        return Response({'Success': True})

    def patch(self, request, pk):
        try:
            course = self.get_object(pk)
            data = CourseSerializer(course, data=request.data, partial=True)
            data.is_valid(raise_exception=True)
            data.save()
        except Exception as e:
            return Response({'Success': False, 'message': e}, status=400)
        return Response({'Success': True})


class CourseCountAPIView(ListAPIView):
    permission_classes = ()

    def get(self, request):
        user_id = request.user.id
        if user_id:
            title = request.GET.get('title')
            course_count = Course.objects.filter(title=title).count()
            return Response({'Count': course_count})
        else:
            return Response({'Count': 0})


class RegisterCount(APIView):
    pass
