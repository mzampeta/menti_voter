import requests
#import random

menti_url = 'https://www.menti.com/dde56001'
# test url: https://www.menti.com/dde56001
# luca url: https://www.menti.com/8dadc184

def voter(url):
    with requests.Session() as c:
        m_id = url.split('https://www.menti.com/')[1]
       
        header = {'Referer': 'https://www.menti.com/'+m_id,'User-Agent': 'Computer new'}
        r1 = c.get(url, headers = header)
        if (r1.status_code != 200):
            exit(str(r1.status_code))
    # Get question id (q_id) for voting
        url = ("https://www.menti.com/core/objects/vote_keys/"+m_id)
        header = {'Referer': 'https://www.menti.com/'+m_id,'User-Agent': 'Computer new'}
        r2 = c.get(url, headers=header)
        if (r2.status_code != 200):
            exit(str(r2.status_code))
        q_id = r2.json()['pace']['active']
    # Get unique identifier
        iden = c.post("https://www.menti.com/core/identifier", data={})
        if (iden.status_code != 200):
            exit(str(iden.status_code))
        identifier = iden.json()['identifier']
    # Voting
        header = {'X-Identifier': identifier}
        payload = {"question": q_id, "question_type": "choices", "vote": "1"}
        vote = c.post('https://www.menti.com/core/vote', data=payload, headers=header)
        print("Vote submitted")
        if (vote.status_code != 200):
            exit(str(vote.status_code))

for i in range(1,102):
    print (i)
    voter(menti_url)

