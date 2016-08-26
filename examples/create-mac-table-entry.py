### Configure MAC address table entry
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
import   cps_utils

cps_utils.add_attr_type("base-mac/table/mac-address",   "mac")

d  =     {"mac-address":   "00:0a:0b:cc:0d:0e", "ifindex":   18, "vlan":   "100"}
obj   =  cps_utils.CPSObject('base-mac/table',data=   d)
tr_obj   =  ('create',   obj.get())

transaction   =  cps_utils.CPSTransaction([tr_obj])
ret   =  transaction.commit()

if not   ret:
    raise   RuntimeError   ("Error   creating   MAC   Table   Entry") 


