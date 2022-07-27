import unittest

from pi_monitor import Builder


class PiMonitorTestCase(unittest.TestCase):
    # smoke test - does it build?
    def test_builds_app(self):
        runner = Builder().build_for_computer()


if __name__ == '__main__':
    unittest.main()
