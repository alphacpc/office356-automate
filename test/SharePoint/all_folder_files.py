
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential
import pandas as pd
from config import username_valid, password, sharepoint_url


user_credentials = UserCredential(username_valid, password)
conn = ClientContext(sharepoint_url).with_credentials(user_credentials)


def executor(conn, url, attrib):
    data = conn.web.get_folder_by_server_relative_url(url).__getattribute__(attrib)
    conn.load(data).execute_query()
    return data


# GET ALL FOLDERS
folders = conn.web.get_folder_by_server_relative_url("Documents partages").folders
conn.load(folders).execute_query()


tabname_folders = [
    {
        "name" : folder.serverRelativeUrl.split('/')[-1],
        "url" : folder.serverRelativeUrl
    }
    for folder in folders 
]


tabs_files = []
for folder in tabname_folders:
    files = conn.web.get_folder_by_server_relative_url(folder['url']).files
    conn.load(files).execute_query()

    for file in files:
        # SCHEMA => ID_FILE | NAME_FILE | FROM_FOLDER | FILE_LENGTH | FILE_DATE_CREATED | FILE_DATE_UPDATED | FILE_URL_LINK
        file_url = f"https://sonatelworkplace.sharepoint.com{file.serverRelativeUrl}"

        tabs_files.append({
            "ID_FILE" : file.unique_id,
            "NAME_FILE" : file.name,
            "FROM_FOLDER" : folder["name"],
            "FILE_LENGTH" : file.length,
            "FILE_DATE_CREATED" : file.time_created,
            "FILE_DATE_UPDATED" : file.time_created,
            "FILE_URL_LINK" : file.serverRelativeUrl
        })

df = pd.DataFrame(tabs_files)
df.to_csv('data.csv')