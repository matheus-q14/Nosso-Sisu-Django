from django.urls import path

from . import views

urlpatterns = [
    path("user/<int:user_id>/", views.home_page, name="home_page"),
    path(
        "user/<int:user_id>/course/choice",
        views.process_course_choice,
        name="process",
    ),
    path("user/create/course", views.create_course, name="create_course"),
    path("user/logout", views.logout_user, name="logout"),
]
