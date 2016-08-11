#Python   code block   to   set   ip   address
#
# Copyright (c) 2015 Dell Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# THIS CODE IS PROVIDED ON AN #AS IS* BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT
#  LIMITATION ANY IMPLIED WARRANTIES OR CONDITIONS OF TITLE, FITNESS
# FOR A PARTICULAR PURPOSE, MERCHANTABLITY OR NON-INFRINGEMENT.
#
# See the Apache Version 2.0 License for specific language governing
# permissions and limitations under the License.
#
import   cps_utils
#  Populate   the   attributes   for   the   CPS   Object
ifindex=16
ip_addr="10.0.0.1"
pfix_len=16
ip_attributes   =  {"base-ip/ipv4/ifindex":   ifindex,"ip":ip_addr,"prefix-length":pfix_len}

#  Create   CPS   Object
cps_utils.add_attr_type('base-ip/ipv4/address/ip',"ipv4")
cps_obj=cps_utils.CPSObject('base-ip/ipv4/address',data=ip_attributes)

#  Create   the   CPS   Transaction for object create
cps_update   =  ('create',   cps_obj.get())
transaction   =  cps_utils.CPSTransaction([cps_update])

#  Commit   the   transaction
ret   =  transaction.commit()

#  Check   for   failure
if not   ret:
    raise   RuntimeError   ("Error   ")
