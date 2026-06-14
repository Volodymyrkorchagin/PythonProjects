from django.shortcuts import render
from .forms import ReviewForm

def review(request):
    result = None

    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            result = form.cleaned_data
    else:
        form = ReviewForm()

    return render(request, 'reviews/review.html', {
        'form': form,
        'result': result
    })