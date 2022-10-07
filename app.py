from balance import doBalancing
from flask import Flask, request, jsonify
from group import group
import requests
import json
import threading 
import time
#Init app

app=Flask(__name__)

#List of multiple groups
group_list={}


#Ensuring thread lock during a ongoing process
sem=threading.Semaphore()

#Creating group
@app.route('/createGroup', methods=['POST'])
def create():
    
    group_name=request.json['name']
       
    mem_list=request.json['members']
    
        
    grp=group(group_name, mem_list)
    group_list[group_name]=grp
    
    return jsonify(grp.name, grp.memb)


#Adding expense in a given group 
@app.route('/expense/<group_name>', methods=['POST'])
def addExp(group_name):
    sem.acquire()
    if group_name not in group_list:
        return jsonify("Group Not Found")
    if group_name in group_list:
        grp=group_list[group_name]
        expense_name=request.json['expense_name']
        value=request.json['value']
        paid_by=request.json['paid_by']
        owed_by=request.json['owed_by']
        grp.addexpense(expense_name, value, paid_by, owed_by)
        sem.release()
        return jsonify(grp.list_expenses[expense_name])
   

#Updating an expense in given group and using expense name
@app.route('/expense/<group_name>/<expense_name>', methods=['PUT'])
def updatExp(group_name, expense_name):
    sem.acquire()
    if group_name not in group_list:
        return jsonify("Group Not Found")
    if group_name in group_list:
        grp=group_list[group_name]
        
        value=request.json['value']
        paid_by=request.json['paid_by']
        owed_by=request.json['owed_by']
        grp.update(expense_name, value, paid_by, owed_by)
        print(type(paid_by))
        sem.release()
        return jsonify(grp.list_expenses[expense_name])
   

#delete an expense in  agroup using /group_name/expense_name
@app.route('/expense/<group_name>/<expense_name>', methods=['DELETE'])
def delete(group_name, expense_name):
    if group_name not in group_list:
        return jsonify("Group Not Found")
    if group_name in group_list:
        
        grp=group_list[group_name]
        if expense_name in grp.list_expenses:
            grp.delete(expense_name)
            return jsonify("Successfull")
        else:
            return jsonify("expense not found")
        
        
    
#Check Balance and user summary in  a group
@app.route('/balance/<group_name>', methods=['GET'])
def fetch(group_name):
    sem.acquire()
    if group_name not in group_list:
        return jsonify("Group Not Found")
    grp=group_list[group_name]
    balance={}
    balance=grp.checkbalance()
    balance_it=doBalancing(balance, group_name)
   
    users=balance_it.list_of_users
    ret={}
    ret["name"]=group_name
    bal={}
    ret["balances"]=bal
    for i in users:
        newbal={}
        
        newbal["total_balance"]=users[i].balance
        newbal["owed_to"]=users[i].owed_to
        newbal["owed_by"]=users[i].owed_by
        bal[users[i].name]=newbal

    sem.release()

    return json.dumps(ret, indent=4)
    

#Run Server

if __name__=='__main__':
       app.run(debug=True)
