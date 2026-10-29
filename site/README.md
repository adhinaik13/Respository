# Adi Naik — Portfolio site

A lightweight, responsive portfolio site for the profile at [github.com/vankudothuadhinaik](https://github.com/vankudothuadhinaik).

## Run locally

This is a static site with no build step:

```bash
cd site
python -m http.server 8000
```

Open http://localhost:8000.

## Deploy

The `.github/workflows/deploy-portfolio.yml` workflow publishes this folder to GitHub Pages when changes reach `main` or when run manually. In repository Settings → Pages, select **GitHub Actions** as the build and deployment source if it is not already configured.

## Content and assets

- Project descriptions, repositories, and contribution states are based on the linked public repositories and the existing profile README.
- Project visuals are illustrative diagrams, not product screenshots or live metrics.
- The current hero uses the existing illustrated portfolio SVG. A personal photo and talking-intro video have not been supplied, so the site does not pretend that an identity-matched character or generated video already exists.
- The résumé download and ID-card data section are omitted until a current résumé PDF is provided. No résumé facts or certifications are invented.

## Accessibility and performance

Semantic landmarks, keyboard focus styles, responsive layouts, reduced-motion support, lazy-loaded project visuals, and no runtime framework dependencies are included. External fonts and the Uptime Sentinel architecture illustration are loaded from their public URLs.
