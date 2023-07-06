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
	query=product_tb.objects.filter(id=pid)
	return render(request,'single.html',{"data":query})

# def checkout(request):
# 	return render(request,'cart.html')

def login(request):
	if request.method=='POST':
		email=request.POST['email']
		password=request.POST['password']
		check=user_register_tb.objects.filter(email=email,password=password)
		if check:
			for x in check:
				request.session['uid']=x.id
				request.session['uname']=x.username
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
		check=user_register_tb.objects.filter(email=email)
		if password==cpassword:
			if check:
				return render(request,'register.html',{"error":"email has already taken !"})
			else:
				user=user_register_tb(username=name,email=email,password=password,phone=phone)
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
		user=product_tb(productname=name,newprice=price,desc=desc,qty=qty,image=image,catagory=category)
		user.save()
		return redirect('/product_table/')
	else:
		return render(request,'addproduct.html')
	


def shop(request):
	query=product_tb.objects.all()
	return render(request,'shop.html',{"data":query})


def product_table(request):
	query=product_tb.objects.all()
	return render(request,'product_table.html',{"data":query})


def prdelete(request):
	regid=request.GET['regid']
	data=product_tb.objects.filter(id=regid).delete()
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
			oldrec=product_tb.objects.filter(id=regid)
			updrec=product_tb.objects.get(id=regid)
			for x in oldrec:
				imageurl=x.image.url
				pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imageurl
				if os.path.exists(pathtoimage):
					os.remove(pathtoimage)
					print('Successfully deleted')
					updrec.image=image
					updrec.save()
					print("-----------------")
		user=product_tb.objects.filter(id=regid).update(productname=name,newprice=price,desc=desc,qty=qty,catagory=category)
		return redirect('/product_table/')
	else:
		regid=request.GET['regid']
		data=product_tb.objects.filter(id=regid)
		return render(request,'prdupdate.html',{'data':data})




	

# --------------------OLD ADD TO CART----------------


# # def addtocart(request):
# #     if request.session.has_key('uid'):
# #         if request.method == "POST":
# #             pid=request.GET["pid"]
# #             prd=product_tb.objects.get(id=pid)
# #             uid=request.session['uid']
# #             usr=user_register_tb.objects.get(id=uid)
# #             product=product_tb.objects.filter(id=pid)
# #             for x in product:
# #                 price=x.price
# #             deliv=(int(price)*10)/100
# #             total=0
# #             total=int(deliv)+int(price)


# #             data1=cart_tb.objects.filter(uid=usr,pid=prd,status="pending")
	    	
# #             if data1:
# #                 total1=0
# #                 for x in data1:
# #                     qty=int(x.quantity)
# #                     qty+=1
# #                     price=x.pid.price
# #                     price1=x.total
# #                     total1=total1+float(price1)

# #                 # add=cart_tb.objects.filter(uid=usr,pid=prd,status="pending").update(quantity=qty)
# #                 total=0
# #                 # for x in data1:
# #                 deliv=(float(price)*10)/100
# #                 total=int(deliv)+(float(price)*int(qty))
# #                 add=cart_tb.objects.filter(uid=usr,pid=prd,status="pending").update(total=total,quantity=qty)
# #                 datas=cart_tb.objects.filter(uid=usr,status="pending")
# #                 # for x in data1:

                   
# #                 return render(request,"cart.html",{"data":datas,"total":total1})
				
# #             else:
# #                 add=cart_tb(pid=prd,uid=usr,quantity=1,total=total)
# #                 add.save()
# #             datas=cart_tb.objects.filter(uid=usr,status="pending")
# #             total=0
# #             for x in datas:
# #                 price=x.total
		
# #                 total=int(deliv)+(float(price)*int(qty))

# #             return render(request,"cart.html",{"data":datas,"total":total})
# #         else:
# #             pid=request.GET['pid']
# #             datas=product_tb.objects.filter(id=pid)
# #             return render(request,"cart.html",{"data":datas})
# #     else:
# #         return HttpResponseRedirect("/login/")
	



# def addtocart(request):
# 	if request.session.has_key('uid'):
# 		if request.method=='POST':
# 			pid=request.GET['pid']
# 			num=request.session['uid']
# 			data1=cart_tb.objects.filter(num=num,status="pending")
# 			for x in data:
# 				qty=x.quantity
			
# 			prd=product_tb.objects.filter(id=pid)
# 			for x in prd:
# 				price=x.price
				

		
				
# 			total=int(price)*(qty)
# 			prdid=product_tb.objects.get(id=pid)
			
# 			userid=user_register_tb.objects.get(id=num)
# 			check=cart_tb.objects.filter(num=num,pid=pid,status="pending")
# 			if check:
# 				data=cart_tb.objects.filter(num=num,status="pending")
# 				total=0
# 				for x in data:
# 					price=x.total
# 					total=int(price)+total
# 					return render(request,"cart.html",{"data":data,"error":"already exist","total":total})
# 			else:
# 				add=cart_tb(num=userid,pid=prdid,total=total,status="pending")
# 				add.save()
# 				data=cart_tb.objects.filter(num=num,status="pending")
# 				total=0
# 				for x in data:
# 					price=x.total
# 					total=int(price)+total
# 				return render(request,"cart.html",{"data":data,"total":total})
# 		else:
# 			pid=request.GET['pid']
# 			query=cart_tb.objects.filter(id=pid)
# 			return render(request,'single.html',{"data":query})



# 	else:
# 		return redirect('/login/')


# def cart_update(request):
#     cid=request.GET['cid']
    
#     uid=request.session['uid']
#     prd=product_tb.objects.all()
#     datas=cart_tb.objects.filter(num=uid,status="pending")
#     quantity=request.POST['qty']
#     for x in datas:
#         price=x.pid.price

	
	

#     newprice=(float(price)*int(quantity))+((float(price)*10)/100)
    
#     # product_tb.objects.filter(id=pid).update(price=newprice)
#     cart_tb.objects.filter(id=cid).update(quantity=quantity)


#     total=0
#     for x in datas:
#         price=x.total
#         total=total+float(newprice)
    
#     return render(request,"cart.html",{"data":datas,"total":total})
    

# def payment(request):
# 	return render(request,'payment.html')











# --------------------NEW ADD TO CART----------------






def addtocart(request):
    if request.session.has_key('uid'):
        if request.method == "POST":
            pid=request.GET["pid"]
            prd=product_tb.objects.get(id=pid)
            uid=request.session['uid']
            usr=user_register_tb.objects.get(id=uid)
            product=product_tb.objects.filter(id=pid)
            for x in product:
                price=x.newprice
            deliv=(int(price)*10)/100
            total=0
            total=int(deliv)+int(price)


            data1=cart_tb.objects.filter(uid=usr,pid=prd,status="pending")
            if data1:
                total1=0
                for x in data1:
                    qty=int(x.quantity)
                    qty+=1
                    price=x.pid.newprice
                    price1=x.total
                    total1=total1+float(price1)

			

                # add=cart_tb.objects.filter(uid=usr,pid=prd,status="pending").update(quantity=qty)
                total=0
                # for x in data1:
                deliv=(float(price)*10)/100
                total=int(deliv)+(float(price)*int(qty))
                add=cart_tb.objects.filter(uid=usr,pid=prd,status="pending").update(total=total,quantity=qty)
                datas=cart_tb.objects.filter(uid=usr,status="pending")
                # for x in data1:
                return render(request,"cart.html",{"data":datas,"total":total1})
            else:
                add=cart_tb(pid=prd,uid=usr,quantity=1,total=total)
                add.save()
            datas=cart_tb.objects.filter(uid=usr,status="pending")
            total=0
            for x in datas:
                price=x.total
                total=total+float(price)
            return render(request,"cart.html",{"data":datas,"total":total})
        else:
            pid=request.GET['pid']
            datas=product_tb.objects.filter(id=pid)
            return render(request,"cart.html",{"data":datas})
    else:
        return HttpResponseRedirect("/login/")






def cart(request):
    # mydata=cart_tb.objects.all()
    # return render(request,"cart.html",{"data1":mydata})
    uid=request.session['uid']
    usr=user_register_tb.objects.get(id=uid)
    datas=cart_tb.objects.filter(uid=usr,status="pending")
    total=0
    for x in datas:
        price=x.total
        total=total+float(price)
    return render(request,"cart.html",{"data":datas,"total":total})
   

# def cart_update(request):
#     cid=request.GET['cid']
#     quantity=request.POST['qty']
#     cart=cart_tb.objects.filter(id=cid)
#     for x in cart:
#         price=x.pid.newprice
	
# 		# qty=x.quantity
# 		# quantity1=x.pid.qty


#     newprice=(float(price)*int(quantity))+((float(price)*10)/100)
#     cart_tb.objects.filter(id=cid).update(quantity=quantity,total=newprice)
#     return HttpResponseRedirect("/cart/")



def cart_update(request):
	cid=request.GET['cid']
	quantity=request.POST['qty']
	cart=cart_tb.objects.filter(id=cid)
	for x in cart:
		price=x.pid.newprice
		qty=x.quantity
		quantity1=x.pid.qty
		pid=x.pid.id

	newprice=(float(price)*int(quantity))+((float(price)*10)/100)
	cart_tb.objects.filter(id=cid).update(quantity=quantity,total=newprice)
	lessqty=int(quantity1)-int(qty)
	product_tb.objects.filter(id=pid).update(qty=lessqty)
	return HttpResponseRedirect("/cart/")
	


def cart_remove(request):
    cid=request.GET['cid']
    cart_tb.objects.filter(id=cid).delete()
    return HttpResponseRedirect("/cart/")





def payment(request):
	return render(request,'payment.html')