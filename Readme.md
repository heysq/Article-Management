# 网络文章下载与管理系统

### Python+selenium+PyQt5编写，实现网页整体保存，链接提取，图片提取与网页主题内容提取



- 运行环境

windows10 64位，Python3.6，PyQt5.9.2,代码在Windows系统编写，暂未考虑Linux与MacOS操作系统。

- 程序功能
  1. 网页解析与保存，可以将网页几乎全部保存在本地，部分图片视频无法保存。保存为本地html格式，css，与js还原度90%
  2. 提供解析页面内链接功能，将链接汇总为html文件和xlsx表格文件，保存到本地link文件夹下
  3. 提供解析页面内图片功能，将网页内的部分图片保存到本地iimages文件夹下
  4. 提供网页文字提取功能（试用），将网页文字内容（段落）提取保存为txt到本地text文件夹下
  5. 提供页面截屏功能，截屏尺寸为软件自带浏览器的尺寸，提供每个屏幕的小截图，提供整个网页截图合成后的长图，因为可能采用动态加载技术，所以部分网页无法完全截屏，所有图片保存到本地screenshuots文件夹下

- 如何使用

  1. git clone到本地后，建议创建python虚拟环境，运行`pip install -r requirements.txt`命令安装软件运行需要的所有模块。

  2. 修改settings下的settinjs.json文件，将FILE_LOCATION 改为想要存储网页的文件夹，注意修改Windows（`\`）下划线为 `/`,使程序读取该设置完成起始目录的设定，与下载分类的选择

  3. 此程序建议安装vc运行库（比如windows7操作系统），windows10 操作系统亲测可以直接使用

  4. 运行主程序`python index.py`,实现存储路径下的内容的管理，与预览

  5. 运行保存网页的程序 `python saveWindow.py`,注意需要给此程序传参数

     比如`python saveWindow.py netarticle://http://www.baidu.comnetarticletitle=百度一下你就知道netarticlecookie=1111`,参数将会在程序内通过netarticle被分割为3个参数`url`,`title`,`cookis`分别代表网页的url，网页的title，网页的cookies（目前暂未实现携带cookies保存功能）

     

   



