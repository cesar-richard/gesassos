# gesassos
Outil de gestion des associations du BDE UTC

## Installation

### Dépendances

    apt-get install python-dev python-libssh2 python-setuptools
    curl http://python-distribute.org/distribute_setup.py | python
    curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python
    pip install pycrypto
    pip install fabric
    apt-get install python-ldap python-mysqldb

## Utilisation

Exécuter dans le dossier du dépôt :

    fab -f . fonction:param1,param2
