from django.shortcuts import render

# Create your views here.
def learn_django(request):
    cname='django is good language'
    duration='4 MONTHS'
    seats=10
    django_details={'nm':cname,'du':duration,'st':seats}
    return render(request,'course/courseone.html',context=django_details)
    # return render(request,'course/courseone.html',context={'nm':cname,'du':duration,'st':seats})
    # return render(request,'course/courseone.html',{'nm':False})
    