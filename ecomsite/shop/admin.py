from django.contrib import admin
from .models import products, orders

admin.site.site_header = "Ecommerce Dashboard"
admin.site.index_title = "Amazon Shopping"
admin.site.site_title = "Amazon"


class poductAdmin(admin.ModelAdmin):

    def change_category_to_default(self, request, queryset):
        queryset.update(category="Default")

    change_category_to_default.short_description = "Default Category"

    list_display = ('id', 'title', 'description', 'price', 'discounted_price', 'category')
    search_fields = ('title', 'category')
    actions = ('change_category_to_default',)
    # fields = ('title', 'description', 'price', 'discounted_price', 'category')
    list_editable = ('price', 'category')

    

class orderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'created_at', 'city', 'state', 'zip', 'id')
    search_fields = ('name', 'email', 'phone', 'city', 'state', 'zip', 'id')



# Register your models here.
admin.site.register(products, poductAdmin)
admin.site.register(orders, orderAdmin)