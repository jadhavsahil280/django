from django.shortcuts import render
from .models import products
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    product_object = products.objects.all()

    #search product code
    query = request.GET.get('search')
    if query != '' and query is not None :
        product_object = product_object.filter(title__icontains = query )


    #paginator code
    paginator = Paginator(product_object, 4)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)

    return render(request, 'shop/index.html', {'product_object':product_object})


def product_details(request, id):
    product_object = products.objects.get(id=id)
    return render(request, 'shop/details.html', {'product_object':product_object})