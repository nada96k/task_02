from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_website(request):
	context = {  
          "msg":"Hello World!"
	}
	return render(request,'mypage.html',context)