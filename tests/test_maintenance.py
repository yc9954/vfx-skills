import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "tools" / f"{name}.py")
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


class PublishTests(unittest.TestCase):
    def test_no_private_data(self):
        check = module("check_publish").violations
        self.assertEqual(check("README.md", b"safe documentation"), [])
        self.assertIn("private/cache path", check(".local/token", b"private"))
        token = ("hf_" + "x" * 32).encode()
        self.assertIn("provider_token", check("src/example.py", token))
        self.assertIn("binary file", check("docs/movie.mp4", b"\0data"))
        self.assertIn("symlink/submodule is not publishable", check("skills/example", b"elsewhere", "120000"))

    def test_python_paths_with_spaces(self):
        migrate = module("migrate_legacy_paths")
        before = 'from pathlib import Path\np = Path("/old/root/some file")\n'
        after = migrate.transform_python(before, "/old/root", "/new/VFX Skills/.local/legacy")
        namespace = {}
        exec(after, namespace)
        self.assertEqual(str(namespace["p"]), "/new/VFX Skills/.local/legacy/some file")

    def test_shell_paths_stay_quoted(self):
        # zsh is a macOS maintenance dependency, not needed by Linux runtime/CI.
        import shutil
        if not shutil.which("zsh"):
            self.skipTest("macOS migration check requires zsh")
        migrate = module("migrate_legacy_paths")
        after = migrate.transform_shell('cd /old/root/pipeline\nexport CACHE=/old/root/cache\n',
                                        "/old/root", "/new/VFX Skills/.local/legacy")
        self.assertIn('cd "/new/VFX Skills/.local/legacy/pipeline"', after)
        self.assertIn('export CACHE="/new/VFX Skills/.local/legacy/cache"', after)


if __name__ == "__main__":
    unittest.main()
