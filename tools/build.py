#!/usr/bin/env python3
"""Writes the static pages for wordsprout.co. Run: python3 tools/build.py (from the repo root).
Edit the content here, then re-run; GitHub Pages serves the generated .html files as they are.
The share-code page, s/index.html, is hand-written and shares styles.css."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APP_STORE = "https://apps.apple.com/us/app/wordsprout-spelling-practice/id6741597283"
EMAIL = "hello@wordsprout.co"
UPDATED = "October 16, 2026"
APPLE = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16.37 12.6c-.02-2.3 1.88-3.4 1.97-3.46-1.07-1.57-2.74-1.78-3.33-1.8-1.42-.14-2.77.83-3.49.83-.72 0-1.83-.81-3.01-.79-1.55.02-2.98.9-3.78 2.29-1.61 2.8-.41 6.94 1.16 9.21.77 1.11 1.68 2.36 2.88 2.31 1.16-.05 1.6-.75 3-.75s1.79.75 3.01.72c1.24-.02 2.03-1.13 2.79-2.25.88-1.29 1.24-2.53 1.26-2.6-.03-.01-2.42-.93-2.46-3.71zM14.08 5.85c.64-.77 1.07-1.85.95-2.92-.92.04-2.03.61-2.69 1.38-.59.68-1.11 1.77-.97 2.82 1.03.08 2.07-.52 2.71-1.28z"/></svg>')
CHECK = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
STORE_BUTTON = f'<a class="btn store" href="{APP_STORE}">{APPLE}<span><small>Download on the</small>App Store</span></a>'

# Cards rise in once as they scroll into view (styles.css skips this under Reduce Motion).
REVEAL_JS = """(function () {
  var els = document.querySelectorAll('.reveal');
  if (!('IntersectionObserver' in window)) { els.forEach(function (el) { el.classList.add('in'); }); return; }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
  }, { rootMargin: '0px 0px -8% 0px' });
  els.forEach(function (el) { io.observe(el); });
})();"""


def page(path, title, description, body, current=""):
    nav = [("/#how", "How it works"), ("/#kids", "For kids"), ("/#parents", "For parents"), ("/#pro", "Pro"),
           ("/support/", "Support")]
    links = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if href == current else ""}>{label}</a>' for href, label in nav)
    full_title = title if title == "WordSprout" else f"{title} · WordSprout"
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{description}">
<meta name="apple-itunes-app" content="app-id=6741597283">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="https://wordsprout.co/img/og.jpg">
<meta property="og:url" content="https://wordsprout.co{current or path}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#FFD60A">
<meta name="color-scheme" content="light">
<link rel="icon" type="image/png" href="/favicon.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
<script>document.documentElement.classList.add('js')</script>
</head>
<body>
<div class="ws">
<a class="skip" href="#main">Skip to content</a>
<header class="hdr"><div class="wrap hdr-in">
  <a class="brand" href="/"><img src="/img/bee.png" alt="" width="42" height="42">WordSprout</a>
  <nav class="nav" aria-label="Main">{links}</nav>
  <a class="btn btn-sm" href="{APP_STORE}">Get the app</a>
</div></header>
<main id="main">
{body}
</main>
<footer class="ftr"><div class="wrap ftr-in">
  <a class="brand" href="/"><img src="/img/bee.png" alt="" width="32" height="32">WordSprout</a>
  <nav aria-label="Footer"><a href="/support/">Support</a><a href="/privacy/">Privacy Policy</a><a href="/terms/">Terms of Service</a><a href="mailto:{EMAIL}">{EMAIL}</a></nav>
  <span>© 2026 WordSprout</span>
</div></footer>
</div>
<script>
{REVEAL_JS}
</script>
</body>
</html>
"""
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)


def redirect(path, to):
    out = ROOT / path / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(f'<!doctype html><meta charset="utf-8"><title>WordSprout</title>'
                   f'<meta http-equiv="refresh" content="0; url={to}"><link rel="canonical" href="{to}">'
                   f'<p><a href="{to}">Continue to WordSprout</a></p>\n')


def ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def checks(items):
    return '<ul class="checks">' + "".join(f"<li><span>{i}</span></li>" for i in items) + "</ul>"


FLOWER_COLORS = ["#FF8FA3", "#B78CFF", "#FF9F43", "#6FB7FF", "#FF6B6B", "#FFFFFF", "#F78FD0"]
FLOWER_KINDS = ["", "bud", "", "sprout", "", "", "bud", "", "sprout", "", "", "bud", "", "", "sprout", "", "bud", ""]
FLOWER_HEIGHTS = [52, 40, 60, 28, 46, 56, 38, 50, 26, 58, 44, 36, 54, 48, 30, 56, 42, 50]


def flower(kind="", color="#FF8FA3", height=44, delay=0.0, style=""):
    return (f'<span class="{("fl " + kind).strip()}" style="--c: {color}; --h: {height}px; --d: {delay:.2f}s;{style}">'
            f'<i class="stem"></i><i class="bloom"></i></span>')


def meadow(count=18, scale=1.0, grow=True, soil=True):
    """A row of flowers along a strip of soil. The same every build, so rebuilding changes nothing."""
    row = "".join(flower(FLOWER_KINDS[i % 18], FLOWER_COLORS[(i * 3) % 7], round(FLOWER_HEIGHTS[i % 18] * scale),
                         0.15 + ((i * 7) % 18) * 0.07) for i in range(count))
    return (f'<div class="meadow{" grow" if grow else ""}" aria-hidden="true"><div class="meadow-row">{row}</div>'
            f'{"<div class=\"soil\"></div>" if soil else ""}</div>')


def bed(*plants):
    """Soil under a phone in a card, with a few plants: (kind, color, height, css position)."""
    spans = "".join(flower(kind, color, height, style=f" {pos};") for kind, color, height, pos in plants)
    return f'<div class="bed" aria-hidden="true">{spans}<div class="soil"></div></div>'


def screen(name, alt, cls="phone", w=600, h=1290, lazy=True):
    """An app screen in a phone (or iPad) frame, WebP with a JPEG fallback."""
    loading = ' loading="lazy" decoding="async"' if lazy else ''
    return (f'<div class="{cls}"><picture><source srcset="/img/app/{name}.webp" type="image/webp">'
            f'<img src="/img/app/{name}.jpg" alt="{alt}" width="{w}" height="{h}"{loading}></picture></div>')


def qr_path(n=25, seed=7):
    """A QR-like pattern for the class card picture. Decorative only: the real card's QR is made in the app."""
    def finder(x, y):
        return f"M{x} {y}h7v7h-7z M{x + 1} {y + 1}v5h5v-5z M{x + 2} {y + 2}h3v3h-3z "
    d = ""
    for y in range(n):
        for x in range(n):
            seed = (seed * 9301 + 49297) % 233280
            in_finder = (x < 8 and y < 8) or (x > n - 9 and y < 8) or (x < 8 and y > n - 9)
            if not in_finder and seed / 233280 > 0.52:
                d += f"M{x} {y}h1v1h-1z "
    return finder(0, 0) + finder(n - 7, 0) + finder(0, n - 7) + d


def band(title, sub, narrow=True):
    """The yellow band at the top of an inner page, with flowers along its bottom edge."""
    return (f'<section class="ihero" aria-labelledby="page-title"><div class="wrap{" narrow" if narrow else ""}">\n'
            f'  <h1 id="page-title">{title}</h1>\n  <p>{sub}</p>\n</div>{meadow(18, scale=.75)}</section>')


ARROW = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 6l6 6-6 6"/></svg>'
GAMES = [
    ("Flashcards", "#7C4DFF", '<rect x="4" y="6" width="13" height="14" rx="2"/><path d="M8 3h11a2 2 0 0 1 2 2v12"/>'),
    ("Pick it", "#2F6FD6", '<circle cx="12" cy="12" r="8"/><path d="M8.5 12.5l2.5 2.5 4.5-5"/>'),
    ("Missing letter", "#D9480F", '<rect x="3" y="7" width="6" height="10" rx="1.5"/><rect x="15" y="7" width="6" height="10" rx="1.5"/><path d="M11 17h2"/>'),
    ("Scramble", "#C47A00", '<path d="M4 7h3l10 10h3M4 17h3l10-10h3M17 4l3 3-3 3M17 14l3 3-3 3"/>'),
    ("Memory match", "#C2255C", '<rect x="3" y="5" width="8" height="10" rx="2"/><rect x="13" y="9" width="8" height="10" rx="2"/>'),
    ("Word search", "#0F8A7E", '<circle cx="10.5" cy="10.5" r="6"/><path d="M15 15l5 5"/>'),
]
CLASS_WORDS = ["rain", "train", "paint", "snail", "tail", "mail", "wait", "chain", "play", "day", "stay", "gray"]
LEAF = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 19c0-8 5-13 14-14-1 9-6 14-14 14zM5 19l7-7"/></svg>'

home = f"""
<section class="hero" aria-labelledby="hero-title">
  <div class="wrap hero-in">
    <div class="hero-copy">
      <a class="pill-new" href="#new"><span class="tag">New</span>Share a list with the whole class{ARROW}</a>
      <h1 id="hero-title">Help every word <em>bloom.</em></h1>
      <p class="lede">Short, happy spelling practice for kids in K–5, built around this week’s list from school. Parents see exactly which words are still tricky.</p>
      <div class="cta-row">
        {STORE_BUTTON}
        <a class="link-arrow" href="#how">See how it works<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5v14M6 13l6 6 6-6"/></svg></a>
      </div>
      <p class="trust"><span>{CHECK}Free to start</span><span>{CHECK}iPhone and iPad</span><span>{CHECK}No ads, no tracking</span></p>
    </div>
    <div class="hero-art fan">
      <svg class="trail" viewBox="0 0 150 80" aria-hidden="true"><path d="M4 66 C 30 20, 60 80, 90 44 S 130 4, 146 14"/></svg>
      <img class="bee-fly" src="/img/bee.png" alt="" width="74" height="74">
      {screen("practice", "A Missing letter game: fill in the gap to spell queen", "phone p-left", lazy=False)}
      {screen("garden", "Maya’s garden: 13 flowers and 5 growing, one plant for each spelling word", "phone p-center", lazy=False)}
      {screen("parent-home", "The parent home: Maya has 5 Ready, 2 Almost and 0 Tricky words", "phone p-right", lazy=False)}
    </div>
  </div>
  {meadow()}
</section>

<section class="sec" id="how" aria-labelledby="how-title"><div class="wrap">
  <div class="center">
    <p class="eyebrow">How a week goes</p>
    <h2 id="how-title">Built for the weekly spelling list</h2>
    <p class="sub">Add the words from school in a minute. Your child practices a few minutes a day. You see who’s ready before test day.</p>
  </div>
  <ol class="steps">
    <li class="step reveal" style="--d: 0s;"><div class="peek sun">{screen("add-list", "Adding this week’s list, with buttons for Add word, Paste a list and Photo")}
      {bed(("", "#FF8FA3", 40, "left: 7%"), ("sprout", "#FF8FA3", 22, "left: 17%"), ("bud", "#B78CFF", 30, "right: 16%"), ("", "#FF9F43", 44, "right: 6%"))}</div>
      <div class="step-body"><span class="day">Monday</span><h3>Add this week’s list</h3><p>Type the words, paste them from the teacher’s email, or snap a photo of the paper list.</p></div></li>
    <li class="step reveal" style="--d: .12s;"><div class="peek pink">{screen("practice", "A practice game with big, friendly letters")}
      {bed(("bud", "#FF6B6B", 32, "left: 8%"), ("", "#6FB7FF", 46, "left: 17%"), ("sprout", "#FF8FA3", 24, "right: 17%"), ("", "#FFFFFF", 38, "right: 7%"))}</div>
      <div class="step-body"><span class="day">Every day</span><h3>Practice in one go</h3><p>A few quick games, a Spelling check with no hints, then a big cheer. Every word is read aloud.</p></div></li>
    <li class="step reveal" style="--d: .24s;"><div class="peek leaf">{screen("list-ready", "Maya’s list: most words Ready, with the test on Friday")}
      {bed(("", "#F78FD0", 44, "left: 6%"), ("", "#FFD60A", 30, "left: 16%"), ("", "#FF8FA3", 36, "right: 16%"), ("", "#B78CFF", 46, "right: 6%"))}</div>
      <div class="step-body"><span class="day">Test day</span><h3>Know they’re ready</h3><p>Every word shows Ready, Almost or Tricky, so you know exactly what to review the night before.</p></div></li>
  </ol>
</div></section>

<section class="sec tight" id="kids" aria-labelledby="kids-title"><div class="wrap two">
  <div>
    <p class="eyebrow">For kids</p>
    <h2 id="kids-title">Practice that feels like play</h2>
    <p class="sub">Six games mix this week’s words into one short session. Every word is read aloud, in your own recorded voice or the device voice.</p>
    <ul class="games">{"".join(f'<li><span class="gi" style="background: {color};"><svg viewBox="0 0 24 24" aria-hidden="true">{icon}</svg></span>{name}</li>' for name, color, icon in GAMES)}</ul>
    <div class="minis">
      <div class="mini"><span class="tag green">Every session</span><b>A Spelling check</b>No hints. Your child types the word, or writes it on paper for a grown-up to check.</div>
      <div class="mini"><span class="tag">New</span><b>Hear it in a sentence</b>Tap Sentence in a Spelling check or test to hear the word used, then the word again.</div>
    </div>
  </div>
  <div class="duo">
    {screen("listen", "Flashcards: Listen, then spell it in your head", "phone d1")}
    {screen("cheer", "You did it: 12 words practiced, 10 right first try", "phone d2")}
    <div class="speech float" style="--d: .5s;"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 9v6h4l5 4V5L8 9H4zM16.5 8.5a5 5 0 0 1 0 7M19 6a8.5 8.5 0 0 1 0 12"/></svg><span>“The queen wore a crown.”<small>Sentence, then the word</small></span></div>
  </div>
</div></section>

<section class="sec garden-band" aria-labelledby="garden-title"><div class="wrap two rev">
  <div>
    <p class="eyebrow" style="color: #1F7A42;">The garden</p>
    <h2 id="garden-title">Every word grows into a flower</h2>
    <p class="sub">Each word is a plant in your child’s garden. Spell it right on two different days and it blooms. Plants never wilt, so there’s nothing to lose and always something to grow.</p>
    <div class="stages cycle">
      <div class="stage" style="--i: 0;"><div class="pot" aria-hidden="true"><span class="seed"></span></div><div class="ground"></div><b>Seed</b><small>New this week</small></div>
      <div class="stage" style="--i: 1;"><div class="pot" aria-hidden="true">{flower("sprout", height=26)}</div><div class="ground"></div><b>Sprout</b><small>Practiced in games</small></div>
      <div class="stage" style="--i: 2;"><div class="pot" aria-hidden="true">{flower("bud", height=38)}</div><div class="ground"></div><b>Bud</b><small>Spelled right once</small></div>
      <div class="stage" style="--i: 3;"><div class="pot" aria-hidden="true">{flower("", height=46)}</div><div class="ground"></div><b>Flower</b><small>Right on two days</small></div>
    </div>
  </div>
  {screen("ipad-garden", "Maya’s garden on iPad, with Week 6 and Week 5 spelling and her sight words in bloom", "ipad", w=1000, h=749)}
</div></section>

<section class="sec" id="parents" aria-labelledby="par-title"><div class="wrap two">
  <div>
    <p class="eyebrow">For parents</p>
    <h2 id="par-title">See which words are still tricky</h2>
    <p class="sub">Your home screen shows a card for each child, with their words sorted so you know where to help.</p>
    <div class="legend">
      <span class="chip"><i style="background: #2F9E5B;"></i>Ready · right on two days, no hints</span>
      <span class="chip"><i style="background: #E0A800;"></i>Almost · right on one day</span>
      <span class="chip"><i style="background: #D9480F;"></i>Tricky · missed most recently</span>
    </div>
    {checks(["<b>A test date countdown.</b> Add Friday’s test and see whether they’re ready for it.",
             "<b>Tap any word for its story.</b> Every answer, from games and tests, and what comes next.",
             "<b>A daily reminder for each child,</b> at the time that suits your family, plus a Home Screen widget.",
             "<b>Sight words too.</b> Dolch and Fry lists to hear and practice."])}
  </div>
  <div class="par-art">
    {screen("parent-home", "The parent home with a card for Maya and a card for Leo")}
    <div class="widget-m float" style="--d: 0s;" role="img" aria-label="Medium Home Screen widget: Up next for Maya, Week 6 spelling, 5 of 12 bloomed, Practice">
      <div style="flex: 1; min-width: 0;"><div class="k">UP NEXT · MAYA</div><div class="t">Week 6 spelling</div><div class="bars">{'<i class="on"></i>' * 5}{'<i></i>' * 7}</div><div class="m">5 of 12 bloomed</div></div>
      <div class="go"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>Practice</div>
    </div>
    <div class="widget-s float" style="--d: 1.5s;" role="img" aria-label="Small Home Screen widget: 7 words to review, 3-day streak, Maya">
      {LEAF}<div class="n">7</div><div class="l">words to review</div><div class="m">3-day streak · Maya</div>
    </div>
  </div>
</div></section>

<section class="sec tight" aria-labelledby="setup-title"><div class="wrap">
  <div class="center">
    <p class="eyebrow">Set up your way</p>
    <h2 id="setup-title">One app for the whole family</h2>
    <p class="sub">Choose how WordSprout is used when you first open it. You can change it later in Settings.</p>
  </div>
  <div class="modes">
    <div class="mode reveal">
      <h3><span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="9" cy="8" r="3.2"/><circle cx="17" cy="9.5" r="2.4"/><path d="M3.5 19c.6-3.3 2.8-5 5.5-5s4.9 1.7 5.5 5M14.5 14.6c.8-.4 1.6-.6 2.5-.6 2.2 0 3.8 1.4 4.3 4"/></svg></span>My family</h3>
      <p>For parents helping one or more kids. Your phone opens to a parent home. Each child gets their own lists, garden and progress.</p>
      {checks(["Hand over your phone in Kid mode", 'Link each child’s own iPad or iPhone <span class="pro-mark">PRO</span>', "Two parents? Sign in on both phones and stay in sync"])}
    </div>
    <div class="mode kid reveal" style="--d: .12s;">
      <h3><span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="8" r="3.4"/><path d="M5.5 20c.7-3.8 3.3-6 6.5-6s5.8 2.2 6.5 6"/></svg></span>Just me</h3>
      <p>For one learner on their own device. It opens straight to the colorful kid side, in the theme they pick.</p>
      {checks(["Great for an older kid with their own iPad", "Or for a grown-up practicing their own words", "Same games, garden and Spelling checks"])}
    </div>
  </div>
  <div class="feature-row">
    <div class="fcard reveal">
      <div class="art">{screen("kid-mode", "Kid mode on a parent’s phone: Hi, Maya, with her lists and a Grown-ups button")}
        {bed(("", "#FF8FA3", 46, "left: 8%"), ("bud", "#B78CFF", 30, "left: 18%"), ("sprout", "#FF8FA3", 22, "right: 19%"), ("", "#6FB7FF", 40, "right: 8%"))}</div>
      <div class="body"><h3>Hand over your phone without worry</h3><p>Tap Kid mode at the top of your child’s page. They see only their own lists and can’t change a thing. Grown-ups unlock with Face ID or a passcode.</p></div>
    </div>
    <div class="fcard reveal" style="--d: .12s;">
      <div class="art blue">{screen("ipad-garden", "WordSprout on a child’s linked iPad", "ipad", w=1000, h=749)}
        <div class="synced float" style="left: 28px; bottom: 28px; --d: .8s;"><span class="sync-dot"></span><span>Maya’s iPad <small>· Synced 5 min ago</small></span></div></div>
      <div class="body"><h3>Their own iPad, your lists <span class="pro-mark">PRO</span></h3><p>Link your child’s iPad or iPhone with a QR code. New lists and your recordings arrive in seconds, often before they open the app, and their practice shows up on your phone.</p></div>
    </div>
  </div>
</div></section>

<section class="sec new-band" id="new" aria-labelledby="new-title"><div class="wrap two">
  <div>
    <p class="eyebrow">New in 3.1</p>
    <h2 id="new-title">Share this week’s list with the whole class</h2>
    <p class="sub">Turn a list into a card with the words, a code and a QR code. Post it in the class group chat or print it for the fridge. Other families scan it and the list, with your recordings, lands in their app.</p>
    <p class="teach">Teachers: one card gets the weekly list to every family.</p>
    <ul class="new-list">
      <li><b>Hear it in a sentence</b>Add a sentence to a word; kids tap Sentence to hear it.</li>
      <li><b>Kid mode, one tap</b>Right at the top of your child’s page.</li>
      <li><b>Ready before they open it</b>Linked iPads get new lists in the background.</li>
      <li><b>See when devices synced</b>Each linked device shows its last sync.</li>
    </ul>
  </div>
  <div class="card-stage">
    <div class="ccard tilt" role="img" aria-label="A class card: Week 7 spelling from Ms. Lopez, Room 12, test Friday, Oct 30, twelve words, a QR code and the code K7Q MRT">
      <div class="cb"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 20c0-9 5.5-14.5 15-15-0.5 9.5-6 15-15 15z"/></svg>WordSprout</div>
      <div><div class="ct">Week 7 spelling</div><div class="cf">Ms. Lopez · Room 12</div><div class="cd">Test Friday, Oct 30</div></div>
      <div class="cw">{"".join(f"<span>{w}</span>" for w in CLASS_WORDS)}</div>
      <div class="cq"><div class="qr"><svg viewBox="0 0 25 25" aria-hidden="true" shape-rendering="crispEdges"><path d="{qr_path()}" fill="#1C1C1E"/></svg></div><div><small>Scan, or get WordSprout and tap Use a code</small><div class="code">K7Q MRT</div></div></div>
    </div>
    <div class="phone phone-scan"><div class="scan-screen" role="img" aria-label="The wordsprout.co share page on a phone: A spelling list for you, code K7Q MRT, Open in WordSprout">
      <div class="ss-top"><img src="/img/bee.png" alt="" width="22" height="22"><b>A spelling list for you</b></div>
      <div class="ss-soil"></div>
      <div class="ss-card"><small>Your code</small><span class="c2">K7Q MRT</span><span class="ob">Open in WordSprout</span><span class="og">Get WordSprout</span></div>
      <div class="ss-steps"><i></i><i></i><i></i></div>
    </div></div>
  </div>
</div></section>

<section class="sec" id="pro" aria-labelledby="pro-title"><div class="wrap">
  <div class="center">
    <p class="eyebrow">Pricing</p>
    <h2 id="pro-title">Free to start. Pro is yours for good.</h2>
    <p class="sub">Everything your child needs to practice is free. Pro is a single purchase for families who want more devices and sharing. No subscription.</p>
  </div>
  <div class="plans">
    <div class="plan reveal">
      <h3>Free</h3>
      <div class="price">$0</div>
      <p class="pl">For every family, forever</p>
      {checks(["Lists for every child", "All six games and Spelling checks", "Written, Typed, Tiles and Pick it tests",
               "Your recorded voice or the device voice for every word", "Kid mode, reminders, the garden and progress",
               "Dolch and Fry sight words"])}
      <p class="fine">No ads. No tracking.</p>
    </div>
    <div class="plan pro reveal" style="--d: .12s;">
      <span class="ribbon">Pay once</span>
      <h3>WordSprout Pro</h3>
      <div class="price">$9.99 <small>one time</small></div>
      <p class="pl">Everything in Free, plus</p>
      {checks(["<b>Link your child’s own iPad or iPhone</b>", "<b>Cloud sync and backup</b> across your devices",
               "<b>Share lists</b> with a code or a class card", "<b>Scan a list</b> from a photo of the paper"])}
      <p class="fine">No subscription. Shared with Family Sharing. Price shown in US dollars.</p>
    </div>
  </div>
</div></section>

<section class="sec tight" aria-labelledby="faq-title"><div class="wrap">
  <h2 id="faq-title" class="center">Questions parents ask</h2>
  <div class="faq">
    <details open><summary>Does it work with my child’s school list?</summary><p>Yes. WordSprout is built around whatever list comes home: type it, paste it, or snap a photo of the paper. Any words work, from kindergarten sight words to 5th-grade spelling.</p></details>
    <details><summary>Do I need to record every word?</summary><p>No. The device voice reads any word you haven’t recorded. Record your own voice for words you want to say your way.</p></details>
    <details><summary>Is my child’s data private?</summary><p>WordSprout has no ads, no analytics and no tracking. Photos you add for a child stay on your device. Read the <a href="/privacy/">privacy policy</a>.</p></details>
    <details><summary>Two parents want to use it. How?</summary><p>Sign in to the same WordSprout account on both phones. Lists, recordings and progress stay in sync.</p></details>
  </div>
  <p class="center" style="margin-top: 24px;"><a class="link-arrow" href="/support/">More answers in Support{ARROW}</a></p>
</div></section>

<section class="sec tight" id="get" aria-labelledby="cta-title"><div class="wrap">
  <div class="cta-band">
    <img class="bee" src="/img/bee.png" alt="" width="88" height="88" loading="lazy">
    <h2 id="cta-title">Ready for this week’s list?</h2>
    <p>Free to start on iPhone and iPad. No ads, no tracking, just practice.</p>
    {STORE_BUTTON}
    {meadow(18, scale=.7, grow=False, soil=False)}
  </div>
</div></section>
"""

GUIDES = [
    ("Getting started", ["Open WordSprout and answer “Who’s practicing?”. Choose Just me or My kids.",
        "Open Settings and add each child’s name and color.",
        "Make a list with New list, then add this week’s spelling words.",
        "Your newest list is this week’s list automatically. You can add a test date.",
        "Open your child’s page and tap “Practice with” their name, then hand over the phone."]),
    ("Add this week’s words", ["Open your child’s list, or make a new one with New list.",
        "To type a word, tap Add word and press Return to add the next one.",
        "To use a list from a message or email, copy it, tap Paste a list, and check the words.",
        "To scan paper, tap Photo, choose a picture of the spelling list, and check the words it read. Photo scanning needs WordSprout Pro.",
        "Turn on the “This week’s list” switch to make it this week’s list, and add a test date if there is one."]),
    ("Record your voice", ["Open a list and open a word.", "Tap Record, say the word, then tap Stop recording.",
        "Tap Play to listen back.", "To redo it, tap Record again. The new recording replaces the old one.",
        "To remove it, tap Remove recording. The word goes back to the device voice."]),
    ("Hand your phone to your child", ["Kid mode is part of My family. Switch to it in Settings under How WordSprout is used.",
        "On your child’s page, tap Practice with and their name.",
        "Your child sees only their own lists and games, and can’t change anything.",
        "To leave kid mode, tap Grown-ups, then use Face ID or your passcode, or answer the question.",
        "Kid mode stays on even if the app closes, until a grown-up unlocks it."]),
    ("Link a child’s device", ["Sign in to your account on your phone. Linking devices needs WordSprout Pro.",
        "Open Settings, tap Linked devices, then tap Link a device.", "Choose which children use that device.",
        "On the child’s device, open WordSprout, choose “This is my kid’s device”, and scan the code on your phone.",
        "Their lists and recordings appear there. To rename or remove a device, open it in Linked devices."]),
    ("Read your child’s progress", ["Your home screen shows a card for each child with Ready, Almost and Tricky counts.",
        "Ready means your child spelled the word correctly, with no hints, on two different days.",
        "Almost means one day of correct spelling checks. Tricky words are the ones they missed most recently, and they are named on the card.",
        "Learning means your child has practiced the word in games but hasn’t spelled it on their own yet. Each practice session ends with Spell it, a short check with no hints.",
        "With a test date set, you also see whether they are ready for the test."]),
    ("Practice reminders", ["Open Settings and tap your child’s name. In Just me, the reminder is in Settings itself.",
        "Turn on Remind each day.", "Pick the time that suits your family.",
        "The reminder shows on every device linked to that child. Turn on “Also remind me on this phone” to get it too.",
        "If nothing arrives, allow notifications for WordSprout in your device settings."]),
]

FAQ = [
    ("Who is WordSprout for?", "Kids in kindergarten through 5th grade practicing their weekly spelling and sight words, and the grown-ups who help them. It works for any word list, so adults can use Just me for their own words too."),
    ("Is it free?", "Yes. Lists, games, tests, recordings, kid mode, reminders and progress are free. WordSprout Pro is a one-time purchase that adds linked child devices, cloud sync, sharing lists with a code and photo scanning."),
    ("Two parents want to use it. How?", "Sign in to the same WordSprout account on both phones. Lists, recordings, progress and this week’s list stay in sync."),
    ("I bought Pro before. How do I get it back?", "Open Settings and tap Restore Purchases, signed in with the same Apple ID you used to buy it."),
    ("Will updating lose my lists or recordings?", "No. Updating keeps your lists, recordings, learners and past results. Results from before 3.0 stay in your history; words earn Learned again with two correct days."),
    ("How do I delete my account?", "Open Settings, sign in if needed, and choose Delete account. This removes your account and synced data. Lists stored only on your device stay until you delete them or the app."),
]


# One topic card per guide, in the same order as GUIDES, then Questions.
TOPICS = [
    ("First steps", "#1F7A42", "M5 12h14M13 6l6 6-6 6"),
    ("Type, paste or photo", "#2F6FD6", "M12 5v14M5 12h14"),
    ("Or use the device voice", "#7C4DFF", "M12 4a3 3 0 0 1 3 3v5a3 3 0 0 1-6 0V7a3 3 0 0 1 3-3zM6 11a6 6 0 0 0 12 0M12 17v3"),
    ("Kid mode", "#C2255C", "M7 11V8a5 5 0 0 1 10 0v3M6 11h12v9H6z"),
    ("Your child’s own iPad", "#0F8A7E", "M7 3h10v18H7zM11 18h2"),
    ("Ready, Almost, Tricky", "#C47A00", "M5 19V11M12 19V5M19 19v-6"),
    ("A daily nudge", "#D9480F", "M6 16V11a6 6 0 0 1 12 0v5l2 2H4zM10 21h4"),
]
topic_cards = "".join(
    f'<a class="topic" href="#guide-{i}"><span class="ti" style="background: {color};"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="{icon}"/></svg></span>'
    f'<span><b>{title}</b><small>{sub}</small></span></a>'
    for i, ((title, _), (sub, color, icon)) in enumerate(zip(GUIDES, TOPICS), 1))
topic_cards += ('<a class="topic" href="#questions"><span class="ti" style="background: #1C1A14;"><svg viewBox="0 0 24 24" aria-hidden="true">'
                '<circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .8-1 1.5v.7M12 17h.01"/></svg></span>'
                '<span><b>Questions</b><small>Pro, accounts, updates</small></span></a>')

# Opens a guide when its topic card (or a link to #guide-N) is followed.
OPEN_GUIDE_JS = """(function () {
  function open() { var el = location.hash && document.getElementById(location.hash.slice(1)); if (el && el.tagName === 'DETAILS') el.open = true; }
  window.addEventListener('hashchange', open); open();
})();"""

support = f"""
{band("How can we help?", f'Short guides for every part of WordSprout. Still stuck? Email <a href="mailto:{EMAIL}" style="font-weight: 800;">{EMAIL}</a> and we’ll get back to you, usually within two business days.', narrow=False)}
<div class="wrap">
  <nav class="topics" aria-label="Topics">{topic_cards}</nav>
  <div class="doc2">
    <nav class="toc" aria-label="On this page">
      <p>On this page</p>
      <a href="#guides">How-to guides</a>
      <a href="#questions">Questions</a>
      <a href="#contact">Contact us</a>
    </nav>
    <div>
      <h2 id="guides">How-to guides</h2>
      <div class="acc">
        {"".join(f'<details id="guide-{i}"><summary><span class="n" aria-hidden="true">{i}</span>{t}</summary><ol>' + "".join(f"<li>{s}</li>" for s in steps) + "</ol></details>" for i, (t, steps) in enumerate(GUIDES, 1))}
      </div>
      <h2 id="questions">Questions</h2>
      <div class="acc">
        {"".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ)}
      </div>
      <div class="contact" id="contact">
        <img src="/img/bee.png" alt="" width="72" height="72" loading="lazy">
        <div><h2>Still stuck?</h2><p>Email <a href="mailto:{EMAIL}" style="font-weight: 800;">{EMAIL}</a> with your device (for example, iPhone 16 or iPad), your iOS version and what happened. A screenshot helps a lot.</p></div>
      </div>
    </div>
  </div>
</div>
<script>
{OPEN_GUIDE_JS}
</script>
"""


privacy = f"""
{band("Privacy Policy", "Last updated " + UPDATED)}
<article class="doc"><div class="wrap">
  <p>This policy explains what WordSprout collects, how it is used, and the choices you have.</p>
  <h2>Data we collect</h2>
  {ul(["Account info (email, name, and authentication identifiers).",
       "Children's names. Photos you add for a child stay on your device and are never uploaded.",
       "Word lists, test results, practice results, and which words each child spelled correctly, with the time.",
       "Audio recordings you create in the app.",
       "Reminder times and the names of linked devices.",
       "Purchase entitlement status for Pro unlock and restore flows.",
       "Error reports from signed-in devices (what failed and the device identifier), used to fix problems."])}
  <h2>How we use data</h2>
  {ul(["Provide app features like tests, progress, cloud sync, linked devices, reminders, and Pro unlock access.",
       "Find and fix errors.", "Respond to support requests."])}
  <p class="callout">WordSprout has no ads, no analytics, and no tracking.</p>
  <h2>Linked child devices</h2>
  {ul(["A child's device you link signs in without an email or Apple ID. It gets an anonymous identifier tied to your account.",
       "It receives only the lists and progress of the children you choose, and sends their practice results back to you.",
       "Unlinking a device stops its updates and hides your family's lists on it. They stay on the device so practice saved offline isn't lost if you link it again; deleting WordSprout from the device removes them."])}
  <h2>Cloud sync and providers</h2>
  {ul(["Supabase stores your account data and synced content.",
       "Apple Sign In and Google Sign-In are available for authentication.",
       "Apple processes in-app purchases and purchase restoration."])}
  <p class="callout">We do not sell your personal information.</p>
  <h2>Your choices</h2>
  {ul(["You can edit or delete your word lists and recordings.", "You can sign out to stop cloud sync.",
       "You can restore previous Pro purchases from the upgrade screen.",
       "If you are signed in, you can delete your account from the Settings screen.",
       "If you used Apple Sign In, you can also revoke WordSprout later from your Apple ID settings."])}
  <h2>Contact</h2>
  <p>Questions about privacy? Email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
</div></article>
"""

terms = f"""
{band("Terms of Service", "Last updated " + UPDATED)}
<article class="doc"><div class="wrap">
  <p>By using WordSprout, you agree to these terms.</p>
  <h2>Use of the app</h2>
  {ul(["Use WordSprout only for lawful, personal, or educational purposes.",
       "Do not misuse the app, attempt unauthorized access, or interfere with the service."])}
  <h2>Accounts and content</h2>
  {ul(["You are responsible for the accuracy of the content you create.",
       "You retain ownership of your word lists and recordings.",
       "You grant WordSprout a limited license to store and sync your content to provide the service."])}
  <h2>Third-party services</h2>
  <p>WordSprout uses Supabase for cloud storage, Apple Sign In and Google Sign-In for authentication, and Apple In-App Purchase for Pro unlock billing.</p>
  <h2>Disclaimer and liability</h2>
  {ul(["The app is provided \"as is\" without warranties.",
       "WordSprout is not liable for indirect or consequential damages."])}
  <h2>Changes and contact</h2>
  {ul(["We may update these terms and will revise the date above.",
       f'Questions? Contact <a href="mailto:{EMAIL}">{EMAIL}</a>.'])}
</div></article>
"""


not_found = f"""
{band("This page isn’t here", "Class pages, class codes and the teacher portal are paused while we focus on families. Shared list codes still work inside the app: open WordSprout and choose Use a code.")}
<article class="doc"><div class="wrap">
  <p><a class="btn" href="/">Go to WordSprout</a></p>
</div></article>
"""

page("index.html", "WordSprout", "Spelling and sight word practice for kids in K–5. Short, fun games, a garden that grows, and a clear view of tricky words for parents.", home, "/")
page("support/index.html", "Support", "How-to guides, answers and contact for WordSprout.", support, "/support/")
page("privacy/index.html", "Privacy Policy", "What WordSprout collects, how it is used, and your choices.", privacy, "/privacy/")
page("terms/index.html", "Terms of Service", "The terms for using WordSprout.", terms, "/terms/")
page("404.html", "Page not found", "This page isn’t here.", not_found, "/404")
# Old site paths that people or the App Store may still link to.
for old, new in [("contact", "/support/"), ("faq", "/support/"), ("getting-started", "/support/"),
                 ("about", "/"), ("pricing", "/"), ("teacher-guide", "/support/"), ("login", "/"), ("signup", "/")]:
    redirect(old, new)
print("Built", ROOT)
