from django.shortcuts import render,HttpResponse,redirect
from .models import Book
from Book.forms import StudentForm, FileUploadForm 
from .models import FileUpload
from django.contrib.auth.decorators import login_required


import logging
logger = logging.getLogger("first")

# Create your views here.

@login_required(login_url='/user/login/')
def Welcome(request):
    logger.info("in welcome view")
    Books = Book.objects.all()
    logger.info(f"all_book_data:- {Books}")
    return render(request,"home.html", {"all_books": Books})


@login_required(login_url='/user/login/')
def Create_book(request):
    logger.info(request.POST)
    if request.method == "GET":
        return render(request, "create_book.html")
    elif request.method == "POST":
        data = request.POST 
        if not data.get("id"):
            Book.objects.create(title = data.get("title"), author = data.get("author"), 
                            publication_date = data.get("publication date"), price = data.get("price"))
        else:
            try:
                book_obj = Book.objects.get(id = (data.get("id")))
            except Exception as msg:
                logger.error(f"{msg}------------------------------in exception")
                book_obj.title = data.get("title")
                book_obj.author = data.get("author")
                book_obj.publication_date = data.get("publication date")
                book_obj.price = data.get("price")
                book_obj.save()

        return redirect("home")    

@login_required(login_url='/user/login/')
def Edit_book(request, id):
    try:    
        book_obj = Book.objects.get(id = id)
    except Book.DoesNotExist as msg:
        return HttpResponse("Book does not exit")
    else:
        return render(request,"create_book.html",  {"Book": book_obj})


@login_required(login_url='/user/login/')
def Delete_book(request, id):
    try:
        book_obj = Book.objects.get(id = id)
    except Book.DoesNotExist as msg:
        return HttpResponse("Book does not exit")
    
    else:
        if request.POST.get("type_of_delete") == "HardDelete":
            book_obj.delete()
        else:   
            book_obj.isdeleted = True                    #soft delete 
            book_obj.save()     
        return redirect("home")

@login_required(login_url='/user/login/')
def show_Deleted_books(request):
    deleted_books = Book.objects.filter(isdeleted=True)
    return render(request, "deleted_book.html", {"deleted_book":deleted_books})


@login_required(login_url='/user/deleted_book/')
def Restore_book(request,id):
    try:
        book_obj = Book.objects.get(id = id) 
    except Book.DoesNotExist:
        return HttpResponse("Book does not exit")
    else:
        book_obj.isdeleted = False
        book_obj.save()
    return redirect("home") 
    
@login_required(login_url='/user/login/')  
def index(request):  
    student = StudentForm()  
    return render(request,"index.html",{'form':student}) 


@login_required(login_url='/user/login/')
def file_upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')  
    else:
        form = FileUploadForm()

    return render(request, 'upload_file.html', {'form': form})


@login_required(login_url='/user/login/')
def file_list(request):
    files = FileUpload.objects.all()
    return render(request, 'file_list.html', {'all_files': files})