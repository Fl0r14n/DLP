from django.shortcuts import render

from django.http import HttpResponseRedirect
from survey import models as sm

def root(request):
    return HttpResponseRedirect('/survey/forms/')

def show_forms(request):
    forms = sm.Form.objects.all()
    return render(request,'show_forms.html',{'forms': forms})    

def fill_form(request, form_id):
    
    def get_answers(question):
        answers = []
        for answer in question.answer_set.all():
            answers.append((answer.text, answer.score))
        return answers

    def get_question(section):        
        result = {}
        question = section.question               
        result['name'] = question.text
        result['number'] = section.question_number
        result['answers'] = get_answers(question)                
        return result
    
    def get_sections(form):
        result = {}        
        for section in form.section_set.all():
            section_name = 'Section {}'.format(section.section_number)                
            if section_name not in result:
                result[section_name] = []
            result[section_name].append(get_question(section))
        return result    
    
    def get_form():
        result = {}    
        form = sm.Form.objects.get(pk=form_id) 
        result['name'] = form.name
        result['description'] = form.description    
        result['sections'] = get_sections(form) 
        #print result
        return result
        
    return render(request, 'fill_form.html',{'form':get_form()})

def submit_form(request):
    if request.method == 'POST':
        return render(request,'submit_form.html',{})
    return render(request,'submit_form.html',{})

def show_results(request):
    pass