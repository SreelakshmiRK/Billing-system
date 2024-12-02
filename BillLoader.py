import datetime
import os
import shutil
import pymysql
import json
from pathlib import Path



# Update the data to set qty for all products to 1
# update Products set qty = 1;
# commit;


#
l_bills_path = "C:/Users/sreen/OneDrive/Desktop/Python/BillingSystem/bills/"
l_processed_path = "C:/Users/sreen/OneDrive/Desktop/Python/BillingSystem/processed_bills/"
l_errors_path = "C:/Users/sreen/OneDrive/Desktop/Python/BillingSystem/error_bills/"

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='inventorymanagement', cursorclass=pymysql.cursors.DictCursor)
cursor = conn.cursor()

l_bill_insert = "insert into billdata ( bill_id, store_id, bill_date) values ({0},{1},STR_TO_DATE('{2}','%Y-%m-%d %H:%i%s'));"
l_bill_det_insert = "insert into billdetails (billdetail_id, bill_id, prod_id,qty,line_total) values ({0},{1},{2},{3},{4});"
l_bill_update = "update billdata set bill_total={0} where bill_id ={1};"

# # generate price dictionary


# # while True:
    # entries = os.listdir(l_bills_path)
entries = ["20210422160511.json","20210422160514.json"]



for file_name in entries:
    with open(l_bills_path + file_name, 'r') as f:
        data = f.read()
        print(data)
        dataj = json.loads(data)
        f.close() 
        print(dataj["bill_id"])
        print(dataj["store_id"])
        print(dataj["bill_date"])
        billed_details ={}
        bill = []
        # Validate Data, generate errors if any
        # If errors Move "l_bills_path + file_name" into "l_errors_path"        
        # Load the "data" into DB Tables, Bill / Bill Details
        # insert into Bill
        # insert into BillDetails
        # Update billdetails.line_total and bill.bill_total
        try:
            print(l_bill_insert.format(dataj["bill_id"],dataj["store_id"],dataj["bill_date"]))
            cursor.execute(l_bill_insert.format(dataj["bill_id"],dataj["store_id"],dataj["bill_date"]))
            conn.commit()
        except:
            log.critical('JSON File '+ file_name + ' load failed!!')
            shutil.move(l_bills_path + file_name, l_errors_path)
            # Move "l_bills_path + file_name" into "l_errors_path + file_name"
        else:    
            x = 0
            for product_id, qty in dataj["bill_details"].items():
                x+=1
                total_bill = 0
                cursor.execute ('select * from products where prod_id = %s',product_id)
                row = cursor.fetchone()
                cost_per_item = row['price']
                line_total = qty * cost_per_item  
                total_bill = total_bill + line_total
   

                try:
                    print(l_bill_det_insert.format(int(dataj["bill_id"])+x,dataj["bill_id"],product_id,qty,line_total))
                    cursor.execute(l_bill_det_insert.format(int(dataj["bill_id"])+x,dataj["bill_id"],product_id,qty,line_total))
                    conn.commit()
                    cursor.execute(l_bill_update.format(total_bill,dataj["bill_id"]))
                    conn.commit()
                  
                    #delete from billdetails where bill_id = dataj["bill_id"];
                    #delete from bill where bill_id = dataj["bill_id"];

                except:
                    log.critical('JSON File '+ file_name + ' load failed!!')
                    shutil.move(l_bills_path + file_name, l_errors_path)
                    # Move "l_bills_path + file_name" into "l_errors_path + file_name"
                else:
                    for fname in os.listdir(l_processed_path):
                        if os.path.isfile(l_processed_path + file_name): 
                            pass
                            # os.remove(l_bills_path + file_name)
                            # shutil.move(l_bills_path + file_name, l_processed_path)
                        else: 
                            shutil.move(l_bills_path + file_name, l_processed_path)
                    # Move "l_bills_path + file_name" into "l_processed_path + file_name"

    # -- update line total
    # -- update bill total
    
    # time.sleep(60)
cursor.close()
conn.close()