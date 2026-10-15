#!/usr/bin/env python3
"""Open an existing custom Mail installation without changing configuration."""
import os
from pathlib import Path
import shutil
import subprocess


def find_app(home, configured=None):
    prefixes = [Path(configured)] if configured else [
        home / '.local/opt/evolution-omarchy',
        home / '.local/opt/evolution-personal',
    ]
    for prefix in prefixes:
        for name in ('omarchy-mail', 'evolution'):
            app = prefix / 'bin' / name
            if prefix.is_absolute() and app.is_file() and os.access(app, os.X_OK):
                return app
    return None


def main():
    app = find_app(Path.home(), os.environ.get('EVOLUTION_OMARCHY_PREFIX'))
    if app:
        os.execv(str(app), [str(app)])
    message = ('Build and install Evolution for Omarchy first. '
               'See the Mail plugin README for manual setup instructions.')
    print(message)
    if shutil.which('notify-send'):
        subprocess.run(['notify-send', 'Mail needs setup', message], check=False)
    return 1


if __name__ == '__main__':
    raise SystemExit(main())
