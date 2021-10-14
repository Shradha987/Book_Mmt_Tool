from books.views import *
from rest_framework.routers import SimpleRouter

router=SimpleRouter()
router.register('/',BooksOperations)
urlpatterns=router.urls