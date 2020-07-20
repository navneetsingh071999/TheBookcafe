from django.shortcuts import render,redirect
from .models import products
from django.contrib import messages


# Create your views here.
def store(request):
    book = products.objects.all()
    return render(request,'store.html',{'book':book})

def search(request):
    name = request.GET['bkname']
    category = products.objects.filter(bkname__icontains=name)
    if category:
        return render(request,'category.html',{'category':category})
    else:
        msg = ['Sorry!! No Book Found.']
        return render(request,'category.html',{'msg':msg})

def more(request):
    bkinfo = request.GET['bkbtn']
    category = products.objects.filter(id=bkinfo)
    return render(request,'more.html',{'category':category})
       

def category(request):
    cate = request.GET['cate']
    if cate == 'novel':
        category = products.objects.filter(bkcatgory="Novels")
        if category:
            return render(request,'category.html',{'category':category})
        else:
            msg = ['Sorry!! No Book Available.']
            return render(request,'category.html',{'msg':msg})
    elif cate == 'Academic':
        category = products.objects.filter(bkcatgory="Academics")
        if category:
            return render(request,'category.html',{'category':category})
        else:
            msg = ['Sorry!! No Book Available.']
            return render(request,'category.html',{'msg':msg})
    elif cate == 'Reference':
        category = products.objects.filter(bkcatgory="Reference")
        if category:
            return render(request,'category.html',{'category':category})
        else:
            msg = ['Sorry!! No Book Available.']
            return render(request,'category.html',{'msg':msg})


def seller(request):
    if request.method == 'POST' and request.FILES['img']:
        seller_name = request.POST['seller_name']
        price = request.POST['price']
        img = request.FILES['img']
        bkname = request.POST['bkname']
        bkauth = request.POST['bkauth']
        bkcatgory = request.POST['bkcatgory']
        bkedtion = request.POST['bkedtion']
        seller_address = request.POST['seller_address']
        seller_email = request.POST['seller_email']
        product = products(seller_email=seller_email,seller_address=seller_address,bkedtion=bkedtion,bkcatgory=bkcatgory,bkauth=bkauth,bkname=bkname,seller_name=seller_name,price=price,img=img)
        product.save()
        print("added")
        return redirect('/store')


