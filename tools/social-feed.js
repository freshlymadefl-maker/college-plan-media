// College Plan: latest Instagram posts widget. Reads social/feed.json (refreshed daily) from GitHub.
(function(){
var BASE="https://raw.githubusercontent.com/freshlymadefl-maker/college-plan-media/main/";
var root=document.getElementById("cp-social-root")||document.currentScript.parentNode;
var css="#cp-soc{font-family:Inter,Helvetica,Arial,sans-serif;max-width:980px;margin:0 auto;color:#1F2D3D}"+
"#cp-soc *{box-sizing:border-box}"+
"#cp-soc .g{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}"+
"#cp-soc a.t{position:relative;display:block;aspect-ratio:4/5;border-radius:14px;overflow:hidden;background:#EAF3FB;box-shadow:0 6px 18px rgba(11,42,74,.10);text-decoration:none}"+
"#cp-soc a.t img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .35s}"+
"#cp-soc a.t:hover img{transform:scale(1.04)}"+
"#cp-soc a.t .d{position:absolute;left:10px;top:10px;background:rgba(255,255,255,.92);color:#0B2A4A;font:600 12px Inter,Helvetica,Arial,sans-serif;padding:5px 9px;border-radius:999px}"+
"#cp-soc .b{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-top:22px}"+
"#cp-soc .b a{display:inline-flex;align-items:center;gap:8px;text-decoration:none;font:600 15px Poppins,Helvetica,Arial,sans-serif;padding:12px 20px;border-radius:10px}"+
"#cp-soc .ig{background:#0B2A4A;color:#fff}#cp-soc .fb{background:#fff;color:#0B2A4A;border:1px solid #C9D8E8}"+
"#cp-soc svg{width:18px;height:18px}"+
"@media (max-width:640px){#cp-soc .g{grid-template-columns:repeat(2,1fr);gap:10px}}";
var IG='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg>';
var FB='<svg viewBox="0 0 24 24" fill="currentColor"><path d="M14 8h3V4h-3c-2.8 0-4 1.8-4 4.3V10H7v4h3v8h4v-8h3l1-4h-4V8.6c0-.4.3-.6.6-.6z"/></svg>';
function esc(s){return String(s||"").replace(/[&<>"]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c];});}
function render(f){
  var p=(f.posts||[]); var n=p.length>=8?8:(p.length>=4?4:p.length); p=p.slice(0,n);
  var h='<style>'+css+'</style><div id="cp-soc">';
  if(p.length){h+='<div class="g">'+p.map(function(x){return '<a class="t" href="'+esc(x.url)+'" target="_blank" rel="noopener" title="'+esc(x.caption)+'"><img src="'+BASE+esc(x.img)+'" alt="'+esc(x.caption)+'" onerror="this.parentNode.style.display=\'none\'"><span class="d">'+esc(x.label)+'</span></a>';}).join("")+'</div>';}
  h+='<div class="b"><a class="ig" href="'+esc(f.instagram||"https://www.instagram.com/college.plan/")+'" target="_blank" rel="noopener">'+IG+'Follow @college.plan</a><a class="fb" href="'+esc(f.facebook||"https://www.facebook.com/1362425533621807")+'" target="_blank" rel="noopener">'+FB+'Facebook</a></div></div>';
  root.innerHTML=h;
}
fetch(BASE+"social/feed.json?t="+Math.floor(Date.now()/600000)).then(function(r){return r.json();}).then(render).catch(function(){render({posts:[]});});
})();
