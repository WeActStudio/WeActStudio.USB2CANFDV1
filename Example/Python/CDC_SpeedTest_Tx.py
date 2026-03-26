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

aux_device_ser = serial.Serial('COM43', 1152000, 8, 'N', 1,timeout=1)

aux_device_ser.write("S8\r".encode('utf-8'))
aux_device_ser.write("Y5\r".encode('utf-8'))
aux_device_ser.write("O\r".encode('utf-8'))
print('port_open ',aux_device_ser.port,aux_device_ser.read_until())

tick_1s = int(round(time.time() * 1000)) + 1000
tx_data_len = 0
rx_data_len = 0
test_frame_count = 100
test_frame = ("b000F"+"aabb"*32+"\r")*test_frame_count
test_write = test_frame.encode('utf-8')
tx_Success = 0
while True:
    aux_device_ser.write(test_write)

    data = aux_device_ser.read(test_frame_count)

    if data == ('\r'*test_frame_count).encode('utf-8'):
        tx_Success = tx_Success + test_frame_count

    rx_data_len = rx_data_len + len(data)
    tx_data_len = tx_data_len + len(test_write)

    ms = int(round(time.time() * 1000))
    if ms > tick_1s:
        tick_1s = ms + 1000
        print('tx speed:',tx_data_len,'Byte/S',tx_data_len/1024,'kByte/S')
        print('tx_Success:',tx_Success)
        print('rx speed:',rx_data_len,'Byte/S',rx_data_len/1024,'kByte/S')
        print('')
        tx_data_len = 0
        rx_data_len = 0

        if check_key_thread.is_alive() == False:
            break

aux_device_ser.write("C\r".encode('utf-8'))
aux_device_ser.read_until(expected='\r'.encode('utf-8'))
aux_device_ser.close()