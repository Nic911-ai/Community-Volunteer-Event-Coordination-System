/* VolunteerHub - one script shared by every page. Data lives in localStorage (keys start with "vh_").
   localStorage = demo only: NOT secure login, and it does not sync between devices. */
const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const S={get:(k,d)=>{try{return JSON.parse(localStorage.getItem('vh_'+k))??d}catch(e){return d}},set:(k,v)=>localStorage.setItem('vh_'+k,JSON.stringify(v))};
const day=n=>{const x=new Date();x.setDate(x.getDate()+n);return x.toISOString().slice(0,10)};
const CATS={'Environmental Conservation':['🌳','#2e7d32'],'Animal Welfare':['🐶','#8d6e63'],'Food and Charity':['🍲','#ef6c00'],'Education':['📚','#1565c0'],'Elderly Support':['🧓','#6a1b9a'],'Community Development':['🌻','#558b2f'],'Health and Wellbeing':['💚','#00897b'],'Disaster Relief':['📦','#c62828'],'Youth Development':['🧑‍🎓','#283593'],'Fundraising':['🎗️','#ad1457']};
// [title, category, location, days from today, time, hours, places, level, description]
const RAW=[['Community Park Cleanup','Environmental Conservation','Riverside Park',5,'09:00',3,20,'Beginner','Pick up litter and tidy paths in a much-loved local park.'],
['Beach Cleanup Campaign','Environmental Conservation','Sandy Bay',9,'08:30',4,30,'Beginner','Help clear the shoreline and sort recycling.'],
['Animal Shelter Assistance','Animal Welfare','Happy Paws Shelter',6,'10:00',3,8,'Intermediate','Walk dogs, clean kennels and socialise cats.'],
['Community Food Bank','Food and Charity','Central Community Hall',3,'13:00',3,15,'Beginner','Sort and pack donated food for local families.'],
['Food Distribution Programme','Food and Charity','Northside Centre',12,'11:00',4,12,'Intermediate','Hand out meal packs and greet visitors warmly.'],
["Children's Reading Programme",'Education','Maple Library',7,'15:30',2,10,'Beginner','Read aloud with primary-school children.'],
['Digital Skills Tutoring','Education','Maple Library',14,'14:00',2,6,'Advanced','Teach basic computer and phone skills to adults.'],
['Elderly Care Home Visit','Elderly Support','Sunset Care Home',8,'14:00',2,10,'Beginner','Chat, play games and bring cheer to residents.'],
['Community Garden Project','Community Development','Green Lane Garden',10,'09:30',4,18,'Beginner','Plant beds and build compost bins together.'],
['Charity Health Awareness Event','Health and Wellbeing','Town Square',16,'10:00',5,14,'Intermediate','Run information stalls on healthy living.'],
['Emergency Donation Packing','Disaster Relief','Warehouse 4, Dockside',4,'09:00',4,25,'Beginner','Pack emergency kits for relief deliveries.'],
['Youth Mentorship Programme','Youth Development','Eastside Youth Club',18,'17:00',2,8,'Advanced','Mentor teenagers on study and career skills.'],
['Charity Fundraising Event','Fundraising','Grand Hall',21,'18:00',5,20,'Intermediate','Help run a fundraising evening: tickets, stalls and set-up.']];
const EV=RAW.map((r,i)=>({id:i+1,t:r[0],cat:r[1],loc:r[2],date:day(r[3]),time:r[4],dur:r[5],places:r[6],lvl:r[7],desc:r[8],feat:i==3}));
const org=e=>`${e.loc} Volunteer Team (fictional)`;
const ACH=[['First Step','Register for your first event',s=>[s.regs,1]],['Community Hero','Complete five events',s=>[s.done,5]],['Green Champion','Join three environmental activities',s=>[s.env,3]],['Helping Hand','Complete ten volunteer hours',s=>[s.hours,10]],['Super Volunteer','Complete twenty-five volunteer hours',s=>[s.hours,25]]];
const ACTIVE=['Submitted','Pending Review','Approved'];
const regs=()=>S.get('regs',[]),ev=id=>EV.find(e=>e.id==id);
const left=e=>e.places-regs().filter(r=>r.eventId==e.id&&ACTIVE.includes(r.status)).length;
const stats=()=>{const R=regs(),done=R.filter(r=>r.status=='Completed');return{regs:R.length,done:done.length,hours:done.reduce((a,r)=>a+ev(r.eventId).dur,0),env:R.filter(r=>r.status!='Cancelled'&&ev(r.eventId).cat==EV[0].cat).length,up:R.filter(r=>ACTIVE.includes(r.status)).length}};
function toast(m){const d=document.createElement('div');d.textContent=m;$('#toast').append(d);setTimeout(()=>d.remove(),3500)}
function note(m){const n=S.get('notes',[]);n.unshift({id:Date.now()+Math.random(),m,read:false,t:new Date().toLocaleString()});S.set('notes',n);nav()}
function check(){const s=stats(),got=S.get('ach',[]);ACH.forEach(a=>{const[c,t]=a[2](s);if(c>=t&&!got.includes(a[0])){got.push(a[0]);toast('🏆 Achievement unlocked: '+a[0]+'! Well done!');note('Achievement unlocked: '+a[0])}});S.set('ach',got)}
if(!S.get('init',0)){S.set('init',1);note('Welcome to VolunteerHub! (Demo notification - real alerts would need a backend and a notification service.)')}
const fav=()=>S.get('favs',[]);
function toggleFav(id){let f=fav();f=f.includes(id)?f.filter(x=>x!=id):[...f,id];S.set('favs',f);toast(f.includes(id)?'Added to favourites':'Removed from favourites')}
const days=d=>Math.ceil((new Date(d)-new Date(day(0)))/864e5);
const ban=(e,c='')=>`<div class="ban ${c}" style="background:linear-gradient(135deg,${CATS[e.cat][1]},#0b3d2e)">${CATS[e.cat][0]}</div>`;
const card=e=>`<div class="card">${ban(e)}<button class="heart" data-fav="${e.id}" aria-label="Favourite">${fav().includes(e.id)?'❤️':'🤍'}</button><div class="in"><span class="tag">${esc(e.cat)}</span><h3>${esc(e.t)}</h3><p>${esc(e.desc)}</p>
<small>📍 ${esc(e.loc)}<br>📅 ${e.date} ${e.time} · ⏱ ${e.dur}h · ${e.lvl}<br>👥 ${left(e)} places left</small><p><a class="btn sm out" href="event-details.html?id=${e.id}">View Details</a><a class="btn sm" href="register.html?id=${e.id}">Sign Up</a></p></div></div>`;
function nav(){const u=S.get('notes',[]).filter(n=>!n.read).length,P=document.body.dataset.page;
 const L=[['Home','index.html','home'],['Explore Events','events.html','events'],['My Registrations','my-registrations.html','regs'],['My Favourites','favourites.html','favs'],['My Profile','profile.html','profile'],['Notifications','notifications.html','notes']];
 $('#nav').innerHTML=`<nav><b>🌿 VolunteerHub</b><button id="burger" aria-label="Menu">☰</button><div class="links">${L.map(l=>`<a href="${l[1]}" class="${P==l[2]||(P=='details'&&l[2]=='events')||(P=='register'&&l[2]=='events')?'on':''}">${l[0]}${l[2]=='notes'&&u?` <span class="badge">${u}</span>`:''}</a>`).join('')}</div></nav>`;
 $('#burger').onclick=()=>$('.links').classList.toggle('open')}
document.addEventListener('click',e=>{const f=e.target.closest('[data-fav]');if(f){toggleFav(+f.dataset.fav);f.textContent=fav().includes(+f.dataset.fav)?'❤️':'🤍';if(document.body.dataset.page=='favs')V.favs()}});
const app=h=>$('#app').innerHTML=h,qid=()=>+new URLSearchParams(location.search).get('id');
const bad=()=>app('<div class="empty"><h2>Event not found</h2><a class="btn" href="events.html">Back to events</a></div>');
const V={
home(){const p=S.get('profile',{}),ints=p.interests||[],rec=EV.filter(e=>ints.includes(e.cat)).slice(0,3),f=EV.find(e=>e.feat),s=stats();
 app(`<section class="hero"><h1>Small Acts. Big Impact.</h1><p>Discover opportunities. Meet people. Make a difference.</p><a class="btn alt" href="events.html">Explore Opportunities</a><a class="btn" style="background:#ffb703;color:#000" href="profile.html">Join Our Community</a></section>
 <h2>⭐ Featured event of the week</h2><div class="grid">${card(f)}</div>
 ${rec.length?`<h2>Recommended for you</h2><div class="grid">${rec.map(card).join('')}</div>`:'<p class="empty">Pick your interests on <a href="profile.html">My Profile</a> to get recommendations.</p>'}
 <h2>Categories</h2><div class="grid">${Object.entries(CATS).map(([c,v])=>`<a class="panel" style="text-decoration:none;color:inherit" href="events.html?cat=${encodeURIComponent(c)}">${v[0]} <b>${c}</b></a>`).join('')}</div>
 <div class="stats"><div class="stat"><b>${EV.length}</b>Opportunities</div><div class="stat"><b>${1248+s.regs}</b>Volunteers registered*</div><div class="stat"><b>86</b>Events completed*</div><div class="stat"><b>${5420+s.hours}</b>Volunteer hours*</div></div><small>*Fictional demonstration data.</small>`)},
events(){const st={view:'grid'},P=new URLSearchParams(location.search);const opt=(a,l)=>`<option value="">${l}</option>`+[...new Set(a)].map(x=>`<option>${esc(x)}</option>`).join('');
 app(`<h1>Explore Events</h1><div class="filters"><input id="q" placeholder="🔍 Search..."><select id="cat">${opt(EV.map(e=>e.cat),'All categories')}</select><select id="loc">${opt(EV.map(e=>e.loc),'All locations')}</select><input type="date" id="dt" title="On or after"><select id="lvl">${opt(EV.map(e=>e.lvl),'Any level')}</select>
 <select id="sort"><option value="date">Sort: upcoming date</option><option value="places">Sort: most places</option></select><button class="btn sm out" id="vw">Grid / List</button><button class="btn sm red" id="clr">Clear filters</button></div><div id="res"></div>`);
 if(P.get('cat'))$('#cat').value=P.get('cat');
 const draw=()=>{let r=EV.filter(e=>(e.t+e.desc+e.cat).toLowerCase().includes($('#q').value.toLowerCase())&&(!$('#cat').value||e.cat==$('#cat').value)&&(!$('#loc').value||e.loc==$('#loc').value)&&(!$('#dt').value||e.date>=$('#dt').value)&&(!$('#lvl').value||e.lvl==$('#lvl').value));
  r.sort($('#sort').value=='date'?(a,b)=>a.date.localeCompare(b.date):(a,b)=>left(b)-left(a));
  $('#res').innerHTML=r.length?`<div class="${st.view}">${r.map(card).join('')}</div>`:'<div class="empty">😕 No events match your filters. Try clearing them!</div>'};
 $$('.filters input,.filters select').forEach(i=>i.oninput=draw);$('#vw').onclick=()=>{st.view=st.view=='grid'?'list':'grid';draw()};$('#clr').onclick=()=>{$$('.filters input,.filters select').forEach(i=>i.value=i.id=='sort'?'date':'');draw()};draw()},
details(){const e=ev(qid());if(!e)return bad();const c=e.cat;
 app(`<p class="crumb"><a href="index.html">Home</a> › <a href="events.html">Events</a> › ${esc(e.t)}</p><button class="btn sm out" onclick="history.back()">← Back</button>${ban(e,'big')}<span class="tag">${esc(c)}</span><h1>${esc(e.t)}</h1><p>${esc(e.desc)} Join a friendly team and make a real difference in your community.</p>
 <div class="panel">📅 ${e.date} at ${e.time} · ⏱ ${e.dur} hours · 📍 ${esc(e.loc)} · Level: ${e.lvl}<br>👥 <b>${left(e)}</b> of ${e.places} places left · ⏳ Starts in ${days(e.date)} days</div>
 <div class="panel"><h3>Responsibilities</h3><ul><li>Follow the team leader's instructions</li><li>Help set up and pack away</li><li>Support participants kindly</li></ul><h3>Skills required</h3><p>${e.lvl=='Advanced'?'Prior experience helpful':'No experience needed - just enthusiasm'}</p><h3>What to bring</h3><p>Water, comfortable clothes, a positive attitude.</p>
 <h3>Organiser</h3><p>${esc(org(e))}</p><h3>Registration requirements</h3><p>Name, email, contact number and availability. Submitting does <b>not</b> guarantee a place.</p></div>
 <a class="btn" href="register.html?id=${e.id}">Register for This Event</a><button class="btn out" data-fav="${e.id}">${fav().includes(e.id)?'❤️ In favourites':'🤍 Add to Favourites'}</button>`)},
register(){const e=ev(qid());if(!e)return bad();const p=S.get('profile',{}),R=regs().find(r=>r.eventId==e.id&&r.status!='Cancelled'&&r.status!='Rejected');
 if(R)return app(`<div class="empty"><h2>You have already registered for ${esc(e.t)}</h2><p>Status: ${R.status}</p><a class="btn" href="my-registrations.html">View My Registrations</a></div>`);
 if(left(e)<=0)return app('<div class="empty"><h2>Sorry, this event is full</h2><a class="btn" href="events.html">Explore more events</a></div>');
 app(`<h1>Sign up: ${esc(e.t)}</h1><form class="panel" id="f" novalidate><label>Full name *<input name="name" value="${esc(p.name)}"></label><span class="err" data-e="name"></span><label>Email *<input name="email" type="email" value="${esc(p.email)}"></label><span class="err" data-e="email"></span>
 <label>Contact number *<input name="phone" value="${esc(p.phone)}"></label><span class="err" data-e="phone"></span><label>Availability *<input name="avail" value="${esc(p.avail)}" placeholder="e.g. Weekends"></label><span class="err" data-e="avail"></span>
 <label>Skills / experience (optional)<textarea name="skills">${esc(p.skills)}</textarea></label><label>Comments (optional)<textarea name="comments"></textarea></label><button class="btn">Submit registration</button></form>`);
 $('#f').onsubmit=ev2=>{ev2.preventDefault();const d=Object.fromEntries(new FormData(ev2.target)),E={};
  ['name','email','phone','avail'].forEach(k=>{if(!d[k].trim())E[k]='This field is required.'});if(!E.email&&!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(d.email))E.email='Enter a valid email address.';if(!E.phone&&!/^[0-9+() -]{6,}$/.test(d.phone))E.phone='Enter a valid phone number.';
  $$('.err').forEach(x=>x.textContent=E[x.dataset.e]||'');if(Object.keys(E).length)return;if(!confirm('Submit your registration for '+e.t+'?'))return;
  const r={id:Date.now(),eventId:e.id,...d,date:new Date().toLocaleDateString(),status:'Submitted'};S.set('regs',[...regs(),r]);note('Registration submitted for '+e.t);check();
  app(`<div class="empty"><div style="font-size:4rem">🎉</div><h1>You're one step closer to making a difference!</h1><div class="panel"><p><b>${esc(e.t)}</b><br>Registered on ${r.date}<br>Status: <span class="tag">Submitted</span> (recorded in this demo - not yet approved)</p></div><a class="btn" href="my-registrations.html">View My Registrations</a><a class="btn out" href="events.html">Explore more events</a></div>`)}},
regs(){const s=stats(),R=regs(),F=new URLSearchParams(location.search).get('s')||'';
 const row=r=>{const e=ev(r.eventId);return`<div class="card"><div class="in"><span class="tag">${r.status}</span><h3>${esc(e.t)}</h3><small>📅 ${e.date} · 📍 ${esc(e.loc)} · ⏱ ${e.dur}h${ACTIVE.includes(r.status)?` · starts in ${days(e.date)} days`:''}</small><p>
 <a class="btn sm out" href="event-details.html?id=${e.id}">View Details</a>${ACTIVE.includes(r.status)?`<button class="btn sm red" data-c="${r.id}">Cancel</button>`:''}
 ${r.status=='Submitted'?`<button class="btn sm" data-a="${r.id}">Demo: send to review</button>`:''}${r.status=='Pending Review'?`<button class="btn sm" data-a="${r.id}">Demo: approve</button><button class="btn sm red" data-r="${r.id}">Demo: reject</button>`:''}${r.status=='Approved'?`<button class="btn sm" data-a="${r.id}">Demo: mark completed</button>`:''}</p></div></div>`};
 app(`<h1>My Registrations</h1><div class="stats"><div class="stat"><b>${s.regs}</b>Total</div><div class="stat"><b>${s.up}</b>Upcoming</div><div class="stat"><b>${s.done}</b>Completed</div><div class="stat"><b>${s.hours}</b>Hours</div></div>
 <div class="filters"><select id="sf"><option value="">All statuses</option>${['Submitted','Pending Review','Approved','Rejected','Cancelled','Completed'].map(x=>`<option ${F==x?'selected':''}>${x}</option>`).join('')}</select></div>
 <p><small>Demo status flow: Submitted → Pending Review → Approved/Rejected → Completed. "Demo" buttons simulate an organiser; no real approval happens.</small></p>
 <div class="grid">${R.filter(r=>!F||r.status==F).map(row).join('')||'<div class="empty">No registrations here yet. <a href="events.html">Find an event!</a></div>'}</div>`);
 $('#sf').onchange=e=>location.search='?s='+encodeURIComponent(e.target.value);
 const upd=(id,fn)=>{const a=regs();fn(a.find(r=>r.id==id));S.set('regs',a);check();V.regs()};
 $$('[data-c]').forEach(b=>b.onclick=()=>{if(confirm('Cancel this registration? This cannot be undone.'))upd(b.dataset.c,r=>{r.status='Cancelled';note('Registration cancelled: '+ev(r.eventId).t);toast('Registration cancelled.')})});
 $$('[data-a]').forEach(b=>b.onclick=()=>upd(b.dataset.a,r=>{r.status={Submitted:'Pending Review','Pending Review':'Approved',Approved:'Completed'}[r.status];note('Status changed to '+r.status+': '+ev(r.eventId).t)}));
 $$('[data-r]').forEach(b=>b.onclick=()=>upd(b.dataset.r,r=>{r.status='Rejected';note('Status changed to Rejected: '+ev(r.eventId).t)}))},
favs(){const f=EV.filter(e=>fav().includes(e.id));app(`<h1>My Favourites</h1>${f.length?`<div class="grid">${f.map(card).join('')}</div>`:'<div class="empty">💚 No favourites yet. Tap the heart on any event.<br><a class="btn" href="events.html">Explore Events</a></div>'}`)},
profile(){const p=S.get('profile',{}),s=stats(),got=S.get('ach',[]),nx=ACH.find(a=>!got.includes(a[0])),pr=nx&&nx[2](s);
 app(`<h1>My Profile</h1><div class="panel"><div style="font-size:3rem">👤</div><b>${s.regs}</b> events joined · <b>${s.hours}</b> volunteer hours
 ${nx?`<p>Next badge: <b>${nx[0]}</b> - ${nx[1]} (${Math.min(pr[0],pr[1])}/${pr[1]})</p><div class="bar"><i style="width:${Math.min(100,pr[0]/pr[1]*100)}%"></i></div>`:'<p>🏆 All badges earned - amazing!</p>'}</div>
 <div class="grid">${ACH.map(a=>`<div class="panel ${got.includes(a[0])?'earned':''}">${got.includes(a[0])?'🏅':'🔒'} <b>${a[0]}</b><br><small>${a[1]}</small></div>`).join('')}</div>
 <form class="panel" id="pf"><label>Full name<input name="name" value="${esc(p.name)}"></label><label>Email<input name="email" type="email" value="${esc(p.email)}"></label><label>Contact number<input name="phone" value="${esc(p.phone)}"></label>
 <label>About me<textarea name="bio">${esc(p.bio)}</textarea></label><label>Skills<input name="skills" value="${esc(p.skills)}"></label><label>Preferred availability<input name="avail" value="${esc(p.avail)}"></label>
 <label>Interests</label>${Object.keys(CATS).map(c=>`<label style="font-weight:400"><input type="checkbox" name="int" value="${c}" ${(p.interests||[]).includes(c)?'checked':''} style="width:auto"> ${c}</label>`).join('')}<br><button class="btn">Save profile</button></form>
 <div class="panel"><small>Data is stored only in this browser (localStorage). It is not secure and does not sync across devices.</small><br><button class="btn red sm" id="rs">Reset demo data</button></div>`);
 $('#pf').onsubmit=e=>{e.preventDefault();const f=new FormData(e.target),d=Object.fromEntries(f);if(d.email&&!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(d.email))return toast('Please enter a valid email.');d.interests=f.getAll('int');delete d.int;S.set('profile',d);toast('Profile saved ✔')};
 $('#rs').onclick=()=>{if(confirm('Delete all demo data?')){Object.keys(localStorage).filter(k=>k.startsWith('vh_')).forEach(k=>localStorage.removeItem(k));location.reload()}}},
notes(){const n=S.get('notes',[]);app(`<h1>Notifications</h1><p><small>Demo notifications only - no emails or SMS are sent. Real ones need a backend and a notification service.</small></p><button class="btn sm out" id="all">Mark all as read</button>
 ${n.map(x=>`<div class="panel ${x.read?'':'unread'}">${esc(x.m)}<br><small>${x.t}</small> ${x.read?'':`<button class="btn sm" data-n="${x.id}">Mark read</button>`}</div>`).join('')||'<div class="empty">All quiet for now.</div>'}`);
 const sv=f=>{S.set('notes',n.map(x=>f(x)));nav();V.notes()};$('#all').onclick=()=>sv(x=>({...x,read:true}));$$('[data-n]').forEach(b=>b.onclick=()=>sv(x=>x.id==b.dataset.n?{...x,read:true}:x))}};
nav();check();V[document.body.dataset.page]();
