# NECO新人課題（REST-API編）

我が友の「もりくらげ」くんがNode.jsでやってしまっていたので、Python＋Flaskでやろうと思いました。

1. ターミナルウィンドウを２つ用意しましょう！
2. 片方で `python3 rest.py`を実行してサーバーを実行！
3. もう片方で`python3 test.py`を実行すると「親切」にプログラムがREST APIの機能を見せてくれます

エンドポイント・機能

`necomember`にてニックネーム（`membernickname`）、本名（`memberrealname`）、趣味（`memberhobby`）で構成されています。

`import requests`を行ってください。

- GET - `requests.get('http://127.0.0.1:5000/necomember/' + membernickname)`
- POST - `requests.post('http://127.0.0.1:5000/necomember/' + membernickname, {"realname": memberrealname, "hobby": memberhobby})`
- PUT - `requests.put('http://127.0.0.1:5000/necomember/' + membernickname, {"realname": memberrealname, "hobby": memberhobby})`
- DELETE - `requests.delete('http://127.0.0.1:5000/necomember/' + membernickname)`


ニックネーム（`membernickname`）で参照する感じになります。

表示したい場合は`.json()`で`print`してください。

使用例は`test.py`を実行して、中身をみてもらえるとより伝わりやすいかと思います。

データベース構築をやってない超簡易的なAPIですが、許してください。


Karolusでした。
