from sys import argv

script,org1,org2,org3,peer0,peer1,peer2,peer3,peer4,peer5 = argv
filename = "../docker-compose-couch.yaml"
target = open(filename,'w')


target.write("#Copyright IBM Corp. All Rights Reserved.\n")
target.write("#\n")
target.write("# SPDX-License-Identifier: Apache-2.0\n")
target.write("#\n\n")

target.write("version: '2'\n\n")

target.write("services:\n")

target.write("  couchdb0:\n")
target.write("    container_name: couchdb0\n")
target.write("    image: hyperledger/fabric-couchdb\n")
target.write("    # Comment/Uncomment the port mapping if you want to hide/expose the CouchDB service,\n")
target.write("    # for example map it to utilize Fauxton User Interface in dev environments.\n")
target.write("    ports:\n")
target.write("      - \"5984:5984\"\n\n")

str = "  " + peer0 + "." + org1 + ".example.com\n"
target.write(str)
target.write("    environment:\n")
target.write("      - CORE_LEDGER_STATE_STATEDATABASE=CouchDB\n")
target.write("      - CORE_LEDGER_STATE_COUCHDBCONFIG_COUCHDBADDRESS=couchdb0:5984\n")
target.write("    depends_on:\n")
target.write("      - couchdb0\n\n")

target.write("  couchdb1:\n")
target.write("    container_name: couchdb1\n")
target.write("    image: hyperledger/fabric-couchdb\n")
target.write("    # Comment/Uncomment the port mapping if you want to hide/expose the CouchDB service,\n")
target.write("    # for example map it to utilize Fauxton User Interface in dev environments.\n")
target.write("    ports:\n")
target.write("      - \"6984:5984\"\n\n")

str = "  " + peer1 + "." + org1 + ".example.com:\n"
target.write(str)
target.write("    environment:\n")
target.write("      - CORE_LEDGER_STATE_STATEDATABASE=CouchDB\n")
target.write("      - CORE_LEDGER_STATE_COUCHDBCONFIG_COUCHDBADDRESS=couchdb1:5984\n")
target.write("    depends_on:\n")
target.write("      - couchdb1\n\n")

target.write("  couchdb2:\n")
target.write("    container_name: couchdb2\n")
target.write("    image: hyperledger/fabric-couchdb\n")
target.write("    # Comment/Uncomment the port mapping if you want to hide/expose the CouchDB service,\n")
target.write("    # for example map it to utilize Fauxton User Interface in dev environments.\n")
target.write("    ports:\n")
target.write("      - \"7984:5984\"\n\n")

str = "  " + peer2 + "." + org2 + ".example.com:\n"
target.write(str)
target.write("    environment:\n")
target.write("      - CORE_LEDGER_STATE_STATEDATABASE=CouchDB\n")
target.write("      - CORE_LEDGER_STATE_COUCHDBCONFIG_COUCHDBADDRESS=couchdb2:5984\n")
target.write("    depends_on:\n")
target.write("      - couchdb2\n\n")

target.write("  couchdb3:\n")
target.write("    container_name: couchdb3\n")
target.write("    image: hyperledger/fabric-couchdb\n")
target.write("    # Comment/Uncomment the port mapping if you want to hide/expose the CouchDB service,\n")
target.write("    # for example map it to utilize Fauxton User Interface in dev environments.\n")
target.write("    ports:\n")
target.write("      - \"8984:5984\"\n\n")

str = "  " + peer3 + "." + org2 + ".example.com:\n"
target.write(str)
target.write("    environment:\n")
target.write("      - CORE_LEDGER_STATE_STATEDATABASE=CouchDB\n")
target.write("      - CORE_LEDGER_STATE_COUCHDBCONFIG_COUCHDBADDRESS=couchdb3:5984\n")
target.write("    depends_on:\n")
target.write("      - couchdb3\n\n")


target.write("  couchdb4:\n")
target.write("    container_name: couchdb4\n")
target.write("    image: hyperledger/fabric-couchdb\n")
target.write("    # Comment/Uncomment the port mapping if you want to hide/expose the CouchDB service,\n")
target.write("    # for example map it to utilize Fauxton User Interface in dev environments.\n")
target.write("    ports:\n")
target.write("      - \"9984:5984\"\n\n")

str = "  " + peer4 + "." + org3 + ".example.com:\n"
target.write(str)
target.write("    environment:\n")
target.write("      - CORE_LEDGER_STATE_STATEDATABASE=CouchDB\n")
target.write("      - CORE_LEDGER_STATE_COUCHDBCONFIG_COUCHDBADDRESS=couchdb4:5984\n")
target.write("    depends_on:\n")
target.write("      - couchdb4\n\n")

target.write("  couchdb5:\n")
target.write("    container_name: couchdb5\n")
target.write("    image: hyperledger/fabric-couchdb\n")
target.write("    # Comment/Uncomment the port mapping if you want to hide/expose the CouchDB service,\n")
target.write("    # for example map it to utilize Fauxton User Interface in dev environments.\n")
target.write("    ports:\n")
target.write("      - \"10984:5984\"\n\n")

str = "  " + peer5 + "." + org3 + ".example.com:\n"
target.write(str)
target.write("    environment:\n")
target.write("      - CORE_LEDGER_STATE_STATEDATABASE=CouchDB\n")
target.write("      - CORE_LEDGER_STATE_COUCHDBCONFIG_COUCHDBADDRESS=couchdb5:5984\n")
target.write("    depends_on:\n")
target.write("      - couchdb5\n")

