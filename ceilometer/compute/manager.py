# -*- encoding: utf-8 -*-
#
# Copyright © 2012-2013 eNovance <licensing@enovance.com>
#
# Author: Julien Danjou <julien@danjou.info>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from ceilometer import agent
from ceilometer.compute.virt import inspector as virt_inspector
from ceilometer.openstack.common import log
from ceilometer.openstack.common import service as os_service
from ceilometer import service

LOG = log.getLogger(__name__)


class AgentManager(agent.AgentManager):

    def __init__(self):
        super(AgentManager, self).__init__('compute', ['local_instances'])
        self._inspector = virt_inspector.get_hypervisor_inspector()

    @property
    def inspector(self):
        return self._inspector


def agent_compute():
    service.prepare_service()
    os_service.launch(AgentManager()).wait()
