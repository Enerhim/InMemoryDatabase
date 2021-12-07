from database import *
from interpreter import *
from sys import argv
import readline

def login(db_name):        
    database = MemoryDatabase(db_name)
    try:
        database.load()
    except FileNotFoundError:
        print(f"{database.name}.json not found")
        return None
        
    return database

try:
    db_name = argv[1]                
except IndexError:
    db_name = input("Database name: ")

db = login(db_name)

if db:
    intp = Interpreter()
    while True:
        try:
            query = input(f"{db.name} >")
            lex = intp.lex(query)
            
            special_request_type = lex["req_type"].lower()
            
            if special_request_type == "duplicate":
                try:
                    duple_name = lex["args"][0]
                except:
                    duple_name = db.name + "--duplicate"
                    
                database = MemoryDatabase(duple_name)
                database.save(override=True)

                with open("db_list.txt", "a") as fp:
                    fp.write(f"\n{database.name}")
                    
            elif special_request_type == "exit":
                quit()
            else:   
                print(intp.execute(db, lex))
            
        except KeyboardInterrupt:
            exit("\n")
