from commons.constants.paths import  DATABASE_PATH

from peewee import ( 
    SqliteDatabase
)

class AppContext:
    database = SqliteDatabase(DATABASE_PATH)
    def __init__(self):
        from modules.models.user import User
        self.database.connect(reuse_if_open="True")
        self.database.create_tables([User])
        
