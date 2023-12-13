from django.contrib import admin

# Register your models here.
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('subject', 'content', 'create_date', 'image')
    search_fields = ['subject', 'content'] 
    class Meta:
        model = Review
        fields = ['subject', 'content', 'create_date', 'user', 'image']
        
        def __init__(self, *args, **kwargs):
            super(ReviewAdmin, self).__init__(*args, **kwargs)
            
admin.site.register(Review)

