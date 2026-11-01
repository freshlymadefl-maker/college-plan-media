set -e
cd /home/claude/college-plan-media
O=instagram/2026-11-02-week
v(){ python3 scripts/render_over_video.py $1 clips/stock/$2.mp4 $O/$1-silent.mp4 $3 ${4:-0} .3 && python3 scripts/add_music.py $O/$1-silent.mp4 $O/$1.mp4 $5; }
n(){ python3 templates/reel/render-fast.py "templates/reel/native-reel.html?cfg=$1" $O/$1-silent.mp4 $2 30 && python3 scripts/add_music.py $O/$1-silent.mp4 $O/$1.mp4 $3; }
m(){ python3 scripts/stock_meme.py $O/$1.json && sh scripts/meme_doodles.sh $O/$1-silent.mp4 $O/$1-dd.mp4 && python3 scripts/add_music.py $O/$1-dd.mp4 $O/$1.mp4 $2; }
v pn-3-people girl-homework-library 10 0 sunny &
v pn-summer students-walking-university 10 0 breeze &
v pn-drive mixkit-8717-1080 9.5 0 bright &
v pn-career student-highlighting 10 2 sunny &
wait
v pn-secret-prep mixkit-4790-1080 10 0 breeze &
v pn-on-time mixkit-40349-1080 8.5 0 bright &
n due-nov2 9.5 sunny &
n gc-november 10 breeze &
wait
n ucf-stats 9.5 bright &
n texting-sat 10.5 sunny &
n trial-county 9 breeze &
n pn-report-card 10.5 bright &
wait
m meme-submit-done sunny &
m meme-after-sat breeze &
wait
ls -la $O
