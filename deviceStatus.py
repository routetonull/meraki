#!/usr/bin/python3.6
from meraki import meraki

apikey = "myAPIkey" # created with meraki dashboard
company = "companyName" # as shown in meraki dashboard

orgs = meraki.myorgaccess(apikey, suppressprint=True)
c = list(filter(lambda o : o.get('name') == company,orgs))

if list:
  c = c[0]
  orgid = c.get('id')

networks = meraki.getnetworklist(apikey, orgid, suppressprint=True)
statuses = meraki.get_device_statuses(apikey,orgid,suppress_print=True)

for device in statuses:
    name = str(device.get('name'))
    status = str(device.get('status'))
    networkName = list(filter(lambda o : o.get('id') == device.get('networkId'),networks))[0].get('name')
    print('NETWORK: {:30} DEVICE: {:25} STATUS: {}'.format(networkName[:30],name[:25],status.upper()))