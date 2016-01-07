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

import httplib2
import unirest

from common import log
from common import conf

LOG = log.getLogger(__name__)
CONF = conf.read_conf()

unirest.timeout(60)

class OfpmClient:

	def init_flow(self, dpid):
		header = {'Content-type':'application/json'}
		body = {'datapathId':"0x" + "{:0>16x}".format(dpid)}
		LOG.debug("body = " + str(body))
		LOG.info("Request initFlow body = " + str(body))
		res = unirest.post(CONF.ofpm_init_flow_url, headers=header, params=str(body), callback=self.__http_response__)
		return

	def __http_request__(self, url, method, header, body=None):
		LOG.debug("START")
		LOG.debug("url = " + url + ", method = " + method + ", header = " + str(header) + ", body = " + str(body))

		resp, content = httplib2.Http().request(url, method, headers=header, body=body)
		LOG.info("Request Result = %s", str(content))
		LOG.debug("END")
		return resp, content

	def __http_response__(self, res):
		LOG.debug("START")
		LOG.info("Response status = " + str(res.code) + ", body = " + str(res.body))
		LOG.debug("END")
