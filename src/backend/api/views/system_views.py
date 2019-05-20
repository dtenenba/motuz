from flask import request
from flask_restplus import Resource

from ..serializers import SystemSerializer
from ..managers import system_manager
from ..managers.auth_manager import token_required


api = SystemSerializer.api
dto = SystemSerializer.dto

"""
GET /api/files DirList

GET /api/uid UidGet (this might go under GET /api/users/$id, but not sure yet)
"""



@api.route('/files')
class SystemFiles(Resource):
    @api.expect(dto, validate=True)
    def post(self):
        """List all files available to the user for a particular URI"""
        data = request.json
        return system_manager.get_files(data['uri'])



@api.route('/uid')
class SystemUid(Resource):
    def get(self):
        """Get the `uid` of the currently logged in user"""
        return system_manager.get_uid()