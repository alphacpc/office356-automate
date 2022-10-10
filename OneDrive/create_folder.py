from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential
from config import username_valid, password, onedrive_url_valid


user_credentials = UserCredential(username_valid, password)

conn = ClientContext(onedrive_url_valid).with_credentials(user_credentials)

def create_folder_on_onedrive(dir_name: str):

    if dir_name:
        
        result = conn.web.folders.add(f'Documents/{dir_name}').execute_query()

        if result:
            relative_url = f'Documents/{dir_name}'

            return relative_url

    else:
        print("Saisir le nom du dossier !!!")


url = create_folder_on_onedrive('')

print("URL values => ", url)