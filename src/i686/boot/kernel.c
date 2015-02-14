#include <summit.h>
#include <multiboot.h>

#if defined(__cplusplus)
extern "C" /* Use C linkage for kernel_main. */
#endif
void kernel_main(multiboot_info_t* mb_info, unsigned int magic)
{
	terminal_initialize();
	terminal_writestring("Multiboot info: ");
	terminal_writestring("Hello, kernel World!\nDoes breakline work now?\nI'll take this as a yes.");
}	