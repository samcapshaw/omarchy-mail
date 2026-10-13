from pathlib import Path
import tempfile
import unittest
from launch import find_app


class LaunchTests(unittest.TestCase):
    def test_missing_app_does_not_fall_back_to_system_evolution(self):
        with tempfile.TemporaryDirectory() as folder:
            self.assertIsNone(find_app(Path(folder)))

    def test_default_and_explicit_installations(self):
        with tempfile.TemporaryDirectory() as folder:
            home = Path(folder)
            app = home / '.local/opt/evolution-omarchy/bin/evolution'
            app.parent.mkdir(parents=True)
            app.write_text('#!/bin/sh\nexit 0\n')
            self.assertIsNone(find_app(home))
            app.chmod(0o755)
            self.assertEqual(find_app(home), app)
            self.assertIsNone(find_app(home, str(home / 'missing')))
            self.assertIsNone(find_app(home, 'relative/path'))
            self.assertEqual(find_app(home, str(app.parent.parent)), app)


if __name__ == '__main__':
    unittest.main()
