from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'npm' : '2306241682',
        'name': 'Akhyar Rasyid Asy syifa',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
