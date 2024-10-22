def handle(event, context):
    return {
        "statusCode": 200,
        "body": "Hello from OpenFaaS!"
    }


# 在代码中调用其他云函数
#
# 您可以在代码中通过发送HTTP请求的方式调用其他云函数。云函数的调用地址可以使用内置的sdk获取。
#
# 当您需要在代码中调用其他云函数时，请确保被调用的云函数已部署成功，且有正在运行的实例。

# import requests
# from sdk import invoke

# def handle(event, context):
#     # 函数调用请求的payload
#     payload = {
#       "key1": "value1",
#       "key2": 0
#     }

#     # 获取函数的调用地址
#     # 基本用法：
#     #     invoke.get_url("组件的命名空间", "组件的名称")
#     # 可选参数：
#     #     - deployment_env: 需要在开发空间调用生产空间的函数，或在生产空间调用开发空间的函数时，将
#     #         deployment_env设置为目标函数所在的空间（dev或prod）。
#     #     - user_id: 需要调用其他用户的函数时，将user_id设置为目标用户的用户ID。
#     try:
#         func_url = invoke.get_url("tools", "json2yaml", deployment_env="dev")
#     except Exception as e:
#         print(e)
#         return 

#     # 发送HTTP请求
#     res = requests.post(func_url, json=payload)

#     # 处理响应
#     data = {
#       "status_code": res.status_code,
#       "text": res.text
#     }

#     return {
#         "statusCode": 200,
#         "body": data
#     }
