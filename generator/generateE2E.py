from sys import argv

script,org1,org2,org3,peer0,peer1,peer2,peer3,peer4,peer5 = argv
filename = "../docker-compose-e2e.yaml"
target = open(filename,'w')

target.write("# Copyright IBM Corp. All Rights Reserved.\n")
target.write("#\n")
target.write("# SPDX-License-Identifier: Apache-2.0\n")
target.write("#\n\n")

target.write("version: '2'\n\n")

target.write("services:\n")
target.write("  ca0:\n")
target.write("    image: hyperledger/fabric-ca\n")
target.write("    environment:\n")
target.write("      - FABRIC_CA_HOME=/etc/hyperledger/fabric-ca-server\n")
target.write("      - FABRIC_CA_SERVER_CA_NAME=ca-")
str = org1 + "\n"
target.write(str)
target.write("      - FABRIC_CA_SERVER_TLS_ENABLED=true\n")
target.write("      - FABRIC_CA_SERVER_TLS_CERTFILE=/etc/hyperledger/fabric-ca-server-config/ca.")
str = org1 + ".example.com-cert.pem\n"
target.write(str)
target.write("      - FABRIC_CA_SERVER_TLS_KEYFILE=/etc/hyperledger/fabric-ca-server-config/39edd0710e9c0cbc443141e1aac083f42b79b9c07c2a78ee8350df271780f6be_sk\n")
target.write("    ports:\n")
target.write("      - \"7054:7054\"\n")
target.write("    command: sh -c 'fabric-ca-server start --ca.certfile /etc/hyperledger/fabric-ca-server-config/ca.")
str= org1 + ".example.com-cert.pem --ca.keyfile /etc/hyperledger/fabric-ca-server-config/39edd0710e9c0cbc443141e1aac083f42b79b9c07c2a78ee8350df271780f6be_sk -b admin:adminpw -d'\n"
target.write(str)
target.write("    volumes:\n")
target.write("      - ./crypto-config/peerOrganizations/")
str = org1 + ".example.com/ca/:/etc/hyperledger/fabric-ca-server-config\n"
target.write(str)
target.write("    container_name: ca_peer")
target.write(org1)
target.write("\n\n")

target.write("  ca1:\n")
target.write("    image: hyperledger/fabric-ca\n")
target.write("    environment:\n")
target.write("      - FABRIC_CA_HOME=/etc/hyperledger/fabric-ca-server\n")
target.write("      - FABRIC_CA_SERVER_CA_NAME=ca-")
str = org2 + "\n"
target.write(str)
target.write("      - FABRIC_CA_SERVER_TLS_ENABLED=true\n")
target.write("      - FABRIC_CA_SERVER_TLS_CERTFILE=/etc/hyperledger/fabric-ca-server-config/ca.")
str = org2 + ".example.com-cert.pem\n"
target.write(str)
target.write("      - FABRIC_CA_SERVER_TLS_KEYFILE=/etc/hyperledger/fabric-ca-server-config/a804ca278aaee68b22b9c0f78018e681e3e8170ccdeb6c4cbdf3ed91657481c5_sk\n")
target.write("    ports:\n")
target.write("      - \"8054:7054\"\n")
target.write("    command: sh -c 'fabric-ca-server start --ca.certfile /etc/hyperledger/fabric-ca-server-config/ca.")
str = org2 + ".example.com-cert.pem --ca.keyfile /etc/hyperledger/fabric-ca-server-config/a804ca278aaee68b22b9c0f78018e681e3e8170ccdeb6c4cbdf3ed91657481c5_sk -b admin:adminpw -d'\n"
target.write(str)
target.write("    volumes:\n")
target.write("      - ./crypto-config/peerOrganizations/")
str = org2 + ".example.com/ca/:/etc/hyperledger/fabric-ca-server-config\n"
target.write(str)
target.write("    container_name: ca_peer")
target.write(org2)
target.write("\n\n")


target.write("  ca2:\n")
target.write("    image: hyperledger/fabric-ca\n")
target.write("    environment:\n")
target.write("      - FABRIC_CA_HOME=/etc/hyperledger/fabric-ca-server\n")
target.write("      - FABRIC_CA_SERVER_CA_NAME=ca-")
str = org3 + "\n"
target.write(str)
target.write("      - FABRIC_CA_SERVER_TLS_ENABLED=true\n")
target.write("      - FABRIC_CA_SERVER_TLS_CERTFILE=/etc/hyperledger/fabric-ca-server-config/ca.org3.example.com-cert.pem\n")
target.write("      - FABRIC_CA_SERVER_TLS_KEYFILE=/etc/hyperledger/fabric-ca-server-config/5728a1c1684230cd5b8909a62dc75b89e3a384635f588aa45a53758a8825723e_sk\n")
target.write("    ports:\n")
target.write("      - \"9054:7054\"\n")
target.write("    command: sh -c 'fabric-ca-server start --ca.certfile /etc/hyperledger/fabric-ca-server-config/ca.")
str = org3 + ".example.com-cert.pem --ca.keyfile /etc/hyperledger/fabric-ca-server-config/5728a1c1684230cd5b8909a62dc75b89e3a384635f588aa45a53758a8825723e_sk -b admin:adminpw -d'\n"
target.write(str)
target.write("    volumes:\n")
target.write("      - ./crypto-config/peerOrganizations/")
str = org3 + ".example.com/ca/:/etc/hyperledger/fabric-ca-server-config\n"
target.write(str)
target.write("    container_name: ca_peer")
target.write(org3)
target.write("\n\n")


target.write("  orderer.example.com:\n")
target.write("    extends:\n")
target.write("      file:   base/docker-compose-base.yaml\n")
target.write("      service: orderer.example.com\n")
target.write("    container_name: orderer.example.com\n\n")

str = "  " + peer0 + "." + org1 + ".example.com\n"
target.write(str)
target.write("    container_name: ")
str = peer0 + "." + org1 + ".example.com\n"
target.write(str)
target.write("    extends:\n")
target.write("      file:  base/docker-compose-base.yaml\n")
target.write("      service: ")
str = "  " + peer0 + "." + org1 + ".example.com\n"
target.write(str)
target.write("\n")

str = "  " + peer1 + "." + org1 + ".example.com\n"
target.write(str)
target.write("    container_name: ")
str = peer1 + "." + org1 + ".example.com\n"
target.write(str)
target.write("    extends:\n")
target.write("      file:  base/docker-compose-base.yaml\n")
target.write("      service: ")
str = "  " + peer1 + "." + org1 + ".example.com\n"
target.write(str)
target.write("\n")

str = "  " + peer2 + "." + org2 + ".example.com\n"
target.write(str)
target.write("    container_name: ")
str = peer2 + "." + org2 + ".example.com\n"
target.write(str)
target.write("    extends:\n")
target.write("      file:  base/docker-compose-base.yaml\n")
target.write("      service: ")
str = "  " + peer2 + "." + org2 + ".example.com\n"
target.write(str)
target.write("\n")

str = "  " + peer3 + "." + org2 + ".example.com\n"
target.write(str)
target.write("    container_name: ")
str = peer3 + "." + org2 + ".example.com\n"
target.write(str)
target.write("    extends:\n")
target.write("      file:  base/docker-compose-base.yaml\n")
target.write("      service: ")
str = "  " + peer3 + "." + org2 + ".example.com\n"
target.write(str)
target.write("\n")

str = "  " + peer4 + "." + org3 + ".example.com\n"
target.write(str)
target.write("    container_name: ")
str = peer4 + "." + org3 + ".example.com\n"
target.write(str)
target.write("    extends:\n")
target.write("      file:  base/docker-compose-base.yaml\n")
target.write("      service: ")
str = "  " + peer4 + "." + org3 + ".example.com\n"
target.write(str)
target.write("\n")

str = "  " + peer5 + "." + org3 + ".example.com\n"
target.write(str)
target.write("    container_name: ")
str = peer5 + "." + org3 + ".example.com\n"
target.write(str)
target.write("    extends:\n")
target.write("      file:  base/docker-compose-base.yaml\n")
target.write("      service: ")
str = "  " + peer5 + "." + org3 + ".example.com\n"
target.write(str)
target.write("\n")