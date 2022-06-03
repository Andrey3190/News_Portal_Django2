import django.forms
from django_filters import FilterSet, ModelChoiceFilter, DateFilter
from .models import News, Category

class NewsFilter(FilterSet):

    category = ModelChoiceFilter(
        field_name = 'category',
        queryset= Category.objects.all(),
        label = 'Category',
        empty_label = 'Все категории',
    )

    data = DateFilter(
        lookup_expr='gt',
        widget=django.forms.DateInput(
            attrs={
                'type': 'date'
            }
        )
    )

    class Meta:
        model = News
        fields = {
            'category':['exact'],
            'name':['icontains'],
            'description':['icontains'],
        }