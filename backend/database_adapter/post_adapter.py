from typing import Optional, Union

from database_adapter.models import DataPost, BasePost, PostSeries
from database_adapter.database import create_session

from sqlalchemy import or_
from sqlalchemy import and_



class PostDatabaseAdapter:
    @staticmethod
    def get_dict_of_params(post_model: BasePost):
        return {
            'company_name': post_model.company_name,
            'date': post_model.date,
            'resource': post_model.resource,
            'title': post_model.title,
            'link': post_model.link,
            'category': post_model.category,
            'doc': post_model.doc,
        }

    @staticmethod
    def convert_model_to_table(post_model: BasePost) -> DataPost:
        post: DataPost = DataPost(
            **PostDatabaseAdapter.get_dict_of_params(post_model)
        )
        print(post)
        return post

    @staticmethod
    def create_post(post_model: BasePost) -> int:
        print(post_model)
        with create_session() as session:
            post = PostDatabaseAdapter.convert_model_to_table(post_model=post_model)
            print(post.id)
            print(post.category)
            print(post.doc)
            session.add(post)
            session.flush()
            post_id = post.id
        return post_id

    @staticmethod
    def delete_post(post_id: int) -> None:
        with create_session() as session:
            session.query(DataPost).filter(DataPost.id == post_id).delete()

    @staticmethod
    def get_posts_from_l_to_r(
            left: int,
            right: int,
            search_company_name: Optional[str] = None,
            search_resource: Optional[str] = None,
            search_title: Optional[str] = None,
            search_category: Optional[str] = None,
            search_link: Optional[str] = None,
            search_doc: Optional[str] = None,
            min_time: Optional[int] = None,
            max_time: Optional[int] = None
    ) -> PostSeries:

        with create_session() as session:
            filters = (
                *[search_company_name is None or DataPost.company_name.in_( search_company_name.split('#')) ],
                *[search_resource is  None or DataPost.resource.in_(search_resource.split('#') )],
                *[search_title is None or DataPost.title.in_(search_title.split('#') )],
                *[search_category is None or DataPost.category.in_(search_category.split('#')) ],
                *[ search_link is None or DataPost.link.in_(search_link.split('#'))],
                *[search_doc is None or DataPost.doc.in_(search_doc.split('#'))],
                *[min_time is None or DataPost.date >= min_time],
                *[max_time is None or DataPost.date <= max_time])

            data_set = session.query(DataPost).filter(*filters).order_by(DataPost.date.desc())[left:right]
            #[left: right]

            posts: PostSeries = PostSeries()
            for i in data_set:
                posts.series.append(BasePost.from_orm(i))
                posts.number_of_posts += 1
        return posts

    @staticmethod
    def get_post_by_id(post_id: int) -> Union[BasePost, None]:
        with create_session() as session:
            post_model = session.query(DataPost).get(post_id)
            if post_model is None:
                post = None
            else:
                post = BasePost.from_orm(post_model)
        return post
