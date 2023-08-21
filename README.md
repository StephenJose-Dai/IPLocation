# IPLocation
一个可以批量查询IP归属国、城市和ASN的小工具，由<a href="https://daishenghui.club">戴戴的Linux</a>制作、福建省智网云科、福建省数网云提供技术指导
## 环境
1、Linux、Windows
2、Python ≥ 3.6
## Windows使用方法
1、配置并激活虚拟环境
````
python -m venv search  //这里的search是虚拟目录的名字，可以取一个你喜欢的
C:\Users\ZWYK\Desktop\search\Scripts\activate
````
2、安装geoip2、tk模块
````
pip install geoip2
pip install tk
````
3、运行git clone下来后里面的Win文件夹的search.py
````
python search.py
````
4、根据提示选择ASN、Country、City数据库和IP文件，然后选择要保存结果的位置和名字即可

5、如果不会的话，可以下载release中现成的程序来运行，直接双击ipsearch.exe然后选择对应的数据库文件、IP文件以及保存的位置和名字即可。

## Linux下的使用方法
1、配置并激活虚拟环境
````
virtualenv search   //这里的search是虚拟目录的名字，可以取一个你喜欢的
source search/bin/activate
````
2、安装geoip2模块
````
pip install geoip2
````
3、运行git clone下来后里面的Linux文件夹的search.py
````
python search.py
````
4、根据提示输入ASN、Country、City数据库的路径和名字以及IP文件的路径和名字，然后选择要保存结果的路径和名字即可
