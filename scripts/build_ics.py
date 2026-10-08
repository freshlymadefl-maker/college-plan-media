"""calendar/events.json -> calendar/florida-college-deadlines.ics (all-day events, reminder the day before at 9am)."""
import json, hashlib, datetime, pathlib

ev = json.loads(pathlib.Path("calendar/events.json").read_text())
now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def esc(s):
    return s.replace("\\", "\\\\").replace(";", r"\;").replace(",", r"\,").replace("\n", r"\n")


def fold(line):
    parts = []
    while len(line.encode()) > 73:
        i = 73
        while len(line[:i].encode()) > 73:
            i -= 1
        parts.append(line[:i])
        line = " " + line[i:]
    parts.append(line)
    return "\r\n".join(parts)


L = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//College Plan//Florida College Deadlines//EN",
     "CALSCALE:GREGORIAN", "METHOD:PUBLISH",
     "X-WR-CALNAME:Florida College Deadlines (College Plan)", "X-WR-TIMEZONE:America/New_York",
     fold("X-WR-CALDESC:" + esc("Florida college deadlines for parents of 8th-12th graders. Always confirm on the official site. collegeplan.beehiiv.com")),
     "REFRESH-INTERVAL;VALUE=DURATION:PT12H", "X-PUBLISHED-TTL:PT12H"]
for e in sorted(ev, key=lambda x: x["date"]):
    d = datetime.date.fromisoformat(e["date"])
    d2 = d + datetime.timedelta(days=1)
    uid = hashlib.sha1((e["date"] + e["title"]).encode()).hexdigest()[:16] + "@collegeplan"
    desc = f"For: {e['who']}. " + (e["note"] + " " if e["note"] else "") + \
        f"Confirm here: {e['src']} | More Florida deadlines every week: collegeplan.beehiiv.com"
    L += ["BEGIN:VEVENT", f"UID:{uid}", f"DTSTAMP:{now}", f"DTSTART;VALUE=DATE:{d:%Y%m%d}",
          f"DTEND;VALUE=DATE:{d2:%Y%m%d}", fold("SUMMARY:" + esc(e["title"])), fold("DESCRIPTION:" + esc(desc)),
          fold("URL:" + e["src"]), "TRANSP:TRANSPARENT",
          "BEGIN:VALARM", "ACTION:DISPLAY", "TRIGGER:-PT15H", fold("DESCRIPTION:" + esc("Tomorrow: " + e["title"])),
          "END:VALARM", "END:VEVENT"]
L.append("END:VCALENDAR")
pathlib.Path("calendar/florida-college-deadlines.ics").write_text("\r\n".join(L) + "\r\n", newline="")
print(len(ev), "events")
