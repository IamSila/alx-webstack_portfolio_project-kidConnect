from django.urls import path
from .views import Base, Report, IndexView
from . import views

urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.LoginView, name='login'),
    path('base/', Base.as_view(), name='base'),
    path('report/', views.report, name='report'),
    path('reported/', views.reported, name='reportedChildren'),
    path('search/', views.search, name="search"),
    path('logout/', views.logoutView, name="logout"),
    path('customAdmin/', views.customAdmin, name="customAdmin"),
    path('customAdmin/update/<str:id>', views.updateDetails, name="update"),
    path('customAdmin/delete/<str:id>', views.delete, name="delete"),
    path('generateDetails/<str:id>', views.generateDetails, name="generateDetails"),
    path('evidence/<str:id>', views.evidence, name="evidence"),
    path('notifications/<str:id>', views.notifications, name="notifications"),
    
]