* [English version](./README.md)
# 固件说明
## Bootloader
如果你想恢复出厂固件可以刷入这个Bootloader:`bootloader_stm32g0_2_fix_uid_user.Hex`,并修改`Option bytes`参数，具体步骤如下：
1. 刷入Bootloader
2. 修改Option bytes参数
3. 设备掉电，重新上电
4. 使用`WeActStudio_Upgrade_Tool`写入fpk格式升级包
5. 设备TX RX闪烁1秒，出厂固件恢复成功
```
Option bytes 参数如下
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

## SLCAN 版本说明
### V1.0.0.1
* 初始版本
### V1.0.0.2
1. 优化USB序列号命名规则，避免重复（后续版本，如提示升级失败，设备需要短接DIO和GND管脚上电强制进入固件升级模式）。
2. 修复TX/RX指示灯显示异常Bug，并优化逻辑：收发周期持续低于50mS为常亮。
### V1.0.0.3
1. 增加更多常用波特率命令。
2. 自定义波特率命令支持时钟分频功能。
2. S7\r 命令波特率由750kbps改为800Kbps。