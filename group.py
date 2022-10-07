#Group object model
from user import user
from balance import doBalancing
class group:
   
    def __init__ (self, name: str, members: list):
        self.name=name
        self.memb=members
        self.list_expenses={}
    def addexpense(self, expense_name, value, paid_by: dict, owed_by :dict):
        
        expense={}
        expense["name"]=expense_name
        expense["value"]=value
        expense["paid_by"]=paid_by
        expense["owed_to"]=owed_by
        
        #adding missing users in the group 
        for key in paid_by:
            if key not in self.memb:
                self.memb.append(key)
        for key in owed_by:
            if key not in self.memb:
                self.memb.append(key)
        
        #Find each and every users actual owed price
        eql=value/(len(paid_by)+len(owed_by))
        expense_balance={}
        for key in paid_by:
            expense_balance[key]=eql-paid_by[key]
        for key in owed_by:
            expense_balance[key]=eql
        expense["expense_balance"]=expense_balance
        self.list_expenses[expense_name]=expense


    #Creating a balancesheet using all expense and finding balance of all users returning a dictionary to balance it
    def checkbalance(self):
        balance={}
        for key in self.list_expenses:
            expense=self.list_expenses[key]
            expense_balance=expense["expense_balance"]
            for name in expense_balance:
                if name in balance:
                    balance[name]= expense_balance[name]+balance[name]
                else:
                    balance[name]=expense_balance[name]
        return balance
        
        
    

    def update(self, expense_name, value, paid_by, owed_by):
        if expense_name in self.list_expenses:
            del self.list_expenses[expense_name]
            expense={}
            expense["name"]=expense_name
            expense["value"]=value
            expense["paid_by"]=paid_by
            expense["owed_by"]=owed_by
            self.list_expenses[expense_name]=expense
            eql=value/(len(paid_by)+len(owed_by))
            expense_balance={}
            for key in paid_by:
                expense_balance[key]=eql-paid_by[key]
            for key in owed_by:
                expense_balance[key]=eql
            expense["expense_balance"]=expense_balance
            self.list_expenses[expense_name]=expense
    
    def delete(self, expense_name):
        if expense_name in self.list_expenses:
            del self.list_expenses[expense_name]






    



    
    
        
        
    
 


       

    
        
    
   


    
    

    


      



