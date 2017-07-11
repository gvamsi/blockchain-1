from sys import argv

script,org1,org2,org3,peer0,peer1,peer2,peer3,peer4,peer5 = argv
filename = "../scripts/script.sh"
target = open(filename,'w')
target.write("#!/bin/bash\n\n")

target.write("echo\n")
target.write("echo \" ____    _____      _      ____    _____           _____   ____    _____ \"\n")
target.write("echo \"/ ___|  |_   _|    / \    |  _ \  |_   _|         | ____| |___ \  | ____|\"\n")
target.write("echo \"\___ \    | |     / _ \   | |_) |   | |    _____  |  _|     __) | |  _|  \"\n")
target.write("echo \" ___) |   | |    / ___ \  |  _ <    | |   |_____| | |___   / __/  | |___ \"\n")
target.write("echo \"|____/    |_|   /_/   \_\ |_| \_\   |_|           |_____| |_____| |_____|\"\n")
target.write("echo\n\n")

target.write("CHANNEL_NAME=\"$1\"\n")
target.write(": ${CHANNEL_NAME:=\"mychannel\"}\n")
target.write(": ${TIMEOUT:=\"60\"}\n")
target.write("COUNTER=1\n")
target.write("MAX_RETRY=5\n")
target.write("ORDERER_CA=/opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/ordererOrganizations/example.com/orderers/orderer.example.com/msp/cacerts/ca.example.com-cert.pem\n\n")

target.write("echo \"Channel name : \"$CHANNEL_NAME\n\n")

target.write("verifyResult () {\n")
target.write("	if [ $1 -ne 0 ] ; then\n")
target.write("		echo \"!!!!!!!!!!!!!!! \"$2\" !!!!!!!!!!!!!!!!\"\n")
target.write("                echo \"================== ERROR !!! FAILED to execute End-2-End Scenario ==================\"\n")
target.write("		echo\n")
target.write("   		exit 1\n")
target.write("	fi\n")
target.write("}\n\n")

target.write("setGlobals () {\n\n")

target.write("	if [ $1 -eq 0 -o $1 -eq 1 ] ; then\n")
target.write("		CORE_PEER_LOCALMSPID=\"")
str = org1 + "MSP\n"
target.write(str)
target.write("		CORE_PEER_TLS_ROOTCERT_FILE=/opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/")
str = org1 + ".example.com/peers/" + peer0 + "." + org1 + ".example.com/tls/ca.crt\n"
target.write(str)
target.write("		CORE_PEER_MSPCONFIGPATH=/opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/")
str = org1 + ".example.com/users/Admin@" + org1 + ".example.com/msp\n"
target.write(str)
target.write("		if [ $1 -eq 0 ]; then\n")
target.write("			CORE_PEER_ADDRESS=")
str = peer0 + "." + org1 + ".example.com:7051\n"
target.write(str)
target.write("		else\n")
target.write("			CORE_PEER_ADDRESS=")
str = peer1 + "." + org1 + ".example.com:7051\n"
target.write(str)
target.write("			CORE_PEER_MSPCONFIGPATH=/opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/")
str = org1 + ".example.com/users/Admin@" + org1 + ".example.com/msp\n"
target.write(str)
target.write("		fi\n\n")

target.write("	elif [ $1 -eq 2 -o $1 -eq 3 ] ; then\n")
target.write("		CORE_PEER_LOCALMSPID=")
str = org2 + "MSP\n"
target.write(str)
target.write("		CORE_PEER_TLS_ROOTCERT_FILE=/opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/")
str = org2 + ".example.com/peers/" + peer2 + "." + org2 + ".example.com/tls/ca.crt\n"
target.write(str)
target.write("		CORE_PEER_MSPCONFIGPATH=/opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/")
str = org2 + ".example.com/users/Admin@" + org2 + ".example.com/msp\n"
target.write(str)
target.write("		if [ $1 -eq 2 ]; then\n")
target.write("			CORE_PEER_ADDRESS=")
str = peer2 + "." + org2 + ".example.com:7051\n"
target.write(str)
target.write("		else\n")
target.write("			CORE_PEER_ADDRESS=")
str = peer3 + "." + org2 + ".example.com:7051\n"
target.write(str)
target.write("		fi\n\n")

target.write("	else\n")
target.write("		CORE_PEER_LOCALMSPID=")
str = org3 + "MSP\n"
target.write(str)
target.write("		CORE_PEER_TLS_ROOTCERT_FILE=/opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/")
str = org3 + ".example.com/peers/" + peer4 + "." + org3 + ".example.com/tls/ca.crt\n"
target.write(str)
target.write("		CORE_PEER_MSPCONFIGPATH=/opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/")
str = org3 + ".example.com/users/Admin@" + org3 + ".example.com/msp\n"
target.write(str)
target.write("		if [ $1 -eq 4 ]; then\n")
target.write("			CORE_PEER_ADDRESS=")
str = peer4 + "." + org3 + ".example.com:7051\n"
target.write(str)
target.write("		else\n")
target.write("			CORE_PEER_ADDRESS=")
str = peer5 + "." + org3 + ".example.com:7051\n"
target.write(str)
target.write("		fi\n")
target.write("	fi\n\n")

target.write("	env |grep CORE\n")
target.write("}\n\n")

target.write("createChannel() {\n")
target.write("	setGlobals 0\n\n")

target.write("        if [ -z \"$CORE_PEER_TLS_ENABLED\" -o \"$CORE_PEER_TLS_ENABLED\" = \"false\" ]; then\n")
target.write("		peer channel create -o orderer.example.com:7050 -c $CHANNEL_NAME -f ./channel-artifacts/channel.tx >&log.txt\n")
target.write("	else\n")
target.write("		peer channel create -o orderer.example.com:7050 -c $CHANNEL_NAME -f ./channel-artifacts/channel.tx --tls $CORE_PEER_TLS_ENABLED --cafile $ORDERER_CA >&log.txt\n")
target.write("	fi\n")
target.write("	res=$?\n")
target.write("	cat log.txt\n")
target.write("	verifyResult $res \"Channel creation failed\"\n")
target.write("	echo \"===================== Channel \\\"$CHANNEL_NAME\\\" is created successfully ===================== \"\n")
target.write("	echo\n")
target.write("}\n\n")

target.write("updateAnchorPeers() {\n")
target.write("        PEER=$1\n")
target.write("        setGlobals $PEER\n\n")

target.write("        if [ -z \"$CORE_PEER_TLS_ENABLED\" -o \"$CORE_PEER_TLS_ENABLED\" = \"false\" ]; then\n")
target.write("		peer channel update -o orderer.example.com:7050 -c $CHANNEL_NAME -f ./channel-artifacts/${CORE_PEER_LOCALMSPID}anchors.tx >&log.txt\n")
target.write("	else\n")
target.write("		peer channel update -o orderer.example.com:7050 -c $CHANNEL_NAME -f ./channel-artifacts/${CORE_PEER_LOCALMSPID}anchors.tx --tls $CORE_PEER_TLS_ENABLED --cafile $ORDERER_CA >&log.txt\n")
target.write("	fi\n")
target.write("	res=$?\n")
target.write("	cat log.txt\n")
target.write("	verifyResult $res \"Anchor peer update failed\"\n")
target.write("	echo \"===================== Anchor peers for org \\\"$CORE_PEER_LOCALMSPID\\\" on \\\"$CHANNEL_NAME\\\" is updated successfully ===================== \"\n")
target.write("	echo\n")
target.write("}\n\n")

target.write("## Sometimes Join takes time hence RETRY atleast for 5 times\n")
target.write("joinWithRetry () {\n")
target.write("	peer channel join -b $CHANNEL_NAME.block  >&log.txt\n")
target.write("	res=$?\n")
target.write("	cat log.txt\n")
target.write("	if [ $res -ne 0 -a $COUNTER -lt $MAX_RETRY ]; then\n")
target.write("		COUNTER=` expr $COUNTER + 1`\n")
target.write("		echo \"PEER$1 failed to join the channel, Retry after 2 seconds\"\n")
target.write("		sleep 2\n")
target.write("		joinWithRetry $1\n")
target.write("	else\n")
target.write("		COUNTER=1\n")
target.write("	fi\n")
target.write("        verifyResult $res \"After $MAX_RETRY attempts, PEER$ch has failed to Join the Channel\"\n")
target.write("}\n\n")

target.write("joinChannel () {\n")
target.write("	for ch in 0 1 2 3 4 5; do\n")
target.write("		setGlobals $ch\n")
target.write("		joinWithRetry $ch\n")
target.write("		echo \"===================== PEER$ch joined on the channel \\\"$CHANNEL_NAME\\\" ===================== \"\n")
target.write("		sleep 2\n")
target.write("		echo\n")
target.write("	done\n")
target.write("}\n\n")

target.write("installChaincode () {\n")
target.write("	PEER=$1\n")
target.write("	setGlobals $PEER\n")
target.write("	peer chaincode install -n mycc -v 1.0 -p github.com/hyperledger/fabric/examples/chaincode/go/chaincode_example02 >&log.txt\n")
target.write("	res=$?\n")
target.write("	cat log.txt\n")
target.write("        verifyResult $res \"Chaincode installation on remote peer PEER$PEER has Failed\"\n")
target.write("	echo \"===================== Chaincode is installed on remote peer PEER$PEER ===================== \"\n")
target.write("	echo\n")
target.write("}\n\n")

target.write("instantiateChaincode () {\n")
target.write("	PEER=$1\n")
target.write("	setGlobals $PEER\n")
target.write("	# while 'peer chaincode' command can get the orderer endpoint from the peer (if join was successful),\n")
target.write("	# lets supply it directly as we know it using the \"-o\" option\n")
target.write("	if [ -z \"$CORE_PEER_TLS_ENABLED\" -o \"$CORE_PEER_TLS_ENABLED\" = \"false\" ]; then\n")
target.write("		peer chaincode instantiate -o orderer.example.com:7050 -C $CHANNEL_NAME -n mycc -v 1.0 -c '{\"Args\":[\"init\",\"a\",\"100\",\"b\",\"200\"]}' -P \"OR	(")
str = "'" + org1 + "MSP.member','" + org2 + "MSP.member','" + org3 + "MSP.member')\" >&log.txt\n"
target.write(str)
target.write("	else\n")
target.write("		peer chaincode instantiate -o orderer.example.com:7050 --tls $CORE_PEER_TLS_ENABLED --cafile $ORDERER_CA -C $CHANNEL_NAME -n mycc -v 1.0 -c '{\"Args\":[\"init\",\"a\",\"100\",\"b\",\"200\"]}' -P \"OR	('")
str = org1 + "MSP.member','" + org2 + "MSP.member','" + org3 + "MSP.member')\" >&log.txt\n"
target.write(str)
target.write("	fi\n")
target.write("	res=$?\n")
target.write("	cat log.txt\n")
target.write("	verifyResult $res \"Chaincode instantiation on PEER$PEER on channel '$CHANNEL_NAME' failed\"\n")
target.write("	echo \"===================== Chaincode Instantiation on PEER$PEER on channel '$CHANNEL_NAME' is successful ===================== \"\n")
target.write("	echo\n")
target.write("}\n\n")

target.write("## Create channel\n")
target.write("echo \"Creating channel...\"\n")
target.write("createChannel\n\n")

target.write("## Join all the peers to the channel\n")
target.write("echo \"Having all peers join the channel...\"\n")
target.write("joinChannel\n\n")

target.write("## Set the anchor peers for each org in the channel\n")
target.write("echo \"Updating anchor peers for ")
str = org1 + "...\"\n"
target.write(str)
target.write("updateAnchorPeers 0\n")
target.write("echo \"Updating anchor peers for ")
str = org2 + "...\"\n"
target.write(str)
target.write("updateAnchorPeers 2\n")
target.write("echo \"Updating anchor peers for ")
str = org3 + "...\"\n"
target.write(str)
target.write("updateAnchorPeers 4\n\n")

target.write("## Install chaincode on Peer0/Org1 and Peer2/Org2 and Peer4/Org3\n")
target.write("echo \"Installing chaincode on ")
str = org1 + "/" + peer0 + "...\"\n"
target.write(str)
target.write("installChaincode 0\n")
target.write("echo \"Install chaincode on ")
str = org2 + "/" + peer2 + "...\"\n"
target.write(str)
target.write("installChaincode 2\n")
target.write("echo \"Install chaincode on ")
str = org3 + "/" + peer4 + "...\"\n"
target.write(str)
target.write("installChaincode 4\n\n")

target.write("#Instantiate chaincode on Peer0/Org1\n")
target.write("echo \"Instantiating chaincode on ")
str = org1 + "/" + peer0 + "...\"\n"
target.write(str)
target.write("instantiateChaincode 0\n\n")

target.write("#Instantiate chaincode on Peer2/Org2\n")
target.write("echo \"Instantiating chaincode on ")
str = org2 + "/" + peer2 + "...\"\n"
target.write(str)
target.write("instantiateChaincode 2\n\n")

target.write("## Install chaincode on Peer3/Org2\n")
target.write("echo \"Installing chaincode on ")
str = org2 + "/" + peer3 + "...\"\n"
target.write(str)
target.write("installChaincode 3\n\n")

target.write("## Install chaincode on Peer5/Org3\n")
target.write("echo \"Installing chaincode on ")
str = org3 + "/" + peer5 + "...\"\n"
target.write(str)
target.write("installChaincode 5\n\n")

target.write("echo\n")
target.write("echo \"===================== All GOOD, End-2-End execution completed ===================== \"\n")
target.write("echo\n\n")

target.write("echo\n")
target.write("echo \" _____   _   _   ____            _____   ____    _____ \"\n")
target.write("echo \"| ____| | \ | | |  _ \          | ____| |___ \  | ____|\"\n")
target.write("echo \"|  _|   |  \| | | | | |  _____  |  _|     __) | |  _|  \"\n")
target.write("echo \"| |___  | |\  | | |_| | |_____| | |___   / __/  | |___ \"\n")
target.write("echo \"|_____| |_| \_| |____/          |_____| |_____| |_____|\"\n")
target.write("echo\n\n")

target.write("exit 0\n")
