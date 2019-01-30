# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for the Mac initialization script."""

import mock
import unittest

from bot.init_scripts import mac
from tests.test_libs import helpers


class RunTest(unittest.TestCase):
  """Test run."""

  def setUp(self):
    helpers.patch(self, [
        'os.path.expanduser', 'system.shell.remove_directory',
        'system.shell.remove_file', 'subprocess.Popen'
    ])
    self.popen = mock.Mock()
    self.stdout = []

    def readline():
      return self.stdout.pop(0)

    self.popen.stdout.readline = readline
    self.mock.Popen.return_value = self.popen

    def expanduser(path):
      return path.replace('~', '/Users/chrome-bot')

    self.mock.expanduser.side_effect = expanduser

  def test_run(self):
    """Test run."""
    self.stdout = [
        'aaaa\n', 'bbbb\n',
        ('Path: /var/folders/bg/tn9j_qb532s4fz11rzz7m6sc0000gm/0'
         '//com.apple.LaunchServices-134500.csstore\n'), 'cccc\n', ''
    ]
    mac.run()

    self.mock.remove_directory.assert_has_calls([
        mock.call('/var/folders/bg/tn9j_qb532s4fz11rzz7m6sc0000gm/0'),
        mock.call('/var/folders/bg/tn9j_qb532s4fz11rzz7m6sc0000gm/T')
    ])