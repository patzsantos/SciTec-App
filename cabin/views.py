"""What can be viewed when lead to the Cabin Administration Page"""

from rest_framework import generics

from cabin.models import Range, Environment
from .serializers import RangeSerializer, EnvironmentSerializer


# 'range/' leads to the 'Cabin Administration' page when superuser is logged in
class EnvironmentList(generics.ListCreateAPIView):
    serializer_class = EnvironmentSerializer

    def get_queryset(self):
        queryset = Environment.objects.all()
        position = self.request.query_params.get('range')
        if position is not None:
            queryset = queryset.filter(Range=Environment)
        return queryset


# ISS cabin environment parameter details and history can be viewed here
class EnvironmentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EnvironmentSerializer
    queryset = Environment.objects.all()


class RangeList(generics.ListCreateAPIView):
    serializer_class = RangeSerializer
    queryset = Range.objects.all()


class RangeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RangeSerializer
    queryset = Range.objects.all()