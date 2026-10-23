import datetime as dt
import io
import json
import pathlib
import shutil
import sys
import tempfile
import unittest
from contextlib import redirect_stdout

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import org_status  # noqa: E402

FIX = pathlib.Path(__file__).resolve().parent / "fixtures" / "fx"
NOW = dt.datetime.fromisoformat("2026-10-23T10:40:00+09:00")


def members(tree):
    out = {m["name"]: m for m in tree["members"]}
    for c in tree["children"]:
        out.update(members(c))
    return out


class OrgStatusTest(unittest.TestCase):
    def setUp(self):
        self.tree = org_status.build_status(FIX, NOW)
        self.m = members(self.tree)

    def test_tree_shape(self):
        self.assertEqual(self.tree["id"], "fx")
        self.assertEqual(self.tree["children"][0]["id"], "fx/teams/t")
        self.assertEqual(set(self.m), {"pm", "a", "b", "c", "d"})

    def test_not_launched(self):
        self.assertEqual(self.m["a"]["state"], "未起動")
        self.assertIsNone(self.m["a"]["last_report"])

    def test_running_ignores_noise(self):
        b = self.m["b"]
        self.assertEqual(b["state"], "動いている")
        self.assertEqual(b["last_report"]["kind"], "report")   # ack は数えない
        self.assertEqual(b["last_report"]["minutes_ago"], 40.0)

    def test_done(self):
        self.assertEqual(self.m["c"]["state"], "終わった")
        self.assertEqual(self.m["c"]["last_report"]["minutes_ago"], 20.0)

    def test_closed_by_status(self):
        self.assertEqual(self.m["d"]["state"], "片づけ済み")

    def test_closed_when_member_dir_removed(self):
        with tempfile.TemporaryDirectory() as t:
            dst = pathlib.Path(t) / "fx"
            shutil.copytree(FIX, dst)
            shutil.rmtree(dst / "teams/t/c")
            m = members(org_status.build_status(dst, NOW))
            self.assertEqual(m["c"]["state"], "片づけ済み")

    def test_text_and_json(self):
        text = org_status.render(self.tree)
        for s in ("未起動", "動いている", "終わった", "片づけ済み", "40.0 分前"):
            self.assertIn(s, text)
        buf = io.StringIO()
        with redirect_stdout(buf):
            org_status.main([str(FIX), "--json"])
        self.assertEqual(json.loads(buf.getvalue())["id"], "fx")


if __name__ == "__main__":
    unittest.main()
