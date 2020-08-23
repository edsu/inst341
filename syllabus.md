# INST341 - Introduction to Digital Curation

**Instructor:** Ed Summers  edsu@umd.edu  
**Office Hours:** Thursday 2-4 and by appointment on [Zoom](https://umd.zoom.us/my/esummers)

## Catalog Description

Explores various dimensions and contexts for digital curation, which includes
all activities involving the management, representation and preservation of both
born-digital and digitized information. Focuses on opportunities, challenges and
demands of every-increasing digital data and networked information
infrastructure.

## Course Description

Our daily lives are suffused with flows of data. From the apps on our phones, to
the web platforms we use, to the devices that track our movements in the world
and the algorithms that analyze and classify us. What does this data look like?
How is it collected and described? Who can access it? How is it persisted,
preserved, and purged. How can we resist it? In this class we will explore these
questions using the theories and practices of *digital curation*. By the end
of the semester you will be able to analyze and document these data flows using
principles drawn from archival studies. We will learn the practice of digital
curation by using open source technologies and the Python programming language.

## Learning Outcomes

At the end of this course you will be able to:

1. Recognize digital curation in your daily life and future career.
2. Use the Python programming language to perform digital curation tasks.
3. Critically examine the social and political aspects of digital curation.

## How We'll Work

The semester is split into 8 different two-week modules. Each module focuses on
some aspect of digital curation. In the first week of each module we will read
and discuss an aspect of digital curation. In the second week of each module we
will exercise some of the ideas in a Jupyter notebook environment.

Here is my suggested general strategy for working on assignments:

1. Start early – don’t wait. That will give you time to work through the
   problems and get help as needed.
2. When you run into a problem, spend 5-10 minutes trying to solve it on your
   own.
3. Then take a break. Sometimes this will allow you to come back and see
   something you missed. Letting your subconscious work on it for a while
   (unsupervised, so to speak) will often lead to useful ideas.
4. If you’ve spent 20-30 minutes and still are stuck, post your question on
   ELMS. We are here to help each other, so don’t beat your head against a brick
   wall—ask for help! When you post, provide as much information as you can.
   Often it helps to post a screenshot with the problem.
5. I will respond as soon as I am able, usually within a day.
6. If you see a question on the discussion board that you can answer, or if you
   have an idea, please respond. Don’t wait for me. You will be helping your
   colleagues.

## Technology Requirements

To complete the exercises in this class you will need a computer to access the
Jupyter notebook environment at https://colab.research.google.com If you prefer
you can use a Jupyter notebook environment on your own computer. But it will be
your responsibility to ensure you are running the correct version of Python (v3)
and Jupyter, and are able to install third party Python modules with
[pip](https://pip.pypa.io/en/stable/) like we will be doing in Colab.

## Grading

Your final grade for the course is computed as the sum of your scores on the
individual elements below converted to a letter grade:

|        |        |        |       |        |       |        |       |        |        |
|--------|--------|--------|-------|--------|-------|--------|-------|--------|--------|
| **A+** | 97-100 | **B+** | 87-89 | **C+** | 77-79 | **D+** | 67-69 |        |        |
| **A**  | 93-96  | **B**  | 83-86 | **C**  | 73-76 | **D**  | 63-67 | **F**  | 0-59   |
| **A-** | 90-92  | **B-** | 80-82 | **C-** | 70-73 | **D-** | 60-63 |        |        |

Final grades will be computed based on the following components:

|                        |            |
|------------------------| ---------: |
| Exercises/Quizzes (10) |  20 points |
| Homework (5)           |  25 points |
| Midterms (2)           |  20 points |
| Reflections (3)        |  10 points |
| Final Project          |  15 points |
| Participation          |  10 points |
| TOTAL                  | 100 points |

## Academic Integrity



## Reading Materials

All reading materials will be posted to ELMS. We will be reading selections from
a couple books which, which you can order print copies of from your favorite
book seller...you know, if you prefer reading real books (I do!). The *Data
Feminism* book is a beautiful produced coffee table style book and well worth
the investment if you have the money.

* Owens, T. (2018). The Theory and Craft of Digital Preservation. Johns Hopkins
University Press.
* D’Ignazio, C. and Klein, L. F. (2020). [Data Feminism](https://data-feminism.mitpress.mit.edu/). MIT Press.

## Modules

The semester is designed to help you build competency with digital curation
concepts while applying them in actual digital curation exercises. These modules
build on foundational concepts of computation that you learned in INST126 as
well as theories about the organization of information in INST201 and INST311.
In addition to gaining fluency with digital curation practice at the end of the
semester you will have designed and developed your own digital curation project
that you can add to your portfolio of work.

### 1. What is Digital Curation? (August 31 - September 11)

Learning outcomes:
* Recognize digital curation as an inherently political project.
* Use Jupyter notebooks and the pathlib module to interact with the file system.

Readings:
* Caswell, Michelle. [Whose Digital Preservation?](https://www.youtube.com/watch?v=atX14DDvKbw). Video presentation from iPRES 2019.
* Owens, T. (2018), Chapter 2, Understanding Digital Objects.

Discussion prompts:
* What is a digital object? What does Owens think are the characteristics of a digital object?
* What is archival appraisal? What does Caswell think is wrong with it?
* What is the mystery file format?

Notebook Exercise
* File and directory navigation
* File sizes

### 2. File Formats and Standards (September 14 - September 25)

Learning outcomes:
* Describe the purpose of standards and their significance for digital curation.
* Use Python to identify and migrate files.

Reading:
* Russell and Vinsel (2019) The Joy of Standards.
* Owens (2018), Chapter 6, Managing Copies and Formats.

Discussion:
* Discover a file format and discuss 1) who created it 2) when was it created by? 3)
  who did the creators work for? 4) what applications use it today?

Notebook exercises:
* Identify the formats of files using fido.
* Determine what applications can be used to open files.

### 3. Internal Metadata (September 28 - October 9)

Learning Outcomes:
* Extract embedded metadata from media files.
* Examine how applications use and modify internal metadata.

Reading:
* Computer Files are Going Extinct: https://onezero.medium.com/the-death-of-the-computer-file-doc-43cb028c0506
* Snowden, E. (2019). Permanent Record, Chapter 16 Tokyo.

Discussion:
* Wha

Exercises:
* Extract media metadata: exinfo, ffmpeg, id3

### 4. External Metadata & Description (October 12 - October 23)

Learning Outcomes:
* Apply bit-level preservation techniques to files.
* Persist extracted metadata as external metadata.

Readings:
* Harris, V. Stories and Names
* Data Feminism, Chapter 6, The Numbers Don't Speak for Themselves.
* #WeMissIPres

Discussion:
* Summarize iPRES presentation.

Exercises:
* Fixity generation
* Five Ws of description.
* Attend and write up a #wemissipres event

### 5. Platforms: October 26 - November 6

Learning outcomes:
* Explain how platforms transform data.
* Use version control to explore data provenance.

Readings:
* Acker, A. and Kriesberg, A. (2017). Tweets may be archived: Civic engagement, digital preservation and Obama White House social media data. Proceedings of the Association for Information Science and Technology, 54(1):1–9.

Discussion:
* What did Acker and Kriesberg discover about the Obama social media archives? 

Exercises:
* Export and examine social media archive.
* COVID data on GitHub: https://github.com/nytimes/covid-19-data ; https://github.com/nychealth/coronavirus-data

### 6. Community: November 9 - November 20

Learning outcomes:
* Evaluate the modes of participation in online communities.

Readings:
* Elliot Higgins. [Bellingcat and Beyond](https://www.youtube.com/watch?v=kZAb7CVGmXM&feature=youtu.be). iPRES 2020.
* [The FAIR Principles](https://www.go-fair.org/fair-principles/).

Disussion:
* 

Exercise:
* [Write the Docs](https://www.writethedocs.org/)
* Digital Asset Management Planning tool.

### 7. Thanksgiving Break: November 23 - November 27

### 8. Infrastructure: November 30 - December 11

Learing outcomes:
* Document how data is produced and maintained.
* Examine the types of data infrastructures in our lived environment.

Reading:
* D'Ignazio and Klein (2020). Chapter 7, Show Your Work. pp 172-201.
* Burrington (2018). [Surveillance and the City](https://www.youtube.com/watch?v=rPquYfE2JOc)

Discussion:
* 

Exercise:
* Photograph data infrastructure in your town or city.
* Explore terpfootprints environmental data.

### 9. Project Wrapup: December 14 - December 22

## Academic Integrity
