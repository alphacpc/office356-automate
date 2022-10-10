import pandas as pd
from pprint import pprint
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential
from config import username_valid, password, onedrive_url_valid


user_credentials = UserCredential(username_valid, password)

conn = ClientContext(onedrive_url_valid).with_credentials(user_credentials)

# GET ALL FOLDERS ON ROOT
list_source = conn.web.get_folder_by_server_relative_url("Documents")
folders = list_source.folders
conn.load(folders)
conn.execute_query()

tab_folders = []

for folder in folders:

    # SCHEMA => FOLDER_ID, FOLDER_NAME, FOLDER_URL, FOLDER_TIME_CREATED, FOLDER_LAST_TIME_MODIFIED
    tab_folders.append({
        "FOLDER_ID" : folder.unique_id,
        "FOLDER_NAME" : folder.name ,
        "FOLDER_URL" : folder.serverRelativeUrl,
        "FOLDER_TIME_CREATED" : folder.time_created,
        "FOLDER_LAST_TIME_MODIFIED" : folder.time_last_modified
    })


df = pd.DataFrame(tab_folders)
df.to_csv('generators/data.csv')