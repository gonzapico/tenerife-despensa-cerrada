const { chromium } = require('playwright'); const path=require('path');
(async()=>{ const file='file://'+path.resolve(process.argv[2]); let ext=[],errs=[]; const b=await chromium.launch(); const out=[];
 for (const [n,vp] of [['desktop',{width:1280,height:900}],['movil',{width:390,height:844}]]){ const c=await b.newContext({viewport:vp}); const p=await c.newPage();
  p.on('request',r=>{ if(!r.url().startsWith('file:')&&!r.url().startsWith('data:')) ext.push(r.url()); }); p.on('console',m=>{ if(m.type()==='error') errs.push(m.text()); }); p.on('pageerror',e=>errs.push(e.message));
  await p.goto(file); await p.waitForTimeout(800);
  const r=await p.evaluate(()=>({scrollW:document.documentElement.scrollWidth,innerW:innerWidth,tabs:document.querySelectorAll('#tabs button').length,kpis:[...document.querySelectorAll('.kpi b')].map(e=>e.textContent),bars:document.querySelectorAll('.bar-row').length}));
  r.n=n; out.push(r); await p.screenshot({path:`cap_pend_${n}.png`});
  if(n==='desktop'){ await p.click('#tabs button:nth-child(9)'); await p.waitForTimeout(300); const q=await p.evaluate(()=>({preg:document.querySelectorAll('fieldset.q').length,txt:document.getElementById('qtxt').textContent.length})); out.push(q); await p.click('#tabs button:nth-child(10)'); await p.waitForTimeout(300); const pr=await p.evaluate(()=>document.getElementById('ptxt').textContent.length); out.push({prompt:pr}); await p.screenshot({path:'cap_pend_reinicio.png'}); }
  await c.close(); }
 await b.close(); console.log(JSON.stringify({ext:ext.length,errs,out})); })();
