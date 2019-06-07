from utils.environment import get_environment_url

def before_all(context):
	context.resource_url = get_environment_url()
