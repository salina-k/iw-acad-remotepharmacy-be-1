from django.shortcuts import render
from .models import Product,Category
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CategorySerializer,ProductSerializer
from .models import Product,Order,Cart,Category
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your views here.
@api_view(['GET'])
def info_view_cat(request,pk):
    if request.method=='GET':
        try:
            obj=Category.objects.get(id=pk)
            catprod = Product.objects.filter(prod=obj)
            b=[]
            for i in catprod:
                b.append(i)

            def produ():

                d=dict()
                l=[]
                for j in b:
                    d.update({'name':j.name ,
                              'desc':j.desc,
                              'image':j.image,
                              'price':j.price,
                              'in_stock':j.in_stock
                              },)
                    l.append(d)
                return l
            content={

                'name':produ,



            }


        except:
            return Response({'error':'Doesnot exists'})
        # queryset=Category.objects.all()
        # result=[]
        # for i in ram:
        #     serializer = InfoSerializer(instance=i)
        #     result.append(serializer.data)
        serializer=CategorySerializer(instance=content)

        return Response(serializer.data)

@api_view(['GET'])
def info_view(request):
    if request.method=='GET':
        queryset=Category.objects.all()
        serializer=CategorySerializer(instance=queryset,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def info_product_view(request):
    if request.method=='GET':
        queryset=Product.objects.all()
        # result=[]
        # for i in ram:
        #     serializer = InfoSerializer(instance=i)
        #     result.append(serializer.data)
        serializer=ProductSerializer(instance=queryset,many=True)

        return Response(serializer.data)

@api_view(['GET'])
def info_view_prod(request,pk):
    if request.method=='GET':
        try:
            obj=Category.objects.get(id=pk)
            catprod=Product.objects.get(prod=obj)
        except:
            return Response({'error':'Doesnot exists'})
        # queryset=Category.objects.all()
        # result=[]
        # for i in ram:
        #     serializer = InfoSerializer(instance=i)
        #     result.append(serializer.data)
        serializer=CategorySerializer(instance=catprod)

        return Response(serializer.data)


@api_view(['GET'])
def info_view_prodindividual(request,pk):
    if request.method=='GET':
        try:
            obj=Product.objects.filter(id=pk)
            def productind():

                d=dict()
                l=[]
                for j in obj:
                    d.update({'name':j.name ,
                              'desc':j.desc,
                              'image':j.image,
                              'price':j.price,
                              'in_stock':j.in_stock
                              },)
                    l.append(d)
                return l

            content = {

                'name': productind,

            }
        except:
            return Response({'error':'Doesnot exists'})
        serializer=CategorySerializer(instance=content)

        return Response(serializer.data)

def TotalPrice(request,user_id):
    user=User.objects.get(id=user_id)
    cartuser=user.cart_set.all()
    orderlist=[]
    for i in cartuser:
        orderlist.append[i.order_set.all()]
    countoforder=len(orderlist)
    loopcontroller=0
    sum=0
    while loopcontroller < len(countoforder):
        sum=sum+int(countoforder[loopcontroller].prod.price)
        s=s+1
    return render(request,'',{'sum':sum})


