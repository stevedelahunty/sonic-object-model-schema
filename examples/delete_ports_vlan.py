#Python code block to delete port to VLAN
#
# Copyright (c) 2015 Dell Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# THIS CODE IS PROVIDED ON AN *AS IS* BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT
# LIMITATION ANY IMPLIED WARRANTIES OR CONDITIONS OF TITLE, FITNESS
# FOR A PARTICULAR PURPOSE, MERCHANTABLITY OR NON-INFRINGEMENT.
#
# See the Apache Version 2.0 License for specific language governing
# permissions and limitations under the License.
#
import cps
import cps_object
# Create CPS Object
cps_obj = cps_object.CPSObject('dell-base-if-cmn/if/interfaces/interface')
# Populate the Vlan attributes VLAN_ID='br100'
VLAN_ID='br100'
cps_obj.add_attr('if/interfaces/interface/name',VLAN_ID)
# Delete the untagged-ports from VLAN, include the ports which is needed in the if_port_list
if_port_list=['e101-002-0']
cps_obj.add_attr('dell-if/if/interfaces/interface/untagged-ports',if_port_list)
# Associate a CPS Set Operation with the CPS Object
cps_update = {'change':cps_obj.get(),'operation': 'set'}
# Add the CPS operation,obj pair to a new CPS Transaction
transaction = cps.transaction([cps_update])
# Check for failure
if not transaction:
    raise RuntimeError ("Error in deleting ports to Vlan")
print "successful"