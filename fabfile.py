"""
Fabric's own fabfile.
"""

from __future__ import with_statement

import nose

from fabric.api import task


@task(default=True)
def test(args=None):
    """
    Run all unit tests and doctests.

    Specify string argument ``args`` for additional args to ``nosetests``.
    """
    # Default to explicitly targeting the 'tests' folder, but only if nothing
    # is being overridden.
    print(args)
    nose.core.run_exit(0)
