/*
 * =====================================================================================
 *
 *       Filename:  redpill.c
 *
 *        Version:  1.0
 *        Created:  05/12/2015 11:01:39 AM
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


int main (int argc, char **argv){
	unsigned char m[2+4], rpill[] = "\x0f\x01\x0d\x00\x00\x00\x00\xc3";
	*((unsigned *) &rpill[3]) = (unsigned)m;
	((void(*)())&rpill)();

	printf("idt base: %#x\n", *((unsigned*)&m[2]));

	if (m[5]>0xd0) {
		printf("Inside Matrix!\n");
	}else {
		printf("Not in Matrix.\n");
	}
	
		return 0;
}

