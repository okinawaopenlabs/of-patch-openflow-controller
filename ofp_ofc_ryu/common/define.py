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

#!/usr/bin/env python
# -*- coding: utf-8 -*-


OFP_OFC_INSTANCE_NAME = 'ofp_ofc_instance_name'

MAJOR_VERSION			=	0
MINOR_VERSION			=	1
BUILD_VERSION			=	1

FLOW_PRIORITY_DROP					= 200
FLOW_PRIORITY_PACKET_IN				= 400
FLOW_PRIORITY_PACKET_IN_DISABLE		= 600
FLOW_PRIORITY_FLOW					= 800

FLOW_IDLE_TIMEOUT_NORMAL				= 65535		# About 18hour.
FLOW_IDLE_TIMEOUT_PACKET_IN_DISABLE		= 60 * 10	# 10minutes
FLOW_IDLE_TIMEOUT_NO_LIMIT				= 0
FLOW_HARD_TIMEOUT_NO_LIMIT				= 0

HTTP_STATUS_SUCCESS			= 200
HTTP_STATUS_CREATED_SUCCESS	= 201
HTTP_STATUS_BAD_REQUEST		= 400
HTTP_STATUS_INTL_SRV_ERR	= 500

SUCCESS_MSG				= "Success"
ERR_MSG_BAD_REQUEST		= "Bad Request"
ERR_MSF_INT_SRV_ERR		= "Internal server error"

