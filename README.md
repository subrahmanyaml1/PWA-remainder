# TaskPulse — Personal Work Reminder PWA

A Progressive Web App that sends time-based work reminders.
Install it directly from Chrome — no app store needed.

## Files
```
pwa-reminder/
├── index.html          ← Main app UI + logic
├── manifest.json       ← Makes Chrome offer "Install App"
├── sw.js               ← Service Worker (offline + notifications)
├── generate_icons.py   ← Run once to create icons
└── icons/
    ├── icon-192.png
    └── icon-512.png
```

## How to Run Locally (for testing)

```bash
# Option 1: Python (built-in)
python3 -m http.server 8080
# Open: http://localhost:8080

# Option 2: Node.js
npx serve .
```

> ⚠️ Must use localhost or HTTPS — PWAs won't install over plain http://

## How to Deploy (Free, with HTTPS)

### GitHub Pages (recommended)
1. Create a new GitHub repository
2. Upload all files to the repo
3. Go to Settings → Pages → Source: main branch
4. Your app is live at: https://yourusername.github.io/repo-name

### Netlify (drag & drop)
1. Go to https://netlify.com
2. Drag the entire `pwa-reminder/` folder onto the deploy area
3. Done — instant HTTPS URL

### Vercel
```bash
npm install -g vercel
vercel
```

## Install from Chrome

Once deployed on HTTPS:
1. Open the URL in Chrome
2. Look for ⊕ icon in the address bar (or ⋮ menu → "Install TaskPulse")
3. Click Install
4. App appears on desktop / home screen

## Features
- ✅ Add reminders with time, category, priority
- ✅ Browser notifications at the right time
- ✅ Repeat options (daily, weekdays, weekends)
- ✅ Filter by category
- ✅ Works offline (cached by Service Worker)
- ✅ Installable from Chrome on desktop & Android
- ✅ Data saved in localStorage

## To Replace Icons
Replace `icons/icon-192.png` and `icons/icon-512.png` with your own images.
Recommended: square images, at least 512×512px.
