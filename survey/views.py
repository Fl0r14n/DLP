from django.shortcuts import render

from django.http import HttpResponseRedirect
from survey import models as sm

def home(request):
    return HttpResponseRedirect('survey/')

def show_forms(request):
    forms = sm.Form.objects.all()
    return render(request,'forms.html',{'forms': forms})    

def fill_form(request, form_id):
    max_score = [0]    
    
    def get_answers(question):
        answers = []
        for answer in question.answer_set.all():
            answers.append((answer.text, answer.score))
            if answer.score > 0:
                max_score[0] += answer.score
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
            section_number = section.section_number                
            if section_number not in result:
                result[section_number] = []
            result[section_number].append(get_question(section))
        return result    
    
    def get_form():
        result = {}    
        form = sm.Form.objects.get(pk=form_id) 
        result['name'] = form.name
        result['description'] = form.description        
        result['sections'] = get_sections(form) 
        result['max_score'] = max_score[0]
        return result
        
    if request.method != 'POST':    
        return render(request, 'form.html', {'form':get_form()})
    else:
        score = 0
        for val in request.POST:
            if val.startswith('c_'):
                score += int(request.POST[val])
        result = sm.Result.objects.create(
            form = sm.Form.objects.get(pk=form_id), 
            participant = request.POST.get('name', ''),
            target_score = request.POST.get('max_score', 0),
            score = score,            
        )         
        return render(request, 'result.html', {'result': result})

def show_results(request, form_id):
    if form_id:
        results = sm.Result.objects.filter(form_id=form_id)
    else:    
        results = sm.Result.objects.all();
    return render(request, 'results.html', {'results': results})