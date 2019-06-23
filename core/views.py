from django.shortcuts import render


#View Geral
def home(request):
	return render(request, 'index.html')

#View do Perfil
@login_required
def perfil(request):
	return render(request, "perfil.html")

def registro(request):
	form = UserCreationForm(request.POST or None)
	form_profile = ProfileForm(request.POST or None)
	
	if form.is_valid() and form_profile.is_valid():
		user = form.save()
		profile = form_profile.save(commit=False)
		profile.user = user
		profile.save()
		return redirect('login')
	contexto = {
		'form': form,
		'form_profile': form_profile
	}
	return render(request, 'registro.html', contexto)

#Views de registro de Usuário
@login_required
def dados(request, id):
	user = User.objects.get(pk=id)
	form = UserCreationForm(request.POST or None, instance=user)
	if form.is_valid():
		form.save()
		return redirect('perfil')
	contexto = {
		'form': form
	}
	return render(request, 'registro.html', contexto)


#Views de Area

def areas_listar(request):
	areas = Areas.objects.all()
	contexto = {
		'lista_areas': areas
	}
	return render(request, 'areas.html', contexto)

def area_cadastrar(request):
	form = AreasForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('areas')
	form = AreasForm()
	contexto = {
		'form' : form
	}
	return render(request, 'area_cadastro.html', contexto)

def area_atualizar(request, id):
	area = Areas.objects.get(pk=id)
	form = AreasForm(request.POST or None, instance=area)
	if form.is_valid():
		form.save()
		return redirect('areas')
	contexto = {
		'form': form
	}
	return render(request, 'area_cadastro.html', contexto)

def area_remover(request, id):
	area = Areas.objects.get(pk=id)
	area.delete()
	return redirect('areas')


#Views de Publico

def publicos_listar(request):
	publicos = Publicos.objects.all()
	contexto = {
		'publicos_lista': publicos
	}
	return render(request, 'publicos.html', contexto)

def publico_cadastrar(request):
	form = PublicosForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('publicos')
	contexto = {
		'form': form
	}
	return render(request, 'publico_cadastro.html', contexto)

def publico_atualizar(request, id):
	publico = Publicos.objects.get(pk=id)
	form = PublicosForm(request.POST or None, instance=publico)
	if form.is_valid():
		form.save()
		return redirect('publicos')
	contexto = {
		'form': form
	}
	return render(request, 'publico_cadastro.html', contexto)

def publico_remover(request, id):
	publico = Publicos.objects.get(pk=id)
	publico.delete()
	return redirect('publicos')

#Views de Curso

def cursos_listar(request):
	cursos = Cursos.objects.all()
	contexto = {
		'cursos_listar': cursos
	}
	return render(request, 'cursos.html', contexto)

def curso_cadastrar(request):
	form = CursosForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('cursos')
	contexto = {
		'form': form
	}
	return render(request, 'curso_cadastrar.html', contexto)

def curso_atualizar(request, id):
	curso = Cursos.objects.get(pk=id)
	form = CursosForm(request.POST or None, request.FILES or None, instance=curso)
	if form.is_valid():
		form.save()
		return redirect('cursos')
	contexto = {
		'form': form
	}
	return render(request, 'curso_cadastrar.html', contexto)

def curso_remover(request, id):
	curso = Cursos.objects.get(pk=id)
	curso.delete()
	return redirect('cursos')