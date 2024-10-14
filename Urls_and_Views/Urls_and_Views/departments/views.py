from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect

from Urls_and_Views.departments.models import Department


# Create your views here.
def index(request):
    return HttpResponse('<h1>Hello, world. You"re at the polls index.</h1>')


def view_with_name(request, variable):  # - Should be named the same way as in urls
    # return HttpResponse(f"<h1>Variable : {variable}</h1>")
    return render(request, 'departments/name_template.html', {'variable': variable})


def view_with_args_kwargs(request, *args, **kwargs):
    return HttpResponse(f"<h1>Args : {args}, Kwargs: {kwargs}</h1>")


def view_with_int_pk(request, pk):
    department = Department.objects.get(pk=pk)
    department_name = department.name
    return HttpResponse(f"<h1>PK : {pk}, NAME: {department_name}</h1>")


def view_with_slug(request, pk, slug):
    # Variant 1
    department = Department.objects.filter(pk=pk, slug=slug)
    if not department:
        raise Http404

    return HttpResponse(f"<h1>Department Slug: {department.first()}</h1>")

    # Variant 2
    # department = get_object_or_404(Department, pk=pk, slug=slug)

    # Variant 3
    # return HttpResponseNotFound()

    # return HttpResponse(f"<h1>Department Slug: {department}</h1>")


def redirect_to_softuni(request):
    return redirect('https://softuni.bg')


def redirect_to_view(request):
    # option 1 - return redirect('http://localhost:8000/') - breaks abstraction
    # option 2 - return redirect(index) breaks Single Responsibility if view is from another app
    return redirect('home')  # - best option
