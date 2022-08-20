from django.urls import path, include
from django.conf.urls.static import static
from project import settings
from . import views

urlpatterns = [
    path("personal", views.personal, name="personal"),
    path("contact", views.contact , name="contact"),
    path("academy", views.academy , name="academy"),
    path("document", views.document , name="document"),
    path("wishlist", views.wishlist , name="wishlist"),
    path("sgnin", views.sgnin , name="sgnin"),
    path("students", views.students ,name="students"),
    path("studentsdesirs", views.studentsdesirs ,name="studentsdesirs"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)