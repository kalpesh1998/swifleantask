from . import views
from django.urls import path


urlpatterns = [
    path('', views.post_list, name='home'),     # Front end web page view
    path('<id>/', views.post_detail, name='post_detail'),   # Enter in class detail
    path('login',views.user_login,name="user_login"),       # User login
    path('logout', views.user_logout, name='user_logout'),  # User Logout
    path('register',views.signup_view,name='signup_view'),  #User Registration
    path("api/classes/",views.ProductListView.as_view()),   # List of classes api
    path("api/classes/<int:id>",views.ProductDetailView.as_view()), # task of classes api
    path("api/<int:id>",views.UserDetailView.as_view()),# User Api

]