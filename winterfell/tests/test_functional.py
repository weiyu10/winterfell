from winterfell.tests import FunctionalTest


# TODO clean up test environment
class TestUserController(FunctionalTest):

    def test_get(self):
        response = self.app.get('/user')
        assert response.status_int == 200

    def test_create_user(self):
        # response = self.app.post('/user', params={'username': 'test_user'})
        response = self.app.post('/user/test_user')
        assert response.status_int == 201

    def test_delete_user(self):
        response = self.app.delete('/user/test_user')
        assert response.status_int == 204
