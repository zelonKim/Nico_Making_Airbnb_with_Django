from django.urls import path
from . import views

urlpatterns = [ # HTTP메서드: ViewSet메서드 -> 사용자가 해당 HTTP메서드를 보내면, ViewSet메서드를 실행함. 
        path("", views.CategoryViewSet.as_view(
            {  
            'get': 'list',  
            'post': 'create',
            },
        ),
    ), 
        path("<int:pk>", views.CategoryViewSet.as_view(
            {
            "get": "retrieve",
            "put": "partial_update",
            "delete": "destroy",
            },
        ),
    ),
] 


