from elasticsearch import Elasticsearch

EsHost = 
EsPort =
EsIndex = 
EsType = 'TEXT TEXT'

def sendes(HOST,DATA):

    now = datetime.datetime.utcnow()
    timestamp = now.strftime("%Y-%m-%dT%H:%M:%S") + ".%03d" % (now.microsecond / 1000) + "Z"

    MyES = []
    MyES.append(DATA)
    MyDATA = {}
    MyDATA['@timestamp'] = timestamp
    MyDATA['host'] = HOST
    MyDATA['data'] = DATA

    #print(DATA)
    try:
        es = Elasticsearch(EsHost, port=int(EsPort))
        es.indices.create(index=EsIndex, ignore=400)
    except Exception as e:
        print('ES Connection Error: ' + str(e))

    try:
        es.index(index=EsIndex, doc_type=EsType, body=MyDATA)
    except Exception as e:
        print('ES Error: ' + str(e))