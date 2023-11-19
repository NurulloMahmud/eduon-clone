from rest_framework.permissions import IsAuthenticated

from main.models import Course, Lesson, Transaction, Enrolled, MentorCourse
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.views import APIView
from main.serializer import CourseSerializer, CourseCommentSerializer, \
    CourseModulSerializer, CourseModulLessonSerializer, LessonCommentSerializer, \
    LessonStarSerializer, CourseStarSerializer, UploadWebinarSerializer, TransactionSerializer, EnrolledSerializer


class UploadCourseAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CourseSerializer

    def post(self, request):
        upload_serailize = CourseSerializer(data=request.data)
        if upload_serailize.is_valid(raise_exception=True):
            upload_serailize.save()
            return Response(data={"Success": True, "data": upload_serailize.data}, status=200)
        return Response(status=400)


class CourseCommentAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CourseCommentSerializer

    def get_object(self, pk):
        return Course.objects.get(pk=pk)

    def get(self, request, pk):
        comment = self.get_object(pk)
        comment_serializer = CourseSerializer(comment, many=True)
        return Response({'Course comment data': comment_serializer.data})

    def post(self, request, pk):
        course = self.get_object(pk)
        comment_data = request.data
        comment_data['course'] = course.id
        comment_serialiser = CourseCommentSerializer(data=comment_data)
        if comment_serialiser.is_valid(raise_exception=True):
            comment_serialiser.save()
            return Response(data={'Success': True, 'data': comment_serialiser.data}, status=200)
        return Response(status=400)


class CourseStarAPIView(GenericAPIView):
    permission_classes = ()
    serializer_class = CourseStarSerializer

    def get_object(self, pk):
        return Course.objects.get(pk=pk)

    def post(self, request, pk):
        course = self.get_object(pk)
        star_data = request.data
        star_data['course'] = course.id
        course_star_serializer = CourseStarSerializer(data=star_data)
        if course_star_serializer.is_valid(raise_exception=True):
            course_star_serializer.save()
            return Response({'Success': True, "data": course_star_serializer.data}, status=200)
        return Response(status=400)


class CourseModulAPIView(GenericAPIView):
    permission_classes = ()
    serializer_class = CourseModulSerializer

    def post(self, request):
        course_modul = CourseModulSerializer(data=request.data)
        if course_modul.is_valid(raise_exception=True):
            course_modul.save()
            return Response({'Success': True, 'data': course_modul.data}, status=200)
        return Response(status=400)


class CourseModulLessonAPIView(GenericAPIView):
    permission_classes = ()
    serializer_class = CourseModulLessonSerializer

    def post(self, request):
        modul_lesson_serializer = CourseModulLessonSerializer(data=request.data)
        if modul_lesson_serializer.is_valid(raise_exception=True):
            modul_lesson_serializer.save()
            return Response({'Success': True, 'data': modul_lesson_serializer.data}, status=200)
        return Response(status=400)


class LessonCommentAPIView(GenericAPIView):
    permission_classes = ()
    serializer_class = LessonCommentSerializer

    def get_object(self, pk):
        return Lesson.objects.get(pk=pk)

    def get(self, request, pk):
        lesson_comment = self.get_object(pk)
        lesson_comment_serializer = CourseSerializer(lesson_comment, many=True)
        return Response({'Lesson comment data': lesson_comment_serializer.data})

    def post(self, request, pk):
        lesson_comment = self.get_object(pk)
        lesson_data = request.data
        lesson_data['lesson'] = lesson_comment.id
        lesson_comment_serializer = LessonCommentSerializer(data=lesson_data)
        if lesson_comment_serializer.is_valid(raise_exception=True):
            lesson_comment_serializer.save()
            return Response({'Success': True, 'data': lesson_comment_serializer.data}, status=200)
        return Response(status=400)


class LessonStarAPIView(GenericAPIView):
    permission_classes = ()
    serializer_class = LessonStarSerializer

    def get_object(self, pk):
        return Lesson.objects.get(pk=pk)

    def get(self, request, pk):
        lesson_star = self.get_object(pk)
        lesson_star_serializer = LessonStarSerializer(lesson_star, many=True)
        return Response({'Lesson star data': lesson_star_serializer.data})

    def post(self, request, pk):
        lesson_star = self.get_object(pk)
        lesson_star_data = request.data
        lesson_star_data['lesson'] = lesson_star.id
        lesson_star_serializer = LessonStarSerializer(data=lesson_star_data)
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
            user = MentorCourse.objects.filter(course=course).values('user')
            if request.user == user:
                data = CourseSerializer(course, data=request.data)
                data.is_valid(raise_exception=True)
                data.save()
        except Exception as e:
            return Response({'Success': False, 'message': e}, status=400)
        return Response({'Success': True})

    def patch(self, request, pk):
        try:
            course = self.get_object(pk)
            user = MentorCourse.objects.filter(course=course).values('user')
            if request.user == user:
                data = CourseSerializer(course, data=request.data, partial=True)
                data.is_valid(raise_exception=True)
                data.save()
        except Exception as e:
            return Response({'Success': False, 'message': e}, status=400)
        return Response({'Success': True})

    def delete(self, request, pk):
        course = self.get_object(pk)
        user = MentorCourse.objects.filter(course=course).values('user')
        if request.user == user:
            course.delete()
            return Response({'Success': True})


class CourseCountAPIView(GenericAPIView):
    permission_classes = ()
    serializer_class = ''

    def get(self, request):
        count_couse = MentorCourse.objects.filter(user=request.user).count()
        return Response({'Spekir course count': count_couse})


class RegisterCount(APIView):
    pass


class UploadWebinarAPIView(CreateAPIView):
    permission_classes = ()
    serializer_class = UploadWebinarSerializer

    def post(self, request):
        webinar_serializer = UploadWebinarSerializer(data=request.data)
        if webinar_serializer.is_valid(raise_exception=True):
            webinar_serializer.save()
            return Response({'Success': True, 'message': webinar_serializer.data}, status=200)
        return Response(status=400)


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
