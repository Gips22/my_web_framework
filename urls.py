from src.urls import Url
from views import Home


urlpatterns = [
    Url('/', Home),
    Url('/favicon.ico', Home)
]


