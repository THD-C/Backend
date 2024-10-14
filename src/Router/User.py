from fastapi import APIRouter
from opentelemetry import trace
import src.DB as DB


user_router = APIRouter(prefix="/user")
tracer = trace.get_tracer(__name__)


@user_router.get("")
def get_user(id: int = None) -> list[DB.User]:
    """
    Returns list of users
    """
    with tracer.start_as_current_span("DB_query-select_users"):
        with DB.Session() as s:
            return (
                s.query(DB.User)
                .filter(DB.User.id == id if id is not None else True)
                .all()
            )


@user_router.post("")
def post_user(user_data: DB.User):
    """
    Adds new user entry
    """
    with tracer.start_as_current_span("DB_query-insert_user"):
        with DB.Session() as s:
            s.add(user_data)
            s.commit()
            s.refresh(user_data)
            return user_data
