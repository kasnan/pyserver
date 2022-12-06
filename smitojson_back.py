import re

fjson = open("predator.json", 'w', encoding="UTF-8")
a = "{\"subtitles\":[{\"head\":{\"language\":\"CONVERTED\",\"title\":null,\"attributes\":{}},\"body\":{\"syncs\":["
temp = ""
sub = ""
start=""
end=""
stridx = 0
ordr = 0

fsmi = open("predator.smi", "r", encoding="UTF8").read().replace('\n', '').replace('"', '\\"')
for idx in range(len(fsmi)-14):
    if fsmi[idx:idx+12] == "<sync start=":
        if len(start) == 0:
            i = idx+12
            while True:
                temp += fsmi[i]
                if fsmi[i+1] == '>':
                    break
                i += 1
            start = ''.join(temp)
        else:
            i = idx+12
            while True:
                temp += fsmi[i]
                if fsmi[i+1] == '>':
                    break
                i += 1
            end = ''.join(temp)
    elif fsmi[idx:idx+14] == "<p class=krcc>":
        i = idx+14
        while True:
            temp += fsmi[i]
            if fsmi[i+1] == '<':
                break
            i += 1
        sub = ''.join(temp)
        #print(sub)

    if len(start) > 0 and len(end) > 0 and len(sub) > 0:
        a += "{\"text\":"+"\""+sub+"\",\"startTime\":"+start+",\"endTime\":"+end+",\"extras\":["
        sub = sub.replace('\\"', '')
        if sub != "&nbsp;":
            sub = sub.replace('<br>', '')
            for splt in sub.split(' '):
                a += "{"+"\"type\":\"WordItem\",\"properties\":{"+"\"variant:\":\""+splt+"\",\"original\":\"null\",\"startIndex\":"+str(stridx)+",\"order\":"+str(ordr)+",\"type\":\"word\",\"level\":0,\"meaning\":\"null\"}"+"},"
                stridx += len(splt) + 1
                ordr += 1
            a = a[:-1]
        
        a += "]},"
        
        start = end
        end = ""
        sub = ""
        
    temp = ""

a = a[:-1]
a += "]}}]}"
fjson.write(a)
fjson.close()
