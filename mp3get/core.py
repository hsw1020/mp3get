# Insert your code here. 
from turtle import down
import requests,json

class mp3get():
    headers={
        'Cookie':'kw_token=AZD79MMMXAP',
        'csrf':'AZD79MMMXAP',
        'Referer':'http://www.kuwo.cn/search/list?key=anykey',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',            
        }
    def searcher(self,keyword):
        s_url='http://www.kuwo.cn/api/www/search/searchMusicBykeyWord'
        params={
            'key': keyword,
            'pn': 1,
            'rn': 30,
            'httpsStatus': 1
        }
        

        r=requests.get(s_url,params=params,headers=self.headers)
        r_json=json.loads(r.text)
        data=r_json.get('data')
        if data :
            mp3_info_list=[]
            result_list=data.get('list')
            for rr in result_list:
                name=rr.get('name')
                album=rr.get('album')
                artist=rr.get('artist')
                rid=rr.get('rid')
                row={
                    'album':album,
                    'name':name,
                    'artist':artist,
                    'rid':rid
                }
                mp3_info_list.append(row)

            return mp3_info_list
        else:
            return 'No mp3 found with this keyword!'
    
    def down_mp3(self,rid):
        d_url=f'http://www.kuwo.cn/api/v1/www/music/playUrl?mid={rid}&type=music&httpsStatus=1'
        r=requests.get(d_url,self.headers)
        data=json.loads(r.text).get('data')
        msg=json.loads(r.text).get('msg')
        if msg=='success':
            mp3_url=data.get('url')
            return mp3_url
        else:
            return 'get mp3 info failed!'

mm=mp3get()
aa=mm.searcher('孤勇者')
pass