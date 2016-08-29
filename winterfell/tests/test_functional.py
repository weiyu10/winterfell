from winterfell.tests import FunctionalTest


# TODO clean up test environment
class TestUserController(FunctionalTest):

    def test_create_and_delete_user(self):
        # Create user
        create_result = self.app.post('/user/test_user',
                                      headers=self.headers)
        assert create_result.status_int == 201

        # Get user info
        user_info = self.app.get('/user/test_user',
                                 headers=self.headers)
        assert user_info.status_int == 200
        assert 'username' in user_info.namespace
        assert 'google_auth_key' in user_info.namespace

        # Delete user
        delete_result = self.app.delete('/user/test_user',
                                        headers=self.headers)
        assert delete_result.status_int == 204
