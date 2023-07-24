---
layout: page
title: Self-Grade Automation
description: Automating the creation and grading of "Self-Grade" assignments
# img: assets/img/3.jpg
importance: 4
category: EECS 16B&#58; Designing Information Devices and Systems II
# giscus_comments: true
---

Like many other large courses, EECS 16B implemented a self-grade system for homeworks to reduce staff workload - students would self-grade their own homeworks, assigning themselves a grade of 0, 2, 5, 8, or 10 points for each problem. Staff would spot check a portion of the homeworks to ensure that students were grading correctly/accurately.

Previously, students filled out a [special self-grade form](https://inst.eecs.berkeley.edu/~ee16b/sp22/self-grade-00.html) on the website, which would then generate out a raw text file that the student would them upload to Gradescope. This was a very unnecessarily long and complicated process, and students would often make mistakes in the process of uploading their self-grades. We would have liked to have students directly submit their self-grades on Gradescope via multiple choice questions, but unfortunately Gradescope doesn't support the automatic grading of multiple choice questions where each answer selection is worth a different amount of points.

Over Fall 2022, I used the Gradescope API to write a script that would automatically grade a self-grade Gradescope assignment, thus allowing self-grades to be handled directly within Gradescope. Additionally, we automated the generation of each homework's self-grade assignment, reducing the amount of manual work required to create each assignment.

While the overall impact of this change was relatively small, it was a great improvement to the student experience and quality of life.