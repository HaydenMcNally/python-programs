contstants = []
x = 'dd';
while x != "yy":
    x = input('Enter unknown letters :')
    if (x != 'yy'):
        contstants.append(x)
pos1 = ""
pos2 = ''
pos3= ''
pos4 = '';
pos5= '';
answer = [pos1,pos2,pos3,pos4,pos5]
count = 0
while count < 5:
    answer[count] = input("Enter known spot:")
    count += 1
print(contstants)
print(answer)


def position_4(answer , contstants,const,const1,const2,const3):
    if answer[4] == '1':
        for const4 in contstants:
            print(const,end = '')
            print(const1,end = '')
            print(const2,end = '')
            print(const3,end = '')
            print(const4)
    else:
        print(const,end = '')
        print(const1,end = '')
        print(const2,end = '')
        print(const3,end = '')
        print(answer[4])

def position_3(answer , contstants,const,const1,const2):
    if answer[3] == '1':
        for const3 in contstants:
            position_4(answer, contstants,const,const1,const2,const3)
    else:
        position_4(answer,contstants, const,const1,const2,answer[3])

def position_2(answer , contstants,const,const1):
    if answer[2] == '1':
        for const2 in contstants:
            position_3(answer, contstants,const,const1,const2)
    else:
        position_3(answer,contstants,const,const1,answer[2])


def position_1(answer , contstants,const):
    if answer[1] == '1':
        for const1 in contstants:
            position_2(answer, contstants,const ,const1)
    else:
        position_2(answer,contstants,const,answer[1])

if answer[0] == '1':
    for const in contstants:
        position_1(answer,contstants,const)
else:
    position_1(answer,contstants,answer[0])
    
