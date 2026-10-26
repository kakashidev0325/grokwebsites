# grokwebsites

Static meme-coin landing pages. Each site lives in its own folder and is deployed as its own Vercel project, with that folder set as the project root directory.

## Layout

One folder per site. Each folder is a self-contained static site:

- `index.html` — the page
- `assets/` — images and other static files
- `vercel.json` — Vercel project settings for that site
- `site.json` — the inputs used to build the page (name, ticker, links, and related fields)

Example: `bonkle/` is the Bonkle site.
