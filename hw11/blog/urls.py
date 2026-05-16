from django.urls import path
from . import views

urlpatterns = [
    # FBV 땐 views.index (함수 그대로) 적었는데,
    # CBV는 클래스라서 .as_view() 붙여야 함
    path('', views.PostList.as_view(), name='post_list'),
    # FBV 땐 path('<int:pk>/', views.detail, ...) 였음
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
]
