* [中文版本](./README_zh.md)
# Firmware description
## Bootloader
If you want to restore the factory firmware, You can download the bootloader: `bootloader_stm32g0_2_fix_uid_user.Hex`, and modify the `Option bytes` parameter, the specific steps are as follows:
1. Download the Bootloader.
2. Modify the Option bytes parameter.
3. Power off the device, and then power on.
4. Open `WeActStudio_Upgrade_Tool`, select the fpk format upgrade package, and write.
5. If TX/RX blinks for 1 second, the factory firmware is restored successfully.
```
The Option bytes parameters
RDP = BB
BOR_EN = Checked
BORF_LEV = 3
BORR_LEV = 3
PCROP1A_STRT = 0x04
PCROP1A_END = 0x33
PCROP_RDP = Checked
WRP1A_STRT = 0x0
WRP1A_END = 0x1
```

## SLCAN version description
### V1.0.0.1
* Initial version
### V1.0.0.2
1. Optimize the USB serial number naming rule to avoid repetition. (In later versions, if an upgrade failure message is displayed, the device needs to short-circuit DIO and GND pins and power on to forcibly enter the firmware upgrade mode)
2. Fix the abnormal TX/RX indicator display Bug, and optimize the logic: If the sending and receiving period is less than 50mS, it is always on.
### V1.0.0.3
1. Add more common baud rate commands.
2. The custom baud rate command supports the clock frequency division function.
3. The `S7\r` command changes the baud rate from 750kbps to 800Kbps.
### V1.0.0.4
1. Improve the USB CDC receive and send performance.
2. Fix the error code 0x07 when the USB CDC receives a large amount of data.
3. Adjust the USB CDC send timeout logic, and do not disconnect the USB connection when the timeout occurs.
4. Update the HAL library to the latest version.
### V1.0.0.5
1. Fixed the issue where the device returned the 0x07 error code when it did not send a frame but received an erroneous frame.
### V1.0.0.6
1. Adjusted the transmit and receive buffer packet sizes for CAN and USB from 16 to 128.
2. Fixed the inconsistency between the remote frame protocol and actual implementation.
3. Added frame filtering functionality.
4. Added enhanced SLCAN mode to improve transmission efficiency.
5. Optimized USB data processing logic.
