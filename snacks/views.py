from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from .models import Snack
from .serializers import SnackSerializer

# Create your views here.
class SnackList(ListAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer

class SnackDetail(RetrieveUpdateDestroyAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer

