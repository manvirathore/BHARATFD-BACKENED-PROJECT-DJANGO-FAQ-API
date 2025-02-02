from rest_framework import generics
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer

class FAQListView(generics.ListAPIView):
    serializer_class = FAQSerializer

    def get_queryset(self):
        lang = self.request.GET.get('lang', 'en')  # Get language from query param
        return FAQ.objects.filter(language=lang)  # Make sure your model has a `language` field

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serialized_data = self.get_serializer(queryset, many=True)
        return Response(serialized_data.data)
