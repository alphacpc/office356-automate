import os
import pandas as pd
from datetime import datetime
from config import username_valid, password, onedrive_url_valid
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential


class OneDrive:

    # CONFIG CONNECT USER
    def auth(self):

        conn = ClientContext(onedrive_url_valid).with_credentials(
            UserCredential(user_name = username_valid, password = password)
        )

        return conn



    # GET ALL FOLDERS WITH FROM ROOT OR FOLDER_NAME
    def get_folders_endpoint(self, folder_name : str = ""):

        conn = self.auth()

        list_source = conn.web.get_folder_by_server_relative_url(f"Documents/{folder_name}")
        folders = list_source.folders
        conn.load(folders)
        conn.execute_query()

        return folders



    # GET FILES FROM FOLDER
    def get_files_from_folder(self, folder_name : str = ""):

        conn = self.auth()
        
        list_source = conn.web.get_folder_by_server_relative_url(f"Documents/{folder_name}")
        files = list_source.files
        conn.load(files)
        conn.execute_query()

        return files





    # DOWNLOAD FILE BY URL
    def download_file(self, file_url : str):
        
        filename = file_url.split("/")[-1]

        dir_name =  f"{ datetime.now().strftime('%d-%m-%Y') }-datas"

        try:
            os.mkdir(dir_name)

        except FileExistsError:
            # print(f"Le dossier { dir_name } existe déjà !")
            pass

        conn = self.auth()
        file_path = os.path.abspath( os.path.join(dir_name, filename) )


        with open(file_path, "wb") as local_file:
            file = conn.web.get_file_by_server_relative_url(file_url)
            file.download(local_file)
            conn.execute_query()

        print(f"Fichier { filename } téléchargé avec succès !")




    # DOWNLOAD FILES FROM FOLDER
    def download_files_from_folder(self, folder_name : str = ""):

        files = self.get_files_from_folder(folder_name)

        for file in files :

            self.download_file(file.serverRelativeUrl)






    # UPLOAD FILE 
    def upload_file_to_onedrive(self, path_file : str, folder_name : str = ""):

            file_name = path_file.split('/')[-1]
            conn = self.auth()

            target_folder = conn.web.get_folder_by_server_relative_url(f"Documents/{folder_name}")

            with open(file_name, 'rb') as content_file:

                file_content = content_file.read()

                target_folder.upload_file(file_name, file_content).execute_query()

            print(f"Le fichier {file_name} chargé avec succès !")






    # UPLOAD FILES ON LOCAL DIRECTORY
    def upload_files_to_onedrive(self, folder_name_local : str, folder_name_onedrive: str = ""):

        folder_name_local = os.listdir(f"{ folder_name_local }")

        files = [file for file in folder_name_local if os.path.isfile(file)]

        for file in files:

            self.upload_file_to_onedrive( file, folder_name_onedrive)







#/personal/stg_diallo67135_orange-sonatel_com/Documents/<filename> => Pour un fichier
