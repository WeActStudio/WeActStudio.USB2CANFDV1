import serial
import time
import threading

def check_key():
    while True:
        if input() == 'q':
            print("quit now")
            break

check_key_thread = threading.Thread(target=check_key)
check_key_thread.start()

aux_device_ser = serial.Serial('COM33', 1152000, 8, 'N', 1,timeout=1)

aux_device_ser.write("S8\r".encode('utf-8'))
aux_device_ser.write("Y5\r".encode('utf-8'))
aux_device_ser.write("O\r".encode('utf-8'))
print('port_open ',aux_device_ser.port,aux_device_ser.read_until())

tick_1s = int(round(time.time() * 1000)) + 1000
test_len = 0
data_len = 0
test_write = "b0008aabbaabbaabbaabb\r".encode('utf-8')
tx_Success = 0
while True:
    aux_device_ser.write(test_write)
    # time.sleep(0.001)
    # data = aux_device_ser.read_all()
    data = aux_device_ser.read_until(expected='\r'.encode('utf-8'))
    if data == '\r'.encode('utf-8'):
        tx_Success = tx_Success + 1
    data_len = data_len + len(data)
    test_len = test_len + len(test_write)
    # print(aux_device_ser.port,data,len(data))

    ms = int(round(time.time() * 1000))
    if ms > tick_1s:
        tick_1s = ms + 1000
        print('tx speed:',test_len,'Byte/S',test_len/1024,'kByte/S')
        print('tx_Success:',tx_Success)
        print('rx speed:',data_len,'Byte/S',data_len/1024,'kByte/S')
        print('')
        test_len = 0
        data_len = 0

        if check_key_thread.is_alive() == False:
            break

aux_device_ser.write("C\r".encode('utf-8'))
aux_device_ser.read_until(expected='\r'.encode('utf-8'))
aux_device_ser.close()