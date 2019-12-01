from django.test import TestCase

# Create your tests here.
from myapp.models import Post
from myapp.models import Rate

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

class RateTestCase(TestCase):
    def setUp(self):
        Rate.objects.create(class_exams_num = '2', class_hw = 'Very Easy', class_comments = 'I liked the class, it was not hard')
        Rate.objects.create(class_exams_num = '5', class_hw = 'Hard to understand', class_comments = 'Pretty hard class but you learn a lot')
        Rate.objects.create(class_exams_num = '3', class_hw = 'Average', class_comments = 'Normal class, I liked it and the exams were not bad')

    def test_created_post_form(self):
        """
        Method `__str__` should be equal to title field
        """
        print("\n")
        f1 = Rate.objects.get(class_comments='I liked the class, it was not hard')
        self.assertEqual(str(f1), f1.class_comments)
        f2 = Rate.objects.get(class_comments='Pretty hard class but you learn a lot')
        self.assertEqual(str(f2), f2.class_comments)
        f3 = Rate.objects.get(class_comments='Normal class, I liked it and the exams were not bad')
        self.assertEqual(str(f3), f3.class_comments)
        print("PASSED: Rate object created with comment 'I liked the class, it was not hard'")
        print("PASSED: Rate object created with comment 'Pretty hard class but you learn a lot'")
        print("PASSED: Rate object created with comment 'Normal class, I liked it and the exams were not bad'")
