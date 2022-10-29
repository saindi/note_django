from django.urls import path
from note import views


app_name = 'note'

urlpatterns = [
    path('', views.NoteListView.as_view(), name='list'),
    path('create/', views.NoteCreateView.as_view(), name='create'),
    path('update/<int:note_id>', views.NoteUpdateView.as_view(), name='update'),
    path('delete/<int:note_id>', views.NoteDeleteView.as_view(), name='delete'),
]
