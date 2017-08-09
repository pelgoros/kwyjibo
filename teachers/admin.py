from django.contrib import admin

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    """Utility for Django Admin tools.
    
    Util class that indicates the django admin how to order the courses when 
    listed.
    
    """
    
    ordering = ['-name',]
    
admin.site.register(Teacher)
admin.site.register(Course, CourseAdmin)
admin.site.register(Shift)
admin.site.register(Practice)
admin.site.register(PracticeFile)
admin.site.register(Script)
admin.site.register(Student)
admin.site.register(Suscription)
admin.site.register(Delivery)
admin.site.register(Correction)
admin.site.register(Revision)