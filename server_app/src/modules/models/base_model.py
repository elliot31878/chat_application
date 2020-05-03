from peewee import ( 
    Model
)
class BaseModel(Model):
    class Meta:
        from modules.data.app_context import AppContext
        database = AppContext.database