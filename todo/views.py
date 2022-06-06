from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm


# Create your views here.


def get_todo_list(request):
    """
    This literally renders the request,
    linked to settings, urls and todo_list.html
    """
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)

def add_item(request):
    """
    This literally renders the request,
    linked to settings, urls and todo_list.html
    """
    if request.method == "POST":
        name = request.POST.get('item_name')
        done = 'done' in request.POST
        Item.objects.create(name=name, done=done)

        return redirect('get_todo_list')
    form = itemForm()
    context = {
        'form' : form
    }
    return render(request, 'todo/add_item.html')