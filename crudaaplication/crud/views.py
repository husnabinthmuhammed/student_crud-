from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Category
from .forms import StudentForm

def category_students(request, category_name):
    students = Student.objects.filter(category_name__category_name=category_name)
    return render(request, 'category_students.html', {'students': students, 'category_name': category_name})

def student_list(request):
    students = Student.objects.all()
    categories = Category.objects.all()
    return render(request, 'student_list.html', {'students': students, 'categories': categories })

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'student_detail.html', {'student': student})

def student_new(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm()
    return render(request, 'student_edit.html', {'form': form})

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_edit.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return render(request, 'student_delete.html')
    #return redirect('student_list')
