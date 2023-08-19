from fastapi import APIRouter, HTTPException, status, Depends
from prisma import Prisma
from ..schemas import user
from ..prisma.prisma import get_db

# Router config
router = APIRouter(
    prefix='/users',
    tags=['users']
)

"""
Function handling creating a user

@param:
@return:
"""
@router.post('/')
async def create_user(user: user.UserCreate, db: Prisma = Depends(get_db)):
    # Query the user with email provided
    db_user = await db.user.find_unique(
        where={
            'email': user.email
        }
    )

    # Throw an error if the user already exists
    if db_user:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Email already registered')
    
    return await db.user.create(
        data={
            'username': user.username,
            'email': user.email,
            'hashedPassword': user.password,            
        }
    )

"""
Function handling getting all users

@param:
@return: users
"""

@router.get('/')
async def get_users(db: Prisma = Depends(get_db)):
    users = await db.user.find_many(
        take=20
    )
    if users is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='')
    return users

"""
Function handling getting a specific user

@param:
@return:
"""
@router.get('/{user_id}')
async def get_user(user_id: str, db: Prisma = Depends(get_db)):
    # Query the user with unique id provided 
    user = await db.user.find_unique(
        where={
            'id': user_id
        }
    )

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Users Not Found!')
    
    return user