from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.
def blogs_home(request):
   blogs = Articles.objects.order_by('-date')
   return render(request, 'blogs/blogs_home.html', {'blogs': blogs})


class blogsDetailView(DetailView):
   model = Articles
   template_name = 'blogs/detail_view.html'
   context_object_name = 'article'


class blogsUpdateView(UpdateView):
   model = Articles
   template_name = 'blogs/create_blog.html'

   form_class = ArticlesForm


class blogsDeleteView(DeleteView):
   model = Articles
   success_url = '/blogs'
   template_name = 'blogs/delete_blog.html'


def create_blog(request):

   error = ''
   if request.method == 'POST':
      form = ArticlesForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect ('blogs_home')
      else:
         error = 'Форма неверно заполнена'

   form = ArticlesForm()

   data = {
      'form': form,
      'error': error
   }

   return render(request, 'blogs/create_blog.html', data)