from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from note.models import NoteModel
from note_django.utils import WithoutLoginRequiredMixin
from user.forms import SignInForm, SignUpForm
from user.models import UserModel
from note_django.utils import SendMail
from django.contrib.auth import login


class UserView(LoginRequiredMixin, TemplateView):
    template_name = 'user/user.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        object_list = NoteModel.objects.filter(user=self.request.user)

        context["object_list"] = object_list

        return context


class SignInView(WithoutLoginRequiredMixin, LoginView):
    template_name = 'user/signin.html'
    form_class = SignInForm

    def form_valid(self, form):
        login(self.request, form.get_user())

        SendMail.user_logged_in(self.request.user)

        return redirect(reverse_lazy('note:list'))


class SignUpView(WithoutLoginRequiredMixin, CreateView):
    model = UserModel
    template_name = 'user/signup.html'
    form_class = SignUpForm

    def form_valid(self, form):
        form.save(commit=False)

        SendMail.create_new_user(UserModel.objects.get(username=form.cleaned_data.get('username')))

        return redirect(reverse_lazy('user:sign-in'))
