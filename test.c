#include<stdio.h>
#include<unistd.h>
#include<fcntl.h>
#include<string.h>
#include<stdlib.h>
void write_to_file(char* str,int fd)
{
  int len = strlen(str);
  char * buff = (char *)malloc(1024 * sizeof(char));
  char * ptr = buff;
  char * pend = buff + 1024;

  while( (ptr + len ) <  pend)
    {
      memcpy(ptr,str,len);
      ptr += len;
      printf(" ptr = %p \n",ptr);
    }
  write(fd,buff,strlen(buff));
}
int main()
{
  int fd = 0;
  if (  -1 == (fd = open("test.log",O_APPEND | O_CREAT | O_RDWR ,0777)) )
    {
      perror("open file failed.");
    }

  char * str = "teststring\n";
  write_to_file(str,fd);
  return 0;
}
