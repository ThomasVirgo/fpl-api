from django.urls import path
from . import views

urlpatterns = [
    path('fixtures/', views.Fixtures.as_view()),
    path('bulk/', views.BulkData.as_view()),
    path('fixtures/team/<int:tid>/', views.TeamFixtures.as_view()),
    path('teams/', views.Teams.as_view())
]