import os
from utils.file import YamlFile

def get_environment_url(filename = 'config.yml'):
	env = os.getenv('ENV', 'local')
	config = YamlFile.read(os.path.join(os.path.dirname(__file__), '..', filename))
	protocol = config['enviroment'][env]['protocol']
	sub_domain = config['enviroment'][env]['sub_domain']
	env_url = generate_url(protocol, sub_domain)
	return env_url

def generate_url(protocol='http', domain='localhost'):
	return protocol + '://' + domain + '/'