from django.shortcuts import render

# Create your views here.


def get_todo_list(request):
    """
    This literally renders the request,
    linked to settings, urls and todo_list.html
    """
    return render(request, 'todo/todo_list.html')
