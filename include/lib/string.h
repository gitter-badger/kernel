#ifndef SUMMIT_STRINGS_H
#define SUMMIT_STRINGS_H

char* itoa(int val, int bas);
int memcmp(const void*, const void*, size_t);
void* memcpy(void* __restrict, const void* __restrict, size_t);
void* memmove(void*, const void*, size_t);
void* memset(void*, int, size_t);
size_t strlen(const char*);

int printf(const char* __restrict, ...);
int putchar(int);
int puts(const char*);
#endif