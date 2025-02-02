from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()  # WYSIWYG Editor for formatted answers
    question_hi = models.TextField(blank=True, null=True)  # Hindi question
    question_bn = models.TextField(blank=True, null=True)  # Bengali question
    answer_hi = RichTextField(blank=True, null=True)  # Hindi answer
    answer_bn = RichTextField(blank=True, null=True)  # Bengali answer

    def save(self, *args, **kwargs):
        translator = Translator()

        if not self.question_hi:
            self.question_hi = translator.translate(self.question, dest='hi').text
        if not self.question_bn:
            self.question_bn = translator.translate(self.question, dest='bn').text
        if not self.answer_hi:
            self.answer_hi = translator.translate(self.answer, dest='hi').text
        if not self.answer_bn:
            self.answer_bn = translator.translate(self.answer, dest='bn').text

        super().save(*args, **kwargs)

    def get_translated_content(self, lang='en'):
        translated_question = getattr(self, f'question_{lang}', self.question)
        translated_answer = getattr(self, f'answer_{lang}', self.answer)
        return {'question': translated_question, 'answer': translated_answer}

    def __str__(self):
        return self.question
