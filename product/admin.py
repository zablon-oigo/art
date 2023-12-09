from django.contrib import admin
from .models import Category, Product, Exhibition,ArtSize,Testimonial


admin.site.register(ArtSize)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','available','created','updated']
    list_filter=['available','created','updated']
    list_editable=['price','available']
    prepopulated_fields={'slug':('name',)}
    


@admin.register(Exhibition)
class ExhibitionAdmin(admin.ModelAdmin):
    list_display=['title','venue','price','start_time','end_time','date']
    list_editable=['start_time','end_time','date']
    list_filter=['publish',]



@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display=['name','created']
    list_filter=['created',]