from django.views.generic import DetailView, ListView, UpdateView, CreateView, TemplateView
from .models import Product, Order, Company
from .forms import OrderForm
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.contrib.messages.views import messages
from ip2geotools.databases.noncommercial import DbIpCity
## importing socket module
import socket
from django.contrib.gis.geos import Point

        

class CompanyListView(ListView):
    model = Company
    
class ProductListView(ListView):
    model = Product
    
    def get_queryset(self):
        slug = self.kwargs.get('slug')
        return Product.objects.filter(company__slug=slug)
    

class ProductDetailView(DetailView):
    model = Product



class OrderListView(ListView):
    model = Order

    def get_queryset(self):
        return Order.objects.filter(order_by=self.request.user)



class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    success_url = 'Product_order_conform'

    def get_context_data(self,  object_list=None, **kwargs):
        context = super(OrderCreateView, self).get_context_data(**kwargs)
        context['product'] = get_object_or_404(Product, slug=self.kwargs['slug'])
        
        ## getting the hostname by socket.gethostname() method
        hostname = socket.gethostname()
        ## getting the IP address using socket.gethostbyname() method
        ip_address = socket.gethostbyname(hostname)
        response = DbIpCity.get(ip_address, api_key='free')
        lat = response.latitude
        lon = response.longitude
        

        context['location'] = Point(float(lat), float(lon))
        return context


    def form_valid(self, form):
        slug = self.kwargs.get('slug')
        product = Product.objects.get(slug__iexact=slug)
        form.instance.product = product
        form.instance.cost = int(form.instance.count) * int(product.price)
        return super(OrderCreateView, self).form_valid(form)


class OrderDetailView(DetailView):
    model = Order


def order_conform(self):
    return render(self, 'Product/thanks.html')

