import os

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_IMAGE']
c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']
c.JupyterHub.hub_ip = os.environ['HUB_IP']
#c.Spawner.default_url = '/lab'
c.JupyterHub.services = [
    {
        'name': 'cull_idle',
        'admin': True,
        'command': 'python /srv/jupyterhub/cull_idle_servers.py --timeout=3600'.split(),
    },
]

notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan'
#notebook_dir= '~/'
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }
c.LocalAuthenticator.create_system_users = True

# our user list
c.Authenticator.whitelist = [
    'troy',
    'joe',
    'michael',
]


c.JupyterHub.load_groups = {
    'shared': [
        'joe',
        'michael',
    ]
}

#service_name = 'shared-notebook'
#service_port = 9999
#group_name = 'shared'
#
## start the notebook server as a service
#c.JupyterHub.services = [
#    {
#        'name': service_name,
#        'url': 'http://{}:{}'.format(os.environ['HUB_IP'], service_port),
#        'command': [
#            'jupyterhub-singleuser',
#            '--group={}'.format(group_name),
#            '--debug',
#        ],
#    }
#]
