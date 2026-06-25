# Google DESIGN.md Reference

Privé's `DESIGN.md` follows the Google Labs [`google-labs-code/design.md`](https://github.com/google-labs-code/design.md) format. Tokens in YAML front matter are normative. Markdown prose explains intent, mood, and application rules for humans and AI coding agents.

## File Structure

A DESIGN.md file has two layers:

1. **YAML front matter** — machine-readable design tokens, delimited by `---` at the top of the file.
2. **Markdown body** — human-readable design rationale organized into `##` sections.

## Token Schema

```yaml
---
version: alpha
name: Privé Perfumes
description: Luxury fragrance retailer — Honduras.
colors:
  <token-name>: <Color>
typography:
  <token-name>:
    fontFamily: <string>
    fontSize: <Dimension>
    fontWeight: <number>
    lineHeight: <Dimension | number>
    letterSpacing: <Dimension>
    fontFeature: <string>
    fontVariation: <string>
rounded:
  <scale-level>: <Dimension>
spacing:
  <scale-level>: <Dimension | number>
components:
  <component-name>:
    backgroundColor: <Color | "{token.ref}">
    textColor: <Color | "{token.ref}">
    typography: <"{token.ref}">
    rounded: <Dimension | "{token.ref}">
    padding: <Dimension>
    size: <Dimension>
    height: <Dimension>
    width: <Dimension>
---
```

## Token Types

| Type | Format | Example |
|------|--------|---------|
| Color | Any CSS color string | `"#192E49"`, `"oklch(62% 0.18 250)"` |
| Dimension | number + unit (`px`, `em`, `rem`) | `48px`, `"-0.02em"` |
| Token reference | `{path.to.token}` | `{colors.primary}` |
| Typography | object | `fontFamily`, `fontSize`, `fontWeight`, `lineHeight`, `letterSpacing` |

Component properties are intentionally narrow: `backgroundColor`, `textColor`, `typography`, `rounded`, `padding`, `size`, `height`, `width`.

## Canonical Markdown Section Order

Sections are optional, but present sections must appear in this order:

1. `## Overview` (alias: Brand & Style)
2. `## Colors`
3. `## Typography`
4. `## Layout` (alias: Layout & Spacing)
5. `## Elevation & Depth` (alias: Elevation)
6. `## Shapes`
7. `## Components`
8. `## Do's and Don'ts`

Unknown sections are preserved. Duplicate section headings are errors.

## CLI

```bash
npx @google/design.md lint DESIGN.md
npx @google/design.md diff DESIGN.md DESIGN-v2.md
npx @google/design.md export --format json-tailwind DESIGN.md > tailwind.theme.json
npx @google/design.md export --format css-tailwind DESIGN.md > theme.css
npx @google/design.md export --format dtcg DESIGN.md > tokens.json
npx @google/design.md spec --rules
```

Windows/PowerShell: use the dot-free alias:

```bash
npx -p @google/design.md designmd lint DESIGN.md
```

## Lint Rules

| Rule | Severity | Checks |
|------|----------|--------|
| `broken-ref` | error | Unresolved token references |
| `missing-primary` | warning | No `primary` color |
| `contrast-ratio` | warning | Component bg/text below WCAG AA 4.5:1 |
| `orphaned-tokens` | warning | Color tokens never referenced by components |
| `missing-typography` | warning | Colors without typography tokens |
| `section-order` | warning | Markdown sections out of canonical order |
| `unknown-key` | warning | Likely typo in top-level YAML key |
| `token-summary` | info | Token counts |
| `missing-sections` | info | Optional sections absent |
