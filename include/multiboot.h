#ifndef SUMMIT_MULTIBOOT_H_
   #define SUMMIT_MULTIBOOT_H_

   #define MULTIBOOT_HEADER_MAGIC 0x1BADB002

   #ifdef __ELF__
      #define MULTIBOOT_HEADER_FLAGS 0x00000003
   #else
      #define MULTIBOOT_HEADER_FLAGS 0x00010003
   #endif

   #define MULTIBOOT_BOOTLOADER_MAGIC 0x2BADB002

   #define STACK_SIZE 0x4000
   #ifndef ASM

   typedef struct multiboot_header
   {
      unsigned long magic;
      unsigned long flags;
      unsigned long checksum;
      unsigned long header_addr;
      unsigned long load_addr;
      unsigned long load_end_addr;
      unsigned long bss_end_addr;
      unsigned long entry_addr;
   } multiboot_header_t;

   typedef struct aout_symbol_table
   {
      unsigned long tabsize;
      unsigned long strsize;
      unsigned long addr;
      unsigned long reserved;
   } aout_symbol_table_t;

   typedef struct elf_section_header_table
   {
      unsigned long num;
      unsigned long size;
      unsigned long addr;
      unsigned long shndx;
   } elf_section_header_table_t;

   typedef struct multiboot_info
   {
      unsigned long flags;
      unsigned long mem_lower;
      unsigned long mem_upper;
      unsigned long boot_device;
      unsigned long cmdline;
      unsigned long mods_count;
      unsigned long mods_addr;
      union {
         aout_symbol_table_t aout_sym;
         elf_section_header_table_t elf_sec;
      } u;
      unsigned long mmap_length;
      unsigned long mmap_addr;
   } multiboot_info_t;

   typedef struct module
   {
      unsigned long mod_start;
      unsigned long mod_end;
      unsigned long string;
      unsigned long reserved;
   } module_t;

   typedef struct memory_map
   {
      unsigned long size;
      unsigned long base_addr_low;
      unsigned long base_addr_high;
      unsigned long length_low;
      unsigned long length_high;
      unsigned long type;
   } memory_map_t;

   #endif

#endif