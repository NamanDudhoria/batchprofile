from django.test import TestCase
from .models import Article, Comment

class ArticleModelTest(TestCase):

    def setUp(self):
        self.article = Article.objects.create(
            title="Test Article",
            content="This is a test article.",
            author="Test Author"
        )

    def test_article_creation(self):
        self.assertEqual(self.article.title, "Test Article")
        self.assertEqual(self.article.content, "This is a test article.")
        self.assertEqual(self.article.author, "Test Author")
        self.assertIsNotNone(self.article.published_date)

class CommentModelTest(TestCase):

    def setUp(self):
        self.article = Article.objects.create(
            title="Test Article",
            content="This is a test article.",
            author="Test Author"
        )
        self.comment = Comment.objects.create(
            article=self.article,
            author="Comment Author",
            content="This is a test comment."
        )

    def test_comment_creation(self):
        self.assertEqual(self.comment.article, self.article)
        self.assertEqual(self.comment.author, "Comment Author")
        self.assertEqual(self.comment.content, "This is a test comment.")
        self.assertIsNotNone(self.comment.created_date)
# Create your tests here.
