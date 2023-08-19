from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import HTTPException, Depends, status
import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate('../../serviceAccountKey.json')
firebase_admin.initialize_app(cred)

"""
Function handling decoding the JWT token
"""
def get_current_user(cred: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
    try:
        # verify the JWT token
        decoded_token = auth.verify_id_token(cred.credentials)
        # Todo: remove the print
        print(decoded_token)
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid Authentication credentials',
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    return decoded_token