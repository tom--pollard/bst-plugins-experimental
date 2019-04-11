from buildstream.testing import sourcetests_collection_hook, register_repo_kind
from tests.ostreerepo import OSTree

# Register a repo type to run the ostree plugin through buildstream's
# generic source plugin tests
register_repo_kind('ostree', OSTree)


# This hook enables pytest to collect the templated source tests from
# buildstream.testing
def pytest_sessionstart(session):
    sourcetests_collection_hook(session)
