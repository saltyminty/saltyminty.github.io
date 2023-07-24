# Portfolio website

Personal projects, teaching materials, photography, and CV, built with [al-folio v1.2](https://github.com/alshedivat/al-folio/releases/tag/v1.2). The theme runtime is supplied by pinned Ruby gems; this repository owns the content and site configuration.

## Local preview

Use Ruby 3.3.5, Node.js, Bundler, and ImageMagick. From this directory:

```sh
bundle config set --local path vendor/bundle
bundle install
bundle exec jekyll serve --livereload
```

Open http://127.0.0.1:4000/. The first build generates responsive WebP images; it takes longer than subsequent builds. GIF animations retain their original files. Generated output is in `_site/`.

Alternatively, with Docker running:

```sh
docker compose -f docker-local.yml up --build
```

The Docker preview is at http://127.0.0.1:8080/.

## Editing

- `_pages/`: home, CV, project index, teaching index, and photography index.
- `_projects/`, `_photography/`, `_teaching/`, `_teaching_eecs106a/`, `_teaching_eecs16b/`: collection content. Preserve existing permalinks when updating pages.
- Project cards use `date_label` for human-readable dates and `_includes/portfolio_card.liquid` for dates and concise titles. This content-specific include uses native theme styling and does not shadow a runtime include. Teaching cards use `card_title` and `description` on the course overview pages.
- `_data/cv.yml`: website CV in the theme's native RenderCV data shape. Updated on 2026-11-12 using the Full and Google resumes, with user-confirmed HKN dates, Combat Robotics ending in 2023, and completed design certification. Preserve benchmark scope and the eight-month period for the PR review count. Projects link to the portfolio; projects without portfolio pages have short CV entries.
- `assets/img/`, `assets/pdf/`: original images and documents.
- `_config.yml`: site identity, collection routes, enabled plugins, and feature settings.
- `.well-known/`: existing verification endpoint; retain it when deploying.

Use native `.liquid` includes such as `figure.liquid` and `projects.liquid`. The theme already preserves project-title capitalization. There are no local theme runtime overrides; prefer gem features before adding one. The four old sample project pages are marked `published: false`.

## Validation

```sh
bundle exec al-folio upgrade audit
bundle exec al-folio upgrade overrides audit
JEKYLL_ENV=production bundle exec jekyll build --trace
python3 bin/check_site.py _site
```

The link checker checks local page links, image sources and responsive variants, scripts, stylesheets, and CSS assets. External links and separate GitHub Pages projects require a separate online check. Review desktop/mobile layouts, navigation, search, dark mode, galleries, and the CV after theme updates.

## Deployment

The build workflow validates changes on pull requests and publishes `master` or `main` directly through GitHub Pages artifacts when pushed. It can also be started manually on those branches. In repository Settings → Pages, the publishing source is GitHub Actions. The workflow includes hidden verification files in the deployment artifact. Local edits and local previews do not publish anything.

Do not stage, commit, push, or deploy automatically. The parent hub's privacy boundary does not prevent this repository's own Git and deployment operations.

## Theme updates

Keep the theme's plugin versions in `Gemfile` and entries in `_config.yml` aligned. Update exact pins deliberately, update the lockfile, run both upgrade audits, build, and check the pages above. Do not copy old theme internals back into the site. The migration starts from upstream commit `b95d6d61a1b0663529094b1b5f4fbe8aa41f8a04`; the pre-upgrade site is retained in Git at `15725ace`.
