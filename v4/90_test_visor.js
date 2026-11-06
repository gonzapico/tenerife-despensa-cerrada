// Pruebas del visor: 0 conexiones externas, 0 errores de consola, sin scroll horizontal en móvil, escenas renderizadas.
const { chromium } = require('playwright'); const path=require('path'); const fs=require('fs');
(async()=>{
  const file='file://'+path.resolve(process.argv[2]); const out=[]; let ext=[], errs=[];
  const browser=await chromium.launch({args:['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist']});
  for (const [name,vp] of [['desktop',{width:1280,height:900}],['movil',{width:390,height:844}]]){
    const ctx=await browser.newContext({viewport:vp,deviceScaleFactor:1}); const page=await ctx.newPage();
    page.on('request',r=>{ if(!r.url().startsWith('file:')&&!r.url().startsWith('data:')&&!r.url().startsWith('blob:')) ext.push(r.url()); });
    page.on('console',m=>{ if(m.type()==='error') errs.push(name+': '+m.text()); });
    page.on('pageerror',e=>errs.push(name+': '+e.message));
    await page.goto(file); await page.waitForTimeout(2500);
    const r=await page.evaluate(()=>({
      scrollW:document.documentElement.scrollWidth, innerW:window.innerWidth,
      chips:document.querySelectorAll('#rejilla .chip').length, pisos:document.querySelectorAll('#tabPisos tr[data-p]').length,
      plan:document.querySelectorAll('#tabPlan tbody tr').length, nevera:document.querySelectorAll('#neveraSvg .prod').length, despensa:document.querySelectorAll('#despensaSvg .prod').length,
      zonas:document.querySelectorAll('#tabZonas tbody tr').length, canvas:!!document.querySelector('#isla3d canvas'), frames: (window.ISLA&&ISLA.frames)||0,
      check1:document.getElementById('checkC1').textContent, check4:document.getElementById('checkC4').textContent, cob:document.getElementById('cobertura').textContent.slice(0,200), calibra:document.getElementById('calibra').textContent}));
    r.name=name; out.push(r);
    await page.screenshot({path:`cap_${name}_1.png`,fullPage:false});
    if(name==='desktop'){ await page.evaluate(()=>document.getElementById('reparto').scrollIntoView()); await page.waitForTimeout(400); await page.screenshot({path:'cap_desktop_4.png'}); await page.evaluate(()=>document.getElementById('nevera').scrollIntoView()); await page.waitForTimeout(400); await page.screenshot({path:'cap_desktop_5.png'}); }
    await ctx.close();
  }
  await browser.close();
  const res={externas:ext.length,ext:ext.slice(0,5),errores:errs.length,errs:errs.slice(0,5),vistas:out};
  console.log(JSON.stringify(res,null,1)); fs.writeFileSync('90_test_resultado.json',JSON.stringify(res,null,1));
})();
