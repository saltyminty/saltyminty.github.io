# Portfolio maintenance

Read `README.md` and `_config.yml` before editing. This is a personal al-folio v1.2 site. The parent hub's privacy and commit rules apply.

- Maintain personal content in the page, collection, data, and asset folders. Preserve real routes and original media.
- Use the pinned theme/plugin gems for runtime behavior. Keep `Gemfile` and `_config.yml` plugin lists aligned.
- Prefer native theme support; add local layout/include/style overrides only for a specific unmet need, then run the override audit.
- `_site/`, `assets/libs/`, caches, and `vendor/` are generated. Do not edit them as source.
- The website CV is separate from the resume bank. Do not add or change biographical claims without source evidence and task authorization.
- Run both theme upgrade audits, a production build, and `python3 bin/check_site.py _site` after changes affecting rendering. Review affected pages at desktop and mobile widths.
- Do not stage, commit, push, or publish unless explicitly requested. Preserve the independent repository's history and remotes.
