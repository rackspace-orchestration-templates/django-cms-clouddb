maintainer 'Brint O\'Hearn'
maintainer_email 'brint.ohearn@rackspace.com'
license 'Apache 2.0'
description 'Create Django CMS site'
long_description IO.read(File.join(File.dirname(__FILE__), 'README.md'))
version '0.0.1'
name 'rax-django-cms'

depends 'apache2'
depends 'application_python'
depends 'git'
depends 'mysql'
depends 'postgresql'
depends 'sqlite'
