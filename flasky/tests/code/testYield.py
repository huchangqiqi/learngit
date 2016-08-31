# def addList(alist):
#     for i in alist:
#         yield i+1
#
# alist = [1,2,3,4]
# for x in addList(alist):
#     print(x)

#
# def yield_run_logic():
#     a = 1
#     for i in range(3):
#         print('begin yield')
#         yield a
#         print('end yield')
#         a += i
# yield_obj = yield_run_logic()
#
# while 1:
#     try:
#         ret = next(yield_obj)
#         print(ret)
#     except StopIteration:
#         print('end test')
#         break
def p_tri(num):
    line = []
    up_line = []
    for x in range(num):
        line.append(1)
        if x > 1:
            for i in range(1,len(up_line)):
                line[i] = up_line[i] + up_line[i-1]
        yield line
        up_line = line[:]

for x in p_tri(6):
    print(x)

