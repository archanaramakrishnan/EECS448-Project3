from django.test import TestCase

# Create your tests here.
from myapp.models import Post

class PostTestCase(TestCase):

    def setUp(self):
        Post.objects.create(user_name='John Doe', title='What motivates you to keep going', text='Talking to upper classmen, talking to my family')
        Post.objects.create(user_name='Jane Doe', title='Best part about EECS 268', text='You get to learn A LOT. But no sleep!!')

    def test_created_post_form(self):
        """
        Method `__str__` should be equal to title field
        """
        print("\n")
        f1 = Post.objects.get(title='What motivates you to keep going')
        self.assertEqual(str(f1), f1.title)
        f2 = Post.objects.get(title='Best part about EECS 268')
        self.assertEqual(str(f2), f2.title)
        print("PASSED: Post object created with title 'What motivates you to keep going'")
        print("PASSED: Post object created with title 'Best part about EECS 268'")
