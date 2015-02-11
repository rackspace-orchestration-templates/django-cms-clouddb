import re
from fabric.api import env, hide, run, task
from envassert import detect, file, group, package, port, process, service, \
    user
from hot.utils.test import get_artifacts


def django_cms_is_responding():
    with hide('running', 'stdout'):
        wget_cmd = ("wget --no-check-certificate --quiet "
                    "--output-document - http://localhost/")
        homepage = run(wget_cmd)
        if re.search('Welcome to django CMS', homepage):
            return True
        else:
            return False


@task
def check():
    env.platform_family = detect.detect()

    assert package.installed("apache2")
    assert file.exists("/srv/workspace/bin/django-admin.py")
    assert file.exists("/etc/apache2/mods-enabled/wsgi.conf")
    assert file.exists("/etc/apache2/mods-enabled/wsgi.load")
    assert port.is_listening(80)
    assert user.exists("pydev")
    assert group.is_exists("pydev")
    assert user.is_belonging_group("pydev", "pydev")
    assert process.is_up("apache2")
    assert service.is_enabled("apache2")
    assert django_cms_is_responding()


@task
def artifacts():
    env.platform_family = detect.detect()
    get_artifacts()
