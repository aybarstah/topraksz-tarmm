import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sablon.reel import render_reel, page

body = """
<div class="hook" id="hook">Balık kakasıyla<br>marul yetişir mi?<u></u></div>
<svg id="ill" width="1080" height="760" viewBox="0 0 1080 760" style="position:absolute;top:560px;left:0">
 <!-- bakteri zinciri -->
 <g id="chain" font-family="Poppins" font-weight="800" text-anchor="middle">
  <g id="c1"><rect x="90" y="60" width="240" height="110" rx="55" fill="#FFF9EE" stroke="#E3D3B8" stroke-width="6"/><text x="210" y="132" font-size="52" fill="#B5543A">NH₃</text></g>
  <g id="a1"><text x="395" y="132" font-size="60" fill="#3C6E3A">→</text><text x="395" y="50" font-size="54">🦠</text></g>
  <g id="c2"><rect x="420" y="60" width="240" height="110" rx="55" fill="#FFF9EE" stroke="#E3D3B8" stroke-width="6" transform="translate(40,0)"/><text x="580" y="132" font-size="52" fill="#C9962C">NO₂⁻</text></g>
  <g id="a2"><text x="765" y="132" font-size="60" fill="#3C6E3A">→</text><text x="765" y="50" font-size="54">🦠</text></g>
  <g id="c3"><rect x="815" y="60" width="240" height="110" rx="55" fill="#DDEBCF" stroke="#9CCB7E" stroke-width="6"/><text x="935" y="132" font-size="52" fill="#2F5D2D">NO₃⁻</text></g>
 </g>
 <!-- borular -->
 <path id="p1" d="M500 300 C560 210 600 220 640 330" stroke="#9CC8C9" stroke-width="22" fill="none" stroke-linecap="round"/>
 <path id="p2" d="M860 420 C860 690 560 720 330 590" stroke="#9CC8C9" stroke-width="22" fill="none" stroke-linecap="round"/>
 <path id="f1" d="M500 300 C560 210 600 220 640 330" stroke="#3C8FA0" stroke-width="10" fill="none" stroke-dasharray="22 26" stroke-linecap="round"/>
 <path id="f2" d="M860 420 C860 690 560 720 330 590" stroke="#3C8FA0" stroke-width="10" fill="none" stroke-dasharray="22 26" stroke-linecap="round"/>
 <!-- tank -->
 <rect x="70" y="290" width="450" height="300" rx="26" fill="#BFDDDD" stroke="#7A6A52" stroke-width="7"/>
 <rect x="70" y="290" width="450" height="40" rx="20" fill="#A7D0D0"/>
 <g id="fishA"><ellipse rx="70" ry="34" fill="#E58A3A"/><path d="M64 0 L116 -34 L116 34 Z" fill="#E58A3A"/><circle cx="-38" cy="-8" r="8" fill="#2E3B2A"/></g>
 <g id="fishB"><ellipse rx="50" ry="24" fill="#C9962C"/><path d="M46 0 L84 -24 L84 24 Z" fill="#C9962C"/><circle cx="-27" cy="-6" r="6" fill="#2E3B2A"/></g>
 <g id="amm" font-family="Poppins" font-weight="800" font-size="34" fill="#B5543A"></g>
 <!-- yetiştirme yatağı -->
 <rect x="600" y="330" width="420" height="90" rx="18" fill="#B59A6E"/>
 <g id="lets"></g>
</svg>
<div class="cap" id="cap"></div>
"""

js = r"""
const caps=[
 [0,3.2,"Cevap: <span class='hl'>evet!</span> 🐟🥬"],
 [3.2,7.2,"Balık suya <span class='hl'>amonyak</span> bırakır.<br>Bu, balık için zehirlidir."],
 [7.2,11.4,"Bakteriler onu önce <b>nitrite</b>,<br>sonra <span class='hl'>nitrata</span> çevirir."],
 [11.4,15.4,"Marul nitratı kökünden alır,<br>temiz su balığa <span class='hl'>geri döner.</span>"],
 [15.4,99,"Bunun adı <span class='hl'>akuaponik</span>.<br>Sen dener miydin? 👇"]];
const cl=(x)=>Math.max(0,Math.min(1,x));
const ease=(x)=>1-Math.pow(1-cl(x),3);
const $=(id)=>document.getElementById(id);
// marullar
const L=$('lets'); const NS='http://www.w3.org/2000/svg';
[700,810,920].forEach((x,i)=>{const g=document.createElementNS(NS,'g');g.setAttribute('id','l'+i);
 g.innerHTML=`<ellipse cx="-38" cy="-30" rx="40" ry="52" fill="#7DB862" transform="rotate(-25 -38 -30)"/><ellipse cx="38" cy="-30" rx="40" ry="52" fill="#7DB862" transform="rotate(25 38 -30)"/><ellipse cx="0" cy="-50" rx="42" ry="62" fill="#5E9B4F"/><line x1="0" y1="0" x2="0" y2="80" stroke="#E8DCC4" stroke-width="5"/><line x1="-14" y1="10" x2="-24" y2="70" stroke="#E8DCC4" stroke-width="4"/><line x1="14" y1="10" x2="24" y2="70" stroke="#E8DCC4" stroke-width="4"/>`;
 g.dataset.x=x; L.appendChild(g);});
// amonyak kabarcıkları
const A=$('amm');
for(let i=0;i<6;i++){const t=document.createElementNS(NS,'text');t.textContent='NH₃';t.setAttribute('id','n'+i);A.appendChild(t);}
let lastCap=-1;
function render(t){
 // hook girişi
 const h=$('hook'); h.style.opacity=ease(t/0.5); h.style.transform=`translateY(${(1-ease(t/0.5))*40}px)`;
 // balıklar yüzer
 $('fishA').setAttribute('transform',`translate(${230+70*Math.sin(t*1.3)},${440+12*Math.sin(t*2.6)}) scale(${Math.cos(t*1.3)>0?1:-1},1)`);
 $('fishB').setAttribute('transform',`translate(${380-60*Math.sin(t*1.1+1)},${520+10*Math.sin(t*2.2)}) scale(${-Math.cos(t*1.1+1)>0?1:-1},1)`);
 // amonyak (3.2–8)
 for(let i=0;i<6;i++){const n=$('n'+i); const st=3.4+i*0.55; const p=(t-st)/2.2;
  const vis=(t>st && t<8.2)?1:0; const y=500-p*190; const x=120+i*62;
  n.setAttribute('x',x); n.setAttribute('y',y); n.setAttribute('opacity',vis*Math.min(1,cl(p*4))*(p<1?1:Math.max(0,1-(p-1)*3)));}
 // zincir (7.2–15.4)
 const seq=[['c1',7.3],['a1',8.1],['c2',8.7],['a2',9.5],['c3',10.1]];
 seq.forEach(([id,s])=>{const e=$(id); const k=ease((t-s)/0.4); const out=t>15.6?Math.max(0,1-(t-15.6)/0.4):1;
  e.setAttribute('opacity',k*out); e.setAttribute('transform',`translate(0,${(1-k)*30})`);});
 // su akışı her zaman, 11.4 sonrası hızlı ve belirgin
 const flow=t>11.4?1:0.35;
 ['f1','f2'].forEach(id=>{$(id).setAttribute('stroke-dashoffset',-t*90); $(id).setAttribute('opacity',flow);});
 // marul büyür (11.4–15)
 [0,1,2].forEach(i=>{const g=$('l'+i); const k=0.45+0.55*ease((t-11.6-i*0.3)/2.4);
  g.setAttribute('transform',`translate(${g.dataset.x},335) scale(${k})`);});
 // altyazı
 const ci=caps.findIndex(c=>t>=c[0]&&t<c[1]); const c=$('cap');
 if(ci!==lastCap){c.innerHTML=caps[ci][2]; lastCap=ci;}
 const k=ease((t-caps[ci][0])/0.3); c.style.opacity=k; c.style.transform=`translateY(${(1-k)*24}px) scale(${0.96+0.04*k})`;
}
render(0);
"""

if __name__ == "__main__":
    render_reel(page(body, js), "gun9/akuaponik_reel", sure=18, fps=30)
