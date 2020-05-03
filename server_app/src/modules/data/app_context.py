from commons.constants.paths import  DATABASE_PATH

from peewee import ( 
    SqliteDatabase
)

class AppContext:
    my_database = SqliteDatabase(DATABASE_PATH)
    def __init__(self):
        super().__init__()
        from modules.models.user import User
        self.my_database.connect(reuse_if_open="True")
        self.my_database.create_tables([User])
