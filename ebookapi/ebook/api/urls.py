from django.urls import path
from ebook.api.views import EbookListAPIView,EbookDetailAPIView

urlpatterns = [
    path('ebook/',EbookListAPIView.as_view(),name='ebook-list'),
    path('ebook/<int:pk>/',EbookDetailAPIView.as_view(),name='ebook-detail')
]