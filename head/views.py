from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView
from rest_framework.response import Response

from head.serializer import CartSerializer
from main.models import Course, Modul, Lesson, Webinar, Cart, CourseStar
from main.serializer import CourseSerializer, CourseModulSerializer, CourseModulLessonSerializer, \
    UploadWebinarSerializer, CourseStarSerializer


class CourseAPIView(GenericAPIView):
    permission_classes = ()
    serializer_class = CourseSerializer

    def get(self, request):
        course = Course.objects.all()
        course_serializer = CourseSerializer(course, many=True)
        return Response({'Course data': course_serializer.data})


class CourseModulAPIView(CreateAPIView):
    permission_classes = ()
    serializer_class = CourseModulSerializer

    def get(self, request):
        course_modul = Modul.objects.all()
        course_modul_serializer = CourseSerializer(course_modul, many=True)
        return Response({'Course modul data': course_modul_serializer.data})


class CourseModulLessonAPIView(CreateAPIView):
    permission_classes = ()
    serializer_class = CourseModulLessonSerializer

    def get(self, request):
        modul_lesson = Lesson.objects.all()
        modul_lesson_serializer = CourseSerializer(modul_lesson, many=True)
        return Response({'Modul lesson data': modul_lesson_serializer.data})


class UploadWebinarAPIView(CreateAPIView):
    permission_classes = ()
    serializer_class = UploadWebinarSerializer

    def get(self, request):
        webinar = Webinar.objects.all()
        webinar_serializer = UploadWebinarSerializer(webinar, many=True)
        return Response({'Webinar data': webinar_serializer.data})


class CartAPIView(CreateAPIView, ListAPIView):
    permission_classes = ()
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
    permission_classes = ()
    serializer_class = CourseStarSerializer

    def post(self, request):
        course_star_serializer = CourseStarSerializer(data=request.data)
        if course_star_serializer.is_valid(raise_exception=True):
            course_star_serializer.save()
            return Response({'Success': True, 'data': course_star_serializer.data}, status=201)
        return Response({'Success': False, 'message': 'Invalid data'}, status=400)

    def get(self, request):
        course_stars = CourseStar.objects.all()
        course_star_serializer = CourseStarSerializer(course_stars, many=True)
        return Response({'Course star rating': course_star_serializer.data})