i=0
while i != 1:
  l=[]
  s = input()
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
            if(f[k] == "date"):
                print("String " + f[0])
            if(f[k] == "numeric"):
                print("BigDecimal " + f[0])
            if(f[k] == "int"):
                print("int " + f[0])
            if(f[k] == "bit"):
                print("int " + f[0])
