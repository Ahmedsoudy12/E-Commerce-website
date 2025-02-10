from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
from .models import Order
# Create your views here.

def index(request):
    product_objects = Product.objects.all()

    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains = item_name)

    # Paginator code
    paginator = Paginator(product_objects,8)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)


    return render(request,'shop/index.html',{'product_objects':product_objects})  # render(request,html file path,context)


def detail(request,id):
    product_object = Product.objects.get(id=id)
    return render(request,'shop/detail.html',{'product_object':product_object})


def checkout(request):

    if request.method == 'POST':
        items = request.POST.get('items','')
        name1 = request.POST.get('name1',"")
        name2 = request.POST.get('name2',"")
        email = request.POST.get('email',"")
        phonenumber = request.POST.get('phonenumber',"")
        address1 = request.POST.get('address1',"")
        address2 = request.POST.get('address2',"")
        city = request.POST.get('city',"")
        state = request.POST.get('state',"")
        zipcode = request.POST.get('zipcode',"")
        total = request.POST.get('total',"")
    
        order = Order(items=items,name1=name1,name2=name2,email=email,phonenumber=phonenumber,address1=address1,address2=address2,city=city,state=state,zipcode=zipcode,total=total)
        order.save()

    return render(request,'shop/checkout.html')



