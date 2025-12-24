from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from .models import Todo


class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'todos/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        """Return all todos for the current user."""
        return Todo.objects.filter(user=self.request.user).order_by('-created_at')


@login_required
def add(request):
    title = request.POST['title']
    Todo.objects.create(title=title, user=request.user)
    return redirect('todos:index')


@login_required
def delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id, user=request.user)
    todo.delete()
    return redirect('todos:index')


@login_required
def update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id, user=request.user)
    isCompleted = request.POST.get('isCompleted', False)
    if isCompleted == 'on':
        isCompleted = True
    
    todo.isCompleted = isCompleted
    todo.save()
    return redirect('todos:index')