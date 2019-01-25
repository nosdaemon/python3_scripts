from pysnmp.hlapi.asyncore import *

snmpEngine = SnmpEngine()
sendNotification(
    snmpEngine,
    CommunityData('404040'),
    UdpTransportTarget(('127.0.0.1', 162)),
    ContextData(),
    'trap',
    NotificationType(ObjectIdentity('SNMPv2-MIB', 'coldStart')),
 )

snmpEngine.transportDispatcher.runDispatcher()
