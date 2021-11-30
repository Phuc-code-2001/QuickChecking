from django.views.generic import ListView
from django.views.generic.detail import DetailView

class TaskListView(ListView):

    template_name = 'task/index.html'
    context_object_name = 'tasks'
    paginate_by = 6

    def get_queryset(self):
        q = self.request.GET.get('q') # Get search key
        if q:
            by_key  = self.request.user.task_set.filter(key__contains=q)
            by_name = self.request.user.task_set.filter(name__contains=q)
            return (by_key | by_name).distinct()
        else:
            return self.request.user.task_set.all().order_by('-date_of_created')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'YourTasks'
        context['task_active'] = 'active'
        return context

class TaskDetailView(DetailView):
    pass