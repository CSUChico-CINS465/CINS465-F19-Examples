from django.test import TestCase
from .models import Suggestion

# Create your tests here.
class SuggestionTestCase(TestCase):
    def setUp(self):
        Suggestion.objects.create(suggestion="lion")
        Suggestion.objects.create(suggestion="cat")

    def test_suggestion_to_string(self):
        lion = Suggestion.objects.get(suggestion="lion")
        cat = Suggestion.objects.get(suggestion="cat")
        self.assertEqual(str(lion), 'lion')
        self.assertEqual(str(cat), 'cat')
