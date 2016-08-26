/*
 * Copyright (c) 2016 Dell Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may
 * not use this file except in compliance with the License. You may obtain
 * a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
 *
 * THIS CODE IS PROVIDED ON AN *AS IS* BASIS, WITHOUT WARRANTIES OR
 * CONDITIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT
 * LIMITATION ANY IMPLIED WARRANTIES OR CONDITIONS OF TITLE, FITNESS
 * FOR A PARTICULAR PURPOSE, MERCHANTABLITY OR NON-INFRINGEMENT.
 *
 * See the Apache Version 2.0 License for specific language governing
 * permissions and limitations under the License.
 */
/****************************************************************** 
Template for an event publish function.

*******************************************************************/

cps_api_return_code_t   event_publish(cps_api_object_t   event_obj)
{
  static   bool init_flag   =  false;
  static   cps_api_event_service_handle_t   handle;


  if (!init_flag)   {
    /*   Not   initialized
	 =>   Connect   to   CPS   event   subsystem
    */
    if (cps_api_event_service_init()   !=   cps_api_ret_code_OK)   {
      return   (cps_api_ret_code_ERR);
    }


    if (cps_api_event_client_connect(&handle)   !=
	cps_api_ret_code_OK
	) {
      return   (cps_api_ret_code_ERR);
    }

    /*   Mark   as initialized   */
    init_flag   =  true;
  }

  cps_api_return_code_t   result; 

  /*   Publish   the   given   object   */
  result   =  cps_api_event_publish(handle,   event_obj);

  /*   Consume   the   given   object   */
  cps_api_object_delete(event_obj);

  return   (result);
}

