from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Movie, Genre, Comment, VipSeat
from .forms import MovieForm, CommentForm

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'CineBoard/register.html'
    success_url = reverse_lazy('login')

class MyLoginView(LoginView):
    template_name = 'CineBoard/login.html'

    def get_default_redirect_url(self):
        return reverse_lazy('profile')

class MyLogoutView(LogoutView):
    next_page = reverse_lazy('movie_list')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'CineBoard/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vip_seat'] = VipSeat.objects.filter(reserved_by=self.request.user).first()
        return context

class MovieListView(ListView):
    model = Movie
    template_name = 'CineBoard/movie_list.html'
    context_object_name = 'movies'

    def get_queryset(self):
        films = Movie.objects.all()
        search_text = self.request.GET.get('q')
        if search_text:
            films = films.filter(title__icontains=search_text)
        genre_slug = self.request.GET.get('genre')
        if genre_slug:
            films = films.filter(genres__slug=genre_slug)
        return films

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Genre.objects.all()
        return context

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'CineBoard/movie_detail.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['vip_seats'] = VipSeat.objects.all()
        context['user_vip_seat'] = (
            VipSeat.objects.filter(reserved_by=self.request.user).first()
            if self.request.user.is_authenticated
            else None
        )
        return context

class MovieCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'CineBoard/movie_form.html'
    success_url = reverse_lazy('movie_list')

    def test_func(self):
        return self.request.user.is_staff

class MovieUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'CineBoard/movie_form.html'
    success_url = reverse_lazy('movie_list')

    def test_func(self):
        return self.request.user.is_staff

class MovieDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Movie
    template_name = 'CineBoard/movie_confirm_delete.html'
    success_url = reverse_lazy('movie_list')

    def test_func(self):
        return self.request.user.is_staff

class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        movie_id = self.kwargs['pk']
        current_movie = Movie.objects.get(id=movie_id)
        form.instance.movie = current_movie
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('movie_detail', kwargs={'pk': self.kwargs['pk']})

class VipBookingView(LoginRequiredMixin, View):
    def post(self, request, seat_id):
        user = request.user
        already_booked = VipSeat.objects.filter(reserved_by=user).exists()
        if already_booked:
            return redirect('movie_list')
        seat = VipSeat.objects.get(id=seat_id)
        if seat.reserved_by is None:
            seat.reserved_by = user
            seat.save()
        return redirect('movie_list')