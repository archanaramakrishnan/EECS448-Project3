from django.test import TestCase

# Create your tests here.
from myapp.models import Post

class PostTestCase(TestCase):

    def setUp(self):
        Post.objects.create(user_name='John Doe', title='Hi', text='Hi there')
        Post.objects.create(user_name='Jane Doe', title='Bye', text='Goodbye')



    def test_created_post_form(self):
        """
        Method `__str__` should be equal to title field
        """
        print("\n")
        f1 = Post.objects.get(title='Hi')
        self.assertEqual(str(f1), f1.title)
        f2 = Post.objects.get(title='Bye')
        self.assertEqual(str(f2), f2.title)
        print("PASSED: Post object created with title 'Hi' and 'Bye'")
        
