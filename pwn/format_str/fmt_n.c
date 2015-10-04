/*
 * =====================================================================================
 *
 *       Filename:  fmt_n.c
 *
 *        Version:  1.0
 *        Created:  10/03/2015 08:57:04 PM
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
	int A = 5, B = 10, count_one, count_two;

	printf("The number of bytes written up to here X%n is stored in count_one, and the number of bytes up to here X%n is stored in count_two.\n", &count_one, &count_two);

	printf("count_one: %d\n", count_one);
	printf("count_two: %d\n", count_two);

	printf("[STACK] A is %d, at 0x%08x. B is %d, at 0x%08x. %x\n", A, (int)&A, B, (int)&B);
		return 0;
}

