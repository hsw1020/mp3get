# mp3get 一个可以下载mp3的库
一个python库，可以搜索和下载任何歌曲 
## 安装/install

```
pip install mp3get

```
## 使用/to use

```
from mp3get import Mp3find  

mp=Mp3find()  

list=mp.searcher('孤勇者')  

mp3_link=mp.down_mp3(rid)  

```
rid 为searcher返回值，为具体mp3的id
