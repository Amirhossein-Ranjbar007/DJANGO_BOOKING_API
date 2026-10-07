from rest_framework.pagination import PageNumberPagination


class BookingPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 20
    page_query_param = 'page'
    page_size_query_param = 'page-size'
    last_page_strings = ('last',)



