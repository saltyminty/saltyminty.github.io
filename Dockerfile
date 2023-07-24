FROM ruby:3.3.5-slim
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends build-essential git imagemagick nodejs zlib1g-dev && rm -rf /var/lib/apt/lists/*
WORKDIR /srv/jekyll
COPY Gemfile Gemfile.lock ./
RUN bundle install --jobs 4 --retry 3
ENV EXECJS_RUNTIME=Node
EXPOSE 8080 35729
CMD ["/srv/jekyll/bin/entry_point.sh"]
