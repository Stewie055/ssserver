from subprocess import call
from random import randint
from random import choice

def choose_word():
    word_list = []
    with open('list','r') as f:
        for line in f.readlines():
            word = line.strip()
            if len(word)>6 and word not in word_list:
                word_list.append(word)
    return choice(word_list)

def readconf(fname='ss.conf'):
    conf = {}
    with open(fname,'r') as f:
        for line in f.readlines():
            key,value = line.split(':')
            conf[key.strip()] = value.strip()
        f.close()
    return conf

def start(password,port):
    status = call(['ssserver','-p',str(port),'-k',password,'-m','rc4-md5','-d','start'])
    print(status,port,password)

def stop():
    status = call(['ssserver','-d','stop'])

def restart(password,port):
    stop()
    start(password,port)

def reset():
    password = choose_word()
    port = randint(2000,10000)
    with open('ss.conf','w+') as f:
        f.write('password:%s\n'%password)
        f.write('port:%s\n'%port)
        f.close()
    stop()
    start(password,port)


if __name__ == '__main__':
    reset()
    print(readconf())

