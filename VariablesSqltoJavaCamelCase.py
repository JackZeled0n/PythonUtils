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
    print(''.join(l))
