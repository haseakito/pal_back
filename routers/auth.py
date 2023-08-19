from fastapi import APIRouter, HTTPException, status, Depends
from prisma import Prisma
from ..prisma.prisma import get_db
from ..schemas import user

# Router config
router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

"""
Asynchronous function handling the auth 
"""
@router.post('/login')
async def login(user_credentials: user.UserLogin, db: Prisma =Depends(get_db)):
    user = db.user.find_unique(
        where={
            'email': user_credentials.email
        }
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Invalid Credentials'
        )
    
    return 
    
