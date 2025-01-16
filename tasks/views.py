from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm

# Список задач
def task_list(request):
    filter_status = request.GET.get('status', 'all')

    if filter_status == 'completed':
        tasks = Task.objects.filter(completed=True)
    elif filter_status == 'not_completed':
        tasks = Task.objects.filter(completed=False)
    else:
        tasks = Task.objects.all()

    if request.method == 'POST':
        task_ids = request.POST.getlist('tasks')  # Получаем список выделенных задач
        Task.objects.filter(id__in=task_ids).delete()  # Удаляем выделенные задачи
        return redirect('task_list')

    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'filter_status': filter_status})


# Детальная информация о задаче
def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'tasks/task_detail.html', {'task': task})

# Создание задачи
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем задачу в базе данных
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

def toggle_task_status(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.completed = not task.completed  # Переключаем статус
    task.save()
    return redirect('task_list')  # Возвращаемся на список задач

# Удаление задачи
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()  # Удаляем задачу
    return redirect('task_list')  # Возвращаемся к списку задач

# Редактирование задачи
def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form, 'task': task})


