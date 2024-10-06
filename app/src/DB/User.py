from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    __tablename__: str = 'User'
    
    id: int = Field(primary_key=True, default=None)
    username: str = Field()
    password: str = Field()
    
    detail_id: int = Field(foreign_key="UserDetail.id", nullable=True, default=None)

    
class UserDetail(SQLModel, table=True):
    __tablename__: str = 'UserDetail'
    
    id: int = Field(primary_key=True, default=None)
    name: str = Field()
    surname: str = Field()
    

