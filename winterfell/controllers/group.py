import logging
from pecan import conf as CONF
from pecan import expose, response
from pecan.rest import RestController
from jinja2 import Environment, PackageLoader
from winterfell.controllers.common import check_call, render_ldif
from winterfell import exception


logger = logging.getLogger(__name__)


class GroupController(RestController):

    @expose('json')
    def get_all(self):
        pass

    @expose('json')
    def post(self, name):
        create_group(name)
        response.status = 201
        return 'create group %s success' % name

    @expose('json')
    def delete(self, name):
        delete_group(name)
        response.status = 204
        return 'delete group %s success' % name


def delete_group(name):
    try:
        # group info only store on ldap
        ldap_delete_cmd = "ldapdelete -x -D %s -w %s  cn=%s,%s"\
                      % (CONF.ldap_admin_dc, CONF.ldap_admin_password,
                         name, CONF.ldap_group_ou)
        check_call(ldap_delete_cmd)
    except:
        raise exception.DeleteGroupFail(name=name, step='ldap')


def create_group(name):
    if validate_group(name):
        raise exception.GroupIsExist(name=name)
    # create group on ldap
    try:
        ldif_context = {'name': name, 'ldap_group_dc': CONF.ldap_group_dc}
        group_ldif = '%s/%s.ldif' % (CONF.ldif_path, name)
        group_ldif_path = render_ldif('group.ldif.j2', group_ldif, ldif_context)
        ldap_create_cmd = "ldapadd -x -D %s -w %s -f %s" \
                          % (CONF.ldap_admin_dc, CONF.ldap_admin_password,
                             group_ldif_path)
        check_call(ldap_create_cmd)
    except:
        raise exception.CreateGroupFail(name=name, step='ldap')


def validate_group(name):
    return True
