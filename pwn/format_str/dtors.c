/*
 * =====================================================================================
 *
 *       Filename:  dtors.c
 *
 *        Version:  1.0
 *        Created:  10/04/2015 12:32:59 AM
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

static void cleanup(void) __attribute__((destructor));

int main (int argc, char **argv){
	printf("In main()\n");
		return 0;
}


void cleanup (void )
{
	printf("In the cleanup()\n");
}

