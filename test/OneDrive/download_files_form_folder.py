import os
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential
from config import username_valid, password, onedrive_url_valid


user_credentials = UserCredential(username_valid, password)
conn = ClientContext(onedrive_url_valid).with_credentials(user_credentials)

def download(file_url):
    
    filename = file_url.split("/")[-1]
    file_path = os.path.abspath( os.path.join("generators", filename) )

    with open(file_path, "wb") as local_file:
        file = conn.web.get_file_by_server_relative_url(file_url)
        file.download(local_file)
        conn.execute_query()
    print(file_path)


# GET 
folder_name = "Classeurs"
files = conn.web.get_folder_by_server_relative_url(f"Documents/{folder_name}").files
conn.load(files).execute_query()


for file in files:
    download(file.serverRelativeUrl)


