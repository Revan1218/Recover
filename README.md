# Recover
适用场景：在vscode删除了文件但是想恢复文件

目标：从vscode恢复删除文件

前提：vscode需要更新至具有 local history功能

Local History可以再设置中设置，可以设置最大历史记录条目数以及记录文件最大大小，**仅有小于这个阈值的文件可以被恢复**

具体方法：
1. 从文件中找到./vscode_server/data/User/History文件夹
2. 将History文件夹拷贝，是其与recover.py处于同一目录下
3. 在运行recover.py，即可恢复部分文件
