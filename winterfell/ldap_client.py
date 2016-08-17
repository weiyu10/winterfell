import ldap
ldap.initialize('ldap://localhost:389')


class ldap_client(object):
    def __init__(self, server_url, user_dc, group_dc):
        self.client = ldap.initialize(server_url)
        self.user_dc = user_dc
        self.group_dc = group_dc

    def search_user(self, name):
        filter_str = 'cn=%s' % name
        return self.client.search_s(self.user_dc, ldap.SCOPE_ONELEVEL,
                                    filter_str)

    def search_group(self, name):
        filter_str = 'cn=%s' % name
        return self.client.search_s(self.group_dc, ldap.SCOPE_ONELEVEL,
                                    filter_str)
