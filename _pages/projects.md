---
layout: page
title: Projects
permalink: /projects/
description: A collection of class and personal projects.
nav: true
nav_order: 3
display_categories: [CS 184&#58; Computer Graphics, CS 194-26&#58; Computational Photography & Computer Vision, EECS 106A&#58; Robotics, EECS 16B&#58; Designing Information Devices and Systems II]
horizontal: false
---

<!-- pages/projects.md -->
<div class="projects">
{%- if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized projects -->
  {%- for category in page.display_categories %}
  <h2 class="font-weight-medium mt-4">{{ category }}</h2>
  {%- assign categorized_projects = site.projects | where: "category", category -%}
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
      {% include portfolio_card.liquid %}
    {%- endfor %}
  </div>
  {%- endif -%}
  {% endfor %}

{%- else -%}
<!-- Display projects without categories -->
  {%- assign sorted_projects = site.projects | sort: "importance" -%}
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
      {% include portfolio_card.liquid %}
    {%- endfor %}
  </div>
  {%- endif -%}
{%- endif -%}
</div>
