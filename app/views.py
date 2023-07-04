from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from.models import *
import os

# Create your views here.

def index(request):
	
	return render(request,'index.html')


def about(request):
	return render(request,'about.html')


def contact(request):
	return render(request,'contact.html')

def single(request):
	pid=request.GET['pid']
	query=ad_product.objects.filter(id=pid)
	return render(request,'single.html',{"data":query})

# def checkout(request):
# 	return render(request,'checkout.html')

def login(request):
	if request.method=='POST':
		email=request.POST['email']
		password=request.POST['password']
		check=u_reg.objects.filter(email=email,password=password)
		if check:
			for x in check:
				request.session['uid']=x.id
				request.session['uname']=x.name
				return render(request,'index.html',{"success":"Logged  In"})
		else:
			return render(request,'login.html',{"error":"Invalid Data Please Register"})
	else:
		return render(request,'login.html')

def register(request):
	if request.method=='POST':
		name=request.POST['name']
		email=request.POST['email']
		password=request.POST['password']
		cpassword=request.POST['cpassword']
		phone=request.POST['phone']
		check=u_reg.objects.filter(email=email)
		if password==cpassword:
			if check:
				return render(request,'register.html',{"error":"email has already taken !"})
			else:
				user=u_reg(name=name,email=email,password=password,phone=phone)
				user.save()
				return render(request,'login.html',{"error":"Rgisterd sucessfully Please Login  !"})
		else:
			return render(request,"register.html",{"error":"Passwords doesn't match !"})
	else:
		return render(request,'register.html')
	



def logout(request):
	if request.session.has_key('uid'):
		del request.session['uid']
		del request.session['uname']
		return  HttpResponseRedirect('/')
	else:
		return redirect('/')
	



def addproduct(request):
	if request.method=='POST':
		name=request.POST['name']
		price=request.POST['price']
		desc=request.POST['desc']
		qty=request.POST['qty']
		image=request.FILES['image']
		category=request.POST['category']
		user=ad_product(name=name,price=price,desc=desc,qty=qty,image=image,category=category)
		user.save()
		return redirect('/product_table/')
	else:
		return render(request,'addproduct.html')
	


def shop(request):
	query=ad_product.objects.all()
	return render(request,'shop.html',{"data":query})


def product_table(request):
	query=ad_product.objects.all()
	return render(request,'product_table.html',{"data":query})


def prdelete(request):
	regid=request.GET['regid']
	data=ad_product.objects.filter(id=regid).delete()
	return redirect('/product_table/')



def prdupdate(request):
	if request.method=='POST':
		name=request.POST['name']
		price=request.POST['price']
		desc=request.POST['desc']
		qty=request.POST['qty']
		category=request.POST['category']
		regid=request.GET['regid']
		checkbox=request.POST["imgup"]
		if checkbox == "yes":
			image=request.FILES["image"]
			oldrec=ad_product.objects.filter(id=regid)
			updrec=ad_product.objects.get(id=regid)
			for x in oldrec:
				imageurl=x.image.url
				pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imageurl
				if os.path.exists(pathtoimage):
					os.remove(pathtoimage)
					print('Successfully deleted')
					updrec.image=image
					updrec.save()
					print("-----------------")
		user=ad_product.objects.filter(id=regid).update(name=name,price=price,desc=desc,qty=qty,category=category)
		return redirect('/product_table/')
	else:
		regid=request.GET['regid']
		data=ad_product.objects.filter(id=regid)
		return render(request,'prdupdate.html',{'data':data})
	




# def addtocart(request):
#     if request.session.has_key('uid'):
#         if request.method == "POST":
#             pid=request.GET["pid"]
#             prd=ad_product.objects.get(id=pid)
#             uid=request.session['uid']
#             usr=u_reg.objects.get(id=uid)
#             product=ad_product.objects.filter(id=pid)
#             for x in product:
#                 price=x.price
#             deliv=(int(price)*10)/100
#             total=0
#             total=int(deliv)+int(price)


#             data1=ad_cart.objects.filter(uid=usr,pid=prd,status="pending")
	    	
#             if data1:
#                 total1=0
#                 for x in data1:
#                     qty=int(x.quantity)
#                     qty+=1
#                     price=x.pid.price
#                     price1=x.total
#                     total1=total1+float(price1)

#                 # add=ad_cart.objects.filter(uid=usr,pid=prd,status="pending").update(quantity=qty)
#                 total=0
#                 # for x in data1:
#                 deliv=(float(price)*10)/100
#                 total=int(deliv)+(float(price)*int(qty))
#                 add=ad_cart.objects.filter(uid=usr,pid=prd,status="pending").update(total=total,quantity=qty)
#                 datas=ad_cart.objects.filter(uid=usr,status="pending")
#                 # for x in data1:

                   
#                 return render(request,"checkout.html",{"data2":datas,"total":total1})
				
#             else:
#                 add=ad_cart(pid=prd,uid=usr,quantity=1,total=total)
#                 add.save()
#             datas=ad_cart.objects.filter(uid=usr,status="pending")
#             total=0
#             for x in datas:
#                 price=x.total
		
#                 total=int(deliv)+(float(price)*int(qty))

#             return render(request,"checkout.html",{"data2":datas,"total":total})
#         else:
#             pid=request.GET['pid']
#             datas=ad_product.objects.filter(id=pid)
#             return render(request,"cart.html",{"data2":datas})
#     else:
#         return HttpResponseRedirect("/login/")
	



def addtocart(request):
	if request.session.has_key('uid'):
		if request.method=='POST':
			pid=request.GET['pid']
			
			prd=ad_product.objects.filter(id=pid)
			for x in prd:
				price=x.price
				qty=1
				
			total=int(price)*(qty)
			prdid=ad_product.objects.get(id=pid)
			num=request.session['uid']
			userid=u_reg.objects.get(id=num)
			check=ad_cart.objects.filter(num=num,pid=pid,status="pending")
			if check:
				data=ad_cart.objects.filter(num=num,status="pending")
				total=0
				for x in data:
					price=x.total
					total=int(price)+total
					return render(request,"checkout.html",{"data":data,"error":"already exist","total":total})
			else:
				add=ad_cart(num=userid,pid=prdid,total=total,status="pending")
				add.save()
				data=ad_cart.objects.filter(num=num,status="pending")
				total=0
				for x in data:
					price=x.total
					total=int(price)+total
				return render(request,"checkout.html",{"data":data,"total":total})
		else:
			pid=request.GET['pid']
			query=ad_cart.objects.filter(id=pid)
			return render(request,'single.html',{"data":query})



	else:
		return redirect('/login/')


def cart_update(request):
    cid=request.GET['cid']
    
    uid=request.session['uid']
    prd=ad_product.objects.all()
    datas=ad_cart.objects.filter(num=uid,status="pending")
    quantity=request.POST['qty']
    for x in datas:
        price=x.pid.price

	
	

    newprice=(float(price)*int(quantity))+((float(price)*10)/100)
    
    # ad_product.objects.filter(id=pid).update(price=newprice)
    ad_cart.objects.filter(id=cid).update(quantity=quantity)


    total=0
    for x in datas:
        price=x.total
        total=total+float(newprice)
    
    return render(request,"checkout.html",{"data":datas,"total":total})
    

def payment(request):
	
	return render(request,'payment.html')