from user import user
class doBalancing:
    def __init__(self, list1:dict, group):
        self.list_of_users={} #List of memebers in each group to calculate who owes whom
        self.lis=list1 #Passed balance sheet from group class to balance among users
        self.group=group #group name
        self.balance()
    def balance(self):
        #Sorting users according to their balances
        lis2=dict(sorted(self.lis.items(), key= lambda x:x[1]))
        key=[]
        value=[]
        n=0
        m=0
        #Retrieving users and their balance from sorted list to calculate cash flow
        for ket in lis2:
            key.append(ket)
            value.append(lis2[ket])
            
        
        for i, k in enumerate(key):
            #creating user objects from the balance sheet and maintaining a list of users with their attributes
            newuser=user(k, self.group)
            newuser.addBalance(value[i])
            self.list_of_users[k]=newuser
            if value[i]>0:
                n+=1
            if value[i]<=0:
                m+=1

      
   
        #Running a loop in sorted list balance list from positive to negative and distribute the cash
        i= len(key)-1
        j=0
        while i>=len(key)-n:
            while j<m:
                
                if abs(value[j])>abs(value[i]):
                    useri=self.list_of_users[key[i]] #Retriving users from user list and filling their attributes of who owes to whom
                    userj=self.list_of_users[key[j]]
                    useri.addOwed_to(key[j], abs(value[i]))
                    userj.addOwed_by(key[i], abs(value[i]))
            
                    value[j]=value[i]+value[j]

            
                    value[i]=0
                    i-=1
                if abs(value[j])<abs(value[i]):
                    useri=self.list_of_users[key[i]]
                    userj=self.list_of_users[key[j]]
                    useri.addOwed_to(key[j], abs(value[j]))
                    userj.addOwed_by(key[i], abs(value[j]))

                    value[i]=value[i]+value[j]
            
                    value[j]=0
                    j+=1
                if (abs(value[j])==abs(value[i])) and (key[i]!=key[j])and (value[i]!=0) and value[j]!=0:
                    useri=self.list_of_users[key[i]]
                    userj=self.list_of_users[key[j]]
            
                    useri.addOwed_to(key[j], abs(value[i]))
                    userj.addOwed_by(key[i], abs(value[j]))
                    value[i]=0
                    value[j]=0
                    i-=1
                    j+=1
                else:
                    continue
