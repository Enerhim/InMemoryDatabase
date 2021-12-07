from database import *
from sys import argv

# Create DB

try:
    name = str(argv[1])
except IndexError:
    name = input("Database Name (default): ")
    if name.isspace() or name == "":
        name = "default"
        
    
database = MemoryDatabase(name)
database.save(override=True)

with open("db_list.txt", "a") as fp:
    fp.write(f"\n{database.name}")