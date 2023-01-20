from django.contrib import admin
from django.urls import path, include

import main.views as main_views

main_urls = [
    path('', main_views.MainView.as_view(), name='main'),
    path('main-save/', main_views.SaveDataView.as_view(), name='main-save'),
    path('main-get/', main_views.GetDataView.as_view(), name='main-get')
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(main_urls))
]
