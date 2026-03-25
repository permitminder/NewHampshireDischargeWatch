"""
State configuration for this NewHampshireDischargeWatch instance.

All state-specific values are centralized here. To deploy for a new state,
run: python deploy_new_state.py <STATE_CODE>

This file is overwritten by deploy_new_state.py — do not add logic here.
"""

STATE_CODE = "NH"
STATE_NAME = "New Hampshire"
APP_NAME = "NewHampshireDischargeWatch"
APP_TAGLINE = "New Hampshire Discharge Monitoring"
DOMAIN = "newhampshiredischargewatch.org"
DATA_FILE = "nh_exceedances_launch_ready.csv"
CONTACT_EMAIL = "data@newhampshiredischargewatch.org"
MAILING_ADDRESS = ""
TIMEZONE_LABEL = "EST"
EPA_REGION = 1
