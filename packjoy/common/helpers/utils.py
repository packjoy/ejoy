from flask import current_app, request

'''
This is to add response header
required by the AMP Cache
not sure if it works here
'''
@current_app.after_request
def apply_cors_to_amp_cache(response):
	response.headers["Access-Control-Allow-Origin"] = '*.ampproject.org'
	response.headers["Access-Control-Allow-Origin"] = '*.amp.cloudflare.com'
	source_origin = request.args.get('__amp_source_origin', '')
	if source_origin:
		response.headers["AMP-Access-Control-Allow-Source-Origin"] = source_origin
	response.headers["Access-Control-Expose-Headers"] = 'Access-Control-Expose-Headers'
	return response


def get_resource_as_string(name, charset='utf-8'):
		with current_app.open_resource(name) as f:
			return f.read().decode(charset)



