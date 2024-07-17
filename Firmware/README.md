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