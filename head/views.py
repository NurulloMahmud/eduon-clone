from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from main.models import Course, Modul, Lesson, Webinar, Cart, CourseStar, CourseComment, LessonStar, LessonComment
from main.permissions import HasPurchasedCourse
from main.serializer import CourseSerializer, CourseModulSerializer, CourseModulLessonSerializer, \
    UploadWebinarSerializer, CourseStarSerializer, CartSerializer, CourseCommentSerializer, LessonStarSerializer, \
    LessonCommentSerializer


class CourseAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CourseSerializer

    def get(self, request):
        course = Course.objects.all()
        course_serializer = CourseSerializer(course, many=True)
        return Response({'Course data': course_serializer.data})


class CourseCommentAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = CourseCommentSerializer

    def get_course_comments(self, course_pk):
        return CourseComment.objects.filter(course_id=course_pk)

    def get(self, request, pk):
        course_comments = self.get_course_comments(pk)
        comment_serializer = CourseCommentSerializer(course_comments, many=True)
        return Response({'Course comment data': comment_serializer.data})


class CourseModulAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CourseModulSerializer

    def get_object(self, pk):
        return Modul.objects.filter(pk=pk)

    def get(self, request, pk):
        course_modul = self.get_object(pk)
        course_modul_serializer = CourseSerializer(course_modul, many=True)
        return Response({'Course modul data': course_modul_serializer.data})


class CourseModulLessonAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated, HasPurchasedCourse)
    serializer_class = CourseModulLessonSerializer

    def get_object(self, pk):
        return Lesson.objects.get(pk=pk)

    def get(self, request, pk):
        modul_lesson = self.get_object(pk)
        modul_lesson_serializer = CourseSerializer(modul_lesson, many=True)
        return Response({'Modul lesson data': modul_lesson_serializer.data})


class UploadWebinarAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated, HasPurchasedCourse)
    serializer_class = UploadWebinarSerializer

    def get(self, request):
        webinar = Webinar.objects.all()
        webinar_serializer = UploadWebinarSerializer(webinar, many=True)
        return Response({'Webinar data': webinar_serializer.data})


class CartAPIView(CreateAPIView, ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CartSerializer

    def post(self, request):

        user = request.user
        course_id = request.data.get('course_id')

        try:
            course = Course.objects.get(pk=course_id)
        except Course.DoesNotExist:
            return Response({'Error': 'Course not found'}, status=404)

        cart_entry, created = Cart.objects.get_or_create(user=user, defaults={'user': user})
        cart_entry.courses.add(course)
        cart_entry.save()

        return Response({'Success': True, 'message': 'Course added to the cart'}, status=201)

    def get(self, request):

        user = request.user
        try:
            cart_entry = Cart.objects.get(user=user)
            cart_serializer = CartSerializer(cart_entry)
            return Response(cart_serializer.data)
        except Cart.DoesNotExist:
            return Response({'Error': 'Cart not found'}, status=404)


class CourseStarAPIViews(CreateAPIView, ListAPIView):
    permission_classes = (IsAuthenticated, HasPurchasedCourse)
    serializer_class = CourseStarSerializer

    def get_object(self, pk):
        return CourseStar.objects.get(pk=pk)

    def get(self, request, pk):
        course_stars = self.get_object(pk)
        course_star_serializer = CourseStarSerializer(course_stars)
        return Response({'Course star rating': course_star_serializer.data})


class LessonStarAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated, HasPurchasedCourse)
    serializer_class = LessonStarSerializer

    def get_object(self, pk):
        return LessonStar.objects.get(pk=pk)

    def get(self, request, pk):
        lesson_star = self.get_object(pk)
        lesson_star_serializer = LessonStarSerializer(lesson_star)
        return Response({'Lesson star data': lesson_star_serializer.data})


class LessonCommentAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated, HasPurchasedCourse)
    serializer_class = LessonCommentSerializer

    def get_object(self, pk):
        return LessonComment.objects.filter(lesson_id=pk)

    def get(self, request, pk):
        lesson_comments = self.get_object(pk)
        lesson_comment_serializer = self.get_serializer(lesson_comments, many=True)
        return Response({'Lesson comment data': lesson_comment_serializer.data})
