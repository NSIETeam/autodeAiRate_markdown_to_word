@echo off
echo 正在安装依赖...
pip install -r requirements.txt

echo 正在打包程序...
python build.py

echo 打包完成！可执行文件在 dist 文件夹中
pause