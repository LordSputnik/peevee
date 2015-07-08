# -*- coding: utf-8 -*-

# Copyright (c) 2015 Ben Ockmore

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

""" This modules validates and transforms paths for the ext4 file system. ext4
is a filesystem commonly used in modern Linux variants. ext4 has a maximum
filename length of 255 bytes, and allows all characters apart from NUL and /,
and all filenames apart from "." and "..".
"""

import pathlib
import six


def validate(input_path):
    """ Validates a unicode input path for the ext4 filesystem. """

    if not isinstance(input_path, six.text_type):
        raise TypeError("ext4.validate: input path must be a unicode string")

    # First, split path into parts - this has a side effect of removing
    # '/' characters
    input_path = pathlib.PurePath(input_path)
    if input_path.is_absolute():
        parts = input_path.parts[1:]
    else:
        parts = input_path.parts

    for part in parts:
        part = part.encode('utf8')
        if len(part) > 255 or '\x00' in part:
            return False

        if part in ['.', '..']:
            return False

    return True
