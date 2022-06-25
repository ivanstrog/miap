from database_adapter.post_adapter import PostDatabaseAdapter
from database_adapter.models import BasePost


def create_some_posts():
    for i in range(100):
        post = BasePost(
            company_name=f'COMPANY{i}',
            date=i,
            resource=f'resource{i}',
            title=f'title{i}',
            link=f'link{i}',
            category=f'category{i}',
            doc=f'doc{i}'
        )

        post_id = PostDatabaseAdapter.create_post(post_model=post)
        print(f'пост {i} добавлен')
