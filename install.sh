#!/bin/sh

APP_PATH='/usr/share/applications'
ICON_PATH='/usr/share/pixmaps'
SRC_PATH='/usr/share/landmark-tool'
BIN_PATH='/usr/bin'

mkdir -p ./pkg/$SRC_PATH

cp -f ./src/*.py $SRC_PATH/
mkdir $SRC_PATH/ui
cp -f ./src/ui/*.py $SRC_PATH/ui/

cp -f ./src/image/icon.png $ICON_PATH/landmark-tool.png
cp -f ./src/landmark-tool.desktop $APP_PATH/
ln -s $SRC_PATH/landmark.py $BIN_PATH/landmark-tool

echo "Done."
echo 'Execute \"landmark-tool\" and have fun'
