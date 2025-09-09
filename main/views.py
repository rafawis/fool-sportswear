from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'nama_aplikasi': 'Main',
        'name': 'Rafa Pradipta Ali Wisnutomo',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)