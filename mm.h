struct block_list* get_free_block() ;
char* get_full_block();
int memory_init();
void memory_destory();
int release_full_block();
void update_current_block();
int append_isover(unsigned int size);
void * mem_alloc(unsigned int size);
