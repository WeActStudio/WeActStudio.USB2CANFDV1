* [中文版本](/Example/Build_You_Own_firmware/README_zh.md)
# Build your own firmware
## Project Setup
### CubeIDE
1. Modify Ld file, add `NOINIT_RAM` without initializing partition, address: 0x20000000, size 0x08.
2. Modify Ld file, FLASH address to 0x8006800, size 49K.
Add bootloader.c, bootloader.h, perf_counter.c, perf_counter.h files.
4. Add `bootloader_init()` at the beginning of the main function.
5. Need to enter the firmware upgrade mode, call `bootloader_enter_update_mode`.

### Keil
1. Change the Settings as shown below
![display](/Images/keil.png)
Add bootloader.c, bootloader.h, perf_counter.c, perf_counter.h files.
3. Add `bootloader_init()` at the beginning of the main function.
4. To enter firmware upgrade mode, simply call `bootloader_enter_update_mode()`.

## Firmware packaging
* Open Tools/firmware_packager, select the firmware, check Do not encrypt, add character watermark, select the header size, and click Pack.
![display](/Images/firmware_packager_en.png)