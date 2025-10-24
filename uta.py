from wise import *

cat ("uta.txt")

def readDict(dictionary,VERBOSE):
    edict={}
    gdict={}
    dname = "langs/"+dictionary+".lng"
    try:
        size = file_len(dname)
    except:
        size = file_len("langs/tlhingan.lng")
        dname = "langs/tlhingan.lng"
        dictionary = "tlhingan"
        
    print ("loading "+dictionary)
    qs = open(dname)
    for i in range(size):
        l = qs.readline()
        l = l.rstrip()
        try:
            (e,g)=l.split('", "')
            e = e.replace('"','')
            g = g.replace('"','')
            edict[e]=g
            gdict[g]=e
            if VERBOSE:
                print(e + " "+g)
        except:
            a=1
    return(edict,gdict)


(ed,gd)=readDict("tlhingan",False)
Done = False
while not Done:
    words = input("text: ")
    out = ""
    ws = words.split()
    for w in ws:
        try:
            out = out + " " + (ed[w])
        except:
            try:
                out = out + " " + (gd[w])
            except:
                out = out + " [" + w+"]"

    if ws[0] == "*lang":
        (ed,gd)=readDict(ws[1],False)
    else:
        if ws[0] == "*pItlh":
            Done = True
        else:
            if ws[0] == "*help":
                cat("help.txt")
            else:
                print (out)
