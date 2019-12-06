# mysqlToMarkdown
将mysql的表结构提取出来，转换为有道markDown

###如何使用：
#####首先，将mysqlToMark中开头的
![Image text](readmeImg\QQ截图20191206105944.png)

#####修改为你数据库的配置，然后直接运行
![Image text](readmeImg\QQ截图20191206110320.png)
#####如图所示，如果输入 all 会输出所有的表的结构，如果输入表名则会输出对应的表的结构，输入0会关闭数据库连接

#####最终的结果将会汇总到该文件夹中
![Image text](readmeImg\QQ截图20191206110624.png)

#####如果该表之前已经生成过，生成前会删除同名文件

生成效果如下：

- cmf_ad

|字段名|  格式 | 备注 |
| :------------: | :------------: | :------------: |
|ad_id|bigint(20)|广告id|
|ad_name|varchar(255)|广告名称|
|ad_content|text|广告内容|
|status|int(2)|状态，1显示，0不显示|

有道词典markdown效果如下：
![Image text](readmeImg\QQ截图20191206111154.png)

###生成的都是.txt文件，可以用pycharm自带的text编辑器打开
###如果出现乱码，用pycharm点击乱码会在顶端提示你修改格式，按照提示转换就好了

###运行结束没找到文件就刷新一下，或者输入0退出程序