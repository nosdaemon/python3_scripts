import socket,datetime
import usnmp


port = 162
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", port))
while 1:
        data, addr = s.recvfrom(4048)
        print(data)
        greq = usnmp.SnmpPacket(data)
        #print(greq.generic_trap)
        #print(greq.specific_trap)
        print(greq.type)
#        print(greq.enterprise)
        print(greq.community)
        print(greq.varbinds)
        print(greq.ver)
        for oid in greq.varbinds:
            print('OID: ' + str(oid))
            VTYPE = greq.varbinds[oid][0]
            VALUE = greq.varbinds[oid][1]
            print(VTYPE)
            print(VALUE)
            if VTYPE == 67:
               d = datetime.timedelta(milliseconds=(int(VALUE)*10)) 
               print(d)
