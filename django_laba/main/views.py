from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main/index.html')

# def about(request):
#     return render(request, 'main/about_page.html')