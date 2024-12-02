import os
import random
import datetime
import json
import time

l_target_path = "C:\\Users\\sreen\\OneDrive\\Desktop\\Python\\BillingSystem\\bill/"
while True :
    l_store_id = random.randint(1,4)
    now = datetime.datetime.now()
    l_bill_id = now.strftime("%Y%m%d%H%M%S")


    start_date = datetime.date(2000, 1, 1)
    end_date = datetime.date(2020, 1, 1)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)

    l_date = start_date + datetime.timedelta(days = random_number_of_days)
    l_bill_details = {}
    bill_details = []

    for i in range(random.randint(1,25)):
        l_prod_id = random.randint(1,25)
        l_qty = random.randint(1,20)
        l_bill_details[l_prod_id] = l_qty
 
        # l_bill_details[2]["prod_id"] = l_prod_id
        # l_bill_details[2]["prod_qty"]= l_qty
        # print(l_bill_details)
        # bill_details.append(l_bill_details) 
        # print(bill_details)
    # print(bill_details)
    # time.sleep(30)
              
    l_data = { "bill_id" : l_bill_id
              ,"store_id" : l_store_id
              ,"bill_date" : l_date
              ,"bill_details" : l_bill_details}
            
    #print(l_data) ---prints the dictionary output in single quote, json format the key should be double quotes
    # hence need to use json.dumps(dictionary)
    # Serializing json   
    json_object = json.dumps(l_data, default = str) #default = str is to get the datetime value
    print(json_object) 
    
    new_file = open (l_target_path + l_bill_id + ".json", "w")
    new_file.write(str(json_object))
    new_file.close()

    time.sleep(3)