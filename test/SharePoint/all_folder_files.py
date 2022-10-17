
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential
from pprint import pprint
import pandas as pd
from config import username_valid, password, sharepoint_url


user_credentials = UserCredential(username_valid, password)

conn = ClientContext(sharepoint_url).with_credentials(user_credentials)


def executor(conn, url, attrib):

    list_data = conn.web.get_folder_by_server_relative_url(url)

    data = list_data.__getattribute__(attrib)
    conn.load(data)
    conn.execute_query()

    return data



# GET ALL FOLDERS
list_folders = conn.web.get_folder_by_server_relative_url("Documents partages")

folders = list_folders.folders
conn.load(folders)
conn.execute_query()


tabname_folders = [
    {
        "name" : folder.serverRelativeUrl.split('/')[-1],
        "url" : folder.serverRelativeUrl
    }
    for folder in folders 
]


tabs_files = []

# GET ALL FILES
for folder in tabname_folders:
    list_files = conn.web.get_folder_by_server_relative_url(folder['url'])

    files = list_files.files
    conn.load(files)
    conn.execute_query()

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