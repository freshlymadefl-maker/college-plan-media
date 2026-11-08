set -e
cd /home/claude/college-plan-media
O=instagram/2026-11-09-week
v(){ python3 scripts/render_over_video.py $1 clips/stock/$2.mp4 $O/$1-silent.mp4 $3 ${4:-0} .3 && python3 scripts/add_music.py $O/$1-silent.mp4 $O/$1.mp4 $5; }
n(){ python3 templates/reel/render-fast.py "templates/reel/native-reel.html?cfg=$1" $O/$1-silent.mp4 $2 30 && python3 scripts/add_music.py $O/$1-silent.mp4 $O/$1.mp4 $3; }
m(){ python3 scripts/stock_meme.py $O/$1.json && sh scripts/meme_doodles.sh $O/$1-silent.mp4 $O/$1-dd.mp4 && python3 scripts/add_music.py $O/$1-dd.mp4 $O/$1.mp4 $2; }
v pn-exam-fees student-stack-of-books 9.5 0 sunny &
v pn-quit mixkit-8717-1080 9.5 0 breeze &
v pn-myth-bf students-walking-university 9.5 0 bright &
v pn-thanksgiving mixkit-4790-1080 9.5 0 sunny &
wait
v pn-course-requests girl-homework-library 9.5 0 breeze &
v pn-9th-vs-12th student-highlighting 9.5 2 bright &
v pn-try-again mixkit-40349-1080 8.5 0 sunny &
n due-nov9 9.5 breeze &
wait
n gc-decisions 10 bright &
n usf-stats 9.5 sunny &
n texting-fsu 10.5 breeze &
n thanksgiving-qs 9.5 bright &
wait
m meme-ucf-materials sunny &
m meme-weekend breeze &
python3 scripts/slideshow_video.py $O/ap-slideshow.mp4 2.4 instagram/2026-11-04-carousel-ap-ib-aice-de/ap{1,2,3,4,5,6,7,8}.png &
python3 scripts/slideshow_video.py $O/jm-slideshow.mp4 2.4 instagram/2026-11-07-scholarship-jose-marti/jm{1,2,3,4,5,6,7}.png &
wait
echo ALLDONE
