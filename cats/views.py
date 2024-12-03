from rest_framework import generics, mixins
from .models import SpyCat
from .serializers import SpyCatSerializer, SpyCatSalarySerializer


class SpyCatSalaryUpdateView(generics.UpdateAPIView):
    queryset = SpyCat.objects.all()
    serializer_class = SpyCatSalarySerializer
    partial = True

    def perform_update(self, serializer):
        serializer.save(salary=self.request.data.get("salary"))


class SpyCatListView(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    queryset = SpyCat.objects.all()
    serializer_class = SpyCatSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SpyCatDetailView(
    mixins.RetrieveModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView
):
    queryset = SpyCat.objects.all()
    serializer_class = SpyCatSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
