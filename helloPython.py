

def deom_string():
    stra = 'hello there!'
    print 1,stra.capitalize()
    print 2,stra.lower()
    print 3,stra.replace("l",'e')

    strb = '\r\nwe lcome\n have\rfun!'
    print 4,strb.lstrip()
    print 5,strb.rsplit()
    print 6,'_:_'.join(['q','w','e'])
    print 7,strb.split(" ")

def demo_list():
    lista=[1,2,4,'s']
    print 1,lista
    print 2,1 in lista

def demo_re():


def deom_random():



if __name__=='__main__':
    deom_string()
    demo_list()