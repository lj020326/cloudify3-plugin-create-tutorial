
import os

# import the operation decorator
from cloudify.decorators import operation

# the operation decorator allows us to access the ctx object
@operation
def start(ctx, **kwargs):
    with open('/tmp/index.html', 'w') as f:
        f.write('<p>Hello Cloudify!</p>')

    command = 'cd /tmp; nohup python -m SimpleHTTPServer > /dev/null 2>&1' \
              ' & echo $! > /tmp/python-webserver.pid'

    # we can use the ctx.logger object to send a formatted log with context
    # to the manager. The message shown here will only be a part of the
    # log sent. A lot of context is supplied with the object.
    ctx.logger.info('Starting HTTP server using: {0}'.format(command))
    os.system(command)


# we're defining multiple operations to which we can refer to afterwards
# in our blueprint
@operation
def stop(ctx, **kwargs):
    try:
        with open('/tmp/python-webserver.pid', 'r') as f:
            pid = f.read()
        ctx.logger.info('Stopping HTTP server [pid={0}]'.format(pid))
        os.system('kill -9 {0}'.format(pid))
    except IOError:
        ctx.logger.info('HTTP server is not running!')
        