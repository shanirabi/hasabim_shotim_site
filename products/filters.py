import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(lookup_expr='iexact')
    # title = django_filters.CharFilter('title','icontains',label='שם היין')


    CHOICES = (
        ('ascending', 'מהנמוך לגבוה'),
        ('descending', 'מהגבוה לנמוך'),

    )

    TYPE_CHOICES = (
        ('wine', 'יין'),
        ('beer', 'בירה'),
        ('alcohol', 'אלכוהול'),
        ('other', 'אחר'),

    )
    ordering_price = django_filters.ChoiceFilter(label=" סדר לפי מחיר ", choices=CHOICES, method='order_by_price')
    type = django_filters.ChoiceFilter(label="סוג מוצר", choices=TYPE_CHOICES)

    class Meta:
        model = Product
        fields = {
            # 'title': ['icontains'],
            # 'price': ['icontains'],
        }

    def order_by_price(self, queryset, name, value):
        expression = 'price' if value == 'ascending' else '-price'
        return queryset.order_by(expression)
