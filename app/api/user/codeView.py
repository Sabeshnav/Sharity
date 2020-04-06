from flask import request
from app.MethodView import SuperView
import json

class CodeView(SuperView):
    """
    Create Code evaluation Service
    """

    method_decorators = []
    _decorators = []

    resource = 'user'
    subresource = 'code'

    def submit(self,user_id):
        body = request.json
        return self.insert_subdocument_array(obj_id=user_id, data=body, resource=self.resource, subresource=self.subresource)

    def get(self,user_id,code_id):
        return self.retrieve_subdocument_array(obj_id=user_id,sub_obj_id=code_id,resource=self.resource,subresource=self.subresource)

    def Update(self,user_id,code_id):
        body = request.json
        return self.update_subdocument_array(obj_id=user_id, sub_obj_id=code_id, resource=self.resource, subresource=self.subresource, data=body)

    def delete(self,user_id, code_id):
        return self.remove_subdocument_array(obj_id=user_id, sub_obj_id=code_id, resource=self.resource, subresource=self.subresource)

    def getAll(self,user_id):
        return self.retrieveAll_subdocument_array(obj_id=user_id, resource=self.resource, subresource=self.subresource)
