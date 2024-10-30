from mi_app import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mi_app import views


urlpatterns = [
    path ('', views.HomeView.as_view(), name='index'),
    path ('about/', views.AboutView.as_view(), name='about'),
    
    path ('pasteleria/', views.PasteleriaView.as_view(), name='pasteleria'),
    path ('pasteleria/<int:pk>/', views.PasteleriaDetailView.as_view(), name='pasteleria_detail'),

    path ('bebidas/', views.BebidaView.as_view(), name='bebidas'),
    path ('bebidas/<int:pk>/', views.BebidaDetailView.as_view(), name='bebidas_detail'),


    path('pasteleria/<int:pk>/comentario/nuevo/', views.ComentariosCreateView.as_view(), name='nuevo_comentario'),
    path('comentarios/<int:pk>/delete/', views.ComentariosDeleteView.as_view(), name='delete_comentario'),
    path('comentarios/<int:pk>/update/', views.ComentariosUpdateView.as_view(), name='update_comentario'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)