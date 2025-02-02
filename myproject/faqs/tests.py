from django.test import TestCase
from .models import FAQ

class FAQTestCase(TestCase):
    def setUp(self):
        FAQ.objects.create(question="What is Django?", answer="A web framework")

    def test_translation(self):
        faq = FAQ.objects.first()
        self.assertEqual(faq.get_translated_question('en'), "What is Django?")


