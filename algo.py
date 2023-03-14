def print_factory():
    global factory
    print("print_factory: ", end='')
    print(factory)
#==================================
def build_100(cmd):
    n, m, b_num = cmd[0], cmd[1], cmd[2:]
    s = 1
    factory = [[] for _ in range(n+1)]
    for (i, stuff) in enumerate(b_num):
        factory[stuff].append(i+1)

    return factory

def moveall_200(cmd):
    global factory
    m_src, m_dst = cmd[0], cmd[1]

    for num in factory[m_dst]:
        factory[m_src].append(num)
    factory[m_dst]=factory[m_src]
    factory[m_src]=list()
    #print_factory()
    print(len(factory[m_dst]))

def exchange_front_300(cmd):
    #print_factory()
    global factory
    m_src, m_dst = cmd[0], cmd[1]
    sline, dline = factory[m_src], factory[m_dst]
    to_src, to_dst = -1, -1
    if sline != []:
        to_dst=sline[0]
        sline.pop(0)

    if dline != []:
        to_src=dline[0]
        dline.pop(0)

        
    if to_src != -1: sline.insert(0, to_src)
    if to_dst != -1: dline.insert(0, to_dst)
    #print_factory()
    print(len(dline))

def split_400(cmd):
    global factory
    m_src, m_dst = cmd[0], cmd[1]
    n = len(factory[m_src])

    if n > 1:
        from_, to = 0, (n//2)-1
        to_move = factory[m_src][from_:to+1]
        #print(to_move)
        to_move.reverse()
        #print(to_move)
        for i in to_move:
            factory[m_dst].insert(0, i)
            factory[m_src].pop(0)
        
    #print_factory()
    print(len(factory[m_dst])) # 옮긴 뒤에만 출력?

    pass

def getPresentInfo_500(p_num):
    global factory

    def binsearch(p_num, belt):
        sorted(belt)
        s, e = 0, len(belt)-1
        while s<=e:
            m = (s+e)//2
            print("m={}, belt[m]={}".format(m, belt[m]))
            if belt[m] > p_num: 
                e=m-1
                print("s={}".format(s))
            elif belt[m] < p_num: 
                s=m+1
                print(f'e={e}')
            elif belt[m] == p_num: 
                return True
        return False            

    p_num=p_num[0]
    a, b = -1, -1
    print("command 500, p_num={}".format(p_num))
    for belt in factory: #10^6까지 가능
        #if p_num in belt:#10^6까지 가능
        if len(belt)==0: continue
        if binsearch(p_num, belt)==True:
            #O(n) 안으로 들어와야함
            idx = belt.index(p_num)
            a = belt[idx-1] if idx!=0 else -1
            b = belt[idx+1] if idx<len(belt)-1 else -1
            print(a+2*b)
            #print(a, b)
            break
            
def getBeltInfo_600(b_num):
    global factory
    b_num=b_num[0]

    #print("command 600")
    c = len(factory[b_num])
    if c==0: 
        a, b = -1, -1
    else:
        a = factory[b_num][0]
        b = factory[b_num][-1]
    print(a+2*b+3*c)

q = int(input())
cmd = list(map(int, input().split()))
factory = build_100(cmd[1:])

for i in range(q-1):
    cmd = list(map(int, input().split()))
    
    if cmd[0] == 200: moveall_200(cmd[1:])
    if cmd[0] == 300: exchange_front_300(cmd[1:])
    if cmd[0] == 400: split_400(cmd[1:])
    if cmd[0] == 500: getPresentInfo_500(cmd[1:])
    if cmd[0] == 600: getBeltInfo_600(cmd[1:])
