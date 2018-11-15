import sys
repeatedValues = []
i = 0 
c = 0
idValue = 0
while i != 1:
    try:
        s = input()
        l = []
        if (len(s) == 0 or s == ' ') :
            i = 1
        else:
            st = s.split('_')
            for j in range(len(st)):
                if (j == 0):
                    l.append(st[j].lower())
                else:
                    l.append(st[j].capitalize())
                f = ''.join(l).split()
            for k in range(len(f)):
                if(k == 1):
                    if ((f[0] != 'id' and idValue == 0)):
                        print("int id \n, ", end='')
                        idValue = 1
                    elif (f[0] == 'id') :
                        print("int id")
                        idValue = 1
                        break
                    else:
                        print(", ", end='')
                        
                    if(f[k] == "date" or f[k] == "varchar" or f[k] == "datetime" or f[k] == "time"):
                        print("String " + f[0])
                    if(f[k] == "numeric" or f[k] == "bigint" or f[k] == "float" or f[k] == "real" or f[k] == "money"):
                        print("BigDecimal " + f[0])
                    if(f[k] == "int" or f[k] == "bit" or f[k] == "tinyint"):
                        print("int " + f[0])
                    c += 1
                    repeatedValues.append(f[0])
    except:
        break
    
repeatedValues = set([x for x in repeatedValues if repeatedValues.count(x) > 1])

print ('Variables repetidas: {}'.format(repeatedValues) if len(repeatedValues) > 0 else sys.exit())