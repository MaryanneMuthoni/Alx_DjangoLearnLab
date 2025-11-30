from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book, Author
from datetime import date

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create users
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Create authors
        self.author1 = Author.objects.create(name="Author One")
        self.author2 = Author.objects.create(name="Author Two")

        # Create books
        self.book1 = Book.objects.create(
            title="Book One",
            author=self.author1,
            publication_year=date(2020, 1, 1)
        )
        self.book2 = Book.objects.create(
            title="Book Two",
            author=self.author2,
            publication_year=date(2021, 6, 15)
        )

        # API client
        self.client = APIClient()

    def test_list_books(self):
        url = reverse("book-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_search_books(self):
        url = reverse("book-list") + "?search=Author One"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Book One")

    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="testpass")
        url = reverse("book-create")
        data = {
            "title": "Book Three",
            "author": self.author1.id,
            "publication_year": "2022-12-31"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.get(id=response.data["id"]).title, "Book Three")

    def test_create_book_unauthenticated(self):
        url = reverse("book-create")
        data = {
            "title": "Book Three",
            "author": self.author1.id,
            "publication_year": "2022-12-31"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        self.client.login(username="testuser", password="testpass")
        url = reverse("book-update", kwargs={"pk": self.book1.id})
        data = {
            "title": "Updated Book One",
            "author": self.author1.id,
            "publication_year": "2020-01-01"
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book One")

    def test_update_book_unauthenticated(self):
        url = reverse("book-update", kwargs={"pk": self.book1.id})
        data = {
            "title": "Updated Book One",
            "author": self.author1.id,
            "publication_year": "2020-01-01"
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_book_authenticated(self):
        self.client.login(username="testuser", password="testpass")
        url = reverse("book-delete", kwargs={"pk": self.book1.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_delete_book_unauthenticated(self):
        url = reverse("book-delete", kwargs={"pk": self.book1.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

