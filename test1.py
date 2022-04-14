import requests, json
r = requests.Session()
kv = {
    "user-agent": "Mozilla/5.0",
    "referer": "https://weibo.com/u/6026794900",
    "cookie":"SINAGLOBAL=8057188833066.809.1649769807945; ariaDefaultTheme=default; ariaFixed=true; ariaReadtype=1; ariaMouseten=null; ariaStatus=false; wb_view_log=1536*8641.25; SCF=AhJI-CCcdeC5wboPkOQHCBq2yAGkwbVNnGufqivUrvbrkHTyezhqkXoAxdZGNwoDm6mbUCzX8szsQnFBQ_OwTBw.; ULV=1649910057730:5:5:5:8587026511188.107.1649910057719:1649906341228; SUB=_2A25PU92YDeRhGeBI7lUX9SjIyjiIHXVsv-PQrDV8PUJbkNB-LXbukW1NRpSSbTi7HcYVvcz8I-vfkxN_pDQoXVqt; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFhw6PoWn1Fxs2qm1FnXdwu5NHD95QcSo-NSo-cSh2XWs4DqcjEi--Xi-zRiKn7i--4i-2EiK.Ni--fi-z7iKysi--fi-z7iKysi--NiKLWiKnXMNxadJ-t; XSRF-TOKEN=iA-mdGRazzHgtdwkVPTyCacs; WBPSESS=Dt2hbAUaXfkVprjyrAZT_NdHgjmJfDCJ3dfv4uRqLh0FkNxN-Gr2I8fTJJ4cMeTuYh33maQGPKjv9hKuHI8uf-0jYLj8w6ba6ets64G335UVwf3XqGoD-HdIQyMLaARVpdS-SjoIdz6wD2DH1J5Tbr-hpG68wOGq09Jw-FxNOwO9BVDS6WkpNJRnH6HrxlOt684bJO5LmMGtGDwszxoBVw=="
}
result = r.get(url="https://weibo.com/ajax/profile/detail?uid=6026794900", headers=kv)
result.raise_for_status()
print(json.loads(result.text)['data']['ip_location'])
