import requests

BASE = "http://127.0.0.1:5000/"

print("これはテストです。\n")
input("データを登録（ENTERで実行）")
membernickname = input("登録するメンバーのニックネームは？")
memberrealname = input("登録するメンバーの本名は？")
memberhobby = input("登録するメンバーの趣味は？")
responce = requests.post(BASE + "necomember/"+membernickname, {"realname": memberrealname, "hobby": memberhobby})
print(responce.json())


input("登録したデータを参照（ENTERで実行）")
responce = requests.get(BASE + "necomember/"+membernickname)
print(responce.json())

input("データをアップデートしましょう（ENTERで実行）")
memberrealname = input("登録するメンバーの”真”の本名は？（任意）")
memberhobby = input("登録するメンバーの本当の趣味は？（任意）")
responce = requests.put(BASE + "necomember/"+membernickname, {"realname": memberrealname, "hobby": memberhobby})
print(responce.json())

input("登録したデータを削除します（ENTERで実行）")
responce = requests.delete(BASE + "necomember/"+membernickname)