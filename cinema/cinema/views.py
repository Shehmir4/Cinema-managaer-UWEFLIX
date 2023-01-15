from django.shortcuts import render, HttpResponseRedirect,redirect
from .models import club

def home(request):

    std = club.objects.all

    return render(request,"base.html",{'std':std})


def addclub(request):
    if request.method=='POST':
        print("Added")
        #retrieve user inputs
        add_rollno = request.POST.get("add_rollno")
        add_name = request.POST.get("add_name")
        add_email = request.POST.get("add_email")
        add_phone = request.POST.get("add_phone")
        add_address = request.POST.get("add_address")

        #create an object for models
        s = club(roll = add_rollno,name = add_name,email = add_email,phone=add_phone,address = add_address)
        s.save()    
    return render(request,'addclub.html')   


def delete_data(request,id):
        pi = club.objects.get(pk=id)
        pi.delete()    
        return redirect('home')


def update_data(request, id):
    # Retrieve the club object with the specified id
    club_obj = club.objects.get(pk=id)

    # Render the update_std.html template and pass the club object as context
    return render(request, "update_std.html", {'std': club_obj}) 


def do_update_std(request, id):
    # Get form data from the request
    roll_no = request.POST.get("std_roll")
    name = request.POST.get("std_name")
    email = request.POST.get("std_email")
    address = request.POST.get("std_address")
    phone = request.POST.get("std_phone")

    # Retrieve the club object with the specified id
    club_obj = club.objects.get(pk=id)

    # Update the club object with the form data
    club_obj.name = name
    club_obj.email = email
    club_obj.address = address
    club_obj.phone = phone
    club_obj.roll = roll_no

    # Save the updated club object to the database
    club_obj.save()
    print(" do _update is saved ")

    # Redirect the user to the home page
    return redirect('home')


