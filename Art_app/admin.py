from django.contrib import admin
from .models import ArtistsContent,Artist,Orders,OrderUpdate
# Register your models here.

admin.site.register(ArtistsContent)
admin.site.register(Artist)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
