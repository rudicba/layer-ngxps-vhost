from charmhelpers.core import hookenv
from charms.reactive import (when, set_state)

config = hookenv.config()


@when('config.changed')
def validate():
    # if valid
    set_state('vhost.valid')
    # if not remove_state
