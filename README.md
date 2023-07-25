[comment]: # "Auto-generated SOAR connector documentation"
# RSA SecureID Authentication Manager

Publisher: Splunk  
Connector Version: 1.0.0  
Product Vendor: RSA  
Product Name: RSA SecureID Authentication Manager  
Product Version Supported (regex): ".\*"  
Minimum Product Version: 6.0.2  

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
**hostname** |  required  | string | IP/Hostname (e.g. 10.10.10.10)
**username** |  required  | string | SSH User
**password** |  required  | password | Password For SSH User
**super_admin_user** |  optional  | string | Super Admin User
**super_admin_user_password** |  optional  | password | Password For Super Admin User

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied configuration  
[enable token](#action-enable-token) - Enables RSA SecureID token to grant user access  
[revoke token](#action-revoke-token) - Revoke RSA SecureID token to block user access  
[list tokens](#action-list-tokens) - List RSA SecureID tokens  

## action: 'test connectivity'
Validate the asset configuration for connectivity using supplied configuration

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'enable token'
Enables RSA SecureID token to grant user access

Type: **generic**  
Read only: **False**

The token must be assigned to a user to run this action.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**token_serial** |  required  | Token serial of assigned RSA SecureID token | string |  `rsa token` 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.token_serial | string |  `rsa token`  |   0056121890128 
action_result.data | string |  |  
action_result.summary | string |  |  
action_result.message | string |  |  
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'revoke token'
Revoke RSA SecureID token to block user access

Type: **generic**  
Read only: **False**

The token must be assigned to a user to run this action.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**token_serial** |  required  | Token serial of assigned RSA SecureID token | string |  `rsa token` 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.token_serial | string |  `rsa token`  |   0056121890128 
action_result.data | string |  |  
action_result.summary | string |  |  
action_result.message | string |  |  
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'list tokens'
List RSA SecureID tokens

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**list_only_assigned_tokens** |  optional  | List RSA SecureID assigned Tokens | boolean | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.list_only_assigned_tokens | boolean |  |   True  False 
action_result.data.\*.status | string |  |   Enabled  Disabled 
action_result.data.\*.token_serial | string |  `rsa token`  |   068283706629 
action_result.summary | string |  |  
action_result.summary.total_tokens | numeric |  |   25 
action_result.message | string |  |  
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1 