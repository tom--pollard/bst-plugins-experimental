# Pylint doesn't play well with fixtures and dependency injection from pytest
# pylint: disable=redefined-outer-name

import os
import pytest

from buildstream.testing.runcli import cli_integration as cli  # pylint: disable=unused-import
from buildstream.testing.integration import integration_cache  # pylint: disable=unused-import
from buildstream.testing.integration import assert_contains
from buildstream.testing._utils.site import HAVE_SANDBOX

pytestmark = pytest.mark.integration


DATA_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "project"
)


@pytest.mark.datafiles(DATA_DIR)
@pytest.mark.skipif(not HAVE_SANDBOX, reason='Only available with a functioning sandbox')
def test_quilt_build(cli, datafiles):
    project = str(datafiles)
    checkout = os.path.join(cli.directory, 'quilt_checkout')

    result = cli.run(project=project, args=['build', "quilt-build-test.bst"])
    result.assert_success()

    result = cli.run(project=project, args=[
        'artifact', 'checkout', '--directory', checkout, 'quilt-build-test.bst'
    ])
    result.assert_success()

    assert_contains(checkout, ['/patches/series', '/patches/test', '/src/hello.c'])