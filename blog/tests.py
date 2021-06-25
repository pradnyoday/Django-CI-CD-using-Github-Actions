from django.test import TestCase
from .models import Post


# Create your tests here.
class ModelTesting(TestCase):
    def setUp(self) -> None:
        self.blog = Post.objects.create(title='First Post', author='Paddy', context='First Post!!', slug='First Post')

    def test_post_model(self):
        d = self.blog
        self.assertTrue(isinstance(d, Post))
        self.assertEqual(str(d), 'First Post')
