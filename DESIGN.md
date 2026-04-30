---
version: "2.0.0"
name: Privé Perfumes
description: "Luxury fragrance retailer in Honduras. Editorial minimalism — sharp edges, warm neutrals, navy authority, pumpkin warmth. Individualism per product. Friendly exclusive — not stuffy, not cheap."

colors:
  primary: "#192E49"
  on-primary: "#FFFFFF"
  text-heading: "#192E49"
  text-body: "#2E2E2E"
  text-muted: "#8A8A8A"
  background: "#FFFFFF"
  surface: "#F5F1EC"
  border: "#E0E0E0"
  border-strong: "#ABABAB"
  accent: "#E87722"
  accent-hover: "#D06318"
  accent-light: "#FFF3ED"
  accent-gold: "#B8956A"
  success: "#5A7A6F"
  success-bg: "#DEE4E2"
  error: "#B3332B"
  error-bg: "#FAF1F0"

typography:
  heading:
    fontFamily: "Jost"
    fontSize: "2rem"
    fontWeight: 400
    letterSpacing: "0.18em"
    textTransform: uppercase
  heading-hero:
    fontFamily: "Jost"
    fontSize: "3.5rem"
    fontWeight: 300
    letterSpacing: "0.02em"
    textTransform: uppercase
  heading-small:
    fontFamily: "Jost"
    fontSize: "0.8125rem"
    fontWeight: 400
    letterSpacing: "0.18em"
    textTransform: uppercase
  body:
    fontFamily: "Barlow"
    fontSize: "0.9375rem"
    fontWeight: 400
    lineHeight: "1.55"
  body-bold:
    fontFamily: "Barlow"
    fontSize: "0.9375rem"
    fontWeight: 600
    lineHeight: "1.55"
  label:
    fontFamily: "Jost"
    fontSize: "0.6875rem"
    fontWeight: 500
    letterSpacing: "0.18em"
    textTransform: uppercase
  price:
    fontFamily: "Jost"
    fontSize: "1.25rem"
    fontWeight: 400
    letterSpacing: "0.04em"
  mood-sentence:
    fontFamily: "Barlow"
    fontSize: "0.9375rem"
    fontWeight: 400
    fontStyle: italic
    lineHeight: "1.5"

rounded:
  storefront: 0px
  internal: 14px

spacing:
  xs: 8px
  sm: 16px
  md: 24px
  lg: 40px
  xl: 64px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.storefront}"
    height: 48px
    typography: "{typography.label}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    rounded: "{rounded.storefront}"
    height: 48px
    typography: "{typography.label}"
  button-cta:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.storefront}"
    height: 48px
    typography: "{typography.label}"
    hoverBackgroundColor: "{colors.accent-hover}"
  nav-bar:
    backgroundColor: "{colors.on-primary}"
    borderBottom: "1px solid {colors.border}"
    height: 64px
  card:
    backgroundColor: "{colors.on-primary}"
    border: "1px solid {colors.border}"
    rounded: "{rounded.storefront}"
  card-interactive:
    backgroundColor: "{colors.on-primary}"
    border: "1px solid {colors.border}"
    rounded: "{rounded.storefront}"
    hoverShadow: "0 4px 12px rgba(0,0,0,0.06)"
  badge-tag:
    typography: "{typography.label}"
    padding: "4px 12px"
    rounded: "{rounded.storefront}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  badge-limited:
    backgroundColor: "{colors.accent-gold}"
    textColor: "#000000"
  badge-exclusive:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
  badge-classic:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-body}"
  input-field:
    backgroundColor: "{colors.on-primary}"
    border: "1px solid {colors.border}"
    rounded: "{rounded.storefront}"
    height: 48px
    focusBorderColor: "{colors.primary}"

---

## Brand Identity

**Privé is friendly exclusive.** Not stuffy luxury, not mass-market friendly. The brand occupies the space between — accessible warmth with premium intent. Think: the person who knows fragrances but doesn't make a show of it.

### Personality
- **Confident, not arrogant.** We know our products. We don't need to prove it with logos everywhere.
- **Warm, not casual.** Every interaction feels personal, like a knowledgeable friend recommending something special.
- **Masculine-leaning, not exclusionary.** The navy + orange palette has a masculine energy, but warmth and approachability keep it open. Think of it as a well-designed men's store that women also love browsing.
- **Premium, not expensive.** We signal quality through restraint and detail, not through price flashing or gold everywhere.

### Voice
- Direct, no fluff. Short sentences that respect the reader's time.
- Mood over notes. "La hora azul, antes de que alguien encienda una luz" beats "bergamota, pachulí, sándalo."
- Spanish-first for all customer-facing content. English only for internal tools and developer documentation.
- Max 2 emojis per asset. Zero in editorial contexts.
- No generic greetings, no hashtag spam, no AI-slop phrases.

## Colors

The palette is built on high-contrast neutrals with warm undertones and two accent colors with distinct roles.

- **Primary (#192E49):** Deep ink navy. The anchor. Used for headings, primary buttons, brand marks, navigation. The single most important color. Masculine, authoritative, confident.
- **Accent (#E87722):** Pumpkin orange. The warmth. Used for CTAs, active states, product interactions, star ratings, fragrance family badges, hover highlights. This is the energy of the brand — approachable, warm, human. Hover state: #D06318 (darker, richer).
- **Accent Gold (#B8956A):** Caramel gold. The exclusivity signal. Used ONLY for limited edition badges, premium tier markers, and special collection tags. Never as a CTA. Never as a large fill. This color says "rare" — use it sparingly so it keeps meaning.
- **Text Body (#2E2E2E):** Near-black for body copy. Softer than pure black.
- **Background (#FFFFFF):** Pure white. Every surface starts here.
- **Surface (#F5F1EC):** Warm cream. The secondary background — not grey, not cold. Warm red/yellow undertones complement the navy. Used for card alternatives, secondary buttons, hover states.
- **Border (#E0E0E0):** Light neutral separator.
- **Success (#5A7A6F):** Muted sage. In-stock indicators, confirmations.
- **Error (#B3332B):** Deep brick red. Sale prices, out-of-stock alerts. Text only, never large fills.

### Color Rules

- Navy is the ONLY color for headings and primary actions
- Pumpkin (#E87722) is the primary accent for CTAs, interactions, and active states
- Gold (#B8956A) is reserved for exclusivity signals only — never for CTAs or large areas
- Surface (#F5F1EC) replaces grey everywhere — warm, not clinical
- Never introduce new colors without updating this file
- No gradients, no transparency overlays

### Accent Shade Scale

| Token | Hex | Use |
|-------|-----|-----|
| accent-light | #FFF3ED | Hover background on white cards |
| accent | #E87722 | CTAs, active states, badges, icons |
| accent-hover | #D06318 | Button hover, pressed states |

## Typography

Two fonts, strict roles. Jost for structure (authority). Barlow for voice (warmth).

- **Jost (headings):** Geometric sans-serif. Always uppercase. Tracking 0.18em for labels, 0.02em for hero. Weight 300 for display, 400 for standard, 500 for small labels. Clean, modern, slightly masculine. Never italic.
- **Barlow (body):** Humanist sans-serif. Always sentence case. Weight 400 for standard, 600 for emphasis. Italic ONLY for mood sentences and editorial voice. Friendly, warm, readable.

### Why These Two Work Together

Jost is geometric and sharp — it gives structure and authority. Barlow is rounder and softer — it gives warmth and approachability. The contrast between them IS the brand personality: structured confidence + friendly voice.

### Typography Rules

- Jost is NEVER used for body text
- Barlow is NEVER used for headings or navigation
- Mood sentences (italic Barlow) are the ONLY expressive typographic element
- All-caps Jost with wide tracking = navigation, badges, tags, buttons
- Never mix the two families in the same element

## Layout

- Max container width: 1600px
- Grid: 20 columns (desktop), 10 columns (mobile)
- Gutter: 24px (mobile), 40px (desktop)
- Vertical rhythm: 36px (mobile), 48px (tablet), 64px (desktop)
- All corners: 0px radius on storefront — no exceptions
- Borders: 1px solid {colors.border} for separation
- Shadows: ultra-subtle, 0.04-0.06 opacity only

## Two Design Contexts

### Storefront (priveperfumes.com, marketing, Claude Design)
- **Accent:** #E87722 pumpkin orange
- **Border radius:** 0px everywhere
- **Fonts:** Jost (headings) + Barlow (body)
- **Feel:** Editorial luxury, sharp, warm

### Internal Tools (prive-staff, prive-portal, dashboards)
- **Accent:** #E87722 pumpkin orange
- **Border radius:** 14px
- **Fonts:** Jost only (simplified)
- **Feel:** Clean, efficient, hacker aesthetic

## Logo

### SVG Assets (in assets/)
- `logo-wordmark-v4.svg` — **USE THIS FOR BANNERS.** viewBox: "340 790 1320 345" (tightly cropped to letterforms). Has built-in white fill + pumpkin #E87722 accent on É
- `logo-wordmark-mono.svg` — Same viewBox, monochrome treatment (no accent)
- `logo-I-centered-v4.svg` — Circle mark with centered PRIVÉ. viewBox: 2000×2000 square (for circle composition, not standalone wordmark)
- `logo-circle-v4.svg` — Standard circle mark
- `logo-circle-accent.svg` — Circle mark with accent treatment
- `logo-letters-v4.svg` — **DO NOT USE FOR BANNERS.** viewBox is 2000×2000 square — letters are tiny in the canvas

### Logo Treatments
- **Style A (Monochrome):** All letterforms same color. Navy on white, or white on navy. Clean, unified
- **Style B (Accent Highlight):** Letterforms in primary color (navy or white), É accent in pumpkin #E87722

### Logo Sizing for Banners
- **2000×980 desktop:** Wordmark at 700×184px (3.8:1 ratio from viewBox)
- **750×735 mobile:** Wordmark at 260×68px (fits within mobile viewport)
- **Header nav:** Wordmark at 140×37px
- **Never exceed the viewport width** — a 400px logo doesn't fit in 375px

### Logo Pitfalls
- **Never use `logo-letters-v4.svg` for banner exports** — its 2000×2000 square viewBox makes the wordmark invisible when scaled
- **Never apply CSS `filter: invert()` to the logo** — it inverts the pumpkin accent along with the letterforms, breaking the É
- **Never add fake accent divs over the logo** — the SVG has a built-in #E87722 accent path
- **Always maintain 3.8:1 aspect ratio** — derived from viewBox 1320×345. Don't squish

## Shapes

Zero border radius on storefront. Every element — buttons, cards, inputs, badges, modals — uses sharp 90-degree corners. This is the editorial character: precise, intentional, no softening.

## Components

### Buttons
- Primary: Navy background, white text, 48px height, 0px radius
- Secondary: Cream (#F5F1EC) background, navy text, same structure
- CTA: Pumpkin (#E87722) background, white text — primary purchase/engagement actions. Hover: #D06318
- All buttons: 0px radius, subtle shadow on hover (no color change except CTA)

### Cards
- White background, 1px border, no border radius
- Hover: subtle shadow (0.04 opacity), no border color change
- Structure: image → metadata → name → description → specs → price → CTA

### Navigation
- White background, 1px bottom border
- Logo: navy with white "PRIVÉ" in Jost uppercase
- Active state: opacity or muted — no underline, no background

### Tags and Badges
- No border radius, no icons
- "NUEVO": navy bg, white text
- "EDICIÓN LIMITADA": gold (#B8956A) bg, black text
- "EXCLUSIVO": pumpkin (#E87722) bg, white text
- "CLÁSICO": cream bg, dark text
- Small caps Jost with wide tracking

## Banners (Shopify & Marketing)

### Dimensions
- **Desktop:** 2000×980px (Shopify recommended)
- **Mobile:** 750×735px (proportional)
- **Format:** JPG at 92% quality (Shopify does not reliably support WebP for all placements)
- **Max file size:** Under 200KB per banner

### Typography Proportions (Critical)
Banners are wide canvases — text must COMMAND the space. Luxury fragrance banners follow strict proportional rules:

- **Headings must dominate 30-40% of vertical height.** For a 980px canvas, headings (including line-height) should occupy 300-400px
- **Heading-to-subtext ratio: minimum 3:1.** If heading is 150px, subtext is 50px. If heading is 120px, subtext is 40px
- **Subtext minimum: 28px on a 2000px wide banner.** Anything smaller is unreadable
- **CTA bars: 80-90px height, 24-28px text**
- **Text structure:** subheading (label) → heading (statement) → body copy (1-2 sentences)

### Desktop Font Sizes (2000×980)
- Main headings: 120-160px (varies by banner)
- Subtext/descriptions: 36-48px
- CTA text: 24-28px
- Taglines: 36-42px
- Navigation labels: 28-32px

### Mobile Font Sizes (750×735)
- Main headings: 48-72px
- Subtext/descriptions: 24-32px
- CTA text: 20-24px

### Banner Copy Structure
Every banner follows:
1. **Subheading** — all-caps Jost, wide tracking, small: "FRAGANCIAS DE AUTOR · DESDE 2022"
2. **Heading** — large Jost, the statement: "Lo que llevas dice más que tu nombre."
3. **Body** — 1-2 sentences Barlow, mood-anchored, not catalogue copy

### Banner Pitfalls
- **Never use CSS `filter: invert()` on SVG logos** — it inverts accent colors too, breaking the pumpkin É
- **Never use fake accent overlays** — if the SVG has a built-in accent path, use it, don't add a positioned div
- **SVG viewBox must be cropped to the artwork** — never use a 2000×2000 square viewBox for a wordmark; use the tight viewBox (e.g., "340 790 1320 345")
- **Never use `html2canvas` output for production** — it misses fonts and SVGs; use Playwright/headless browser for image exports
- **Never design banners for 1920×600** — always use Shopify's 2000×980 recommendation
- **Inline SVG paths break during regex/file operations** — use data URIs for exports, relative paths for live page

## Do's and Don'ts

### Do
- Use warm cream (#F5F1EC) for secondary surfaces
- Use pumpkin (#E87722) for CTAs and interaction points
- Use gold (#B8956A) sparingly for premium/exclusive signals only
- Write mood-anchored copy in italic Barlow
- Keep layouts spacious with deliberate vertical rhythm
- Design for warm/humid tropical context — airy, not heavy
- Use Spanish for all customer-facing text
- Price format: "L. X,XXX" (lempiras, period for thousands)

### Don't
- Never use border-radius on storefront elements
- Never use teal (#2A9D8F), green (#108474), or flame (#FF4500) — all dead
- Never use serif fonts
- Never use gradients or color overlays
- Never round buttons, cards, or badges on storefront
- Never use cute or playful language
- Never use more than 2 emojis in any asset
- Never use grey (#F5F5F5) for surfaces — use warm cream (#F5F1EC)
- Never use hashtag spam
- Never use gold (#B8956A) for CTAs or large fills
- Never use pumpkin (#E87722) for body text or headings
