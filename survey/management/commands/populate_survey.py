from django.core.management.base import BaseCommand
import random
from uuid import uuid4

from survey.models import *

class Command(BaseCommand):
                  
            
    def handle(self, *args, **kwargs):
        min_forms = 10
        max_forms = 15
        min_sections_per_form = 1
        max_sections_per_form = 2
        min_questions_per_section = 2
        max_questions_per_section = 4
        min_answers_per_question = 2
        max_answers_per_question = 3
        max_value_per_answer = max_answers_per_question

        def _clean_db():
            Form.objects.all().delete()            

        def _create_forms():
            for i in range(random.randint(min_forms,max_forms)):
                form_name = 'Form number {}'.format(i)
                if bool(random.getrandbits(1)):
                    form_description = 'Just a sample description for {}'.format(form_name)
                else:
                    form_description = ''
                form = Form.objects.create(
                    name = form_name,
                    description = form_description,
                )
                _create_sections_per_form(form)                

        def _create_sections_per_form(form_obj):
            #first we create the questions
            questions = _create_questions(form_obj)
            for question in questions:
                _create_answers_per_question(question)        

            #now we create the sections            
            for i in range(random.randint(min_sections_per_form, max_sections_per_form)):
                for j in range(len(questions)):
                    question_obj = questions[j]
                    Section.objects.create(
                        form = form_obj,
                        section_number = i+1,
                        question = question_obj,
                        question_number = j+1,                
                    )

        def _create_questions(form):
            result = []
            uuid = str(uuid4())
            for i in range(random.randint(min_questions_per_section, max_questions_per_section)):
                question_text = 'Form: {} Section UUID: {} Question number {}?'.format(form.name, uuid, i+1)
                question = Question.objects.create(
                    text = question_text,
                )
                result.append(question)
            return result

        def _create_answers_per_question(question_obj):            
            for i in range(random.randint(min_answers_per_question, max_answers_per_question)):
                question_score = random.randint(0, max_value_per_answer)
                question_text = 'Answer {} with score {}?'.format(i, question_score)
                Answer.objects.create(
                    question = question_obj,
                    text = question_text,
                    score = question_score,
                )  
                
        _clean_db()
        _create_forms()