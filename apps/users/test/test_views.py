from .test_setup import TestSetup


class TestViews(TestSetup):

    def test_user_cannot_register_without_data(self):
        response = self.client.post(self.create_url)
        self.assertEqual(response.status_code, 400)

    def test_user_can_register(self):
        response = self.client.post(self.create_url,
                                    self.user_data,
                                    format='json')
        self.assertEqual(response.data['username'], self.user_data['username'])
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(response.data), 2)

    def test_user_cannot_register_twice(self):
        response = self.client.post(self.create_url,
                                    self.user_data,
                                    format='json')
        second_response = self.client.post(self.create_url,
                                           self.user_data,
                                           format='json')
        self.assertEqual(second_response.status_code, 400)
