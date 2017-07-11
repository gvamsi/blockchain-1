from sys import argv

script = argv
filename = "../network_setup.sh"
target = open(filename,'w')

target.write("#!/bin/bash\n")
target.write("#\n")
target.write("# Copyright IBM Corp. All Rights Reserved.\n")
target.write("#\n")
target.write("# SPDX-License-Identifier: Apache-2.0\n")
target.write("#\n\n")


target.write("UP_DOWN=\"$1\"\n")
target.write("CH_NAME=\"$2\"\n")
target.write("CLI_TIMEOUT=\"$3\"\n")
target.write("IF_COUCHDB=\"$4\"\n")

target.write(": ${CLI_TIMEOUT:=\"10000\"}\n\n")

target.write("COMPOSE_FILE=docker-compose-cli.yaml\n")
target.write("COMPOSE_FILE_COUCH=docker-compose-couch.yaml\n")
target.write("#COMPOSE_FILE=docker-compose-e2e.yaml\n\n")

target.write("function printHelp () {\n")
target.write("	echo \"Usage: ./network_setup <up|down> <\$channel-name> <\$cli_timeout> <couchdb>.The arguments must be in order.\"\n")
target.write("}\n\n")

target.write("function validateArgs () {\n")
target.write("	if [ -z \"${UP_DOWN}\" ]; then\n")
target.write("		echo \"Option up / down / restart not mentioned\"\n")
target.write("		printHelp\n")
target.write("		exit 1\n")
target.write("	fi\n")
target.write("	if [ -z \"${CH_NAME}\" ]; then\n")
target.write("		echo \"setting to default channel 'mychannel'\"\n")
target.write("		CH_NAME=mychannel\n")
target.write("	fi\n")
target.write("}\n\n")

target.write("function clearContainers () {\n")
target.write("        CONTAINER_IDS=$(docker ps -aq)\n")
target.write("        if [ -z \"$CONTAINER_IDS\" -o \"$CONTAINER_IDS\" = \" \" ]; then\n")
target.write("                echo \"---- No containers available for deletion ----\"\n")
target.write("        else\n")
target.write("                docker rm -f $CONTAINER_IDS\n")
target.write("        fi\n")
target.write("}\n")

target.write("function removeUnwantedImages() {\n")
target.write("        DOCKER_IMAGE_IDS=$(docker images | grep \"dev\|none\|test-vp\|peer[0-9]-\" | awk '{print $3}')\n")
target.write("        if [ -z \"$DOCKER_IMAGE_IDS\" -o \"$DOCKER_IMAGE_IDS\" = \" \" ]; then\n")
target.write("                echo \"---- No images available for deletion ----\"\n")
target.write("        else\n")
target.write("                docker rmi -f $DOCKER_IMAGE_IDS\n")
target.write("        fi\n")
target.write("}\n\n")

target.write("function networkUp () {\n")
target.write("    #Generate all the artifacts that includes org certs, orderer genesis block,\n")
target.write("    # channel configuration transaction\n")
target.write("    source generateArtifacts.sh $CH_NAME\n")

target.write("    if [ \"${IF_COUCHDB}\" == \"couchdb\" ]; then\n")
target.write("      CHANNEL_NAME=$CH_NAME TIMEOUT=$CLI_TIMEOUT docker-compose -f $COMPOSE_FILE -f $COMPOSE_FILE_COUCH up -d 2>&1\n")
target.write("    else\n")
target.write("      CHANNEL_NAME=$CH_NAME TIMEOUT=$CLI_TIMEOUT docker-compose -f $COMPOSE_FILE up -d 2>&1\n")
target.write("    fi\n")
target.write("    if [ $? -ne 0 ]; then\n")
target.write("	echo \"ERROR !!!! Unable to pull the images \"\n")
target.write("	exit 1\n")
target.write("    fi\n")
target.write("    docker logs -f cli\n")
target.write("}\n\n")

target.write("function networkDown () {\n")
target.write("    docker-compose -f $COMPOSE_FILE down\n\n")

target.write("    #Cleanup the chaincode containers\n")
target.write("    clearContainers\n\n")

target.write("    #Cleanup images\n")
target.write("    removeUnwantedImages\n\n")

target.write("    # remove orderer block and other channel configuration transactions and certs\n")
target.write("    rm -rf channel-artifacts/*.block channel-artifacts/*.tx crypto-config\n")
target.write("}\n\n")

target.write("validateArgs\n\n")

target.write("#Create the network using docker compose\n")
target.write("if [ \"${UP_DOWN}\" == \"up\" ]; then\n")
target.write("	networkUp\n")
target.write("elif [ \"${UP_DOWN}\" == \"down\" ]; then ## Clear the network\n")
target.write("	networkDown\n")
target.write("elif [ \"${UP_DOWN}\" == \"restart\" ]; then ## Restart the network\n")
target.write("	networkDown\n")
target.write("	networkUp\n")
target.write("else\n")
target.write("	printHelp\n")
target.write("	exit 1\n")
target.write("fi\n")