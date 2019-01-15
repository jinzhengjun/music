import requests

headers = {
    "Content-Type":"application/x-www-form-urlencoded",
    "Referer":"https://music.163.com/search/",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.3"
}

data = {
    "params":"Sd9LvLwoMfK1GLjZvzhpjzv5oMI2yS1luWQD/u/W28RkDtM70hzvj3l+f9bUHZiqKDk2259fGdtE6JDhzghdL/+p5C4xQO1sWS2b/P/r/JVGMsucyu/sUFtxkbOYJH1HC0vCYcXMS4ZkBSEzo9K1y369lWRcmvVz1jBX37cPndNEYXwA7A2wAOzhEDewby3YQZ33/jQIrEQcQ4/+X5on2uAyTw1Iez6FoZcOOgByON7B9DEKePV4GdA0XHw2SF3DmmDXZfNo0lVvhuS6swHjbKNEA1TTskLFiVn19C8Oj4I=",
    "encSecKey":"123f32e1d9e87b184ae0db6b78b8457e2b7095eb7582f3f7f3f98747dc0b1687438a557d1735aa8f677dfe0be6f1ae81e3edcf52bcb0b061c12ccaeac6c7a1ce09c75fd504ba83cfe5666a492162e61ced24eb74ea1333b68b604ec6d64bb3ce5350a41c9c60dfe6952e577876ead1a2f42d820b0cb713c41b3a935c4c4a9594"
}



url = "https://music.163.com/weapi/cloudsearch/get/web?csrf_token="
response = requests.post(url = url,headers = headers,data= data)

print(response.json())