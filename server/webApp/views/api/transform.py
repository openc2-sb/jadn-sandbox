import logging

import os
import traceback
from flask import current_app, json, jsonify, request
from flask_restful import Resource

from jadnschema.transform.resolve_references import resolve_references


logger = logging.getLogger(__name__)

class Transform(Resource):
    """
    Endpoint for api/transform
    """

    def get(self):
        return jsonify({
            "transformations": current_app.config.get("VALID_TRANSFORMATIONS")
        })

    def post(self):
        # """
        # take list of schemas, validate schemas, and transform schemas based on selected transformation type 
        # :param schema_list: list of schema_data and schema_name 
        # :param transformation_type: selected transformation type
        # :param base_schema: selected base file for resolving imports
        # :return: list of transformed schemas with schema_name and schema_data (200),
        #   a transformed schema + schema_name (200) 
        #   or list of invalid schemas (500)
        # """

        request_json = request.json

        invalid_schema_list = []
        if len(invalid_schema_list) != 0:
            return invalid_schema_list, 500
             
        else:
            transformed = request_json["transformation_type"]
            output = []
            if transformed == 'strip comments':
                for schema in request_json["schema_list"]:
                    schema_content_str = schema['data']
                    schema_content_dict = json.loads(schema_content_str)
                    schema_stripped = transform.strip_comments(schema_content_dict)
                    schema_name, ext = os.path.splitext(schema['name'])
                    output.append({
                        'schema_name': schema_name,
                        'schema': schema_stripped,
                        })
                return output
            
            elif transformed == "resolve references":
                schema_base = ''
                schema_list = []
                schema_base_name = 'schema_base'

                for schema in request_json["schema_list"]:

                    data = schema.get('data')
                    if isinstance(data, str):
                        data = json.loads(data)

                    if schema['name'] == request_json["schema_base"]:
                        schema_base = data
                        schema_base_name = schema['name']
                    else:
                        schema_list.append(data)

                if not schema_base:
                    return 'Base Schema not found', 404
                
                if not schema_list:
                    return "No Schema files provided", 404

                try:
                    resoved_schema = resolve_references(schema_base, schema_list)
                    base_name, ext = os.path.splitext(schema_base_name)  # Split filename and extension
                    schema_base_name = f"{base_name}-resolved{ext}"  # Append '-resolved' and reattach extension                    
                    output = [{'schema_name': schema_base_name + '-resolved', "schema_fmt": 'jadn', 'schema': resoved_schema }]
                except Exception as err:            
                    tb = traceback.format_exc()
                    print(tb)
                    return str(err), 500

                return output, 200
            
            return 'Invalid Transformation', 500
            
    

# Register resources
resources = {
    Transform: {"urls": ("/", )},
}


def add_resources(bp, url_prefix=""):
    for cls, opts in resources.items():
        args = [f"{url_prefix}{url}" for url in opts["urls"]] + opts.get("args", [])
        bp.add_resource(cls, *args, **opts.get("kwargs", {}))
