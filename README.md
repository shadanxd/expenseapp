
# EXPENSE SPLITTING APP

A flask API to add mulitple expenses among friend group and split among each other equally


## Installation

Ensure python3 and pip installed in the system
Install splitting app using pip

```bash
  pip install flask
  cd splitapp
```

## Run 

By default app runs on port:5000

```bash
  python3 app.py
```
    
## API Reference


1. Create Group 
2. Add expense in the Group
3. Update expense in  a Group
4. Delete expense in  a Group
5. Get balance of each user who owes whom in a particular group

#### 1. Create Group

```http
  POST /createGroup
```
#### json raw input
```JSON
  { 
      "name": "<Group Name>",
      "members": ["Member1", "Member2"]
  }
```


#### 2. Add Expense

```http
  POST /expense/<group_name>
```
#### json raw input
```JSON
 {
    "expense_name":"<item name>",
    "value": <amount>,
    "paid_by": {"Member1":<amount>, "Member2":<amount>},
    "owed_by":{"Member3":<amount>, "Member4":<amount>}
  }
```
#### 3. Update Expense

```http
  PUT /expense/<group_name>/<expense_name>
```
#### json raw input
```JSON
 {
    "value": <amount>,
    "paid_by": {"Member1":<amount>, "Member2":<amount>},
    "owed_by":{"Member3":<amount>, "Member4":<amount>}
  }
```
#### 4. Delete Expense in a group

```http
  DELETE /expense/<group_name>/<expense_name>
```
#### 5. Get balance of each group

```http
  GET /balance/<group_name>
```




