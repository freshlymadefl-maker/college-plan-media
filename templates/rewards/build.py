# Builds the referral reward PDFs' HTML. Run from templates/rewards, then render with page.pdf (Letter, print_background).
css = open('../cheatsheet.html').read().split('<style>')[1].split('</style>')[0]
extra = """
.cols { display:grid; grid-template-columns:1fr 1fr; gap:14px; }
.box { border:1px solid var(--line); border-radius:10px; padding:10px 13px; }
.box h3 { font-family:'Poppins'; font-weight:600; font-size:11pt; color:var(--navy); margin:0 0 4px; }
.box ul, .chk { margin:0; padding:0; list-style:none; }
.chk li, .box li { position:relative; padding-left:20px; margin:5px 0; font-size:10.3pt; }
.chk li:before, .box li:before { content:""; position:absolute; left:0; top:2px; width:11px; height:11px; border:1.5px solid #8FA7C0; border-radius:3px; }
.box.q li:before { border-radius:50%; width:6px; height:6px; top:6px; left:3px; background:var(--blue); border:none; }
.grade { display:grid; grid-template-columns:1.05in 1fr; gap:14px; padding:8px 0; border-bottom:1px dashed var(--line); }
.grade:last-child { border-bottom:none; }
table.trk td, table.trk th { height:30px; font-size:8.6pt; padding:5px 6px; }
table.trk tbody td { border-right:1px solid var(--line); }
table.trk thead th { font-size:8.3pt; }
table.trk.apps td { height:36px; }
table.trk.apps th:first-child { width:17%; }
.lines { border-bottom:1px solid var(--line); height:24px; }
"""

def doc(title, body):
    return f'<!doctype html><html><head><meta charset="utf-8"><title>{title}</title><style>{css}{extra}</style></head><body>{body}</body></html>'

def top(tag):
    return f'<div class="top"><img src="../wordmark_navy.png" alt="College Plan"><div class="tag">{tag}</div></div>'

FOOT = '<div class="foot"><span>A thank-you from <b>College Plan</b> for sharing us with another Florida family.</span><span><b>collegeplan.beehiiv.com</b></span></div>'

def foot(text):
    return f'<div class="foot"><span>{text}</span><span><b>collegeplan.beehiiv.com</b></span></div>'

def g(when, sub, items):
    lis = ''.join(f'<li>{i}</li>' for i in items)
    return f'<div class="grade"><div class="when">{when}<span>{sub}</span></div><ul class="chk">{lis}</ul></div>'

def qbox(h, items):
    lis = ''.join(f'<li>{i}</li>' for i in items)
    return f'<div class="box q"><h3>{h}</h3><ul>{lis}</ul></div>'

def chk(items):
    return '<ul class="chk">' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'

# 1) Grade-by-grade checklist (1 referral)
p1 = f"""<div class="page">{top('Referral reward · Florida parents')}
<h1>The 8th–12th Grade <em>College Planning Checklist</em></h1>
<p class="sub">Check things off one year at a time, so senior year isn’t a scramble. Built for Florida families.</p>
{g('8th grade', 'and the summer after', [
 'Ask which middle school courses earn high school credit (like Algebra 1 or a world language)',
 'Plan a 9th-grade schedule with the right level of challenge for your student',
 'Start a service-hour log: Bright Futures hours count during high school (ask your district whether the summer before 9th grade counts)',
 'Make one folder (paper or digital) for awards, report cards and certificates'])}
{g('9th grade', 'grades start to count', [
 'Know that core-course grades count toward the Bright Futures GPA from day one',
 'Find out your school’s service-hour form and turn hours in every year',
 'Plan for two years of the same world language before graduation',
 'Try a club, job, or activity your student actually enjoys',
 'Save copies of report cards and awards in the folder'])}
{g('10th grade', 'explore', [
 'Take the PSAT 10 or another practice test if your school offers it',
 'Ask the counselor about dual enrollment, AP, IB or AICE options and eligibility',
 'Plan a summer that builds something: a job, volunteering, a program or a project',
 'Keep logging and turning in service hours'])}
{foot('Requirements change. Confirm with your school counselor and official sources.')}</div>
<div class="page">{top('The 8th–12th Grade College Planning Checklist')}
<div style="height:14px"></div>
{g('11th grade', 'the big year', [
 'Take the PSAT/NMSQT in October (the National Merit qualifier)',
 'Take the SAT, ACT or CLT in winter or spring, and leave room to retest',
 'Ask the counselor for a Bright Futures evaluation to see where your student stands',
 'Build a first college list: reach, target and likely schools',
 'Visit a few campuses (see our Campus Visit Kit)',
 'In spring, ask two teachers for recommendation letters for senior year',
 'Over the summer, brainstorm and draft the main essay'])}
{g('12th grade', 'apply + pay for it', [
 'Write down every school’s deadlines and requirements (see our Senior Application Tracker)',
 'Complete self-reported academic records where required (like UF’s STARS or the SSAR)',
 'Submit the FAFSA as soon as you can once it opens',
 'Submit the Florida Financial Aid Application (FFAA): it’s how students apply for Bright Futures',
 'Apply for scholarships every month, not just in spring',
 'Compare financial aid offers side by side before choosing',
 'Finish service hours and requirements before graduation. The FFAA final deadline is Aug 31 after graduation'])}
<div class="callout"><b>Tip:</b> Put one 20-minute “college check-in” on the family calendar each month. Small steps beat a senior-year pile-up.</div>
{FOOT}</div>"""
open('checklist.html', 'w').write(doc('College Planning Checklist', p1))

# 2) Campus visit kit (3 referrals)
crit = ['Academics / majors', 'Class size', 'Campus feel', 'Housing', 'Food', 'Clubs &amp; activities', 'Safety',
        'Distance from home', 'Estimated cost after aid', 'Gut feeling (1–5)']
rows = ''.join(f'<tr><th>{c}</th><td></td><td></td><td></td></tr>' for c in crit)
lines = ''.join('<div class="lines"></div>' for _ in range(7))
p2 = f"""<div class="page">{top('Referral reward · Florida parents')}
<h1>The <em>Campus Visit</em> Kit</h1>
<p class="sub">What to do before, during and after a college visit, with the questions most families forget to ask.</p>
<h2><span class="n">1</span> Before you go</h2>
{chk(['Register for the official tour and information session on the school’s admissions site',
      'Ask whether you can sit in on a class or meet someone from your student’s intended major',
      'Check whether the school tracks visits as “demonstrated interest”',
      'Have your student write down three things they want to find out'])}
<h2><span class="n">2</span> Questions to ask</h2>
<div class="cols">
{qbox('Admissions', ['What does a typical admitted student look like here?', 'How do you review applications: grades, rigor, essays, activities?', 'Are test scores required, optional or recommended?', 'How do you use self-reported grades?'])}
{qbox('Current students', ['What do you wish you had known before coming here?', 'How easy is it to get the classes you need?', 'What do people do on weekends?', 'How hard was it to find housing after freshman year?'])}
{qbox('Financial aid', ['What percent of need do you typically meet?', 'Do merit scholarships need a separate application?', 'How does Bright Futures work with your aid package?', 'What do students actually pay after aid, on average?'])}
{qbox('Your major', ['How big are classes in the first two years?', 'Are there internships, research or co-ops?', 'Where do graduates in this major work?', 'Is it hard to get into the major once enrolled?'])}
</div>
{foot('Bring this page with you. Snap a photo of each campus to remember it.')}</div>
<div class="page">{top('The Campus Visit Kit')}
<h2 style="margin-top:20px"><span class="n">3</span> Compare up to three schools</h2>
<table><thead><tr><th></th><th>School 1</th><th>School 2</th><th>School 3</th></tr></thead><tbody>{rows}</tbody></table>
<h2><span class="n">4</span> Right after the visit</h2>
{chk(['Have your student write three things they loved and one thing they didn’t, the same day',
      'Save the admissions rep’s name and email',
      'Note anything to mention in a “Why this school?” essay'])}
<div style="margin-top:12px">{lines}</div>
{FOOT}</div>"""
open('campus-visit-kit.html', 'w').write(doc('Campus Visit Kit', p2))

# 3) Senior application tracker (5 referrals)
appcols = ['School', 'Deadline + type<br>(EA / ED / RD)', 'Essays / supplements', 'Self-report<br>(STARS / SSAR)',
           'Test scores sent', 'Recs requested', 'Transcript sent', 'Submitted ✓', 'Decision']
approws = ''.join('<tr>' + '<td></td>' * len(appcols) + '</tr>' for _ in range(13))
schcols = ['Scholarship', 'Amount', 'Deadline', 'What it needs', 'Submitted ✓', 'Result']
schrows = ''.join('<tr>' + '<td></td>' * len(schcols) + '</tr>' for _ in range(9))
cmp_rows = ''.join(f'<tr><th>{r}</th><td></td><td></td><td></td></tr>' for r in
                   ['Total cost of attendance', 'Grants + scholarships (free money)', 'Loans offered', 'What we would actually pay'])
ah = ''.join(f'<th>{c}</th>' for c in appcols)
sh = ''.join(f'<th>{c}</th>' for c in schcols)
p3 = f"""<div class="page">{top('Referral reward · Florida parents')}
<h1>The Senior Year <em>Application Tracker</em></h1>
<p class="sub">One page to see every school, every deadline and every piece at a glance. Fill it in pencil and update it weekly.</p>
<table class="trk apps"><thead><tr>{ah}</tr></thead><tbody>{approws}</tbody></table>
<div class="callout"><b>Deadline tip:</b> Write each school’s deadline one week early. Portals get slow on deadline day, and recommendation letters and transcripts can take time to arrive.</div>
{foot('Always confirm deadlines on each college’s official admissions site.')}</div>
<div class="page">{top('The Senior Year Application Tracker')}
<h2 style="margin-top:20px"><span class="n">1</span> Financial aid checklist</h2>
{chk(['FAFSA submitted', 'FAFSA confirmation saved', 'FFAA submitted (Bright Futures + state aid)',
      'CSS Profile (only if a school requires it)', 'Scholarship applications on the calendar'])}
<h2><span class="n">2</span> Scholarship tracker</h2>
<table class="trk"><thead><tr>{sh}</tr></thead><tbody>{schrows}</tbody></table>
<h2><span class="n">3</span> Decision time: compare aid offers</h2>
<table class="trk"><thead><tr><th></th><th>School 1</th><th>School 2</th><th>School 3</th></tr></thead><tbody>{cmp_rows}</tbody></table>
{FOOT}</div>"""
open('application-tracker.html', 'w').write(doc('Senior Application Tracker', p3))
print('built')
