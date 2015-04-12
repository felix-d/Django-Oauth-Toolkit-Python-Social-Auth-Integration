from beers.models import Beer
from beers.serializer import BeerSerializer
from rest_framework import generics, permissions


# List our beers and add beers
class BeerList(generics.ListCreateAPIView):
    serializer_class = BeerSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Beer.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# Get a beer and remove a beer
class BeerDetail(generics.RetrieveDestroyAPIView):
    serializer_class = BeerSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Beer.objects.filter(owner=user)
