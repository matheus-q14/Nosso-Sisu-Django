from django.urls import path

from . import views

urlpatterns = [
    path("user/<int:user_id>/", views.home_page, name="home_page"),
    path(
        "user/<int:user_id>/course/choice",
        views.processCourseChoice,
        name="process",
    ),
    path("user/logout", views.logout_user, name="logout"),
]
