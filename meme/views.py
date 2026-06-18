from django.shortcuts import render, redirect, get_object_or_404
from .models import Meme
from .forms import MemeForm, ContactForm
from django.core.paginator import Paginator
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def main(request):
    memes = Meme.objects.all().order_by('-likes', '-created_at')

    paginator = Paginator(memes, 6) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'meme/main.html', {
        'page_obj': page_obj
    })

@login_required
def add_meme(request):
    if request.method == 'POST':
        form = MemeForm(request.POST, request.FILES)

        if form.is_valid():
            meme = form.save(commit=False)
            meme.created_by = request.user
            meme.save()
            return redirect('main')
    else:
        form = MemeForm()

    return render(request, 'meme/add_meme.html', {'form': form})

@login_required
def delete_meme(request, meme_id):
    meme = get_object_or_404(Meme, id=meme_id)

    if meme.created_by != request.user:
        return redirect('main')

    if request.method == "POST":
        meme.delete()
        return redirect('main')

    return render(request, 'meme/confirm_delete.html', {'meme': meme})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'meme/contacts.html', {'form': form})

@login_required
def like_meme(request, pk):
    meme = get_object_or_404(Meme, pk=pk)

    if request.user in meme.likes.all():
        meme.likes.remove(request.user)
    else:
        meme.likes.add(request.user)

    return redirect('main')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('main')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})