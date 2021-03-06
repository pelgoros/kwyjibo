from django.contrib import admin

# Register your models here.

from .models import *

class CourseAdmin(admin.ModelAdmin):
    """Utility for Django Admin tools.
    
    Util class that indicates the django admin how to order the courses when 
    listed.
    
    """
    
    ordering = ['-name',]

class StudentAdmin(admin.ModelAdmin):

    list_display = ('uid', 'user', 'get_full_name', )

class DeliveryAdmin(admin.ModelAdmin):

    list_display = ('id', 'student_uid', 'student_full_name', 'assignment_uid', 'date', 'revision_status')

    def student_uid(self, obj):
        return obj.student.uid

    def student_full_name(self, obj):
        return obj.student.get_full_name()

    def assignment_uid(self, obj):
        return obj.assignment.uid

    def revision_status(self, obj):
        return obj.revision.status

class RevisionAdmin(admin.ModelAdmin):

    list_display = ('id', 'student', 'assignment', 'date', 'exit_value', 'status')

    def student(self, obj):
        return obj.delivery.student.uid

    def assignment(self, obj):
        return obj.delivery.assignment.uid

    def date(self, obj):
        return obj.delivery.date
        
    
admin.site.register(Teacher)
admin.site.register(Course, CourseAdmin)
admin.site.register(Shift)
admin.site.register(Assignment)
admin.site.register(AssignmentFile)
admin.site.register(Script)
admin.site.register(Student, StudentAdmin)
admin.site.register(Suscription)
admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(Correction)
admin.site.register(Revision, RevisionAdmin)
