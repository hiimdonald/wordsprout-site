# wordsprout.co

The static website for WordSprout, served by GitHub Pages at https://wordsprout.co.

- Edit the page content in `tools/build.py`, then run `python3 tools/build.py` to regenerate the `.html` files and commit them.
- Styles are in `styles.css`. Motion is CSS only (plus a small scroll script in each page) and stops under Reduce Motion.
- App screens are in `img/app/` as WebP with a JPEG fallback, cropped from the phone and iPad screens in the app repo's `marketing/app-store/3.0`. The class card and Home Screen widgets on the home page are drawn in HTML.
- `s/index.html` (the share-code page that class card QR codes open) is hand-written; keep its header and footer in step with `tools/build.py`.
- `CNAME` sets the custom domain. `404.html` handles old portal links (class codes, teacher pages).
- The privacy policy and terms must match the in-app versions (Settings › Privacy Policy and Terms of Service).
