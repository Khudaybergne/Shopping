import sqlite3
db = sqlite3.connect('Foods.db',timeout=10)
cursor = db.cursor()
async def start_db():
    cursor.execute('''
CREATE TABLE IF NOT EXISTS foods(
                   type TEXT,
                   price TEXT,
                   name TEXT,
                   photo TEXT,
                   ingridients TEXT)
''')
async def add_to_db(types_to,price,name,photo,ingri):
    cursor.execute('''
INSERT INTO foods(type,price,name,photo,ingridients)
                   VALUES(?,?,?,?,?)
''',(types_to,price,name,photo,ingri)
    )
    db.commit()
async def show_foods():
    cursor.execute('SELECT * FROM foods')
    datas = cursor.fetchall()
    return datas

# async def userreg():
cursor.execute("""
CREATE TABLE IF NOT EXISTS registrasiya(
                   Name TEXT,
                   Tel TEXT,
               Id TEXT,
               user_name TEXT)""")
# cursor.execute(""" ALTER TABLE registrasiya
# ADD user_name TYPE;
# """)
# db.commit()  ##Tablitsaga jana zat qosiw



async def updatereg(name,telefon,user_id,user_name):
    cursor.execute("""
INSERT INTO registrasiya(Name,Tel,Id,user_name)
                   VALUES(?,?,?,?)""",(name,telefon,user_id,user_name))
    db.commit()

async def users():
    cursor.execute("SELECT * FROM registrasiya")
    users=cursor.fetchall()
    return users



async def zakaz_def():
    cursor.execute("""
CREATE TABLE IF NOT EXISTS zakaz(
                   Food_Type TEXT,
                   Food_NameTEXT ,
               Telefon TEXT,
               Name TEXT)""")

async def zakazz_def(food_type,food_nametext,telefon,name):
    cursor.execute("""
INSERT INTO zakaz(Food_type,Food_NameTEX,Telefon,Name)
                   VALUES(?,?,?,?)""",(food_nametext,food_type,telefon,name)
                   )

async def open_zakaz():
    cursor.execute("SELECT * FROM zakaz")
    zakaz=cursor.fetchall()
    return zakaz