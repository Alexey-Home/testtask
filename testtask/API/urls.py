from django.urls import path


from.views import *

urlpatterns = [
    path("", ApiHome.as_view(), name='home'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('product/<int:pk>', ProductsShow.as_view(), name='product'),
    path('video/<int:pk>', VideoShow.as_view(), name='video'),
]