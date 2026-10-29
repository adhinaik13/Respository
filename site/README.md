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
- The selected-work section includes accessible filters for systems, backend, developer tools, security, and data projects.
- The contact section includes a copy-email action with a fallback for browsers that block clipboard access.
- The hero includes an original animated vector developer character and a bundled portfolio illustration. The character is illustrative, not a photographic likeness. A personal photo and talking-intro video have not been supplied, so the site does not claim to contain an identity-matched character or finished talking video.
- The résumé download and ID-card data section are omitted until a current résumé PDF is provided. No résumé facts or certifications are invented.

## Accessibility and performance

Semantic landmarks, keyboard focus styles, responsive layouts, reduced-motion support, accessible project filters, lazy-loaded project visuals, and no runtime framework dependencies are included. All illustration assets are bundled locally. The page has no third-party scripts, font downloads, or image-CDN dependencies.
