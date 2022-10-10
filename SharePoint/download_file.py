import os
from datetime import datetime
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential
from config import username_valid, password, sharepoint_url


# CONNECT USER
user_credentials = UserCredential(username_valid, password)

conn = ClientContext(sharepoint_url).with_credentials(user_credentials)

# CREATE FOLDER WITH DATE TODAY
dirName =  f"{ datetime.now().strftime('%d-%m-%Y') }-datas"


try:
    os.mkdir(dirName)
    print(f"Le dossier {dirName} créé avec succès !") 

except FileExistsError:
    print(f"Le dossier { dirName } existe déjà !")



# FUNC DOWNLOADER SIGLE FILE
def download(file_url):

    filename = file_url.split("/")[-1]

    file_path = os.path.abspath( os.path.join(dirName, filename) )

    with open(file_path, "wb") as local_file:
        
        file = conn.web.get_file_by_server_relative_url(file_url)
        file.download(local_file)
        conn.execute_query()

    print(file_path)


