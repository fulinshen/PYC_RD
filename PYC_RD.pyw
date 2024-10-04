import random
import os
import tkinter as tk




try:
    os.mkdir("key")
except FileExistsError:
    pass
else:
    pass
try:
    os.mkdir("close")
except FileExistsError:
    pass
else:
    pass
try:
    os.mkdir("open")
except FileExistsError:
    pass
else:
    pass
try:
    os.mkdir("read")
except FileExistsError:
    pass
else:
    pass
def opens(a,b):

    txtp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    if a in txtp:
        a=txtp[txtp.index(a)-b]
        return a
    else:
        return a
def open_in_key():
    j=open('close/'+close.get(),'r')
    jo=open('key/'+key.get(),'r')
    c=list(j.read())
    d=jo.read().split()
    i=0
    while i<len(d):
        d[i]=int(d[i])
        i+=1
    b=[]
    i=0
    while i<len(c):
        b.append(opens(c[i],d[i]))
        i+=1
    jk=open('open/open.txt','w')
    for i in b:
        jk.write(i)
    jk.close()

def txt(a,n):
    txtp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    a=a.lower()
    if a in txtp:
        if txtp.index(a)+n>=26:
            a=txtp[txtp.index(a)+n-26]
            return a
        else:
            a=txtp[txtp.index(a)+n]
            return a
    else:
        return a
txts=' '
def reads():
    global txtps,txts
    try:
        txtp=open('''read/'''+en.get(),'r')
        txts=str(txtp.read())
    except FileNotFoundError:
        txtp=open('''read/'''+en.get(),'w')
        txtp.write("hello")
        txtp.close()
        txtp=open('''read/'''+en.get(),'r')
        txts=str(txtp.read())
    else:
        pass
def closes():
    global d,c,txts
    i=0
    d=[]
    c=[]

    while i<len(txts):
        input_2=random.randint(1,26)
        d.append(input_2)
        c.append(txt(txts[i],input_2))
        i+=1
    i=0
    b=[]
    j=open('close/close.txt','w')
    k=open('key/key.txt','w')
    for i in c:
        j.write(i)
    for i in d:
        k.write(str(i)+' ')
    k.close()
    j.close()

a=0
def en():
    global a
    a=1



root=tk.Tk()
root.title("PYC_RD")
tx=tk.StringVar()
tx.set("read.txt")
cf=tk.Button()
en=tk.Entry(textvariable=tx)
ho=["确定","加密","解密"]
fo=["yes","encryption","deciphering"]
f=tk.Button()

f["command"]=reads

cf["command"]=closes
english=tk.Button()
chinese=tk.Button()
close_and_key=tk.Button()
txtname=tk.StringVar()
txtnam=tk.StringVar()
txtname.set("key.txt")
txtnam.set("close.txt")
close=tk.Entry(textvariable=txtnam)
key=tk.Entry(textvariable=txtname)
cf_1=tk.Button()
cf_1["command"]=open_in_key
hd=tk.StringVar()
hd.set("keet")


cf["text"]=ho[1]
f["text"]=ho[0]
cf_1["text"]=ho[2]


f.pack(side='left', expand=True, fill='both')
en.pack(side='left', expand=True, fill='both')
cf.pack()
cf_1.pack()
close.pack(side='bottom', expand=True, fill='both')
key.pack(side='left', expand=True, fill='both')

tk.mainloop()
