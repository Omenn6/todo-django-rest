from django.test import TestCase
from django.contrib.auth import get_user_model


from tasks.models import Category, Label, Task, Comment


User = get_user_model()


class TaskModelsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="pavel", password="qwe321")
        self.category = Category.objects.create(name="Work")
        self.label = Label.objects.create(name="Important")

    def test_user_creation(self):
        self.assertEqual(str(self.user), "pavel")

    def test_category_creation(self):
        self.assertEqual(str(self.category), "Work")

    def test_label_creation(self):
        self.assertEqual(str(self.label), "Important")

    def test_task_creation(self):
        task = Task.objects.create(
            title="My Task",
            description="Test description",
            owner=self.user,
            category=self.category
        )
        task.labels.add(self.label)

        self.assertEqual(task.title, "My Task")
        self.assertEqual(task.owner.username, "pavel")
        self.assertEqual(task.category.name, "Work")
        self.assertEqual(task.labels.count(), 1)
        self.assertEqual(str(task), "My Task")

    def test_comment_creation(self):
        task = Task.objects.create(title="Task for comment", owner=self.user)

        comment = Comment.objects.create(
            text="Test Comment",
            task=task,
            author=self.user,
        )

        self.assertEqual(comment.text, "Test Comment")
        self.assertEqual(comment.task.title, "Task for comment")
        self.assertEqual(comment.author.username, "pavel")
        expected_str = f"Comment by {self.user} on {task}"
        self.assertEqual(str(comment), expected_str)
