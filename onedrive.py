import msal
from office365.graph_client import GraphClient
from config import ID_SECRET, APP_ID, TOKEN_VALUE


def acquire_token_func():
    authority_url = 'https://login.microsoftonline.com/consumers'
    app = msal.PublicClientApplication(
        authority=authority_url,
        client_id=APP_ID
    )
    token = app.initiate_device_flow(scopes=["Files.Read.All"])
    return token


tenant_name = "sonatelworkplace"
client = GraphClient(acquire_token_func)
drives = client.drives.get().execute_query()
for drive in drives:
    print("Drive url: {0}".format(drive.web_url))