
#include <errno.h>
#include <signal.h>
#include <sys/wait.h>

#include <linux/sched.h>
#include <linux/kernel.h>
#include <linux/tty.h>
#include <asm/segment.h>

char sys_name[24];

int sys_whoami(char *name, int size)
{
		
	int i = 0;
	while(sys_name[i] && i < size)
	{
		put_fs_byte(sys_name[i], name+i);
		i ++;
	}
	if (i < size)
	{
		put_fs_byte(0, name+i);
		return i;
	}
	else
	{
		errno = EINVAL;
		return -1;
	}
}

int sys_iam(const char *name)
{
	int i = 0;
	char c;
	while((c = get_fs_byte(name+i)) != 0 && i < 23)
	{
		sys_name[i++] = c;
	}
	if (get_fs_byte(name+i) != 0)
	{
		errno = EINVAL;
		return -1;
	}
	else
	{
		sys_name[i] = 0;
		return i;
	}
}
