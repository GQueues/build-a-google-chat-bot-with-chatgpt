import logging

from oauth2client import client

# Bearer Tokens received by apps will always specify this issuer.
CHAT_ISSUER = 'chat@system.gserviceaccount.com'

# Url to obtain the public certificate for the issuer.
PUBLIC_CERT_URL_PREFIX = 'https://www.googleapis.com/service_accounts/v1/metadata/x509/'

# Intended audience of the token, which will be the project number of the app.
# TODO: Update audience with project number
AUDIENCE = '362822420032'

def is_request_valid(request):
    """Verify the validity of a bearer token received by an app, using OAuth2Client.

    Args:
        request: The request object containing the Authorization header with the bearer token.

    Returns:
        True if the bearer token is valid and intended for the app, False otherwise.
        
    Raises:
        Exception: If the Authorization header is missing.
    """

    try:
        # Get the token from the Authorization header
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            raise Exception('Authorization header is missing')
        
        token = auth_header.split(' ')[1]

        # Verify valid token, signed by CHAT_ISSUER, intended for a third party.
        token = client.verify_id_token(token, AUDIENCE, cert_uri=PUBLIC_CERT_URL_PREFIX + CHAT_ISSUER)

        logging.info("verified token: %s" % token)

        if token['iss'] != CHAT_ISSUER:
            return False
    except:
        return False
    
    return True


