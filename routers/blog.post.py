from urllib import response
from fastapi import APIRouter

from enum import Enum
from typing import Optional

from fastapi import FastAPI,status,Response

router = APIRouter(prefix ='/blog',tags=['blog -post'])
@router.post('/{id}',status_code= status.HTTP_200_OK)
def blog_post_id(id:int,response = Response):
    blogs =[]
    
    if(id < 5):
        response.status_code = status.HTTP_200_OK
        blogs.insert(id)
        return {"message" : f" this id {id } is valid"}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message" : f" this id {id } is invalid"}