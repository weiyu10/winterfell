from winterfell import hooks
# Server Specific Configurations
server = {
    'port': '9091',
    'host': '0.0.0.0'
}

# Pecan Application Configurations
app = {
    'root': 'winterfell.controllers.root.RootController',
    'hooks': [hooks.ExceptionHook()],
    'modules': ['winterfell'],
    'static_root': '%(confdir)s/public',
    'template_path': '%(confdir)s/winterfell/templates',
    'debug': True,
    'errors': {
        404: '/error/404',
        '__force_dict__': True
    }
}

logging = {
    'root': {'level': 'DEBUG', 'handlers': ['console']},
    'loggers': {
        'winterfell': {'level': 'DEBUG', 'handlers': ['console']},
        'pecan': {'level': 'DEBUG', 'handlers': ['console']},
        'py.warnings': {'handlers': ['console']},
        '__force_dict__': True
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'color'
        }
    },
    'formatters': {
        'simple': {
            'format': ('%(asctime)s %(levelname)-5.5s [%(name)s]'
                       '[%(threadName)s] %(message)s')
        },
        'color': {
            '()': 'pecan.log.ColorFormatter',
            'format': ('%(asctime)s [%(padded_color_levelname)s] [%(name)s]'
                       '[%(threadName)s] %(message)s'),
            '__force_dict__': True
        }
    }
}

# Custom Configurations must be in Python dictionary format::
#
# foo = {'bar':'baz'}

# default password when user not provide password
user_default_password = 'test'

ldif_path = '/root/ldap'

fatal_exception_format_errors = False

ldap_admin_dc = 'cn=Manager,dc=weiyu,dc=com'
ldap_admin_password = 'ldapiswonderful'
ldap_people_ou = 'ou=People,dc=weiyu,dc=com'

#
# All configurations are accessible at::
# pecan.conf
