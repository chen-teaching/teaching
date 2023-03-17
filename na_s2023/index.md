---
title:  Numerical Analysis (Spring 2023)
keywords: [' Numerical Analysis', 'MATH-UA.0252', 'MA-UY.4424', 'NYU', 'Courant', 'Tandon']
description: Course overview for NYU Numerical Analysis Spring 2023
...


Welcome to Numerical Analysis!
Numerical analysis studies algorithms and mathematical problems in the presence of (small) errors. 
In practice, such errors are unavoidable, so it is important to understand their impacts.
Numerical analysis is one of the core fields in applied math, and this class will cover a number of key topics in numerical analysis.
Linear algebra is a prerequisite, as much of numerical analysis is based on linear algebra.
There is no prerequisite for coding.


**Instructor**: Tyler Chen  
**Email**: tyler.chen@nyu.edu  
**Class**: M,W 3:30-4:50PM; JABS 775B  
**Office Hours**: M,W 5:00-6:00PM; 370 Jay Street Floor 11


**Teaching Assistant**: Fanghe (Athena) Liu  
**Recitation**: F 2:00-3:20PM; RGSH 325  
**Office Hours**: F 3:40-4:40PM; 2 Metrotech Floor 8 


[**Syllabus**](./syllabus.html)  
[**Edstem discussion**](https://edstem.org/us/courses/34528/)  
[**Gradescope**](https://www.gradescope.com/courses/487363)  

[**Course notes (last update: Feb 13)**](https://drive.google.com/drive/folders/1KCqfpPS0vBOovHyvVdJXieG8LgY6xPdj?usp=share_link)


[**Final project details**](./project.pdf)


## Schedule

N=Course notes, GC = Greenbaum & Chartier. Numbers are chapter \#s.


<div class="schedule-container">

<div class="week weektitle">
<div class="label">**Week**</div>
<div class="topic">**Topic**</div>
<div class="reading">**Reading**</div>
<div class="hw">**Homework/Quiz**</div>
</div>


<div class="week">
<div class="label">**1.** (1/22)</div>
<div class="topic">Intro to numerical analysis</div>
<div class="reading">syllabus, GC1, GC2, N1-N4, [[ws1]](./ws1.pdf)</div>
<div class="hw">Intro Survey [[pdf]](./intro_survey.pdf) [[tex]](./intro_survey.tex) (due 1/25)</div>
</div>

<div class="week">
<div class="label">**2.** (1/29)</div>
<div class="topic">Floating point arithmetic, stability/conditioning</div>
<div class="reading">GC5, GC6, N4, N5, N6, [[ws2]](./ws2.pdf)</div>
<div class="hw">HW1 (due 2/02) [[pdf]](./hw1.pdf) [[tex]](./hw1.tex)</div>
</div>

<div class="week">
<div class="label">**3.** (2/05)</div>
<div class="topic">Rounding error analysis, Solving structured linear systems</div>
<div class="reading">GC7.2, [[ws3]](./ws3.pdf)</div>
<div class="hw">quiz 1 (2/06)</div>
</div>

<div class="week">
<div class="label">**4.** (2/12)</div>
<div class="topic">LU / PLU / Gaussian elimination</div>
<div class="reading">GC7.2, N8, [[ws4]](./ws4.pdf)</div>
<div class="hw">HW2 (due 2/16) [[pdf]](./hw2.pdf) [[tex]](./hw2.tex)</div>
</div>

<div class="week">
<div class="label">**5.** (2/19)</div>
<div class="topic">LU cont. (no class 2/20)</div>
<div class="reading">GC7.6.2, N9, [[ws5]](./ws5.pdf)</div>
<div class="hw">quiz 2 (2/22) </div>
</div>

<div class="week">
<div class="label">**6.** (2/26)</div>
<div class="topic">QR</div>
<div class="reading">N10</div>
<div class="hw">quiz 2 bonus (due 02/27) [[pdf]](./q2_bonus.pdf) [[tex]](./q2_bonus.tex); HW3 (due 3/02) [[pdf]](./hw3.pdf) [[tex]](./hw3.tex)</div>
</div>

<div class="week">
<div class="label">**7.** (3/5)</div>
<div class="topic">SVD</div>
<div class="reading">[[ws6]](./ws6.pdf)</div>
<div class="hw">quiz 3 (3/06) [[online]](https://www.gradescope.com/courses/487363/assignments/2704691)</div>
</div>

<div class="week current">
<div class="label">**--** (3/12)</div>
<div class="topic">SPRING BREAK</div>
<div class="reading">\ </div>
<div class="hw"></div>
</div>

<div class="week">
<div class="label">**8.** (3/19)</div>
<div class="topic">Norms, conditioning of linear systems, least squares</div>
<div class="reading">N11, N12</div>
<div class="hw">HW4 (due 03/23) [[pdf]](./hw4.pdf) [[tex]](./hw4.tex)</div>
</div>

<div class="week">
<div class="label">**9.** (3/26)</div>
<div class="topic">Eigenvalue/vector</div>
<div class="reading">GC7.6, GC7.4, N13</div>
<div class="hw">quiz 4 (03/27), project proposal (due 3/30)</div>
</div>

<div class="week">
<div class="label">**10.** (4/02)</div>
<div class="topic">Root finding</div>
<div class="reading">GC4</div>
<div class="hw">HW5 (due 4/06)</div>
</div>

<div class="week">
<div class="label">**11.** (4/09)</div>
<div class="topic">Orthogonal polynomials</div>
<div class="reading">\ </div>
<div class="hw">quiz 5 (due 4/10)</div>
</div>

<div class="week">
<div class="label">**12.** (4/16)</div>
<div class="topic">Polynomial approximation</div>
<div class="reading">\ </div>
<div class="hw">HW6 (due 4/20)</div>
</div>

<div class="week">
<div class="label">**13.** (4/23)</div>
<div class="topic">Numerical Integration</div>
<div class="reading">GC10</div>
<div class="hw">quiz 6 (4/24), Final Report (4/27)</div>
</div>

<div class="week">
<div class="label">**14.** (4/30)</div>
<div class="topic">Numerical Differentiation</div>
<div class="reading">GC9 </div>
<div class="hw">HW7 (due 5/04)</div>
</div>

<div class="week">
<div class="label">**15.** (5/07)</div>
<div class="topic">Review</div>
<div class="reading">\ </div>
<div class="hw">quiz 7 (5/08), Final Presentations (5/15)</div>
</div>


</div>
