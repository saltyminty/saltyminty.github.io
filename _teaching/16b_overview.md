---
layout: page
title: EECS 16B&#58; Designing Information Devices and Systems II
permalink: /teaching/eecs16b/
description: Overview
nav: true
horizontal: false
---

[EECS 16B (*Designing Information Devices and Systems II*)](https://inst.eecs.berkeley.edu/~ee16b/sp23/) is Berkeley EECS's second introductory undergraduate course teaching students a foundation in linear algebra, circuits, and a survey of Electrical Engineering topics.

I have always been very straightforward about this: like many students, I hated this class. Yet I taught it for 5 semesters, and even served as head TA for it.

I was primarily motivated to teach this class because I saw my places where it could be improved. My goal has always been to reduce or eliminate area of student frustration.

Aside from standard staff duties of running sections, office hours, and proctoring (there's not much interesting content to talk about there anyway), below are some of the long-term aspects of the course I've worked on:

<!-- pages/projects.md -->
<div class="projects">
{%- if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized projects -->
  {%- for category in page.display_categories %}
  <h2 class="category">{{ category }}</h2>
  {%- assign categorized_projects = site.teaching_eecs16b | where: "category", category -%}
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
  {%- assign sorted_projects = site.teaching_eecs16b | sort: "importance" -%}
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

Some other aspects of course content I've worked on which don't warrant their own page:
- Rewrote lab syllabus
- Rewrote lab reports to focus more on lab understanding rather than miscellaneous trivia
- general quality of life changes to all lab docs
- added new components to lab 7 part 2 to add new sections on PID control
- optimized lab 8 memory usage to allow for longer word recording/classification durations