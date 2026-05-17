from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size = 5 # no of item per page
    page_size_query_param = 'page_size' # page size from client
    max_page_size = 50  # max items a client can request
    
    def get_paginated_response(self, data):
        return Response({
            'total_items': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'next': self.get_next_link(),
            'prev': self.get_previous_link(),
            'results': data
        })