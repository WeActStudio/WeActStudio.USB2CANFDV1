#ifndef __BOOTLOADER_H
#define __BOOTLOADER_H

#ifdef __cplusplus
extern "C"
{
#endif

#include "main.h"

#define FIRMWARE_UPDATE_VAR_ADDR            0x20000000

#define FIRMWARE_UPDATE_MAGIC_WORD          0xA5A5A5A5      /* 固件需要更新的特殊标记（不建议修改，一定要和 APP 一致） */
#define FIRMWARE_RECOVERY_MAGIC_WORD        0x5A5A5A5A      /* 需要恢复出厂固件的特殊标记（不建议修改，一定要和 APP 一致） */
#define BOOTLOADER_RESET_MAGIC_WORD         0xAAAAAAAA      /* bootloader 复位的特殊标记（不建议修改，一定要和 APP 一致） */

void bootloader_init(void);
uint64_t bootloader_get_update_flag(void);
void bootloader_enter_update_mode(void);
char *bootloader_get_version(void);

#ifdef __cplusplus
}
#endif

#endif
