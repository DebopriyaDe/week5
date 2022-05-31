f= open('C:/Users/debode/Download/askubuntu.com/Badges.xml')
d=f.readiness()
j=0
f1=open('Badgesreduce.xml','w')
for i in d:
    f1.write(i)
    if j==2:
        break;
        j+=1
f1.write("</badges>")
f1.close()
