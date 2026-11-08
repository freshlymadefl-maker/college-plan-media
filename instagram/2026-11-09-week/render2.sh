cd /home/claude/college-plan-media
while pgrep -f "2026-11-09-week/render.sh" >/dev/null; do sleep 10; done
O=instagram/2026-11-09-week
cd templates/reel && python3 render-fast.py nine-counts-reel.html ../../$O/vo-nine-counts.mp4 33.5 24 ../../tts/out/nine-counts.mp3
echo VODONE
