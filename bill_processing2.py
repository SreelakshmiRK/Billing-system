import os
import json
import datetime
import time
import cost
import glob   

# # Read Fil
in_path = "C:\\Users\\sreen\\OneDrive\\Desktop\\Python\\BillingSystem\\bill/*.json"
b_target_path = "C:\\Users\\sreen\\OneDrive\\Desktop\\Python\\BillingSystem\\processed_bill/"
files=glob.glob(in_path)   
for file in files:     
    f=open(file, 'r')  
    var_text = f.read()
    # # Print the data in one go
    print("------------------------Input Data from json--------------------------")        
    print(var_text)       
    f.close() 
    # Parse JSON using "loads" Method
    y = json.loads(var_text)

    # Get Subset of JSON
    data = (y["bill_details"])

    billed_details ={}
    bill = []
    total_bill = 0

    for key, value in data.items():
        b_prod_id = key
        b_prod_qty = value

        for s in range(25):

            if (cost.l_cost[s]["prod_id"] == int(b_prod_id)) :
                bill_item = b_prod_qty * cost.l_cost[s]["prod_cost"]            
                prod_cost= cost.l_cost[s]["prod_cost"]
                billed_details["prod_id"] = b_prod_id
                billed_details["prod_qty"] = b_prod_qty            
                billed_details["cost_per_unit"] = prod_cost
                billed_details["product_cost"] = bill_item  
                total_bill = total_bill + bill_item
                bill.append(billed_details.copy())   
        
    billed_data = { "bill_id" : y["bill_id"]
                   ,"store_id" : y["store_id"]
                   ,"bill_date" :y["bill_date"]
                   ,"final_bill" : total_bill
                   ,"bill_details" : bill}      

    print("-----------------------------Billed Data-----------------------------")        
    # print(billed_data)

    json_object = json.dumps(billed_data, default = str) #default = str is to get the datetime value
    print(json_object) 
     
    new_file = open(b_target_path + y["bill_id"] + ".json", "w")
    new_file.write(str(json_object))
    new_file.close()

    #time.sleep(3)

         