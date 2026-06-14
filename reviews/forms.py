from django import forms

class ReviewForm(forms.Form):
    nickname = forms.CharField(max_length=50)
    email = forms.EmailField()
    stars = forms.IntegerField(min_value=1, max_value=5)
    text = forms.CharField(widget=forms.Textarea)