from setuptools import setup, find_packages

setup(name='StompWS',

      version='0.0.1',

      url='https://github.com/veithly/PyStompWS',

      license='MIT',

      author='RickyShao',

      author_email='veithly@live.com',

      description='A WebSocket client based on the Stomp protocol',

      keywords='stomp, websocket',

      packages=find_packages(exclude=['test', 'weights', 'config', 'data']),

      long_description=open('README.md', encoding='utf-8').read(),

      zip_safe=False,

      install_requires=['websocket_client>=0.57.0'])
