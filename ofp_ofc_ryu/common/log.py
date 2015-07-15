#   Copyright 2015 Okinawa Open Laboratory, General Incorporated Association
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import logging
import os
import traceback

from common import conf

CONF = conf.read_conf()

def _get_log_file_path():
	logfile = CONF.log_file
	logdir = CONF.log_dir

	if logfile and not logdir:
		return logfile

	if logfile and logdir:
		return os.path.join(logdir, logfile)

	return None

def _set_logger_cfg(log_root):
	_fmt = CONF.logging_default_format_string
	if (CONF.debug and CONF.logging_debug_format_suffix):
		_fmt += ' ' + CONF.logging_debug_format_suffix
	logpath = _get_log_file_path()
	if logpath:
		filelog = logging.handlers.WatchedFileHandler(logpath)
		filelog.setFormatter(logging.Formatter(fmt=_fmt))
		log_root.addHandler(filelog)
	if CONF.debug:
		log_root.setLevel(logging.DEBUG)
	elif CONF.verbose:
		log_root.setLevel(logging.INFO)
	else:
		log_root.setLevel(logging.WARNING)
	return log_root

def getLogger(name='ofp-ofc'):
	return _set_logger_cfg(logging.getLogger(name))

