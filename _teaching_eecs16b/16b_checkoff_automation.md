---
layout: page
title: Lab Autograder
description: Automating compiling and uploading lab grades
# img: assets/img/3.jpg
importance: 2
category: EECS 16B&#58; Designing Information Devices and Systems II
# giscus_comments: true
---

EECS 16B Labs use a google form for students to request help or get "checked off" for completing each lab. The corrresponding google sheet is then manually updated by a TA to mark the student as checked off for the lab. While this process itself wasn't to much of an hassle, it left students unable to verify their grades - lab grades would need to be manually compiled, formatted, and then uploaded to Gradescope and/or the status checker, which was time-consuming, error-prone, and only occurred twice a semester.

In Spring 2022 and Fall 2022, co-head TA Shrey Aeron and I worked to automate this process, writing a new lab autograder using the Google Sheets API and Gradescope API to automatically parse the checkoff sheet, compile and calculate each student's grade, and directly upload the grades to Gradescope for students to see. We hooked this up to a cronjob that would rerun the autograder multiple times a day (typically at the end of each lab section), allowing students to immediately see their grades. This both allowed students to immediately file any discrepancies, and allowed us to more easily track student progress with labs.

This lab autograder would later also be used in other EECS courses, such as EECS 106A.