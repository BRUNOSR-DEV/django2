# para um melhor projeto

# cada app tem suas rotas (urls)

from django.urls import path

# .views - desse módulo core no arquivo views
from .views import index, contato, produto

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('produto', produto, name='produto'),
]

