"""Settings for pelican."""

AUTHOR = 'Tony Simpson'
SITENAME = 'tonysimpson.github.com'
SITEURL = 'http://tonysimpson.github.com'

WITH_PAGINATION = True
DEFAULT_PAGINATION = 10
REVERSE_ARCHIVE_ORDER = True

# Uncomment what ever you want to use
#GOOGLE_ANALYTICS = 'XX-XXXXXXX-XX'
DISQUS_SITENAME = 'tonysimpsongithubcom'
GITHUB_URL = 'http://github.com/tonysimpson/tonysimpson.github.com'
TWITTER_USERNAME = 'agjasimpson'

# This can also be the absolute path to a theme that you downloaded
# i.e. './themes/anothertheme/'
THEME = 'notmyidea'

# The folder ``images`` should be copied into the folder ``static`` when
# generating the output.
STATIC_PATHS = ['images', ]

# See http://pelican.notmyidea.org/en/latest/settings.html#timezone
TIMEZONE = 'UTC'

# I like to put everything into the category ``Blog``, which also appears on
# the main menu. Tags will not appear on the menu.
DEFAULT_CATEGORY = 'Blog'

# I like to have ``Archives`` in the main menu.
MENUITEMS = (
    ('Archives', '{0}/archives.html'.format(SITEURL)),
)


