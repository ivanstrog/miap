import uvicorn
from fastapi import FastAPI, APIRouter, Depends, status, HTTPException
from typing import Optional
from database_adapter.models import BasePost, PostSeries
from threading import Thread
from datetime import datetime

from database_adapter.post_adapter import PostDatabaseAdapter

app = FastAPI(title='Miap Api')


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post('/create/')
def create_post(
        post_model: BasePost,
        post_adapter: PostDatabaseAdapter = Depends(),
):
    post_id = post_adapter.create_post(post_model=post_model)

    return {"id": post_id, "status": status.HTTP_201_CREATED}


@app.post('/delete/')
def delete_post(
        post_id: int,
        post_adapter: PostDatabaseAdapter = Depends(),
):
    post_adapter.delete_post(post_id=post_id)
    return status.HTTP_201_CREATED


@app.get('/posts/', response_model=PostSeries)
def get_posts(
        left: int,
        right: int,
        search_company_name: Optional[str] = None,
        search_resource: Optional[str] = None,
        search_title: Optional[str] = None,
        search_category: Optional[str] = None,
        search_link: Optional[str] = None,
        search_doc: Optional[str] = None,
        min_time:Optional[int] = None,
        max_time:Optional[int] = None,
        post_adapter: PostDatabaseAdapter = Depends(),
) -> PostSeries:
    return post_adapter.get_posts_from_l_to_r(left=left, right=right,
                                              search_company_name=search_company_name,
                                              search_resource=search_resource,
                                              search_title=search_title,
                                              search_category=search_category,
                                              search_link=search_link,
                                              search_doc=search_doc,
                                              min_time = min_time,
                                              max_time = max_time)


@app.get('/get_post/', response_model=BasePost)
def get_post_by_id(post_id: int, post_adapter: PostDatabaseAdapter = Depends()):
    return post_adapter.get_post_by_id(post_id=post_id)


if __name__ == '__main__':
    uvicorn.run(
        '__main__:app',
        host='0.0.0.0',
        port=8000,
        reload=True,
    )
