from sys import argv

script,org1,org2,org3 = argv
filename = "../generateArtifacts.sh"
target = open(filename,'w')

target.write("#!/bin/bash +x\n")
target.write("#\n")
target.write("# Copyright IBM Corp. All Rights Reserved.\n")
target.write("#\n")
target.write("# SPDX-License-Identifier: Apache-2.0\n")
target.write("#\n\n\n")


target.write("#set -e\n\n")

target.write("CHANNEL_NAME=$1\n")
target.write(": ${CHANNEL_NAME:=\"mychannel\"}\n")
target.write("echo $CHANNEL_NAME\n\n")

target.write("export FABRIC_ROOT=$PWD/../..\n")
target.write("export FABRIC_CFG_PATH=$PWD\n")
target.write("echo\n\n")

target.write("OS_ARCH=$(echo \"$(uname -s|tr '[:upper:]' '[:lower:]'|sed 's/mingw64_nt.*/windows/')-$(uname -m | sed 's/x86_64/amd64/g')\" | awk '{print tolower($0)}')\n\n")

target.write("## Using docker-compose template replace private key file names with constants\n")
target.write("function replacePrivateKey () {\n")
target.write("	ARCH=`uname -s | grep Darwin`\n")
target.write("	if [ \"$ARCH\" == \"Darwin\" ]; then\n")
target.write("		OPTS=\"-it\"\n")
target.write("	else\n")
target.write("		OPTS=\"-i\"\n")
target.write("	fi\n\n")

target.write("	cp docker-compose-e2e-template.yaml docker-compose-e2e.yaml\n\n")

target.write("        CURRENT_DIR=$PWD\n")
target.write("        cd crypto-config/peerOrganizations/")
str = org1 + ".example.com/ca/\n"
target.write(str)
target.write("        PRIV_KEY=$(ls *_sk)\n")
target.write("        cd $CURRENT_DIR\n")
target.write("        sed $OPTS \"s/CA1_PRIVATE_KEY/${PRIV_KEY}/g\" docker-compose-e2e.yaml\n\n")

target.write("        cd crypto-config/peerOrganizations/")
str = org2 + ".example.com/ca/\n"
target.write(str)
target.write("        PRIV_KEY=$(ls *_sk)\n")
target.write("        cd $CURRENT_DIR\n")
target.write("        sed $OPTS \"s/CA2_PRIVATE_KEY/${PRIV_KEY}/g\" docker-compose-e2e.yaml\n\n")

target.write("        cd crypto-config/peerOrganizations/")
str = org3 + ".example.com/ca/\n"
target.write(str)
target.write("        PRIV_KEY=$(ls *_sk)\n")
target.write("        cd $CURRENT_DIR\n")
target.write("        sed $OPTS \"s/CA3_PRIVATE_KEY/${PRIV_KEY}/g\" docker-compose-e2e.yaml\n")
target.write("}\n\n")

target.write("## Generates Org certs using cryptogen tool\n")
target.write("function generateCerts (){\n")
target.write("	CRYPTOGEN=$FABRIC_ROOT/release/$OS_ARCH/bin/cryptogen\n\n")

target.write("	if [ -f \"$CRYPTOGEN\" ]; then\n")
target.write("            echo \"Using cryptogen -> $CRYPTOGEN\"\n")
target.write("	else\n")
target.write("	    echo \"Building cryptogen\"\n")
target.write("	    make -C $FABRIC_ROOT release\n")
target.write("	fi\n\n")

target.write("	echo\n")
target.write("	echo \"##########################################################\"\n")
target.write("	echo \"##### Generate certificates using cryptogen tool #########\"\n")
target.write("	echo \"##########################################################\"\n")
target.write("	$CRYPTOGEN generate --config=./crypto-config.yaml\n")
target.write("	echo\n")
target.write("}\n\n")

target.write("## Generate orderer genesis block , channel configuration transaction and anchor peer update transactions\n")
target.write("function generateChannelArtifacts() {\n\n")

target.write("	CONFIGTXGEN=$FABRIC_ROOT/release/$OS_ARCH/bin/configtxgen\n")
target.write("	if [ -f \"$CONFIGTXGEN\" ]; then\n")
target.write("            echo \"Using configtxgen -> $CONFIGTXGEN\"\n")
target.write("	else\n")
target.write("	    echo \"Building configtxgen\"\n")
target.write("	    make -C $FABRIC_ROOT release\n")
target.write("	fi\n\n")

target.write("	echo \"##########################################################\"\n")
target.write("	echo \"#########  Generating Orderer Genesis block ##############\"\n")
target.write("	echo \"##########################################################\"\n")
target.write("	# Note: For some unknown reason (at least for now) the block file can't be\n")
target.write("	# named orderer.genesis.block or the orderer will fail to launch!\n")
target.write("	$CONFIGTXGEN -profile OrgsOrdererGenesis -outputBlock ./channel-artifacts/genesis.block\n\n")

target.write("	echo\n")
target.write("	echo \"#################################################################\"\n")
target.write("	echo \"### Generating channel configuration transaction 'channel.tx' ###\"\n")
target.write("	echo \"#################################################################\"\n")
target.write("	$CONFIGTXGEN -profile OrgsChannel -outputCreateChannelTx ./channel-artifacts/channel.tx -channelID $CHANNEL_NAME\n\n")

target.write("	echo\n")
target.write("	echo \"#################################################################\"\n")
target.write("	echo \"#######    Generating anchor peer update for ")
str = org1 + "MSP   ##########\"\n"
target.write(str)
target.write("	echo \"#################################################################\"\n")
target.write("	$CONFIGTXGEN -profile OrgsChannel -outputAnchorPeersUpdate ./channel-artifacts/")
str = org1 + "MSPanchors.tx -channelID $CHANNEL_NAME -asOrg " + org1 + "MSP\n\n"
target.write(str)

target.write("	echo\n")
target.write("	echo \"#################################################################\"\n")
target.write("	echo \"#######    Generating anchor peer update for ")
str = org2 + "MSP   ##########\"\n"
target.write(str)
target.write("	echo \"#################################################################\"\n")
target.write("	$CONFIGTXGEN -profile OrgsChannel -outputAnchorPeersUpdate ./channel-artifacts/")
str = org2 + "MSPanchors.tx -channelID $CHANNEL_NAME -asOrg " + org2 + "MSP\n\n"
target.write(str)

target.write("	echo\n")
target.write("	echo \"#################################################################\"\n")
target.write("	echo \"#######    Generating anchor peer update for ")
str = org3 + "MSP   ##########\"\n"
target.write(str)
target.write("	echo \"#################################################################\"\n")
target.write("	$CONFIGTXGEN -profile OrgsChannel -outputAnchorPeersUpdate ./channel-artifacts/")
str = org3 + "MSPanchors.tx -channelID $CHANNEL_NAME -asOrg " + org3 + "MSP\n\n"
target.write(str)
target.write("	echo\n")
target.write("}\n\n")

target.write("generateCerts\n")
target.write("replacePrivateKey\n")
target.write("generateChannelArtifacts\n")
