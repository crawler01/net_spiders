import  requests
headers = {
    'referer':'https://cq.esf.fang.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
    'cookie':'city=cq; global_cookie=64nj6jo7otdra03672hvunpgk17k6q5qtg4; Integrateactivity=notincludemc; budgetLayer=1%7Ccq%7C2020-02-17%2015%3A58%3A02; lastscanpage=0; logGuid=2e4e75d0-8ab0-4be2-9ae4-c3475208ce3f; __utmc=147393320; csrfToken=5_CT8KsJkbWED9Wb62PavwfD; g_sourcepage=esf_fy%5Elb_pc; __utma=147393320.1264219938.1581925758.1582095380.1582101898.4; __utmz=147393320.1582101898.4.4.utmcsr=cq.fang.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt_t0=1; __utmt_t1=1; __utmt_t2=1; unique_cookie=U_vdw599fnazegjx9x0d8j6z0kk2dk6swy42k*38; __utmb=147393320.24.10.1582101898'
}
print(requests.get('https://cq.esf.fang.com/chushou/3_194781618.htm',headers= headers).text)