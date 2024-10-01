
from django.urls import path
from. import views
urlpatterns = [
    path("<username>/",views.profile_views)
    # path('', home_view ,name="home"), 
    
] 