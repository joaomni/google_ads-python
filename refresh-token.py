from google_auth_oauthlib.flow import InstalledAppFlow

client_id = "834070085776-23n24e6qblml467iegt98tr287d0u44a.apps.googleusercontent.com"
client_secret = "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"
# Utiliza a URI "urn:ietf:wg:oauth:2.0:oob" para uma aplicação de console
redirect_uri = 'urn:ietf:wg:oauth:2.0:oob'

flow = InstalledAppFlow.from_client_secrets_file(
    'client_secrets.json',
    scopes=['https://www.googleapis.com/auth/adwords'],
    redirect_uri=redirect_uri
)

authorization_url, _ = flow.authorization_url(
    access_type='offline',
    prompt='consent'
)

print('Faça login e dê permissão ao aplicativo por meio deste URL: \n',
      authorization_url)
authorization_code = input('Digite o código de autorização: ')

flow.fetch_token(
    authorization_response=authorization_code
)

credentials = flow.credentials
refresh_token = credentials.refresh_token

print('Token de atualização (refresh token):', refresh_token)
