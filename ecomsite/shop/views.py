from django.shortcuts import redirect, render
from .models import products, orders
from django.core.paginator import Paginator
import json
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

        return redirect('orderReceived', order_id = order.id)

        
    return render(request, 'shop/checkout.html')

def orderReceived(request, order_id):
    orderitem = orders.objects.get(id=order_id)
    items = json.loads(orderitem.item)

    cart_items = []
    grand_total = 0

    for item_id, item in  items.items():
        subtotal = item['price'] * item['qty']
        grand_total += subtotal
        cart_items.append({**item, 'subtotal': subtotal, 'item_id': item_id})

    return render(request, 'shop/order-received.html', {
        'order': orderitem,
        'cartitems': cart_items,
        'grand_total': grand_total
    })
