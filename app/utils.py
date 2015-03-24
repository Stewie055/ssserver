from subprocess import call
from random import randint
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

def stop():
    status = call(['ssserver','-d','stop'])

def restart(password,port):
    stop()
    start(password,port)

def reset():
    password = 'random'
    port = randint(2000,10000)
    with open('ss.conf','w+') as f:
        f.write('password:%s\n'%password)
        f.write('port:%s\n'%port)
        f.close()
    restart(password,port)

if __name__ == '__main__':
    reset()
    print(readconf())

