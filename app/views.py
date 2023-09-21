from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse, QueryDict
from . models import Product, Customer, Cart, OrderPlaced, Payment, Payapp
from django.db.models import Count
from . forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
def home(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    all_product = Product.objects.all().order_by('-id')[:30]

    return render(request, 'app/index.html', locals())

def comingsoon(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/comingsoon.html', locals())

def allproduct(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    all_product = Product.objects.all().order_by('-id')

    return render(request, 'app/allproduct.html', locals())

def about(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/about.html', locals())


# learnig CRUD DASH SECTION

def dashboard(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    customers = Customer.objects.all()
    orders = OrderPlaced.objects.all().order_by('-id')

    total_customers = customers.count()
    total_orders = orders.count()

    delivered = orders.filter(status ='Delivered').count()
    pending = orders.filter(status ='Pending').count()
    accepted = orders.filter(status ='Accepted').count() + orders.filter(status ='Packed').count()+ orders.filter(status ='On the Way').count()
    return render(request, 'app/dashboard.html', locals())

def order(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    orders = OrderPlaced.objects.filter(user=request.user).order_by('-id')
    total_orders = orders.count()

    delivered = orders.filter(status ='Delivered').count()
    pending = orders.filter(status ='Pending').count() 
    accepted = orders.filter(status ='Accepted').count() + orders.filter(status ='On the Way').count() + orders.filter(status ='Packed').count()
    return render(request, 'app/order.html', locals())


def customer(request, pk):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    customer = Customer.objects.get(id=pk)
    orders = OrderPlaced.objects.filter(customer = customer)
    orders_count = orders.count()

    return render(request, 'app/customer.html', locals())


# learnig CRUD DASH SECTION


def contact(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/contact.html', locals())

class CategoryView(View):    
    def get(self, request, val):
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, 'app/category.html', locals())

class CategoryTitle(View):    
    def get(self, request, val):
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request, 'app/category.html', locals())


class ProductDetail(View):    
    def get(self, request, pk):
        totalitem = 0
        product = Product.objects.get(pk=pk)
        in_cart = False
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            in_cart = Cart.objects.filter(user = request.user, product = product).exists()
        user = request.user
        return render(request, 'app/productdetail.html', locals())

@method_decorator(login_required, name = 'dispatch')
class ProfileView(View):    
    def get(self, request):
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        form = CustomerProfileForm()
        return render (request, 'app/profile.html', locals())
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']

            reg = Customer(user=user, name=name, locality=locality, city = city, state=state, mobile=mobile)
            reg.save()
            messages.success(request, 'Congratulation !, Profile Save Successfully')
            return redirect ('address')
        else:
            messages.warning(request, 'Invalid Input Data')
        return render (request, 'app/address.html', locals())


class CustomerRegistrationView(View):
    def get(self, request):
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        form = CustomerRegistrationForm()
        return render(request, 'app/CustomerRegistration.html', locals())
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Congratulation! User Registration Successfully")
            return redirect('/accounts/login')

        else:
            messages.warning(request, "invalid Input Data")
        return render(request, 'app/customerregistration.html', locals())

@login_required
def add_to_cart(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id = product_id)
    product.added_to_cart=True
    print(product.added_to_cart)
    Cart(user = user, product = product).save()
    return redirect('/cart')

@method_decorator(login_required, name = 'dispatch')
class checkout(View):
    def get(self, request):
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        user = request.user
        add = Customer.objects.filter(user=user)
        cart_items = Cart.objects.filter(user = user)
        famount = 0
        for p in cart_items:
            value = p.quantity*p.product.discounted_price
            famount = famount + value
            percent = famount*0.02
        totalamount = famount + percent + 1000
        return render(request, 'app/checkout.html', locals())
    def post(self, request):
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        user = request.user
        add = Customer.objects.filter(user=user)
        cart_items = Cart.objects.filter(user = user)
        famount = 0
        for p in cart_items:
            value = p.quantity*p.product.discounted_price
            famount = famount + value
            percent = famount*0.02
        totalamount = famount + percent + 1000
        if request.method == 'POST':
            payment_image = request.FILES.get('payment_image')
            payment = Payment(
                payment_image = payment_image,
                amount = totalamount,
                user = user,
            )
            payment.save()
            return redirect('paymentdone')
        elif request.method == 'GET':
            return render(request, 'app/contact.html', locals())
        else:
            return render(request, 'app/home.html', locals())
      


@login_required
def show_cart(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    percent = 0
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount = amount + value
        percent = amount*0.02
    totalamount = amount + percent + 1000
    return render(request, 'app/addtocart.html', locals())


@login_required
def payment_done(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    order_id = request.GET.get('order_id')
    payment_id = request.GET.get('payment_id')
    cust_id = request.GET.get('cust_id')
    user = request.user
    customer = Customer.objects.filter(id=user.id)

    payment = Payment.objects.filter('payment_image')
    payment.paid=True
    payment.save()

    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user = user, customer = customer, product = c.product, quantity = c.quantity, payment = payment).save()
        c.delete()
    return redirect('order')

@login_required
def plus_cart(request):
    
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user = request.user))
        c.quantity += 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
            percent = amount*0.02
        totalamount = amount + percent + 1000
        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)

@login_required
def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user = request.user))
        c.quantity -= 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
            percent = amount * 0.02
        totalamount = amount + percent + 1000
        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)

@login_required
def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user = request.user))
        c.delete()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
            percent = amount * 0.02
        totalamount = amount + percent + 1000
        data = {
            'amount':amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)

@login_required
def address(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    add = Customer.objects.filter(user=request.user)
    return render (request, 'app/address.html', locals())

@method_decorator(login_required, name = 'dispatch')
class UpdateAddress(View):
    def get(self, request, pk):
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        add = Customer.objects.get(pk=pk) 
        form = CustomerProfileForm(instance = add )
        return render(request, 'app/updateAddress.html', locals())
    def post(self, request, pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data['state']
            add.save()
            messages.success(request, "Congratulation !! Profile Update Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return redirect('address')
        
def search(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    query = request.GET['search']
    product = Product.objects.filter(Q(title__icontains=query))
    return render(request, 'app/search.html', locals())

def paymentsuccessful(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/paymentsuccessful.html', locals())

def PayApp(request):
    user = request.user
    cart_items = Cart.objects.filter(user = user)
    famount = 0
    for p in cart_items:
        value = p.quantity*p.product.discounted_price
        famount = famount + value
        percent = famount*0.02
    totalamount = famount + percent + 1000
    if request.method == 'POST':
        paid = Payapp()
        paid.user = user
        paid.name = request.POST.get('name')
        paid.contact = request.POST.get('contact')
        paid.address = request.POST.get('address')
        paid.state = request.POST.get('state')
        paid.amount = totalamount
        if len(request.FILES) != 0:
            paid.receipt = request.FILES['image'] 
            paid.paid = True
        if not paid.name or not paid.contact or not paid.address or not paid.state or not paid.receipt:
            messages.info(request, 'All Fields must be filled out.')
            return redirect('payapp')
        paid.save()
        for c in cart_items:
            OrderPlaced(user=user, product=c.product, quantity = c.quantity, payment=paid).save()
            c.delete()
        return redirect('paymentsuccessful')
    return render(request, 'app/payapp.html', locals())



    