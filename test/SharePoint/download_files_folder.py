import os
from pprint import pprint
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


def add_file_local(file_url):

    filename = file_url.split("/")[-1]

    file_path = os.path.abspath( os.path.join(dirName, filename) )


    with open(file_path, "wb") as local_file:
        
        file = conn.web.get_file_by_server_relative_url(file_url)
        file.download(local_file)
        conn.execute_query()

    print(file_path)




# GET ALL FOLDERS
list_folders = conn.web.get_folder_by_server_relative_url("Documents partages")

folders = list_folders.folders
conn.load(folders)
conn.execute_query()


tabname_folders = [
    {   
        "id" : index + 1,
        "name" : folder.serverRelativeUrl.split('/')[-1],
        "url" : folder.serverRelativeUrl
    }
    for index, folder in enumerate(folders) 
]

print("\n#######################################")
print("############# TELECHARGEMENT ##########")
print("#######################################\n")
for item in tabname_folders:
    print(f"{item['id']} : Pour télécharger le contenu de {item['name']}")


try :
    
    xEntre = int(input("Veuillez choisir une option : "))

    if xEntre >= 1 and xEntre <= len(tabname_folders) :

        list_files = conn.web.get_folder_by_server_relative_url(tabname_folders[xEntre - 1]['url'])

        files = list_files.files
        conn.load(files)
        conn.execute_query()

        for file in files:

            add_file_local(file.serverRelativeUrl)
        

    else:
        print("A Bientot !")


except ValueError:
    print("Impossible de convertir cette chaine")
    print("A Bientot !")

