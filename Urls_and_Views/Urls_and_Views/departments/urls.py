from django.urls import path, include

from Urls_and_Views.departments import views

urlpatterns = [
    path('', views.index, name='home'),
    path('numbers/', include([
        path('<int:pk>/', views.view_with_int_pk),
        path('<int:pk>/<slug:slug>/', views.view_with_slug),
    ])),
    path('softuni/', views.redirect_to_softuni),
    path('redirect_to_view/', views.redirect_to_view),
    path('<str:variable>/', views.view_with_name),
    # path('<path:variable>/', views.view_with_name), - vsichko zaedno sus / e path
    path('<param>/', views.view_with_args_kwargs),

]
