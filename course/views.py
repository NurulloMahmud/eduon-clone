from rest_framework.permissions import IsAuthenticated

from main.models import (
    Course, Transaction, Enrolled, MentorCourse, LessonStar, LessonComment, CourseComment, \
    CourseStar, Webinar)
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.views import APIView

from main.permissions import CanAccessPurchasedContentPermission, CanModifyOwnCoursesPermission
from main.serializer import (
    CourseSerializer, CourseCommentForPostSerializer, \
    CourseModulSerializer, LessonCommentForPostSerializer, \
    LessonStarForPostSerializer, CourseStarForPostSerializer, UploadWebinarForPostSerializer,
    TransactionSerializer, EnrolledSerializer, \
    CourseModulLessonForPostSerializer, MentorCourseSerializer)


class UploadCourseAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CourseSerializer

    def post(self, request):
        upload_serailize = CourseSerializer(data=request.data)
        if upload_serailize.is_valid(raise_exception=True):
            upload_serailize.save()
            return Response(data={"Success": True, "data": upload_serailize.data}, status=200)
        return Response(status=400)


class CourseCommentView(CreateAPIView):
    queryset = CourseComment.objects.all()
    serializer_class = CourseCommentForPostSerializer
    permission_classes = (IsAuthenticated, CanAccessPurchasedContentPermission)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CourseStarAPIView(CreateAPIView):
    queryset = CourseStar.objects.all()
    serializer_class = CourseStarForPostSerializer
    permission_classes = (IsAuthenticated, CanAccessPurchasedContentPermission)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CourseModulAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CourseModulSerializer

    def post(self, request):
        course_modul = CourseModulSerializer(data=request.data)
        if course_modul.is_valid(raise_exception=True):
            course_modul.save()
            return Response({'Success': True, 'data': course_modul.data}, status=200)
        return Response(status=400)


class ModulLessonAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CourseModulLessonForPostSerializer

    def post(self, request):
        modul_lesson_serializer = CourseModulLessonForPostSerializer(data=request.data)
        modul_lesson_serializer.is_valid(raise_exception=True)
        modul_lesson_serializer.save()
        return Response({'Success': True, 'data': modul_lesson_serializer.data}, status=200)


class LessonCommentAPIView(CreateAPIView):
    queryset = LessonComment.objects.all()
    serializer_class = LessonCommentForPostSerializer
    permission_classes = (IsAuthenticated, CanAccessPurchasedContentPermission)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LessonStarAPIView(CreateAPIView):
    queryset = LessonStar.objects.all()
    serializer_class = LessonStarForPostSerializer
    permission_classes = (IsAuthenticated, CanAccessPurchasedContentPermission)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EditCourseAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated, CanModifyOwnCoursesPermission)
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

    def delete(self, request, pk):
        course = self.get_object(pk)
        course.delete()
        return Response({'Success': True})


class SpeakerUploadedCoursesAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MentorCourseSerializer

    def get(self, request):
        speaker_uploaded_courses = MentorCourse.objects.filter(user=request.user)
        response_data = {'Number of speaker uploaded courses': speaker_uploaded_courses.count()}

        serializer = self.serializer_class(speaker_uploaded_courses, many=True)
        response_data['Speaker Uploaded Courses'] = serializer.data

        return Response(response_data, status=200)


class RegisterCount(APIView):
    pass


class UploadWebinarAPIView(CreateAPIView):
    queryset = Webinar.objects.all()
    serializer_class = UploadWebinarForPostSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserBalanceAPIView(GenericAPIView):
    permission_classes = ()
    serializer_class = TransactionSerializer

    def get(self, request):
        balance = Transaction.objects.all()
        balance_serializer = TransactionSerializer(balance, many=True)
        return Response({'User transaction data': balance_serializer.data})


class EnrolledAPIView(GenericAPIView):
    permission_classes = ()
    serializer_class = ''

    def get(self, request):
        enrolled = Enrolled.objects.all()
        enrolled_serializer = EnrolledSerializer(enrolled, many=True)
        return Response({'Enrolled data': enrolled_serializer.data})
