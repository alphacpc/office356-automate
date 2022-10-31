import pandas as pd
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential
from config import username_valid, password, onedrive_url_valid


user_credentials = UserCredential(username_valid, password)
conn = ClientContext(onedrive_url_valid).with_credentials(user_credentials)

# GET ALL FOLDERS ON ROOT
folder_name = "Classeurs"
files = conn.web.get_folder_by_server_relative_url(f"Documents/{folder_name}").files
conn.load(files).execute_query()


tab_files = []
for file in files:

    # SCHEMA => FILE_ID, FILE_NAME, FILE_LENGTH, FILE_URL, FILE_TIME_CREATED, FILE_LAST_TIME_MODIFIED
    tab_files.append({
        "FILE_ID" : file.unique_id,
        "FILE_NAME" : file.name ,
        "FROM_FOLDER" : file.serverRelativeUrl.split("/")[-2],
        "FILE_LENGTH" : file.length ,
        "FILE_URL" : file.serverRelativeUrl,
        "FILE_TIME_CREATED" : file.time_created,
        "FILE_LAST_TIME_MODIFIED" : file.time_last_modified
    })


df = pd.DataFrame(tab_files)
df.to_csv(f"generators/files_{folder_name}.csv")