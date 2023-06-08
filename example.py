from rest_framework.viewsets import GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend

class ViewSet(GenericViewSet):
    filter_backends = (DjangoFilterBackend,)
