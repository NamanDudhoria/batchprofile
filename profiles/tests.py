from django.test import TestCase
from django.utils import timezone
from .models import CustomUser, Project, Domain, PlacementActivity

class DomainModelTest(TestCase):
    def setUp(self):
        self.domain = Domain.objects.create(name="Finance")

    def test_domain_creation(self):
        self.assertEqual(self.domain.name, "Finance")
        self.assertEqual(str(self.domain), "Finance")

class CustomUserModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username="testuser",
            password="password123",
            first_name="Test",
            last_name="User",
            email="testuser@example.com"
        )
        self.domain = Domain.objects.create(name="Finance")
        self.user.domains.add(self.domain)

    def test_user_creation(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.get_full_name(), "Test User")
        self.assertEqual(self.user.email, "testuser@example.com")
        self.assertIn(self.domain, self.user.domains.all())

class ProjectModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username="testuser",
            password="password123"
        )
        self.domain = Domain.objects.create(name="Finance")
        self.project = Project.objects.create(
            user=self.user,
            title="Test Project",
            description="This is a test project.",
            project_url="http://example.com",
            completed_date=timezone.now(),
            verification_status=True
        )
        self.project.domains.add(self.domain)

    def test_project_creation(self):
        self.assertEqual(self.project.title, "Test Project")
        self.assertEqual(self.project.description, "This is a test project.")
        self.assertEqual(self.project.project_url, "http://example.com")
        self.assertTrue(self.project.verification_status)
        self.assertIn(self.domain, self.project.domains.all())

class PlacementActivityModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username="testuser",
            password="password123"
        )
        self.activity = PlacementActivity.objects.create(
            user=self.user,
            title="Test Activity",
            description="This is a test activity.",
            activity_type="project",
            points=10,
            completed_date=timezone.now(),
            verification_status=True
        )

    def test_activity_creation(self):
        self.assertEqual(self.activity.title, "Test Activity")
        self.assertEqual(self.activity.description, "This is a test activity.")
        self.assertEqual(self.activity.activity_type, "project")
        self.assertEqual(self.activity.points, 10)
        self.assertTrue(self.activity.verification_status)
        self.assertEqual(str(self.activity), "Test Activity (Project Submission)")