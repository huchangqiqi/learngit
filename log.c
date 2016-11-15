#include "log.h"
#include "mm.h"
#include<stdio.h>
#include<string.h>
#include<time.h>
#include<stdarg.h>
#include<fcntl.h>
#include<errno.h>
#include<unistd.h>
#include<stdlib.h>
#include<pthread.h>

#define MAX_SIZE 200

pthread_mutex_t mutex ;
pthread_cond_t cond;
pthread_t thrd ;

static int log_fd ;
static int flag ;
static int is_full ;

/*
char* buff = NULL;
char* ptr = NULL;
char* pend = NULL;
*/

static char* get_level(log_level_t level){
  switch(level)
    {
    case DEBUG:return "DEBUG";
    case INFO:return "INFO";
    case WARN:return "WARN";
    case ERROR:return "ERROR";
    case FATAL:return "FATAL";
    default: return "";
    }
}

/*
char *
new_buff()
{
  buff = (char* )malloc(sizeof(char)*20000);
  ptr = buff;
  pend = buff + 20000;
  return ptr;
}
*/

static void*
persistence(void* arg)
{
  char *page;
  while(1)
    {
      while((page=get_full_block()) == NULL)
        {
          pthread_cond_wait(&cond,&mutex);
        }
      write(log_fd,page,strlen(page));
      release_full_block();
      if(flag == 1)
        {
          break;
        }
    }
  return NULL;
}

/*
void *
mem_alloc(size_t size)
{
  void * ret  = ptr;

  pthread_mutex_lock(&mutex);
  if((ptr + size) < pend)
    {
      ptr += size;
    }
  else{
    is_full = 1;
    ret = NULL;
  }
  pthread_mutex_unlock(&mutex);
  return ret;
}
*/

int
log_cache(const char *log)
{
  int len = strlen(log);
  void* begin;

  cache:
  if( (begin = mem_alloc(len)) != NULL)
    {
      memcpy(begin,log,len);
    }
  else
    {
      pthread_cond_signal(&cond);
      goto cache;
    }
  return 0;
}


int
log_write(const char* file, const char* func,
              const int line,log_level_t level,char* msg,...)
{
  char log[MAX_SIZE] = {'\0'};
  size_t len = 0;

  time_t rawtime;
  time(&rawtime);
  struct tm* timeinfo = localtime(&rawtime);
  strftime(log,MAX_SIZE,"%y-%m-%d %H:%M:%S ",timeinfo);

  len = strlen(log);
  snprintf(log+len, MAX_SIZE - len,"%s %s %d [%s] ",
           file,func,line,get_level(level));

  len = strlen(log);
  va_list arg_ptr;
  va_start(arg_ptr,msg);
  vsnprintf(log+len,MAX_SIZE -len,msg,arg_ptr);
  va_end(arg_ptr);

  log_cache(log);

  return 0;
}

int
log_init()
{
  if((log_fd = open("test.log",O_CREAT | O_APPEND | O_RDWR,0666)) == -1)
    {
      perror("open file test.log failed.");
    }

  pthread_mutex_init(&mutex,NULL);
  pthread_cond_init(&cond,NULL);

  //new_buff();

  if(pthread_create(&thrd,NULL,persistence,NULL) != 0)
    {
      perror("create thread failed.");
    }
  return 0;
}

int
log_destory()
{
  flag = 1;
  update_current_block();
  pthread_cond_signal(&cond);
  pthread_join(thrd,NULL);
  pthread_mutex_destroy(&mutex);
  close(log_fd);
  return 0;
}

void*
print_log(void* arg)
{
  for(int i = 0;i < 10 ; i++)
    {
      LOG_DEBUG(":我是测试字符串%s ,第 %d次打印, 线程 %s \n","zp",i,(char*)arg);
      LOG_INFO(":我是测试字符串%s ,第 %d次打印, 线程 %s \n","cc",i,(char*)arg);
      LOG_ERROR(":我是测试字符串%s ,第 %d次打印, 线程 %s \n","hm",i,(char*)arg);
      LOG_FATAL(":我是测试字符串%s ,第 %d次打印, 线程 %s \n","xh",i,(char*)arg);
      LOG_WARN(":我是测试字符串%s ,第 %d次打印, 线程 %s \n","xl",i,(char*)arg);
    }

  return NULL;
}

int
main()
{
  pthread_t thread_id[10];
  char threadname[10][10] = {
    "thread-A",
    "thread-B",
    "thread-C",
    "thread-D",
    "thread-E",
    "thread-F",
    "thread-G",
    "thread-H",
    "thread-I",
    "thread-J",
  };

  log_init();

  for(int i = 0;i < 10; i++)
    {
      pthread_create(&thread_id[i],NULL,print_log,(void*)threadname[i]);
    }
  for(int i = 0 ;i < 10 ;i++)
    {
      pthread_join(thread_id[i],NULL);
    }
  log_destory();
  return 0;
}
