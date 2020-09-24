from rest_framework            import generics
from rest_framework            import permissions
from rest_framework.exceptions import ValidationError
from rest_framework.generics   import get_object_or_404

from ebook.models          import Ebook, Review
from ebook.api.pagination  import SmallSetPagination
from ebook.api.serializers import EbookSerializer, ReviewSerializer
from ebook.api.permissions import IsAdminUserOrReadOnly, IsReviewAuthorOrRedaOnly

class EbookListAPIView(generics.ListCreateAPIView):
    queryset = Ebook.objects.all().order_by("-id")
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = SmallSetPagination

class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class ReviewCreateAPIView(generics.CreateAPIView):
    querset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self,serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook = get_object_or_404(Ebook, pk=ebook_pk)
        review_author = self.request.user
        serializer.save(ebook=ebook,review_author=review_author)

class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrRedaOnly]