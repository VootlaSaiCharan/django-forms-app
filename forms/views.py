from django.shortcuts import render,redirect
from .forms import DetailsForm
from .models import Detail
from django.http import HttpResponse

# Create your views here.

def home(request):
    details=Detail.objects.all()
    return render(request,'home.html',{'details':details})



def create_view(request):
    if request.method=='POST':
        form=DetailsForm(request.POST)
        if form.is_valid():
            form.save() # very imp step ,if i miss this ,detail wont be saved into the database
            return redirect('home')
    else:
            form = DetailsForm()
            # return HttpResponse("something went wrong")
    # form=DetailsForm()
    return render(request,"form.html",{'form':form})


def update_view(request,id):
    detail_instance=Detail.objects.get(id=id)
    if request.method== 'POST':
        form=DetailsForm(request.POST,instance=detail_instance)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return HttpResponse("Something went wronggggg")


    form=DetailsForm(instance=detail_instance)
    return render(request,'form.html',{'form':form})

def delete_view(request,id):
    detail_instance=Detail.objects.get(id=id)
    if request.method== 'POST': 
        detail_instance.delete()
        return redirect('home')
    else:
        return HttpResponse("Invalid request method. Please use POST to delete.")


# def home(request):
#     if request.method == 'POST':
#         f=DetailsForm(request.POST)
#         if f.is_valid():
#             Detail.objects.create(
#                 name=f.cleaned_data['name'],
#                 phno=f.cleaned_data['phno'],
#                 email=f.cleaned_data['email'],
#                 addr=f.cleaned_data['addr']
#             )
#             return HttpResponse("thank you for submitting the form, details")

        

#     form=DetailsForm()

#     context={ 
#         'form':form
#      }
    
#     return render(request,"home.html",context)