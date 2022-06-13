from django.urls import path
from .views import (NewsList, NewsDetail, SearchList,
                    NewsCreate, NewsUpdate, NewsDelete, UserUpdate, CategoryList, subscribe_category, unsubscribe_category)

urlpatterns = [
    path("", NewsList.as_view(), name='news_list'),
    path('<int:pk>', NewsDetail.as_view(), name='news_detail'),
    path('search/', SearchList.as_view(), name='news_search'),
    path('create/', NewsCreate.as_view(), name='news_create'),
    path('<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('protected/', UserUpdate.as_view(), name='protected_update'),
    path('category/', CategoryList.as_view(), name='subscribes'),
    path('category/<int:pk>/subscribes/', subscribe_category, name='subscribes'),
    path('category/<int:pk>/unsubscribes/', unsubscribe_category, name='unsubscribes'),

]