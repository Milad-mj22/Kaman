
from django.urls import path

from .views import articles, register_phone , home, under_construction, videos
from django.conf import settings
from django.conf.urls.static import static
from . import views



# urlpatterns = [
#     path('', home, name='home'),
#     path('register-phone/', register_phone, name='register_phone'),
#     # path('demo/', views.demo_view, name='demo'),

#     path('about/', views.about, name='about'),
#     path('products/', views.products, name='products'),
#     path('demo/', views.demo, name='demo'),
#     path('contact/', views.contact, name='contact'),
#     path('register-phone/', views.register_phone, name='register_phone'),


# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("products/", views.products, name="products"),
    path("demo/", views.demo, name="demo"),
    path("contact/", views.contact, name="contact"),
    path('fill-info/', views.fill_info, name='fill_info'),
    path('register-phone/', register_phone, name='register_phone'),
    path('articles/', articles, name='articles'),
    path('article/<int:id>/', views.article_detail, name='article_detail'),
    path('videos/', videos, name='videos'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

