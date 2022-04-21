from .base import *

# you need to set "WORKING_ENVIRONMENT = 'staging', 'production'" as an environment variable
# in your OS (on which your website is hosted)

if config("WORKING_ENVIRONMENT") == "staging":
    from .staging import *
elif config("WORKING_ENVIRONMENT") == "production":
    from .production import *
else:
    from .development import *
