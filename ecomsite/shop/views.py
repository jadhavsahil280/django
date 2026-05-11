from django.shortcuts import redirect, render
from .models import products, orders
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

def checkout(request):

    if request.method == "POST":
        item = request.POST.get('items')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')

        order = orders(item=item, name=name, email=email, phone=phone, address=address, city=city, state=state, zip=zip)
        order.save()

        
    return render(request, 'shop/checkout.html')

def orderReceived(request):
    return render(request, 'shop/order-received.html')