from pecan import make_app
from winterfell import model
from winterfell import hooks


def setup_app(config):

    model.init_model()
    app_conf = dict(config.app)

    return make_app(
        app_conf.pop('root'),
        hooks=[hooks.AuthHook(),
               hooks.ExceptionHook()
               ],
        logging=getattr(config, 'logging', {}),
        **app_conf
    )
