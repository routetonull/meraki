# meraki

Meraki dashboard scripts and tests.

Details [HERE](https://www.ifconfig.it)

## deviceStatus.py

Get status (online/offline) of all devices.

Example of use:

    ./deviceStatus.py | sort | grep OFFLINE

## dumpfw.py

Get security policies of all MX devices. Useful for compliance testing.
Note: content filtering is not available with Meraki dashboard API yet. Make a wish.