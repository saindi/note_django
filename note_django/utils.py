from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from note.models import NoteModel
from note_django import settings
from django.core.mail import send_mail

from user.models import UserModel


class SendMail:
    @staticmethod
    def user_create_note(note: NoteModel) -> None:
        subject = "You create new note!"
        message = f"You note:\n{note.title}\n{note.content}"

        send_mail(subject, message, "admin@note_django.com", [note.user.email])

    @staticmethod
    def user_update_note(note: NoteModel) -> None:
        subject = "You note is update"
        message = f"You note:\n{note.title}\n{note.content}"

        send_mail(subject, message, "admin@note_django.com", [note.user.email])

    @staticmethod
    def user_delete_note(note: NoteModel) -> None:
        subject = "You note is DELETE!!!"
        message = f"You note:\n{note.title}\n{note.content}"

        send_mail(subject, message, "admin@note_django.com", [note.user.email])

    @staticmethod
    def create_new_user(user: UserModel) -> None:
        subject = "Register new acc!"
        message = "Register new acc!"

        send_mail(subject, message, "admin@note_django.com", [user.email])

    @staticmethod
    def user_logged_in(user: UserModel) -> None:
        subject = "You are logged in"
        message = "New account login " + user.username

        send_mail(subject, message, "admin@note_django.com", [user.email])


class WithoutLoginRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

        return super(WithoutLoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class UserCreateThisNoteRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        try:
            note = NoteModel.objects.get(id=kwargs['note_id'])
        except NoteModel.DoesNotExist:
            return HttpResponseRedirect(reverse_lazy('note:list'))

        if request.user != note.user:
            return HttpResponseRedirect(reverse_lazy('note:list'))

        return super(UserCreateThisNoteRequiredMixin, self).dispatch(request, *args, **kwargs)
