from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from tasks.models import Task
from django.contrib.auth import get_user_model

User = get_user_model()


class TaskAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="pavel", password="qwe321")
        self.client.force_authenticate(user=self.user)
        self.url = reverse('task-list')

    def test_get_tasks_list(self):
        Task.objects.create(title="My Task", owner=self.user)

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'My Task')

    def test_create_task(self):
        data = {
            "title": "Test Task",
            "description": "Test Description",
        }

        response = self.client.post(self.url, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, "Test Task")

    def test_delete_task(self):
        task = Task.objects.create(title="Delete Me", owner=self.user)
        delete_url = reverse('task-detail', args=[task.id])

        response = self.client.delete(delete_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

    def test_search_task_by_title(self):
        Task.objects.create(title="Купить хлеб", owner=self.user)
        Task.objects.create(title="Помыть кота", owner=self.user)

        response = self.client.get(f"{self.url}?search=хлеб")

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Купить хлеб")

    def test_cannot_delete_someone_else_task(self):
        other_user = User.objects.create_user(username="Ivan", password="password123")
        other_task = Task.objects.create(title="Ivan's Task", owner=other_user)

        url = reverse('task-detail', args=[other_task.id])
        response = self.client.delete(url)

        self.assertIn(response.status_code, [status.HTTP_403_FORBIDDEN, status.HTTP_404_NOT_FOUND])

    def test_create_task_without_title_fails(self):
        data = {"description": "No title here"}
        response = self.client.post(self.url, data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
