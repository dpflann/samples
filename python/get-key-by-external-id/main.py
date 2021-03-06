# (c) 2018 Ionic Security Inc.
# By using this code, I agree to the Terms & Conditions (https://dev.ionic.com/use.html)
# and the Privacy Policy (https://www.ionic.com/privacy-notice/).

import os
import sys
import json
import ionicsdk
import binascii

external_ids = ['02e09520-e52c-42aa-b21c-a60698cf31a2']

# read persistor password from environment variable
persistorPassword = os.environ.get('IONIC_PERSISTOR_PASSWORD')
if (persistorPassword == None):
    print("[!] Please provide the persistor password as env variable: IONIC_PERSISTOR_PASSWORD")
    sys.exit(1)

# initialize agent with password persistor
try:
    persistorPath = os.path.expanduser("~/.ionicsecurity/profiles.pw")
    persistor = ionicsdk.DeviceProfilePersistorPasswordFile(persistorPath, persistorPassword)
    agent = ionicsdk.Agent(None, persistor)
except ionicsdk.exceptions.IonicException as e:
    print("Error initializing agent: {0}".format(e.message))
    sys.exit(-2)

# get key by external id
try:
    keys = agent.getkeys2([], externalkeyids=external_ids)[0]
except ionicsdk.exceptions.IonicException as e:
    print("Error fetching a key: {0}".format(e.message))
    sys.exit(-2)

# display fetched key
for key in keys:
    print("---")
    print("KeyId        : " + key.id)
    print("KeyBytes     : " + binascii.hexlify(key.bytes))
    print("FixedAttrs   : " + json.dumps(key.attributes))
    print("MutableAttrs : " + json.dumps(key.mutableAttributes))
