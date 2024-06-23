from django.contrib import admin
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
    list_display = ('name','occupation','date')
    search_fields = ('name','occupation','date')

admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Fact, FactAdmin)
admin.site.register(Description, DescriptionAdmin)
admin.site.register(Type_words, TypedWordsAdmin)
admin.site.register(SEO_tag, SEO_TAGAdmin)
