#User Model
# Attributes of a user: name, balance, owed_to list and owed_by list

class user:
    def __init__(self, name, group):
        self.name=name
        self.group=group
        self.owed_to=[]
        self.owed_by=[]
        self.balance=None
    def addOwed_to(self, owed_to:str, amount:int):
        dic={}
        dic[owed_to]=amount
        self.owed_to.append(dic)
    def addOwed_by(self, owed_by:str, amount):
        dic={}
        dic[owed_by]=amount
        self.owed_by.append(dic)
    def addBalance(self, amount):
        self.balance=amount
