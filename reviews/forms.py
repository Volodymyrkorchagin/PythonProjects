from django import forms

class ReviewForm(forms.Form):
    nickname = forms.CharField(max_length=50)
    rating = forms.IntegerField(min_value=0, max_value=100)
    review = forms.CharField(widget=forms.Textarea)
    spoilers = forms.BooleanField(required=False)