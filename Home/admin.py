from django.contrib import admin
from django.utils.html import format_html
from django.conf import settings
from Home.models import SEO_tag,Type_words,Description,Fact,Service,Skill,Testimonial

# Register your models here.
class SEO_TAGAdmin(admin.ModelAdmin):
    list_display = ('title','date')
    search_fields = ('title','date')

class TypedWordsAdmin(admin.ModelAdmin):
    list_display = ('tags','date')

class DescriptionAdmin(admin.ModelAdmin):
    list_display = ('title','date')
    search_fields = ('title','date')

class FactAdmin(admin.ModelAdmin):
    list_display = ('title','count','date')
    search_fields = ('title','date')

class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill','date')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title','date')

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('image_preview','name','occupation','date')
    search_fields = ('name','occupation','date')
   
    def image_preview(self, obj):
        if obj.image:
            image_url = settings.STATIC_URL + 'assets/img/testimonials/' + obj.image
            return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;" />', image_url)
        else:
            return 'No Image'

admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Fact, FactAdmin)
admin.site.register(Description, DescriptionAdmin)
admin.site.register(Type_words, TypedWordsAdmin)
admin.site.register(SEO_tag, SEO_TAGAdmin)
