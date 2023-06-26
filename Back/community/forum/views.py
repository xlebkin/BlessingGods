from django.shortcuts import render,  redirect
from .models import Artiles
from .forms import ArtilesForm
from django.views.generic import DetailView, UpdateView, DeleteView
def home(request):
    news = Artiles.objects.order_by('-id')
    return render(request, 'forum/index.html', {'news': news})

def create(request):
    news = Artiles.objects.order_by('-id')
    error = ''
    if request.method == 'POST':
        form = ArtilesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/forum/')
        else:
            error = 'Форма была неверной'
    form = ArtilesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'forum/create.html', data)
class NewsDetailView(DetailView):
    model = Artiles
    template_name = 'forum/detail.html'
    context_object_name = 'article'
