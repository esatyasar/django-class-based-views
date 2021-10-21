from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student
from django.views.generic import TemplateView, UpdateView, CreateView, DetailView, ListView
from django.urls import reverse_lazy
# Create your views here.

def home(request):
    return render(request, "fscohort/home.html")

class HomeView(TemplateView):
    template_name = "fscohort/home.html"

class StudentListView(ListView):
    model = Student
    # default template name : # app/modelname_list.html
    # this fits our template name no need to use this time
    # template_name = "fscohort/student_list.html"
    context_object_name = 'students' # default context name : object_list
    paginate_by = 10

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "fscohort/student_add.html" # default name app/modelname_form.html
    success_url = reverse_lazy("list")

class StudentDetailView(DetailView):
    model = Student
    pk_url_kwarg = 'id'
    
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "fscohort/student_update.html" # default app/modelname_form.html
    success_url = '/student_list/' #'reverse_lazy("list")
    # pk_url_kwarg = 'id'

def student_delete(request, id):
    
    student = Student.objects.get(id=id)
   
    if request.method == "POST":

    
        student.delete()
        return redirect("list")
    
    context= {
        "student":student
    }
    return render(request, "fscohort/student_delete.html",context)