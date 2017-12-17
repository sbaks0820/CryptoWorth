#!/bin/bash
SCRIPT='worth.py'
SCRIPT=$PWD/$SCRIPT
chmod +x $SCRIPT
echo "alias worth='$SCRIPT'" >> ~/.bashrc
