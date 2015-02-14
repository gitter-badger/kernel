#include <summit.h>
#include <multiboot.h>

#if defined(__cplusplus)
extern "C" /* Use C linkage for kernel_main. */
#endif

void kernel_main(multiboot_info_t* mb_info, unsigned int magic)
{	

	terminal_initialize();
	if ( magic == MULTIBOOT_BOOTLOADER_MAGIC ) {
		printf("Booted with multiboot. %d == %d\n", magic, MULTIBOOT_BOOTLOADER_MAGIC );
	}
}	