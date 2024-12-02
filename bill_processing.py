import os
import json
import datetime
import time
import cost

# # Read Fil
input_file = open("C:\\Users\\sreen\\OneDrive\\Desktop\\Python\\BillingSystem\\bill/20210421125844.json","r")
var_text = input_file.read()
# # Print the data in one go
print("------------------------Input Data from json--------------------------")        
print(var_text)
# # Close the File stream handler
input_file.close()

# Parse JSON using "loads" Method
y = json.loads(var_text)

# Get Subset of JSON
data = (y["bill_details"])
b_prod_id = data["prod_id"]
b_prod_qty = data["prod_qty"]
billed_data = {}
billed_details ={}
   
for s in range(len(cost.l_cost)):
    if cost.l_cost[s]["prod_id"] == b_prod_id :
        bill_item = b_prod_qty * cost.l_cost[s]["prod_cost"]
        billed_details["prod_id"] = b_prod_id
        billed_details["prod_qty"] = b_prod_qty
        billed_details["prod_cost"] = cost.l_cost[s]["prod_cost"]
        billed_details["total_bill_per_item"] = bill_item
    
    
    billed_data = { "bill_id" : y["bill_id"]
                  ,"store_id" : y["store_id"]
                  ,"bill_date" :y["bill_date"]
                  ,"bill_details" : billed_details}

print("-----------------------------Billed Data-----------------------------")        
print(billed_data)

# # JSON Nested value, Get First Product
# print(y["BillDetails"][0]["Product"])

# JSON Get All Products
# for entries in y["bill_details"]:
    # Total cost = entries[
    # print(restaurant["Product"])

         