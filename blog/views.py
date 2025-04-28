from .models import Blog
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse


class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'content', 'preview', 'publication_sign']
    context_object_name = 'blog'
    success_url = reverse_lazy('blog:blog_list')


class BlogListView(ListView):
    model = Blog
    context_object_name = 'blogs'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(publication_sign=True)


class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['content', 'publication_sign', 'title', 'preview']

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')
