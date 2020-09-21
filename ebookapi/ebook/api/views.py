from rest_framework import generics
from rest_framework import mixins

from ebook.models          import Ebook, Review
from ebook.api.serializers import EbookSerializer, ReviewSerializer

class EbookListAPIView(generics.ListCreateAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer

class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
