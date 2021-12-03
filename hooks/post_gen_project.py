import os
components_slug = ['{', '{', 'cookiecutter.project_slug', '}', '}']
components_title = ['{', '{', 'cookiecutter.project_title', '}', '}']
slug = ''.join(components_slug)
title = ''.join(components_title)
os.system('mkdir "%s"; echo "== %s\n\nWelcome to the %s project.\n" > "%s/README.adoc"; echo "Project ready!"' % (slug, title, title, slug))
