from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = "App"

urlpatterns = [
    path("", views.index, name="Home"),
    path("about/", views.about, name="About"),
    path("features/", views.features, name="Features"),
    path("news/", views.news, name="News"),
    path("contact/", views.contact, name="Contact"),
    path("team/", views.team, name="Team"),
    path("signup/", views.signup, name="Signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="Logout"),
    path('tour/', views.tour, name="Tour"),
    path('articles/', views.articles, name="Articles"),
    path('hotels/', views.hotels, name="Hotels"),
    path('hotels/<int:hotel_id>', views.allhotels, name="AllHotels"),
    path('places/', views.places, name="Places"),
    path('places/<int:place_id>', views.allplaces, name="AllPlaces"),
    path('search/', views.search, name="Search"),
    path('search/places/<int:place_id>', views.search_places, name="SearchPlaces"),
    path('search/hotels/<int:hotel_id>', views.search_hotels, name="SearchHotels"),
    path('faq/', views.faq, name="Faq"),
    path('support/', views.support, name="Support"),
    path('terms/', views.terms, name="Terms"),
    path('privacy/', views.privacy, name="Privacy"),
]
