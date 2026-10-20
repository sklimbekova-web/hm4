from django import forms
from .models import Movie, Comment, VipSeat

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'poster', 'release_year', 'duration_minutes', 'rating', 'genres']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class VipBookingForm(forms.Form):
    seat = forms.ModelChoiceField(
        queryset=VipSeat.objects.filter(reserved_by__isnull=True),
        empty_label="Выберите свободное VIP-место",
        widget=forms.Select(attrs={'class': 'form-select'})
    )