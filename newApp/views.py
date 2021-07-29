import datetime
import re

from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.http.response import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from django.views.generic.list import ListView

from newApp.forms import CRUDform
from newApp.models import CRUDfunctions, UserInfo


async def current_time(request):
    now = datetime.datetime.now()
    # now=""
    if now:
        html = "<html><body>It is now %s.</body></html>" % now
        return HttpResponse(html)
    else:
        # return HttpResponseNotFound('<h1>Page not found</h1>')
        raise PermissionDenied


def my_view(request):
    return HttpResponse(status=201)


def create_view(request):
    context = {}
    form = CRUDform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(list_view)
    context['form'] = form
    return render(request, "create_view.html", context)


def list_view(request):
    context = {}
    context['dataset'] = CRUDfunctions.objects.all()
    return render(request, 'list_view.html', context)


def detail_view(request, id):
    context = {}
    context['data'] = CRUDfunctions.objects.get(id=id)
    return render(request, 'detail_view.html', context)


def update_view(request, id):
    context = {}
    obj = get_object_or_404(CRUDfunctions, id=id)
    form = CRUDform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(detail_view, id=id)
    context['form'] = form
    return render(request, 'update_view.html', context)


def delete_view(request, id):
    context = {}
    obj = get_object_or_404(CRUDfunctions, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect(list_view)
    return render(request, 'delete_view.html', context)


class MyView(View):
    def get(self, request):
        context = {}
        context['dataset'] = CRUDfunctions.objects.all()
        return render(request, 'list_view.html', context)


class MyCreateView(CreateView):
    model=CRUDfunctions
    fields=['title','description']

class MyListView(ListView):
    model=CRUDfunctions

class MyDetailView(DetailView):
    model=CRUDfunctions

class MyUpdateView(UpdateView):
    model=CRUDfunctions
    fields=['title','description']
    success_url ="/c-list"

class MyDeleteView(DeleteView):
    model=CRUDfunctions
    success_url ="/c-list"
    # template_name='delete_view '

class MyFormView(FormView):
    form_class=CRUDform
    template_name='newApp/form_view.html'
    success_url='/list'

class MyFormVIew2(View):
    form_class=CRUDform
    initial = {'title': 'description'}
    template_name='get-post.html'
    def get(self, request, *args, **kwargs):
        form =self.form_class(initial=self.initial)
        return render(request,self.template_name,{'form':form})
    
    def post(self, request, *args, **kwargs):
        form =self.form_class(initial=self.initial)
        if form.is_valid():
            return HttpResponseRedirect('/list')
        return render(request,self.template_name,{'form':form})