from django.urls import reverse_lazy
from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import News
from .models import Category
from .filters import NewsFilter, CategoryFilter
from .forms import NewsForm
from .forms import UserForm
from .forms import SubscribeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

class NewsList(ListView):
    model = News
    ordering = '-data'
    queryset = News.objects.order_by('data')
    template_name = 'news_portal.html'
    context_object_name = 'news_portal'
    paginate_by = 10


    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filterset'] = self.filterset
        return context


class NewsDetail(DetailView):
    model = News
    template_name = 'post.html'
    context_object_name = 'post'


class SearchList(ListView):
    model = News
    ordering = 'name'
    template_name = 'search.html'
    context_object_name = 'search.qs'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filterset'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        return context



class NewsCreate(CreateView, PermissionRequiredMixin):
    form_class = NewsForm
    model = News
    template_name = 'news_edit.html'
    permission_required = ('info.add_news')



class NewsUpdate(UpdateView, PermissionRequiredMixin):
    form_class = NewsForm
    model = News
    template_name = 'news_edit.html'
    permission_required = ('info.change_news')


class NewsDelete(DeleteView, PermissionRequiredMixin):
    model = News
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')
    permission_required = ('info.delete_news')


class UserUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'user_update.html'
    form_class = UserForm
    success_url = reverse_lazy('news_list')



    def get_object(self, **kwargs):
        return self.request.user


class CategoryList(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'category'
    queryset = Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

@login_required
def subscribe_category(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    if request.user not in category.subscribers.all():
        category.subscribers.add(user)
    return redirect('/news_portal/category/')

@login_required
def unsubscribe_category(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    if request.user in category.subscribers.all():
        category.subscribers.remove(user)
    return redirect('/news_portal/category/')




