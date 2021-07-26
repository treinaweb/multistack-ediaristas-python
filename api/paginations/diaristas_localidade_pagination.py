from django.core import paginator
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class DiaristasLocalidadePagination(PageNumberPagination):
    page_size = 2

    def get_paginated_response(self, data):
        return Response({
            'quantidade_diaristas': (self.page.paginator.count - self.page_size)
            if self.page.paginator.count > self.page_size else 0,
            'diaristas': data
        })