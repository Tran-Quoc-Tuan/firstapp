from django.http import HttpResponse, JsonResponse
from .models import Chaper, Category, Story
from rest_framework import generics
from .serializers import CategorySerializer, StorySerializer, ChaperSerializer


# def list_truyen(request):
#     truyen = Story.objects.all()
#     page = Paginator(truyen, 20)
#     pageNumber = request.GET.get('page')
#     try:
#         customers = page.page(pageNumber)
#     except PageNotAnInteger:
#         customers = page.page(1)
#     except EmptyPage:
#         customers = page.page(page.num_pages)
#     return render(request, 'crawler_story/truyen.html', {'truyen': customers})


class Index(generics.ListAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class StoryDetail(generics.RetrieveAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class ListCategories(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoriesDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ListChap(generics.ListAPIView):
    queryset = Chaper.objects.all()
    serializer_class = ChaperSerializer


class ChapDetail(generics.RetrieveAPIView):
    queryset = Chaper.objects.all()
    serializer_class = ChaperSerializer
