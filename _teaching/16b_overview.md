---
layout: page
title: EECS 16B&#58; Designing Information Devices and Systems II
permalink: /teaching/eecs16b/
card_title: EECS 16B
description: Lab curriculum, the Arduino migration, and automation for grading and section sign-ups.
nav: true
horizontal: false
---

[EECS 16B (*Designing Information Devices and Systems II*)](https://inst.eecs.berkeley.edu/~ee16b/sp23/) is Berkeley EECS's second introductory undergraduate course teaching students a foundation in linear algebra, circuits, and a survey of Electrical Engineering topics.

I have always been very straightforward about this: like many students, I hated this class. Yet I taught it for 5 semesters, and even served as head TA for it.

I was primarily motivated to teach this class because I saw many places where it could be improved. My goal was to reduce or eliminate sources of student frustration.

Alongside running sections, holding office hours, and proctoring exams, I worked on longer-term improvements to the curriculum and course logistics:

<!-- pages/projects.md -->
<div class="projects">
{%- if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized projects -->
  {%- for category in page.display_categories %}
  <h2 class="font-weight-medium mt-4">{{ category }}</h2>
  {%- assign categorized_projects = site.teaching_eecs16b | where: "category", category -%}
  {%- assign sorted_projects = categorized_projects | sort: "importance" %}
  <!-- Generate cards for each project -->
  {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {%- for project in sorted_projects -%}
      {% include projects_horizontal.liquid %}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="row row-cols-1 row-cols-md-3">
    {%- for project in sorted_projects -%}
      {% include projects.liquid %}
    {%- endfor %}
  </div>
  {%- endif -%}
  {% endfor %}

{%- else -%}
<!-- Display projects without categories -->
  {%- assign sorted_projects = site.teaching_eecs16b | sort: "importance" -%}
  <!-- Generate cards for each project -->
  {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {%- for project in sorted_projects -%}
      {% include projects_horizontal.liquid %}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="row row-cols-1 row-cols-md-3">
    {%- for project in sorted_projects -%}
      {% include projects.liquid %}
    {%- endfor %}
  </div>
  {%- endif -%}
{%- endif -%}
</div>

Other curriculum improvements included:
- Rewrote the lab syllabus.
- Rewrote lab reports to focus on understanding the experiments rather than miscellaneous trivia.
- Improved clarity and usability across the lab documentation.
- Added sections on PID control to Lab 7, Part 2.
- Optimized Lab 8 memory usage to support longer recordings for word classification.
