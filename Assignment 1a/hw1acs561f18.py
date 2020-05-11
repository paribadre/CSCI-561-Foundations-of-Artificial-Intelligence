def VC(status,location):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    elif location == "B":
        return "Left"


f=open("input.txt","r")
o=open("output.txt","w")
for line in f:
    line = line.replace('\n', '')
    location,status = line.split(",")
    str=VC(status,location)
    o.write(str)
    o.write('\n')
f.close()
o.close()
