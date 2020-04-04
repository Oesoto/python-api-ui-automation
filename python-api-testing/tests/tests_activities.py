import unittest
from datetime import datetime
from core import activities as act


class ApiActivities(unittest.TestCase):
    now = datetime.now()

    def test_get_all_activities(self):
        self.response = act.get_all_activities()
        # Esperamos que el código de respuesta del endpoint sea 200
        self.assertEqual(self.response.status_code, 200)

    def test_get_activity(self, activity_id):
        self.response = act.get_activity(activity_id)
        self.assertEqual(self.response.status_code, 200)

    def test_notfound_activity(self, activity_id):
        self.response = act.get_activity(activity_id)
        self.assertEqual(self.response.status_code, 404)

    def test_create_activity(self, activity_id, activity_title):
        self.response = act.create_activity(activity_id, activity_title, self.now, True)
        self.assertEqual(self.response.status_code, 200)

    def test_update_activity(self, activity_id, activity_title):
        self.response = act.edit_activity(activity_id, activity_title, self.now, True)
        self.assertEqual(self.response.status_code, 200)
    
    def test_delete_activity(self, activity_id):
        self.response = act.delete_activity(activity_id)
        self.assertEqual(self.response.status_code, 200)
    
    def test_validate_status_code(self, status_code):
        code = self.response.status_code
        self.assertEqual(code, status_code)

    def test_validate_response_text(self, response_text):
        response = self.response.text
        self.assertEqual(response, response_text)


if __name__ == '__main__':
    unittest.main()