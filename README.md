# Python3 修改文件md5程序

## 本地运行

```sh
# 进入虚拟环境
source ./venv/bin/activate

# 运行程序主文件
python3 main.py
```

## 打包

```sh
# 进入虚拟环境
source ./venv/bin/activate

# 安装 py2app
pip3 install py2app

#自己开发，打包速度快。(因为本机安装了依赖库，所以可以直接运行)
python3 setup.py py2app -A

#给其他没有sdk的电脑使用，包括lib库。(没有安装sdk的电脑使用，需要去掉-A，将把所有的依赖全部打包。)
python3 setup.py py2app

```

打包后会在 `dist` 目录下生成 `MacOS` 可执行文件