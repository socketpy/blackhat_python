/*
 * =====================================================================================
 *
 *       Filename:  get_path.c
 *
 *        Version:  1.0
 *        Created:  09/27/2015 12:36:48 AM
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

//returns the exact address of ENV (given by argv[1]) when run on PROGRAM (given by argv[2])
int main (int argc, char **argv){
	char *tgt;

	if (argc < 3) {
		printf("Usage: %s <ENV> <TARGET PROGRAM>\n", argv[0]);
		exit(0);
	}
	tgt = getenv(argv[1]);		//getting the addr of ENV

	if (tgt == NULL) {
		printf("Not Found\n");
	}else {
		tgt += (strlen(argv[0]) - strlen(argv[2])) * 2;
		printf("%s will be at %p\n", argv[1], tgt);
	}
		return 0;
}

