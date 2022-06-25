import time




from backend.database_adapter.models import BasePost,PostSeries
from threading import Thread
from datetime import datetime

from backend.database_adapter.post_adapter import PostDatabaseAdapter


router = APIRouter(
    prefix='/post',
    tags=['post'],
)




