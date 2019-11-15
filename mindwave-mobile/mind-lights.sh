#!/bin/bash

DEVICES=$(cut -d '|' -f 1 <<< "$(magic-home discover | grep 192)")
echo "$DEVICES"

