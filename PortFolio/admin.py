from django.contrib import admin
from .models import PortfolioDetails , Portfolio
from django.utils.html import format_html

class PortfolioDetailsAdmin(admin.ModelAdmin):
    list_display = ('portfolio_name', 'portfolio_client', 'portfolio_project_date')
    search_fields = ('portfolio_name', 'portfolio_client')
    list_filter = ('portfolio_client',)
    
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('portfolio_image_preview','date', 'portfolio_category')
    search_fields = ('portfolio_name','date', 'portfolio_category',)
    list_filter = ('portfolio_category','date')
    
    def portfolio_image_preview(self, obj):
        if obj.portfolio_image:
            return format_html('<img src="{}" height="120px" />', obj.portfolio_image.url)
        else:
            return format_html('<p>No image</p>')

    portfolio_image_preview.short_description = 'Portfolio Image'

admin.site.register(Portfolio,PortfolioAdmin)
admin.site.register(PortfolioDetails, PortfolioDetailsAdmin)
