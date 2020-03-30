from flask import request
from app.MethodView import SuperView
import json

class CodeView(SuperView):
    """
    Create Code evaluation Service
    """

    method_decorators = []
    _decorators = []

    resource = 'code'

    def submitCode(self,user_id):
        body = request.json
        return self.insert(body,objectId=user_id)

    def getCode(self,user_id,code_id):
        return self.retrieve(user_id=user_id,obj_id=code_id)

    def updateCode(self,user_id,code_id):
        body = request.json
        return self.update(data=body,user_id=user_id,obj_id=code_id)

    def deleteCode(self,user_id,code_id):
        return self.remove(user_id=user_id,obj_id=code_id)

    def getEveryCode(self,user_id):
        search = {"user_id":user_id}
        return self.retrieveAll(search=search)
