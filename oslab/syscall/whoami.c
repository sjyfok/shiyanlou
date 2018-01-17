/*
 * Compile: "gcc testlab2.c"
 * Run: "./a.out"
 */

#include <string.h>
#include <assert.h>
#include <stdio.h>
#include <errno.h>
#include <stdlib.h>
#define __LIBRARY__
#include <unistd.h>

_syscall2(int, whoami,char*,name,unsigned int,size);
_syscall1(int, iam, const char*, name);

#define MAX_NAME_LEN        23
#define NAMEBUF_SIZE        (MAX_NAME_LEN + 1)
/* truncate a long name to SHORT_NAME_LEN for display */
#define SHORT_NAME_LEN      (MAX_NAME_LEN + 2)



int main(void)
{
	char name[NAMEBUF_SIZE];
	int ret = whoami(name, NAMEBUF_SIZE);
	printf("%s\r\n", name);
	return ret;
}
