from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential
from config import username_valid, password, onedrive_url_valid


user_credentials = UserCredential(username_valid, password)

conn = ClientContext(onedrive_url_valid).with_credentials(user_credentials)

def upload_to_onedrive(dir_name, file_name):

    target_folder = conn.web.get_folder_by_server_relative_url("Documents/Hello")

    with open(file_name, 'rb') as content_file:

        file_content = content_file.read()

        target_folder.upload_file(file_name, file_content).execute_query()


upload_to_onedrive("./data.csv")