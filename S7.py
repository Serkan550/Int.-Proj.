import snap7

IP = '192.168.100.100'  #IP Address
RACK = 0    #Where PLC is located
SLOT = 1    #Where CPU is located

DB_NUMBER = 100
START_ADDRESS = 0
SIZE = 259

#Create a client
plc = snap7.client.Client()

#Connect to a server
plc.connect(IP, RACK, SLOT)

plc_info = plc.get_cpu_info()
print(f'Module Type : {plc_info}')

plc_state = plc.get_cpu_state()
print(f'CPU State : {plc_state}')
"""
db = plc.db_read(DB_NUMBER, START_ADDRESS, Destination)
#snap7.util.set_bool(db, 0, True)
#plc.db_write(DB_NUMBER, START_ADDRESS, SIZE, db)

product_name = db[0:20].decode('utf-8').strip('\x00')
print(f'Product Name : {product_name}')

plc_time = plc.get_plc_datetime()
print(f'PLC Time : {plc_time}')

def read_db(db_number, start_address, size):
    db = plc.db_read(db_number, start_address, size)
    return db

snap7.util.get_date_time_object(db)

def write_db(db_number, start_address, size, data):
    plc.db_write(db_number, start_address, size, data)
"""
