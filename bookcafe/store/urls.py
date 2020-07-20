from django.urls import path
from . import views

urlpatterns = [

        path('',views.store,name='store'),
        path('seller',views.seller,name='seller'),
        path('category',views.category,name='category'),
        path('search',views.search,name='search'),
        path('more',views.more,name='more')
]
