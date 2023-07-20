#!/bin/bash

# install requirements
sudo yum update -y
sudo yum install -y python3-devel
sudo yum install -y python3-pip
sudo yum install -y git

# install github cli
type -p yum-config-manager >/dev/null || sudo yum install yum-utils
sudo yum-config-manager --add-repo https://cli.github.com/packages/rpm/gh-cli.repo
sudo yum install gh# environment variables


