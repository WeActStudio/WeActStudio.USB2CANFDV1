/*---------------------------------------
- WeAct Studio Official Link
- taobao: weactstudio.taobao.com
- aliexpress: weactstudio.aliexpress.com
- github: github.com/WeActStudio
- gitee: gitee.com/WeAct-TC
- blog: www.weact-tc.cn
---------------------------------------*/

#include "bootloader.h"
#include "perf_counter.h"
#include "stdio.h"

/* �̼����µı�־λ���ñ�־λ���ܱ����� */
#if   defined ( __CC_ARM )
volatile uint64_t update_flag __attribute__((at(FIRMWARE_UPDATE_VAR_ADDR), zero_init));

#elif defined (__ARMCC_VERSION) && (__ARMCC_VERSION >= 6100100)
		#define __INT_TO_STR(x)     #x
		#define INT_TO_STR(x)       __INT_TO_STR(x)
		volatile uint64_t update_flag __attribute__((section(".bss.ARM.__at_" INT_TO_STR(FIRMWARE_UPDATE_VAR_ADDR))));
#elif defined (__GNUC__)
		volatile uint64_t update_flag __attribute__((section(".no_init_ram")));
#else
		#error "variable placement not supported for this compiler."
#endif

/**
 * @brief  �����ʼ��ǰ��һЩ����
 * @note   ִ�е��˴����ں�ʱ���ѳ�ʼ��
 * @retval None
 */
void bootloader_init(void)
{
    /* �����ж�������󣬿������ж� */
    __IRQ_SAFE 
    {
		#if defined (__GNUC__)
    		SCB->VTOR = 0x08006800;
		#else
			extern int Image$$ER_IROM1$$Base;
			SCB->VTOR = (uint32_t)&Image$$ER_IROM1$$Base;
		#endif
    }
    __enable_irq();
}

uint64_t bootloader_get_update_flag(void)
{
	return update_flag;
}

void bootloader_enter_update_mode(void)
{
	update_flag = FIRMWARE_UPDATE_MAGIC_WORD;
  HAL_NVIC_SystemReset();
}

uint32_t version_addr;
char fw_version[40];
char *bootloader_get_version(void)
{
	char *version;
	version_addr = 1024*(50+26) - 16;
	version = (char *)version_addr;
	
	sprintf(fw_version,"WeAct Studio V%d.%d.%d.%d_%02x%02x%02x%02x\r",version[0],version[1],version[2],version[3],version[7],version[6],version[5],version[4]);
	
	return fw_version;
}
