from django.contrib import admin
from django.urls import path

from notes import views 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("notes/", views.NoteView.as_view(), name="notes"),
    path("notes/update/<int:note_id>/", views.update_note, name="update_note"),
    path("notes/delete/<int:note_id>/", views.delete_note, name="delete_note"),
]
