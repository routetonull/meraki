#!/usr/bin/python3.6

from meraki import meraki

apikey = "myAPIkey" # get API key from Meraki dashboard
orgs = meraki.myorgaccess(apikey, suppressprint=True)

company = "myCompany" # insert company name
c = list(filter(lambda o : o.get('name') == company,orgs))

if list:
  c = c[0]
  orgid = c.get('id')

#read all networks
networks = meraki.getnetworklist(apikey, orgid, suppressprint=True)

for net in networks:
  netID = net.get('id')
  netName = net.get('name')
  print ('*'*80)
  print('NETWORK NAME {:20} ID {}'.format(netName,netID))
  deviceList = meraki.getnetworkdevices(apikey, netID,suppressprint=True)
  for device in deviceList:
    if "MX" in device.get('model'):
      d='SECURITY POLICIES FOR DEVICE {} SERIAL {}'.format(device.get('model'), device.get('serial'))
      print ('*'*80)
      print(d)
      print ('*'*80)
      g = meraki.getmxl3fwrules(apikey, netID, suppressprint=True)
      print(g)