
import raven

RAVEN_CONFIG = {
    'dsn': 'http://somethingblahblah',
    'release': raven.fetch_git_sha(os.path.dirname(__file__) + "/../.."),
}
