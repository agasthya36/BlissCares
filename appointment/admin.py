from django.contrib import admin

# Register your models here.
from .models import Appointment
from .models import Doctors
from .models import Consultation
from .models import Post
from .models import Comment
admin.site.register(Appointment)
admin.site.register(Consultation)
admin.site.register(Doctors)
admin.site.register(Post)
admin.site.register(Comment)