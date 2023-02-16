from django.shortcuts import render, get_object_or_404

# Create your views here.
from animals.models import Animals
from comment.models import Comment
from comment.forms import CommentForm


def animals_list_view (request):
    animals=Animals.objects.filter(published=True)
    context={"animals_list": animals,'page':'animals'}
    return render(request, "animals/animals_list.html",context)

def animals_id_view(request, pk):
    pk = get_object_or_404(Animals, pk=pk)
    context = {"pk": pk,'page':'animals'}
    comments = Comment.objects.filter(animals = pk, published=True)
    if request.method=="POST": 
         form = CommentForm(request.POST) 
         if form.is_valid(): 
           comment =  form.save(commit=False) 
           comment.animals = pk 
           comment.save() 
           form = CommentForm() 
    else:
        form = CommentForm()
    context = {"pk": pk,'page':'animals', 'comments_list':comments, 'form':form}
    return render(request, "animals/animals_id.html", context)
