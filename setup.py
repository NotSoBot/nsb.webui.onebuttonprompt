from setuptools import find_packages, setup

setup_kwargs = {
    'name': 'OneButtonPrompt',
    'version': '0.0.1',
    'url': 'https://github.com/notsobot/nsb.webui.onebuttonprompt',
    'author': 'AIrjen',
    'description': (
        'Generate prompts',
    ),
    'package_dir': {
        'onebuttonprompt': '__init__.py',
    },
    'include_package_data': True,
    'platforms': 'any',
}

setup(**setup_kwargs)
