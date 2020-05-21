from django.shortcuts import render, redirect
from DbCon.forms import StudentForm
from DbCon.models import Students


# Create your views here.
def std(request):
	if request.method == "POST":
		form = StudentForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('/view')
			except:
				pass
	else:
		form = StudentForm()
	return render(request, 'index.html', {'form': form})
