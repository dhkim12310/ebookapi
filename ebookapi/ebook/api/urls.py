from django.urls import path
from ebook.api.views import (EbookListAPIView,
                             EbookDetailAPIView,
                             ReviewCreateAPIView,
                             ReviewDetailAPIView)

urlpatterns = [
    path('ebook/',EbookListAPIView.as_view(),name='ebook-list'),
    path('ebook/<int:pk>/',EbookDetailAPIView.as_view(),name='ebook-detail'),
    path('ebook/<int:ebook_pk>/review/',ReviewCreateAPIView.as_view(),name='ebook-review'),
    path('review/<int:pk>',ReviewDetailAPIView.as_view(),name='review-datail')
]