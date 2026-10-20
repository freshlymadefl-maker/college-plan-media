set -e
cd /home/claude/college-plan-media
O=instagram/2026-10-plan-now
r(){ python3 scripts/render_over_video.py $1 clips/stock/$2.mp4 $O/$1-silent.mp4 $3 0 .3 && python3 scripts/add_music.py $O/$1-silent.mp4 $O/$1.mp4 $4; }
r pn-9th-counts student-highlighting 10 sunny &
r pn-language student-stack-of-books 10 breeze &
r pn-they-need mixkit-8717-1080 10 bright &
r pn-dinner-qs mixkit-4874-1080 10.5 sunny &
(python3 templates/reel/render-fast.py "templates/reel/native-reel.html?cfg=pn-paid-hours" $O/pn-paid-hours-silent.mp4 10.5 30 && python3 scripts/add_music.py $O/pn-paid-hours-silent.mp4 $O/pn-paid-hours.mp4 breeze) &
wait; ls -la $O
