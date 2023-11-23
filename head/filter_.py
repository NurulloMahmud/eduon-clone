from django_filters import rest_framework as filters

from main.models import Course


class CourseFilter(filters.FilterSet):
    first_ = filters.CharFilter(field_name='title', lookup_expr='gte')
    last_ = filters.CharFilter(field_name='title', lookup_expr='lte')

    class Meta:
        model = Course
        fields = ('title', 'description')