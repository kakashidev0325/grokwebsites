"""Token-colored SVG scenes. Fills use classes .bg .bg2 .surf .a .a2 .ink so themes recolor them."""
import math, random

def stars(n, y=480, cls="ink", seed=1):
    rng = random.Random(seed)
    return "".join(
        '<circle class="%s" cx="%d" cy="%d" r="%s" opacity="%.2f"/>' % (
            cls, rng.randint(0, 1440), rng.randint(0, y), rng.choice(("1", "1.4", "2", "2.6")), 0.35 + rng.random() * 0.6
        ) for _ in range(n)
    )

def dots(n, cls="a", seed=2):
    rng = random.Random(seed)
    return "".join(
        '<circle class="%s" cx="%d" cy="%d" r="%d" opacity="%.2f"/>' % (
            cls, rng.randint(0, 1440), rng.randint(0, 900), 2 + rng.randint(0, 4), 0.25 + rng.random() * 0.5
        ) for _ in range(n)
    )

def wrap(inner):
    return '<svg class="scene" viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid slice" aria-hidden="true">' + inner + "</svg>"

def S(name):
    b = {
"halftone": '<rect class="bg" width="1440" height="900"/>' + dots(160, "a", 3) + '<circle class="line" cx="720" cy="380" r="260" fill="none" stroke-width="28" opacity=".25"/><circle class="a" cx="720" cy="380" r="150" fill="none" stroke="currentColor" stroke-width="3" opacity=".7"/>',
"corner": '<rect class="bg" width="1440" height="900"/>' + "".join('<path class="line" d="M%d %dH%d" stroke-width="1" opacity=".2"/>' % (0, y, 1440) for y in range(30, 900, 42)) + '<g class="a" fill="none" stroke="currentColor" stroke-width="4"><path d="M70 70h140M70 70v140M1370 70h-140M1370 70v140M70 830h140M70 830v-140M1370 830h-140M1370 830v-140"/></g><circle class="a2" cx="1180" cy="200" r="80" opacity=".35"/>',
"blobs": '<rect class="bg" width="1440" height="900"/><ellipse class="a2" cx="260" cy="180" rx="240" ry="140" opacity=".55"/><ellipse class="a" cx="1160" cy="200" rx="280" ry="160" opacity=".4"/><ellipse class="surf" cx="720" cy="820" rx="560" ry="200"/><circle class="a" cx="180" cy="680" r="70" opacity=".35"/>',
"bubbles": '<rect class="bg" width="1440" height="900"/><g class="ink" fill="none" stroke="currentColor" stroke-width="3"><circle cx="180" cy="150" r="70"/><circle cx="1220" cy="190" r="120"/><circle cx="300" cy="720" r="36"/><circle cx="1000" cy="680" r="84"/></g><path class="a" d="M180 420c90-90 180-10 250 20" fill="none" stroke="currentColor" stroke-width="10" stroke-linecap="round"/><path class="a2" d="M1040 460c70 40 150 10 210-40" fill="none" stroke="currentColor" stroke-width="10" stroke-linecap="round"/>' + dots(18, "a", 9),
"appcards": '<rect class="bg" width="1440" height="900"/><g class="surf"><rect x="140" y="130" width="280" height="168" rx="24"/><rect x="1000" y="170" width="300" height="150" rx="24"/><rect x="160" y="610" width="230" height="130" rx="24"/></g><rect class="a" x="1060" y="560" width="250" height="150" rx="24" opacity=".25"/><circle class="a" cx="720" cy="450" r="200" opacity=".08"/>',
"hills": '<rect class="bg" width="1440" height="900"/>' + stars(70, 360, "a2", 4) + '<circle class="a" cx="1120" cy="170" r="64"/><path class="bg2" d="M0 600c180-90 300-30 460-90s280-10 420 50 300 20 560-70v410H0z"/><path class="surf" d="M0 740c200-50 340-10 500-60s300 20 460 30 250-30 480-70v260H0z" opacity=".9"/>',
"blobblue": '<rect class="bg" width="1440" height="900"/><ellipse class="a" cx="1080" cy="430" rx="360" ry="300"/><ellipse class="a2" cx="1200" cy="360" rx="170" ry="150" opacity=".75"/><circle class="a" cx="180" cy="160" r="50" opacity=".15"/><circle class="a" cx="240" cy="760" r="100" opacity=".1"/>',
"clouds": '<rect class="bg" width="1440" height="900"/><g class="surf"><ellipse cx="220" cy="170" rx="130" ry="48"/><ellipse cx="300" cy="156" rx="80" ry="40"/><ellipse cx="1000" cy="140" rx="160" ry="52"/><ellipse cx="640" cy="210" rx="100" ry="36"/></g><circle class="a" cx="1180" cy="230" r="52"/><path class="a2" d="M0 690c140-80 240-20 360-54s240-8 340 46 250 16 380-36 230-30 360 16v238H0z" opacity=".85"/><path class="bg2" d="M0 780c200-40 320-8 480-34s280 14 430 18 260-24 530-8v144H0z"/>',
"rings": '<rect class="bg" width="1440" height="900"/>' + stars(80, 900, "ink", 6) + '<g class="a" fill="none" stroke="currentColor" stroke-width="2"><circle cx="720" cy="440" r="110"/><circle cx="720" cy="440" r="190"/><circle cx="720" cy="440" r="280"/><circle cx="720" cy="440" r="370"/></g>' + "".join('<circle class="a2" cx="%d" cy="%d" r="6"/>' % (720+int(math.cos(a)*r), 440+int(math.sin(a)*r)) for a,r in ((0.4,190),(1.7,280),(2.8,370),(4.1,110),(5.3,280))),
"marks": '<rect class="bg" width="1440" height="900"/><g class="a" fill="none" stroke="currentColor" stroke-width="10"><path d="M150 200l80 80M230 200l-80 80"/><path d="M1160 560l90 90M1250 560l-90 90"/></g><text class="ink" x="90" y="780" font-size="220" font-family="Georgia,serif" opacity=".08">?</text>',
"grid": '<rect class="bg" width="1440" height="900"/><g class="a" fill="none" stroke="currentColor" stroke-width="1" opacity=".28">' + "".join('<path d="M%d 0v900M0 %dH1440"/>' % (x, x if x < 900 else 0) for x in range(0, 1440, 56)) + '</g><rect class="a" x="90" y="90" width="180" height="110" fill="none" stroke="currentColor" stroke-width="2"/><rect class="a2" x="1120" y="640" width="220" height="140" fill="none" stroke="currentColor" stroke-width="2"/><circle class="a" cx="720" cy="450" r="7"/>',
"rules": '<rect class="bg" width="1440" height="900"/><g class="ink" opacity=".16" stroke="currentColor">' + "".join('<path d="M90 %dH1340"/>' % y for y in range(110, 860, 34)) + '</g><rect class="a" x="70" y="70" width="8" height="760"/>',
"roof": '<rect class="bg" width="1440" height="900"/><g class="bg2">' + "".join('<rect x="%d" y="%d" width="%d" height="%d"/>' % (x, 900-h, w, h) for x,w,h in ((40,70,300),(130,100,380),(250,60,240),(1040,90,340),(1150,120,420),(1290,80,260))) + '</g><g class="a">' + "".join('<rect x="%d" y="%d" width="8" height="12" opacity=".8"/>' % (70+(i%10)*26, 460+(i%6)*28) for i in range(36)) + '</g><rect class="surf" y="700" width="1440" height="200"/><rect class="a2" y="688" width="1440" height="16"/>',
"spots": '<rect class="bg" width="1440" height="900"/>' + "".join('<ellipse class="a" cx="%d" cy="%d" rx="%d" ry="%d" opacity=".2"/>' % ((i*173)%1440, (i*97)%900, 28+(i%4)*14, 16+(i%3)*8) for i in range(16)) + '<circle class="a" cx="1180" cy="190" r="86" fill="none" stroke="currentColor" stroke-width="16"/>',
"grain": '<rect class="bg" width="1440" height="900"/>' + stars(100, 900, "a2", 8) + '<rect class="a" x="70" y="60" width="1300" height="780" fill="none" stroke="currentColor" stroke-width="2" opacity=".45"/><rect class="a2" x="96" y="86" width="1248" height="728" fill="none" stroke="currentColor" stroke-width="1" opacity=".35"/>',
"circuit": '<rect class="bg" width="1440" height="900"/><g class="a" fill="none" stroke="currentColor" stroke-width="2"><path d="M80 200h280l40 40h220l40-40h420"/><path d="M180 720h260l46-90h200l40 90h480"/><path d="M400 200v200h140v100"/><path d="M1020 150v250h180"/></g><g class="a2"><circle cx="360" cy="200" r="6"/><circle cx="660" cy="240" r="6"/><circle cx="1040" cy="150" r="6"/><circle cx="1180" cy="720" r="6"/></g>',
"ghost": '<rect class="bg" width="1440" height="900"/><ellipse class="surf" cx="280" cy="190" rx="190" ry="80"/><ellipse class="surf" cx="1120" cy="160" rx="230" ry="90"/><path class="surf" d="M500 760c40-90 90-90 130 0s90 90 130 0 80-90 130 0v140H500z"/><circle class="a" cx="200" cy="640" r="16" opacity=".7"/><circle class="a2" cx="1240" cy="600" r="22" opacity=".6"/>',
"mag": '<rect class="bg" width="1440" height="900"/><rect class="ink" width="1440" height="16"/><rect class="ink" y="884" width="1440" height="16"/><g class="ink" opacity=".12" stroke="currentColor">' + "".join('<path d="M%d 30v840"/>' % x for x in (360, 720, 1080)) + '</g>',
"seal": '<rect class="bg" width="1440" height="900"/><g class="a" opacity=".2" stroke="currentColor">' + "".join('<path d="M0 %dH1440"/>' % y for y in range(0, 900, 28)) + '</g><circle class="a" cx="1170" cy="210" r="96" fill="none" stroke="currentColor" stroke-width="8"/><circle class="a" cx="1170" cy="210" r="72" fill="none" stroke="currentColor" stroke-width="2"/>',
"planet": '<rect class="bg" width="1440" height="900"/>' + stars(70, 460, "a2", 5) + '<ellipse class="a" cx="720" cy="1020" rx="860" ry="380"/><ellipse class="a2" cx="720" cy="930" rx="700" ry="170" opacity=".85"/><ellipse class="bg2" cx="980" cy="800" rx="90" ry="28" opacity=".45"/><circle class="surf" cx="230" cy="160" r="34"/>',
"sun": '<rect class="bg" width="1440" height="900"/>' + "".join('<polygon class="a" opacity=".35" points="720,200 %d,%d %d,%d"/>' % (720+int(math.cos(a)*30), 200+int(math.sin(a)*30), 720+int(math.cos(a+0.2)*560), 200+int(math.sin(a+0.2)*560)) for a in (i*0.52 for i in range(12))) + '<circle class="a" cx="720" cy="200" r="72"/>',
"galaxy": '<rect class="bg" width="1440" height="900"/>' + stars(110, 900, "ink", 7) + '<ellipse class="a" cx="860" cy="430" rx="360" ry="90" fill="none" stroke="currentColor" stroke-width="3" opacity=".55" transform="rotate(-18 860 430)"/><ellipse class="a2" cx="860" cy="430" rx="210" ry="46" opacity=".35" transform="rotate(-18 860 430)"/>',
"candles": '<rect class="bg" width="1440" height="900"/>' + "".join('<rect class="%s" x="%d" y="%d" width="18" height="%d" opacity=".9"/>' % ("a" if i % 3 else "a2", 30+i*46, 640-(i*13%200), 48+(i%5)*22) for i in range(30)),
"waves": '<rect class="bg" width="1440" height="900"/><path class="a2" d="M0 640c140 50 260-50 400-24s250 70 380 20 250-80 380-16 220 30 280 8v252H0z" opacity=".8"/><path class="a" d="M0 740c180 36 300-30 460-8s270 40 420 8 250-40 380-12 160 16 180 6v166H0z" opacity=".45"/><circle class="surf" cx="220" cy="170" r="42"/>',
"torii": '<rect class="bg" width="1440" height="900"/><g class="a" fill="none" stroke="currentColor" stroke-width="12"><path d="M430 760V320h580v440"/><path d="M360 320h720"/><path d="M390 400h660"/></g><circle class="a2" cx="720" cy="230" r="42"/><g class="ink" opacity=".08">' + "".join('<circle cx="%d" cy="820" r="16"/>' % (160+i*80) for i in range(15)) + '</g>',
"stickers": '<rect class="bg" width="1440" height="900"/><g class="a"><rect x="120" y="120" width="190" height="140" rx="18" transform="rotate(-8 215 190)"/></g><g class="a2"><rect x="1100" y="150" width="210" height="150" rx="18" transform="rotate(8 1205 225)"/></g><g class="surf"><rect x="170" y="620" width="170" height="120" rx="16" transform="rotate(6 255 680)"/><rect x="1080" y="610" width="220" height="150" rx="16" transform="rotate(-7 1190 685)"/></g>',
"stripes": '<rect class="bg" width="1440" height="900"/>' + "".join('<rect class="a" x="%d" width="22" height="900" opacity="%.2f"/>' % (i*48, 0.12+(i%3)*0.08) for i in range(30)) + '<circle class="ink" cx="720" cy="450" r="230" fill="none" stroke="currentColor" stroke-width="2" opacity=".25"/>',
    }
    return wrap(b[name])

def scene_svg(name):
    return S(name)
