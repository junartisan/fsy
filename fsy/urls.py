from django.contrib import admin
from django.urls import path, include
from participants.views import home
admin.site.site_header = "FSY 2026 - Cebu City - Cebu Central Stake and Bogo District "
admin.site.site_title = "FSY 2026 Admin Portal"
admin.site.index_title = "FSY 2026 Admin Portal"



urlpatterns = [
    path('', include('participants.urls')),
    path('', home, name='home'), 
    path('admin/', admin.site.urls),
    #path('events/', include('events.urls')),
]
