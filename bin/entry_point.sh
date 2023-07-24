#!/bin/bash
set -euo pipefail
cd /srv/jekyll
bundle check || bundle install --jobs 4 --retry 3
exec bundle exec jekyll serve --watch --force_polling --host 0.0.0.0 --port 8080 --livereload --destination /tmp/_site
