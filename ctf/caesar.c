/*
 * =====================================================================================
 *
 *       Filename:  caesar.c
 *
 *        Version:  1.0
 *        Created:  03/03/2015 05:03:45 PM
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


/* caesar encryption algorithm
 * arguments:		str (string encrypted or decrypted)
 *					len (length of str)
 *					key (key - number of shift: positive for encryption and negative for decryption)*/
void caesar_encryption (char* str, size_t len, int key){
	size_t i;
	for (i = 0; i < len; i++) {
		str[i] += key;
	}
}		/* -----  end of function caesar_encryption  ----- */
