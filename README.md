# An In-Memory Database System made using the Python Programming Language.
This database can store key : value pairs in memory like a Python dictonary. The database can be saved and loaded from the Hard Disk as JSON so 
that the data is not lost when the system shutdowns or restarts.

The advantage of this database is that it can deliver and update data with incredible speed since its stored in memory s
instead of the disk which tends to be much slower.

There is also a small and simple query language with the database to add, delete, update, get, save and load data

Requirements
--------------
Python 3.8 or above

Usage
---------

### To create a database run:
`python create_memory_db.py [databse name]`

### After creating a database, you can login to it by running:
`python db_console.py [database name]`

### After Loging in, you can perform queries to add, delete, update, get, save and load the database

- Add data: <br/>
`add [key] [value]` <br/>

- Delete data: <br/>
`delete [key] <br/>`

- Get Data: <br/>
`get [key]` Get one key <br/>
`get [key1] [key2] [key3]...` Get Specific Keys <br/>
`get` Get all keys <br/>

- Update Data: <br/>
`update [key] [new value]` <br/>

- Save Data to db_list/: <br/>
`save` Save database <br/>
`save override` Overwrite existing database <br/>

- Load data from db_list/: <br/>
`load` <br/>

- Undo: <br/>
`undo` Undo latest change (work in progress) <br/>

- Duplicate Database: <br/>
`duplicate [optional: new database name]` Duplicates database with current data <br/>

Use `exit` to exit the console. <br/>

To add in the future
-----------
- Support for arrays
- Rename database
- Change database store path
- Complex Queries
- Implementation with other languages and terminal


How it works
--------------
I am too tired to type this out, the code is open source.. go read it
