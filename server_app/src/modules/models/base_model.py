from peewee import ( 
    Model
)
class BaseModel(Model):
    class Meta:
        from ..data.app_context import AppContext
        database = AppContext.my_database