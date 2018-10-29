from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="login-page"),
    path("about/", views.about, name="about-page"),
    path("index/", views.index, name="index-page"),
    path("tables/", views.tables, name="table-page"),
    path("charts/", views.charts, name="charts-page"),
    path("forgot-password/", views.forgot, name="forgotPassword-page")

]
