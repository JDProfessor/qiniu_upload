此程序实现了七牛的表单上传，适用于文件较小的情况。（增量备份）

baseinfo    模块：填写基本信息 
				1. deadline 为token的截止时间,默认为60S
				2. backupdir 为需要备份的目录
				3. dic     需要填写仓库名
				4. ak
				5. sk

tkproductor 模块：生成token

iteration   模块 ：生成需备份的目录文件遍历（bug:如果某一次备份出现断网的情况剩余文件将无法备份）

log         模块 ：将备份后的文件，写入log.txt中作为记录

Time 		模块  :可以设置deadline

client_poster 模块 ：文件上传器

streaminghttp，encode 为第三方库
