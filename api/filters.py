from django_filters import rest_framework as filters
from .models import Title


class TitlesFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', looup_expr='contains')
    genre = filters.CharFilter(field_name='genre_slug')
    category = filters.CharFilter(field_name='category_slug')

    class Meta:
        model = Title
        fields = ('name', 'category', 'genre', 'year')
