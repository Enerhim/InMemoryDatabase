import json
import os

class Database:
    def __init__(self, name: str) -> None:
        self.name = name.replace(" ", "-")

class MemoryDatabase(Database):
    def __init__(self, name: str) -> None:
        Database.__init__(self, name=name)
        self.data = {"config": {"name": self.name}}
        self.backupData = {}
        
    def addKey(self, key : str, value):
        self.backupData = self.data
        
        if key in self.data:
            return{f"Key {key} already exists"}
        else:
            self.data[key] = value
            return {key: self.data[key]}
            
    def deleteKey(self, key : str):
        self.backupData = self.data
        
        del self.data[key]
        return self.data
      
    def updateKey(self, key : str, value):
        self.backupData = self.data
        
        if key in self.data:
            self.data[key] = value
            return {key: self.data[key]}
        else: 
            return{f"Key {key} doesnt exist"}            
            
    def getKeys(self, keys : str):
        data_to_ret = {}
        
        for key in keys:
            if key in self.data: data_to_ret[key] = self.data.get(key)
            else: data_to_ret[key] = None
        
        return data_to_ret
    
    def getKey(self, key : str):
        data_to_ret = {}
        
        if key in self.data: data_to_ret[key] = self.data.get(key)
        else: data_to_ret[key] = None 
        
        return data_to_ret
    
    def getAllKeys(self):
        return self.data
    
    def save(self, override=False):
        self.backupData = self.data
        
        if os.path.exists(f"db_list/{self.name}.json"):
            if override:
                with open(f"db_list/{self.name}.json", 'w') as fp:
                    json.dump(self.data, fp)
                return {f"db_list/{self.name}.json already exists. Overriding"}
            else:
                return {f"db_list/{self.name}.json already exists. Use 'save override' to override changes"}
        else:
            with open(f"db_list/{self.name}.json", 'w') as fp:
                json.dump(self.data, fp)
        
        return {f"Saved to db_list/{self.name}.json"}
            
    def load(self):
        self.backupData = self.data
        
        with open(f'db_list/{self.name}.json', 'r') as fp:
            self.data = json.load(fp)
        
        return {f"Loaded db_list/{self.name}.json"}
    
    def undoChange(self):
        self.data = self.backupData
        return self.data
                
    def __repr__(self) -> str:
        return str(self.data)