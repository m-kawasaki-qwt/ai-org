import pathlib
import re
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import org_timeline  # noqa: E402

FIX = pathlib.Path(__file__).resolve().parent / "fixtures" / "tl"


class OrgTimelineTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = pathlib.Path(tempfile.mkdtemp()) / "tl"
        shutil.copytree(FIX, cls.tmp)
        org_timeline.main(["x", str(cls.tmp)])
        cls.html = (cls.tmp / "timeline.html").read_text(encoding="utf-8")

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp.parent)

    def test_written_and_static(self):
        self.assertTrue(self.html.startswith("<!doctype html>"))
        self.assertNotRegex(self.html, r"https?://")
        self.assertNotIn("<script", self.html)

    def test_lanes_in_org_order(self):
        names = [m for m in ["tl/pm", "teams/t/leader", "teams/t/worker-1", "teams/t/reviewer", "teams/t/ghost"]]
        idx = [self.html.index(f"<b>{n.replace('tl/', '')}</b>") for n in names]
        self.assertEqual(idx, sorted(idx))
        self.assertLess(self.html.index("<b>user</b>"), idx[0])

    def test_kinds_and_unknown_shown(self):
        for k in ("start", "r_request", "r_ng", "mystery_kind"):
            self.assertIn(k, self.html)

    def test_noise_folded(self):
        self.assertNotIn("a00004", self.html)  # notify_sent
        self.assertNotIn("a00005", self.html)  # ack
        self.assertIn("ack 1 件", self.html)
        self.assertIn("notify_skipped 1 件", self.html)
        self.assertNotIn("a0000e", self.html)

    def test_body_escaped_and_readable(self):
        self.assertIn("&lt;script&gt;alert(1)&lt;/script&gt; &amp; 本文です", self.html)

    def test_session_numbers(self):
        self.assertIn("2,706,908", self.html)
        self.assertIn("12.1", self.html)
        self.assertIn("2.71M", self.html)

    def test_gap_column_and_lifecycle(self):
        self.assertRegex(self.html, r"<th class=gap>⋯<br>19分")
        self.assertIn("起動 10:21:00 → 終了 10:22:00", self.html)

    def test_multi_launch_labelled_and_no_dash(self):
        self.assertIn("（最後の起動分のみ）", self.html)
        self.assertNotIn("<small>-</small>", self.html)

    def test_yaml_reader(self):
        m = org_timeline.read_yaml_machine(FIX / "reports/sessions/tl__teams__t__worker-1.yaml")
        self.assertEqual(m["id"], "tl/teams/t/worker-1")
        self.assertEqual(m["tokens_total"], "2706908")
        self.assertNotIn("input", m)


if __name__ == "__main__":
    unittest.main()
