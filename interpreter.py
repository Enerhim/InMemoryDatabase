from database import *
import shlex

class Interpreter:
    def __init__(self) -> None:
        self.req_types = [
            "add","delete","update","undo","get","save","load","config","duplicate"
        ]
    
    def lex(self, q: str):
        q = shlex.split(q)
        lexed_q = {}
        lexed_q["req_type"] = q[0]
        lexed_q["args"] = q[1:]
        return lexed_q
    
    def execute(self, database, q : dict):
        if q["req_type"].lower() in self.req_types:
            
            rq_type = q["req_type"].lower()
            args = q["args"]
            
            if rq_type == "add":
                return database.addKey(args[0], args[1])
            elif rq_type == "delete":
                return database.deleteKey(args[0])
            elif rq_type == "update":
                return database.updateKey(args[0], args[1])
            elif rq_type == "undo":
                return database.undoChange()
            elif rq_type == "get":
                if len(args) == 0:
                    return database.getAllKeys()
                elif len(args) == 1:
                    return database.getKey(args[0])
                elif len(args) > 1:
                    return database.getKeys(args[0:])
            elif rq_type == "save":
                try:
                    if args[0].lower() == "override":
                        return database.save(override=True)
                except IndexError: 
                    return database.save(override=False)
            elif rq_type == "load":
                return database.load()
            elif rq_type == "config":
                if args[0] == "save_path":
                    database.savePath = args[1]
                    return {database.savePath}
                elif args[0] == "name":
                    database.rename(args[1])
                    return {database.name}
                    