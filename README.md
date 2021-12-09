# An In-Memory Database System made using the Python Programming Language.
This database can store key : value pairs in memory like a Python dictonary. The database can be saved and loaded from the Hard Disk so 
that the data is not lost when the system shutdowns or restarts

The advantage of this database is that it can deliver and update data with incredible speed since its stored in memory s
instead of the disk which tends to be much slower

There is also a small and simple query language with the database to add, delete, update, get, save and load data
--------------

### To create a database run:
`python create_memory_db.py [databse name]`

### After creating a database, you can login to it by running:
`python db_console.py [database name]`

### After Loging in, you can perform queries to add, delete, update, get, save and load the database

- Add data:
add [key] [value]

- Delete data:
delete [key]

- Get Data:
get [key1] [key2] [key3]... Get Specific Keys
