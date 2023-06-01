[comment]: # "Auto-generated SOAR connector documentation"
# RSA SecureID Authentication Manager

Publisher: Splunk  
Connector Version: 1.0.0  
Product Vendor: RSA  
Product Name: RSA SecureID Authentication Manager  
Product Version Supported (regex): ".\*"  
Minimum Product Version: 5.4.0  

RSA SucureID Authentication Manager app to enable and revoke RSA token

[comment]: # "File: README.md"
[comment]: # "Copyright (c) 2023 Splunk Inc."
[comment]: # ""
[comment]: # "Licensed under the Apache License, Version 2.0 (the 'License');"
[comment]: # "you may not use this file except in compliance with the License."
[comment]: # "You may obtain a copy of the License at"
[comment]: # ""
[comment]: # "    http://www.apache.org/licenses/LICENSE-2.0"
[comment]: # ""
[comment]: # "Unless required by applicable law or agreed to in writing, software distributed under"
[comment]: # "the License is distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,"
[comment]: # "either express or implied. See the License for the specific language governing permissions"
[comment]: # "and limitations under the License."
[comment]: # ""



### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a RSA SecureID Authentication Manager asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**url** |  required  | string | URL (e.g. https://10.10.10.10)
**username** |  required  | string | SSH User
**password** |  required  | password | Password For SSH User

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied configuration  
[enable token](#action-enable-token) - Enables RSA SecureID token  
[disable token](#action-disable-token) - Disables RSA SecureID token  

## action: 'test connectivity'
Validate the asset configuration for connectivity using supplied configuration

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'enable token'
Enables RSA SecureID token

Type: **correct**  
Read only: **False**

The token must be assigned to a user.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**super_admin_user** |  required  | Super Admin User | string | 
**super_admin_user_password** |  required  | Password For Super Admin User | string | 
**token** |  required  | Token serial of RSA SecureID token | string |  `rsa secureid token` 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |  
action_result.parameter.super_admin_user | string |  |  
action_result.parameter.super_admin_user_password | string |  |  
action_result.parameter.token | string |  |   0056121890128 
action_result.data | string |  |  
action_result.message | string |  |  
action_result.summary | string |  |  
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'disable token'
Disables RSA SecureID token

Type: **contain**  
Read only: **False**

The token must be assigned to a user.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**super_admin_user** |  required  | Super Admin User | string | 
**super_admin_user_password** |  required  | Password For Super Admin User | string | 
**token** |  required  | Token serial of RSA SecureID token | string |  `rsa secureid token` 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |  
action_result.parameter.super_admin_user | string |  |  
action_result.parameter.super_admin_user_password | string |  |  
action_result.parameter.token | string |  |   0056121890128 
action_result.status | string |  |  
action_result.data | string |  |  
action_result.message | string |  |  
action_result.summary | string |  |  
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1 