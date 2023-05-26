from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100
    page_query_param = 'page'

    def get_page_number(self, request, paginator):
        page_number = request.data.get(self.page_query_param, 1)
        if page_number in self.last_page_strings:
            page_number = paginator.num_pages
        return page_number

    def get_page_size(self, request):
        page_size = request.data.get(self.page_size_query_param, self.page_size)
        if page_size > 0:
            return page_size

        return self.page_size