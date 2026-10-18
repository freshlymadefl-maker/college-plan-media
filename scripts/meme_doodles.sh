#!/bin/sh
# Overlay 2 doodles on a stock-meme video's white margins: meme_doodles.sh in.mp4 out.mp4
D=templates/doodles/png
ffmpeg -loglevel error -y -i "$1" -i $D/star-orange.png -i $D/squiggle-blue.png -filter_complex \
"[1:v]scale=96:-1,rotate=0.25:c=none:ow=rotw(0.25):oh=roth(0.25)[a];[2:v]scale=220:-1[b];[0:v][a]overlay=930:110[x];[x][b]overlay=80:1740,format=yuv420p" \
-c:v libx264 -crf 20 -an "$2"
