from django.shortcuts import render,redirect, get_object_or_404

# notes/views.py
#from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm

def index(request):
    notes = Note.objects.all().order_by('-created_at')
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NoteForm()
    return render(request, 'index.html', {'notes': notes, 'form': form})

def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('index')


def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NoteForm(instance=note)
    return render(request, 'edit.html', {'form': form, 'note': note})
