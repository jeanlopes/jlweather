from distutils.core import setup

data_files = [('share/applications', ['jlweather.desktop']),
			  ('/etc/xdg/autostart', ['jlweather.desktop'])]

setup(name='jlweather',
	  author='Jean Lopes',
	  author_email='jeanoliveiralopes@gmail.com',
	  url='https://github.com/jeanlopes/jlweather',
	  license='GPL',
	  version='0.1',
	  description='A small app system tray to show current weather forecast',
	  keywords='weather, forecast',
	  packages=['jlweather', 'jlweather.lib', 'jlweather.lib.cssselect', 'jlweather.lib.daemon', 'jlweather.lib.daemon.version'],
	  data_files=data_files,
	  scripts=['scripts/jlweather'])