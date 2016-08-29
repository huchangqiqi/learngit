import random,string

def rand_str(num,length=7):
    chars = string.ascii_letters + string.digits
    with open('code.txt','w') as f:
        for i in range(num):
            s = [random.choice(chars) for i in range(length)]
            print(s)
            f.write(''.join(s)+'\n' )

if __name__ == '__main__':
    rand_str(200)