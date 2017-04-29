#!/bin/sh

INSTALL_PATH="/usr/share/landmark-tool"
BIN_PATH="/usr/bin"
ICON_PATH="/usr/share/pixmaps"
APP_PATH="/usr/share/applications"

rm -rf $INSTALL_PATH
rm -f $BIN_PATH/landmark-tool
rm -f $APP_PATH/landmark-tool.desktop
rm -f $ICON_PATH/landmark-tool.png

echo "Done."
