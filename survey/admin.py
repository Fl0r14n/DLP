from django.contrib import admin

# Register your models here.

class AdminForm(admin.ModelAdmin):
    list_display = ('name','description','creation_date',)
    list_filter = ('name','description','creation_date',)    

class AdminSection(admin.ModelAdmin):
    
    list_display = ('form_name', 'section_number', 'question', 'question_number',)    
    
class AdminQuestion(admin.ModelAdmin):
    list_display = ('text',)

class AdminAnswer(admin.ModelAdmin):
    list_display = ('question_name', 'score', 'text',)

class AdminResult(admin.ModelAdmin):
    list_display = ('form_name', 'participant', 'threshold', 'score',)

from survey.models import *
admin.site.register(Form, AdminForm)
admin.site.register(Section, AdminSection)
admin.site.register(Question, AdminQuestion)
admin.site.register(Answer, AdminAnswer)
admin.site.register(Result, AdminResult)