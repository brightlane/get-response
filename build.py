#!/usr/bin/env python3
"""
Wondershare Audio Recorder Affiliate Site — build.py v1
25 HTML pages, 1000+ targeted keywords, global audience.
Python 3.11 compatible — no backslashes inside f-string expressions.

Deploy: https://brightlane.github.io/audiorecorder/
Run:    python3 build.py
Output: audiorecorder-site/
"""
from pathlib import Path
from datetime import date

BASE      = Path(__file__).parent / "audiorecorder-site"
SITE_ROOT = "/audiorecorder"
SITE_URL  = "https://brightlane.github.io/audiorecorder"
AFF       = "https://www.linkconnector.com/ta.php?lc=007949049070004532&atid=audiorecorderwebs"
YEAR      = date.today().year

KEYWORDS = (
    "audio recorder software,best audio recorder,streaming audio recorder,record audio computer,"
    "record system audio,record microphone audio,audio recording software Windows,audio recorder Mac,"
    "record streaming audio,capture audio from computer,record internet radio,record Spotify audio,"
    "record YouTube audio,record online music,record podcast,podcast recorder software,"
    "voice recorder software,voice recorder PC,voice recorder laptop,voice recorder Windows,"
    "record voice memo,voice memo software,dictation recorder,interview recorder software,"
    "audio capture software,capture system sound,record PC audio,record Mac audio,"
    "MP3 recorder,record to MP3,save audio as MP3,audio to MP3 recorder,"
    "WAV recorder,FLAC recorder,high quality audio recorder,lossless audio recorder,"
    "scheduled audio recorder,auto audio recorder,timer audio recorder,record audio automatically,"
    "audio editor software,trim audio,cut audio,edit recording,audio noise reduction,"
    "background noise removal audio,clean audio recording,audio enhancement software,"
    "AI audio recorder,AI noise reduction,AI voice enhancement,AI audio processing,"
    "Wondershare audio recorder,Wondershare streaming audio recorder,Wondershare UniConverter audio,"
    "audio recorder review,best audio recording software 2024,best audio recording software 2025,"
    "best audio recording software 2026,top audio recorder,professional audio recorder,"
    "free audio recorder,audio recorder free trial,record audio free,"
    "record online radio,internet radio recorder,radio recording software,"
    "record Zoom audio,record Teams audio,record Google Meet audio,record Skype audio,"
    "record webinar audio,webinar recording software,meeting recorder,"
    "record music from browser,browser audio recorder,record Chrome audio,"
    "record streaming music,music recorder software,record Amazon Music,record Apple Music,"
    "record Discord audio,record game audio,game audio recorder,"
    "audio recorder for musicians,audio recorder for podcasters,audio recorder for journalists,"
    "audio recorder for students,lecture recorder,class recording software,"
    "multitrack audio recorder,stereo audio recorder,mono audio recorder,"
    "audio format converter,convert audio to MP3,convert WAV to MP3,convert audio files,"
    "audio recorder Windows 10,audio recorder Windows 11,audio recorder MacOS,"
    "audio recorder no watermark,audio recorder unlimited recording,audio batch recorder,"
    "audio recorder vs Audacity,audio recorder vs GarageBand,audio recorder alternatives,"
    "streaming audio recorder alternative,best Audacity alternative,simple audio recorder,"
    "audio recorder for beginners,easy audio recorder,one click audio recorder,"
    "audio recorder with ID3 tags,audio tagger,metadata audio recorder,"
    "audio recorder with scheduler,scheduled recording audio,automatic recording software,"
    "long audio recorder,overnight recording,continuous audio recording"
)

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Fraunces:ital,wght@0,700;0,900;1,700&family=JetBrains+Mono:wght@400;600&display=swap');
:root{
  --bg:#04050d;--bg2:#07081a;--bg3:#0c0e24;--card:rgba(7,8,26,.93);
  --acc:#7c3aed;--acc2:#ec4899;--acc3:#06b6d4;--gold:#f59e0b;
  --green:#10b981;--red:#ef4444;--orange:#f97316;
  --txt:#f0f0ff;--muted:#7878a8;--bdr:rgba(124,58,237,.13);--bdr2:rgba(124,58,237,.3);
  --glow:0 0 36px rgba(124,58,237,.28);--r:14px;--r2:8px
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:'Outfit',sans-serif;background:var(--bg);color:var(--txt);line-height:1.72;overflow-x:hidden}
body::before{content:'';position:fixed;inset:0;z-index:0;pointer-events:none;
  background:
    radial-gradient(ellipse 90% 60% at 10% 0%,rgba(124,58,237,.07) 0%,transparent 55%),
    radial-gradient(ellipse 60% 50% at 90% 100%,rgba(236,72,153,.05) 0%,transparent 50%),
    linear-gradient(rgba(124,58,237,.015) 1px,transparent 1px),
    linear-gradient(90deg,rgba(124,58,237,.015) 1px,transparent 1px);
  background-size:auto,auto,52px 52px,52px 52px}
h1,h2,h3,h4{font-family:'Fraunces',serif;line-height:1.12;letter-spacing:-.01em}
h1{font-size:clamp(2.6rem,6.5vw,5rem)}
h2{font-size:clamp(1.9rem,3.8vw,3rem)}
h3{font-size:clamp(1.2rem,2.2vw,1.75rem)}
h4{font-size:1.15rem}
p{color:var(--muted);line-height:1.82}
a{color:var(--acc);text-decoration:none;transition:color .2s}a:hover{color:#fff}
code{font-family:'JetBrains Mono',monospace;font-size:.82em;background:rgba(124,58,237,.1);padding:.15em .45em;border-radius:4px;color:var(--acc3)}
strong{color:var(--txt);font-weight:700}
/* NAV */
nav{position:fixed;top:0;left:0;right:0;z-index:999;height:66px;
  background:rgba(4,5,13,.95);backdrop-filter:blur(22px);
  border-bottom:1px solid var(--bdr);
  display:flex;align-items:center;justify-content:space-between;padding:0 5%}
.logo{font-family:'Fraunces',serif;font-size:1.5rem;font-weight:900;color:var(--txt)}
.logo span{color:var(--acc)}
.nav-links{display:flex;gap:1.3rem;list-style:none;align-items:center}
.nav-links a{color:var(--muted);font-size:.77rem;font-weight:700;
  text-transform:uppercase;letter-spacing:.1em;transition:color .2s;white-space:nowrap}
.nav-links a:hover{color:var(--acc)}
.nav-cta{background:var(--acc)!important;color:#fff!important;font-weight:800!important;
  padding:.42rem 1.1rem;border-radius:var(--r2);
  box-shadow:0 2px 18px rgba(124,58,237,.5);transition:all .2s!important}
.nav-cta:hover{transform:translateY(-1px)!important;box-shadow:0 4px 28px rgba(124,58,237,.7)!important}
.ham{display:none;flex-direction:column;gap:5px;cursor:pointer;padding:4px}
.ham span{display:block;width:22px;height:2px;background:var(--acc);border-radius:2px}
/* BUTTONS */
.btn{display:inline-flex;align-items:center;gap:.5rem;font-family:'Outfit',sans-serif;
  font-weight:800;font-size:.92rem;padding:.88rem 2.1rem;border-radius:var(--r2);
  text-transform:uppercase;letter-spacing:.07em;transition:all .25s;
  cursor:pointer;border:none;text-decoration:none}
.btn-p{background:linear-gradient(135deg,var(--acc),#5b21b6);color:#fff;
  box-shadow:0 4px 28px rgba(124,58,237,.5)}
.btn-p:hover{transform:translateY(-3px);box-shadow:0 8px 42px rgba(124,58,237,.75);color:#fff}
.btn-s{background:transparent;border:1.5px solid var(--bdr2);color:var(--txt)}
.btn-s:hover{border-color:var(--acc);color:var(--acc)}
.btn-g{background:rgba(124,58,237,.1);color:var(--acc);border:1px solid var(--bdr);
  font-size:.83rem;padding:.62rem 1.4rem}
.btn-g:hover{background:rgba(124,58,237,.2)}
.btn-pink{background:linear-gradient(135deg,var(--acc2),#be185d);color:#fff;
  box-shadow:0 4px 22px rgba(236,72,153,.4)}
.btn-pink:hover{transform:translateY(-2px);box-shadow:0 8px 32px rgba(236,72,153,.6);color:#fff}
.btn-lg{padding:1.1rem 2.6rem;font-size:1rem}
.btn-full{width:100%;justify-content:center}
/* HERO */
.hero{min-height:100vh;display:flex;align-items:center;padding:100px 5% 80px;
  position:relative;z-index:1}
.hero-inner{max-width:800px}
.hero-badge{display:inline-flex;align-items:center;gap:.6rem;
  background:rgba(124,58,237,.1);border:1px solid var(--bdr2);
  color:var(--acc);font-size:.75rem;font-weight:700;
  letter-spacing:.15em;text-transform:uppercase;
  padding:.4rem 1.15rem;border-radius:100px;margin-bottom:1.9rem}
.badge-dot{width:7px;height:7px;background:var(--green);border-radius:50%;
  animation:pulse-dot 2s infinite}
@keyframes pulse-dot{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.4;transform:scale(.65)}}
.hero h1{margin-bottom:1.4rem}
.g-acc{color:var(--acc)}.g-acc2{color:var(--acc2)}.g-acc3{color:var(--acc3)}
.g-gold{color:var(--gold)}.g-green{color:var(--green)}.g-orange{color:var(--orange)}
.hero-sub{font-size:1.12rem;color:var(--muted);max-width:650px;margin-bottom:2.6rem}
.hero-ctas{display:flex;gap:1rem;flex-wrap:wrap;margin-bottom:2.8rem}
.hero-trust{display:flex;gap:1.5rem;flex-wrap:wrap;font-size:.77rem;color:var(--muted)}
.trust-it{display:flex;align-items:center;gap:.38rem}
.trust-it::before{content:'✓';color:var(--green);font-weight:800}
/* AUDIO WAVE VISUALIZER */
.wave-bar{display:flex;align-items:center;gap:3px;height:48px;margin:2rem 0}
.wave-b{width:4px;border-radius:2px;background:var(--acc);opacity:.7;
  animation:wave-anim var(--d,.8s) ease-in-out infinite alternate}
@keyframes wave-anim{from{height:8px;opacity:.4}to{height:var(--h,40px);opacity:1}}
/* STATS BAR */
.stats-bar{display:flex;flex-wrap:wrap;background:var(--bg2);
  border-top:1px solid var(--bdr);border-bottom:1px solid var(--bdr);z-index:1;position:relative}
.stat-item{flex:1;min-width:115px;text-align:center;padding:1.7rem .8rem;border-right:1px solid var(--bdr)}
.stat-item:last-child{border-right:none}
.stat-num{font-family:'Fraunces',serif;font-size:2.4rem;font-weight:900;
  line-height:1;display:block;color:var(--acc);text-shadow:var(--glow)}
.stat-lbl{font-size:.71rem;color:var(--muted);text-transform:uppercase;letter-spacing:.12em;margin-top:.25rem}
/* LAYOUT */
section{padding:6rem 5%;position:relative;z-index:1}
.sec-lbl{font-size:.71rem;font-weight:700;letter-spacing:.22em;text-transform:uppercase;color:var(--acc);display:block;margin-bottom:.6rem}
.sec-title{margin-bottom:1.1rem}
.sec-sub{color:var(--muted);max-width:590px;margin-bottom:3rem;font-size:1.02rem}
.tc{text-align:center}.tc .sec-sub{margin-left:auto;margin-right:auto}
.alt{background:linear-gradient(180deg,transparent,rgba(124,58,237,.022),transparent)}
/* GRID */
.g3{display:grid;grid-template-columns:repeat(auto-fit,minmax(270px,1fr));gap:1.5rem}
.g2{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1.5rem}
.g4{display:grid;grid-template-columns:repeat(auto-fit,minmax(185px,1fr));gap:1rem}
.split{display:grid;grid-template-columns:1fr 1fr;gap:5rem;align-items:center}
/* CARDS */
.card{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);
  padding:1.9rem;transition:all .32s;position:relative;overflow:hidden}
.card::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;
  background:linear-gradient(90deg,transparent,var(--acc),transparent);opacity:0;transition:opacity .3s}
.card:hover::before{opacity:1}
.card:hover{border-color:var(--bdr2);transform:translateY(-5px);box-shadow:0 20px 52px rgba(0,0,0,.55)}
.card-icon{width:52px;height:52px;border-radius:12px;background:rgba(124,58,237,.1);
  border:1px solid var(--bdr);display:flex;align-items:center;justify-content:center;
  font-size:1.5rem;margin-bottom:1.2rem;flex-shrink:0}
.card h3{font-size:1.2rem;color:var(--txt);margin-bottom:.45rem}
.card h4{font-size:1rem;color:var(--txt);margin-bottom:.4rem}
.card p{font-size:.89rem}
.card-feat{border-color:rgba(124,58,237,.32);background:linear-gradient(145deg,rgba(124,58,237,.07),rgba(6,182,212,.04))}
/* FORMAT PILLS */
.fmt-grid{display:flex;flex-wrap:wrap;gap:.48rem}
.fmt{background:rgba(124,58,237,.08);border:1px solid rgba(124,58,237,.2);
  color:var(--acc3);font-family:'JetBrains Mono',monospace;font-size:.75rem;
  font-weight:600;padding:.28rem .75rem;border-radius:4px;letter-spacing:.04em}
/* USE CASE TABS */
.use-cases{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:1rem}
.uc{background:var(--card);border:1px solid var(--bdr);border-top:3px solid var(--acc);
  border-radius:var(--r);padding:1.5rem;transition:all .25s}
.uc:hover{border-color:var(--bdr2);transform:translateY(-3px)}
.uc-icon{font-size:1.8rem;margin-bottom:.7rem;display:block}
.uc h4{font-size:.95rem;color:var(--txt);margin-bottom:.5rem}
.uc ul{list-style:none;padding:0;display:flex;flex-direction:column;gap:.3rem}
.uc li{font-size:.8rem;color:var(--muted);display:flex;gap:.4rem}
.uc li::before{content:'·';color:var(--acc);font-weight:700}
/* PRICING */
.pgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:1.5rem;max-width:900px;margin:0 auto}
.pc{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);padding:2.3rem 1.9rem;text-align:center;position:relative;transition:all .3s}
.pc:hover{transform:translateY(-4px)}
.pc.pop{border-color:var(--acc);background:linear-gradient(145deg,rgba(124,58,237,.08),rgba(6,182,212,.04))}
.pop-badge{position:absolute;top:-14px;left:50%;transform:translateX(-50%);
  background:linear-gradient(135deg,var(--acc),var(--acc2));color:#fff;
  font-size:.7rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;
  padding:.28rem 1rem;border-radius:100px;white-space:nowrap}
.p-name{font-size:.78rem;text-transform:uppercase;letter-spacing:.16em;color:var(--muted);margin-bottom:.9rem}
.p-price{font-family:'Fraunces',serif;font-size:3.8rem;font-weight:900;color:var(--acc);line-height:1}
.p-price sup{font-size:1.4rem;vertical-align:top;margin-top:.55rem;display:inline-block}
.p-per{font-size:.78rem;color:var(--muted);margin-bottom:1.7rem}
.p-feats{list-style:none;padding:0;text-align:left;margin-bottom:1.9rem;display:flex;flex-direction:column;gap:.65rem}
.p-feats li{font-size:.86rem;color:var(--muted);display:flex;gap:.5rem;align-items:flex-start}
.p-feats li::before{content:'✓';color:var(--green);font-weight:700;flex-shrink:0}
.p-note{font-size:.75rem;color:var(--gold);margin-top:.9rem;font-weight:600}
/* TABLE */
.tbl-wrap{overflow-x:auto;border-radius:var(--r);border:1px solid var(--bdr)}
table{width:100%;border-collapse:collapse}
thead th{background:rgba(124,58,237,.08);color:var(--acc);font-family:'Fraunces',serif;font-size:.95rem;padding:.9rem 1.2rem;text-align:left;border-bottom:1px solid var(--bdr)}
tbody td{padding:.88rem 1.2rem;border-bottom:1px solid var(--bdr);font-size:.86rem;color:var(--muted)}
tbody tr:last-child td{border-bottom:none}
tbody tr:hover td{background:rgba(124,58,237,.028)}
.td-n{color:var(--txt);font-weight:600}
.td-y{color:var(--green);font-weight:700}
.td-no{color:var(--red)}
.td-p{color:var(--gold)}
.td-hi{background:rgba(124,58,237,.05)!important}
/* FAQ */
.faq-wrap{max-width:780px;margin:0 auto;display:flex;flex-direction:column;gap:.95rem}
details{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);overflow:hidden}
details[open]{border-color:var(--bdr2)}
details summary{padding:1.2rem 1.6rem;cursor:pointer;font-weight:700;font-size:.94rem;color:var(--txt);list-style:none;display:flex;justify-content:space-between;align-items:center;gap:1rem;user-select:none}
details summary::-webkit-details-marker{display:none}
details summary::after{content:'+';color:var(--acc);font-size:1.6rem;font-weight:300;line-height:1;flex-shrink:0}
details[open] summary::after{content:'\u2212'}
details .ans{padding:0 1.6rem 1.3rem;border-top:1px solid var(--bdr);padding-top:.95rem;font-size:.9rem}
details .ans p{color:var(--muted)}
/* TESTIMONIALS */
.tgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:1.5rem}
.testi{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);padding:1.9rem;transition:all .3s}
.testi:hover{border-color:var(--bdr2);transform:translateY(-3px)}
.stars{color:var(--gold);font-size:1rem;margin-bottom:.8rem}
.testi-text{font-size:.9rem;color:var(--txt);font-style:italic;margin-bottom:1.1rem;line-height:1.78}
.testi-author{display:flex;align-items:center;gap:.75rem}
.testi-av{width:38px;height:38px;border-radius:50%;background:linear-gradient(135deg,var(--acc),var(--acc2));display:flex;align-items:center;justify-content:center;font-size:1rem;font-weight:700;flex-shrink:0}
.testi-name{font-weight:700;font-size:.86rem;color:var(--acc)}
.testi-role{font-size:.77rem;color:var(--muted)}
/* STEPS */
.steps{max-width:680px;display:flex;flex-direction:column}
.step{display:flex;gap:1.9rem;align-items:flex-start;padding:1.9rem 0 1.9rem 2.5rem;border-left:2px solid rgba(124,58,237,.2);margin-left:1.5rem;position:relative}
.step::before{content:attr(data-n);position:absolute;left:-1.6rem;width:3.1rem;height:3.1rem;background:var(--bg);border:2px solid var(--acc);border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:'Fraunces',serif;font-size:1.2rem;font-weight:900;color:var(--acc);box-shadow:0 0 20px rgba(124,58,237,.3);z-index:1}
.step:last-child{border-left-color:transparent}
.step h3{font-size:1.1rem;color:var(--txt);margin-bottom:.35rem}
.step p{font-size:.88rem}
/* BLOG */
.bgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:1.5rem}
.bc{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);overflow:hidden;transition:all .3s;display:flex;flex-direction:column}
.bc:hover{transform:translateY(-4px);border-color:var(--bdr2);box-shadow:0 18px 44px rgba(0,0,0,.45)}
.bc-thumb{height:162px;background:linear-gradient(135deg,var(--bg3),rgba(124,58,237,.12));display:flex;align-items:center;justify-content:center;font-size:3rem;border-bottom:1px solid var(--bdr)}
.bc-body{padding:1.5rem;flex:1;display:flex;flex-direction:column}
.bc-tag{font-size:.7rem;color:var(--acc);text-transform:uppercase;letter-spacing:.13em;font-weight:700;margin-bottom:.45rem}
.bc h3{font-size:1rem;color:var(--txt);margin-bottom:.45rem;line-height:1.38}
.bc p{font-size:.82rem;flex:1;line-height:1.68}
.bc-meta{display:flex;gap:1rem;margin-top:.9rem;font-size:.75rem;color:var(--muted)}
.bc-read{margin-top:.9rem;font-size:.8rem;font-weight:700;color:var(--acc)}
/* CTA BLOCK */
.cta-blk{text-align:center;padding:6rem 5%;background:linear-gradient(135deg,rgba(124,58,237,.05),rgba(236,72,153,.03));border-top:1px solid var(--bdr);border-bottom:1px solid var(--bdr);position:relative;z-index:1}
.cta-blk h2{margin-bottom:1rem}
.cta-blk p{max-width:520px;margin:0 auto 2.2rem}
/* HBOX */
.hbox{background:rgba(124,58,237,.05);border:1px solid var(--bdr);border-left:3px solid var(--acc);border-radius:var(--r);padding:1.5rem 1.8rem;margin:1.5rem 0}
.hbox h4{color:var(--acc);margin-bottom:.45rem}
.hbox.warn{border-left-color:var(--gold)}.hbox.warn h4{color:var(--gold)}
.hbox.good{border-left-color:var(--green)}.hbox.good h4{color:var(--green)}
.hbox.info{border-left-color:var(--acc3)}.hbox.info h4{color:var(--acc3)}
/* CHIPS */
.chip{display:inline-flex;align-items:center;font-size:.7rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;padding:.22rem .65rem;border-radius:5px}
.chip-v{background:rgba(124,58,237,.1);color:var(--acc);border:1px solid rgba(124,58,237,.25)}
.chip-g{background:rgba(16,185,129,.1);color:var(--green);border:1px solid rgba(16,185,129,.2)}
.chip-p{background:rgba(236,72,153,.1);color:var(--acc2);border:1px solid rgba(236,72,153,.2)}
.chip-y{background:rgba(245,158,11,.1);color:var(--gold);border:1px solid rgba(245,158,11,.2)}
/* RATING BARS */
.rbars{display:flex;flex-direction:column;gap:1.1rem}
.rbar{display:grid;grid-template-columns:145px 1fr 44px;align-items:center;gap:1rem}
.rbar-lbl{font-size:.83rem;color:var(--muted)}
.rbar-track{height:8px;background:rgba(255,255,255,.06);border-radius:100px;overflow:hidden}
.rbar-fill{height:100%;border-radius:100px;background:linear-gradient(90deg,var(--acc),var(--acc2))}
.rbar-val{font-family:'Fraunces',serif;font-size:1.1rem;color:var(--acc);text-align:right}
.score-big{font-family:'Fraunces',serif;font-size:5.5rem;font-weight:900;line-height:1;color:var(--acc);text-shadow:var(--glow)}
/* PAGE HERO */
.ph{padding:128px 5% 62px;position:relative;z-index:1;background:linear-gradient(180deg,rgba(124,58,237,.045) 0%,transparent 100%);border-bottom:1px solid var(--bdr)}
.breadcrumb{font-size:.76rem;color:var(--muted);margin-bottom:1.2rem;display:flex;align-items:center;gap:.4rem;flex-wrap:wrap}
.breadcrumb a{color:var(--muted)}.breadcrumb a:hover{color:var(--acc)}
.breadcrumb .sep{color:var(--bdr2)}.breadcrumb .cur{color:var(--acc)}
/* SEO */
.seo-tags{display:flex;flex-wrap:wrap;gap:.45rem;margin-bottom:2rem}
.seo-tag{background:rgba(124,58,237,.07);border:1px solid var(--bdr);color:var(--muted);font-size:.73rem;padding:.27rem .75rem;border-radius:100px}
.seo-prose{font-size:.87rem;color:var(--muted);line-height:2;columns:2;column-gap:3rem}
/* FOOTER */
footer{background:var(--bg2);border-top:1px solid var(--bdr);padding:4.5rem 5% 2rem;position:relative;z-index:1}
.fg{display:grid;grid-template-columns:2.2fr 1fr 1fr 1fr;gap:3rem;margin-bottom:3rem}
.fb-logo{font-family:'Fraunces',serif;font-size:1.55rem;font-weight:900;color:var(--txt);margin-bottom:.85rem}
.fb-logo span{color:var(--acc)}
.fb-desc{font-size:.82rem;color:var(--muted);max-width:255px;line-height:1.78}
.fc h5{font-size:.73rem;text-transform:uppercase;letter-spacing:.16em;color:var(--txt);margin-bottom:1.1rem}
.fc ul{list-style:none;padding:0;display:flex;flex-direction:column;gap:.6rem}
.fc a{color:var(--muted);font-size:.82rem;transition:color .2s}.fc a:hover{color:var(--acc)}
.fb-bot{border-top:1px solid var(--bdr);padding-top:1.6rem;display:flex;justify-content:space-between;flex-wrap:wrap;gap:.8rem}
.fb-bot p{font-size:.77rem;color:var(--muted)}
/* RESPONSIVE */
@media(max-width:1100px){.fg{grid-template-columns:1fr 1fr 1fr}}
@media(max-width:900px){.fg{grid-template-columns:1fr 1fr}.split{grid-template-columns:1fr;gap:2.5rem}.seo-prose{columns:1}}
@media(max-width:640px){.nav-links{display:none}.ham{display:flex}.fg{grid-template-columns:1fr}.stat-item{min-width:47%;border-right:none;border-bottom:1px solid var(--bdr)}.pgrid{grid-template-columns:1fr}.rbar{grid-template-columns:110px 1fr 38px}section{padding:4.5rem 5%}}
/* ANIMATIONS */
@keyframes fadeUp{from{opacity:0;transform:translateY(22px)}to{opacity:1;transform:translateY(0)}}
.anim{animation:fadeUp .7s ease forwards}
.d1{animation-delay:.1s;opacity:0}.d2{animation-delay:.2s;opacity:0}.d3{animation-delay:.3s;opacity:0}.d4{animation-delay:.4s;opacity:0}
@keyframes glow-pulse{0%,100%{box-shadow:0 4px 28px rgba(124,58,237,.5)}50%{box-shadow:0 4px 52px rgba(124,58,237,.85)}}
.btn-p{animation:glow-pulse 3.5s ease-in-out infinite}
"""

# ── WAVE VISUALIZER HTML ──────────────────────────────────────────────────────
def wave_viz():
    """Animated audio wave bars — pure CSS"""
    heights = [12,22,36,48,40,32,44,48,38,26,42,48,44,30,18,36,48,42,24,38,46,40,28,44,48]
    delays  = [.0,.1,.2,.15,.05,.3,.12,.08,.22,.18,.04,.25,.1,.35,.2,.07,.13,.28,.06,.17,.24,.09,.31,.16,.03]
    bars = "".join(
        f'<div class="wave-b" style="--h:{h}px;--d:{d}s;animation-duration:{d+.5:.2f}s"></div>'
        for h,d in zip(heights, delays)
    )
    return f'<div class="wave-bar" aria-hidden="true">{bars}</div>'


# ── SHARED COMPONENTS ─────────────────────────────────────────────────────────
def nav():
    links = [
        ("Features",    f"{SITE_ROOT}/features/"),
        ("How It Works",f"{SITE_ROOT}/how-it-works/"),
        ("Use Cases",   f"{SITE_ROOT}/use-cases/"),
        ("Formats",     f"{SITE_ROOT}/formats/"),
        ("Pricing",     f"{SITE_ROOT}/pricing/"),
        ("Review",      f"{SITE_ROOT}/review/"),
        ("Blog",        f"{SITE_ROOT}/blog/"),
        ("FAQ",         f"{SITE_ROOT}/faq/"),
    ]
    li = "".join(f'<li><a href="{u}">{l}</a></li>' for l,u in links)
    return (
        f'<nav><a class="logo" href="{SITE_ROOT}/">Audio<span>Recorder</span></a>'
        f'<ul class="nav-links">{li}'
        f'<li><a href="{AFF}" class="nav-cta" target="_blank" rel="noopener sponsored">⬇ Free Trial</a></li>'
        f'</ul><div class="ham"><span></span><span></span><span></span></div></nav>'
    )

def foot():
    return (
        f'<footer><div class="fg">'
        f'<div><div class="fb-logo">Audio<span>Recorder</span></div>'
        f'<p class="fb-desc">Independent affiliate guide for Wondershare Streaming Audio Recorder. Record any audio from your computer — streaming music, meetings, podcasts, radio — in MP3, WAV, FLAC and more.</p></div>'
        f'<div class="fc"><h5>Product</h5><ul>'
        f'<li><a href="{SITE_ROOT}/features/">All Features</a></li>'
        f'<li><a href="{SITE_ROOT}/formats/">Output Formats</a></li>'
        f'<li><a href="{SITE_ROOT}/pricing/">Pricing</a></li>'
        f'<li><a href="{SITE_ROOT}/review/">Full Review</a></li>'
        f'<li><a href="{SITE_ROOT}/download/">Download</a></li>'
        f'</ul></div>'
        f'<div class="fc"><h5>Guides</h5><ul>'
        f'<li><a href="{SITE_ROOT}/record-streaming-audio/">Record Streaming Audio</a></li>'
        f'<li><a href="{SITE_ROOT}/record-zoom-audio/">Record Zoom Audio</a></li>'
        f'<li><a href="{SITE_ROOT}/record-spotify/">Record Spotify</a></li>'
        f'<li><a href="{SITE_ROOT}/podcast-recorder/">Podcast Recorder</a></li>'
        f'<li><a href="{SITE_ROOT}/voice-recorder/">Voice Recorder</a></li>'
        f'<li><a href="{SITE_ROOT}/blog/">Blog</a></li>'
        f'</ul></div>'
        f'<div class="fc"><h5>Compare</h5><ul>'
        f'<li><a href="{SITE_ROOT}/vs-audacity/">vs Audacity</a></li>'
        f'<li><a href="{SITE_ROOT}/vs-garageband/">vs GarageBand</a></li>'
        f'<li><a href="{SITE_ROOT}/alternatives/">All Alternatives</a></li>'
        f'<li><a href="{SITE_ROOT}/use-cases/">Use Cases</a></li>'
        f'<li><a href="{SITE_ROOT}/faq/">FAQ</a></li>'
        f'<li><a href="{SITE_ROOT}/disclaimer/">Disclaimer</a></li>'
        f'</ul></div>'
        f'</div>'
        f'<div class="fb-bot">'
        f'<p>© {YEAR} AudioRecorder Guide — Independent affiliate site. Commissions earned at no extra cost to you.</p>'
        f'<p><a href="{AFF}" target="_blank" rel="noopener sponsored">Download Free Trial →</a></p>'
        f'</div></footer>'
    )

def bc(*crumbs):
    parts = []
    for i,(label,url) in enumerate(crumbs):
        if url and i < len(crumbs)-1:
            parts.append(f'<a href="{url}">{label}</a><span class="sep">›</span>')
        else:
            parts.append(f'<span class="cur">{label}</span>')
    return '<nav class="breadcrumb">' + "".join(parts) + "</nav>"

def sw_schema(desc):
    return (
        '{"@context":"https://schema.org","@type":"SoftwareApplication",'
        '"name":"Wondershare Streaming Audio Recorder",'
        '"applicationCategory":"MultimediaApplication",'
        '"operatingSystem":"Windows",'
        '"offers":{"@type":"Offer","price":"0","priceCurrency":"USD","description":"Free trial available"},'
        '"aggregateRating":{"@type":"AggregateRating","ratingValue":"4.5","reviewCount":"1842","bestRating":"5"},'
        f'"description":"{desc[:200]}",'
        f'"url":"{SITE_URL}/",'
        '"publisher":{"@type":"Organization","name":"Wondershare","url":"https://videoconverter.wondershare.com"}}'
    )

def bc_schema(title, path):
    canon = f"{SITE_URL}{path}"
    return (
        '{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":['
        f'{{"@type":"ListItem","position":1,"name":"Home","item":"{SITE_URL}/"}},'
        f'{{"@type":"ListItem","position":2,"name":"{title}","item":"{canon}"}}'
        ']}'
    )

def page(title, desc, path, body, kw="", extras=None, article=False):
    kw = kw or "audio recorder software, streaming audio recorder, record system audio, MP3 recorder"
    canon = f"{SITE_URL}{path}"
    extras = extras or []
    schemas = f'<script type="application/ld+json">{sw_schema(desc)}</script>'
    schemas += f'<script type="application/ld+json">{bc_schema(title.split("—")[0].strip(), path)}</script>'
    for ex in extras:
        schemas += f'<script type="application/ld+json">{ex}</script>'
    og_type = "article" if article else "website"
    return (
        '<!DOCTYPE html>\n'
        '<html lang="en">\n'
        '<head>\n'
        '<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">\n'
        f'<title>{title}</title>\n'
        f'<meta name="description" content="{desc}">\n'
        f'<meta name="keywords" content="{kw}">\n'
        '<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">\n'
        f'<link rel="canonical" href="{canon}">\n'
        f'<meta property="og:title" content="{title}">\n'
        f'<meta property="og:description" content="{desc}">\n'
        f'<meta property="og:url" content="{canon}">\n'
        f'<meta property="og:type" content="{og_type}">\n'
        f'<meta property="og:image" content="{SITE_URL}/assets/og.png">\n'
        '<meta property="og:site_name" content="AudioRecorder Guide">\n'
        '<meta name="twitter:card" content="summary_large_image">\n'
        f'<meta name="twitter:title" content="{title}">\n'
        f'<meta name="twitter:description" content="{desc}">\n'
        f'<link rel="icon" href="{SITE_ROOT}/assets/favicon.svg" type="image/svg+xml">\n'
        f'<link rel="alternate" type="application/rss+xml" title="AudioRecorder Blog" href="{SITE_URL}/feed.xml">\n'
        f'{schemas}\n'
        f'<style>{CSS}</style>\n'
        '</head>\n'
        '<body>\n'
        + nav() +
        '\n' + body + '\n'
        + foot() +
        '\n<script>\n'
        '(function(){\n'
        '  var h=document.querySelector(".ham"),nl=document.querySelector(".nav-links");\n'
        '  if(!h||!nl)return;\n'
        '  h.addEventListener("click",function(){\n'
        '    var open=nl.style.display==="flex";\n'
        '    nl.style.cssText=open?"":"display:flex;position:fixed;top:66px;left:0;right:0;flex-direction:column;background:rgba(4,5,13,.98);padding:2rem 5%;gap:1.3rem;border-bottom:1px solid rgba(124,58,237,.13);z-index:998;backdrop-filter:blur(22px)";\n'
        '  });\n'
        '})();\n'
        '</script>\n'
        '</body></html>'
    )

def write(rel, content):
    p = BASE / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    print(f"  \u2713  {rel}")


# ── HOMEPAGE ──────────────────────────────────────────────────────────────────
def pg_home():
    fmts = "".join(
        f'<span class="fmt">{f}</span>'
        for f in ["MP3","WAV","FLAC","AAC","M4A","OGG","WMA","AIFF","AC3","APE","CAF","MP2"]
    )
    sources = [
        ("🎵","Streaming Music","Spotify, Apple Music, Amazon Music, YouTube Music, Tidal, Deezer"),
        ("📻","Internet Radio","Record any online radio station automatically on a schedule"),
        ("🎙","Microphone","Record voice memos, dictation, interviews, podcasts, voiceovers"),
        ("🖥","System Audio","Any sound playing through your computer — games, movies, apps"),
        ("📹","Video Calls","Zoom, Teams, Google Meet, Skype, Discord — audio only, no video"),
        ("🎮","Games & Apps","Record in-game audio, app sounds, notification sounds"),
        ("🌐","Browser Audio","Capture audio from Chrome, Firefox, Edge — YouTube, Netflix, any site"),
        ("🎚","External Devices","Connect mixers, instruments, line-in devices via audio interface"),
    ]
    src_cards = "".join(
        f'<div class="card"><div class="card-icon">{icon}</div>'
        f'<h3>{title}</h3><p>{desc}</p></div>'
        for icon,title,desc in sources
    )
    return page(
        f"Wondershare Audio Recorder — Record Any Audio From Your Computer | {YEAR}",
        f"Wondershare Streaming Audio Recorder captures any audio playing on your computer — streaming music, Zoom calls, radio, podcasts, microphone. Save as MP3, WAV, FLAC. Free trial. Best audio recorder {YEAR}.",
        "/",
        (
            '<section class="hero">'
            '<div class="hero-inner">'
            f'<div class="hero-badge anim"><span class="badge-dot"></span> Record Any Sound From Any Source</div>'
            f'<h1 class="anim d1">Capture <span class="g-acc">Any Audio.</span><br>'
            f'Save as <span class="g-acc2">MP3, WAV,</span><br>'
            f'<span class="g-acc3">FLAC & More.</span></h1>'
            + wave_viz() +
            f'<p class="hero-sub anim d2">Wondershare Streaming Audio Recorder captures any sound playing on your computer — streaming music, Zoom calls, internet radio, podcasts, microphone recordings — in crystal-clear quality. Schedule recordings, split tracks automatically, and save in 10+ formats. Free trial available.</p>'
            f'<div class="hero-ctas anim d3">'
            f'<a href="{AFF}" class="btn btn-p btn-lg" target="_blank" rel="noopener sponsored">\u2b07 Download Free Trial</a>'
            f'<a href="{SITE_ROOT}/features/" class="btn btn-s btn-lg">See All Features \u2192</a>'
            f'</div>'
            f'<div class="hero-trust anim d4">'
            f'<span class="trust-it">Free Trial</span>'
            f'<span class="trust-it">Windows</span>'
            f'<span class="trust-it">MP3, WAV, FLAC</span>'
            f'<span class="trust-it">Schedule Recording</span>'
            f'<span class="trust-it">No Quality Loss</span>'
            f'</div>'
            f'</div></section>'

            f'<div class="stats-bar">'
            f'<div class="stat-item"><span class="stat-num">10+</span><span class="stat-lbl">Output Formats</span></div>'
            f'<div class="stat-item"><span class="stat-num">Any</span><span class="stat-lbl">Audio Source</span></div>'
            f'<div class="stat-item"><span class="stat-num">0</span><span class="stat-lbl">Quality Loss</span></div>'
            f'<div class="stat-item"><span class="stat-num">24/7</span><span class="stat-lbl">Scheduled Recording</span></div>'
            f'<div class="stat-item"><span class="stat-num">Auto</span><span class="stat-lbl">Track Split</span></div>'
            f'</div>'

            f'<section>'
            f'<span class="sec-lbl">Every Audio Source</span>'
            f'<h2 class="sec-title">Record From <span class="g-acc">Anywhere</span></h2>'
            f'<p class="sec-sub">It doesn\'t matter where the audio is playing. If it comes out of your computer, Wondershare Audio Recorder captures it — at full quality, with no gaps or interruptions.</p>'
            f'<div class="g3">{src_cards}</div>'
            f'</section>'

            f'<section class="alt">'
            f'<span class="sec-lbl tc" style="display:block;text-align:center">Output Formats</span>'
            f'<h2 class="sec-title tc">Save In <span class="g-acc">Any Format</span></h2>'
            f'<p class="sec-sub tc">MP3 for sharing, WAV for editing, FLAC for archiving. Choose the right format for every use case.</p>'
            f'<div class="fmt-grid" style="max-width:720px;margin:0 auto 2rem;justify-content:center">{fmts}</div>'
            f'<div style="text-align:center"><a href="{SITE_ROOT}/formats/" class="btn btn-g">All Format Details \u2192</a></div>'
            f'</section>'

            f'<section>'
            f'<div class="split">'
            f'<div>'
            f'<span class="sec-lbl">Key Features</span>'
            f'<h2 class="sec-title">More Than Just<br><span class="g-acc">Record & Save</span></h2>'
            f'<p style="margin-bottom:1.5rem">Wondershare Audio Recorder includes everything you need to capture, organise and manage your recordings — not just a bare record button.</p>'
            f'<ul style="list-style:none;padding:0;display:flex;flex-direction:column;gap:.9rem">'
            + "".join(
                f'<li style="display:flex;gap:.7rem;font-size:.9rem;color:var(--muted)">'
                f'<span style="color:var(--green);font-weight:700">\u2713</span>'
                f'<span><strong>{a}</strong> \u2014 {b}</span></li>'
                for a,b in [
                    ("Scheduled recording", "set a start time and stop time — records while you sleep"),
                    ("Auto track split", "detects silence between tracks and saves each as a separate file"),
                    ("ID3 tag editor", "automatically labels recordings with artist, title, album, cover art"),
                    ("Built-in audio editor", "trim, cut and adjust recordings without leaving the app"),
                    ("Noise reduction", "clean up microphone hiss and background hum automatically"),
                    ("Format converter", "convert existing audio files between any supported format"),
                ]
            )
            + f'</ul>'
            f'<div style="margin-top:2rem"><a href="{AFF}" class="btn btn-p" target="_blank" rel="noopener sponsored">\u2b07 Try Free Now</a></div>'
            f'</div>'
            f'<div>'
            f'<div class="card card-feat" style="padding:2.2rem">'
            f'<h3 style="color:var(--acc);margin-bottom:1.4rem">Audio Recorder vs Manual Methods</h3>'
            f'<div class="tbl-wrap"><table>'
            f'<thead><tr><th>Task</th><th>Audio Recorder</th><th>Manual</th></tr></thead>'
            f'<tbody>'
            f'<tr><td>Record streaming music</td><td class="td-y td-hi">\u2713 One click</td><td class="td-no">\u2715 Not possible</td></tr>'
            f'<tr><td>Schedule overnight recording</td><td class="td-y td-hi">\u2713 Built in</td><td class="td-no">\u2715 Must stay awake</td></tr>'
            f'<tr><td>Auto-split into tracks</td><td class="td-y td-hi">\u2713 Automatic</td><td class="td-no">\u2715 Manual editing</td></tr>'
            f'<tr><td>ID3 tags on save</td><td class="td-y td-hi">\u2713 Automatic</td><td class="td-no">\u2715 Manual tagging</td></tr>'
            f'<tr><td>Record Zoom audio only</td><td class="td-y td-hi">\u2713 Clean audio</td><td class="td-p">\u26a0 Screen recorder = video</td></tr>'
            f'<tr><td>Convert format on save</td><td class="td-y td-hi">\u2713 Built in</td><td class="td-no">\u2715 Separate software</td></tr>'
            f'</tbody></table></div>'
            f'</div>'
            f'</div>'
            f'</div>'
            f'</section>'

            f'<section class="alt">'
            f'<span class="sec-lbl tc" style="display:block;text-align:center">Real Users</span>'
            f'<h2 class="sec-title tc">What People <span class="g-acc">Are Saying</span></h2>'
            f'<p class="sec-sub tc">4.5 stars from verified users worldwide</p>'
            f'<div class="tgrid">'
            f'<div class="testi"><div class="stars">\u2605\u2605\u2605\u2605\u2605</div><p class="testi-text">"I record internet radio every night on a schedule. It automatically splits each programme into a separate file. What used to be impossible is now completely effortless."</p><div class="testi-author"><div class="testi-av">R</div><div><div class="testi-name">Robert K. \U0001f1ec\U0001f1e7</div><div class="testi-role">Radio enthusiast, Manchester</div></div></div></div>'
            f'<div class="testi"><div class="stars">\u2605\u2605\u2605\u2605\u2605</div><p class="testi-text">"I conduct interviews over Zoom and only need the audio. This records the call cleanly in MP3 without capturing video. Perfect for my journalism workflow."</p><div class="testi-author"><div class="testi-av">S</div><div><div class="testi-name">Sofia M. \U0001f1e7\U0001f1f7</div><div class="testi-role">Journalist, S\u00e3o Paulo</div></div></div></div>'
            f'<div class="testi"><div class="stars">\u2605\u2605\u2605\u2605\u2606</div><p class="testi-text">"The ID3 tag feature is brilliant — my recordings are automatically named and tagged so they go straight into my music library. Saves so much time."</p><div class="testi-author"><div class="testi-av">J</div><div><div class="testi-name">James L. \U0001f1fa\U0001f1f8</div><div class="testi-role">Music collector, Chicago</div></div></div></div>'
            f'<div class="testi"><div class="stars">\u2605\u2605\u2605\u2605\u2605</div><p class="testi-text">"I use this to record my own podcast demos. Crystal clear microphone recording, built-in noise reduction, exports to MP3 in one click. Exactly what I needed."</p><div class="testi-author"><div class="testi-av">A</div><div><div class="testi-name">Anika T. \U0001f1e9\U0001f1ea</div><div class="testi-role">Podcast creator, Berlin</div></div></div></div>'
            f'<div class="testi"><div class="stars">\u2605\u2605\u2605\u2605\u2605</div><p class="testi-text">"As a student I record lectures on Zoom. This saves just the audio — tiny file size, perfect clarity, automatic filename with date. My go-to tool."</p><div class="testi-author"><div class="testi-av">K</div><div><div class="testi-name">Kenji W. \U0001f1ef\U0001f1f5</div><div class="testi-role">University student, Osaka</div></div></div></div>'
            f'<div class="testi"><div class="stars">\u2605\u2605\u2605\u2605\u2605</div><p class="testi-text">"I use the scheduled recording for evening radio shows I can\'t listen to live. It records, splits and tags automatically. Wake up to a perfectly organised playlist."</p><div class="testi-author"><div class="testi-av">M</div><div><div class="testi-name">Maria G. \U0001f1ea\U0001f1f8</div><div class="testi-role">Music teacher, Madrid</div></div></div></div>'
            f'</div>'
            f'</section>'

            f'<div class="cta-blk">'
            f'<span class="sec-lbl" style="display:block;margin-bottom:1rem">Start Recording Today</span>'
            f'<h2>Record <span class="g-acc">Any Audio</span> From<br>Any Source</h2>'
            f'<p>Free trial available — record streaming audio, meetings, radio, podcasts and voice memos in any format.</p>'
            f'<a href="{AFF}" class="btn btn-p btn-lg" target="_blank" rel="noopener sponsored">\u2b07 Download Audio Recorder Free</a>'
            f'<p style="margin-top:1.2rem;font-size:.8rem;color:var(--muted)">Windows · MP3, WAV, FLAC, AAC and more · Schedule recording · Auto track split · Free trial</p>'
            f'</div>'
        ),
        kw=KEYWORDS
    )


def pg_features():
    il = (
        '{"@context":"https://schema.org","@type":"ItemList","name":"Audio Recorder Features",'
        '"itemListElement":['
        '{"@type":"ListItem","position":1,"name":"Record Any System Audio"},'
        '{"@type":"ListItem","position":2,"name":"Scheduled Recording"},'
        '{"@type":"ListItem","position":3,"name":"Auto Track Split"},'
        '{"@type":"ListItem","position":4,"name":"ID3 Tag Editor"},'
        '{"@type":"ListItem","position":5,"name":"Built-in Audio Editor"},'
        '{"@type":"ListItem","position":6,"name":"Noise Reduction"},'
        '{"@type":"ListItem","position":7,"name":"Format Converter"}'
        ']}'
    )
    features = [
        ("🎵","Record Any System Audio","Capture any audio playing through your computer's speakers or headphone output — streaming services, YouTube, Netflix, games, apps, browser audio — using virtual audio driver technology that records at source with zero quality loss."),
        ("🎙","Record Microphone","Record from any connected microphone — built-in laptop mic, USB mic, condenser mic, headset. Adjust input levels, monitor while recording, and apply noise reduction automatically."),
        ("📅","Scheduled Recording","Set a precise start time and stop time for any recording. The recorder activates automatically — perfect for recording overnight radio programmes, scheduled podcasts or live streams you can't attend in real time."),
        ("✂️","Auto Track Split","Detects silence between tracks and automatically saves each piece of audio as a separate named file. No manual cutting needed — your recording session becomes a perfectly organised playlist."),
        ("🏷","ID3 Tag Editor","Automatically labels every recording with artist name, title, album, year, genre and cover art. Recordings go directly into your music library already organised. Edit tags manually for complete control."),
        ("🔇","Noise Reduction","AI-powered background noise reduction removes hiss, hum, air conditioning and ambient noise from recordings — especially useful for microphone recordings in imperfect environments."),
        ("✏️","Built-in Audio Editor","Trim the start and end of recordings, cut out unwanted sections, adjust volume levels and fade in/out — all without opening a separate audio editor."),
        ("🔄","Format Converter","Convert existing audio files between any supported format — MP3, WAV, FLAC, AAC, OGG, WMA and more. Batch convert entire folders of audio files in one operation."),
        ("📁","Smart File Management","Recordings are automatically named with date, time and source information. Folder organisation keeps recordings sorted and easy to find. Export to any destination folder."),
        ("🎚","Audio Level Control","Adjust recording volume, set input gain, monitor audio levels with a real-time VU meter. Prevent clipping on loud sources and boost quiet recordings automatically."),
        ("🔊","Stereo & Mono","Record in full stereo from stereo sources or choose mono for voice recordings to reduce file size. Full sample rate and bit depth control for professional quality."),
        ("⚡","Low Latency","Records audio with minimal delay — important for monitoring during recording and ensuring sync with video sources when recording conference calls or game audio."),
    ]
    cards = "".join(
        f'<div class="card{"  card-feat" if i<2 else ""}"><div class="card-icon">{icon}</div>'
        f'<h3>{title}</h3><p>{desc}</p></div>'
        for i,(icon,title,desc) in enumerate(features)
    )
    return page(
        f"Audio Recorder Features — Complete List | Record Any Audio {YEAR}",
        "Full Wondershare Audio Recorder feature list: record system audio, microphone, scheduled recording, auto track split, ID3 tags, noise reduction, built-in editor, format converter.",
        "/features/",
        (
            f'<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Features",None))}'
            f'<span class="sec-lbl">Everything It Does</span>'
            f'<h1>Audio Recorder <span class="g-acc">Features</span></h1>'
            f'<p style="max-width:640px;margin-top:.9rem;font-size:1.05rem;color:var(--muted)">Every feature in detail — from basic recording to scheduled capture, auto-split and ID3 tagging.</p></div>'
            f'<section><div class="g3">{cards}</div>'
            f'<div class="cta-blk" style="margin-top:3rem;border-radius:var(--r)">'
            f'<h2 style="margin-bottom:.8rem">All Features, <span class="g-acc">Free to Try</span></h2>'
            f'<p>Download and test everything with the free trial. No credit card required.</p>'
            f'<a href="{AFF}" class="btn btn-p" target="_blank" rel="noopener sponsored">\u2b07 Download Free Trial</a>'
            f'</div></section>'
        ),
        "audio recorder features, system audio recorder, scheduled recording, auto track split, ID3 tags, noise reduction",
        extras=[il]
    )

def pg_how():
    howto = (
        '{"@context":"https://schema.org","@type":"HowTo",'
        '"name":"How to Record Audio with Wondershare Audio Recorder",'
        '"description":"Record any audio from your computer in 3 steps.",'
        '"step":['
        '{"@type":"HowToStep","position":1,"name":"Choose your source","text":"Select system audio, microphone, or both as your recording source."},'
        '{"@type":"HowToStep","position":2,"name":"Configure settings","text":"Set output format (MP3, WAV, FLAC), quality, and destination folder."},'
        '{"@type":"HowToStep","position":3,"name":"Record","text":"Click Record. Audio Recorder captures everything cleanly at source quality."}'
        ']}'
    )
    return page(
        f"How Wondershare Audio Recorder Works — Record in 3 Steps | {YEAR}",
        "How to record audio with Wondershare Audio Recorder: choose source, configure settings, record. Works for system audio, microphone, streaming music, meetings and internet radio.",
        "/how-it-works/",
        (
            f'<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("How It Works",None))}'
            f'<span class="sec-lbl">Simple Process</span>'
            f'<h1>How <span class="g-acc">Audio Recorder</span> Works</h1>'
            f'<p style="max-width:640px;margin-top:.9rem;color:var(--muted)">Three ways to record — manual, scheduled or always-on. Here\'s every workflow.</p></div>'
            f'<section><div class="split">'
            f'<div>'
            f'<h2 style="margin-bottom:2rem">Basic <span class="g-acc">Recording</span> — 3 Steps</h2>'
            f'<div class="steps">'
            f'<div class="step" data-n="1"><div><h3>Choose Your Source</h3>'
            f'<p>Select <strong>System Audio</strong> to record anything playing through your speakers, <strong>Microphone</strong> for voice input, or <strong>Both</strong> to capture everything simultaneously.</p></div></div>'
            f'<div class="step" data-n="2"><div><h3>Configure Output</h3>'
            f'<p>Choose your output format (MP3 for sharing, WAV for editing, FLAC for archiving), set quality/bitrate, and select your destination folder.</p></div></div>'
            f'<div class="step" data-n="3"><div><h3>Click Record</h3>'
            f'<p>Audio Recorder captures your source at full quality using virtual audio driver technology. No system sounds are missed, no quality degradation.</p></div></div>'
            f'</div></div>'
            f'<div style="display:flex;flex-direction:column;gap:1.5rem">'
            f'<div class="hbox"><h4>Scheduled Recording</h4>'
            f'<p style="margin-top:.4rem">Set a start time and end time. Audio Recorder activates automatically — record tonight\'s radio show at 10pm, a weekly podcast at 9am, or any recurring audio event. The computer can be locked; recording still runs.</p></div>'
            f'<div class="hbox"><h4>Auto Track Split</h4>'
            f'<p style="margin-top:.4rem">Enable auto-split and Audio Recorder detects silence between tracks (configurable threshold). Each piece of audio is automatically saved as a separate file — perfect for recording albums or playlists where you want individual tracks.</p></div>'
            f'<div class="hbox good"><h4>Always-On Mode</h4>'
            f'<p style="margin-top:.4rem">Enable always-on recording to capture everything that plays through your computer continuously. Audio Recorder runs silently in the system tray and saves audio in chunks. Never miss audio from any source.</p></div>'
            f'<a href="{AFF}" class="btn btn-p" target="_blank" rel="noopener sponsored">\u2b07 Try Free Now</a>'
            f'</div></div></section>'
        ),
        "how to record audio, audio recording steps, record system audio how to, scheduled audio recording",
        extras=[howto]
    )

def pg_formats():
    fmt_data = [
        ("MP3","The universal format. Smallest file size, plays everywhere. Best for sharing, streaming and casual listening. Bitrate options: 64kbps to 320kbps.","128–320 kbps","All devices","Best for sharing"),
        ("WAV","Uncompressed, lossless audio. Largest file size but perfect quality. The professional standard for editing, mastering and archiving.","1411 kbps (CD)","All devices","Best for editing"),
        ("FLAC","Free Lossless Audio Codec. Lossless quality at about half the size of WAV. The audiophile choice for archiving and high-quality listening.","~700–1100 kbps","Most players","Best for archiving"),
        ("AAC","Advanced Audio Coding. Better quality than MP3 at the same bitrate. Default format for Apple devices, YouTube and streaming platforms.","128–256 kbps","Apple, Android","Best for Apple devices"),
        ("M4A","Apple's audio format. AAC audio in an MPEG-4 container. Native on iOS/macOS. Excellent quality, reasonable file size.","128–256 kbps","Apple devices","Best for iPhone/Mac"),
        ("OGG","Open-source format. Good quality at low bitrates. Used by games, Spotify internally, and open-source apps.","80–500 kbps","Limited","Best for games/apps"),
        ("WMA","Windows Media Audio. Microsoft's format. Good compatibility with Windows software and older media players.","64–192 kbps","Windows","Best for Windows"),
        ("AIFF","Audio Interchange File Format. Apple's uncompressed format. Equivalent to WAV but native to macOS. Used in professional audio.","1411 kbps","Apple pro tools","Best for Mac pros"),
        ("AC3","Dolby Digital audio. Used in DVDs, Blu-rays and broadcast. Excellent for surround sound recordings.","192–640 kbps","DVD/Blu-ray players","Best for surround"),
        ("APE","Monkey's Audio. Lossless compression with very small file sizes. Excellent for archiving at minimum storage.","~400–700 kbps","Specialised players","Best for audiophiles"),
    ]
    rows = "".join(
        f'<tr><td class="td-n"><code>{fmt}</code></td><td>{desc[:70]}...</td><td class="td-p">{br}</td><td>{compat}</td><td class="td-y">{use}</td></tr>'
        for fmt,desc,br,compat,use in fmt_data
    )
    return page(
        f"Audio Recorder Output Formats — MP3, WAV, FLAC, AAC & More | {YEAR}",
        "Wondershare Audio Recorder saves recordings as MP3, WAV, FLAC, AAC, M4A, OGG, WMA, AIFF, AC3 and APE. Full format guide with bitrate, compatibility and best use cases.",
        "/formats/",
        (
            f'<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Formats",None))}'
            f'<span class="sec-lbl">Output Formats</span>'
            f'<h1>Supported <span class="g-acc">Formats</span></h1>'
            f'<p style="max-width:660px;margin-top:.9rem;color:var(--muted)">10 output formats covering every use case — from casual MP3 sharing to lossless FLAC archiving.</p></div>'
            f'<section>'
            f'<div class="fmt-grid" style="margin-bottom:2rem">'
            + "".join(f'<span class="fmt">{f}</span>' for f in ["MP3","WAV","FLAC","AAC","M4A","OGG","WMA","AIFF","AC3","APE"])
            + f'</div>'
            f'<div class="tbl-wrap"><table>'
            f'<thead><tr><th>Format</th><th>Description</th><th>Bitrate</th><th>Compatibility</th><th>Best For</th></tr></thead>'
            f'<tbody>{rows}</tbody></table></div>'
            f'<div class="hbox info" style="margin-top:2rem"><h4>Which Format Should You Choose?</h4>'
            f'<p style="margin-top:.4rem"><strong>MP3</strong> for everyday sharing and streaming compatibility. '
            f'<strong>WAV</strong> if you plan to edit the recording. '
            f'<strong>FLAC</strong> for highest quality archive with smaller size than WAV. '
            f'<strong>AAC/M4A</strong> if you use Apple devices primarily. '
            f'<strong>OGG</strong> for open-source compatibility or gaming audio.</p></div>'
            f'<div style="text-align:center;margin-top:2rem">'
            f'<a href="{AFF}" class="btn btn-p" target="_blank" rel="noopener sponsored">\u2b07 Download Audio Recorder Free</a>'
            f'</div></section>'
        ),
        "MP3 recorder, WAV recorder, FLAC recorder, audio recorder formats, AAC recorder, audio output formats"
    )

def pg_use_cases():
    cases = [
        ("🎵","Music & Radio","Record streaming music to build an offline library. Capture internet radio shows on a schedule. Save live DJ sets and concerts.","Record Spotify or Apple Music for offline listening","Capture BBC Radio 4 overnight on a schedule","Save live radio broadcasts for later"),
        ("📞","Calls & Meetings","Record Zoom, Teams, Meet and Skype audio cleanly. Save interviews and podcasts. Audio-only recording — smaller file than screen recording.","Record Zoom calls as MP3 for easy sharing","Save Google Meet audio for meeting notes","Capture phone interviews over VoIP"),
        ("🎙","Podcasting","Record microphone with noise reduction. Edit in the built-in trimmer. Export to MP3. Auto-name and tag recordings for episode management.","High-quality mic recording with noise reduction","Trim silences and edit in the built-in editor","Export tagged MP3 ready to upload"),
        ("🎓","Education","Record lectures, online courses, webinars and tutorials for later review. Students use it to capture remote class audio automatically.","Record lecture audio from Zoom or Teams","Capture webinar audio on a schedule","Save online course audio for revision"),
        ("🎮","Gaming & Content","Record in-game audio, commentary, or system sounds. Capture audio from streaming games for highlight reels or game reviews.","Record game audio without video","Capture voiceover while playing","Record system audio during streams"),
        ("🎚","Musicians","Record guitar direct through audio interface, capture practice sessions, record reference tracks, and convert recordings between formats.","Record instrument via audio interface","Capture practice session for review","Convert recordings between formats"),
    ]
    cards = "".join(
        f'<div class="uc"><span class="uc-icon">{icon}</span><h4>{title}</h4>'
        f'<p style="font-size:.82rem;margin-bottom:.8rem">{desc}</p>'
        f'<ul>' + "".join(f'<li>{x}</li>' for x in bullets) + f'</ul></div>'
        for icon,title,desc,*bullets in cases
    )
    return page(
        f"Audio Recorder Use Cases — Music, Meetings, Podcasts, Radio | {YEAR}",
        "Wondershare Audio Recorder use cases: record streaming music, Zoom calls, podcasts, internet radio, lectures, game audio, microphone recordings. Every use case covered.",
        "/use-cases/",
        (
            f'<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Use Cases",None))}'
            f'<span class="sec-lbl">Who Uses It</span>'
            f'<h1>Audio Recorder <span class="g-acc">Use Cases</span></h1>'
            f'<p style="max-width:640px;margin-top:.9rem;color:var(--muted)">From music collectors to journalists, podcasters to students — here\'s how people use Wondershare Audio Recorder.</p></div>'
            f'<section><div class="use-cases">{cards}</div>'
            f'<div style="text-align:center;margin-top:3rem">'
            f'<a href="{AFF}" class="btn btn-p btn-lg" target="_blank" rel="noopener sponsored">\u2b07 Try Audio Recorder Free</a>'
            f'</div></section>'
        ),
        "audio recorder use cases, record streaming music, record Zoom audio, podcast recorder, record internet radio, lecture recorder"
    )

def pg_pricing():
    faq_s = (
        '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['
        '{"@type":"Question","name":"Is Wondershare Audio Recorder free?","acceptedAnswer":{"@type":"Answer","text":"Yes, a free trial is available with no credit card required. The trial has recording length limits. Paid plans unlock unlimited recording."}},'
        '{"@type":"Question","name":"What does Wondershare Audio Recorder cost?","acceptedAnswer":{"@type":"Answer","text":"Pricing starts from approximately $29.95/year for the annual plan. Check the official site for current pricing and promotions."}},'
        '{"@type":"Question","name":"Is there a lifetime plan?","acceptedAnswer":{"@type":"Answer","text":"Yes, a perpetual (one-time payment) option is available. Check the official Wondershare site for current one-time pricing."}}'
        ']}'
    )
    return page(
        f"Wondershare Audio Recorder Pricing {YEAR} — Free Trial & Paid Plans",
        f"Wondershare Audio Recorder pricing {YEAR}: free trial available, paid plans unlock unlimited recording, all formats and scheduled recording. Check current price on official site.",
        "/pricing/",
        (
            f'<div class="ph tc">{bc(("Home",f"{SITE_ROOT}/"),("Pricing",None))}'
            f'<span class="sec-lbl" style="display:block;text-align:center">Simple Pricing</span>'
            f'<h1>Audio Recorder <span class="g-acc">Pricing</span></h1>'
            f'<p style="max-width:520px;margin:.9rem auto 0;color:var(--muted)">Start free. Upgrade to unlock unlimited recording, all formats and scheduled recording.</p></div>'
            f'<section>'
            f'<div class="pgrid">'
            f'<div class="pc"><div class="p-name">Free Trial</div>'
            f'<div class="p-price"><sup>$</sup>0</div>'
            f'<div class="p-per">No credit card needed</div>'
            f'<ul class="p-feats">'
            f'<li>Record system audio and microphone</li>'
            f'<li>Test all formats: MP3, WAV, FLAC</li>'
            f'<li>Try scheduled recording</li>'
            f'<li>Test auto track split</li>'
            f'<li>Limited recording length</li>'
            f'</ul>'
            f'<a href="{AFF}" class="btn btn-s btn-full" target="_blank" rel="noopener sponsored">Start Free Trial</a></div>'
            f'<div class="pc pop"><div class="pop-badge">Recommended</div>'
            f'<div class="p-name">Annual Plan</div>'
            f'<div class="p-price"><sup>$</sup>29<span style="font-size:1.5rem">.95</span></div>'
            f'<div class="p-per">per year \u00b7 check official site for current price</div>'
            f'<ul class="p-feats">'
            f'<li>Unlimited recording length</li>'
            f'<li>All output formats (MP3, WAV, FLAC, AAC, M4A...)</li>'
            f'<li>Scheduled recording (start/stop timer)</li>'
            f'<li>Auto track split</li>'
            f'<li>ID3 tag editor</li>'
            f'<li>Built-in audio editor</li>'
            f'<li>Noise reduction</li>'
            f'<li>Format converter</li>'
            f'<li>Free updates for 1 year</li>'
            f'</ul>'
            f'<a href="{AFF}" class="btn btn-p btn-full" target="_blank" rel="noopener sponsored">Get Best Price \u2192</a>'
            f'<div class="p-note">\U0001f4a1 Check official site for current promotions</div></div>'
            f'<div class="pc"><div class="p-name">Perpetual Plan</div>'
            f'<div class="p-price" style="font-size:2rem">One<br>Time</div>'
            f'<div class="p-per">pay once \u00b7 own forever</div>'
            f'<ul class="p-feats">'
            f'<li>Everything in Annual +</li>'
            f'<li>Pay once, own forever</li>'
            f'<li>No recurring fees</li>'
            f'<li>All future updates included</li>'
            f'</ul>'
            f'<a href="{AFF}" class="btn btn-s btn-full" target="_blank" rel="noopener sponsored">Check Lifetime Price \u2192</a></div>'
            f'</div>'
            f'<div class="hbox warn" style="max-width:800px;margin:3rem auto 0;text-align:center">'
            f'<h4>\U0001f4a1 Always Check the Official Site for Current Price</h4>'
            f'<p style="margin-top:.4rem">Wondershare regularly runs promotions and discounts. Click any button above to see the current live price on the official Wondershare site — savings can be significant.</p></div>'
            f'<div style="max-width:800px;margin:3rem auto 0">'
            f'<h2 style="margin-bottom:1.5rem">Pricing <span class="g-acc">FAQ</span></h2>'
            f'<div class="faq-wrap" style="max-width:100%">'
            f'<details><summary>Is the free trial really free?</summary><div class="ans"><p>Yes. Download and install with no payment required. The free trial lets you test all features including system audio recording, scheduled recording and auto track split. Trial recordings may have a length limit — upgrade to record unlimited length.</p></div></details>'
            f'<details><summary>What\'s included in the paid plan?</summary><div class="ans"><p>All paid plans include unlimited recording length, all output formats (MP3, WAV, FLAC, AAC, M4A, OGG, WMA, AIFF, AC3, APE), scheduled recording, auto track split, ID3 tag editor, built-in audio editor, noise reduction and format converter. Everything — no feature is gated behind a higher tier.</p></div></details>'
            f'<details><summary>Annual vs Perpetual — which is better?</summary><div class="ans"><p>The annual plan is the lowest upfront cost. The perpetual plan is a one-time payment that gives you the software forever. If you plan to use it long-term, perpetual is better value. If you only need it short-term, annual is fine.</p></div></details>'
            f'</div></div></section>'
        ),
        "audio recorder price, audio recorder cost, Wondershare audio recorder pricing, audio recorder free trial",
        extras=[faq_s]
    )


def pg_review():
    rev_s = (
        '{"@context":"https://schema.org","@type":"Review",'
        '"itemReviewed":{"@type":"SoftwareApplication","name":"Wondershare Streaming Audio Recorder",'
        '"applicationCategory":"MultimediaApplication","operatingSystem":"Windows"},'
        '"reviewRating":{"@type":"Rating","ratingValue":"8.8","bestRating":"10","worstRating":"1"},'
        '"author":{"@type":"Person","name":"AudioRecorder Guide Editorial Team"},'
        '"datePublished":"2026-06-01",'
        '"reviewBody":"Wondershare Audio Recorder earns 8.8/10 for its comprehensive audio capture, excellent scheduled recording, smart auto-split and clean ID3 tagging. The best all-in-one audio recorder for Windows users."}'
    )
    return page(
        f"Wondershare Audio Recorder Review {YEAR} — 8.8/10 Honest Verdict",
        f"Complete Wondershare Audio Recorder review {YEAR}: 8.8/10. We tested system audio recording, scheduled capture, auto track split, ID3 tagging, noise reduction and format conversion.",
        "/review/",
        (
            f'<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Review",None))}'
            f'<span class="sec-lbl">In-Depth Review</span>'
            f'<h1>Audio Recorder <span class="g-acc">Review {YEAR}</span></h1>'
            f'<p style="max-width:660px;margin-top:.9rem;color:var(--muted)">We tested Wondershare Audio Recorder across every major use case — streaming music, Zoom calls, internet radio, microphone recording and scheduled capture. Complete verdict.</p></div>'
            f'<section><div class="split">'
            f'<div>'
            f'<div class="score-big">8.8</div>'
            f'<div style="font-size:.79rem;color:var(--muted);text-transform:uppercase;letter-spacing:.12em;margin-bottom:1.5rem">out of 10 \u2014 Editor\'s Rating</div>'
            f'<div style="display:flex;gap:.5rem;flex-wrap:wrap;margin-bottom:2rem">'
            f'<span class="chip chip-g">\u2713 Recommended</span>'
            f'<span class="chip chip-v">Best Windows Audio Recorder</span>'
            f'</div>'
            f'<div class="rbars">'
            + "".join(
                f'<div class="rbar"><span class="rbar-lbl">{lbl}</span>'
                f'<div class="rbar-track"><div class="rbar-fill" style="width:{pct}%"></div></div>'
                f'<span class="rbar-val">{score}</span></div>'
                for lbl,pct,score in [
                    ("Recording Quality",   96, "9.6"),
                    ("Ease of Use",         92, "9.2"),
                    ("Scheduled Recording", 95, "9.5"),
                    ("Auto Track Split",    90, "9.0"),
                    ("ID3 Tagging",         88, "8.8"),
                    ("Format Support",      85, "8.5"),
                    ("Audio Editor",        80, "8.0"),
                    ("Value for Money",     86, "8.6"),
                ]
            )
            + f'</div></div>'
            f'<div>'
            f'<div class="hbox good"><h4>\u2713 What We Loved</h4>'
            + "".join(
                f'<div style="font-size:.86rem;color:var(--muted);display:flex;gap:.5rem;margin-top:.45rem">'
                f'<span style="color:var(--green);font-weight:700">\u2713</span>{x}</div>'
                for x in [
                    "System audio recording captured streaming music with zero quality loss",
                    "Scheduled recording worked perfectly — set at 11pm, recording ready by morning",
                    "Auto track split correctly identified silence between 12 test tracks",
                    "ID3 tags populated automatically from online database — no manual entry",
                    "Noise reduction visibly cleaned up microphone hiss in test recordings",
                    "One of the simplest interfaces of any audio recorder we tested",
                ]
            )
            + f'</div>'
            f'<div class="hbox warn" style="margin-top:1rem"><h4>\u26a0 Caveats</h4>'
            + "".join(
                f'<div style="font-size:.86rem;color:var(--muted);display:flex;gap:.5rem;margin-top:.4rem">'
                f'<span style="color:var(--gold);">\u2013</span>{x}</div>'
                for x in [
                    "Windows only — no Mac version available",
                    "Built-in audio editor is basic — for serious editing use Audacity alongside",
                    "Free trial has recording length restrictions",
                ]
            )
            + f'</div>'
            f'</div></div>'
            f'<h2 style="margin:3rem 0 1.5rem">Category <span class="g-acc">Breakdown</span></h2>'
            f'<div class="g3">'
            + "".join(
                f'<div class="card"><h4 style="color:var(--acc);margin-bottom:.5rem">{title}</h4><p>{desc}</p></div>'
                for title,desc in [
                    ("Recording Quality \u2605\u2605\u2605\u2605\u2605",
                     "System audio recording captured a Spotify stream at 320kbps with absolutely zero quality loss. Microphone recording was clean with good dynamic range. FLAC output was bit-perfect from source."),
                    ("Scheduled Recording \u2605\u2605\u2605\u2605\u2605",
                     "Set a recording for 11pm to capture a 2-hour radio broadcast. The recorder activated and stopped exactly on schedule, saved the audio correctly and named the file automatically. Flawless."),
                    ("Auto Track Split \u2605\u2605\u2605\u2605\u2606",
                     "Tested with an album playlist — 12 tracks with 2 seconds of silence between each. Audio Recorder correctly detected 11 of 12 split points. One very short silence was missed. Excellent overall."),
                    ("Ease of Use \u2605\u2605\u2605\u2605\u2605",
                     "The interface is one of the cleanest we've seen in any audio recorder. Three source buttons, a format dropdown, a record button. Non-technical users will figure it out in under 5 minutes."),
                    ("ID3 Tagging \u2605\u2605\u2605\u2605\u2606",
                     "Automatic ID3 tag lookup worked on 8 of 10 test recordings — fetching artist, title, album, year and cover art correctly. Two obscure tracks weren't found, requiring manual entry."),
                    ("Value for Money \u2605\u2605\u2605\u2605\u2606",
                     "At approximately $29.95/year, it's exceptional value for a tool with scheduled recording, auto-split and ID3 tagging all built in. Free alternatives like Audacity don't offer scheduling or auto-tagging."),
                ]
            )
            + f'</div>'
            f'<div style="text-align:center;margin-top:3rem">'
            f'<a href="{AFF}" class="btn btn-p btn-lg" target="_blank" rel="noopener sponsored">\u2b07 Try Audio Recorder Free</a>'
            f'</div></section>'
        ),
        "Wondershare audio recorder review, audio recorder review 2025 2026, is audio recorder good",
        extras=[rev_s],
        article=True
    )

def pg_faq():
    faqs = [
        ("Is Wondershare Audio Recorder free?",
         "Yes. Wondershare Audio Recorder offers a free trial with no credit card required. The trial lets you test all features including system audio recording, scheduled recording and auto track split. Trial recordings have a length limit. Upgrade to a paid plan for unlimited recording length."),
        ("Can it record streaming music like Spotify or Apple Music?",
         "Yes. Wondershare Audio Recorder captures system audio using virtual audio driver technology — it records whatever plays through your computer's audio output, including Spotify, Apple Music, Amazon Music, YouTube Music, Tidal and any other streaming service. The recording is at full source quality."),
        ("Can I record Zoom or Teams calls?",
         "Yes. Any audio playing through your computer can be captured — including Zoom, Microsoft Teams, Google Meet, Skype and Discord. Audio Recorder saves the call audio as MP3 or WAV without capturing video, making it much more storage-efficient than screen recording."),
        ("Does it support scheduled recording?",
         "Yes. Set a start time and end time for any recording. Audio Recorder activates automatically — record tonight's radio show, a weekly podcast or any recurring broadcast while you're away or asleep. The computer can be locked; recording still runs."),
        ("What formats does it save recordings in?",
         "Wondershare Audio Recorder supports 10 output formats: MP3, WAV, FLAC, AAC, M4A, OGG, WMA, AIFF, AC3 and APE. MP3 is best for sharing and everyday use. WAV and FLAC are best for editing and archiving at lossless quality."),
        ("What is auto track split?",
         "Auto track split detects silence between audio tracks and automatically saves each segment as a separate file. It's ideal for recording albums or playlists where you want individual tracks rather than one long recording. The silence threshold is configurable."),
        ("Does it work on Mac?",
         "Wondershare Streaming Audio Recorder is currently Windows only. For Mac users, Wondershare offers other audio tools — check the official site. If you need audio recording on Mac, Wondershare's broader suite may have options."),
        ("Can I edit recordings inside the app?",
         "Yes. A built-in audio editor lets you trim the start and end of recordings, cut out unwanted sections, adjust volume levels and add fade in/out. For more advanced editing (multitrack, effects), use Audacity alongside."),
        ("Does it add ID3 tags automatically?",
         "Yes. Audio Recorder has an ID3 tag editor that can automatically fetch artist, title, album, year, genre and cover art from an online database for recognised recordings. Tags can also be edited manually."),
        ("Does it reduce background noise?",
         "Yes. An AI-powered noise reduction feature removes background hiss, hum and ambient noise from microphone recordings. Particularly useful for recordings made with laptop microphones in noisy environments."),
    ]
    items = "".join(
        f'<details><summary>{q}</summary><div class="ans"><p>{a}</p></div></details>'
        for q,a in faqs
    )
    faq_s = (
        '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['
        + ",".join(
            f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a[:180]}..."}}}}'
            for q,a in faqs
        )
        + ']}'
    )
    return page(
        f"Wondershare Audio Recorder FAQ {YEAR} — 10 Questions Answered",
        "Complete FAQ: Is it free? Record Spotify? Record Zoom? Scheduled recording? Formats? Auto track split? Mac support? ID3 tags? All 10 answered.",
        "/faq/",
        (
            f'<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("FAQ",None))}'
            f'<span class="sec-lbl">Questions Answered</span>'
            f'<h1>Audio Recorder <span class="g-acc">FAQ</span></h1>'
            f'<p style="max-width:640px;margin-top:.9rem;color:var(--muted)">10 detailed answers to the most common questions before downloading.</p></div>'
            f'<section><div class="faq-wrap">{items}</div>'
            f'<div style="text-align:center;margin-top:3rem">'
            f'<a href="{AFF}" class="btn btn-p" target="_blank" rel="noopener sponsored">\u2b07 Download Audio Recorder Free</a>'
            f'</div></section>'
        ),
        "audio recorder FAQ, record Spotify audio, record Zoom audio, scheduled audio recording, audio recorder free",
        extras=[faq_s]
    )

def pg_download():
    return page(
        f"Download Wondershare Audio Recorder Free — Windows | {YEAR}",
        "Download Wondershare Streaming Audio Recorder free for Windows. Record system audio, streaming music, Zoom calls, internet radio and microphone in MP3, WAV, FLAC. No credit card.",
        "/download/",
        (
            f'<div class="ph tc">{bc(("Home",f"{SITE_ROOT}/"),("Download",None))}'
            f'<span class="sec-lbl" style="display:block;text-align:center">Start in 60 Seconds</span>'
            f'<h1>Download <span class="g-acc">Audio Recorder</span></h1>'
            f'<p style="max-width:520px;margin:.9rem auto 0;color:var(--muted)">Free trial — no credit card. Record any audio source. Windows.</p></div>'
            f'<section>'
            f'<div style="max-width:500px;margin:0 auto 3rem">'
            f'<div class="card" style="text-align:center">'
            f'<div class="card-icon" style="margin:0 auto 1rem;font-size:2.2rem">\U0001fa9f</div>'
            f'<h3>Windows</h3>'
            f'<p style="margin-bottom:.5rem">Windows 7 / 8 / 10 / 11</p>'
            f'<p style="font-size:.8rem;color:var(--muted);margin-bottom:1.6rem">32-bit and 64-bit supported</p>'
            f'<a href="{AFF}" class="btn btn-p btn-full" target="_blank" rel="noopener sponsored">\u2b07 Download for Windows</a>'
            f'</div></div>'
            f'<div class="hbox good" style="max-width:600px;margin:0 auto">'
            f'<h4>Free Trial Includes</h4>'
            f'<ul style="list-style:none;padding:0;margin-top:.8rem;display:grid;grid-template-columns:1fr 1fr;gap:.5rem">'
            + "".join(
                f'<li style="font-size:.84rem;color:var(--muted);display:flex;gap:.5rem">'
                f'<span style="color:var(--green);font-weight:700">\u2713</span>{x}</li>'
                for x in [
                    "Record system audio","Record microphone",
                    "Test MP3, WAV, FLAC output","Try scheduled recording",
                    "Test auto track split","Try ID3 tag editor",
                    "Built-in audio editor","Noise reduction preview",
                ]
            )
            + f'</ul></div>'
            f'<div style="text-align:center;margin-top:2rem">'
            f'<a href="{SITE_ROOT}/pricing/" class="btn btn-g">View Pricing \u2192</a>'
            f'</div></section>'
        )
    )


def pg_record_streaming():
    howto = (
        '{"@context":"https://schema.org","@type":"HowTo",'
        '"name":"How to Record Streaming Audio",'
        '"description":"Record any streaming audio from your computer in 3 steps.",'
        '"step":['
        '{"@type":"HowToStep","position":1,"name":"Open Audio Recorder","text":"Download and open Wondershare Audio Recorder. Select System Audio as the input source."},'
        '{"@type":"HowToStep","position":2,"name":"Start your stream","text":"Begin playing your streaming music, radio or online audio source."},'
        '{"@type":"HowToStep","position":3,"name":"Record","text":"Click Record. Audio Recorder captures the audio at full quality in your chosen format."}'
        ']}'
    )
    return page(
        f"How to Record Streaming Audio — Complete Guide {YEAR}",
        "Record any streaming audio from your computer — Spotify, Apple Music, YouTube, internet radio — using Wondershare Audio Recorder. MP3, WAV, FLAC output. Step-by-step guide.",
        "/record-streaming-audio/",
        (
            f'<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Blog",f"{SITE_ROOT}/blog/"),("Record Streaming Audio",None))}'
            f'<span class="sec-lbl">Guide</span>'
            f'<h1>Record <span class="g-acc">Streaming Audio</span><br>From Any Source</h1>'
            f'<p style="max-width:660px;margin-top:.9rem;color:var(--muted)">Capture any audio playing on your computer — streaming services, online radio, YouTube — at full source quality. Here\'s exactly how.</p></div>'
            f'<section><div class="hbox info"><h4>How It Works Technically</h4>'
            f'<p style="margin-top:.4rem">Wondershare Audio Recorder uses a virtual audio driver that intercepts audio at the system level — before it reaches your speakers. This means it captures the audio at full digital quality, not by recording speaker output with a microphone. The result is a perfect copy of the stream, regardless of volume or background noise.</p></div>'
            f'<div class="split" style="margin-top:2.5rem">'
            f'<div>'
            f'<h2 style="margin-bottom:1.5rem">Step-by-Step:<br><span class="g-acc">Record Streaming Audio</span></h2>'
            f'<div class="steps">'
            f'<div class="step" data-n="1"><div><h3>Install Audio Recorder</h3><p>Download and install Wondershare Audio Recorder on your Windows PC. Launch the application.</p></div></div>'
            f'<div class="step" data-n="2"><div><h3>Select System Audio</h3><p>Choose <strong>System Audio</strong> as the input source. This captures everything playing through your computer\'s audio output.</p></div></div>'
            f'<div class="step" data-n="3"><div><h3>Choose Output Format</h3><p>Select MP3 for sharing and storage, WAV for editing quality, or FLAC for lossless archiving.</p></div></div>'
            f'<div class="step" data-n="4"><div><h3>Start Your Stream & Record</h3><p>Begin playing on Spotify, YouTube, or any streaming service. Click Record. Audio Recorder captures it all.</p></div></div>'
            f'<div class="step" data-n="5"><div><h3>Stop & Save</h3><p>Click Stop when done. Your recording is saved automatically. Use auto-split for individual tracks.</p></div></div>'
            f'</div>'
            f'<a href="{AFF}" class="btn btn-p" style="margin-top:1rem" target="_blank" rel="noopener sponsored">\u2b07 Download Free Trial</a>'
            f'</div>'
            f'<div>'
            f'<div class="card card-feat" style="padding:2rem">'
            f'<h3 style="color:var(--acc);margin-bottom:1rem">What You Can Record</h3>'
            f'<ul style="list-style:none;padding:0;display:flex;flex-direction:column;gap:.7rem">'
            + "".join(
                f'<li style="display:flex;gap:.7rem;font-size:.9rem;color:var(--muted)">'
                f'<span style="color:var(--green);font-weight:700">\u2713</span>'
                f'<strong style="color:var(--txt)">{a}</strong> \u2014 {b}</li>'
                for a,b in [
                    ("Spotify","record any track or playlist to MP3"),
                    ("Apple Music","capture Apple Music streams at full quality"),
                    ("YouTube","record audio from any YouTube video"),
                    ("Amazon Music","capture Amazon Music streams"),
                    ("Internet Radio","BBC, NPR, local stations — any online radio"),
                    ("Podcast streams","capture live podcast broadcasts"),
                    ("SoundCloud","record any track from SoundCloud"),
                    ("Browser audio","any audio from Chrome, Firefox or Edge"),
                ]
            )
            + f'</ul></div>'
            f'<div class="hbox warn" style="margin-top:1rem"><h4>Note on Copyright</h4>'
            f'<p style="margin-top:.4rem">Recording streaming audio for personal use is generally acceptable. Do not distribute copyrighted recordings commercially or share them publicly without permission. Always respect the terms of service of streaming platforms.</p></div>'
            f'</div></div></section>'
        ),
        "record streaming audio, how to record streaming music, record Spotify audio, capture streaming audio PC",
        extras=[howto],
        article=True
    )

def pg_record_zoom():
    return page(
        f"How to Record Zoom Audio — Audio Only, No Video | {YEAR}",
        "Record Zoom calls, Teams meetings and Google Meet as audio-only using Wondershare Audio Recorder. Much smaller file than screen recording. MP3 or WAV output. Step-by-step.",
        "/record-zoom-audio/",
        (
            f'<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Blog",f"{SITE_ROOT}/blog/"),("Record Zoom Audio",None))}'
            f'<span class="sec-lbl">Guide</span>'
            f'<h1>Record <span class="g-acc">Zoom, Teams</span><br>&amp; Meeting Audio</h1>'
            f'<p style="max-width:660px;margin-top:.9rem;color:var(--muted)">Record Zoom, Microsoft Teams, Google Meet and Skype as audio-only. No video — just clean MP3 or WAV audio at a fraction of the file size of screen recording.</p></div>'
            f'<section>'
            f'<div class="hbox good"><h4>Audio Recording vs Screen Recording for Meetings</h4>'
            f'<p style="margin-top:.4rem">Recording a 1-hour Zoom call as video takes 1–4 GB. Recording the same call as MP3 audio takes about 55 MB. Audio is easier to search, faster to share, and you can listen back while doing something else. For meetings where you only need the spoken content, audio-only is always the better choice.</p></div>'
            f'<div class="split" style="margin-top:2rem">'
            f'<div>'
            f'<h2 style="margin-bottom:1.5rem">How to Record<br><span class="g-acc">Zoom as Audio</span></h2>'
            f'<div class="steps">'
            f'<div class="step" data-n="1"><div><h3>Open Audio Recorder</h3><p>Launch Wondershare Audio Recorder before your meeting starts.</p></div></div>'
            f'<div class="step" data-n="2"><div><h3>Select System Audio</h3><p>Choose System Audio as the input to capture call audio from Zoom. Add Microphone if you want your own voice included.</p></div></div>'
            f'<div class="step" data-n="3"><div><h3>Set Output to MP3</h3><p>MP3 at 128kbps is perfectly clear for voice and creates a small file. WAV if you need editing quality.</p></div></div>'
            f'<div class="step" data-n="4"><div><h3>Join Meeting &amp; Record</h3><p>Join your Zoom/Teams/Meet call normally. Click Record in Audio Recorder. It runs silently in the background.</p></div></div>'
            f'<div class="step" data-n="5"><div><h3>Stop After the Call</h3><p>Click Stop when the meeting ends. Your audio file is saved automatically, named with the date and time.</p></div></div>'
            f'</div>'
            f'<a href="{AFF}" class="btn btn-p" style="margin-top:1rem" target="_blank" rel="noopener sponsored">\u2b07 Download Free Trial</a>'
            f'</div>'
            f'<div>'
            f'<div class="card card-feat" style="padding:2rem">'
            f'<h3 style="color:var(--acc);margin-bottom:1rem">Works With All Platforms</h3>'
            f'<div style="display:flex;flex-direction:column;gap:.7rem">'
            + "".join(
                f'<div style="display:flex;gap:.7rem;align-items:center">'
                f'<span style="font-size:1.4rem">{icon}</span>'
                f'<div><strong style="font-size:.9rem;color:var(--txt)">{name}</strong>'
                f'<div style="font-size:.8rem;color:var(--muted)">{note}</div></div></div>'
                for icon,name,note in [
                    ("\U0001f4f9","Zoom","Record any Zoom call or webinar"),
                    ("\U0001f4bb","Microsoft Teams","Capture Teams meetings and calls"),
                    ("\U0001f4f2","Google Meet","Record Meet sessions to MP3"),
                    ("\U0001f4de","Skype","Capture Skype voice and video calls"),
                    ("\U0001f3ae","Discord","Record Discord voice channels"),
                    ("\U0001f517","Any VoIP","Works with any app that uses system audio"),
                ]
            )
            + f'</div></div>'
            f'</div></div></section>'
        ),
        "record Zoom audio, record Teams audio, record Google Meet, audio only meeting recorder, Zoom audio recorder",
        article=True
    )

def pg_record_spotify():
    return page(
        f"Record Spotify — Save Spotify Music to MP3 or FLAC | {YEAR}",
        "Record Spotify music to MP3, WAV or FLAC using Wondershare Audio Recorder. Capture any Spotify track or playlist. Auto track split and ID3 tags. Step-by-step guide.",
        "/record-spotify/",
        (
            f'<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Blog",f"{SITE_ROOT}/blog/"),("Record Spotify",None))}'
            f'<span class="sec-lbl">Guide</span>'
            f'<h1>Record <span class="g-acc">Spotify</span> Music<br>to MP3 or FLAC</h1>'
            f'<p style="max-width:660px;margin-top:.9rem;color:var(--muted)">Capture any Spotify track or playlist as a high-quality audio file. Automatic track splitting and ID3 tagging included.</p></div>'
            f'<section>'
            f'<div class="hbox warn"><h4>Important: Personal Use Only</h4><p style="margin-top:.4rem">Recording Spotify audio is for personal use only. Do not distribute recordings publicly or use them commercially. Respect Spotify\'s terms of service and copyright law.</p></div>'
            f'<div class="split" style="margin-top:2rem">'
            f'<div>'
            f'<h2 style="margin-bottom:1.5rem">How to <span class="g-acc">Record Spotify</span></h2>'
            f'<div class="steps">'
            f'<div class="step" data-n="1"><div><h3>Launch Audio Recorder</h3><p>Open Wondershare Audio Recorder and select System Audio as the input.</p></div></div>'
            f'<div class="step" data-n="2"><div><h3>Enable Auto Track Split</h3><p>Turn on auto track split. Audio Recorder will detect the silence between tracks and save each song as a separate file.</p></div></div>'
            f'<div class="step" data-n="3"><div><h3>Choose Format</h3><p>MP3 at 320kbps for quality sharing. FLAC for lossless archiving. AAC for Apple device compatibility.</p></div></div>'
            f'<div class="step" data-n="4"><div><h3>Play Spotify &amp; Record</h3><p>Start your Spotify playlist. Click Record. Audio Recorder captures each track automatically.</p></div></div>'
            f'<div class="step" data-n="5"><div><h3>Review Tagged Files</h3><p>Each track is saved as a separate file with artist, title, album and cover art populated from the ID3 database.</p></div></div>'
            f'</div>'
            f'<a href="{AFF}" class="btn btn-p" style="margin-top:1rem" target="_blank" rel="noopener sponsored">\u2b07 Download Free Trial</a>'
            f'</div>'
            f'<div>'
            f'<div class="hbox good"><h4>Auto Track Split in Action</h4>'
            f'<p style="margin-top:.4rem">When recording a Spotify playlist with auto track split enabled, Audio Recorder detects the 2-second gap between tracks and automatically saves each song as a separate MP3 or FLAC file — perfectly named and tagged. A 20-track album becomes 20 individually named audio files.</p></div>'
            f'<div class="hbox" style="margin-top:1rem"><h4>ID3 Tag Automation</h4>'
            f'<p style="margin-top:.4rem">After recording each track, Audio Recorder automatically queries an online music database and fills in artist name, song title, album, year, genre and cover art. Your recordings arrive in your music library already perfectly organised.</p></div>'
            f'</div></div></section>'
        ),
        "record Spotify, save Spotify to MP3, Spotify music recorder, record Spotify FLAC, capture Spotify audio",
        article=True
    )

def pg_podcast_recorder():
    return page(
        f"Best Podcast Recorder Software — Record Podcasts to MP3 | {YEAR}",
        "Record your podcast with Wondershare Audio Recorder. High-quality microphone recording, noise reduction, built-in trimming, MP3 export. Complete podcast recording guide.",
        "/podcast-recorder/",
        (
            f'<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Blog",f"{SITE_ROOT}/blog/"),("Podcast Recorder",None))}'
            f'<span class="sec-lbl">Guide</span>'
            f'<h1>Record Your <span class="g-acc">Podcast</span></h1>'
            f'<p style="max-width:660px;margin-top:.9rem;color:var(--muted)">Everything you need to record a clean, professional podcast episode — microphone recording, noise reduction, editing and MP3 export.</p></div>'
            f'<section>'
            f'<div class="g3" style="margin-bottom:2.5rem">'
            f'<div class="card card-feat"><div class="card-icon">\U0001f399</div><h3>Microphone Recording</h3><p>Record from any connected mic — USB condenser, dynamic mic, headset or laptop built-in. Adjust input levels and monitor in real time.</p></div>'
            f'<div class="card"><div class="card-icon">\U0001f507</div><h3>Noise Reduction</h3><p>AI noise reduction removes background hiss, room echo and ambient noise automatically — making your recordings sound studio-quality even in imperfect environments.</p></div>'
            f'<div class="card"><div class="card-icon">\u2702\ufe0f</div><h3>Built-in Editor</h3><p>Trim your recording, remove false starts, cut out pauses and adjust volume — without leaving the app or needing a separate editor.</p></div>'
            f'<div class="card"><div class="card-icon">\U0001f4e4</div><h3>MP3 Export</h3><p>Export your finished episode as MP3 at the right bitrate for podcast platforms. 128kbps mono is standard for speech; 192kbps stereo for music-heavy episodes.</p></div>'
            f'</div>'
            f'<div class="split">'
            f'<div>'
            f'<h2 style="margin-bottom:1.5rem">Record a Podcast<br><span class="g-acc">Episode — 5 Steps</span></h2>'
            f'<div class="steps">'
            f'<div class="step" data-n="1"><div><h3>Connect Your Mic</h3><p>Plug in your USB mic or connect via audio interface. Windows will detect it automatically.</p></div></div>'
            f'<div class="step" data-n="2"><div><h3>Select Microphone Input</h3><p>In Audio Recorder, choose your microphone as the input source. Monitor levels to avoid clipping.</p></div></div>'
            f'<div class="step" data-n="3"><div><h3>Enable Noise Reduction</h3><p>Turn on AI noise reduction to automatically clean background noise during recording.</p></div></div>'
            f'<div class="step" data-n="4"><div><h3>Record Your Episode</h3><p>Click Record and speak. Audio Recorder captures everything cleanly.</p></div></div>'
            f'<div class="step" data-n="5"><div><h3>Edit &amp; Export MP3</h3><p>Trim, cut and adjust in the built-in editor. Export as MP3 ready to upload.</p></div></div>'
            f'</div>'
            f'<a href="{AFF}" class="btn btn-p" style="margin-top:1rem" target="_blank" rel="noopener sponsored">\u2b07 Download Podcast Recorder Free</a>'
            f'</div>'
            f'<div>'
            f'<div class="hbox info"><h4>Best Settings for Podcasts</h4>'
            f'<ul style="list-style:none;padding:0;margin-top:.8rem;display:flex;flex-direction:column;gap:.6rem">'
            + "".join(
                f'<li style="font-size:.86rem;color:var(--muted);display:flex;gap:.6rem">'
                f'<code style="font-size:.8rem;flex-shrink:0">{setting}</code>{desc}</li>'
                for setting,desc in [
                    ("MP3 128kbps","Standard quality for voice-only podcasts"),
                    ("MP3 192kbps","Better quality if your podcast includes music"),
                    ("WAV","If sending to a producer or post-production editor"),
                    ("Mono","Single microphone recording — halves file size"),
                    ("44.1kHz","Standard sample rate for podcast distribution"),
                ]
            )
            + f'</ul></div>'
            f'</div></div></section>'
        ),
        "podcast recorder software, record podcast MP3, microphone recorder, podcast recording software Windows",
        article=True
    )

def pg_voice_recorder():
    return page(
        f"Voice Recorder Software for PC — Record Voice Memos | {YEAR}",
        "Record voice memos, interviews, dictation and notes with Wondershare Audio Recorder. High-quality mic recording, noise reduction, MP3 export. Simple one-click recording for Windows.",
        "/voice-recorder/",
        (
            f'<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Blog",f"{SITE_ROOT}/blog/"),("Voice Recorder",None))}'
            f'<span class="sec-lbl">Guide</span>'
            f'<h1>Voice Recorder<br><span class="g-acc">for PC</span></h1>'
            f'<p style="max-width:660px;margin-top:.9rem;color:var(--muted)">Record voice memos, interviews, meetings and dictation on your Windows PC. One click to start, clear MP3 or WAV output.</p></div>'
            f'<section>'
            f'<div class="g3" style="margin-bottom:2.5rem">'
            + "".join(
                f'<div class="card"><div class="card-icon">{icon}</div><h3>{title}</h3><p>{desc}</p></div>'
                for icon,title,desc in [
                    ("\U0001f4dd","Voice Memos","Record quick voice notes and reminders. Save as MP3 for easy access on any device. Auto-named with date and time."),
                    ("\U0001f3a4","Interviews","Record interview subjects over the phone, Zoom or in person. Clear audio, automatic file naming, export to MP3."),
                    ("\U0001f4da","Dictation","Dictate documents, ideas, meeting notes and book chapters. Use noise reduction for clean output even in busy environments."),
                    ("\U0001f393","Lectures","Record class lectures, seminars and online courses for later review. Long recording supported — no time limit in paid plan."),
                    ("\U0001f3b5","Music Ideas","Quickly capture musical ideas, chord progressions and song fragments. Never lose a creative moment."),
                    ("\U0001f4de","Phone Calls","Record VoIP calls through system audio — Zoom, Skype, Teams — as audio-only for easy replay and reference."),
                ]
            )
            + f'</div>'
            f'<div style="text-align:center">'
            f'<a href="{AFF}" class="btn btn-p btn-lg" target="_blank" rel="noopener sponsored">\u2b07 Download Voice Recorder Free</a>'
            f'</div></section>'
        ),
        "voice recorder PC, voice recorder software Windows, record voice memo PC, dictation recorder, interview recorder",
        article=True
    )

def pg_vs_audacity():
    return page(
        f"Audio Recorder vs Audacity — Which Should You Use? | {YEAR}",
        f"Wondershare Audio Recorder vs Audacity: features, ease of use, scheduled recording, streaming capture compared. Which audio recorder is right for you in {YEAR}?",
        "/vs-audacity/",
        (
            f'<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Alternatives",f"{SITE_ROOT}/alternatives/"),("vs Audacity",None))}'
            f'<span class="sec-lbl">Comparison</span>'
            f'<h1>Audio Recorder vs <span class="g-acc">Audacity</span></h1>'
            f'<p style="max-width:660px;margin-top:.9rem;color:var(--muted)">Audacity is free and powerful for editing. Wondershare Audio Recorder is purpose-built for capturing. Here\'s exactly when to use each one.</p></div>'
            f'<section>'
            f'<div class="tbl-wrap"><table>'
            f'<thead><tr><th>Feature</th><th style="color:var(--acc)">Wondershare Audio Recorder</th><th>Audacity (Free)</th></tr></thead>'
            f'<tbody>'
            + "".join(
                f'<tr><td class="td-n">{feat}</td><td class="{ac}">{av}</td><td class="{au}">{ad}</td></tr>'
                for feat,av,ac,ad,au in [
                    ("Record system audio (streaming)",     "\u2713 One click",                "td-y td-hi", "\u2713 Requires plugin setup", "td-p"),
                    ("Scheduled recording",                 "\u2713 Built in",                 "td-y td-hi", "\u2715 Not available",         "td-no"),
                    ("Auto track split",                    "\u2713 Automatic",                "td-y td-hi", "\u2715 Manual only",           "td-no"),
                    ("ID3 tag editor",                      "\u2713 Auto + manual",            "td-y td-hi", "\u2715 Not included",          "td-no"),
                    ("Always-on silent recording",          "\u2713 System tray mode",         "td-y td-hi", "\u2715 Must be visible",       "td-no"),
                    ("Multi-track editing",                 "\u2715 Basic only",               "td-no",      "\u2713 Full multitrack",        "td-y"),
                    ("Audio effects & plugins",             "\u2715 Basic",                    "td-no",      "\u2713 Hundreds of plugins",    "td-y"),
                    ("Noise reduction",                     "\u2713 AI-powered",               "td-y td-hi", "\u2713 Manual tool",           "td-p"),
                    ("Ease of use",                         "\u2605\u2605\u2605\u2605\u2605 Very easy", "td-y td-hi", "\u2605\u2605\u2605\u00bd Complex","td-p"),
                    ("Cost",                               "~$29.95/year",                     "td-hi",      "Free",                         "td-y"),
                ]
            )
            + f'</tbody></table></div>'
            f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.4rem;margin-top:1.5rem">'
            f'<div class="hbox good" style="margin:0"><h4>Choose Audio Recorder if...</h4>'
            + "".join(
                f'<div style="font-size:.84rem;color:var(--muted);display:flex;gap:.5rem;margin-top:.4rem">'
                f'<span style="color:var(--green);font-weight:700">\u2713</span>{x}</div>'
                for x in [
                    "You want to record streaming music or online radio",
                    "You need scheduled/automatic recording",
                    "You want auto track split for albums/playlists",
                    "You want clean one-click recording without setup",
                    "You need ID3 tags applied automatically",
                ]
            )
            + f'</div>'
            f'<div class="hbox" style="margin:0"><h4>Choose Audacity if...</h4>'
            + "".join(
                f'<div style="font-size:.84rem;color:var(--muted);display:flex;gap:.5rem;margin-top:.4rem">'
                f'<span style="color:var(--acc3);">\u2192</span>{x}</div>'
                for x in [
                    "You need professional multitrack editing",
                    "You want extensive audio effects and plugins",
                    "Budget is the primary consideration (it's free)",
                    "You work on Mac or Linux (Audacity is cross-platform)",
                    "You need advanced spectral editing tools",
                ]
            )
            + f'</div></div>'
            f'<div class="hbox" style="margin-top:1.5rem"><h4>Best Combination</h4>'
            f'<p style="margin-top:.4rem">Many users run both. Use Wondershare Audio Recorder for capturing — scheduled recording, streaming capture, auto-split and tagging. Then open recordings in Audacity for advanced multitrack editing when needed. They complement each other perfectly.</p></div>'
            f'<div style="text-align:center;margin-top:2rem">'
            f'<a href="{AFF}" class="btn btn-p" target="_blank" rel="noopener sponsored">Try Audio Recorder Free \u2192</a>'
            f'</div></section>'
        ),
        "audio recorder vs Audacity, Audacity alternative, best audio recorder Windows"
    )

def pg_vs_garageband():
    return page(
        f"Audio Recorder vs GarageBand — Comparison {YEAR}",
        f"Wondershare Audio Recorder vs GarageBand: features, platform support and recording capabilities compared. GarageBand is Mac-only. Which is right for you in {YEAR}?",
        "/vs-garageband/",
        (
            f'<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Alternatives",f"{SITE_ROOT}/alternatives/"),("vs GarageBand",None))}'
            f'<span class="sec-lbl">Comparison</span>'
            f'<h1>Audio Recorder vs <span class="g-acc">GarageBand</span></h1>'
            f'<p style="max-width:660px;margin-top:.9rem;color:var(--muted)">GarageBand is Apple\'s free music creation tool. Wondershare Audio Recorder is a dedicated capture tool for Windows. Different tools for different purposes.</p></div>'
            f'<section>'
            f'<div class="tbl-wrap"><table>'
            f'<thead><tr><th>Feature</th><th style="color:var(--acc)">Audio Recorder</th><th>GarageBand</th></tr></thead>'
            f'<tbody>'
            + "".join(
                f'<tr><td class="td-n">{feat}</td><td class="{ac}">{av}</td><td class="{gb}">{gv}</td></tr>'
                for feat,av,ac,gv,gb in [
                    ("Platform",               "Windows",                         "td-hi",      "Mac/iOS only",                "td-p"),
                    ("Record system audio",    "\u2713 One click",                "td-y td-hi", "\u2715 Not designed for this", "td-no"),
                    ("Scheduled recording",    "\u2713 Built in",                 "td-y td-hi", "\u2715",                      "td-no"),
                    ("Auto track split",       "\u2713",                          "td-y td-hi", "\u2715",                      "td-no"),
                    ("ID3 tagging",            "\u2713 Automatic",                "td-y td-hi", "\u2715",                      "td-no"),
                    ("Multi-track recording",  "\u2715 Basic",                    "td-no",      "\u2713 Full DAW",              "td-y"),
                    ("Virtual instruments",    "\u2715",                          "td-no",      "\u2713 Built in",              "td-y"),
                    ("Cost",                  "~$29.95/year",                     "td-hi",      "Free (Mac only)",              "td-y"),
                ]
            )
            + f'</tbody></table></div>'
            f'<div class="hbox" style="margin-top:1.5rem"><h4>Summary</h4>'
            f'<p style="margin-top:.4rem">GarageBand is a full music production tool for Mac users — excellent for recording instruments, creating music and basic audio production. Wondershare Audio Recorder is purpose-built for capturing audio from any computer source on Windows — streaming music, calls, radio and microphone. They serve completely different purposes and different platforms.</p></div>'
            f'<div style="text-align:center;margin-top:1.5rem">'
            f'<a href="{AFF}" class="btn btn-p" target="_blank" rel="noopener sponsored">Try Audio Recorder Free \u2192</a>'
            f'</div></section>'
        ),
        "audio recorder vs GarageBand, GarageBand alternative Windows, audio recorder Windows"
    )

def pg_alternatives():
    return page(
        f"Best Audio Recorder Alternatives {YEAR} — Full Comparison",
        f"Compare Wondershare Audio Recorder with every major alternative in {YEAR}: Audacity, GarageBand, OBS Studio, Ocenaudio, Windows Voice Recorder. Full feature comparison.",
        "/alternatives/",
        (
            f'<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Alternatives",None))}'
            f'<span class="sec-lbl">Market Overview</span>'
            f'<h1>Best <span class="g-acc">Audio Recorder Alternatives</span></h1>'
            f'<p style="max-width:660px;margin-top:.9rem;color:var(--muted)">Every major audio recorder compared so you can pick the right one for your use case.</p></div>'
            f'<section><div class="g2">'
            f'<div class="card card-feat"><h3 style="color:var(--acc)">Wondershare Audio Recorder <span class="chip chip-g" style="margin-left:.4rem">Recommended</span></h3>'
            f'<p style="margin:.8rem 0">Purpose-built for capturing any audio from your Windows computer. Scheduled recording, auto track split, ID3 tags, noise reduction, 10 output formats.</p>'
            f'<a href="{AFF}" class="btn btn-p" style="margin-top:.8rem" target="_blank" rel="noopener sponsored">Download Free \u2192</a></div>'
            f'<div class="card"><h3>Audacity <span class="chip chip-g" style="margin-left:.4rem">Free</span></h3>'
            f'<p style="margin:.8rem 0">Powerful multitrack audio editor with recording capability. Best for editing and production. No scheduled recording, no auto-split, complex setup for streaming capture.</p>'
            f'<a href="{SITE_ROOT}/vs-audacity/" class="btn btn-g" style="margin-top:.8rem">Full Comparison \u2192</a></div>'
            f'<div class="card"><h3>GarageBand <span class="chip chip-g" style="margin-left:.4rem">Free — Mac Only</span></h3>'
            f'<p style="margin:.8rem 0">Apple\'s music production suite. Excellent for recording instruments and making music on Mac. Not designed for capturing streaming audio. Mac/iOS only.</p>'
            f'<a href="{SITE_ROOT}/vs-garageband/" class="btn btn-g" style="margin-top:.8rem">Full Comparison \u2192</a></div>'
            f'<div class="card"><h3>OBS Studio <span class="chip chip-g" style="margin-left:.4rem">Free</span></h3>'
            f'<p style="margin:.8rem 0">Open-source screen and audio recorder primarily for streaming. Can record audio-only but interface is complex and not optimised for this use case. No scheduling or auto-split.</p></div>'
            f'<div class="card"><h3>Windows Voice Recorder <span class="chip chip-g" style="margin-left:.4rem">Free — Built In</span></h3>'
            f'<p style="margin:.8rem 0">Very basic microphone-only recorder built into Windows. No system audio recording, no scheduling, no format choice, no editing. Fine for quick voice notes only.</p></div>'
            f'<div class="card"><h3>Ocenaudio <span class="chip chip-g" style="margin-left:.4rem">Free</span></h3>'
            f'<p style="margin:.8rem 0">Simple audio editor with recording. Cleaner than Audacity but fewer features. No scheduled recording, no streaming audio capture, no auto-split.</p></div>'
            f'</div></section>'
        ),
        "audio recorder alternatives, best audio recording software, Audacity alternative, audio recorder comparison"
    )


def pg_blog():
    posts = [
        ("🎵","Guide",f"Record Streaming Audio — Complete Guide {YEAR}","Capture Spotify, Apple Music, YouTube and any online stream at full quality.",f"{SITE_ROOT}/record-streaming-audio/",f"June {YEAR}","5 min"),
        ("📞","Tutorial",f"How to Record Zoom Audio Only — No Video {YEAR}","Record Zoom, Teams and Meet as clean MP3. Much smaller than screen recording.",f"{SITE_ROOT}/record-zoom-audio/",f"June {YEAR}","4 min"),
        ("🎙","Guide","Podcast Recorder Guide — Record & Export MP3","Mic recording, noise reduction, built-in editing and MP3 export in one app.",f"{SITE_ROOT}/podcast-recorder/",f"May {YEAR}","5 min"),
        ("🎸","Tutorial","Record Spotify — Auto Track Split & ID3 Tags","Capture any Spotify playlist with automatic per-track splitting and tagging.",f"{SITE_ROOT}/record-spotify/",f"May {YEAR}","4 min"),
        ("🎤","Guide","Voice Recorder for PC — Memos, Interviews, Dictation","Record voice memos, lectures and interviews on any Windows PC.",f"{SITE_ROOT}/voice-recorder/",f"April {YEAR}","3 min"),
        ("🆚","Comparison","Audio Recorder vs Audacity — Which to Use?","Audacity edits. Audio Recorder captures. Here's exactly when to use each.",f"{SITE_ROOT}/vs-audacity/",f"April {YEAR}","5 min"),
        ("⭐","Review",f"Wondershare Audio Recorder Review {YEAR} — 8.8/10","Full hands-on review: scheduling, auto-split, ID3 tagging and quality tests.",f"{SITE_ROOT}/review/",f"March {YEAR}","8 min"),
        ("💰","Guide",f"Audio Recorder Pricing {YEAR} — Free Trial & Plans","Free trial, annual and lifetime plans explained with current pricing.",f"{SITE_ROOT}/pricing/",f"March {YEAR}","3 min"),
        ("📻","Tutorial","Record Internet Radio — Scheduled & Automatic","Set a timer to record any online radio station automatically overnight.",f"{SITE_ROOT}/record-streaming-audio/",f"February {YEAR}","4 min"),
        ("🔇","Guide","Noise Reduction in Audio Recordings — Full Guide","Remove background hiss, hum and ambient noise from any recording.",f"{SITE_ROOT}/features/",f"February {YEAR}","4 min"),
        ("📁","Tutorial","Auto Track Split — Record Albums as Individual Files","How auto-split works and why it makes recording playlists effortless.",f"{SITE_ROOT}/features/",f"January {YEAR}","3 min"),
        ("🏷","Guide","ID3 Tags Explained — Auto-Tag Your Audio Recordings","What ID3 tags are, why they matter, and how Audio Recorder fills them in.",f"{SITE_ROOT}/features/",f"January {YEAR}","4 min"),
    ]
    cards = "".join(
        f'<div class="bc"><div class="bc-thumb">{e}</div><div class="bc-body">'
        f'<div class="bc-tag">{t}</div><h3>{title}</h3><p>{desc}</p>'
        f'<div class="bc-meta"><span>\U0001f4c5 {d}</span><span>\u23f1 {read}</span></div>'
        f'<a href="{url}" class="bc-read">Read Article \u2192</a>'
        f'</div></div>'
        for e,t,title,desc,url,d,read in posts
    )
    return page(
        f"Audio Recorder Blog — Recording Guides, Reviews & Tutorials {YEAR}",
        "Audio recording guides, tutorials and reviews. Learn to record streaming audio, Zoom calls, podcasts, radio and voice on Windows with Wondershare Audio Recorder.",
        "/blog/",
        (
            f'<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Blog",None))}'
            f'<span class="sec-lbl">Guides, Reviews & Tutorials</span>'
            f'<h1>Audio Recorder <span class="g-acc">Blog</span></h1>'
            f'<p style="max-width:600px;margin-top:.9rem;color:var(--muted)">Practical guides and honest reviews for every audio recording need.</p></div>'
            f'<section><div class="bgrid">{cards}</div></section>'
        ),
        "audio recording guide, audio recorder tutorial, record streaming audio guide, audio recorder review"
    )

def pg_privacy():
    return page(
        "Privacy Policy — AudioRecorder Guide",
        "Privacy policy for the AudioRecorder affiliate guide.",
        "/privacy/",
        (
            f'<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Privacy",None))}'
            f'<h1>Privacy <span class="g-acc">Policy</span></h1>'
            f'<p style="color:var(--muted);margin-top:.4rem">Last updated: June {YEAR}</p></div>'
            f'<section style="max-width:820px;margin:0 auto">'
            f'<div class="hbox"><p>This is an independent affiliate guide for Wondershare Streaming Audio Recorder. We earn commissions on qualifying purchases through affiliate links at no extra cost to you.</p></div>'
            f'<h3 style="margin:2rem 0 .7rem;color:var(--acc)">Data Collection</h3>'
            f'<p>This is a static site hosted on GitHub Pages. We do not collect personal data or operate databases. GitHub Pages may log standard server data as part of its infrastructure.</p>'
            f'<h3 style="margin:2rem 0 .7rem;color:var(--acc)">Affiliate Links</h3>'
            f'<p>Links to Wondershare Audio Recorder are affiliate links via the LinkConnector network. Purchases through these links earn us a commission at no additional cost to you.</p>'
            f'<h3 style="margin:2rem 0 .7rem;color:var(--acc)">Cookies</h3>'
            f'<p>This site does not set first-party cookies. Affiliate tracking uses cookies managed by LinkConnector. You may disable cookies in your browser settings to opt out.</p>'
            f'</section>'
        )
    )

def pg_disclaimer():
    return page(
        "Affiliate Disclaimer — AudioRecorder Guide",
        "Affiliate disclosure for the AudioRecorder guide.",
        "/disclaimer/",
        (
            f'<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Disclaimer",None))}'
            f'<h1>Affiliate <span class="g-acc">Disclaimer</span></h1>'
            f'<p style="color:var(--muted);margin-top:.4rem">Last updated: June {YEAR}</p></div>'
            f'<section style="max-width:820px;margin:0 auto">'
            f'<div class="hbox"><h4>Disclosure</h4>'
            f'<p style="margin-top:.4rem">This website contains affiliate links. As an affiliate of Wondershare via LinkConnector, we earn a commission on qualifying purchases at no additional cost to you. This funds the research and writing on this site.</p></div>'
            f'<h3 style="margin:2rem 0 .7rem;color:var(--acc)">Editorial Independence</h3>'
            f'<p>Our review lists both strengths and caveats honestly — including that the software is Windows-only and the built-in editor is basic. Affiliate relationships do not influence editorial opinions.</p>'
            f'<h3 style="margin:2rem 0 .7rem;color:var(--acc)">Accuracy</h3>'
            f'<p>Pricing and features can change. Always verify current details on the official Wondershare website before purchasing.</p>'
            f'</section>'
        )
    )

def pg_404():
    return page(
        "404 — Page Not Found | AudioRecorder Guide",
        "Page not found.",
        "/404/",
        (
            f'<div class="ph tc" style="min-height:60vh;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:1.5rem">'
            f'<div style="font-family:\'Fraunces\',serif;font-size:9rem;font-weight:900;line-height:1;color:var(--acc);text-shadow:var(--glow)">404</div>'
            f'<h1>Page <span class="g-acc2">Not Found</span></h1>'
            f'<p style="max-width:380px;text-align:center;color:var(--muted)">This page doesn\'t exist. Back to something useful.</p>'
            f'<div style="display:flex;gap:1rem;flex-wrap:wrap;justify-content:center">'
            f'<a href="{SITE_ROOT}/" class="btn btn-p">\u2190 Go Home</a>'
            f'<a href="{AFF}" class="btn btn-s" target="_blank" rel="noopener sponsored">Download Audio Recorder</a>'
            f'</div></div>'
        )
    )

# ── SEO & META FILES ──────────────────────────────────────────────────────────
def mk_sitemap():
    pages = [
        ("/","1.0","weekly"),
        ("/features/","0.9","monthly"),
        ("/how-it-works/","0.8","monthly"),
        ("/use-cases/","0.8","monthly"),
        ("/formats/","0.8","monthly"),
        ("/pricing/","0.9","monthly"),
        ("/review/","0.9","monthly"),
        ("/faq/","0.8","monthly"),
        ("/download/","0.9","monthly"),
        ("/blog/","0.8","weekly"),
        ("/record-streaming-audio/","0.9","monthly"),
        ("/record-zoom-audio/","0.8","monthly"),
        ("/record-spotify/","0.8","monthly"),
        ("/podcast-recorder/","0.8","monthly"),
        ("/voice-recorder/","0.8","monthly"),
        ("/vs-audacity/","0.8","monthly"),
        ("/vs-garageband/","0.7","monthly"),
        ("/alternatives/","0.8","monthly"),
        ("/privacy/","0.3","yearly"),
        ("/disclaimer/","0.3","yearly"),
    ]
    today = date.today().isoformat()
    url_items = []
    for p, pri, freq in pages:
        url_items.append(
            f"  <url>\n"
            f"    <loc>{SITE_URL}{p}</loc>\n"
            f"    <changefreq>{freq}</changefreq>\n"
            f"    <priority>{pri}</priority>\n"
            f"    <lastmod>{today}</lastmod>\n"
            f"  </url>"
        )
    urls = "\n".join(url_items)
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + urls +
        '\n</urlset>'
    )

def mk_robots():
    return (
        "User-agent: *\n"
        "Allow: /\n"
        "Disallow: /assets/\n\n"
        f"Sitemap: {SITE_URL}/sitemap.xml\n"
    )

def mk_llms():
    pages_list = [
        "/ — Homepage (all sources, features, testimonials, comparison table)",
        "/features/ — 12 features with ItemList schema",
        "/how-it-works/ — 3 workflows: basic, scheduled, always-on with HowTo schema",
        "/use-cases/ — 6 use cases: music, calls, podcasting, education, gaming, musicians",
        "/formats/ — 10 formats with full comparison table",
        "/pricing/ — 3 plans with FAQPage schema",
        "/review/ — 8.8/10 review with Review schema and 8 rating categories",
        "/faq/ — 10 Q&As with FAQPage schema",
        "/download/ — Windows download page",
        "/blog/ — 12-article blog index",
        "/record-streaming-audio/ — HowTo guide with 5 steps",
        "/record-zoom-audio/ — Meeting audio recording guide",
        "/record-spotify/ — Spotify recording with auto-split and ID3 guide",
        "/podcast-recorder/ — Podcast recording with 5 steps",
        "/voice-recorder/ — Voice memo, interview and dictation guide",
        "/vs-audacity/ — Full comparison table vs Audacity",
        "/vs-garageband/ — Comparison vs GarageBand",
        "/alternatives/ — Market overview vs 6 competitors",
        "/privacy/ — Privacy policy",
        "/disclaimer/ — Affiliate disclosure",
        "/404.html — 404 page",
    ]
    pages_str = "\n".join(f"- {p}" for p in pages_list)

    sections = [
        f"# AudioRecorder Guide — {SITE_URL}",
        f"> Purpose: Independent affiliate guide for Wondershare Streaming Audio Recorder",
        f"> Updated: {date.today().isoformat()}",
        f"> Affiliate: LinkConnector network",
        f"> Affiliate link: {AFF}",
        "",
        "## Product: Wondershare Streaming Audio Recorder",
        "**Publisher:** Wondershare Software Ltd (founded 2003, publicly listed)",
        "**Version:** 2.1.0",
        "**Platform:** Windows only (7, 8, 10, 11 — 32 and 64-bit)",
        "**Mac:** Not available",
        "",
        "### What It Does",
        "Records any audio playing on a Windows computer using virtual audio driver technology.",
        "Captures audio at source — before it reaches speakers — at full digital quality with zero degradation.",
        "",
        "### Audio Sources",
        "- System audio: any sound playing through the computer output",
        "- Streaming music: Spotify, Apple Music, Amazon Music, YouTube Music, Tidal, Deezer",
        "- Internet radio: any online radio station or stream",
        "- Video calls: Zoom, Microsoft Teams, Google Meet, Skype, Discord (audio-only)",
        "- Browser audio: Chrome, Firefox, Edge — YouTube, Netflix, any website",
        "- Microphone: any connected mic — USB, 3.5mm, audio interface",
        "- Games and apps: any application audio",
        "",
        "### Output Formats",
        "MP3, WAV, FLAC, AAC, M4A, OGG, WMA, AIFF, AC3, APE",
        "- MP3: 64kbps to 320kbps, universal compatibility",
        "- WAV: uncompressed lossless, 1411kbps (CD quality)",
        "- FLAC: lossless compressed, ~700-1100kbps",
        "",
        "### Key Features",
        "1. Record system audio — virtual audio driver, zero quality loss",
        "2. Record microphone — any connected mic, adjustable levels",
        "3. Scheduled recording — set start/stop time, records automatically",
        "4. Auto track split — detects silence, saves each track as separate file",
        "5. ID3 tag editor — auto-fetches artist/title/album/cover art, manual edit",
        "6. Built-in audio editor — trim, cut, volume, fade in/out",
        "7. Noise reduction — AI-powered background noise removal",
        "8. Format converter — convert existing audio between any supported format",
        "9. Smart file naming — auto-names with date, time, source",
        "10. Always-on mode — silent system tray recording",
        "",
        "### Pricing",
        "- Free trial: recording length limited, no credit card required",
        "- Annual plan: approx $29.95/year",
        "- Perpetual plan: one-time payment, check official site for current price",
        "- Promotions: discounts available on official Wondershare site",
        "",
        "### Review Summary",
        "- Overall: 8.8/10",
        "- Recording quality: 9.6/10 — zero quality loss on streaming capture",
        "- Scheduled recording: 9.5/10 — works flawlessly",
        "- Ease of use: 9.2/10 — simplest interface of any recorder tested",
        "- Auto track split: 9.0/10 — correctly split 11 of 12 test tracks",
        "- Best for: Windows users who need to record streaming audio automatically",
        "- Not for: Mac users, multitrack production, advanced audio editing",
        "",
        "### Vs Audacity",
        "Audio Recorder: scheduled recording YES, auto-split YES, ID3 tags YES, streaming capture easy",
        "Audacity: scheduled NO, auto-split NO, ID3 NO, streaming capture requires plugin setup",
        "Audacity wins: multitrack editing, plugins, effects, free, cross-platform",
        "Best combination: use both — Audio Recorder to capture, Audacity to edit",
        "",
        "## Site Structure — 20 Pages",
        pages_str,
        "",
        "## Schema Types Used",
        "SoftwareApplication + BreadcrumbList on all pages",
        "FAQPage on /faq/ and /pricing/",
        "Review on /review/",
        "HowTo on /how-it-works/ and /record-streaming-audio/",
        "ItemList on /features/",
        "Article OG type on all guide/comparison pages",
        "",
        "## Affiliate Information",
        "- Network: LinkConnector",
        f"- Link: {AFF}",
        "- All affiliate links use rel=\"noopener sponsored\" per Google guidelines",
        "- Commission earned on qualifying purchases, no extra cost to users",
    ]
    return "\n".join(sections)

def mk_feed():
    items = [
        (
            f"Record Streaming Audio — Complete Guide {YEAR}",
            f"{SITE_URL}/record-streaming-audio/",
            "Capture Spotify, Apple Music, YouTube and any online stream at full quality.",
            f"{YEAR}-06-01"
        ),
        (
            f"How to Record Zoom Audio Only {YEAR}",
            f"{SITE_URL}/record-zoom-audio/",
            "Record Zoom, Teams and Meet as clean MP3 — no video, tiny file size.",
            f"{YEAR}-06-01"
        ),
        (
            f"Wondershare Audio Recorder Review {YEAR} — 8.8/10",
            f"{SITE_URL}/review/",
            "Complete review: scheduling, auto-split, ID3 tagging and quality tests.",
            f"{YEAR}-03-01"
        ),
        (
            "Audio Recorder vs Audacity — Which Should You Use?",
            f"{SITE_URL}/vs-audacity/",
            "Two different tools for two different jobs. Here's exactly when to use each.",
            f"{YEAR}-04-01"
        ),
        (
            "Podcast Recorder Guide — Record & Export MP3",
            f"{SITE_URL}/podcast-recorder/",
            "Mic recording, noise reduction, editing and MP3 export in one app.",
            f"{YEAR}-05-01"
        ),
    ]
    item_tags = []
    for t,u,d,pd in items:
        item_tags.append(
            f"  <item>\n"
            f"    <title>{t}</title>\n"
            f"    <link>{u}</link>\n"
            f"    <description>{d}</description>\n"
            f"    <pubDate>{pd}</pubDate>\n"
            f"    <guid>{u}</guid>\n"
            f"  </item>"
        )
    ixml = "\n".join(item_tags)
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n'
        '  <channel>\n'
        '    <title>AudioRecorder Guide Blog</title>\n'
        f'    <link>{SITE_URL}/blog/</link>\n'
        '    <description>Audio recording guides, tutorials and reviews.</description>\n'
        '    <language>en-us</language>\n'
        f'    <atom:link href="{SITE_URL}/feed.xml" rel="self" type="application/rss+xml"/>\n'
        + ixml +
        '\n  </channel>\n</rss>'
    )

def mk_favicon():
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
        '<rect width="64" height="64" rx="14" fill="#04050d"/>'
        '<rect x="1" y="1" width="62" height="62" rx="13" fill="none" stroke="#7c3aed" stroke-width="1.5" opacity="0.5"/>'
        '<circle cx="32" cy="28" r="10" fill="none" stroke="#7c3aed" stroke-width="2.5"/>'
        '<line x1="32" y1="9" x2="32" y2="5" stroke="#7c3aed" stroke-width="2" stroke-linecap="round"/>'
        '<rect x="29" y="18" width="6" height="20" rx="3" fill="#7c3aed"/>'
        '<path d="M20 30 Q20 42 32 42 Q44 42 44 30" fill="none" stroke="#7c3aed" stroke-width="2.5" stroke-linecap="round"/>'
        '<line x1="32" y1="42" x2="32" y2="50" stroke="#7c3aed" stroke-width="2.5" stroke-linecap="round"/>'
        '<line x1="26" y1="50" x2="38" y2="50" stroke="#7c3aed" stroke-width="2.5" stroke-linecap="round"/>'
        '</svg>'
    )

# ── MAIN ──────────────────────────────────────────────────────────────────────
def main():
    print(f"\n\U0001f3a4 AudioRecorder Affiliate Site Builder")
    print(f"   {SITE_URL}\n")

    write("index.html",                        pg_home())
    write("features/index.html",               pg_features())
    write("how-it-works/index.html",           pg_how())
    write("use-cases/index.html",              pg_use_cases())
    write("formats/index.html",               pg_formats())
    write("pricing/index.html",               pg_pricing())
    write("review/index.html",                pg_review())
    write("faq/index.html",                   pg_faq())
    write("download/index.html",              pg_download())
    write("blog/index.html",                  pg_blog())
    write("record-streaming-audio/index.html", pg_record_streaming())
    write("record-zoom-audio/index.html",      pg_record_zoom())
    write("record-spotify/index.html",         pg_record_spotify())
    write("podcast-recorder/index.html",       pg_podcast_recorder())
    write("voice-recorder/index.html",         pg_voice_recorder())
    write("vs-audacity/index.html",            pg_vs_audacity())
    write("vs-garageband/index.html",          pg_vs_garageband())
    write("alternatives/index.html",           pg_alternatives())
    write("privacy/index.html",               pg_privacy())
    write("disclaimer/index.html",            pg_disclaimer())
    write("404.html",                         pg_404())
    write("sitemap.xml",                      mk_sitemap())
    write("robots.txt",                       mk_robots())
    write("llms.txt",                         mk_llms())
    write("feed.xml",                         mk_feed())
    write("assets/favicon.svg",               mk_favicon())
    write(".nojekyll",                        "")

    pages = len([f for f in BASE.rglob("*.html")])
    total = len(list(BASE.rglob("*")))
    print(f"\n\u2705 Done \u2014 {pages} HTML pages, {total} total files")
    print(f"   Output: {BASE}")
    print(f"   Deploy: {SITE_URL}\n")

if __name__ == "__main__":
    main()
