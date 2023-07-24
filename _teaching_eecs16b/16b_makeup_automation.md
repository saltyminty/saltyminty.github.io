---
layout: page
title: Makeup Section Automation
description: Automating student signup for makeup lab sections
# img: assets/img/3.jpg
importance: 3
category: EECS 16B&#58; Designing Information Devices and Systems II
# giscus_comments: true
---

When students don't finish the assigned lab during their lab section, they can sign up for a "makeup" lab section to complete the lab. However, because space was limited, students would sign up for a makeup lab section by filling out a google form, and then a TA would manually schedule students into makeup sections. This was a time-consuming process, and students would often have to wait a day or two before they could attend the makeup lab section.

In Spring 2022 and Fall 2022, I automated the makeup lab section process. There was an existing section signup system created by CS 61A that was typically used for section signups at the beginning of the semester. I modified this system to allow students to sign up for makeup lab sections by writing a script to automatically create or remove makeup section sign-up slots throughout the week based on the number of seats available in each section. This script would also automatically perform validation like preventing students from signing up for multiple sections or signing up for makeup sections before their lab section.

This system allowed students to sign up for makeup sections much more easily without having to wait for manual TA processing.