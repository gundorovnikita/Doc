from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from .forms import *

def index(request):
	doc= Document.objects.all()
	if request.method == 'POST':
		create = create_document(request.POST)
		if create.is_valid():
			create.save()
			return redirect('index_url')
	else :
		create = create_document()

	context = {
		'doc':doc,
		'create':create,
	}
	return render(request,'index.html', context)

