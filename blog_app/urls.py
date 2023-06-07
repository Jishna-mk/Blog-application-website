from django.urls import path
from. import views
# from .views import like_post, dislike_post

urlpatterns = [
    path("",views.first,name="first"),
    path("signup",views.signup,name="signup"),
    path("signin",views.signin,name="signin"),
    path("signout",views.signout,name="signout"),
    path("add_blog",views.add_blog,name="add_blog"),
    path("my_blog",views.my_blog,name="my_blog"),
    path("delete_page/<int:bid>",views.delete_page,name="delete_page"),
    # path("user/like_post/<int:bid>/<int:Likes>/",views.like_post,name="like_post"),
    path("my_view",views.my_view,name="my_view"),
    path("user/like_post/<int:bid>/", views.like_post, name="like_post"),

    # path('post/<int:post_id_id>/like/', like_post, name='like_post'),
    # path('post/<int:post_id>/dislike/', dislike_post, name='dislike_post'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('index',views.index,name='index'),
]