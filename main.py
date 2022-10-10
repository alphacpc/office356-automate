import os
import pandas as pd
from pprint import pprint
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential
from config import username_valid, password, onedrive_url_valid


user_credentials = UserCredential(username_valid, password)

conn = ClientContext(onedrive_url_valid).with_credentials(user_credentials)
