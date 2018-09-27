from django.contrib import admin
from .models import Job

### the code below will show the Job class in the admin interface
### if you don't want this to show the admin interface, delete the code
admin.site.register(Job)

