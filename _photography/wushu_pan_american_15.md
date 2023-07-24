---
layout: page
title: 15th Pan American Wushu Championships
permalink: /photography/15th-pan-american-wushu-championships/
description: October 12, 2026, Buenos Aires, Argentina
img: /assets/img/photography/wushu/pan-american-15/WMY_9592.jpg
importance: 1
category: Wushu
images:
  lightbox2: true
_styles: |
  .al-lightbox-caption {
    display: none;
  }
photos:
  - file: WMY_9592.jpg
    alt: An athlete in red executing a flying kick above the competition carpet.
  - file: WMY_0123.jpg
    alt: Two athletes in matching red uniforms standing together beside the competition floor.
  - file: WMY_0138.jpg
    alt: Two athletes in red crossing paths during a paired weapons routine.
  - file: WMY_0182.jpg
    alt: One athlete leaping as their partner lunges low during a paired routine.
  - file: WMY_0193.jpg
    alt: Two athletes facing each other in low stances during a paired weapons routine.
  - file: WMY_0202.jpg
    alt: Two athletes in red performing a synchronized airborne movement.
  - file: WMY_0209.jpg
    alt: Two athletes facing each other with extended weapons during a paired routine.
  - file: WMY_0244.jpg
    alt: An athlete standing with a weapon raised while their partner lies on the competition carpet.
  - file: WMY_0644.jpg
    alt: An athlete in red extending one arm from a deep low stance.
  - file: WMY_0652.jpg
    alt: An athlete in red holding a wide stance with arms extended.
  - file: WMY_0691.jpg
    alt: An athlete in white holding a low stance with one arm raised.
  - file: WMY_0752.jpg
    alt: An athlete in white extending a straight sword from a low stance.
  - file: WMY_1060.jpg
    alt: An athlete in dark teal extending a leg and an arm in a low stance.
  - file: WMY_1777.jpg
    alt: An athlete in red balancing close to the floor during a weapons routine.
  - file: WMY_1838.jpg
    alt: An athlete in red balancing upside down on one hand.
  - file: WMY_2151.jpg
    alt: An athlete in teal holding a weapon overhead.
  - file: WMY_2261.jpg
    alt: An athlete in teal seated low on the carpet with one arm extended.
  - file: WMY_2345.jpg
    alt: An athlete in bright pink standing with a long weapon and one hand raised.
  - file: WMY_2438.jpg
    alt: An athlete in bright pink extending a long weapon from a low stance.
  - file: WMY_2510.jpg
    alt: An athlete in bright pink leaning low with a long weapon extended.
  - file: WMY_2731.jpg
    alt: An athlete in lavender raising one knee while performing a sword routine.
  - file: WMY_7839.jpg
    alt: An athlete in red and yellow standing with arms raised.
  - file: WMY_8654.jpg
    alt: An athlete in red holding a sword from a deep side stance.
  - file: WMY_8850.jpg
    alt: An athlete in blue and yellow holding a low stance with a weapon.
  - file: WMY_9612.jpg
    alt: An athlete in red balancing on one leg with the other leg raised.
  - file: WMY_9664.jpg
    alt: An athlete in red reaching upward during a jump.
  - file: WMY_9685.jpg
    alt: An athlete in red holding a low stance with both arms extended.
  - file: WMY_9722.jpg
    alt: An athlete in white speaking with people beside the competition floor.
---

<div class="row row-cols-1">
  {% for photo in page.photos %}
    {% assign photo_path = 'assets/img/photography/wushu/pan-american-15/' | append: photo.file %}
    <div class="col mb-4">
      <a href="{{ photo_path | relative_url }}" data-lightbox="pan-american-wushu-15" aria-label="{{ photo.alt | escape }}">
        {% include figure.liquid path=photo_path alt=photo.alt class="img-fluid rounded z-depth-1" sizes="(min-width: 800px) 770px, 95vw" loading="lazy" %}
      </a>
    </div>
  {% endfor %}
</div>
