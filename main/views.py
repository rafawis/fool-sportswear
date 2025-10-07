
import datetime
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
import json

# Create your views here.
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        logout(request)
        response = JsonResponse({
            'success': True,
            'redirect_url': reverse('main:login'),
        })
        response.delete_cookie('last_login')
        return response
    else:
        logout(request)
        response = redirect('main:login')
        response.delete_cookie('last_login')
        return response

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'
    if filter_type == "all":
        product_list = Product.objects.all()
    elif filter_type == "featured":
        product_list = Product.objects.filter(is_featured=True)
    else:
        product_list = Product.objects.filter(user=request.user)
    context = {
        'nama_aplikasi': 'Fool Sportswear',
        'name': 'Rafa Pradipta Ali Wisnutomo',
        'class': 'PBP E',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main.html", context)

@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }
    return render(request, "create_product.html", context)


def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))


@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
            return HttpResponse(status=404)

def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)




def show_json_by_id(request, product_id):
    try:
        product= Product.objects.select_related('user').get(pk=product_id)
        data ={
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
    


@csrf_exempt
@require_POST
def login_ajax(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"status": "ERROR", "message": "Invalid JSON format."}, status=400)

    form = AuthenticationForm(data=data)

    if form.is_valid():
        user = form.get_user()
        login(request, user)
        
        response = JsonResponse({"status": "SUCCESS", "message": "Login successful!"}, status=200)
        response.set_cookie('last_login', str(datetime.datetime.now())) # Perlu import datetime

        return response
    
    errors = dict(form.errors.items())
    return JsonResponse({"status": "ERROR", "message": "Invalid credentials or missing input.", "errors": errors}, status=400)

@csrf_exempt
@require_POST
def register_ajax(request):
    try:
        # Mengambil data dari JSON body, karena AJAX modern sering mengirim JSON
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"status": "ERROR", "message": "Invalid JSON format."}, status=400)

    form = UserCreationForm(data)

    if form.is_valid():
        user = form.save()
        messages.success(request, 'Your account has been successfully created! You can now log in.')
        return JsonResponse({"status": "SUCCESS", "message": "Account created successfully."}, status=201)
    
    # Ambil error per field untuk ditampilkan
    errors = dict(form.errors.items())
    return JsonResponse({"status": "ERROR", "message": "Failed to create account. Please check your input.", "errors": errors}, status=400)


@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name")) # strip HTML tags!
    price = int(strip_tags(request.POST.get("price")))
    description = strip_tags(request.POST.get("description"))
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    user = request.user

    new_product = Product(
        name=name, 
        price=price,
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )
    new_product.save()

    return JsonResponse({"status": "SUCCESS", "message": "Product created successfully."}, status=201)

@csrf_exempt
@require_POST
def edit_product_entry_ajax(request, id):
    product = get_object_or_404(Product, pk=id)
    product.name = strip_tags(request.POST.get("name"))
    product.price = int(strip_tags(request.POST.get("price")))
    product.description = strip_tags(request.POST.get("description"))
    product.category = request.POST.get("category")
    product.thumbnail = request.POST.get("thumbnail")
    product.is_featured = request.POST.get("is_featured") == 'on'
    product.user = request.user
    product.save()
    return JsonResponse({"status": "SUCCESS", "message": "Product updated successfully."}, status=200)

@csrf_exempt
@require_POST
@login_required(login_url='/login')
def delete_product_ajax(request, id): # <-- FUNGSI DELETE BARU
    try:
        # Ensure user owns the product (security check)
        product = Product.objects.get(pk=id, user=request.user) 
        product.delete()
        return HttpResponse("DELETED", status=200)
    except Product.DoesNotExist:
        return HttpResponseNotFound("Product not found or access denied")

