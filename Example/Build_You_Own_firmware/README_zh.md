* [English version](/Example/Build_You_Self_firmware/README.md)
# 构建自己的固件
## 工程设置
### CubeIDE
1. 修改Ld文件，增加`NOINIT_RAM`不初始化分区，地址：0x20000000，大小0x08。
2. 修改Ld文件，FLASH地址改为0x8006800，大小49K。
3. 增加bootloader.c、bootloader.h、perf_counter.c、perf_counter.h文件。
4. main函数开头增加`bootloader_init()`。
5. 需要进入固件升级模式时，调用`bootloader_enter_update_mode()`即可。

### Keil
1. 修改设置，见下图  
![display](/Images/keil.png)
2. 增加bootloader.c、bootloader.h、perf_counter.c、perf_counter.h文件。
3. main函数开头增加`bootloader_init()`。
4. 需要进入固件升级模式时，调用`bootloader_enter_update_mode()`即可。

## 固件打包
* 打开Tools/firmware_packager工具，选择相应固件，勾选不加密，添加字符水印，选择表头尺寸后，点击打包即可
![display](/Images/firmware_packager_zh.png)