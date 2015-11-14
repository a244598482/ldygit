from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context
from django.shortcuts import render_to_response
from addr_book.models import Book
from addr_book.models import Author
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from PIL import Image
def homepage(request):
    book_list = Book.objects.all()
    return render_to_response("homepage.html", {"Book_list":book_list})
def show(request):
    thebook=Book.objects.get(id=request.GET["id"])
    return render_to_response("show.html", {"thebook":thebook})
def show2(request):
    theauthor=Author.objects.get(id=request.GET["id"])
    return render_to_response("show2.html", {"theauthor":theauthor})
@csrf_exempt
def add(request):
    author_list = Author.objects.all()
    if request.POST:
        post = request.POST
        havenoword=True
        if("AuthorID" in request.POST):
        	if((len(post["ISBN"])!=0) and (len(post["Title"])!=0)):
                    havenoword=False
                    author=Author.objects.get(AuthorID=post["AuthorID"])
                    new_book = Book(
                            ISBN = post["ISBN"],
                            Title = post["Title"],
                            AuthorID = author,
                            Publisher = post["Publisher"],
                            PublishDate = post["PublishDate"],
                            Price = post["Price"])           
                    new_book.save()  
                    return HttpResponseRedirect("/")
        return render_to_response("add.html",{"havenoword":havenoword,"author_list":author_list})
    else:
        return render_to_response("add.html",{"author_list":author_list})
@csrf_exempt
def add2(request):
    if request.POST:
        post = request.POST
        havenoword2=True
    	if((len(post["AuthorID"])!=0) and (len(post["Name"])!=0)):
                havenoword2=False
                new_author = Author(
                        AuthorID = post["AuthorID"],
                        Name = post["Name"],
                        Age = post["Age"],
                        Countury = post["Countury"])         
                new_author.save()  
                return HttpResponseRedirect("/add/")
        return render_to_response("add2.html",{"havenoword":havenoword2})
    else:
        return render_to_response("add2.html")
def delete(request):
    everyid = request.GET["id"]
    Book.objects.filter(id=everyid).delete()
    return HttpResponseRedirect("/")
@csrf_exempt
def update(request):
    new_book=Book.objects.get(id=request.GET["id"])
    if request.POST:	
        post = request.POST
        new_book.Title = post["Title"]
        new_book.Publisher = post["Publisher"]
        new_book.PublishDate = post["PublishDate"]
        new_book.Price = post["Price"]      
        new_book.save()
        return HttpResponseRedirect("/")
    else:
    	c = Context({"new_book": new_book})
    	return render_to_response("update.html", c)
@csrf_exempt
def search1(request):
    new_book=Book.objects.filter(Title=request.POST["search1"])
    if len(new_book)==0:
        return render_to_response("searcherror.html")
    else:
    	c = Context({"Book_list": new_book})
    	return render_to_response("search1.html", c)
@csrf_exempt
def search2(request):
    new_author=Author.objects.filter(Name=request.POST["search2"])
    new_book=Book.objects.filter(AuthorID=new_author)
    if len(new_book)==0:
        return render_to_response("searcherror.html")
    else:
    	c = Context({"Book_list": new_book})
        return render_to_response("search1.html", c)
"""
@csrf_exempt
def png(request):
    username="ding"
    if request.method == 'POST':        
        if 'image' in request.FILES:
            image=request.FILES["image"]
            img=Image.open(image)
            img.thumbnail((250,250),Image.ANTIALIAS)
            url=image.name
            name='./'+username+'.png'
            img.save(name,"jpeg")
    return render_to_response("jpg.html")
"""