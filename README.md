# python3-http-debian云函数模板

## 使用方法

python3-http-debian模板文件结构如下：
```
.
|-- Dockerfile
|-- function
|   |-- handler.py
|   |-- handler_test.py
|   |-- requirements.txt
|   `-- tox.ini
|-- index.py
`-- requirements.txt
```
使用IDE工具时，在高级模式下，可以看到和编辑所有文件；在简单模式下，仅可以看到和编辑function目录下的文件。

通常情况下，仅需要在`function/handler.py`的`handle`函数中编写代码处理HTTP请求，并在`function/requirements.txt`中添加依赖，即可部署和使用云函数。若对HTTP服务端和镜像的环境有更多的自定义需求，可以在高级模式下编辑`index.py`和`Dockerfile`等文件。

# 开发者工具

## 函数间调用Python SDK

最近更新时间：2023-12-27 10:57:41



### Enginefaas SDK 简介

Enginefaas 是云工作空间平台云函数间调用 SDK，集成云函数业务流接口，简化云函数的调用方法。在使用该 SDK 的情况下，用户可以方便的从本地、容器、以及云端函数里快速调用某一个云函数，无需再进行云函数 API 的接口封装。



### 功能特性

Enginefaas SDK 的功能特性可分为以下几点：

- 高性能，低时延的进行函数调用。

- 填写必须的参数后，即可快速进行函数间的调用（SDK 会默认获取环境变量中的参数，例如 deployment_env，SecretId 等）。

- 支持内网域名的访问。

- 支持 keepalive 能力。

- 支持跨地域函数调用。

- 支持 Python 原生调用方式。



### 快速开始

#### 云端函数互调

**示例**

1. 在云端创建一个被调用的 Python 云函数，命名为 “awesome-app.echo”。函数内容如下：

```python
def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    return req
```



2. 在云端创建调用的 Python 云函数，命名为 “awesome-app.caller”。可通过以下方式，结合您的实际情况编辑 handle函数。

```python
from enginefaas import client

def handle(req):
	result = client.invoke("awesome-app.echo", data={"hello": "it is me"})

    return result
```



输出结果如下：

```json
{"hello": "it is me"}
```



### pip 安装

```
pip install enginefaas
```



### 接口列表

#### API Reference

- invoke

##### invoke

调用函数，暂时只支持同步调用。

**参数信息：**

| 参数名              | 是否必填 | 类型   | 描述                                             |
| ------------------- | -------- | ------ | ------------------------------------------------ |
| component_full_name | 是       | String | 组件全名（命名空间.组件名）。                    |
| data                | 否       | Object | 函数接收请求的入参，必须可以被json.dumps的对象。 |
| deployment_env      | 否       | String | 部署环境类型，默认从云函数环境变量中读取。       |

