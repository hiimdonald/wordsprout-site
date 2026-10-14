#!/usr/bin/env python3
"""Writes the static pages for wordsprout.co. Run: python3 tools/build.py (from the repo root).
Edit the content here, then re-run; GitHub Pages serves the generated .html files as they are."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APP_STORE = "https://apps.apple.com/us/app/wordsprout-spelling-practice/id6741597283"
EMAIL = "hello@wordsprout.co"
UPDATED = "October 14, 2026"
APPLE = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16.37 12.6c-.02-2.3 1.88-3.4 1.97-3.46-1.07-1.57-2.74-1.78-3.33-1.8-1.42-.14-2.77.83-3.49.83-.72 0-1.83-.81-3.01-.79-1.55.02-2.98.9-3.78 2.29-1.61 2.8-.41 6.94 1.16 9.21.77 1.11 1.68 2.36 2.88 2.31 1.16-.05 1.6-.75 3-.75s1.79.75 3.01.72c1.24-.02 2.03-1.13 2.79-2.25.88-1.29 1.24-2.53 1.26-2.6-.03-.01-2.42-.93-2.46-3.71zM14.08 5.85c.64-.77 1.07-1.85.95-2.92-.92.04-2.03.61-2.69 1.38-.59.68-1.11 1.77-.97 2.82 1.03.08 2.07-.52 2.71-1.28z"/></svg>')


def page(path, title, description, body, current=""):
    nav = [("/", "Home"), ("/support/", "Support"), ("/privacy/", "Privacy"), ("/terms/", "Terms")]
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
<link rel="icon" type="image/png" href="/favicon.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
</head>
<body>
<header class="site-header"><div class="wrap">
  <a class="brand" href="/"><img src="/img/bee.png" alt="" width="40" height="40">WordSprout</a>
  <nav class="nav" aria-label="Main">{links}</nav>
</div></header>
<main>
{body}
</main>
<footer class="site-footer"><div class="wrap">
  <span>© 2026 WordSprout · <a href="mailto:{EMAIL}">{EMAIL}</a></span>
  <nav aria-label="Footer"><a href="/support/">Support</a><a href="/privacy/">Privacy Policy</a><a href="/terms/">Terms of Service</a></nav>
</div></footer>
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


SHOTS = [
    ("01-practice-feels-like-play", "A practice game with big, friendly letters"),
    ("02-every-word-grows", "A child's garden where each learned word blooms"),
    ("03-see-tricky-words", "The parent home showing each child's tricky words"),
    ("04-add-this-weeks-list", "Adding this week's spelling list"),
    ("05-every-word-read-aloud", "Every word read aloud"),
    ("06-ready-for-test-day", "Ready for the spelling test"),
    ("07-one-big-cheer", "The celebration at the end of a session"),
    ("08-hand-over-your-phone", "Kid mode on a parent's phone"),
    ("09-daily-reminder", "A daily practice reminder for each child"),
    ("10-six-games", "Six practice games"),
]

home = f"""
<section class="hero" aria-labelledby="hero-title"><div class="wrap">
  <div>
    <h1 id="hero-title">Help every word bloom.</h1>
    <p class="lede">WordSprout turns this week's spelling and sight words into short, happy practice for kids in K–5, and shows parents exactly which words are tricky.</p>
    <div class="actions">
      <a class="button" href="{APP_STORE}">{APPLE}Get it on the App Store</a>
      <span class="note">iPhone and iPad · Free to start</span>
    </div>
  </div>
  <div class="hero-shot"><img src="/img/screens/02-every-word-grows.jpg" alt="Maya's garden: each spelling word is a plant that blooms when she learns it" width="550" height="1196"></div>
</div></section>
<div class="flowers" aria-hidden="true"></div>

<section aria-labelledby="how-title"><div class="wrap">
  <h2 id="how-title">Built for the weekly spelling list</h2>
  <p class="section-lede">Add the words from school in a minute. Your child practices in short sessions. You see who's ready for the test.</p>
  <div class="features">
    <div class="feature"><div class="emoji" aria-hidden="true">✏️</div><h3>Add words your way</h3><p>Type them, paste a list from an email, or snap a photo of the paper list.</p></div>
    <div class="feature"><div class="emoji" aria-hidden="true">🎙️</div><h3>Every word speaks</h3><p>Record your own voice, or let the device voice read any word you haven't recorded.</p></div>
    <div class="feature"><div class="emoji" aria-hidden="true">🎮</div><h3>Six fun games</h3><p>Flashcards, Pick it, Missing letter, Scramble, Memory match and Word search, mixed into one short session.</p></div>
    <div class="feature"><div class="emoji" aria-hidden="true">🌼</div><h3>A garden that grows</h3><p>Each word is a plant. Spell it right on two different days and it blooms. Plants never wilt.</p></div>
    <div class="feature"><div class="emoji" aria-hidden="true">👀</div><h3>Know what's tricky</h3><p>See Ready, Almost and Tricky words for each child, and whether they're ready for test day.</p></div>
    <div class="feature"><div class="emoji" aria-hidden="true">🔒</div><h3>Kid mode</h3><p>Hand over your phone. Kids see only their own lists and can't change anything until a grown-up unlocks it.</p></div>
  </div>
</div></section>

<section aria-labelledby="screens-title" style="padding-top:0"><div class="wrap">
  <h2 id="screens-title">Take a look</h2>
  <div class="screens" tabindex="0" aria-label="App screenshots, scroll sideways">
    {"".join(f'<img src="/img/screens/{name}.jpg" alt="{alt}" width="550" height="1196" loading="lazy">' for name, alt in SHOTS)}
  </div>
</div></section>

<section aria-labelledby="family-title" style="padding-top:0"><div class="wrap">
  <h2 id="family-title">For the whole family</h2>
  <div class="split">
    <div class="panel"><h3>Free</h3>{ul(["Word lists for every child", "Every game and spelling test", "Device voice for every word, and your own recordings", "Kid mode, reminders and progress"])}</div>
    <div class="panel"><h3>WordSprout Pro</h3>{ul(["Link your child's own iPad or iPhone", "Cloud sync and backup across your devices", "Scan a spelling list from a photo", "Share lists with a code", "A one-time purchase, shareable with Family Sharing"])}</div>
  </div>
</div></section>

<section style="padding-top:0"><div class="wrap">
  <div class="cta">
    <h2>Ready for this week's list?</h2>
    <p>No ads. No tracking. Just practice.</p>
    <a class="button" href="{APP_STORE}">{APPLE}Get it on the App Store</a>
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
        "Ready means your child spelled the word correctly on two different days.",
        "Almost means they are close. Tricky words are the ones they keep missing, and they are named on the card.",
        "Not yet means your child hasn’t practiced the word enough to tell.",
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

support = f"""
<article class="doc"><div class="wrap">
  <h1>Support</h1>
  <p class="updated">Need help? Email <a href="mailto:{EMAIL}">{EMAIL}</a> and we’ll get back to you, usually within two business days.</p>
  <h2>How-to guides</h2>
  {"".join(f'<details><summary>{t}</summary><ol>' + "".join(f"<li>{s}</li>" for s in steps) + "</ol></details>" for t, steps in GUIDES)}
  <h2>Questions</h2>
  {"".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ)}
  <h2>Still stuck?</h2>
  <p class="callout">Email <a href="mailto:{EMAIL}">{EMAIL}</a> with your device (for example, iPhone 16 or iPad), your iOS version and what happened. A screenshot helps a lot.</p>
</div></article>
"""

privacy = f"""
<article class="doc"><div class="wrap">
  <h1>Privacy Policy</h1>
  <p class="updated">Last updated {UPDATED}</p>
  <p>This policy explains what WordSprout collects, how it is used, and the choices you have.</p>
  <h2>Data we collect</h2>
  {ul(["Account info (email, name, and authentication identifiers).",
       "Children's names and optional photos you add for each learner.",
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
       "Unlinking the device removes your family's data from it."])}
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
<article class="doc"><div class="wrap">
  <h1>Terms of Service</h1>
  <p class="updated">Last updated {UPDATED}</p>
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
<article class="doc"><div class="wrap">
  <h1>This page isn’t here</h1>
  <p class="updated">Class pages, class codes and the teacher portal are paused while we focus on families. Shared list codes still work inside the app: open WordSprout and choose Use a code.</p>
  <p><a class="button" href="/">Go to WordSprout</a></p>
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
