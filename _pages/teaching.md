---
layout: page
title: Teaching
permalink: /teaching/
description: Collection of materials/projects for courses I've taught. This section is currently under construction.
nav: true
nav_order: 4
# display_categories: [CS 184&#58; Computer Graphics,
#   EECS 106A&#58; Introduction to Robotics,
#   EECS 16B&#58; Designing Information Devices and Systems II]
horizontal: false
---

While in Berkeley, I've taught the following courses:
- CS 184: Computer Graphics\
*Spring 2024*
- EECS 106A: Introduction to Robotics\
*Fall 2023*
- EECS 16B: Designing Information Devices and Systems II\
*Fall 2021, Spring 2022,\
Summer 2022, Fall 2022, Spring 2023 (Head TA)*


<!-- pages/projects.md -->
<div class="projects">
{%- if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized projects -->
  {%- for category in page.display_categories %}
  <h2 class="category">{{ category }}</h2>
  {%- assign categorized_projects = site.teaching | where: "category", category -%}
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
  {%- assign sorted_projects = site.teaching | sort: "importance" -%}
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