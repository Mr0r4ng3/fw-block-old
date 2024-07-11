from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LoginView, LogoutView
from fw_block import settings, views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.Index.as_view(), name="index"),
    path("search/", views.Search.as_view(), name="search"),
    path("block/", views.Block.as_view(), name="block"),
    path("unblock/<str:ip>", views.Unblock.as_view(), name="unblock"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]

if settings.DEBUG:

    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]
