import sys

f = open("textgrep.txt","r")
context = f.read()
print(context)


content = context.splitlines()
string = sys.argv[2]
k=1
if(len(sys.argv) >3):
  if(sys.argv[3] == "-i"):
    contents = context.lower().splitlines()
    for i in contents:
      c = i.split(" ")
      for j in c:
        if(string in  j):
           k=k+1
    print(k)


  elif(sys.argv[3] == "-n"):
     for i in content:
        c = i.split(" ")
        for j in c:
           if(string in  j):
              k=k+1
     print(k)
  elif (sys.argv[3] == "-v"):
      k=1
      for i in content:
         c = i.split(" ")
         d1 = 1
         for j in c:
            if(string   in  j):
               d1=0
         if(d1==1):
             print(i)

  elif(sys.argv[3] == "-w"):
     for i in content:
        if(string in i):
            print(i)


else:
  k=1
  for i in content:
    c = i.split(" ")
    for j in c:
      if(string in  j):
        print(string + str(k))
    k=k+1

