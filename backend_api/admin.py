from django.contrib import admin




# Register your models here.
from .models import Wood, Lighting,Appliances,Paint,Landscaping
admin.site.register(Wood)
admin.site.register(Lighting)
admin.site.register(Appliances)
admin.site.register(Paint)
admin.site.register(Landscaping)