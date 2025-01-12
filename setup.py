from setuptools import find_packages, setup

setup_kwargs = {
    'name': 'onebuttonprompt',
    'version': '0.0.1',
    'url': 'https://github.com/notsobot/nsb.webui.onebuttonprompt',
    'author': 'AIrjen',
    'description': (
        'Generate prompts',
    ),
    'packages': find_packages(include=['src', 'src.*']),
    'include_package_data': True,
    'platforms': 'any',
}

setup(**setup_kwargs)
