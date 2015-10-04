/*
 * =====================================================================================
 *
 *       Filename:  exploitable.c
 *
 *        Version:  1.0
 *        Created:  09/27/2015 12:32:05 AM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Taishi Nojima (tn246), taishi.nojima@yale.edu
 *
 * =====================================================================================
 */
#include    <stdio.h>
#include    <stdlib.h>
#include    <assert.h>
#include	<string.h>

int main (int argc, char **argv){
	char msg[1024];
	static int test_value = 72, next_value = 0x11111111;

	strcpy(msg, argv[1]);

	printf(msg);
	printf("\n");

	printf("[DEBUG] test_value @ 0x%08x = %d 0x%08x\n", (int)&test_value, test_value, test_value );
	printf("[DEBUG] next_value @ 0x%08x = %d 0x%08x\n", (int)&next_value, next_value, next_value );
	int (*ret)() = (int(*)())next_value;
	ret();
		return 0;
}

/*
 * canopus@canopus:~/blackhat_python/pwn/format_str|master
 * ⇒  ./shellcode AAAA%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.
 * AAAAbffff7c1.1a81d4.1a81d4.1a81d4.8.4c.41414141.252e7825.78252e78.2e78252e.252e7825.78252e78.2e78252e.252e7825.
 * [DEBUG] test_value @ 0x0804a028 = -72 0xffffffb8
 * [DEBUG] next_value @ 0x0804a02c = 286331153 0x11111111
 * [2]    921 segmentation fault (core dumped)  ./shellcode AAAA%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.
 *
 * canopus@canopus:~/blackhat_python/pwn/format_str|master
 * ⇒  ./shellcode $(python fmt_exploit.py ./shellcode 7 0804a02c bfffff8d)))]]]
 */
