from rest_framework.pagination import PageNumberPagination



class PaymentsListPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 15
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    last_page_strings = ('last', )

