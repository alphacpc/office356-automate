import os
from xmlrpc.client import Boolean, boolean
from office365.sharepoint.files.file import File
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential
from office365.runtime.client_request_exception import ClientRequestException

from config import username_valid, password, sharepoint_url


# User Connect
def auth():

    user_credentials = UserCredential(username_valid, password)
    conn = ClientContext(sharepoint_url).with_credentials(user_credentials)
    return conn


# List all files
def formated_date(date):
    return date.split("T")[0]

def formated_time(time):
    return time.split("T")[1].split("Z")[0]




##############################

def check_exist_folder(folder_name_sharepoint):
    conn = auth()
    
    try:
        req = conn.web.get_folder_by_server_relative_url(f"Documents partages/{folder_name_sharepoint}")
        req.get().execute_query()
        return req
    
    except ClientRequestException as e:
        print(e)
        return False



def share(folder_name, isEdit = False):
    
    req = check_exist_folder(folder_name)
    if req:
        conn = auth()

        req.share_link()
        
        result = conn.web.create_anonymous_link(conn, url=f"{req.serverRelativeUrl}", is_edit_link = True).execute_query()
        return result

    
    return False



print(share("Data/"))