from prisma import Prisma
from fastapi import HTTPException

"""
Asynchronous function handling the database connection
"""
async def get_db():
    db = Prisma()
    try:
        await db.connect()        
    except:
        raise HTTPException(status_code=500, detail='Internal Server Error')
    finally:
        await db.disconnect()