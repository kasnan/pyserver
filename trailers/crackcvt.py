path = "C:/Users/kasna/Documents/vsworkspace/Pyworkspace/pyserver/trailers/"

f = open(path+"cvt.txt", 'r')
line = f.readline()
f.close()

line = line.replace("[M","\n[M")
line2 = line.split("\n")
print(line2[1])
