from sys import argv

script,org1,org2,org3,peer0,peer1,peer2,peer3,peer4,peer5 = argv
filename = "../base/docker-compose-base.yaml"
target = open(filename,'w')
target.write("# Copyright IBM Corp. All Rights Reserved.\n")
target.write("#\n")
target.write("# SPDX-License-Identifier: Apache-2.0\n")
target.write("#\n\n")

target.write("version: '2'\n\n")

target.write("services:\n\n")

target.write("  orderer.example.com:\n")
target.write("    container_name: orderer.example.com\n")
target.write("    image: hyperledger/fabric-orderer\n")
target.write("    environment:\n")
target.write("      - ORDERER_GENERAL_LOGLEVEL=debug\n")
target.write("      - ORDERER_GENERAL_LISTENADDRESS=0.0.0.0\n")
target.write("      - ORDERER_GENERAL_GENESISMETHOD=file\n")
target.write("      - ORDERER_GENERAL_GENESISFILE=/var/hyperledger/orderer/orderer.genesis.block\n")
target.write("      - ORDERER_GENERAL_LOCALMSPID=OrdererMSP\n")
target.write("      - ORDERER_GENERAL_LOCALMSPDIR=/var/hyperledger/orderer/msp\n")
target.write("      # enabled TLS\n")
target.write("      - ORDERER_GENERAL_TLS_ENABLED=true\n")
target.write("      - ORDERER_GENERAL_TLS_PRIVATEKEY=/var/hyperledger/orderer/tls/server.key\n")
target.write("      - ORDERER_GENERAL_TLS_CERTIFICATE=/var/hyperledger/orderer/tls/server.crt\n")
target.write("      - ORDERER_GENERAL_TLS_ROOTCAS=[/var/hyperledger/orderer/tls/ca.crt]\n")
target.write("    working_dir: /opt/gopath/src/github.com/hyperledger/fabric\n")
target.write("    command: orderer\n")
target.write("    volumes:\n")
target.write("    - ../channel-artifacts/genesis.block:/var/hyperledger/orderer/orderer.genesis.block\n")
target.write("    - ../crypto-config/ordererOrganizations/example.com/orderers/orderer.example.com/msp:/var/hyperledger/orderer/msp\n")
target.write("    - ../crypto-config/ordererOrganizations/example.com/orderers/orderer.example.com/tls/:/var/hyperledger/orderer/tls\n")
target.write("    ports:\n")
target.write("      - 7050:7050\n\n")

str = "  " + peer0 + "." + org1 + ".example.com:\n"
target.write(str)
target.write("    container_name:")
str = " " + peer0 + "." + org1 + ".example.com\n"
target.write(str)
target.write("    extends:\n")
target.write("      file: peer-base.yaml\n")
target.write("      service: peer-base\n")
target.write("    environment:\n")
target.write("      - CORE_PEER_ID=")
str = peer0 + "." + org1 + ".example.com\n"
target.write(str)
target.write("      - CORE_PEER_ADDRESS=")
str = peer0 + "." + org1 + ".example.com:7051\n"
target.write(str)
target.write("      - CORE_PEER_GOSSIP_EXTERNALENDPOINT=")
str = peer0 + "." + org1 + ".example.com:7051\n"
target.write(str)
target.write("      - CORE_PEER_LOCALMSPID=")
str = org1 + "MSP\n"
target.write(str)
target.write("    volumes:\n")
target.write("        - /var/run/:/host/var/run/\n")
str = "        - ../crypto-config/peerOrganizations/" + org1 + ".example.com/peers/" + peer0 + "." +org1 + ".example.com/msp:/etc/hyperledger/fabric/msp\n"
target.write(str)
str = "        - ../crypto-config/peerOrganizations/" + org1 + ".example.com/peers/" + peer0 + "." +org1 + ".example.com/tls:/etc/hyperledger/fabric/tls\n"
target.write(str)
target.write("    ports:\n")
target.write("      - 7051:7051\n")
target.write("      - 7053:7053\n\n")

str = "  " + peer1 + "." + org1 + ".example.com:\n"
target.write(str)
target.write("    container_name:")
str = " " + peer1 + "." + org1 + ".example.com\n"
target.write(str)
target.write("    extends:\n")
target.write("      file: peer-base.yaml\n")
target.write("      service: peer-base\n")
target.write("    environment:\n")
target.write("      - CORE_PEER_ID=")
str = peer1 + "." + org1 + ".example.com\n"
target.write(str)
target.write("      - CORE_PEER_ADDRESS=")
str = peer1 + "." + org1 + ".example.com:7051\n"
target.write(str)
target.write("      - CORE_PEER_GOSSIP_EXTERNALENDPOINT=")
str = peer1 + "." + org1 + ".example.com:7051\n"
target.write(str)
target.write("      - CORE_PEER_GOSSIP_BOOTSTRAP=")
str = peer0 + "." + org1 + ".example.com:7051\n"
target.write(str)
target.write("      - CORE_PEER_LOCALMSPID=")
str = org1 + "MSP\n"
target.write(str)
target.write("    volumes:\n")
target.write("        - /var/run/:/host/var/run/\n")
str = "        - ../crypto-config/peerOrganizations/" + org1 + ".example.com/peers/" + peer1 + "." +org1 + ".example.com/msp:/etc/hyperledger/fabric/msp\n"
target.write(str)
str = "        - ../crypto-config/peerOrganizations/" + org1 + ".example.com/peers/" + peer1 + "." +org1 + ".example.com/tls:/etc/hyperledger/fabric/tls\n"
target.write(str)
target.write("    ports:\n")
target.write("      - 8051:7051\n")
target.write("      - 8053:7053\n\n")

str = "  " + peer2 + "." + org2 + ".example.com:\n"
target.write(str)
target.write("    container_name:")
str = " " + peer2 + "." + org2 + ".example.com\n"
target.write(str)
target.write("    extends:\n")
target.write("      file: peer-base.yaml\n")
target.write("      service: peer-base\n")
target.write("    environment:\n")
target.write("      - CORE_PEER_ID=")
str = peer2 + "." + org2 + ".example.com\n"
target.write(str)
target.write("      - CORE_PEER_ADDRESS=")
str = peer2 + "." + org2 + ".example.com:7051\n"
target.write(str)
target.write("      - CORE_PEER_GOSSIP_EXTERNALENDPOINT=")
str = peer2 + "." + org2 + ".example.com:7051\n"
target.write(str)
target.write("      - CORE_PEER_GOSSIP_BOOTSTRAP=")
str = peer2 + "." + org2 + ".example.com:7051\n"
target.write(str)
target.write("      - CORE_PEER_LOCALMSPID=")
str = org2 + "MSP\n"
target.write(str)
target.write("    volumes:\n")
target.write("        - /var/run/:/host/var/run/\n")
str = "        - ../crypto-config/peerOrganizations/" + org2 + ".example.com/peers/" + peer2 + "." +org2 + ".example.com/msp:/etc/hyperledger/fabric/msp\n"
target.write(str)
str = "        - ../crypto-config/peerOrganizations/" + org2 + ".example.com/peers/" + peer2 + "." +org2 + ".example.com/tls:/etc/hyperledger/fabric/tls\n"
target.write(str)
target.write("    ports:\n")
target.write("      - 9051:7051\n")
target.write("      - 9053:7053\n\n")

str = "  " + peer3 + "." + org2 + ".example.com:\n"
target.write(str)
target.write("    container_name:")
str = " " + peer3 + "." + org2 + ".example.com\n"
target.write(str)
target.write("    extends:\n")
target.write("      file: peer-base.yaml\n")
target.write("      service: peer-base\n")
target.write("    environment:\n")
target.write("      - CORE_PEER_ID=")
str = peer3 + "." + org2 + ".example.com\n"
target.write(str)
target.write("      - CORE_PEER_ADDRESS=")
str = peer3 + "." + org2 + ".example.com:7051\n"
target.write(str)
target.write("      - CORE_PEER_GOSSIP_EXTERNALENDPOINT=")
str = peer3 + "." + org2 + ".example.com:7051\n"
target.write(str)
target.write("      - CORE_PEER_GOSSIP_BOOTSTRAP=")
str = peer3 + "." + org2 + ".example.com:7051\n"
target.write(str)
target.write("      - CORE_PEER_LOCALMSPID=")
str = org2 + "MSP\n"
target.write(str)
target.write("    volumes:\n")
target.write("        - /var/run/:/host/var/run/\n")
str = "        - ../crypto-config/peerOrganizations/" + org2 + ".example.com/peers/" + peer3 + "." +org2 + ".example.com/msp:/etc/hyperledger/fabric/msp\n"
target.write(str)
str = "        - ../crypto-config/peerOrganizations/" + org2 + ".example.com/peers/" + peer3 + "." +org2 + ".example.com/tls:/etc/hyperledger/fabric/tls\n"
target.write(str)
target.write("    ports:\n")
target.write("      - 10051:7051\n")
target.write("      - 10053:7053\n\n")

str = "  " + peer4 + "." + org3 + ".example.com:\n"
target.write(str)
target.write("    container_name:")
str = " " + peer4 + "." + org3 + ".example.com\n"
target.write(str)
target.write("    extends:\n")
target.write("      file: peer-base.yaml\n")
target.write("      service: peer-base\n")
target.write("    environment:\n")
target.write("      - CORE_PEER_ID=")
str = peer4 + "." + org3 + ".example.com\n"
target.write(str)
target.write("      - CORE_PEER_ADDRESS=")
str = peer4 + "." + org3 + ".example.com:7051\n"
target.write(str)
target.write("      - CORE_PEER_GOSSIP_EXTERNALENDPOINT=")
str = peer4 + "." + org3 + ".example.com:7051\n"
target.write(str)
target.write("      - CORE_PEER_GOSSIP_BOOTSTRAP=")
str = peer4 + "." + org3 + ".example.com:7051\n"
target.write(str)
target.write("      - CORE_PEER_LOCALMSPID=")
str = org3 + "MSP\n"
target.write(str)
target.write("    volumes:\n")
target.write("        - /var/run/:/host/var/run/\n")
str = "        - ../crypto-config/peerOrganizations/" + org3 + ".example.com/peers/" + peer4 + "." +org3 + ".example.com/msp:/etc/hyperledger/fabric/msp\n"
target.write(str)
str = "        - ../crypto-config/peerOrganizations/" + org3 + ".example.com/peers/" + peer4 + "." +org3 + ".example.com/tls:/etc/hyperledger/fabric/tls\n"
target.write(str)
target.write("    ports:\n")
target.write("      - 11051:7051\n")
target.write("      - 11053:7053\n\n")

str = "  " + peer5 + "." + org3 + ".example.com:\n"
target.write(str)
target.write("    container_name:")
str = " " + peer5 + "." + org3 + ".example.com\n"
target.write(str)
target.write("    extends:\n")
target.write("      file: peer-base.yaml\n")
target.write("      service: peer-base\n")
target.write("    environment:\n")
target.write("      - CORE_PEER_ID=")
str = peer5 + "." + org3 + ".example.com\n"
target.write(str)
target.write("      - CORE_PEER_ADDRESS=")
str = peer5 + "." + org3 + ".example.com:7051\n"
target.write(str)
target.write("      - CORE_PEER_GOSSIP_EXTERNALENDPOINT=")
str = peer5 + "." + org3 + ".example.com:7051\n"
target.write(str)
target.write("      - CORE_PEER_GOSSIP_BOOTSTRAP=")
str = peer5 + "." + org3 + ".example.com:7051\n"
target.write(str)
target.write("      - CORE_PEER_LOCALMSPID=")
str = org3 + "MSP\n"
target.write(str)
target.write("    volumes:\n")
target.write("        - /var/run/:/host/var/run/\n")
str = "        - ../crypto-config/peerOrganizations/" + org3 + ".example.com/peers/" + peer5 + "." +org3 + ".example.com/msp:/etc/hyperledger/fabric/msp\n"
target.write(str)
str = "        - ../crypto-config/peerOrganizations/" + org3 + ".example.com/peers/" + peer5 + "." +org3 + ".example.com/tls:/etc/hyperledger/fabric/tls\n"
target.write(str)
target.write("    ports:\n")
target.write("      - 12051:7051\n")
target.write("      - 12053:7053\n\n") 