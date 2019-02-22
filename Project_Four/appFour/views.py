from django.shortcuts import render

# Create your views here.
def index(request):
    context_dic = {'text':'hola mundo', 'number':100}
    return render(request,'appFour/index.html',context=context_dic)

def other(request):
    return render(request,'appFour/other.html')

def relative(request):
    return render(request,'appFour/relative_url.html')
