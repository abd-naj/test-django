from django.contrib import admin
from .models import Login, Personal ,Contact ,Academy ,Wishlist ,Document

# Register your models here.
class LoginAdmin(admin.ModelAdmin):
    list_display = [ 'email' , 'password' ]
class PagesAdmin(admin.ModelAdmin):
    list_display = ['name' , 'ratio' , 'placeofpirth' , 'dataofbirth' , 'namefather' , 'mothername' , 'gender' , 'status']
class ContactAdmin(admin.ModelAdmin):
    list_display = [ 'email' , 'phone' , 'name' , 'website' ]
class AcademyAdmin(admin.ModelAdmin):
    list_display = [ 'modified' , 'elementaryschool' , 'preparatoryschool' , 'highschool' , 'certificatedate' , 'certificatesource' ]
class WishlistAdmin(admin.ModelAdmin):
    list_display = [ 'name' , 'ratio' , 'placeofbirth' , 'dateofbirth' , 'gender' , 'fathersnameandlineage' , 'mothersnameandlineage' , 'status' , 'firstwish' , 'secondwish' , 'thirdwish' , 'fourthwish' ]



admin.site.register(Login ,LoginAdmin)
admin.site.register(Personal ,PagesAdmin)
admin.site.register(Contact ,ContactAdmin)
admin.site.register(Document )
admin.site.register(Academy ,AcademyAdmin)
admin.site.register(Wishlist ,WishlistAdmin)


admin.site.site_header = 'بيانات المسجلين على المفاضلة'
admin.site.site_title = 'trade-off registration'
