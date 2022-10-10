import os
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential
from config import username_valid, password, onedrive_url_valid


user_credentials = UserCredential(username_valid, password)

conn = ClientContext(onedrive_url_valid).with_credentials(user_credentials)


# FUNC TO GET ALL FILES IN FOLDER
def get_files_folder(path):

    return [file for file in path if os.path.isfile(file)]



# FUNC TO UPLOAD FILE ON FOLDER
def upload_to_onedrive(folder_name,file_name):

    target_folder = conn.web.get_folder_by_server_relative_url(f"Documents/{folder_name}")
    
    with open(file_name, 'rb') as content_file:

        file_content = content_file.read()

        target_folder.upload_file(file_name, file_content).execute_query()






files = get_files_folder(os.listdir("."))





for file in files:

    upload_to_onedrive("Hello", file)