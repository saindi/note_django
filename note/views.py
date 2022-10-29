from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from note.models import NoteModel
from note_django.utils import UserCreateThisNoteRequiredMixin, SendMail
from note.tasks import send_spam_email


class NoteListView(ListView):
    model = NoteModel
    template_name = 'note/note_list.html'
    context_object_name = 'object_list'


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = NoteModel
    template_name = 'note/note_create.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        instance = form.save(commit=False)

        instance.user = self.request.user
        instance.save()

        SendMail.user_create_note(instance)

        return super().form_valid(form)


class NoteUpdateView(LoginRequiredMixin, UserCreateThisNoteRequiredMixin, UpdateView):
    model = NoteModel
    template_name = 'note/note_update.html'
    fields = ['title', 'content']
    pk_url_kwarg = 'note_id'

    def form_valid(self, form):
        instance = form.save(commit=False)

        SendMail.user_update_note(instance)

        return super().form_valid(form)


class NoteDeleteView(LoginRequiredMixin, UserCreateThisNoteRequiredMixin, DeleteView):
    model = NoteModel
    template_name = 'note/note_delete.html'
    pk_url_kwarg = 'note_id'
    success_url = reverse_lazy("user:profile")

    def form_valid(self, form):
        super().form_valid(form)

        SendMail.user_delete_note(self.object)


        return redirect(self.success_url)
