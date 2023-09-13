from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Student

class Home(ListView):
    model = Student
    template_name = 'home.html'
    context_object_name = 'students'   

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('student_name', 'student_lastname', 'gpa')
        
    def clean_gpa(self):
        gpa = self.cleaned_data['gpa']        
        if gpa <= 0 or gpa > 5:
            raise ValidationError("GPA shall be between 0 and 5")
        return gpa

class Student_add(CreateView):
    form_class = StudentForm
    template_name = 'student_add.html'
    success_url = reverse_lazy('home')
    
    def clean(self):
        cleaned_data = super().clean()
        gpa = cleaned_data.get('gpa')
        if gpa:
            self.clean_gpa()