cd /home/claude/college-plan-media
while pgrep -f "2026-11-02-week/render.sh" >/dev/null; do sleep 10; done
O=instagram/2026-11-02-week
python3 scripts/slideshow_video.py $O/pasco-slideshow.mp4 2.4 instagram/2026-10-28-county-pasco/pa{1,2,3,4,5,6,7}.png &
python3 scripts/slideshow_video.py $O/equitable-slideshow.mp4 2.4 instagram/2026-10-31-scholarship-equitable/eq{1,2,3,4,5,6,7}.png &
wait
cd templates/reel && python3 render-fast.py gpa-3-numbers-reel.html ../../$O/vo-gpa.mp4 32.5 24 ../../tts/out/gpa-3-numbers.mp3
echo ALLDONE
