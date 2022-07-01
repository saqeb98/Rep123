import time
from aifc import Error

import requests
import json

class Execution_Failure(Error):
    pass

def login(token):
    s = requests.Session()

    head = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    head["Authorization"] = "Bearer " + token
    suiteid = 'SUITE1013'
    pes = s.post('https://app.flinko.com:8109/optimize/v1/dashboard/execution/suite/' + suiteid, headers=head)
    out = json.loads(pes.content)
    exid = out['responseObject']['id']
    
    time.sleep(3)
    sc = 0
    while (sc < 1):
        r1 = s.get('https://app.flinko.com:8110/optimize/v1/executionResponse/result/' + exid, headers=head)
        c1 = json.loads(r1.content)
        try:
            fr2 = c1['responseObject']['suiteStatus']
            fr1 = fr2
        except:
            print("pending....")
        if fr1 == 'PASS':
            print('Success')
            sc = 1
        if fr1 == 'FAIL':
            raise Test_Failed
            sc = 1
        time.sleep(10)

login('eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJtb2hhbW1lZC5zYXFlYkB0ZXN0eWFudHJhLmNvbSIsInNjb3BlIjpbInJlYWQiLCJ3cml0ZSJdLCJuYW1lIjoiU2FxZWIiLCJhY3RpdmF0aW9uU3RhdHVzIjoiQUNUSVZFIiwiaWQiOiJVU1IxMTM2IiwicHJpdmlsZWdlIjoiU3VwZXIgQWRtaW4iLCJleHAiOjE2NTcwMjA1NDgsInVzZXJOYW1lIjoibW9oYW1tZWQuc2FxZWJAdGVzdHlhbnRyYS5jb20iLCJsaWNlbnNlSWQiOiJMSUMxMDM1IiwianRpIjoicFJSYW9TdkdZMkExR04yV1BOaTRqNTJYZ0w4IiwiY2xpZW50X2lkIjoiY2xpZW50Vml2In0.ogStJtwYCV9Gas6XLtednRt1mT5zm22u385qcLk6dDxxM4j2kSbqTVOmZB46-T88tu2IRVJMer7gfdNi31Z_TQWJ1JONTa-mWVzFsCc2fPvh45tW0_LjTnErKrMYx-uDgjyB886K3endefkdSSLJGEwqL9njcNiVnfvMQsYCm0A4LcxfowKfY9U1DhjbSd4a5_3qwBdtOLI3sqrGc62WFww1jpFEM9G4iQKDTCZlLanMUIMq5RSE0qnlaqyDz4DzdHLFulsZJ98D4cQN_l_KYTxm9atdw1KHSAz__SGzx6ZOT89QlnI9u48dPqcyH6RDWWTqQ1DtjnFJaKA5RAl1Pg')
