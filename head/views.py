from django.db.models import Count
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.filters import SearchFilter

from main.models import Course, Modul, Lesson, Webinar, Cart, CourseStar, CourseComment, LessonStar, LessonComment, User
from main.permissions import CanModifyOwnCoursesPermission, CanAccessPurchasedContentPermission
from main.serializer import CourseSerializer, CourseModulSerializer, \
    UploadWebinarForGetSerializer, CourseStarForGetSerializer, CartForGetSerializer, CourseCommentForGetSerializer, \
    LessonStarForGetSerializer, \
    LessonCommentForGetSerializer, CourseModulLessonForGetSerializer, CartForPostSerializer


class CourseAPIView(GenericAPIView):
    permission_classes = ()
    serializer_class = CourseSerializer

    def get(self, request):
        course = Course.objects.all()
        course_serializer = CourseSerializer(course, many=True)
        return Response({'Course data': course_serializer.data})


class CourseCommentAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated, CanAccessPurchasedContentPermission)
    serializer_class = CourseCommentForGetSerializer

    def get_course_comments(self, pk):
        return CourseComment.objects.filter(course_id=pk)

    def get(self, request, pk):
        course_comments = self.get_course_comments(pk)
        comment_serializer = CourseCommentForGetSerializer(course_comments, many=True)
        return Response({'Course comment data': comment_serializer.data})


class CourseModulAPIView(CreateAPIView):
    permission_classes = ()
    serializer_class = CourseModulSerializer

    def get_object(self, pk):
        return Modul.objects.filter(course_id=pk)

    def get(self, request, pk):
        course_modul = self.get_object(pk)
        course_modul_serializer = CourseModulSerializer(course_modul, many=True)
        return Response({'Course modul data': course_modul_serializer.data})


class ModulLessonAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated, CanAccessPurchasedContentPermission)
    serializer_class = CourseModulLessonForGetSerializer

    def get_object(self, pk):
        return Lesson.objects.filter(modul_id=pk)

    def get(self, request, pk):
        modul_lesson = self.get_object(pk)
        modul_lesson_serializer = CourseModulLessonForGetSerializer(modul_lesson, many=True)
        return Response({'Modul lesson data': modul_lesson_serializer.data})


class UploadWebinarAPIView(CreateAPIView):
    permission_classes = ()
    serializer_class = UploadWebinarForGetSerializer

    def get(self, request):
        webinar = Webinar.objects.all()
        webinar_serializer = UploadWebinarForGetSerializer(webinar, many=True)
        return Response({'Webinar data': webinar_serializer.data})


class AddCartAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CartForPostSerializer

    def post(self, request):
        user = request.user
        modul_lesson_serializer = CartForPostSerializer(data=request.data)
        if modul_lesson_serializer.is_valid(raise_exception=True):
            modul_lesson_serializer.save(user=user)
            return Response({'Success': True, 'data': modul_lesson_serializer.data}, status=200)
        return Response(status=400)


class GetCartAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CartForGetSerializer

    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user=user)

    def get(self, request, *args, **kwargs):
        carts = self.get_queryset()
        serializer = self.get_serializer(carts, many=True)
        return Response(serializer.data)


class CourseStarAPIViews(GenericAPIView):
    permission_classes = (IsAuthenticated, CanAccessPurchasedContentPermission)
    serializer_class = CourseStarForGetSerializer

    def get_queryset(self, pk):
        return CourseStar.objects.filter(course_id=pk)

    def get(self, request, pk):
        course_stars = self.get_queryset(pk)
        course_star_serializer = CourseStarForGetSerializer(course_stars, many=True)
        return Response({'Course star data': course_star_serializer.data})


class LessonStarAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated, CanAccessPurchasedContentPermission)
    serializer_class = LessonStarForGetSerializer

    def get_objects(self, pk):
        return LessonStar.objects.filter(lesson_id=pk)

    def get(self, request, pk):
        lesson_star = self.get_objects(pk)
        lesson_star_serializer = LessonStarForGetSerializer(lesson_star, many=True)
        return Response({'Lesson star data': lesson_star_serializer.data})


class LessonCommentAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated, CanAccessPurchasedContentPermission)
    serializer_class = LessonCommentForGetSerializer

    def get_object(self, pk):
        return LessonComment.objects.filter(lesson_id=pk)

    def get(self, request, pk):
        lesson_comments = self.get_object(pk)
        lesson_comment_serializer = LessonCommentForGetSerializer(lesson_comments, many=True)
        return Response({'Lesson comment data': lesson_comment_serializer.data})


class CourseSearch(ListAPIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = (SearchFilter,)
    search_fields = ['title']


class CourseFilterAPIView(GenericAPIView):
    permission_classes = ()
    serializer_class = CourseSerializer

    def get(self, request, deg):
        if deg == 0:
            course = Course.objects.all().order_by('price')
            course_serializer = CourseSerializer(course, many=True)
            return Response({'Course data': course_serializer.data})

        elif deg == 1:
            course = Course.objects.all().order_by('-price')
            course_serializer = CourseSerializer(course, many=True)
            return Response({'Course data': course_serializer.data})
        elif deg == 2:
            course = Course.objects.annotate(num_enrollments=Count('enrolled')).order_by('-num_enrollments')[:int(5)]
            course_serializer = CourseSerializer(course, many=True)
            return Response({'Course data': course_serializer.data})

        else:
            return Response({'Message': 'Invalid filter value'})
