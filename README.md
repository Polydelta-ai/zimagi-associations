<p align="center">
  <img width="460" height="150" src="assets/zimagi-logo.png">
</p>
<hr/>

<h1 align="center"><b>Trade Association</b> <i>Data Module</i></h1>
<br/>

## Dependencies
<hr/>
<br/>
This Zimagi module **requires and builds on** the following modules:

<br/>

 * [**Organization Data Module**](https://github.com/Polydelta-ai/zimagi-organizations)

<br/>

## Overview
<hr/>
<br/>

This module provides association models that have general location, informational, and size data sourced and imported from the Directory of Associations.

<br/>

## Components
<hr/>
<br/>

### Roles
<br/>

| _Name_ | _Description_ |
| ---- | ----------- |
| **association-admin** | _Administrative privileges over association related data_ |
<br/>

### Data Models
<br/>

| _Name_ | _Description_ |
| ---- | ----------- |
| **association** | _Data model that extends organization with association informational fields_ |
<br/>

### Plugin Providers
<br/>

| _Name_ | _Type_ | _Description_ |
| ---- | ---- | ----------- |
| **directory_of_associations** | **source** | _Requests association data from the Directory of Associations web site_ |
<br/>

### Importers and Calculations
<br/>

| _Name_ | _Type_ | _Description_ |
| ---- | ---- | ----------- |
| **directory_of_associations_ak** | **import** | _Imports Directory of Associations data for Alaska into internal data models_ |
| **directory_of_associations_al** | **import** | _Imports Directory of Associations data for Alabama into internal data models_ |
| **directory_of_associations_ar** | **import** | _Imports Directory of Associations data for Arkansas into internal data models_ |
| **directory_of_associations_az** | **import** | _Imports Directory of Associations data for Arizona into internal data models_ |
| **directory_of_associations_ca** | **import** | _Imports Directory of Associations data for California into internal data models_ |
| **directory_of_associations_co** | **import** | _Imports Directory of Associations data for Colorado into internal data models_ |
| **directory_of_associations_ct** | **import** | _Imports Directory of Associations data for Connecticut into internal data models_ |
| **directory_of_associations_dc** | **import** | _Imports Directory of Associations data for District of Columbia into internal data models_ |
| **directory_of_associations_de** | **import** | _Imports Directory of Associations data for Delaware into internal data models_ |
| **directory_of_associations_fl** | **import** | _Imports Directory of Associations data for Florida into internal data models_ |
| **directory_of_associations_ga** | **import** | _Imports Directory of Associations data for Georgia into internal data models_ |
| **directory_of_associations_hi** | **import** | _Imports Directory of Associations data for Hawaii into internal data models_ |
| **directory_of_associations_ia** | **import** | _Imports Directory of Associations data for Iowa into internal data models_ |
| **directory_of_associations_id** | **import** | _Imports Directory of Associations data for Idaho into internal data models_ |
| **directory_of_associations_il** | **import** | _Imports Directory of Associations data for Illinois into internal data models_ |
| **directory_of_associations_in** | **import** | _Imports Directory of Associations data for Indiana into internal data models_ |
| **directory_of_associations_ks** | **import** | _Imports Directory of Associations data for Kansas into internal data models_ |
| **directory_of_associations_ky** | **import** | _Imports Directory of Associations data for Kentucky into internal data models_ |
| **directory_of_associations_la** | **import** | _Imports Directory of Associations data for Louisiana into internal data models_ |
| **directory_of_associations_ma** | **import** | _Imports Directory of Associations data for Massachusetts into internal data models_ |
| **directory_of_associations_md** | **import** | _Imports Directory of Associations data for Maryland into internal data models_ |
| **directory_of_associations_me** | **import** | _Imports Directory of Associations data for Maine into internal data models_ |
| **directory_of_associations_mi** | **import** | _Imports Directory of Associations data for Michigan into internal data models_ |
| **directory_of_associations_mn** | **import** | _Imports Directory of Associations data for Minnesota into internal data models_ |
| **directory_of_associations_mo** | **import** | _Imports Directory of Associations data for Missouri into internal data models_ |
| **directory_of_associations_ms** | **import** | _Imports Directory of Associations data for Mississippi into internal data models_ |
| **directory_of_associations_mt** | **import** | _Imports Directory of Associations data for Montana into internal data models_ |
| **directory_of_associations_nc** | **import** | _Imports Directory of Associations data for North Carolina into internal data models_ |
| **directory_of_associations_nd** | **import** | _Imports Directory of Associations data for North Dakota into internal data models_ |
| **directory_of_associations_ne** | **import** | _Imports Directory of Associations data for Nevada into internal data models_ |
| **directory_of_associations_nh** | **import** | _Imports Directory of Associations data for New Hampshire into internal data models_ |
| **directory_of_associations_nj** | **import** | _Imports Directory of Associations data for New Jersey into internal data models_ |
| **directory_of_associations_nm** | **import** | _Imports Directory of Associations data for New Mexico into internal data models_ |
| **directory_of_associations_nv** | **import** | _Imports Directory of Associations data for Nevada into internal data models_ |
| **directory_of_associations_ny** | **import** | _Imports Directory of Associations data for New York into internal data models_ |
| **directory_of_associations_oh** | **import** | _Imports Directory of Associations data for Ohio into internal data models_ |
| **directory_of_associations_ok** | **import** | _Imports Directory of Associations data for Oklahoma into internal data models_ |
| **directory_of_associations_or** | **import** | _Imports Directory of Associations data for Oregon into internal data models_ |
| **directory_of_associations_pa** | **import** | _Imports Directory of Associations data for Pennsylvania into internal data models_ |
| **directory_of_associations_ri** | **import** | _Imports Directory of Associations data for Rhode Island into internal data models_ |
| **directory_of_associations_sc** | **import** | _Imports Directory of Associations data for South Carolina into internal data models_ |
| **directory_of_associations_sd** | **import** | _Imports Directory of Associations data for South Dakota into internal data models_ |
| **directory_of_associations_tn** | **import** | _Imports Directory of Associations data for Tennessee into internal data models_ |
| **directory_of_associations_tx** | **import** | _Imports Directory of Associations data for Texas into internal data models_ |
| **directory_of_associations_ut** | **import** | _Imports Directory of Associations data for Utah into internal data models_ |
| **directory_of_associations_va** | **import** | _Imports Directory of Associations data for Virginia into internal data models_ |
| **directory_of_associations_vt** | **import** | _Imports Directory of Associations data for Vermont into internal data models_ |
| **directory_of_associations_wa** | **import** | _Imports Directory of Associations data for Washington into internal data models_ |
| **directory_of_associations_wi** | **import** | _Imports Directory of Associations data for Wisconsin into internal data models_ |
| **directory_of_associations_wv** | **import** | _Imports Directory of Associations data for West Virginia into internal data models_ |
| **directory_of_associations_wy** | **import** | _Imports Directory of Associations data for Wyoming into internal data models_ |
<br/>

### Orchestration Profiles
<br/>

| _Name_ | _Description_ |
| ---- | ----------- |
| **build** | _Builds data centric Zimagi specifications_ |
<br/>

## How to Use
<hr/>
<br/>

_From the Linux command line interface:_

```bash
# Install the Zimagi application and remote client

pip install zimagi

# Initialize Zimagi platform and make any configuration updates

zimagi env get
#
# The first time executed the zimagi command will provide a link
# to the autogenerated configuration file for the user.  Make any
# changes to this file and run the zimagi command again to continue
# initializing the platform
#

# Install this module into the Zimagi platform

zimagi module add \
    https://github.com/Polydelta-ai/zimagi-associations.git \
    reference=main

# Import data
zimagi import --tags=association

# Work with the Zimagi association related data models
# (also available through the Command API)

zimagi association list --help
zimagi association get --help
zimagi association save --help
zimagi association remove --help
zimagi association clear --help

# Access association related data through the Data API

# List or search associations
curl https://localhost:5323/association
# Get JSON list of specific fields for searchable associations
curl https://localhost:5323/association/json
# Get a CSV export of specific fields for searchable associations
curl https://localhost:5323/association/csv
# Get a total count of searchable associations with field name (non NULL)
curl https://localhost:5323/association/count/{field_name}
# Get a list of unique field values for searchable associations (non NULL)
curl https://localhost:5323/association/values/{field_name}
```

_From a Python script:_

```bash
# First ensure zimagi is added to environment or requirements.txt
zimagi>=0.8.0
```

```python
# Import the zimagi package
import zimagi

# Create a message handler for streaming Command API messages
# (if you need or want)
def message_callback(message):
    message.display()

# Create API gateway (using default/development settings)
api = zimagi.Client(
    user = "admin",
    token = "uy5c8xiahf93j2pl8s00e6nb32h87dn3",
    encryption_key = "RFJwNYpqA4zihE8jVkivppZfGVDPnzcq",
    host = "localhost",
    command_port = 5123,
    data_port = 5323,
    message_callback = message_callback
)

# Add Zimagi module

api.extend('https://github.com/Polydelta-ai/zimagi-associations.git', 'main',
    provider = 'git'
)

# Execute any Zimagi command
#
# Can reference commands using:
#
# * space separated strings "user list" (CLI format)
# * slash separated strings "user/list" (API format)
# * dot separated strings   "user.list"
#
response = api.execute('association.list')
#
# OR
#
response = api.association__list() # __ converted to /

#
# Association SDK interface
#

# Import associations
api.run_imports(tags = ['association'])

# Save or update association related information
api.save('association', None, # key is autogenerated
    name = "Super Association",
    city = "Washington",
    state = "DC",
    zipcode = 20024
)

# List and search access associations (hyperlinked related objects)
results = api.list('association', name__icontains = "Engineering")

# Return field collections in various formats
json_results = api.json('association', fields = ['name', 'city', 'state'])
df = api.dataframe('association', fields = ['name', 'zipcode'])

# Access association data
data = api.get('association', "{key}")

# Get association field information
results = api.values('association', 'name')
count = api.count('association', 'name')

# Remove associations
api.remove('association', "{key}")
api.clear('association', staff_count__gte = 100)
```