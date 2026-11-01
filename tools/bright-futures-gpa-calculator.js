(function(){
var root=document.getElementById("cp-gpa-root")||document.currentScript.parentNode;
root.innerHTML="<div id=\"cp-gpa\" style=\"font-family:Inter,Helvetica,Arial,sans-serif;color:#1F2D3D;max-width:680px;margin:0 auto;\">\n<style>\n#cp-gpa *{box-sizing:border-box}\n#cp-gpa .card{background:#fff;border:1px solid #D6E2EE;border-radius:16px;padding:20px 20px 22px}\n#cp-gpa h3{font-family:Poppins,Helvetica,Arial,sans-serif;color:#0B2A4A;font-size:22px;margin:0 0 4px}\n#cp-gpa p.sub{color:#5E7186;margin:0 0 14px;font-size:15px;line-height:1.45}\n#cp-gpa .row{display:grid;grid-template-columns:1.4fr 0.8fr 0.9fr 1fr 28px;gap:8px;align-items:center;margin-bottom:8px}\n#cp-gpa .head{font-size:12px;font-weight:600;color:#5E7186;text-transform:uppercase;letter-spacing:.04em;margin-bottom:6px}\n#cp-gpa select{font:15px Inter,Helvetica,Arial,sans-serif;padding:9px 8px;border:1px solid #C9D8E8;border-radius:10px;background:#F7FAFD;color:#1F2D3D;width:100%}\n#cp-gpa .x{background:none;border:0;color:#8A9AAD;font-size:20px;cursor:pointer;padding:0;line-height:1}\n#cp-gpa .btns{display:flex;gap:10px;flex-wrap:wrap;margin-top:6px}\n#cp-gpa .ghost{background:#EAF3FB;color:#0B2A4A;border:1px solid #C9D8E8;border-radius:10px;padding:10px 14px;font:600 14px Poppins,Helvetica,Arial,sans-serif;cursor:pointer}\n#cp-gpa .go{margin-top:14px;width:100%;background:#0B2A4A;color:#fff;border:0;border-radius:10px;padding:14px;font:600 16px Poppins,Helvetica,Arial,sans-serif;cursor:pointer}\n#cp-gpa .res{margin-top:18px;border-radius:14px;padding:18px;display:none;background:#0B2A4A;color:#fff}\n#cp-gpa .res.on{display:block}\n#cp-gpa .big{font:700 44px Poppins,Helvetica,Arial,sans-serif;line-height:1;margin:4px 0 8px}\n#cp-gpa .res p{margin:6px 0;line-height:1.45}\n#cp-gpa .bar{height:10px;border-radius:6px;background:rgba(255,255,255,.18);margin:12px 0 4px;position:relative}\n#cp-gpa .fill{height:10px;border-radius:6px;background:#B5A21F}\n#cp-gpa .tick{position:absolute;top:-4px;width:2px;height:18px;background:#fff}\n#cp-gpa .ticks{display:flex;justify-content:space-between;font-size:12px;opacity:.85}\n#cp-gpa .cta{display:inline-block;margin-top:12px;background:#B5A21F;color:#fff;text-decoration:none;font:600 15px Poppins,Helvetica,Arial,sans-serif;padding:10px 16px;border-radius:8px;border:0;cursor:pointer}\n#cp-gpa .share{background:#fff;color:#0B2A4A;margin-left:6px}\n#cp-gpa .fine{font-size:12px;color:#5E7186;margin-top:14px;line-height:1.45}\n#cp-gpa .count{font-size:13px;color:#5E7186;margin-top:8px}\n@media (max-width:540px){#cp-gpa .row{grid-template-columns:1fr 1fr 24px;grid-template-areas:'s g x' 'l n .';row-gap:6px;padding-bottom:10px;border-bottom:1px solid #EEF3F8}#cp-gpa .row .s{grid-area:s}#cp-gpa .row .g{grid-area:g}#cp-gpa .row .l{grid-area:l}#cp-gpa .row .n{grid-area:n}#cp-gpa .row .x{grid-area:x}#cp-gpa .head{display:none}}\n</style>\n<div class=\"card\">\n  <h3>Bright Futures GPA Calculator</h3>\n  <p class=\"sub\">Florida's Bright Futures uses its own GPA: 16 core credits, weighted for Honors, AP, IB, AICE and dual enrollment. Add your student's core classes to see where they stand.</p>\n  <div class=\"row head\"><span>Subject</span><span>Grade</span><span>Level</span><span>Length</span><span></span></div>\n  <div id=\"gpa-rows\"></div>\n  <div class=\"btns\">\n    <button type=\"button\" class=\"ghost\" id=\"gpa-add\">+ Add a class</button>\n    <button type=\"button\" class=\"ghost\" id=\"gpa-sample\">Fill a 9th grade example</button>\n  </div>\n  <div class=\"count\" id=\"gpa-count\"></div>\n  <button type=\"button\" class=\"go\" id=\"gpa-go\">Calculate the Bright Futures GPA</button>\n  <div class=\"res\" id=\"gpa-res\" aria-live=\"polite\"></div>\n  <p class=\"fine\">How it works (Bright Futures Student Handbook, Chapter 1, Florida Department of Education): only the 16 core credits count (4 English, 4 math at or above Algebra I, 3 natural science, 3 social science, 2 sequential credits of the same world language). A = 4, B = 3, C = 2, D = 1, F = 0. Honors, AP, Pre-IB, IB, Pre-AICE, AICE and academic dual enrollment add 0.25 per semester course or 0.50 per year course. Students may use up to 2 additional credits from those areas (or AP/IB/AICE fine arts) to raise the GPA. Minimums: 3.50 for Academic Scholars, 3.00 for Medallion Scholars, plus test scores and service hours. This is an estimate, not an official evaluation; your school counselor can request the official one.</p>\n</div>\n\n</div>\n";

(function(){
  var SUBJ=['English','Math','Science','Social studies','World language','Extra (AP/IB/AICE fine arts or 5th core)'];
  var rows=document.getElementById('gpa-rows');
  function opt(list,sel){return list.map(function(o){return '<option'+(o[0]===sel?' selected':'')+' value="'+o[0]+'">'+o[1]+'</option>';}).join('');}
  function addRow(s,g,l,len){
    var d=document.createElement('div');d.className='row';
    d.innerHTML='<select class="s">'+opt(SUBJ.map(function(x){return [x,x];}),s||'English')+'</select>'+
      '<select class="g">'+opt([['4','A'],['3','B'],['2','C'],['1','D'],['0','F']],g||'4')+'</select>'+
      '<select class="l c3">'+opt([['0','Regular'],['1','Honors / AP / IB / AICE / DE']],l||'0')+'</select>'+
      '<select class="n c4">'+opt([['1','Full year'],['0.5','Semester']],len||'1')+'</select>'+
      '<button type="button" class="x" aria-label="Remove class">×</button>';
    d.querySelector('.x').addEventListener('click',function(){d.remove();count();});
    d.querySelectorAll('select').forEach(function(x){x.addEventListener('change',count);});
    rows.appendChild(d);count();
  }
  function count(){
    var c=0;rows.querySelectorAll('.row').forEach(function(r){c+=parseFloat(r.querySelector('.n').value);});
    document.getElementById('gpa-count').textContent=c+' credit'+(c===1?'':'s')+' added (a full Bright Futures GPA uses 16, up to 18).';
  }
  document.getElementById('gpa-add').addEventListener('click',function(){addRow();});
  document.getElementById('gpa-sample').addEventListener('click',function(){
    rows.innerHTML='';
    [['English','4','1','1'],['Math','3','1','1'],['Science','4','1','1'],['Social studies','4','0','1'],['World language','3','0','1']].forEach(function(r){addRow(r[0],r[1],r[2],r[3]);});
  });
  ['English','Math','Science','Social studies'].forEach(function(s){addRow(s);});
  document.getElementById('gpa-go').addEventListener('click',function(){
    var pts=0,cr=0;
    rows.querySelectorAll('.row').forEach(function(r){
      var g=parseFloat(r.querySelector('.g').value),w=parseFloat(r.querySelector('.l').value),n=parseFloat(r.querySelector('.n').value);
      pts+=(g+(w?0.5:0))*n;cr+=n;
    });
    var out=document.getElementById('gpa-res');
    if(!cr){out.className='res on';out.innerHTML='<p>Add at least one class first.</p>';return;}
    var gpa=Math.floor(pts/cr*100)/100, pct=Math.min(100,gpa/4.5*100), h;
    if(gpa>=3.5) h='<p><strong>At or above 3.50:</strong> on track for the Academic Scholars GPA (100% of tuition and applicable fees at Florida public colleges and universities).</p>';
    else if(gpa>=3.0) h='<p><strong>At or above 3.00:</strong> on track for the Medallion Scholars GPA (75% of tuition and applicable fees). '+(Math.ceil((3.5-gpa)*100)/100).toFixed(2)+' more to reach the Academic Scholars 3.50.</p>';
    else h='<p><strong>Below 3.00 for now.</strong> '+(Math.ceil((3.0-gpa)*100)/100).toFixed(2)+' to go for Medallion Scholars. Honors-level classes and strong grades in the remaining core classes can move this a lot.</p>';
    out.className='res on';
    out.innerHTML='<div style="font-size:14px;opacity:.85">Estimated Bright Futures GPA ('+cr+' credit'+(cr===1?'':'s')+')</div><div class="big">'+gpa.toFixed(2)+'</div>'+
      '<div class="bar"><div class="fill" style="width:'+pct+'%"></div><div class="tick" style="left:'+(3/4.5*100)+'%"></div><div class="tick" style="left:'+(3.5/4.5*100)+'%"></div></div>'+
      '<div class="ticks"><span>0</span><span>3.00 Medallion · 3.50 Academic</span><span>4.5</span></div>'+h+
      '<p style="font-size:14px;opacity:.9">GPA is only one piece: Bright Futures also needs a minimum SAT, ACT or CLT score, service or work hours, and the FFAA filed by Aug 31 after graduation.</p>'+
      '<a class="cta" href="https://collegeplan.beehiiv.com" target="_top">Free weekly Florida tips for your student\'s grade</a>'+
      '<button type="button" class="cta share" id="gpa-share">Send to another parent</button>';
    document.getElementById('gpa-share').addEventListener('click',function(){
      var u='https://collegeplan.beehiiv.com/bright-futures-gpa-calculator', t='Free Bright Futures GPA calculator for Florida parents';
      if(navigator.share){navigator.share({title:t,text:t,url:u}).catch(function(){});}
      else if(navigator.clipboard){navigator.clipboard.writeText(t+': '+u);this.textContent='Link copied!';}
    });
  });
})();

})();
