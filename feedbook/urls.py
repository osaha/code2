from django.urls import path
from .views import BookRequestListView, BookRequestDetailView, BookDataCreateView
from . import views
urlpatterns = [
    path('', views.top, name='top'),
    path('list/', BookRequestListView.as_view(), name='list'),
    path('detail/<int:pk>', BookRequestDetailView.as_view(),name='detail'),
    path('create/', BookDataCreateView.as_view(),name='create'),
]