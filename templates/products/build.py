# Builds the paid roadmap PDFs' HTML (run from templates/products), then render with page.pdf (Letter, print_background).
# Facts verified Oct 8, 2026 against FLDOE, Bright Futures handbook 2026-27, flsenate.gov statutes, studentaid.gov,
# College Board, ACT and each university's admissions deadline page. Re-verify every August.
css = open('../cheatsheet.html').read().split('<style>')[1].split('</style>')[0]
extra = """
.cols { display:grid; grid-template-columns:1fr 1fr; gap:12px; }
.box { border:1px solid var(--line); border-radius:10px; padding:10px 13px; }
.box h3 { font-family:'Poppins'; font-weight:600; font-size:11pt; color:var(--navy); margin:0 0 4px; }
.box p { margin:2px 0; font-size:9.6pt; }
.chk { margin:0; padding:0; list-style:none; }
.chk li { position:relative; padding-left:20px; margin:4px 0; font-size:10pt; }
.chk li:before { content:""; position:absolute; left:0; top:2px; width:11px; height:11px; border:1.5px solid #8FA7C0; border-radius:3px; }
.month { display:grid; grid-template-columns:1.05in 1fr; gap:14px; padding:7px 0; border-bottom:1px dashed var(--line); }
.month:last-child { border-bottom:none; }
table.trk td, table.trk th { height:28px; font-size:8.5pt; padding:5px 6px; }
table.trk tbody td { border-right:1px solid var(--line); }
table.dates td, table.dates th { font-size:9pt; padding:5px 8px; }
table.dates td:first-child { font-family:'Poppins'; font-weight:600; color:var(--navy); white-space:nowrap; width:1.05in; }
.lines { border-bottom:1px solid var(--line); height:24px; }
.cover { background: linear-gradient(160deg,#0E3359 0%,#0B2A4A 60%,#081F38 100%); color:#fff; padding:0.9in 0.8in; }
.cover .pill { display:inline-block; font-family:'Poppins'; font-weight:600; font-size:9pt; letter-spacing:.16em; text-transform:uppercase; background:#B5A21F; color:#fff; border-radius:999px; padding:7px 14px; }
.cover h1 { color:#fff; font-size:40pt; margin:28px 0 10px; line-height:1.04; }
.cover h1 em { color:#F1E27A; }
.cover .lead { font-size:14pt; color:#C9DAEC; max-width:5.8in; line-height:1.45; }
.cover .inside { margin-top:40px; background:rgba(255,255,255,.07); border:1px solid rgba(255,255,255,.18); border-radius:14px; padding:18px 22px; }
.cover .inside h3 { font-family:'Poppins'; font-size:11pt; letter-spacing:.12em; text-transform:uppercase; color:#F1E27A; margin:0 0 8px; }
.cover .inside ol { margin:0; padding-left:20px; columns:2; column-gap:28px; font-size:10.5pt; line-height:1.7; color:#E6EEF7; }
.cover .brand { position:absolute; left:0.8in; right:0.8in; bottom:0.7in; display:flex; justify-content:space-between; align-items:flex-end; font-size:9pt; color:#9FB6CF; }
.cover .brand img { height:34px; }
.big2 { font-family:'Poppins'; font-weight:600; font-size:15pt; color:var(--navy); margin:0; }
.tag2 { display:inline-block; font-family:'Poppins'; font-weight:600; font-size:8pt; letter-spacing:.1em; text-transform:uppercase; color:#fff; background:var(--navy); border-radius:999px; padding:3px 9px; margin-right:6px; }
.grid4 { display:grid; grid-template-columns:repeat(4,1fr); gap:10px; }
.grid4 .box h3 { font-size:10.5pt; }
.grid4 .box li { font-size:9pt; }
.src { font-size:8pt; color:var(--muted); line-height:1.5; }
/* roomier sizing for the paid guides */
.page:not(.cover) { font-size:11.4pt; }
.page h1 { font-size:30pt; margin-top:26px; }
.page .sub { font-size:12.5pt; margin-bottom:20px; }
.page h2 { font-size:15pt; margin:24px 0 10px; }
.chk li { font-size:11pt; margin:5px 0; padding-left:24px; }
.chk li:before { width:13px; height:13px; top:3px; }
.box { padding:14px 16px; }
.box h3 { font-size:12.5pt; margin-bottom:6px; }
.box p { font-size:10.8pt; line-height:1.5; }
.cols { gap:14px; }
.month { padding:8px 0; grid-template-columns:1.2in 1fr; }
table.tight td, table.tight th { padding:5px 9px; font-size:9.8pt; }
table.dates.sm td, table.dates.sm th { font-size:9pt; padding:4px 8px; }
.when { font-size:12pt; }
.when span { font-size:9.5pt; }
.callout { font-size:11pt; padding:13px 16px; margin-top:18px; }
table.dates td, table.dates th { font-size:10pt; padding:7px 9px; }
table.trk td, table.trk th { height:34px; font-size:9pt; }
table th, table td { font-size:10.4pt; padding:9px 10px; }
.grid4 .box li { font-size:10pt; }
.grid4 .box h3 { font-size:11.5pt; }
.note { font-size:9.6pt; }
.lines { height:30px; }
.small .box p { font-size:9.8pt; line-height:1.4; }
.small .box { padding:10px 13px; }
.cover .lead { font-size:16pt; }
.cover h1 { font-size:46pt; }
.cover .inside { margin-top:56px; padding:24px 28px; }
.cover .inside ol { font-size:12pt; line-height:1.9; }
"""

def doc(title, body):
    return f'<!doctype html><html><head><meta charset="utf-8"><title>{title}</title><style>{css}{extra}</style></head><body>{body}</body></html>'

def top(tag):
    return f'<div class="top"><img src="../wordmark_navy.png" alt="College Plan"><div class="tag">{tag}</div></div>'

def foot(text, n):
    return f'<div class="foot"><span>{text}</span><span><b>@college.plan</b> · {n}</span></div>'

def chk(items):
    return '<ul class="chk">' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'

def month(when, sub, items):
    return f'<div class="month"><div class="when">{when}<span>{sub}</span></div>{chk(items)}</div>'

def page(tag, body, ftext, n):
    return f'<div class="page">{top(tag)}{body}{foot(ftext, n)}</div>'

def cover(pill, title, lead, inside):
    lis = ''.join(f'<li>{i}</li>' for i in inside)
    return f"""<div class="page cover"><span class="pill">{pill}</span><h1>{title}</h1><p class="lead">{lead}</p>
<div class="inside"><h3>What's inside</h3><ol>{lis}</ol></div>
<div class="brand"><img src="../wordmark_white.png" alt="College Plan"><span>For personal use by the purchasing family. Please don't share or resell.<br>Not affiliated with the State of Florida or any university.</span></div></div>"""

def blank_table(cols, rows, cls='trk'):
    h = ''.join(f'<th>{c}</th>' for c in cols)
    r = ''.join('<tr>' + '<td></td>' * len(cols) + '</tr>' for _ in range(rows))
    return f'<table class="{cls}"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table>'

# =====================================================================================
# SENIOR YEAR ROADMAP (Class of 2027)
# =====================================================================================
ST = 'Florida Senior Year Roadmap · Class of 2027'
s = []
s.append(cover('Class of 2027 · Florida', 'The Florida Senior Year <em>Roadmap</em>',
  'Every deadline, form and step for senior year, month by month, so nothing slips through the cracks. Made for Florida families.',
  ['Senior year at a glance', 'Key dates: UF, FSU, UCF, USF, FIU, FAU', 'SAT and ACT dates for 2026–27', 'Month-by-month checklist',
   'Bright Futures: the senior checklist', 'FAFSA + FFAA step by step', 'Application tracker', 'Scholarship tracker',
   'Compare aid offers', 'Questions for financial aid offices']))

s.append(page(ST, f"""
<h1>Senior year <em>at a glance</em></h1>
<p class="sub">Five things decide how smoothly senior year goes. Everything else in this roadmap supports these.</p>
<div class="cols">
<div class="box"><h3>1. Know every deadline</h3><p>Early deadlines at Florida universities start <b>October 15</b>. Write each school's dates in the tracker (page 8) the first week of school.</p></div>
<div class="box"><h3>2. File two aid forms</h3><p>The <b>FAFSA</b> (federal aid) and the <b>FFAA</b> (Florida's form for Bright Futures and state aid). They are separate. You need both.</p></div>
<div class="box"><h3>3. Lock in Bright Futures</h3><p>GPA, test score, service or work hours, then the FFAA. Ask the counselor for a Bright Futures evaluation in the fall.</p></div>
<div class="box"><h3>4. Ask early, follow up</h3><p>Check which schools want recommendation letters (UF and UCF don't use them). If needed, ask teachers <b>3–4 weeks</b> ahead. Check every portal weekly.</p></div>
</div>
<div class="box" style="margin-top:12px"><h3>5. Compare real costs before May 1</h3><p>Acceptance letters arrive first, then aid offers. Compare what you'd actually pay at each school (page 10) before paying a deposit. UF, FSU, FIU and FAU list <b>May 1</b> as the deposit deadline for Early Action and regular admits. Early Decision deposits are due much sooner.</p></div>
<h2><span class="n">✓</span> This month's quick wins</h2>
{chk(['Make a list of every school your student is applying to, with the plan for each (Early Decision, Early Action or regular)',
      'Create StudentAid.gov accounts for your student and each parent who must be a FAFSA contributor (usually one)',
      'Find the school counselor’s email and ask for a Bright Futures evaluation',
      'Put one 20-minute “college check-in” on the family calendar every week this fall'])}
<div class="callout"><b>How to use this roadmap:</b> Read it once now. Then each month, open the month-by-month checklist (pages 4–5), check things off, and update the trackers. Use pencil, because dates and plans change.</div>
""", 'Dates change. Always confirm on each school’s official admissions site.', 2))

dates = [
 ('Sept 23, 2026', 'The 2027–28 FAFSA opened (uses 2025 tax information)'),
 ('Oct 1', 'FFAA opens (Florida’s application for Bright Futures and state aid)'),
 ('Oct 15', 'UF Early Decision (binding) · FSU Early Decision and Early Action (EA for Florida residents) · UCF Early Action · FAU Early Action'),
 ('Oct 22', 'UF STARS self-reported record due (ED) · FSU and FAU early materials due'),
 ('Nov 1', 'UF Early Action (STARS due Nov 8)'),
 ('Nov 2', 'USF Early Action · FIU Early Action (FIU: all documents due the same day)'),
 ('Nov 15–16', 'UCF early materials due (Nov 15) · USF early materials due (Nov 16)'),
 ('Dec 1', 'FSU regular deadline'),
 ('Dec 4–17', 'Early decisions arrive: UCF and FAU (Dec 4), USF (Dec 9), FIU (Dec 10), UF ED (Dec 11), FSU (Dec 17)'),
 ('Dec 16', 'USF regular deadline · FIU regular deadline'),
 ('Jan 8, 2027', 'UF Early Decision admits: confirm and pay the non-refundable $200 deposit, or the admission is canceled'),
 ('Jan 15', 'UF regular deadline (STARS Jan 22) · FSU Early Decision deposit due · USF regular materials and scholarship deadline · FAU merit scholarship deadline'),
 ('Jan 22', 'UF Early Action decisions'),
 ('Feb–Mar', 'Regular decisions: USF (Feb 10), FSU (Feb 18), UF (Mar 19). Rolling deadlines: FSU and USF (Mar 1), FIU final (Mar 2), FAU (Mar 12)'),
 ('May 1', 'UCF regular deadline · Deposit deadline (Early Action and regular admits) at UF, FSU, FIU and FAU'),
 ('Aug 31, 2027', 'FFAA final deadline · Last test date that counts for Bright Futures'),
]
drows = ''.join(f'<tr><td>{d}</td><td>{t}</td></tr>' for d, t in dates)
s.append(page(ST, f"""
<h1>Key dates for <em>Florida seniors</em></h1>
<p class="sub">From each university's 2026–27 freshman deadline page and the federal and state aid calendars. Some school pages don't print a year, so double-check before you rely on a date.</p>
<table class="dates sm"><thead><tr><th>Date</th><th>What's due</th></tr></thead><tbody>{drows}</tbody></table>
<div class="callout" style="margin-top:10px"><b>Early Decision is binding.</b> If admitted Early Decision (UF and FSU both offer it this year), your student commits to attend. Early Action is not binding. When in doubt, choose Early Action.</div>
""", 'Sources: admissions.ufl.edu, admissions.fsu.edu, ucf.edu, usf.edu, admissions.fiu.edu, fau.edu, studentaid.gov, FloridaBrightFutures.gov.', 3))

sat = [('Nov 7, 2026', 'Oct 23'), ('Dec 5, 2026', 'Nov 20'), ('Mar 6, 2027', 'Feb 19'), ('May 1, 2027', 'Apr 16'), ('June 5, 2027', 'May 21')]
act = [('Oct 17, 2026', 'Sept 11'), ('Dec 12, 2026', 'Nov 6'), ('Feb 27, 2027', 'Jan 22'), ('Apr 10, 2027', 'Mar 5'), ('June 12, 2027', 'May 7'), ('July 10, 2027', 'June 4')]
srows = ''.join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a, b in sat)
arows = ''.join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a, b in act)
s.append(page(ST, f"""
<h1>Month by <em>month</em></h1>
<p class="sub">Check off each item as you go. If you're starting late, begin with the current month and use “Key dates” to catch up.</p>
{month('Aug – Sept', 'set the plan', ['Finalize the college list and each school’s plan (ED, EA or regular)', 'If a school wants recommendation letters (UF and UCF don’t), ask teachers 3–4 weeks before the deadline', 'Create StudentAid.gov accounts for your student and each parent contributor', 'Draft the main essay and list each school’s supplemental essays', 'Register for a fall SAT or ACT if your student needs a higher score'])}
{month('October', 'early deadlines', ['File the FAFSA (it opened Sept 23) and save the confirmation', 'File the FFAA once it opens Oct 1', 'Submit applications due Oct 15, then complete UF STARS or other self-reported records', 'Ask the counselor for a Bright Futures evaluation', 'Check every portal for missing items'])}
{month('November', 'keep it moving', ['Submit Nov 1–2 Early Action applications (UF, USF, FIU)', 'Send official test scores to schools that require them', 'Turn in early materials by each school’s deadline', 'Retake the SAT or ACT if needed for Bright Futures or admissions'])}
{month('December', 'decisions start', ['Watch for early decisions (they start Dec 4 at UCF and FAU)', 'Submit regular applications (FSU Dec 1, USF and FIU Dec 16)', 'Apply for at least two scholarships', 'Celebrate every win, and take a breath after any “no”'])}
""", 'Dates change. Confirm on each school’s official site.', 4))

s.append(page(ST, f"""
<div style="height:10px"></div>
{month('January', 'regular round', ['Submit UF’s regular application (Jan 15) and STARS (Jan 22)', 'Check scholarship deadlines (USF and FAU merit: Jan 15)', 'Review the FAFSA Submission Summary for errors', 'Send mid-year grades if a school asks for them'])}
{month('Feb – March', 'finish strong', ['Track regular decisions in the application tracker', 'Make sure service or work hours are documented and turned in (your district sets the deadline)', 'Spring and summer test dates still count for Bright Futures (tests taken through Aug 31)', 'Keep grades up: admission offers can depend on final grades'])}
{month('April', 'compare + choose', ['Compare aid offers side by side (page 10)', 'Visit admitted-student days at your top choices', 'Ask financial aid offices about anything unclear in an offer', 'Decide as a family'])}
{month('May', 'commit', ['Pay the deposit by the school’s deadline (often May 1)', 'Let the other schools know your student won’t be attending', 'Sign up for orientation and housing at the chosen school'])}
{month('June – Aug', 'last steps', ['Request the final transcript be sent to the chosen school', 'If the FFAA isn’t done, submit it by Aug 31, 2027', 'Last Bright Futures test chances: June 5 SAT, June 12 and July 10 ACT, Aug 28 SAT (anticipated). Tests count through Aug 31, 2027'])}
<h2 style="margin-top:14px"><span class="n">✎</span> Test dates for 2026–27</h2>
<div class="cols"><div><table class="dates sm"><thead><tr><th>SAT date</th><th>Register by</th></tr></thead><tbody>{srows}</tbody></table></div>
<div><table class="dates sm"><thead><tr><th>ACT date</th><th>Register by</th></tr></thead><tbody>{arows}</tbody></table></div></div>
""", 'Test dates: College Board and ACT (2026–27). Late registration costs extra.', 5))

s.append(page(ST, f"""
<h1>Bright Futures: <em>the senior checklist</em></h1>
<p class="sub">Bright Futures is Florida's biggest scholarship. Requirements for the Class of 2027:</p>
<table class="tight"><thead><tr><th></th><th>Florida Academic Scholars</th><th>Florida Medallion Scholars</th></tr></thead><tbody>
<tr><th>Pays</th><td>100% of tuition and applicable fees at Florida public colleges and universities</td><td>75% of tuition and applicable fees at Florida public universities (100% for an associate degree at a Florida College System school)</td></tr>
<tr><th>Bright Futures GPA</th><td>3.50 weighted</td><td>3.00 weighted</td></tr>
<tr><th>Test score (one of)</th><td>SAT 1330 · ACT 29 · CLT 95</td><td>SAT 1190 · ACT 24 · CLT 82</td></tr>
<tr><th>Hours</th><td>100 volunteer hours, 100 paid work hours, or a combination totaling 100</td><td>75 volunteer hours, 100 paid work hours, or a combination totaling 100</td></tr>
</tbody></table>
<p class="note">The Bright Futures GPA uses 16 core credits: 4 English, 4 math (Algebra 1 or higher), 3 natural science, 3 social science and 2 credits of the same world language. Honors, AP, IB, AICE and academic dual enrollment courses earn extra weight.</p>
<h2 style="margin-top:16px"><span class="n">1</span> This fall</h2>
{chk(['Ask the counselor for a Bright Futures evaluation: where does your student stand on GPA, test score and hours?', 'If a score is short, register for the next SAT, ACT or CLT. Students can test as many times as they want', 'Count documented hours. Each one must be signed by your student, a parent and the organization, plus any reflection your district requires'])}
<h2 style="margin-top:12px"><span class="n">2</span> Apply: the FFAA</h2>
{chk(['Submit the Florida Financial Aid Application (FFAA). It opens Oct 1 of senior year', 'Final deadline: <b>Aug 31, 2027</b>, with no exceptions. File it in the fall and save the confirmation'])}
<h2 style="margin-top:12px"><span class="n">3</span> Before graduation</h2>
{chk(['Turn in all hours by your district’s deadline', 'Finish the 16 core credits with the GPA you need (tests taken by Aug 31, 2027 still count)'])}
<div class="callout" style="margin-top:10px"><b>Not automatic:</b> Even a student who meets every requirement gets nothing without the FFAA. Mid-year graduates have different deadlines; ask the counselor.</div>
""", 'Source: Florida Bright Futures Student Handbook 2026–27 and FAS/FMS requirements (FloridaBrightFutures.gov).', 6))

s.append(page(ST, f"""
<h1>FAFSA + FFAA, <em>step by step</em></h1>
<p class="sub">Two forms, two purposes. Do both in the fall of senior year.</p>
<div class="cols">
<div class="box"><h3>FAFSA (federal)</h3><p>Opens the door to Pell Grants, work-study, federal loans and many colleges' own aid, plus Florida need-based grants. The 2027–28 FAFSA opened Sept 23, 2026 and uses <b>2025</b> tax information.</p></div>
<div class="box"><h3>FFAA (Florida)</h3><p>Florida's application for Bright Futures and other state scholarships and grants. Opens Oct 1 of senior year. Final deadline Aug 31 after graduation.</p></div>
</div>
<h2><span class="n">1</span> FAFSA checklist</h2>
{chk(['Your student and each parent contributor create a StudentAid.gov account (usually one parent; both if married parents filed taxes separately)', 'Gather your 2025 federal tax return and any untaxed income records', 'Your student starts the FAFSA and invites the parent as a “contributor”', 'Every contributor gives consent to share tax information. Without it, no federal aid', 'List every college your student is applying to', 'Submit, then save the confirmation and review the FAFSA Submission Summary', 'Check each college’s financial aid priority date. Many are earlier than you’d expect'])}
<h2><span class="n">2</span> FFAA checklist</h2>
{chk(['Your student completes the FFAA on Florida’s student financial aid website', 'Use your student’s legal name and Social Security number exactly as the school has them', 'Submit and save the confirmation', 'If your student graduates mid-year, the deadline is Dec 31'])}
<h2><span class="n">3</span> Also check</h2>
{chk(['Does any school on the list require the CSS Profile? (Mostly private colleges.)', 'Does any school require a separate scholarship application?', 'Are there county or local scholarships through your high school?'])}
""", 'Sources: studentaid.gov (2027–28 FAFSA), FloridaBrightFutures.gov (FFAA).', 7))

appcols = ['School', 'Plan<br>(ED/EA/RD)', 'Deadline', 'Essays', 'Self-report<br>(e.g. STARS)', 'Scores sent', 'Recs<br>(if required)', 'Submitted ✓', 'Decision']
s.append(page(ST, f"""
<h1>Application <em>tracker</em></h1>
<p class="sub">One row per school. Write each deadline one week early: portals get slow on deadline day.</p>
{blank_table(appcols, 17)}
""", 'Update weekly. Check every portal for missing items.', 8))

schcols = ['Scholarship', 'Amount', 'Deadline', 'What it needs', 'Submitted ✓', 'Result']
s.append(page(ST, f"""
<h1>Scholarship <em>tracker</em></h1>
<p class="sub">Apply for a couple every month instead of a pile in spring. Local scholarships often have fewer applicants.</p>
{blank_table(schcols, 14)}
<div class="callout"><b>Where to look:</b> your high school's counseling office, each university's scholarship page, your county's education foundation, employers, churches and community groups.</div>
""", 'Never pay to apply for a scholarship.', 9))

cmp = ['Cost of attendance (tuition, fees, housing, food, books)', 'Bright Futures', 'Grants (free money)', 'Scholarships (free money)', 'Total free money', 'Cost minus free money', 'Loans offered', 'Work-study', 'What we would actually pay per year']
crow = ''.join(f'<tr><th>{c}</th><td></td><td></td><td></td></tr>' for c in cmp)
s.append(page(ST, f"""
<h1>Compare <em>aid offers</em></h1>
<p class="sub">Aid letters look different at every school. Put them side by side before paying a deposit.</p>
<table class="trk"><thead><tr><th></th><th>School 1</th><th>School 2</th><th>School 3</th></tr></thead><tbody>{crow}</tbody></table>
<h2><span class="n">?</span> Questions to ask each financial aid office</h2>
{chk(['Is this aid renewable every year? What GPA or credits does it require?', 'How does Bright Futures combine with your scholarships?', 'Will this offer change if we have new information (like a job change)?', 'When is the deposit due, and is it refundable?'])}
<p class="src" style="margin-top:16px">This roadmap is for planning help only and isn't official advice. Requirements and dates can change; confirm with your school counselor, each university and FloridaBrightFutures.gov. College Plan is not affiliated with the State of Florida or any university. © 2026 College Plan.</p>
""", 'collegeplan.beehiiv.com', 10))
open('senior-roadmap.html', 'w').write(doc('The Florida Senior Year Roadmap', ''.join(s)))

# =====================================================================================
# FRESHMAN ROADMAP (Class of 2030): plan now, don't cram later
# =====================================================================================
FT = 'Freshman Roadmap · Plan now, don’t cram later'
f = []
f.append(cover('Class of 2030 · Florida', 'The Freshman <em>Roadmap</em>',
  'Plan now, don\'t cram later. Small steps in 9th grade make senior year calm instead of chaotic. A four-year plan built for Florida families.',
  ['Why 9th grade matters', 'Florida graduation requirements', 'Bright Futures, explained early', 'The four-year game plan', '9th grade month by month',
   'Four-year course planner', 'Service hour log', 'Activities + awards log', 'Dual enrollment, AP, IB + AICE', 'A peek at 10th–12th']))

f.append(page(FT, f"""
<h1>Why 9th grade <em>matters</em></h1>
<p class="sub">Most families start thinking about college in junior year. By then, half of the high school record is already written.</p>
<div class="cols">
<div class="box"><h3>Grades count from day one</h3><p>Every core course in 9th grade goes into the GPA colleges see and into the <b>Bright Futures GPA</b>. A rough first semester is fixable, but easier to avoid.</p></div>
<div class="box"><h3>Courses build on each other</h3><p>Math, science and world language follow a sequence. Choices in 9th grade decide which advanced courses are open in 11th and 12th.</p></div>
<div class="box"><h3>Hours add up slowly</h3><p>Bright Futures asks for volunteer or paid work hours <b>earned during high school</b>. A few hours a month starting now is easy. 100 hours in senior spring is not.</p></div>
<div class="box"><h3>Habits beat cramming</h3><p>A weekly check of grades, a simple log for hours and awards, and one family check-in a month. That's the whole system.</p></div>
</div>
<h2><span class="n">✓</span> Do these in the first month</h2>
{chk(['Find the school counselor’s name and email, and save them in your phone', 'Log in to the parent portal and learn where grades show up', 'Ask the counselor how your district counts Bright Futures service hours (and whether the summer before 9th grade counts)', 'Start the service hour log (page 8) and the activities log (page 9)', 'Put a 20-minute “college check-in” on the family calendar once a month'])}
<div class="callout"><b>The mindset:</b> You're not choosing a college in 9th grade. You're keeping doors open, so in 12th grade your student gets to choose.</div>
""", 'Requirements change. Confirm with your school counselor.', 2))

f.append(page(FT, f"""
<h1>Florida graduation <em>requirements</em></h1>
<p class="sub">The standard 24-credit diploma, for students entering 9th grade in 2026&#8209;27.</p>
<table class="tight"><thead><tr><th>Subject</th><th>Credits</th><th>Notes</th></tr></thead><tbody>
<tr><th>English</th><td>4</td><td>English 1–4</td></tr>
<tr><th>Math</th><td>4</td><td>Must include Algebra 1 and Geometry</td></tr>
<tr><th>Science</th><td>3</td><td>Must include Biology 1; two must have a lab</td></tr>
<tr><th>Social studies</th><td>3</td><td>World History, U.S. History, U.S. Government (½) and Economics (½)</td></tr>
<tr><th>Arts</th><td>1</td><td>Fine or performing arts, speech and debate, or career and technical/practical arts</td></tr>
<tr><th>PE</th><td>1</td><td>Includes health</td></tr>
<tr><th>Personal financial literacy</th><td>½</td><td>Required for students entering 9th grade in 2023–24 and later</td></tr>
<tr><th>Electives</th><td>7½</td><td></td></tr>
</tbody></table>
<h2 style="margin-top:14px"><span class="n">!</span> Tests and GPA</h2>
{chk(['Pass the Grade 10 English Language Arts test (or earn a concordant score)', 'Pass the Algebra 1 end-of-course exam (or earn a comparative score)', 'End-of-course exams in Algebra 1, Geometry, Biology 1 and U.S. History count for <b>30%</b> of the course grade', 'Take the U.S. Government civic literacy test (taking it is required; passing is not)', 'Graduate with at least a 2.0 unweighted GPA'])}
<h2 style="margin-top:14px"><span class="n">★</span> Worth knowing</h2>
<div class="cols small">
<div class="box"><h3>Scholar designation</h3><p>Extra recognition on the diploma: Algebra 2 and statistics (or equally rigorous courses), chemistry or physics plus one more equally rigorous science, 2 credits of one world language, at least one AP, IB, AICE or dual enrollment course, and passing the Geometry, Biology 1 and U.S. History end-of-course exams.</p></div>
<div class="box"><h3>18-credit option (ACCEL)</h3><p>Florida also has an 18-credit accelerated diploma option with no PE requirement and fewer electives. Ask the counselor whether it fits your student.</p></div>
</div>
""", 'Sources: Fla. Stat. 1003.4282 and 1003.4285; FLDOE graduation requirements.', 3))

f.append(page(FT, f"""
<h1>Bright Futures, <em>explained early</em></h1>
<p class="sub">It can pay 75% to 100% of tuition and applicable fees at Florida public colleges and universities. Here's what your student needs, and what to start now.</p>
<div class="cols">
<div class="box"><h3>The 16 core credits</h3><p>The Bright Futures GPA only uses these: 4 English, 4 math (Algebra 1 or higher), 3 natural science, 3 social science and <b>2 credits of the same world language</b>.</p></div>
<div class="box"><h3>Weighted courses help</h3><p>Honors, AP, IB, AICE and academic dual enrollment courses add 0.5 per year-long course (0.25 per semester) to the Bright Futures GPA.</p></div>
<div class="box"><h3>Volunteer or work hours</h3><p>Academic Scholars: 100 volunteer hours, 100 paid work hours or a combination. Medallion: 75 volunteer hours, 100 paid work hours or a combination totaling 100. Hours must be earned during high school, documented, and signed by your student, a parent and the organization. Your district approves which activities count.</p></div>
<div class="box"><h3>A test score, later</h3><p>Scores for the Class of 2030 aren't published yet. For the Class of 2028, Academic Scholars need SAT 1350, ACT 29 or CLT 96, and Medallion needs SAT 1200, ACT 25 or CLT 83, plus a 3.5 or 3.0 weighted GPA. Requirements have been rising.</p></div>
</div>
<h2><span class="n">✓</span> Bright Futures to-dos for 9th grade</h2>
{chk(['Get your district’s service hour form and approved activity list', 'Log hours as they happen and turn them in at the end of every school year', 'Start a world language your student can continue for two years', 'Choose honors or advanced classes where your student is ready for them', 'Remember the last step, years from now: the FFAA in senior year. Bright Futures is never automatic'])}
""", 'Source: Florida Bright Futures Student Handbook 2026–27 (FloridaBrightFutures.gov).', 4))

f.append(page(FT, f"""
<h1>The four-year <em>game plan</em></h1>
<p class="sub">One small focus per year. This is the “don't cram later” part.</p>
<div class="grid4">
<div class="box"><h3>9th: build habits</h3><ul class="chk"><li>Strong grades in core classes</li><li>Start the hour log</li><li>Begin a world language</li><li>Try 1–2 activities</li><li>Spring: PSAT 8/9 if your school offers it</li></ul></div>
<div class="box"><h3>10th: go deeper</h3><ul class="chk"><li>Add rigor where ready (honors, AP, AICE, IB)</li><li>Spring: PSAT 10 if offered</li><li>Ask about dual enrollment</li><li>Keep logging hours</li><li>Summer job, program or project</li></ul></div>
<div class="box"><h3>11th: the big year</h3><ul class="chk"><li>Fall: PSAT/NMSQT (the National Merit qualifier)</li><li>Winter or spring: SAT, ACT or CLT</li><li>Bright Futures evaluation</li><li>Build a college list, visit campuses</li><li>Ask teachers for recs in spring if schools require them</li></ul></div>
<div class="box"><h3>12th: apply + pay</h3><ul class="chk"><li>Early deadlines start mid-October</li><li>FAFSA in the fall</li><li>FFAA for Bright Futures</li><li>Scholarships monthly</li><li>Compare aid, then decide by May 1</li></ul></div>
</div>
<h2><span class="n">✎</span> Our family's goals</h2>
<div class="cols">
<div><p class="big2" style="font-size:11pt">By the end of 9th grade, we want…</p><div class="lines"></div><div class="lines"></div><div class="lines"></div><div class="lines"></div></div>
<div><p class="big2" style="font-size:11pt">Interests to explore…</p><div class="lines"></div><div class="lines"></div><div class="lines"></div><div class="lines"></div></div>
</div>
<div class="callout"><b>Keep it light:</b> The goal is steady progress, not a résumé factory. One meaningful activity beats five your student doesn't care about.</div>
""", 'PSAT 8/9 and PSAT 10 are offered in the spring at many schools. Ask your school.', 5))

f.append(page(FT, f"""
<h1>9th grade, <em>month by month</em></h1>
<p class="sub">About 20 minutes a month. Check them off as you go.</p>
{month('Aug – Sept', 'settle in', ['Save the counselor’s contact info and log in to the parent portal', 'Ask how your district handles Bright Futures service hours', 'Start the hour log and the activities log', 'Help your student pick one or two activities to try'])}
{month('Oct – Nov', 'first check', ['Review progress reports together. Catch slipping grades early', 'Find tutoring or teacher help hours if a class is hard', 'Look for a volunteer opportunity your student would actually enjoy'])}
{month('Dec – Jan', 'mid-year', ['Look at first-semester grades: what worked, what didn’t?', 'Turn in any hours your school wants logged mid-year', 'Update the activities log with awards and roles'])}
{month('Feb – Mar', 'plan 10th grade', ['Course selection for 10th grade: talk about honors and advanced options', 'Keep the world language going for a second year', 'Ask the counselor about dual enrollment timing'])}
{month('Apr – May', 'finish strong', ['Spring tests: PSAT 8/9 if your school offers it, and end-of-course exams', 'Turn in all service hours for the year', 'Plan a summer that builds something: a job, volunteering, a program or a project'])}
{month('Summer', 'recharge + grow', ['Volunteer or work (ask your district if summer hours count)', 'Read for fun', 'Update both logs before school starts'])}
""", 'Small steps every month beat a senior-year scramble.', 6))

yrs = ['9th grade', '10th grade', '11th grade', '12th grade']
subj = ['English', 'Math', 'Science', 'Social studies', 'World language', 'Arts / PE / electives', 'Advanced (Honors, AP, AICE, IB, DE)']
cp = ''.join(f'<tr><th style="height:58px">{s_}</th>' + '<td></td>' * 4 + '</tr>' for s_ in subj)
f.append(page(FT, f"""
<h1>Four-year <em>course planner</em></h1>
<p class="sub">Sketch the plan in pencil with your counselor. Check it each spring at course selection.</p>
<table class="trk"><thead><tr><th>Subject</th>{''.join(f'<th>{y}</th>' for y in yrs)}</tr></thead><tbody>{cp}</tbody></table>
<h2><span class="n">✓</span> Quick checks</h2>
{chk(['Algebra 1 and Geometry are on the plan', 'Biology 1 and at least two lab sciences', 'Two years of the <b>same</b> world language (for Bright Futures)', 'Personal financial literacy (½ credit)', 'Room for at least one advanced or dual enrollment course'])}
""", 'Bright Futures uses 16 core credits. Ask the counselor to check the plan.', 7))

hcols = ['Date', 'Organization', 'What we did', 'Hours', 'Contact + phone', 'Signed?']
f.append(page(FT, f"""
<h1>Service hour <em>log</em></h1>
<p class="sub">Write it down the same day. Every entry must be documented and signed by your student, a parent and the organization. Use your district's official form when you turn hours in.</p>
{blank_table(hcols, 16)}
<p class="note">Running total: ________ hours. Goal: 100 (or 75 for Medallion volunteer hours). Paid work hours can count too.</p>
""", 'Your district approves which activities count. Ask before you start.', 8))

acols = ['Activity, award or job', 'Grade(s)', 'Role / what I did', 'Hours per week', 'Proud of']
f.append(page(FT, f"""
<h1>Activities + <em>awards log</em></h1>
<p class="sub">Future applications will ask about activities, awards and jobs. This log turns senior-year guesswork into copy and paste.</p>
{blank_table(acols, 17)}
""", 'Include jobs, family responsibilities and personal projects too.', 9))

f.append(page(FT, f"""
<h1>Dual enrollment, AP, <em>IB + AICE</em></h1>
<p class="sub">Four ways to take college-level work in high school. AP, IB, AICE and academic (college-credit) dual enrollment courses earn extra weight in the Bright Futures GPA.</p>
<div class="cols">
<div class="box"><h3>Dual enrollment</h3><p>Real college classes through a Florida college or university, counting for high school and college credit. Public school students pay no tuition or fees, and course materials are free. Open to grades 6–12. College-credit courses need a 3.0 unweighted GPA plus a qualifying placement test score; career certificate courses need a 2.0.</p></div>
<div class="box"><h3>AP (Advanced Placement)</h3><p>College-level courses taught at your high school, with an exam in May. A qualifying score can earn college credit.</p></div>
<div class="box"><h3>IB (International Baccalaureate)</h3><p>A full two-year diploma program in 11th and 12th grade at participating schools, often with pre-IB courses in 9th and 10th.</p></div>
<div class="box"><h3>AICE (Cambridge)</h3><p>A program of advanced courses and exams offered at many Florida high schools, with its own AICE diploma.</p></div>
</div>
<h2 style="margin-top:12px"><span class="n">?</span> Questions for the counselor</h2>
{chk(['Which of these does our school offer, and when can my student start?', 'Which college is our district’s dual enrollment partner, and what are its deadlines?', 'Which placement tests count (PERT, SAT, ACT, PSAT)?', 'How do these choices fit the four-year course plan?'])}
<h2 style="margin-top:12px"><span class="n">→</span> A peek at what's next</h2>
{chk(['<b>10th:</b> add rigor where ready, PSAT 10 in spring, keep logging hours', '<b>11th:</b> PSAT/NMSQT in the fall, SAT/ACT/CLT, college list and visits', '<b>12th:</b> applications from mid-October, FAFSA and FFAA, scholarships, decide by May 1'])}
<p class="src" style="margin-top:6px">Sources: Fla. Stat. 1007.271 (dual enrollment), 1003.4282 and 1003.4285 (graduation), Florida Bright Futures Student Handbook 2026–27, College Board. This roadmap is for planning help and isn't official advice; confirm with your school counselor. College Plan is not affiliated with the State of Florida or any school. © 2026 College Plan.</p>
""", 'collegeplan.beehiiv.com', 10))
open('freshman-roadmap.html', 'w').write(doc('The Freshman Roadmap', ''.join(f)))
print('built')
