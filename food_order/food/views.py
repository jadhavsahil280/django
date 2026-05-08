from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Item
from .forms import ItemForm
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView


# Create your views here.

# def index(request):

#     item_list = Item.objects.all()

#     context = {
#         'item_list' : item_list,
#     }

#     return render(request, 'food/index.html', context)


class indexClassBaseView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'

class ItemDetailView(DetailView):
    model = Item
    template_name = "food/details.html"


# def detail(request, item_id):
#     item_details = Item.objects.get(pk = item_id)
#     context={
#         "item_details" : item_details
#     }
#     return render(request, 'food/details.html', context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/item_form.html', {'form':form})

class createItem(CreateView):
    model = Item
    form_class = ItemForm
    # fields = ['item_name', 'item_desc', 'item_image', 'item_price']
    template_name = 'food/item_form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)
    


def edit_item(request, item_id):
    item = Item.objects.get(pk = item_id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/item_form.html', {'form':form})

def delete_item(request, item_id):
    item = Item.objects.get(pk = item_id)

    if request.method == "POST":
        item.delete()
        return redirect('food:index')
    
