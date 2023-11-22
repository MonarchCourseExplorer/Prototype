Title: CS 263: Syllabus (@semester@)
Author: @instructor@
Date: @docModDate@
TOC: yes


# Basic Course Information

%if _kennedy

The course schedule and website are located at
<https://www.cs.odu.edu/~tkennedy/cs263/latest>.

%endif

## Catalog Description

Laboratory work required. An introduction to the Python programming language
for students who are familiar with programming in C++ or Java. Topics include
basic language syntax, data structures, control flow, classes, inheritance, and
basic elements of the Python standard library. Not open to students with credit
for CS 253.

## Overall Description

This course is intended as an introduction to Python for students already
familiar another language (with an emphasis on C++ or Java). The overall focus
of this course is to prepare to teach you how to apply your existing knowledge
to write *Pythonic* code.


## Prerequisites

The prerequisites for this course are:

* CS 250, Problem Solving and
   Programming II in C++, or CS 251, Programming and Problem Solving in Java

*  [CS 252](https://www.cs.odu.edu/~zeil/cs252/latest/), Introduction to Unix for Programmers


### General Programming Knowledge

Students should be familiar with certain basic programming techniques that are
largely independent of any specific programming language:

  * using editors, compilers and other basic software development tools.
  * basic software design (i.e., stepwise refinement and top-down design)
  * software testing, including the use of scaffolding code (stubs and
    drivers), selection of test cases for black-box testing, and head to head
    testing.


### C++ & Java Knowledge

I will assume that you are familiar with the basics of C++ and/or Java. This
includes:

  * the various C++/Java statements and control-flow constructs,
  * the built-in data types,
  * the use of arrays, pointers, pointers to arrays, and linked lists,
  * the use and writing of functions, and
  * the basic use of structs and/or classes for implementing
       abstract data types.


### Python 3 & Rust Knowledge

Prior knowledge of [Python](https://docs.python.org/3/) and
[Rust](https://www.rust-lang.org/learn) is neither expected nor assumed.


### General Computer Literacy

You will be studying techniques in this course for preparing
professional-quality software documentation. The key embedded word in "software
documentation" is "document". Students taking this course should be able to use
word processors and other common tools to produce good quality documents,
including mixing text and graphics in a natural and professional manner.


## Instructor

%if _kennedy

| **Instructor**    | **Office**   | **Phone #**  | **Email**           | **Home Page & Office Hours**        |
| :------------     | :---------   | :---------   | :-----------        | :---------------------------------- |
| Thomas J. Kennedy | Dragas 1100D | 757.683.7725 | tkennedy@cs.odu.edu | <http://www.cs.odu.edu/~tkennedy>   |

%endif

Important: All email related to this course should have the phrase **CS 263**
somewhere in the subject line.  This flags your message in my mailbox for
faster attention.

%if _kennedy

\bSidebar

This is my general email policy. However, this is usually $O(n)$ (i.e., an
upper bound).

\eSidebar

I try to respond to all (properly marked) messages
  
  - before I leave campus each day (Monday through Friday)
  - within 48 on weekends & holidays.

**Any delays in replying to email will be noted in a Canvas Announcement.**

%endif


### Office Hours

%if _kennedy

My general office hours are available at <https://www.cs.odu.edu/~tkennedy/>.
Instructions for scheduling a formal appointment are listed on the same page
and [here](doc:officeHours).  My office hours consist of web-conference (Zoom)
appointments.

General questions about course content and reports of website problems should
normally be asked in the Forums on Canvas or via email.

%endif

Questions about grades, how to solve assignments and other graded activities
must be send to @email@.

For more discussion on course communications, please refer to the
[Communications policy](doc:communications).

%if _kennedy

%endif


# Required Materials

## Textbooks

There is no required textbook.

## Supplemental Materials

All supplemental resources and materials will be available in Canvas

## Technology Requirements

### Computer Accounts

Students will need an account on the CS Dept. Unix network to participate in
this class. This account is unrelated to any University-wide account you may
have from the ODU's Information Technology Services (ITS).

If you have had a CS Unix account in the recent past, you should find it still
active with your login name, password, and files unchanged. If you have had an
account and it has not been restored, contact the CS Dept systems staff at
root@cs.odu.edu requesting that it be restored.

If you do not yet have such an account, go to the [CS Dept. home
page](https://www.cs.odu.edu/) and look for "Account Creation" under "Online
Services". All students in this course are responsible for making sure they
have a working CS Unix account **prior to** the first assignment.

### Compilers

The "official" environment in which students' programming assignments will be
evaluated is defined by our Dept. Linux servers. It is the student's
responsibility to be sure that their code compiles and executes using the
compilers and run-time environment provided there. As of this writing, the
compiler versions used are

  -  C++: g++ 9.3.0
  -  Java: 11.0.12
  -  Python: 3.11


## Objectives (Early Draft)

The overall goal of this course is to *prepare students to write, design,
refactor, and test code in Python at a level comparable to a student completing
a 200-level programming course in C++ (CS250), Java (CS 251), or Python (CS
253) in preperation for 300-level and 400-level coursework.*

A student who successfully completes this course will be able to (in Python):

  1. Run a program consisting of a single file and containing a `main`
     function.
  2. Run a program consisting of multiple modules and containing a `main`
     function.
  3. Organize code into multiple modules.
  4. Write tests for a module.
  5. Apply the basics of test-driven development through PyTest and/or
     `unittest`.
  6. Make use of the various loops (for and while)
  7. Make use of the conditional blocks (i.e., if, if-else, and if-else-if-else).
  8. Test and write functions.
  9. Design ADTs in accordance with the Class Checklist.
  10. Discuss when polymorphism is appropriate.
  12. Discuss when it is appropriate to utilize dataclasses, classes, and enums.
  13. Write code that utilized dunder functions.
  14. Refactor code to follow best practices (e.g., PEP 8 and PEP 20).
  15. Apply code linting tools (e.g., pylint and black) to write idiomatic
      (Pythonic) code.
  15. Discuss the various NumPy `np.array` mechanics (e.g., broadcasting).


  


T.B.W.


# Course Schedule

The course schedule is available in Canvas under *Modules* and *Calendar*. An
alternate schedule/outline can be accessed at
<https://www.cs.odu.edu/~tkennedy/cs263/latest/Directory/outline/index.html>.


# Grading

Your Final Course Grade will be computed using the following weights:

| ------------- | --- |
| Assignments   | 60% |
| Exam I        | 10% |
| Exam II       | 10% |
| Final Exam    | 20% |

The Final Exam is cumulative. If your Final Exam score (percentage) is higher
than:

  - Exam 1... your Final Exam grade will replace your Exam 1 grade.
  - Exam 2... your Final Exam grade will replace your Exam 2 grade.
  - Exam 1 & Exam 2... your Final Exam grade will replace both your Exam 1
    grade and Exam 2 grade.

\bExample{Grading Schema}

| Percent     | Letter Grade | 4pt Value |
| :---        | :-----:      | :------   |
| $\geq 85$   | A            | 4.0       |
| $\geq 80.5$ | A-           | 3.7       |
| $\geq 74.5$ | B+           | 3.3       |
| $\geq 70$   | B            | 3.0       |
| $\geq 60$   | B-           | 2.7       |
| $\geq 59.5$ | C+           | 2.3       |
| $\geq 55$   | C            | 2.0       |
| $\geq 50.5$ | C-           | 1.7       |
| $\geq 44.5$ | D+           | 1.3       |
| $\geq 40$   | D            | 1.0       |
| N/A         | D-           | 0.7       |
| $< 39$      | F            | 0.0       |

\eExample


## Assignments

Assignments for this course will include *programming assignments* (in Python)
which must be done on an individual basis.


### Assignment Grading

Assignments will be turned in through the CS submission system, rather than
through Canvas--more information is available [here](doc:submitting). Most
of the assignments will be graded by an automatic grader. The results will be
sent to your ODU email account. 

Unless the assignment explicitly states otherwise, you may submit a total of
three times per assignment; the instructor will take the last of the marks,
although you may request that your score be "rolled back" to an earlier one.
You may NOT submit after viewing the sample solution.


### Auto-Grader & Testing

Test driven development is a topic of particular import--not only in academia,
but in industry.

*You will be expected to make use of Blackbox Testing*. This is a topic of
particular import. Blackbox testing is covered in CS 250--a prerequisite for
this course. You will also need to make use of white-box testing and unit
testing.
 
**All tests are designed by me--the instructor.** The Auto-Grader runs tests
that I use to evaluate my solution. These tests evaluate mechanics of
import--e.g., dynamic binding and function overloading.

Be systematic in all changes to your assignment solution and modifications to
your tests. Do not haphazardly make changes to an assignment and resubmit
hoping for a better grade. Treat each submission attempt as your final
submission. Ask for guidance before each subsequent submission.


## Exams

Exams will be administered online via Canvas.

## Incomplete Grades 

A grade of "I" indicates assigned work yet to be completed in a given course,
or absence from the final examination, and is assigned only upon instructor
approval of a student request. The "I" grade may be awarded only in exceptional
circumstances beyond the student's control. The "I" grade becomes an "F" if not
removed by the day grades are due for following term based on specific
criteria: [Incomplete, Withdraws and Z
grades.](https://ww1.odu.edu/academics/academic-records/grades/incompletes-withdraws-zgrades).


# Expectations

## Assignment Expectations

**It is my expectation that you have completed approximately 70% of each
assignment once half the allotted time has passed.** For a two week assignment
this would be one week. This will allow you sufficient time to address any
issues, refine your testing process, and discuss your solution with me during
my office hours.

I expect every student to discuss each assignment with me at least once.


# Course Policies

## Due Dates and Late Submissions

Late papers, assignments, projects, and make-up exams will not normally be
permitted.

Exceptions will be made only in situations of unusual and
unforeseeable circumstances beyond the student's control, and such
arrangements must be made prior to the due date in any situations
where the conflict is foreseeable.

"*I've fallen behind and can't catch up*", "*I'm having a busier
semester than I expected*", or "*I registered for too many classes
this semester*" are \emph{not} grounds for an extension.

Extensions to due dates will not be granted simply to allow
"porting" from one system to another. "*But I had it working on my home
PC!*" is not an acceptable excuse.


## Academic Honesty

Everything turned in for grading in this course must be your own work. If an
assignment is **explicitly** described as a team assignment, it must be the
work of the team members only.

The instructor reserves the right to question a student orally or in writing
and to use his evaluation of the student's understanding of the assignment and
of the submitted solution as evidence of cheating.  Violations will be reported
to the Office of Student Conduct & Academic Integrity for consideration for
possible punitive action.

Students who contribute to violations by sharing their code/designs with others
may be subject to the same penalties.

* Students are expected to use standard Unix protection mechanisms (`chmod`) to
  keep their assignments from being read by their classmates. Failure to do so
will result in grade penalties, at the very least.

This policy is \emph{not} intended to prevent students from providing
legitimate assistance to one another. Students are encouraged to seek/provide
one another aid in learning to use the operating system, in issues pertaining
to the programming language, or to general issues relating to the course
subject matter.

> Students should avoid, however, explicit discussion of approaches to solving
> a particular programming assignment, and under no circumstances should
> students show one another their code for an ongoing assignment, nor discuss
> such code in detail.


**Use of Online Resources**

You may **not** post details of course assignments, projects, or tests at
online Forums, Bulletin Boards, Homework sites, etc., soliciting help.

You may use information that you have not solicited but have located, subject
to the following restrictions:

* Just as when writing a paper, if you use someone else's
  ideas, you must cite your sources appropriately. Within code, such
  citations appear in comments.

    Example:

        /*...*/
        double x = 23.0;
        double xsqrt = sqrt(x);
        // Search algorithm based upon code by S Zeil at
        // https://www.cs.odu.edu/~zeil/cs361/latest/Public/functionAnalysis/index.html#orderedsequentialsearch
        int loc = 0;
        while (loc < arraySize && numbers[loc] < xsqrt)
        /*...*/

* Just as when writing a paper, if you use someone else's
  words (code), you must cite your sources appropriately **and** mark
  the quoted text. Within code, such
  citations appear in comments.

    Example:

        /*...*/
        double x = 23.0;
        double xsqrt = sqrt(x);

        // Begin quoted code from  S Zeil at
        // https://www.cs.odu.edu/~zeil/cs361/latest/Public/functionAnalysis/index.html#orderedsequentialsearch
        int loc = 0;
        while (loc < listLength && list[loc] < searchItem)
        {
            ++loc;
        }
        // End quoted code

        /*...*/

* Failure to appropriately cite any such "found code" will be taken as
    evidence of plagiarism.

* The overall principle stated in the first sentence of this section remains in
  effect.  "Everything turned in for grading in this course must be your own
  work."   If the bulk of your assignment, project, test answer, etc., are
  copied, even with appropriate citation, to the degree that, in the judgment of
  the instructor, you have not demonstrated your own knowledge of the course
  material, you will receive a zero for that submission.


# University Policies

## Code of Student Conduct and Academic Integrity  

The Office of Student Conduct & Academic Integrity (OSCAI) oversees the
administration of the student conduct system, as outlined in the Code of
Student Conduct. Old Dominion University is committed to fostering an
environment that is: safe and secure, inclusive, and conducive to academic
integrity, student engagement, and student success. The University expects
students and student organizations/groups to uphold and abide by standards
included in the Code of Student Conduct. These standards are embodied within a
set of core values that include personal and academic integrity, fairness,
respect, community, and responsibility. 

## Honor Pledge 

By attending Old Dominion University, you have accepted the responsibility to
abide by the Honor Pledge:  

> I pledge to support the Honor System of Old Dominion University. I will
> refrain from any form of academic dishonesty or deception, such as cheating
> or plagiarism. I am aware that as a member of the academic community it is my
> responsibility to turn in all suspected violations of the Honor Code. I will
> report to a hearing if summoned. 

## Discrimination Policy 

The purpose of this policy is to establish uniform guidelines in order to
promote a work and education environment that is free from harassment and
discrimination, as defined below, and to affirm the University's commitment to
foster an environment that emphasizes the dignity and worth of every member of
the Old Dominion University community. The [Discrimination
Policy](https://ww1.odu.edu/about/policiesandprocedures/university/1000/1005)
details the process to address complaints or reports of retaliation, as defined
by this policy. 

## Diversity and Inclusion  

The [Division of Student Engagement & Enrollment
Services](https://ww1.odu.edu/sees) values the uniqueness of our Monarch
community. The word "engagement" reflects our commitment to embrace the
differences in our cultural backgrounds, perceptions, beliefs, traditions,
world views, socio-economic status, cognitive and physical abilities. 

We will strive to serve as the pre-eminent model for engaging every student to
achieve their own success. Our core values are fueled by our responsibility and
actions toward community development and engagement, cultural competence and
understanding, physical and mental wellness and inclusion for every member of
ODU. We will embrace our greatest strength - the diverse composition of our
student body and workforce. For more information regarding diversity and
inclusion, please visit the Office of [Intercultural Relations.](https://www.odu.edu/oir) 


## University Email Policy 

With the increasing reliance and acceptance of electronic communication, email
is considered an official means for University communication. Old Dominion
University provides each student an email account for the purposes of teaching
and learning, research, administration, and service. It is the responsibility
of every eligible student to activate MIDAS, the Monarch Identification and
Authorization System, in order to obtain email access. It is important that all
students are aware of the expectations associated with email use as outlined in
the [Student Email
Standard.](https://ww1.odu.edu/about/policiesandprocedures/computing/standards/11/02)
The email account provided by the University is
considered to be an official point of contact for correspondence. Students are
expected to check their official e-mail account on a frequent and consistent
basis in order to stay current with University communications. Mail sent to the
ODU email address may include notification of University-related actions,
including academic, financial, and disciplinary actions. For more information
about student email, please visit [Student Computing.](http://www.odu.edu/academics/student-computing)  

## Withdrawal 

A syllabus constitutes an agreement between the student and the course
instructor about course requirements. Participation in this course indicates
your acceptance of its teaching focus, requirements, and policies. Please
review the syllabus and the course requirements as soon as possible. If you
believe that the nature of this course does not meet your interests, needs or
expectations, if you are not prepared for the amount of work involved – or if
you anticipate assignment deadlines or abiding by the course policies will
constitute an unacceptable hardship for you – you should drop the course by the
drop/add deadline, which is listed in the [ODU Schedule of Classes](https://www.odu.edu/academics/calendar). For more
information, please visit the [Office of the University Registrar.](https://www.odu.edu/registrar)

## Privacy of Student Information 

Old Dominion University recognizes its duty to uphold the public's trust and
confidence, not only in following laws and regulations, but in following high
standards of ethical behavior. Members of the Old Dominion University community
are responsible for maintaining the highest ethical standards and principles of
integrity. The [Code of
Ethics](https://ww1.odu.edu/content/odu/about/policiesandprocedures/university/1000/1002.html)
is a set of values-based statements that demonstrate the University's
commitment to this goal. The [Privacy of
Student](https://www.odu.edu/about/policiesandprocedures/studentinfo)
Information details Family Educational Rights & Privacy Act (FERPA), along with
other information regarding privacy. 


## Educational Accessibility

Old Dominion University is committed to ensuring equal access to all qualified
students with disabilities in accordance with the Americans with Disabilities
Act. The Office of Educational Accessibility (OEA) is the campus office that
works with students who have disabilities to provide and/or arrange reasonable
accommodations.

* If you experience a disability which will impact your ability to access any
  aspect of my class, please present me with an accommodation letter from OEA
  so that we can work together to ensure that appropriate accommodations are
  available to you.

* If you feel that you will experience barriers to your ability to learn and/or
  testing in my class but do not have an accommodation letter, please consider
  scheduling an appointment with OEA to determine if academic accommodations are
  necessary.

The Office of Educational Accessibility is located at 1021 Student Success
Center and their phone number is (757) 683-4655. Additional information is
available at the OEA website
[http://www.odu.edu/educationalaccessibility/](http://www.odu.edu/educationalaccessibility/)

