"""
slackd.common.slack_client
~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2016 David M. Westerhoff
:license: All rights reserved

"""

import slacker
from config import read_config_token

slack_client = slacker.Slacker(read_config_token())
