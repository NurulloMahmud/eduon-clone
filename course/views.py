from main.models import Course, Category, SubCategory, CourseStar, CourseComment, Modul, Lesson, LessonComment, \
    LessonStar, Webinar, Transaction, Enrolled
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView
from rest_framework.views import APIView
from main.serializer import CategorySerializer, SubCategorySerializer, CourseSerializer, CourseCommentSerializer, \
    CourseModulSerializer, CourseModulLessonSerializer, LessonCommentSerializer, \
    LessonStarSerializer, CourseStarSerializer, UploadWebinarSerializer, TransactionSerializer, EnrolledSerializer


class CourseAPIView(GenericAPIView):
    permission_classes = ()
    serializer_class = CourseSerializer

    def get(self, request):
        course = Course.objects.all()
        course_serializer = CourseSerializer(course, many=True)
        return Response({'Course data': course_serializer.data})

    def post(self, request):
        upload_serailize = CourseSerializer(data=request.data)
        if upload_serailize.is_valid(raise_exception=True):
            upload_serailize.save()
            return Response(data={"Success": True, "data": upload_serailize.data}, status=200)
        return Response(status=400)


class CourseCommentAPIView(CreateAPIView):
    permission_classes = ()
    serializer_class = CourseCommentSerializer

    def get(self, request):
        comment = CourseComment.objects.all()
        comment_serializer = CourseSerializer(comment, many=True)
        return Response({'Course comment data': comment_serializer.data})

    def post(self, request):
        comment_serialiser = CourseCommentSerializer(data=request.data)
        if comment_serialiser.is_valid(raise_exception=True):
            comment_serialiser.save()
            return Response(data={'Success': True, 'data': comment_serialiser.data}, status=200)
        return Response(status=400)


class CourseStarAPIView(CreateAPIView):
    permission_classes = ()
    serializer_class = CourseStarSerializer

    def get(self, request):
        course_star = CourseStar.objects.all()
        course_star_serializer = CourseSerializer(course_star, many=True)
        return Response({'Course star data': course_star_serializer.data})

    def post(self, request):
        course_star_serializer = CourseStarSerializer(data=request.data)
        if course_star_serializer.is_valid(raise_exception=True):
            course_star_serializer.save()
            return Response({'Success': True, "data": course_star_serializer.data}, status=200)
        return Response(status=400)


class CourseModulAPIView(CreateAPIView):
    permission_classes = ()
    serializer_class = CourseModulSerializer

    def get(self, request):
        course_modul = Modul.objects.all()
        course_modul_serializer = CourseSerializer(course_modul, many=True)
        return Response({'Course modul data': course_modul_serializer.data})

    def post(self, request):
        course_modul = CourseModulSerializer(data=request.data)
        if course_modul.is_valid(raise_exception=True):
            course_modul.save()
            return Response({'Success': True, 'data': course_modul.data}, status=200)
        return Response(status=400)


class CourseModulLessonAPIView(CreateAPIView):
    permission_classes = ()
    serializer_class = CourseModulLessonSerializer

    def get(self, request):
        modul_lesson = Lesson.objects.all()
        modul_lesson_serializer = CourseSerializer(modul_lesson, many=True)
        return Response({'Modul lesson data': modul_lesson_serializer.data})

    def post(self, request):
        modul_lesson_serializer = CourseModulLessonSerializer(data=request.data)
        if modul_lesson_serializer.is_valid(raise_exception=True):
            modul_lesson_serializer.save()
            return Response({'Success': True, 'data': modul_lesson_serializer.data}, status=200)
        return Response(status=400)


class LessonCommentAPIView(CreateAPIView):
    permission_classes = ()
    serializer_class = LessonCommentSerializer

    def get(self, request):
        lesson_comment = LessonComment.objects.all()
        lesson_comment_serializer = CourseSerializer(lesson_comment, many=True)
        return Response({'Lesson comment data': lesson_comment_serializer.data})

    def post(self, request):
        lesson_comment_serializer = LessonCommentSerializer(data=request.data)
        if lesson_comment_serializer.is_valid(raise_exception=True):
            lesson_comment_serializer.save()
            return Response({'Success': True, 'data': lesson_comment_serializer.data}, status=200)
        return Response(status=400)


class LessonStarAPIView(CreateAPIView):
    permission_classes = ()
    serializer_class = LessonStarSerializer

    def get(self, request):
        lesson_star = LessonStar.objects.all()
        lesson_star_serializer = LessonStarSerializer(lesson_star, many=True)
        return Response({'Lesson star data': lesson_star_serializer.data})

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

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response({'Success': True})


class CourseCountAPIView(GenericAPIView):
    permission_classes = ()
    serializer_class = ''

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


class UploadWebinarAPIView(CreateAPIView):
    permission_classes = ()
    serializer_class = UploadWebinarSerializer

    def get(self, request):
        webinar = Webinar.objects.all()
        webinar_serializer = UploadWebinarSerializer(webinar, many=True)
        return Response({'Webinar data': webinar_serializer.data})

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
