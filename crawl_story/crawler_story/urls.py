from django.urls import path
from .views import Index, StoryDetail, CategoriesDetail, ListCategories, ListChap, ChapDetail


urlpatterns = [
    path('', Index.as_view()),
    path('<int:pk>/', StoryDetail.as_view(), name='story-detail'),
    path('category/', ListCategories.as_view(), name='category'),
    path('category/<int:pk>/', CategoriesDetail.as_view(), name='Category'),
    path('chaper/', ListChap.as_view(), name='Chap'),
    path('chaper/<int:pk>/', ChapDetail.as_view(), name='Chaper'),
]
