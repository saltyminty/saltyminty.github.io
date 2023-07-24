---
layout: page
title: Photography
permalink: /photo/
description: Photography and Video. This section is currently under construction.
nav: true
nav_order: 5
display_categories: [Landscape, People, Animals]
# display_categories: [HKN, Wushu, Personal, Idk]
horizontal: false
---

I do photography and videography for various events and organizations. I shoot on:
* Canon EOS R
- RF 24-240mm f/4-6.3 IS USM
- RF 50mm f/1.8 STM
- RF 16mm f/2.8 STM
<!-- - MSM  -->

<div class="text-left">
  <img src="/assets/img/photography/IMG_9402.JPG" class="mx-auto d-block img-fluid rounded z-depth-0.5" alt="Left Image" style="width: 50%;">
</div>
<div class="caption">
  That's me! Aside from personal usage and volunteering, I've done photography for HKN (EECS honor society), Cal Wushu, and FeiTian Dance.
</div>


<!-- pages/projects.md -->
<div class="projects">
{%- if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized projects -->
  {%- for category in page.display_categories %}
  <h2 class="category">{{ category }}</h2>
  {%- assign categorized_projects = site.photography | where: "category", category -%}
  {%- assign sorted_projects = categorized_projects | sort: "importance" %}
  <!-- Generate cards for each project -->
  {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-2">
    {%- for project in sorted_projects -%}
      {% include projects_horizontal.html %}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="grid">
    {%- for project in sorted_projects -%}
      {% include projects.html %}
    {%- endfor %}
  </div>
  {%- endif -%}
  {% endfor %}

{%- else -%}
<!-- Display projects without categories -->
  {%- assign sorted_projects = site.photography | sort: "importance" -%}
  <!-- Generate cards for each project -->
  {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-2">
    {%- for project in sorted_projects -%}
      {% include projects_horizontal.html %}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="grid">
    {%- for project in sorted_projects -%}
      {% include projects.html %}
    {%- endfor %}
  </div>
  {%- endif -%}
{%- endif -%}
</div>

<br><br>
Additionally, some videos I've worked on:
- Every semester, HKN produces a CM (Candidate Meeting) Video, an informal music/dance video to introduce the club to newly invited candidates.
  - [Spring 2024 CM Video](https://youtu.be/8D25xfglmWc?si=jFwJ7R6BFgQnhKFn)
  - [Spring 2022 CM Video](https://youtu.be/hIZF-3YH6Is?si=ejSHUdzVUsmZlibT)
- At the end of every semester, HKN produces a Banquet Video to showcase the club's semester, events, and members.
  - [Spring 2022 Banquet Video](https://youtu.be/x9nWwW2Gmio?si=_dk0cU2XoSpBf9yH)
  - [Spring 2024 Banquet Video](https://youtu.be/VCjesyACUns?si=fsIp6uMxwAcX55nT)
- [EECS 16B Lab Video](https://youtu.be/tnO_SFtI5A8)