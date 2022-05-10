import string
from flask import Flask
from flask_restful import Api, Resource, abort, reqparse

app = Flask(__name__)
api = Api(app)

necomemberpost = reqparse.RequestParser()
necomemberpost.add_argument("realname", type=str, help="メンバーの本名 (必須)", required = True)
necomemberpost.add_argument("hobby", type=str, help="メンバーの趣味 (任意)")

necomemberupdate = reqparse.RequestParser()
# PUTは必須項目なし
necomemberupdate.add_argument("realname", type=str, help="メンバーの本名 (必須)")
necomemberupdate.add_argument("hobby", type=str, help="メンバーの趣味 (任意)")

necomember = {}

def abortnonexist(membername):
    if membername not in necomember:
        abort(404, "リクエストされたニックネームで登録されているNECOメンバーは存在しません。")

def abortexist(membername):
    if membername in necomember:
        abort(409, "すでに"+membername+"のデータは登録されています。")

class Members(Resource):
    def get(self, membername):
        abortnonexist(membername)
        return necomember[membername]

    def post(self, membername):
        abortexist(membername)
        necorequires = necomemberpost.parse_args()
        necomember[membername] = necorequires
        return necomember[membername], 201

    def put(self, membername):
        necorequires = necomemberpost.parse_args()
        necomember[membername] = necorequires
        return necomember[membername], 201
    
    def delete(self, membername):
        abortnonexist(membername)
        del necomember[membername]
        return '削除されました', 204

        
    
api.add_resource(Members, "/necomember/<string:membername>")

if __name__ == "__main__":
    app.run(debug=True)
