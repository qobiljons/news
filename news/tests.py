from django.test import TestCase
from django.urls import reverse
from .models import Post

# Create your tests here.


class PostModelTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title="News", body="News Body")

    def test_text_content(self):
        post = Post.objects.get(id=self.post.id)
        self.assertEqual(post.title, "News")
        self.assertEqual(post.body, "News Body")


class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(title="Theme 2", body="There 2 Text")

    def test_views_url_exist_at_proper_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

