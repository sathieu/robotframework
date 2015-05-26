#  Copyright 2015 Mathieu Parent <math.parent@gmail.com>
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import sys
if sys.platform.startswith('java'):
    from java.awt import Robot
else:
    try:
        import pyautogui
    except ImportError:
        pyautogui = None

from robot.version import get_version


class Mouse(object):
    """Test library for manipulating mouse on the machine where tests are run.

    = Using with Python =

    With Python you need to have one of the following modules installed to be
    able to use this library. The first module that is found will be used.

    - pyautogui :: https://pyautogui.readthedocs.org/

    = Using with Jython =

    With Jython this library uses APIs provided by the JVM platforms. This API
    is always available and thus no external modules are needed.

    = Using with IronPython =

    This library is not compatible with IronPython.

    """

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    ROBOT_LIBRARY_VERSION = get_version()

    def __init__(self, screenshot_directory=None):
        if sys.platform.startswith('java'):
            self._click = self._java_click
            self._move = self._java_move
        elif sys.platform == 'cli':
            self._click = self._no_click
            self._move = self._no_move
        else:
            if pyautogui:
                self._click = self._pyautogui_click
                self._move = self._pyautogui_move
            else:
                self._click = self._no_click
                self._move = self._no_move


    def click(self):
        """Click at the current position.
        """
        self._click()

    def click_at(self, x, y):
        """Click at specified position.
        """
        self._move(x, y)
        self._click()

    def right_click(self):
        """Right-click at the current position.
        """
        self._click('right')

    def right_click_at(self, x, y):
        """Right-click at specified position.
        """
        self._move(x, y)
        self._click('right')

    def move_mouse_at(self, x, y):
        """Click at the current position.
        """
        self._move(x, y)

    def _pyautogui_move(self, x, y):
        """Internal PyAutoGUI method to move pointer.
        """
        pyautogui.moveTo(x, y)

    def _pyautogui_click(self, button='left'):
        """Internal PyAutoGUI method to click.
        """
        pyautogui.click(button)

    def _no_move(self, x, y):
        """Internal failing method to move pointer.
        """
        raise RuntimeError('Moving mouse is not supported on this platform '
                           'by default. See library documentation for details.')

    def _no_click(self, button='left'):
        """Internal failing method to click.
        """
        raise RuntimeError('Clicking is not supported on this platform '
                           'by default. See library documentation for details.')

