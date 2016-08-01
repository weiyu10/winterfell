from winterfell.tests import FunctionalTest


# TODO clean up test environment
class TestUserController(FunctionalTest):

    def test_get(self):
        response = self.app.get('/user')
        assert response.status_int == 200

    def test_create_and_delete_user(self):
        # create user
        create_result = self.app.post('/user/test_user')
        assert create_result.status_int == 201

        # delete user
        delete_result = self.app.delete('/user/test_user')
        assert delete_result.status_int == 204
