* [中文版本](./README_zh.md)
# Tool Version Description
## cangaroo
### V0.2.4
* Initial version
### V0.2.4.1
1. Fix software startup measurement crash after device removal.
2. Fixed 800kbps baud rate setting error problem.
3. Optimize the custom baud rate function to support more baud rates (firmware version must be ≥`V1.0.0.3`).
4. Add the firmware version printing function, see the Log window.
5. Add more common baud rate options.
### V0.2.4.2
1. Add USB2CANFDV2 device support.
2. Add CAN sample rate options (50%, 62.5%, 75%) and CANFD sample rate options (87.5%).
3. Add a few parameters to display.
4. Fix the bug.
### V0.2.4.3
1. Added frame filtering function.
2. Added enhanced SLCAN mode to improve transmission efficiency.
3. Optimized serial port data processing logic.
4. Fixed some logic issues in the transmit window.
5. Optimized the device configuration window.
6. add app version display,fix some bugs

## WeActStudio_Upgrade_Tool
For firmware upgrade
### How to Upgrade, Windows
1. Extract WeActStudio_Upgrade_Tool.7z
2. Run WeActStudio_Upgrade_Tool.exe
3. Connect the device using a data cable
4. Select the fpk firmware
5. Open the serial port
6. Click the "Send" button to start the upgrade

### How to Upgrade, Linux , macOS or Windows
1. Extract WeActStudio_Upgrade_Tool_Python.zip
2. Connect the device using a data cable
3. Run WeActStudio_Upgrade_Tool.py, need to install pyserial library  
Example: python WeActStudio_Upgrade_Tool.py firmware.fpk
4. Wait for the upgrade to complete.

## firmware_packager
Firmware packaging tool, so that firmware support using the `WeActStudio_Upgrade_Tool` tool burning