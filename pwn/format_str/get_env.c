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

int main (int argc, char **argv){
	char *tgt;
	tgt = getenv(argv[1]);

	if (tgt == NULL) {
		printf("Not Found\n");
	}else {
		printf("%s :: %p\n", argv[1], tgt);
	}
		return 0;
}

