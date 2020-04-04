import unittest
from datetime import datetime
from core import books


class ApiBooks(unittest.TestCase):
    now = datetime.now()

    def test_get_all_books(self):
        self.response = books.get_all_books()
        # Esperamos que el código de respuesta del endpoint sea 200
        self.assertEqual(self.response.status_code, 200)

    def test_create_book(self, book_id, book_title, description, page_count, excerpt):
        self.response = books.create_book(book_id, book_title, description, page_count, excerpt, self.now)
        self.assertEqual(self.response.status_code, 200)

    def test_delete_book(self, book_id):
        self.response = books.delete_book(book_id)
        self.assertEqual(self.response.status_code, 200)

    def test_get_book(self, book_id):
        self.response = books.get_book(book_id)
        self.assertEqual(self.response.status_code, 200)

    def test_notfound_book(self, book_id):
        self.response = books.get_book(book_id)
        self.assertEqual(self.response.status_code, 404)

    def test_update_book(self, book_id, book_title, description, page_count, excerpt):
        self.response = books.update_book(book_id, book_title, description, page_count, excerpt, self.now)
        self.assertEqual(self.response.status_code, 200)

    def test_validate_status_code(self, status_code):
        code = self.response.status_code
        self.assertEqual(code, status_code)

    def test_validate_response_text(self, response_text):
        response = self.response.text
        self.assertEqual(response, response_text)


if __name__ == '__main__':
    unittest.main()
