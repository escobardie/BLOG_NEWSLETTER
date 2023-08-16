from django.urls import path
from . import views

urlpatterns = [

    path('suscrip/', views.SubcriptioView.as_view(), name='suscripcion'), # SUSCRIPCION BASADA EN CLASES
    path('create_letter/', views.CreateLetterView.as_view(), name='create_letter'), # CREACION DE BOLETIN BASADA EN CLASES
        
    ################# PAGINA LISTADO DE EMAILS EN HTML #################
    path('listing_letter/', views.ListNewslatterView.as_view(), name='lista_boletin'),
    path('detail_boletin/<int:id>/',views.NewslatterDetailView.as_view(), name='detail_boletin'),
    # path('reenvio_boletin/<int:id>/',views.NewslatterUpdateView.as_view(), name='reenvio_boletin'),
    path('reenvio_boletin/<int:id>/',views.NewslatterUpdateView.as_view(), name='reenvio_boletin'),

    path('listing_emails/', views.ListEmailsView.as_view(), name='lista_emails'),
]
