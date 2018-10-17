i = 0 
c = 0
while i != 1:
    try:
        s = input()
        l=[]
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
                    if(f[k] == "date" or f[k] == "varchar" or f[k] == "datetime" or f[k] == "time"):
                        if(c == 0) : 
                            print("String " + f[0])
                        else :
                            print(", String " + f[0])
                    if(f[k] == "numeric" or f[k] == "bigint" or f[k] == "float" or f[k] == "real" or f[k] == "money"):
                        if(c == 0) : 
                            print("BigDecimal " + f[0])
                        else :
                            print(", BigDecimal " + f[0])
                    if(f[k] == "int" or f[k] == "bit" or f[k] == "tinyint"):
                        if(c == 0) : 
                            print("int " + f[0])
                        else :
                            print(", int " + f[0])
                    c += 1
    except:
        break
