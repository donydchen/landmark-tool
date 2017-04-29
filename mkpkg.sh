#!/bin/sh

APP_PATH='usr/share/applications'
ICON_PATH='usr/share/pixmaps'
SRC_PATH='usr/share/landmark-tool'

rm -rf ./pkg/
rm -rf ./*.deb
mkdir -p ./pkg/$APP_PATH
mkdir -p ./pkg/$ICON_PATH
mkdir -p ./pkg/$SRC_PATH
cp -rf ./DEBIAN ./pkg/

cp -f ./src/*.py ./pkg/$SRC_PATH/
mkdir ./pkg/$SRC_PATH/ui
cp -f ./src/ui/*.py ./pkg/$SRC_PATH/ui/

cp -f ./src/image/icon.png ./pkg/$ICON_PATH/landmark-tool.png
cp -f ./src/landmark-tool.desktop ./pkg/$APP_PATH/

dpkg -b ./pkg landmark_tool_0.1.1_all.deb
