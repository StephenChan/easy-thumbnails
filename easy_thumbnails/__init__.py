VERSION = (2, 9, 0, 'final', 0)


def get_version(*args, **kwargs):
    # Don't litter django/__init__.py with all the get_version stuff.
    # Only import if it's actually called.
    from .version_utils import get_version
    # Upstream version plus a local version label.
    # https://packaging.python.org/en/latest/specifications/version-specifiers/#local-version-identifiers
    return get_version(*args, **kwargs) + '+coralnet'
