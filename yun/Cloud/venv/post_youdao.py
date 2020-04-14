import random
import  requests
import  time




class Youdao():
    def __init__(self,content):
        self.content=content
        self.url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        self.ts=self.get_ts()
        self.salt=self.get_salt()
        self.sign=self.get_sign()



    def get_salt(self):
        return self.ts + str(random.randint(0, 10))

    def get_md5(self,value):
        import hashlib
        m = hashlib.md5()
        m.update(value.encode("utf-8"))
        return m.hexdigest()

    def get_sign(self):
        s = "fanyideskweb" + self.content + self.salt + "Nw(nmmbP%A-r6U3EUn]Aj"
        return self.get_md5(s)

    def get_ts(self):
        ts = str(int(round(time.time() * 1000)))
        return ts

    def get_content(self):
        return content

    def yield_form_data(self):
        return {
            'i': self.content,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': self.salt,
            'sign': self.sign,
            'ts': self.ts,
            'bv': '4b9de992aa3d23c2999121d735e53f9c',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME'
        }


    def get_headers(self):
        return {
            'Cookie': 'OUTFOX_SEARCH_USER_ID = 448036216@10.169.0.82;OUTFOX_SEARCH_USER_ID_NCOO = 1424564220.2692347;JSESSIONID = aaahViJUBLIF_4jcItYfx;___rl__test__cookies = 1586760675060',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 55.0.2883.87UBrowser / 6.2.4098.3Safari / 537.36',
        }


    def fanyi(self):
        response= requests.post(self.url, data=self.yield_form_data(),headers=self.get_headers())
        import json
        content=json.loads(response.text)

        return content['translateResult'][0][0]['tgt']


if __name__ == '__main__':
    while(True):
        i=input("please input :")
        youdao = Youdao(i)
        print("fanyi result :",youdao.fanyi())
