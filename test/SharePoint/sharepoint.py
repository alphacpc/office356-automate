from office365.sharepoint.files.file import File
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential

from config import username, password


# User Connect
def get_sharepoint_context_user_connected():

    sharepoint_url = 'https://sonatelworkplace.sharepoint.com'

    user_credentials = UserCredential(username, password)

    conn = ClientContext(sharepoint_url).with_credentials(user_credentials)

    return conn


# List all files
def formated_date(date):
    return date.split("T")[0]


def formated_time(time):
    return time.split("T")[1].split("Z")[0]



def get_files(conn):
    
    list_source = conn.web.get_folder_by_server_relative_url("Documents partages/Data")
    files = list_source.files
    conn.load(files)
    conn.execute_query()

    print(files)

    for file in files :

        print(file.unique_id, file.name, file.length, file.serverRelativeUrl, file.time_created, file.time_last_modified)

        break




# Download files from folder
def download_files(conn, file_name="liste_page_vierge.txt", folder_name="Data"):
    
    file_url = f'/teams/DemoTest/Documents%20partages/Data/liste_page_vierge.txt'

    file = File.open_binary(conn, file_url)
    
    return file



# Basic Query
def basic_query(conn):

    web = conn.web.get().execute_query()

    print("Web title: {0}".format(web.properties['Title']))




