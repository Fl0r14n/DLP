from django.db import models

# Create your models here.

def to_string(self):
    d = vars(self)
    result = ''
    for k,v in d.iteritems():
        if not k.startswith('_'):
            result += '({0} : {1}), '.format(k,v)
    return result + '\n'

class Form(models.Model):    
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)    
    creation_date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return to_string(self)
    
    class Meta:        
        ordering = ['-creation_date', 'name']

class Question(models.Model):            
    text = models.CharField(max_length=255)
    
    def __unicode__(self):
        return '{}'.format(self.text)

class Section(models.Model):
    form = models.ForeignKey(Form)    
    section_number = models.PositiveSmallIntegerField(blank=True)
    question = models.ForeignKey(Question)
    question_number = models.PositiveSmallIntegerField(blank=True)

    def __unicode__(self):
        return to_string(self)
    
    class Meta:
        ordering = ['form', 'section_number','question_number']
        
    def form_name(self):
        return self.form.name
    
    form_name.admin_order_field = 'form_name'
    
class Answer(models.Model):
    question = models.ForeignKey(Question)    
    text = models.CharField(max_length=255)
    score = models.SmallIntegerField(blank=True)
    
    def __unicode__(self):
        return to_string(self)
    
    class Meta:
        ordering = ['question', '-score']
        
    def question_name(self):
        return self.question.text
    
    question_name.admin_order_field = 'question_name'

class Result(models.Model):
    form = models.ForeignKey(Form, blank=True, null=True, on_delete=models.SET_NULL)
    participant = models.CharField(max_length=64, blank=True)    
    fill_date = models.DateTimeField(auto_now_add=True)
    target_score = models.SmallIntegerField(blank=True)
    score = models.SmallIntegerField(blank=True)    
    
    def __unicode__(self):
        return to_string(self)
    
    class Meta:
        ordering = ['participant', '-score']
        
    def form_name(self):
        return self.form.name
    
    form_name.admin_order_field = 'form_name'    