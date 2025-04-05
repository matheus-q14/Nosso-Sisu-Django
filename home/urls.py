from django.urls import path

from . import views

urlpatterns = [
    path("user/<int:user_id>/", views.home_page, name="home_page"),
    path(
        "user/course/choice",
        views.processCourseChoice,
        name="process_choice",
    ),
]
