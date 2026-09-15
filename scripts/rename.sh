#!/bin/bash

OLD_NAME="python-grpc-service-template"
NEW_NAME="$1"

PATTERN="s/$OLD_NAME/$NEW_NAME/g"

replace() {
    echo "Replacing $1"
    sed -i $PATTERN $1
}

replace "README.md"
replace "pyproject.toml"
replace "uv.lock"

SCRIPT=$(realpath "${BASH_SOURCE[0]}")
rm $SCRIPT
echo "Self destructed script."