import unittest
from core import authors as auths


class ApiAuthors(unittest.TestCase):

    def test_get_authors_for_book(self, book_id):
        self.response = auths.get_authors_for_book(book_id)
        self.assertEqual(self.response.status_code, 200)

    def test_get_all_authors(self):
        self.response = auths.get_all_authors()
        # Esperamos que el código de respuesta del endpoint sea 200
        self.assertEqual(self.response.status_code, 200)

    def test_create_author(self, author_id, book_id, first_name, last_name):
        self.response = auths.create_author(author_id, book_id, first_name, last_name)
        self.assertEqual(self.response.status_code, 200)

    def test_delete_author(self, author_id):
        self.response = auths.delete_author(author_id)
        self.assertEqual(self.response.status_code, 200)

    def test_get_author(self, author_id):
        self.response = auths.get_author(author_id)
        self.assertEqual(self.response.status_code, 200)

    def test_update_author(self, author_id, book_id, first_name, last_name):
        self.response = auths.update_author(author_id, book_id, first_name, last_name)
        self.assertEqual(self.response.status_code, 200)

    def test_validate_status_code(self, status_code):
        code = self.response.status_code
        self.assertEqual(code, status_code)

    def test_validate_response_text(self, response_text):
        response = self.response.text
        self.assertEqual(response, response_text)


if __name__ == '__main__':
    unittest.main()
