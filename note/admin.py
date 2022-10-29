from django.contrib import admin
from note.models import NoteModel


@admin.register(NoteModel)
class NoteModelAdmin(admin.ModelAdmin):
    list_display = "title", "content", "time_create", "user"

