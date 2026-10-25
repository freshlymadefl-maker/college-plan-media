set -e
cd /home/claude/college-plan-media
O=instagram/2026-10-26-week
v(){ python3 scripts/render_over_video.py $1 clips/stock/$2.mp4 $O/$1-silent.mp4 $3 ${4:-0} .3 && python3 scripts/add_music.py $O/$1-silent.mp4 $O/$1.mp4 $5; }
n(){ python3 templates/reel/render-fast.py "templates/reel/native-reel.html?cfg=$1" $O/$1-silent.mp4 $2 30 && python3 scripts/add_music.py $O/$1-silent.mp4 $O/$1.mp4 $3; }
m(){ python3 scripts/stock_meme.py $O/$1.json && sh scripts/meme_doodles.sh $O/$1-silent.mp4 $O/$1-dd.mp4 && python3 scripts/add_music.py $O/$1-dd.mp4 $O/$1.mp4 $2; }
v pn-brag-folder frustrated-woman-account 10 0 sunny &
v pn-psat girl-homework-library 10 0 breeze &
v pn-blink students-walking-university 10 0 bright &
v pn-paths student-highlighting 10 2 sunny &
wait
v pn-scary student-stack-of-books 10 0 breeze &
v pn-uplift mixkit-4874-1080 8.5 6 bright &
n due-oct26 9.5 sunny &
n stress-meter 10 breeze &
wait
n fsu-stats 9.5 bright &
n pn-gold-seal 10.5 sunny &
n this-or-that 10 breeze &
n halloween-ea 10.5 bright &
wait
n bf-fake-award 10 sunny &
m meme-fafsa breeze &
m meme-extra-hour bright &
wait
ls -la $O
