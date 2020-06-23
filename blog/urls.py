from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import *

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('blog/', include('blog.urls')),
    path('', posts_list, name='posts_list_url'),
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('post/<str:slug>/update', PostUpdate.as_view(), name='post_update_url'),
    path('post/<str:slug>/delete', PostDelete.as_view(), name='post_delete_url'),

    path('tags/', tags_list, name='tags_list_url'),
    path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
    path('tag/<str:slug>/update/', TagUpdate.as_view(), name='tag_update_url'),
    path('tag/<str:slug>/delete/', TagDelete.as_view(), name='tag_delete_url'),

    path('scripts/', scripts_list, name='scripts_list_url'),
    path('script/create/', ScriptCreate.as_view(), name='script_create_url'),
    path('script/<str:slug>/', ScriptDetail.as_view(), name='script_detail_url'),
    path('script/<str:slug>/update/', ScriptUpdate.as_view(), name='script_update_url'),
    path('script/<str:slug>/delete/', ScriptDelete.as_view(), name='script_delete_url'),

    path('mans/', mans_list, name='mans_list_url'),
    path('man/create/', ManCreate.as_view(), name='man_create_url'),
    path('man/<str:slug>/', ManDetail.as_view(), name='man_detail_url'),
    path('man/<str:slug>/update/', ManUpdate.as_view(), name='man_update_url'),
    path('man/<str:slug>/delete/', ManDelete.as_view(), name='man_delete_url'),

    path('link/', links_list, name='links_list_url'),
]
