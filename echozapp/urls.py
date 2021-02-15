from django.urls import path
from . import views
urlpatterns = [
    path('map/', views.map, name='map'),
    path('mapmy/', views.mapmy, name='mapmy'),
    path('index/', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('mypage/', views.mypage, name='mypage'),
    path('What/', views.What, name='What'),
    path('What2/', views.What2, name='What2'),
    path('How/', views.How, name='How'),
    path('Where/', views.Where, name='Where'),
    path('Board/', views.Board, name='Board'),
    path('Boardwrite/', views.Boardwrite, name='Boardwrite'),
    path('Boardview/', views.Boardview, name='Boardview'),
    path('Boardupdate/', views.Boardupdate, name='Boardupdate'),
    path('Boarddel/', views.Boarddel, name='Boarddel'),
    path("search1/", views.Board, name="search1"),
    path("search2/", views.Board, name="search2"),
    path("search1/<name>", views.search1, name="search1"),
    path("search2/<content>", views.search2, name="search2"),
    path('Events/', views.Events, name='Events'),
    path('checklist0/', views.checklist0, name='checklist0'),
    path('checklist1/', views.checklist1, name='checklist1'),
    path('checklist2/', views.checklist2, name='checklist2'),
    path('checklist3/', views.checklist3, name='checklist3'),
    path('news1/', views.news1, name='news1'),
    path('news2/', views.news2, name='news2'),
    path('news3/', views.news3, name='news3'),
    path('news4/', views.news4, name='news4'),
    path('news5/', views.news5, name='news5'),
    path('news6/', views.news6, name='news6'),
    path('news7/', views.news7, name='news7'),
    path('news8/', views.news8, name='news8'),
    path('shop1/', views.shop1, name='shop1'),
    path('shop2/', views.shop2, name='shop2'),
    path('shop3/', views.shop3, name='shop3'),
    path('tip1/', views.tip1, name='tip1'),
    path('tip2/', views.tip2, name='tip2'),
    path('tip3/', views.tip3, name='tip3'),
    path('zero1/', views.zero1, name='zero1'),
    path('zero2/', views.zero2, name='zero2'),
    path('video1/', views.video1, name='video1'),
    path('video2/', views.video2, name='video2'),
    path('video3/', views.video3, name='video3'),
    path('video4/', views.video4, name='video4'),
    path('video5/', views.video5, name='video5'),
    path('event121/', views.event121, name='event121'),
    path('event11/', views.event11, name='event11'),
    path('event21/', views.event21, name='event21'),
    path('event1231/', views.event1231, name='event1231'),
    path('event131/', views.event131, name='event131'),


]