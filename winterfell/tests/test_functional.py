import uuid
from winterfell.tests import FunctionalTest


def get_random_username(prefix):
        return prefix + str(uuid.uuid4())

def get_random_groupname(prefix):
        return prefix + str(uuid.uuid4())

# TODO clean up test environment
class TestUserController(FunctionalTest):

    def test_get_one_user(self):
        user = get_random_username('get_one_user')
        self.post_json('/users/%s' % user)

        response = self.get_json('/users/%s' % user)

        assert response.status_int == 200
        assert 'username' in response.namespace
        assert 'mail' in response.namespace
        assert 'google_auth_key' in response.namespace

    def test_get_all_user(self):
        first_user = get_random_username('get_all_user')
        second_user = get_random_username('get_all_user')
        self.post_json('/users/%s' % first_user)
        self.post_json('/users/%s' % second_user)

        response = self.get_json('/users')
        assert response.status_int == 200
        assert users in response.namespace
        # TODO check more detail users info

    def test_create_user(self):
        user = get_random_username('create_user')
        response = self.post_json('/users/%s' % user)

        assert create_result.status_int == 201

    def test_delete_user(self):
        user = get_random_username('delete_user')
        self.post_json('/users/%s' % user)
        response = self.delete_json('/users/%s' % user)

        assert response.status_int == 204

    def test_create_exist_user(self):
        user = get_random_username('exist_user')
        self.post_json('/users/%s' % user)
        response = self.post_json('/users/%s' % user)

        assert response.status_int == 304
        assert 'User %s exist' % user in create_result.body

    def test_delete_absent_user(self):
        user = get_random_username('absent_user')
        response = self.delete_json('/users/%s' % user)
        assert response.status_int == 404

    def test_change_user_info(self):
        user = get_random_username('change_user_info')
        user_mail = 'no_mail@google.com'
        self.post_json('/users/%s' % user)
        response = self.put_json('/users/%s/mail/%s' % (user, user_mail))

        assert response.status_int == 204

        # check user's mail info
        response = self.get_json('/users/%s' % user)

        assert user_mail == response.namespace['mail']


class TestgroupController(FunctionalTest):

    def test_get_all_group(self):
        first_group = get_random_groupname('get_all_group')
        second_group = get_random_groupname('get_all_group')
        self.post_json('/groups/%s' % first_group)
        self.post_json('/groups/%s' % second_group)

        response = self.get_json('/groups')
        assert response.status_int == 200
        assert groups in response.namespace

    def test_get_one_group(self):
        group = get_random_groupname('get_one_group')
        self.post_json('/groups/%s' % group)

        response = self.get_json('/groups/%s' % group)

        assert response.status_int == 200
        assert 'groupname' in response.namespace
        assert 'members' in response.namespace

    def test_create_group(self):
        group = get_random_groupname('create_group')
        response = self.post_json('/groups/%s' % group)

        assert create_result.status_int == 201

    def test_delete_group(self):
        group = get_random_groupname('delete_group')
        self.post_json('/groups/%s' % group)
        response = self.delete_json('/groups/%s' % group)

        assert response.status_int == 204

    def test_create_exist_group(self):
        group = get_random_groupname('exist_group')
        self.post_json('/groups/%s' % group)
        response = self.post_json('/groups/%s' % group)

        assert response.status_int == 304
        assert 'group %s exist' % group in create_result.body

    def test_delete_absent_group(self):
        group = get_random_groupname('absent_group')
        response = self.delete_json('/groups/%s' % group)
        assert response.status_int == 404


    def test_add_user_to_group(self):
        user = get_random_username('add_user_to_group')
        group = get_random_groupname('add_user_to_group')
        # create user and group
        self.post_json('/groups/%s' % group)
        self.post_json('/users/%s' % user)

        put_uri = '/groups/%s/users/%s' % (user, group)
        response = self.put_json(put_uri)
        assert response.status_int == 200

    def remove_user_from_group(self):
        user = get_random_username('remove_user_from_group')
        group = get_random_groupname('remove_user_from_group')
        # create user and group
        self.post_json('/groups/%s' % group)
        self.post_json('/users/%s' % user)

        delete_uri = '/groups/%s/users/%s' % (user, group)
        response = self.delete_json(delete_uri)
        assert response.status_int == 204

    def add_absent_user_to_group(self):
        user = get_random_username('absent_user')
        group = get_random_groupname('add_absent_user_to_group')
        # create user and group
        self.post_json('/groups/%s' % group)
        put_uri = '/groups/%s/users/%s' % (user, group)
        response = self.put_json(put_uri)

        assert response.status_int == 400
        assert 'User %s absent' % user in response.body

    def add_user_to_absent_group(self):
        user = get_random_username('absent_user')
        group = get_random_groupname('add_absent_user_to_group')
        # create user and group
        self.post_json('/users/%s' % user)
        put_uri = '/groups/%s/users/%s' % (user, group)
        response = self.put_json(put_uri)

        assert response.status_int == 400
        assert 'Group %s absent' % group in response.body

    def remove_absent_user_from_group(self):
        user = get_random_username('absent_user')
        group = get_random_groupname('remove_absent_user_from_group')
        # create user and group
        self.post_json('/groups/%s' % group)

        delete_uri = '/groups/%s/users/%s' % (user, group)
        response = self.delete_json(delete_uri)
        assert response.status_int == 400
        assert 'user %s absent' % user in response.body

    def remove_user_from_absent_group(self):
        user = get_random_username('remove_user_from_absent_group')
        group = get_random_groupname('absent_group')
        self.post_json('/users/%s' % user)

        delete_uri = '/groups/%s/users/%s' % (user, group)
        response = self.delete_json(delete_uri)
        assert response.status_int == 400
        assert 'group %s absent' % group in response.body

    def check_user_belongs_group(self):
    def repeat_add_user_to_group(self):
