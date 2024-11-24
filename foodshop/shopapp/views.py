from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from shopapp.models import fooditem,Cart,Order
from django.db.models import Q
import random
import razorpay

# Create your views here.

def index(request):
    context={}
    f=fooditem.objects.filter(is_active=True)
    context['fooditems']=f 
    print(f)
    return render(request,'index.html',context)

def catfilter(request,cv):
    c1=Q(is_active=True)
    c2=Q(cat=cv)
    f=fooditem.objects.filter(c1 & c2)
    context={}
    context['fooditems']=f 
    return render(request,'index.html',context)

def sort(request,sv):
    if sv=='0':
        col='price'
    else:
        col='-price'
    f=fooditem.objects.filter(is_active=True).order_by(col)
    context={}
    context['fooditems']=f 
    return render(request,'index.html',context)

def range(request):
    min=request.GET['min']
    max=request.GET['max']
    c1=Q(price__gte=min)
    c2=Q(price__lte=max)
    c3=Q(is_active=True)
    f=fooditem.objects.filter(c1 & c2 & c3)
    context={}
    context['fooditems']=f 
    return render(request,'index.html',context)




def fdetails(request,fid):
    f=fooditem.objects.filter(id=fid)
    context={}
    context['fooditems']=f
    return render(request,'fooditemdetails.html',context)

def addtocart(request,fid):
    if request.user.is_authenticated:
        userid=request.user.id
        u=User.objects.filter(id=userid)
        print(u)
        print(u[0])
        f=fooditem.objects.filter(id=fid)
        print(f)
        print(f[0])
        c1=Q(uid=u[0])
        c2=Q(fid=f[0])
        c=Cart.objects.filter(c1 & c2)
        print(len(c))
        context={}
        context['fooditems']=f
        n=len(c)
        if n ==1:
            context['errmsg']="product already exists"
        else:
            c=Cart.objects.create(uid=u[0],fid=f[0])
            c.save()
            context['success']="The food item has been placed in your cart"
            
        return render(request,'fooditemdetails.html',context)
    else:
        return redirect("/login")

def yourcart(request):
    c=Cart.objects.filter(uid=request.user.id)
    s=0
    for x in c:
        s=s+x.fid.price*x.qty
    np=len(c)
    context={}
    context['data']=c
    context['total']=s
    context['items']=np
    return render(request,'yourcart.html',context)



def remove(request,cid):
    c=Cart.objects.filter(id=cid)
    c.delete()
    return redirect('/yourcart')

def updateqty(request,qv,cid):
    c=Cart.objects.filter(id=cid)
    if qv=='1':
        t=c[0].qty+1
        c.update(qty=t)
    else:
        if c[0].qty>1:
            t=c[0].qty-1
            c.update(qty=t)
        
    return redirect('/yourcart')

def confirmorder(request):
    userid=request.user.id
    c=Cart.objects.filter(uid=userid)
    oid=random.randrange(1000,9999)
    for x in c:
        o=Order.objects.create(order_id=oid,fid=x.fid,uid=x.uid,qty=x.qty)
        o.save()
        x.delete()
    orders=Order.objects.filter(uid=userid)
    context={}
    context['data']=orders
    np=len(orders)
    s=0
    for x in orders:
        s=s+x.fid.price*x.qty
    context['total']=s
    context['items']=np
    return render(request,"confirmorder.html",context)

def paynow(request):
    orders=Order.objects.filter(uid=request.user.id)
    np=len(orders)
    s=0
    for x in orders:
        s=s+x.fid.price*x.qty
        oid=x.order_id
    client = razorpay.Client(auth=("rzp_test_zifxxYsHIF3TD7", "MO7Dmgv6ziiTppbw6MstCkvT"))

    data = { "amount": s*100, "currency": "INR", "receipt": oid }
    payment = client.order.create(data=data)
    return render(request,"pay.html")


def register(request):
    if request.method=="POST":
        uname=request.POST['uname']
        upass=request.POST['upass']
        ucpass=request.POST['ucpass']
        if uname=="" or upass=="" or ucpass=="":
            context = {'errmsg': "Please ensure all fields are filled!"}
            return render(request,'uregister.html',context)
        elif upass!=ucpass:
            context = {'errmsg': "Passwords are not identical!"}
            return render(request,'uregister.html',context)
        else:
            try:
                u=User.objects.create(password=upass,username=uname,email=uname)
                u.set_password(upass)
                u.save()
                context={'successmsg':"User account created successfully"}
                return render(request,'uregister.html',context)
            except:
                context={'errmsg':"Account already exists, use a different email address"}
                return render(request,'uregister.html',context)

    else:
        return render(request,'uregister.html')

def ulogin(request):
    if request.method=="POST":
        uname=request.POST['uname']
        upass=request.POST['upass']
        context={}
        if uname=="" or upass=="":
            context={'errmsg':"Please ensure all fields are filled!"}
            return render(request,'ulogin.html',context)
        else:
            u=authenticate(username=uname,password=upass)
            if u is not None:
                login(request,u)   
                return redirect('/index')
            else:
                context={'errmsg':"Invalid login credentials"}
                return render(request,'ulogin.html',context)
                
    else:
        return render(request,'ulogin.html')

def ulogout(request):
    logout(request)
    return redirect('/index')