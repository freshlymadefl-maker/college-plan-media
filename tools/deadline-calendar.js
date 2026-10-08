(function(){
var root=document.getElementById("cp-cal-root")||document.currentScript.parentNode;
root.innerHTML="<div id=\"cp-cal\" style=\"font-family:Inter,Helvetica,Arial,sans-serif;color:#1F2D3D;max-width:640px;margin:0 auto;\">\n<style>\n#cp-cal *{box-sizing:border-box}\n#cp-cal .card{background:#fff;border:1px solid #D6E2EE;border-radius:16px;padding:20px}\n#cp-cal h3{font-family:Poppins,Helvetica,Arial,sans-serif;color:#0B2A4A;font-size:22px;margin:0 0 4px}\n#cp-cal p.sub{color:#5E7186;margin:0 0 16px;font-size:15px}\n#cp-cal .btns{display:flex;flex-wrap:wrap;gap:10px}\n#cp-cal .btns a{flex:1 1 170px;text-align:center;text-decoration:none;font:600 15px Poppins,Helvetica,Arial,sans-serif;padding:12px 14px;border-radius:10px;background:#0B2A4A;color:#fff}\n#cp-cal .btns a.alt{background:#EAF3FB;color:#0B2A4A;border:1px solid #C9D8E8}\n#cp-cal .how{font-size:13px;color:#5E7186;margin:12px 0 0;line-height:1.45}\n#cp-cal h4{font-family:Poppins,Helvetica,Arial,sans-serif;color:#0B2A4A;font-size:17px;margin:22px 0 10px}\n#cp-cal ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:8px}\n#cp-cal li{display:grid;grid-template-columns:64px 1fr;gap:12px;align-items:center;background:#F7FAFD;border:1px solid #E1EAF3;border-radius:12px;padding:10px 12px}\n#cp-cal .d{background:#0B2A4A;color:#fff;border-radius:8px;text-align:center;padding:6px 0;font-family:Poppins,Helvetica,Arial,sans-serif;line-height:1.05}\n#cp-cal .d small{display:block;font-size:11px;letter-spacing:.1em;color:#C9DAEC}\n#cp-cal .d b{font-size:22px}\n#cp-cal .t{font-weight:600;color:#0B2A4A;font-size:15px}\n#cp-cal .w{font-size:12px;color:#5E7186}\n#cp-cal .fine{font-size:12px;color:#5E7186;margin-top:14px}\n</style>\n<div class=\"card\">\n  <h3>Florida College Deadline Calendar</h3>\n  <p class=\"sub\">Add every Florida college deadline that matters to your phone in one tap: UF, FSU, UCF and USF dates, SAT dates, the FFAA and more. When dates change or new ones are added, your calendar updates automatically.</p>\n  <div class=\"btns\">\n    <a id=\"cal-apple\" href=\"#\">Add to iPhone / Mac</a>\n    <a id=\"cal-google\" class=\"alt\" href=\"#\" target=\"_blank\" rel=\"noopener\">Add to Google Calendar</a>\n    <a id=\"cal-outlook\" class=\"alt\" href=\"#\" target=\"_blank\" rel=\"noopener\">Add to Outlook</a>\n  </div>\n  <p class=\"how\">On iPhone, tap \"Subscribe\" when asked. You'll get a reminder the day before each deadline. To remove it later, delete the \"Florida College Deadlines\" calendar.</p>\n  <h4>Coming up</h4>\n  <ul id=\"cal-list\"><li><div class=\"d\"><small>\u2026</small><b>\u2026</b></div><div><div class=\"t\">Loading dates\u2026</div></div></li></ul>\n  <p class=\"fine\">Always confirm dates on each college's official site. College Plan is not affiliated with any college or the State of Florida.</p>\n</div>\n\n</div>\n";

(function(){
  var ICS='cdn.jsdelivr.net/gh/freshlymadefl-maker/college-plan-media@main/calendar/florida-college-deadlines.ics';
  var JSON_URL='https://cdn.jsdelivr.net/gh/freshlymadefl-maker/college-plan-media@main/calendar/events.json';
  document.getElementById('cal-apple').href='webcal://'+ICS;
  document.getElementById('cal-google').href='https://calendar.google.com/calendar/r?cid='+encodeURIComponent('webcal://'+ICS);
  document.getElementById('cal-outlook').href='https://outlook.live.com/calendar/0/addfromweb?url='+encodeURIComponent('https://'+ICS)+'&name='+encodeURIComponent('Florida College Deadlines');
  var M=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'];
  fetch(JSON_URL).then(function(r){return r.json();}).then(function(ev){
    var today=new Date(); today.setHours(0,0,0,0);
    var up=ev.filter(function(e){return new Date(e.date+'T12:00:00')>=today;}).sort(function(a,b){return a.date<b.date?-1:1;}).slice(0,8);
    var ul=document.getElementById('cal-list'); ul.innerHTML='';
    up.forEach(function(e){
      var d=new Date(e.date+'T12:00:00'), li=document.createElement('li');
      li.innerHTML='<div class="d"><small>'+M[d.getMonth()]+'</small><b>'+d.getDate()+'</b></div><div><div class="t"></div><div class="w"></div></div>';
      li.querySelector('.t').textContent=e.title; li.querySelector('.w').textContent=e.who+(e.note?' · '+e.note:'');
      ul.appendChild(li);
    });
  }).catch(function(){ document.getElementById('cal-list').innerHTML='<li><div></div><div class="t">Add the calendar above to see every date.</div></li>'; });
})();

})();
