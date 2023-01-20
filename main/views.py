from django.views.generic import TemplateView
from rest_framework.generics import CreateAPIView, RetrieveAPIView

from main.models import SomeString
from main.serializers import SomeStringSerializer


class SaveDataView(CreateAPIView):
    queryset = SomeString.objects.all()
    serializer_class = SomeStringSerializer


class GetDataView(RetrieveAPIView):
    queryset = SomeString.objects.last()
    serializer_class = SomeStringSerializer
    
    def get_object(self):
        return SomeString.objects.last()


class MainView(TemplateView):
    template_name = 'main/index.html'
