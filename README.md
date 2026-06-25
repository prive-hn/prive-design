# Privé Design System

Single source of truth for Privé Perfumes visual identity. This repo uses Google's `DESIGN.md` format: YAML front matter for machine-readable tokens, markdown prose for human design rationale.

## What's Here

| File | Purpose |
|------|---------|
| `DESIGN.md` | Canonical Privé design tokens + rationale (Google DESIGN.md format) |
| `REFERENCE-google-design-spec.md` | Local reference for the Google DESIGN.md schema, CLI, and lint rules |
| `index.html` | Live visual styleguide — colors, typography, components, voice |
| `banners.html` | Shopify/banner styleguide and export source |
| `render-banners.py` | Playwright renderer for Shopify banner JPG exports |

## Live

Deployed at **https://prive-design.fly.dev**

## Colors

| Token | Hex | Role |
|-------|-----|------|
| Primary | `#192E49` | Navy — headings, buttons, brand |
| Display accent | `#E87722` | Pumpkin — decorative accents, icons, large fills, star ratings |
| CTA accent | `#A85310` | Dark pumpkin — only orange approved for white CTA text |
| Accent gold | `#B8956A` | Caramel — exclusive signals ONLY |
| Surface | `#F5F1EC` | Warm cream — secondary bg |
| Text body | `#2E2E2E` | Body copy |
| Text muted | `#6E6E6E` | Captions/metadata; AA on white |
| Error | `#B3332B` | Sale, out-of-stock |

## Dead Colors (Never Use)

- `#8A8A8A` muted text — fails WCAG AA on white
- `#D06318` old CTA hover — not enough contrast with white text
- `#2A9D8F` teal — Judge.me/plugin legacy
- `#108474` green — old accent
- `#FF4500` flame — old accent

## Typography

- **Jost** — headings, labels, nav, buttons (uppercase, tracking 0.18em)
- **Barlow** — body, mood sentences, descriptions (sentence case, italic for mood only)

## Two Contexts

- **Storefront**: 0px radius, Jost + Barlow
- **Internal tools**: 14px radius, light theme, same Privé color tokens

## Validate

```bash
npx @google/design.md lint DESIGN.md
npx @google/design.md export --format json-tailwind DESIGN.md > tailwind.theme.json
npx @google/design.md export --format css-tailwind DESIGN.md > theme.css
```
