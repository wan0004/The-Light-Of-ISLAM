from django.contrib import admin
from .models import Participant
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin


class ParticipantAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    fieldsets = [
        (
            'Participants', {
                'fields':[
                    'name', 'sex', 'dob', 'address', 'aadhar_no', 'phone_no', 
                ]     
            }
        ),
    ]

    list_display = ['name', 'sex', 'address']
    list_filter = ('sex',)



admin.site.register(Participant, ParticipantAdmin)


admin.site.unregister(Group)
admin.site.site_header = 'The Light Of Islam'
admin.site.site_title = 'The Light Of Islam'
admin.site.index_title = 'Light Of Islam Administrator'