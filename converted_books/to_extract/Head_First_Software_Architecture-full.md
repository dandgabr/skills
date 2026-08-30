# Head First Software Architecture A Learners Guide to Architectural Thinking (Raju Gandhi, Mark Richards, Neal Ford) (z-library.sk, 1lib.sk, z-lib.sk)

> Documento convertido de PDF para Markdown para referência de skills.


<a id='p1'></a>
<!-- Página 1 -->

Software
Architecture
A Learner’s Guide to
Architectural Thinking

Raju Gandhi,
Mark Richards
& Neal Ford




```
A Brain-Friendly Guide .5”
```


<a id='p2'></a>
<!-- Página 2 -->


<a id='p3'></a>
<!-- Página 3 -->

Other related books from O’Reilly
Fundamentals of Software Architecture
Software Architecture: The Hard Parts




Other books in O’Reilly’s Head First series
Head First Android Development
Head First C#
Head First Design Patterns
Head First Git
Head First Go
Head First iPhone and iPad Development
Head First Java
Head First JavaScript Programming
Head First Learn to Code
Head First Object-Oriented Analysis and Design
Head First Programming
Head First Python
Head First Software Development
Head First Web Design

<a id='p4'></a>
<!-- Página 4 -->


<a id='p5'></a>
<!-- Página 5 -->

Head First Software Architecture
```
Wouldn’t it be dreamy if there was
a book about software architecture
that was more fun than getting a root
canal and more revealing than reams of
documentation? It’s probably just a fantasy...




Raju Gandhi
Mark Richards
Neal Ford




Beijing Boston Farnham Sebastopol Tokyo
```


<a id='p6'></a>
<!-- Página 6 -->

Head First Software Architecture
by Raju Gandhi, Mark Richards & Neal Ford


Copyright © 2024 Defmacro Software L.L.C., Mark Richards and Neal Ford. All rights reserved.
Printed in the United States of America.
Published by O’Reilly Media, Inc., 1005 Gravenstein Highway North, Sebastopol, CA 95472.
O’Reilly Media books may be purchased for educational, business, or sales promotional use. Online editions are
also available for most titles (http://oreilly.com). For more information, contact our corporate/institutional sales
department: (800) 998-9938 or corporate@oreilly.com.

Series Creators: Kathy Sierra, Bert Bates
Series Advisors: Eric Freeman, Elisabeth Robson
Acquisitions Editor: Melissa Duffield
Development Editor: Sarah Grey
Cover Designer: Susan Thompson, based on a series design by Ellie Volckhausen
Cover/Interior Illustrations: José Marzan Jr.
Production Editor: Christopher Faucher
Proofreader: Rachel Head
Indexer: nSight, Inc.
Page Viewers: Buddy and Skye (“the dogs”), Princess Zara, baby Delphine,
```
Sparks, Fauci, Linda Ruth, and Amadeus (“the cats”)


```

Printing History:

March 2024: First Edition.


The O’Reilly logo is a registered trademark of O’Reilly Media, Inc. The Head First series designations, Head First
Software Architecture, and related trade dress are trademarks of O’Reilly Media, Inc.
Many of the designations used by manufacturers and sellers to distinguish their products are claimed as trademarks.
Where those designations appear in this book, and O’Reilly Media, Inc., was aware of a trademark claim, the
designations have been printed in caps or initial caps.
While every precaution has been taken in the preparation of this book, the publisher and the authors assume no
responsibility for errors or omissions, or for damages resulting from the use of the information contained herein.
No dogs, cats, or chefs were harmed in the making of this book.



## ISBN: 978-1-098-13435-8

[LSI] [2024-03-04]

<a id='p7'></a>
<!-- Página 7 -->


## DEDICATION



```
From Mark and Neal
```

To all the conference attendees who patiently sat
```
through many drafts of this material
(2004-2024)


From Raju
To my Dad
જય શ્રી કૃષ્ણ
```


<a id='p8'></a>
<!-- Página 8 -->

the authors



Authors of Head First Software Architecture
```
Mark Richards




Raju Gandhi Neal Ford

Raju Gandhi
Raju is an architect, consultant, author, and teacher and a regularly invited speaker at conferences around the
world. He believes in keeping things simple, and his approach is always to understand and explain the “why,”
as opposed to the “how.” He lives in Columbus, Ohio, with his wonderful wife, Michelle; their sons, Mason
and Micah; their daughter, Delphine; and three furry family members, Buddy, Skye, and Princess Zara. You
can find his contact information at RajuGandhi.com.


Mark Richards
Mark is an experienced hands-on software architect and the founder of DeveloperToArchitect.com, a free
website devoted to helping developers in their journeys to becoming software architects. He has been in the
software industry since 1983 and has significant experience and expertise in application, integration, and
enterprise architecture. Mark has authored numerous technical books and videos, including Fundamentals of
Software Architecture and Software Architecture: The Hard Parts (O’Reilly), co-authored with Neal Ford. Mark also
does training and has spoken at hundreds of conferences and user groups around the world.


Neal Ford
Neal Ford is director, software architect, and meme wrangler at ThoughtWorks, a global IT consultancy with
a focus on end-to-end software development and delivery. He is also the designer and developer of many
applications, articles, and video presentations and the author and/or editor of an increasingly large number of
books, spanning a variety of subjects and technologies. His professional focus is designing and building largescale enterprise applications. He is also an internationally acclaimed speaker who has spoken at more than 300
developer conferences worldwide and has delivered more than 2,000 presentations.



```

vi

<a id='p9'></a>
<!-- Página 9 -->

```
table of contents




```

Table of Contents (the summary)
```
Intro xix
1 Software Architecture Demystified: Let’s Get Started! 1
2 Architectural Characteristics: Know Your Capabilities 41
3 The Two Laws of Software Architecture: Everything’s a Trade-Off 81
4 Logical Components: The Building Blocks 123
5 Architectural Styles: Categorization and Philosophies 167
6 Layered Architecture: Separating Concerns 185
7 Modular Monoliths: Driven by the Domain 215
8 Microkernel Architecture: Crafting Customizations 247
9 Do It Yourself: The TripEZ Travel App 277
10 Microservices Architecture: Bit by Bit 303
11 Event-Driven Architecture: Asynchronous Adventures 349
12 Do It Yourself: Testing Your Knowledge 403
13 Appendix: Leftovers: The Top Six Topics We Didn’t Cover 427
Index 441


```

Table of Contents (the real thing)
```
Intro
Because software architecture is hard, your brain will trick
you into thinking you can’t learn it. Your brain’s thinking, ”Better to
focus on more important things, like what to eat for lunch and whether pigs have wings.”
The good news is that you CAN trick your brain into thinking software architecture is an
important skill to learn, and in this chapter we’re going to show you just how to do that.
Who is this book for? xxii
We know what you’re thinking xxiii
We know what your brain is thinking xxiii
Metacognition: Thinking about thinking xxv
Here’s what WE did xxvi
Here’s what YOU can do to bend your brain into submission xxvii
Read me xxviii
Do it yourself chapters xxx
The technical review team xxxi
Joint acknowledgments xxxii
Individual acknowledgments xxxiii



vii
```


<a id='p10'></a>
<!-- Página 10 -->

table of contents




```
software architecture demystified


1
Let’s Get Started!
Software architecture is fundamental to the success
of your system. This chapter demystifies software architecture. You’ll
gain an understanding of architectural dimensions and the differences between
architecture and design. Why is this important? Because understanding and
applying architectural practices helps you build more effective and correct
software systems—systems that not only function better, but also meet the
needs and concerns of the business and continue to operate as your business
and technical environments undergo constant change. So, without further delay,
let’s get started.


Building your understanding of software architecture 2
Building plans and software architecture 3
The dimensions of software architecture 4
Puzzling out the dimensions 5
The first dimension: Architectural characteristics 6
The second dimension: Architectural decisions 8
The third dimension: Logical components 10
The fourth dimension: Architectural styles 12
A design perspective 16
An architectural perspective 17
The spectrum between architecture and design 18
Where along the spectrum does your decision fall? 19
Strategic versus tactical 20
High versus low levels of effort 22
Significant versus less-significant trade-offs 24
Putting it all together 26
You made it! 27




```

viii

<a id='p11'></a>
<!-- Página 11 -->

```
table of contents



architectural characteristics


```

2
```
Know Your Capabilities

What does your architecture need to support? Architectural
characteristics (the capabilities of an architecture) are the fundamental
building blocks of any system. Without them, you cannot make architectural
decisions, select an architectural style, or in many cases even create a logical
architecture. In this chapter you’ll learn how to define some of the more common
characteristics (like scalability, reliability, and testability), how they influence a
software architecture, how they help you make architectural decisions, and how to
identify which ones are important for your particular situation. Ready to add some
capabilities to your software architecture?


Causing Lafter 42
Cubicle conversation 43
What are architectural characteristics? 44
Defining architectural characteristics 45
Characteristics are nondomain design considerations 46
Characteristics influence architectural structure 47
Limit characteristics to prevent overengineering 48
Consider explicit and implicit capabilities 50
The International Zoo of “-ilities” 51
Process architectural characteristics 52
Structural architectural characteristics 53
Operational architectural characteristics 54
Cross-cutting architectural characteristics 55
Sourcing architectural characteristics from the problem domain 60
Sourcing architectural characteristics from environmental awareness 61
Sourcing architectural characteristics from holistic domain knowledge 61
Composite architectural characteristics 63
Priorities are contextual 64
Lost in translation 66
Architectural characteristics and logical components 68
Balancing domain considerations and architectural characteristics 69
Limiting architectural characteristics 70


ix
```


<a id='p12'></a>
<!-- Página 12 -->

table of contents



```
the two laws of software architecture


3
Everything’s a Trade-Off
What happens when there are no “best practices”? The nice thing
about best practices is that they’re relatively risk-free ways to achieve certain goals. They’re
called “best” (not “better” or “good”) for a reason—you know they work, so why not just use
them? But one thing you’ll quickly learn about software architecture is that it has no best
practices. You’ll have to analyze every situation carefully to make a decision, and you’ll need
to communicate not just the “what” of the decision, but the “why.”

So, how do you navigate this new frontier? Fortunately, you have the laws of software architecture
to guide you. This chapter shows you how to analyze trade-offs as you make decisions. We’ll
also show you how to create architectural decision records to capture the “hows” and “whys” of
decisions. By the end of this chapter, you’ll have the tools to navigate the uncertain territory that is
software architecture.

It starts with a sneaker app 82
What do we know so far? 84
Communicating with downstream services 86
Analyzing trade-offs 87
Trade-off analysis: Queue edition 88
Trade-off analysis: Topic edition 89
The first law of software architecture 90
It always comes back to trade-offs 92
Making an architectural decision 93
What else makes a decision architectural? 94
The second law of software architecture 96
Architectural decision records (ADRs) 97
Writing ADRs: Getting the title right 99
Writing ADRs: What’s your status? 100
Writing ADRs: Establishing the context 104
Writing ADRs: Communicating the decision 105
Writing ADRs: Considering the consequences 107
Writing ADRs: Ensuring governance 109
Writing ADRs: Closing notes 109
The benefits of ADRs 112
Two Many Sneakers is a success 113


```

x

<a id='p13'></a>
<!-- Página 13 -->

```
table of contents



logical components


```

4
```
The Building Blocks
Ready to start creating an architecture? It’s not as easy as
it sounds—and if you don’t do it correctly, your software system could come
crumbling to the ground, just like a poorly designed skyscraper or bridge.

In this chapter we’ll show you several approaches for identifying and creating
logical components, the functional building blocks of a system that describe how its
pieces all fit together. Using the techniques described in this chapter will help you
to create a solid architecture—a foundation upon which you can build a successful
software system.

Put on your hard hat and gloves, get your tools ready, and let’s get started.
Logical components revisited 124
Name that component 125
Adventurous Auctions goes online 126
Logical versus physical architecture 127
Creating a logical architecture 129
Step 1: Identifying initial core components 130
Workflow approach 132
Actor/action approach 134
The entity trap 136
Step 2: Assign requirements 138
Step 3: Analyze roles and responsibilities 140
Sticking to cohesion 141
Step 4: Analyze characteristics 142
The Bid Capture component 144
Component coupling 145
Afferent coupling 146
Efferent coupling 147
Measuring coupling 148
A tightly coupled system 150
Applying the Law of Demeter 151
A balancing act 153
Some final words about components 154
Name that component 156


xi
```


<a id='p14'></a>
<!-- Página 14 -->

table of contents



```
architectural styles


5
Categorization and Philosophies
There are lots of different architectural styles out
there. Each one exists for a reason and has its own philosophy about how
and when it should be used. Understanding a style’s philosophy will help you
judge whether it’s the right one for your domain. This chapter gives you a
framework for the different kinds of architectural styles (which we’ll be diving
into for the remainder of this book), to help you make sense of these and all
the other architectural styles you’ll encounter as a software architect.

Let’s fill in that final piece of the puzzle, shall we?



There are lots of architecture styles 168
The world of architecture styles 169
Partitioning: technical versus domain 170
Deployment model: monolithic versus distributed 172
Monolithic deployment models: the cons 174
Monolithic: the pros 175
Distributed deployment models: the pros 176
Distributed: The cons 177
And that’s a wrap! 180




```

xii

<a id='p15'></a>
<!-- Página 15 -->

```
table of contents



layered architecture


```

6
```
Separating Concerns
What if your problem is simple and time is of the
essence? Should you even bother with architecture? It depends on how long
you want to keep what you build. If it’s disposable, throw caution to the wind.
If not, then choose the simplest architecture that still provides some measurable
organization and benefit, without imposing many constraints on speed of delivery. The
layered architecture has become that architecture because it’s easy to understand and
implement, leveraging design patterns developers already know. Let’s peel back the
layers of this architecture.


Naan & Pop: Gathering requirements 186
Design patterns redux 188
Layering MVC 189
Layering it on 192
Translating layers into code 193
Domains, components, and layers 195
Drivers for layered architecture 198
Layers, meet the real world: Physical architectures 199
Physical architecture trade-offs 200
One final caveat about domain changes 203
Layered architecture superpowers 204
Layered architecture kryptonite 205
Layered architecture star ratings 206
Wrapping it up 208




xiii
```


<a id='p16'></a>
<!-- Página 16 -->

table of contents



```
modular monoliths


7
Driven by the Domain
There’s more than one way to build a monolith. So far,
you’ve encountered the layered architecture, which aligns things technically.
You can go a long way with a layered monolith, but when changes begin to involve
lots of communication and coordination between different teams, you might need a
little more horsepower under the hood—and perhaps even a different architectural
style.

This chapter looks at the modular monolith architectural style, which divides
applications up by business concerns as opposed to technical concerns. You’ll
learn what this means, what to look out for, and all the trade-offs associated with
this style. Let’s take the modular monolith for a spin, shall we?




Modular monolith? 219
Domain changes 221
Why modular monoliths? 222
Show me the code! 224
Keeping modules modular 227
Taking modularity all the way to the database 231
Beware of joins 233
Modular monolith superpowers 234
Modular monolith kryptonite 235
Modular monolith star ratings 236
Naan & Pop is delivering pizza! 238




```

xiv

<a id='p17'></a>
<!-- Página 17 -->

```
table of contents



microkernel architecture


```

8
```
Crafting Customizations
You can craft custom experiences, one capability at a
time. Some architecture styles are particularly well suited for some capabilities,
and the microkernel architecture is the world champion at customization. But it’s
also useful for a bewildering range of applications. Once you understand this
architectural style, you’ll start seeing it everywhere!

Let’s dig into an architecture that lets your users have it their way.




The benefits of Going Green 248
The two parts of microkernel architectures 251
The spectrum of “microkern-ality” 253
Device assessment service core 255
Encapsulated versus distributed plugins 257
Plugin communication 259
Plugin contracts 264
Going Green goes green 265
Microkernel superpowers 266
Microkernel kryptonite 267
Microkernel star ratings 268
Wrapping it up 270




xv
```


<a id='p18'></a>
<!-- Página 18 -->

table of contents



```
do it yourself


9
The TripEZ Travel App

Ready to extend your journey into software
architecture? In this chapter, you’re the software architect. You’ll
be determining architectural characteristics, building a logical architecture,
making architectural decisions, and deciding whether to use a layered,
modular, or microkernel architecture. The exercises in this chapter will give
you an end-to-end view of what a software architect does and show you
how much you’ve learned. Get ready to create an architecture for a startup
company building a travel integration convenience site. Bon voyage—we hope
you have a good trip building your architecture.

Making travel easier 278
TripEZ’s user workflow 279
Planning the architecture 280
The architects’ roadmap 281
Step 1: Identify architectural characteristics 282
Step 2: Identify logical components 284
Step 3: Choose an architectural style 286
Step 4: Document your decision 288
Step 5: Diagram your architecture 290
There are no right (or wrong) answers 292




```

xvi

<a id='p19'></a>
<!-- Página 19 -->

```
table of contents



microservices architecture


```

10
```
Bit by Bit
How do you make an architecture easier to change?
Business is changing faster than ever, and software architectures need to
keep up. In this chapter you’ll learn how to create a flexible architecture that
can change as your business changes, scale as your business grows, and
remain operational even when system failures occur. Intrigued? We hope
so, because in this chapter we’re going to show you microservices—an
architectural style that solves all of these problems and more. Let’s get started
on our journey through microservices, bit by bit.


Are you feeling okay? 304
What’s a microservice? 307
It’s my data, not yours 308
How micro is “micro”? 310
Granularity disintegrators 312
Why should you make microservices smaller? 313
Granularity integrators 314
Why should you make microservices bigger? 315
It’s all about balance 316
Sharing functionality 319
Code reuse with a shared service 320
Code reuse with a shared library 321
Managing workflows 325
Orchestration: Conducting microservices 326
Choreography: Let’s dance 328
Microservices architecture superpowers 332
Microservices architecture kryptonite 333
Microservices star ratings 334
Wrapping it up 336




xvii
```


<a id='p20'></a>
<!-- Página 20 -->

table of contents




```
event-driven architecture

11
Asynchronous Adventures
What if your architecture could do lots of things at the
same time? As businesses grow and become more successful, they need to
be able to handle more and more users, without slowing down or crashing systems.
In this chapter, you’ll learn how to design high-performance systems that can scale
as a business grows. Get ready for event-driven architecture, a highly popular
distributed architecture style. It’s very fast, highly scalable, and easy to extend—but
it’s also quite complex. You’ll be learning about lots of new concepts in this chapter,
including things like events, messages, and asynchronous communication, so you
can create an architectural that can do many things at once. Fasten your seatbelt,
and let’s go on an asynchronous adventure through event-driven architecture.


Too slow 350
Speeding things up 351
Der Nile flows faster than ever 352
What is an event? 354
Events versus messages 356
Initiating and derived events 358
Is anyone listening? 360
Asynchronous communication 361
Fire-and-forget 363
Asynchronous for the win 365
Synchronous for the win 367
Database topologies 369
Monolithic database 370
Domain-partitioned databases 372
Database-per-service 374
EDA versus microservices 378
Hybrids: Event-driven microservices 382
Event-driven architecture superpowers 384
Event-driven architecture kryptonite 385
Event-driven architecture star ratings 386
Putting it all together 388
Wrapping up 389


```

xviii

<a id='p21'></a>
<!-- Página 21 -->

```
table of contents



do it yourself


```

12
```
Testing Your Knowledge
Ready to test your skills in creating a distributed
architecture? In this chapter, you’re the software architect. You’ll be
determining architectural characteristics, building a logical architecture, making
architectural decisions, and deciding whether to use microservices or event-driven
architecture. The exercises in this chapter will give you an end-to-end view of what
a software architect does and show you how much you’ve learned. Get ready to
create an architecture for a student standardized test–taking system called Make
the Grade. Good luck—we hope you get an A on your architecture!




Welcome to Make The Grade 404
Student testing workflow 405
Planning the architecture 406
The architects’ roadmap 407
Step 1: Identify architectural characteristics 408
Step 2: Identify logical components 410
Step 3: Choose an architectural style 412
Step 4: Document your decision 414
Step 5: Diagram your architecture 416
There are no right (or wrong) answers! 418




xix
```


<a id='p22'></a>
<!-- Página 22 -->

table of contents



```
appendix: leftovers


```


## A

```
The Top Six Topics We Didn’t Cover
There’s a lot more to be said about software
architecture. We promise you’re done with this book. But reading this
book is just the first step in your journey to thinking architecturally, and we
couldn’t in good conscience let you go without a little more preparation. So,
we’ve gathered a few additional juicy bits into this appendix. Each of the topics
that follow deserves as much attention as the other topics we’ve covered.
However, our goal here is just to give you a high-level idea of what they’re
all about. And yes, this really is the end of the book. Except for the index, of
course—it’s a real page-turner!




#1 The coding architect 428
#2 Expectations for architects 430
#3 The soft skills of architecture 432
#4 Diagramming techniques 434
#5 Knowledge depth versus breadth 436
#6 Practicing architecture with katas 438




```

xx

<a id='p23'></a>
<!-- Página 23 -->

how to use this book
```
Intro
I can’t believe
they put that in a
software architecture
book.




ning question:
In this section we answer theinbur
a sof tware
“So why DID they put tha t
architecture book?”




xxi
```


<a id='p24'></a>
<!-- Página 24 -->

how to use this book



Who is this book for?
```
If you can answer “yes” to both of these:

1 Do you want to learn what software architecture is all
about?


2 Do you prefer stimulating dinner-party conversation to
dry, dull academic lectures?


This book is for you.




```

Who should probably back away from this book?
```
If you can answer “yes” to any of these:

1 Are you completely new to the tech industry?

(While we firmly believe that software developers should understand
the basics of software architecture, you might want to get a bit of
experience developing software before diving into this book.)
2 Are you a seasoned software architect looking for a
reference book?

3 Are you afraid to try something new? Would you rather
sit in a corner licking 9-volt batteries than advance your
career? Do you believe that a technical book can’t be
serious if it uses zoo animals to explain architectural
characteristics like scalability and fault tolerance?


This book is not for you.




[Note from marketing: This book is
for anyone with a credit card.]



```

xxii  intro

<a id='p25'></a>
<!-- Página 25 -->

```
the intro



```

We know what you’re thinking
```
Your bra
```

“How can this be a serious book on software architecture?” THIS is imin thinks
```
portant.
```

“What’s with all the graphics?”
“Can I actually learn it this way?”


We know what your brain is thinking
Your brain craves novelty. It’s always searching, scanning, waiting for
something unusual. It was built that way, and it helps you stay alive.
So what does your brain do with all the routine, ordinary, normal things you
encounter? Everything it can to stop them from interfering with the brain’s real
job—recording things that matter. It doesn’t bother saving the boring things;
they never make it past the “this is obviously not important” filter.
How does your brain know what’s important? Suppose you’re out for a day
hike and a tiger jumps in front of you. What happens inside your head and
body?
Neurons fire. Emotions crank up. Chemicals surge.
And that’s how your brain knows...
```
in thinks
Your bran’t worth Great. Only 450
```

This must be important! Don’t forget it! THIS is
```
saving.
more dull, dry,
```

But imagine you’re at home, or in a library. It’s a safe, warm, tiger‑free zone. boring pages.
You’re studying. Getting ready for an exam. Or trying to learn some tough
technical topic your boss thinks will take a week, 10 days at the
most.
Just one problem. Your brain’s trying to do you a big favor. It’s
trying to make sure that this obviously unimportant content
doesn’t clutter up scarce resources. Resources that are better
spent storing the really big things. Like tigers. Like the danger
of fire. Like how you should never have posted those “party”
photos on your Facebook page. And there’s no simple way
to tell your brain, “Hey brain, thank you very much, but no
matter how dull this book is and how little I’m registering on
the emotional Richter scale right now, I really do want you to
keep this stuff around.”




```
you are here 4  xxiii
```


<a id='p26'></a>
<!-- Página 26 -->

how to use this book




```
t” re ader as a learner.
We think of a “Head Firs
ve to get it, then
ar n so m et hing? First you ha .
So what does it ta
ke to le cts into your head
rg et it. It’s no t about pushing fa d
n’t fo logy, an
make sure you do science, neurobio
th e lat es t re se arch in cognitive te xt on a page. We
Based on
ar ni ng ta ke s a lot more than
hology, le
educational psyc
your brain on.
know what turns
ciples:
First lear ning prin
Some of the Head
much
ne and make learning
s are far mo re me morable than words alo thi ngs more
Make it visual. Im
age ke
studies). They also ma
89% im pro vem ent in recall and transfer to, rat her than on the
more effective (up to in or ne ar th e gr aphics they relate
the words with solve problems relate
d
understandable. Put wil l be up to twi ce as likely to be able to
r page, and learners
bottom or on anothe
to the content. performed up
recent studies, students
tio na l an d pe rs onalized style. In a first-person,
Use a conver sa
ng
ectly to the reader, usi
st-l ear nin g tes ts if the content spoke dir ing . Use casual language.
to 40% better on po for ma l ton e. Tel l sto ries instead of lec tur
her than tak ing a ting dinner par ty
conversational style rat would you pay more
attention to: a stimula
too ser iou sly . Wh ich
Don’t take yourself
e?
companion, or a lec tur rons, nothing much
actively flex your neu
to th ink mo re deeply. Unless you pired to solve problems
,
Get the learner mo tiv ate d, eng aged, curious, and ins
A reader has to be exercises, and
happens in your head. you need challenges,
ge ner ate new kno wledge. And for that, multiple senses.
draw conclusions, and th sides of the brain and
ies tha t inv olv e bo
estions, and activit
thought-provok ing qu to learn this but I can
’t
te nt ion . We ’ve all had the “I really want
he reader’s at out of the ordina ry,
Get—and keep—t ion to things that are
e on e” exp eri enc e. Your brain pays attent l top ic doesn’t have to be
stay awake past pag ect ed. Lea rni ng a new, tough, technica
-catching, unexp
interesting, strange, eye if it’s not.
wil l lea rn much more quick ly
boring. Your brain ing is largely depend
ent
w tha t you r abi lity to remember someth ing .
ions. We now kno en you feel someth
Touch their emot r wh at you car e abo ut. You remember wh
t. You remembe emotions like
on its emotional conten his dog. We’re talking
g hea rt‑w ren chi ng stories about a boy and you sol ve a puzzle, learn
No, we’re not talkin the fee ling of “I rul e!” that comes when
, “what the...?” and more technical than
surprise, curiosity, fun or rea lize you kno w something that “I’m
y else thinks is har d,
something everybod
ine ering doesn’t.
thou” Bob from eng




```

xxiv  intro

<a id='p27'></a>
<!-- Página 27 -->

```
the intro


I wonder how
```

Metacognition: Thinking about thinking I can trick my brain
If you really want to learn, and you want to learn more quickly and more into remembering
deeply, pay attention to how you pay attention. Think about how you think. this stuff...
Learn how you learn.
Most of us did not take courses on metacognition or learning theory when we
were growing up. We were expected to learn, but rarely taught to learn.
But we assume that if you’re holding this book, you really want to learn what
software architecture is all about. And you probably don’t want to spend a
lot of time on it. If you want to use what you read in this book, you need to
remember what you read. And for that, you’ve got to understand it. To get the most
```
from this book, or any book or learning experience, take responsibility for your
```

brain. Your brain on this content.
The trick is to get your brain to see the new material you’re learning as Really
Important. Crucial to your well‑being. As important as a tiger. Otherwise,
you’re in for a constant battle, with your brain doing its best to keep the new
content from sticking.

So just how DO you get your brain to treat software
architecture like it’s a hungry tiger?
There’s the slow, tedious way, or the faster, more effective way. The slow way is about
sheer repetition. You obviously know that you are able to learn and remember even
the dullest of topics if you keep pounding the same thing into your brain. With
enough repetition, your brain says, “This doesn’t feel important, but they keep looking
at the same thing over and over and over, so I suppose it must be.”
The faster way is to do anything that increases brain activity, especially
different types of brain activity. The things on the previous page are a big part of the
solution, and they’re all things that have been proven to help your brain work in your
favor. For example, studies show that putting words within the pictures they describe (as
opposed to somewhere else on the page, like a caption or in the body text) causes your
brain to try to make sense of how the words and picture relate, and this causes more
neurons to fire. More neurons firing = more chances for your brain to get that this is
something worth paying attention to, and possibly recording.
A conversational style helps because people tend to pay more attention when they
perceive that they’re in a conversation, since they’re expected to follow along and
hold up their end. The amazing thing is, your brain doesn’t necessarily care that the
“conversation” is between you and a book! On the other hand, if the writing style is
formal and dry, your brain perceives it the same way you experience being lectured to
while sitting in a roomful of passive attendees. No need to stay awake.
But pictures and conversational style are just the beginning…




```
you are here 4  xxv
```


<a id='p28'></a>
<!-- Página 28 -->

how to use this book



Here’s what WE did
We used visuals, because your brain is tuned for visuals, not text. As far as your brain’s
concerned, a visual really is worth a thousand words. And when text and visuals work
together, we embedded the text in the visuals because your brain works more effectively
when the text is within the thing the text refers to, as opposed to in a caption or buried in a
paragraph somewhere.
We used redundancy, saying the same thing in different ways and with different media types,
and multiple senses, to increase the chance that the content gets coded into more than one area
of your brain.
We used concepts and visuals in unexpected ways because your brain is tuned for novelty,
and we used visuals and ideas with at least some emotional content, because your brain
is tuned to pay attention to the biochemistry of emotions. That which causes you to feel
something is more likely to be remembered, even if that feeling is nothing more than a little
humor, surprise, or interest.
We used a personalized, conversational style, because your brain is tuned to pay more
attention when it believes you’re in a conversation than if it thinks you’re passively listening
to a presentation. Your brain does this even when you’re reading.
We included dozens of activities, because your brain is tuned to learn and remember more
when you do things than when you read about things. And we made the exercises challenging
yet doable, because that’s what most people prefer.
We used multiple learning styles, because you might prefer step-by-step procedures, while
someone else wants to understand the big picture first, and someone else just wants to see
an example. But regardless of your own learning preference, everyone benefits from seeing the
same content represented in multiple ways.
We included content for both sides of your brain, because the more of your brain you
engage, the more likely you are to learn and remember, and the longer you can stay focused.
Since working one side of the brain often means giving the other side a chance to rest, you
can be more productive at learning for a longer period of time.
And we included stories and exercises that present more than one point of view,
because your brain is tuned to learn more deeply when it’s forced to make evaluations and
judgments.
We included challenges, with exercises, and we asked questions that don’t always have
a straight answer, because your brain is tuned to learn and remember when it has to work at
something. Think about it—you can’t get your body in shape just by watching people at the
gym. But we did our best to make sure that when you’re working hard, it’s on the right things.
That you’re not spending one extra dendrite processing a hard-to-understand example
or parsing difficult, jargon-laden, or overly terse text.
We used people. In stories, examples, visuals, etc., because, well, because you’re a person.
And your brain pays more attention to people than it does to things.



xxvi  intro

<a id='p29'></a>
<!-- Página 29 -->

```
the intro


Here’s what YOU can do to bend
your brain into submission
So, we did our part. The rest is up to you. These tips are a
starting point; listen to your brain and figure out what works
for you and what doesn’t. Try new things.
Cut this out and sti
on your refrigerator.ck it

```

1 Slow down. The more you understand, the 6 Drink water. Lots of it.
```
less you have to memorize. Your brain works best in a nice bath of fluid.
Don’t just read. Stop and think. When the book asks Dehydration (which can happen before you ever
you a question, don’t just skip to the answer. Imagine feel thirsty) decreases cognitive function.
that someone really is asking the question. The
more deeply you force your brain to think, the better 7 Listen to your brain.
chance you have of learning and remembering. Pay attention to whether your brain is getting
overloaded. If you find yourself starting to skim
```

2 Do the exercises. Write your own notes. the surface or forget what you just read, it’s time
```
We put them in, but if we did them for you, that for a break. Once you go past a certain point, you
would be like having someone else do your workouts won’t learn faster by trying to shove more in, and
for you. And don’t just look at the exercises. Use a you might even hurt the process.
pencil. There’s plenty of evidence that physical
activity while learning can increase the learning.
8 Feel something.
Your brain needs to know that this matters. Get
```

3 Read the “There Are No Dumb Questions.”
```
involved with the stories. Make up your own
That means all of them. They’re not optional captions for the photos. Groaning over a bad joke
sidebars, they’re part of the core content! is still better than feeling nothing at all.
Don’t skip them.

```

4 Make this the last thing you read before bed. 9 Apply it every day!
```
Or at least the last challenging thing. There’s only one way to learn how to really
Part of learning (especially the transfer to long-term understand software architecture: apply it
memory) happens after you put the book down. Your every day. You are going to be doing software
brain needs time on its own, to do more processing. If architecture a lot in this book, and like with any
you put in something new during that processing time, other skill, the only way to get good at it is to
some of what you just learned will be lost. practice. We’re going to give you a lot of practice:
every chapter has exercises that pose problems for
you to solve. Don’t just skip over them—a lot of the
```

5 Talk about it. Out loud. learning happens when you solve the exercises. We
Speaking activates a different part of the brain. If included a solution to each exercise—don’t be afraid
you’re trying to understand something, or increase to peek at the solution if you get stuck! (It’s easy
your chance of remembering it later, say it out loud. to get snagged on something small.) But try to solve
Better still, try to explain it out loud to someone else. the problem before you look at the solution. And
You’ll learn more quickly, and you might uncover definitely get it working before you move on to the
ideas you hadn’t known were there when you were next part of the book.
reading about it.

```
you are here 4  xxvii
```


<a id='p30'></a>
<!-- Página 30 -->

how to use this book



Read me
This is a learning experience, not a reference book. We deliberately stripped out
everything that might get in the way of learning whatever it is we’re working on at
that point in the book. And the first time through, you need to begin at the beginning,
because the book makes assumptions about what you’ve already seen and learned.

We break things down, then build them back again.
We are fans of teasing things apart. This gives us the chance to focus on one aspect
of software architecture at a time. We use a lot of visuals to explain various aspects of
software architecture. We make sure you have a deep understanding of each aspect,
and have the confidence to know when and how to use them. Only then do we start to
bring things together, to explain the more complex ideas in software architecture.


We don’t exhaustively cover everything.
We use the 80/20 approach. We assume that if you are going for a PhD in
software architecture, this isn’t going to be your only book. So, we don’t talk about
everything—just the stuff that you’ll actually use, and that you need to hit the ground
running. We want to hit the ground running.


The activities are NOT optional.
The exercises and activities are not add-ons; they’re part of the core content of the
book. Some of them are to help with memory, some are for understanding, and some
will help you apply what you’ve learned. Don’t skip the exercises. The crossword
puzzles are the only thing you don’t have to do, but they’re good for giving your brain a
chance to think about the words and terms you’ve been learning in a different context.




xxviii  intro

<a id='p31'></a>
<!-- Página 31 -->

```
the intro




```

The redundancy is intentional and important.
One distinct difference in a Head First book is that we want you to really get it. And
we want you to finish the book remembering what you’ve learned. Most reference
books don’t have retention and recall as a goal, but this book is about learning, so you’ll
see some of the same concepts come up more than once.


The examples are as generic as possible.
To teach you software architecture, we have to use business problems—otherwise, the
concepts we introduce in this book would be too abstract and hard to follow. We’ve
­deliberately made the examples in this book generic, yet also interesting, fascinating,
and downright fun. No matter your background, we are certain you will be able to
relate to them when practicing software architecture, whatever kind of work you do.


The Brain Power exercises don’t always have answers.
For some of them, there is no right answer, and for others, part of the learning
experience is for you to decide if and when your answers are right. In some of the
Brain Power exercises, you will find hints to point you in the right direction.




O’Reilly online le arning
```
For more than 40 years, O’Reilly Media has provided
technology and business training, knowledge, and insight to help
companies succeed.
```

Our unique network of experts and innovators share their knowledge and expertise
through books, articles, and our online learning platform. O’Reilly’s online learning
platform gives you on-demand access to live training courses, in-depth learning
paths, interactive coding environments, and a vast collection of text and video from
O’Reilly and 200+ other publishers. For more information, visit http://oreilly.com.


```
you are here 4  xxix
```


<a id='p32'></a>
<!-- Página 32 -->

how to use this book



Do it yourself chapters
A unique aspect of this particular Head First book is what we
call “do it yourself ” chapters. These chapters (there are two of
them) are entirely exercise-based and give you a chance to create
an architecture from beginning to end, applying all the concepts
you’ve learned up to that point.
In these chapters, you’re the software architect. You’ll
determine architectural characteristics, build a logical architecture,
and make architectural decisions, including what kind of
architectural style to use. Doing the exercises in these chapters
gives you an end-to-end view of what a software architect does
and shows you how much you’ve learned.



```
In Chapter 9, the first “do it yourself ” chapter, you’ll create
an architecture for a trip-management system called TripEZ
(pronounced like “trapeze”) that aims to make travel easier,
especially for road warriors. This new online trip-management
dashboard app will allow travelers to see and manage all of their
travel reservations, organized by trip, through a browser or on their
mobile devices.




```

In Chapter 12, the second “do it yourself ” chapter, you’ll
create an architecture for a standardized-testing system called
Make the Grade. All Dataville Public School students in
specific grade levels take the same test to determine how well
students, teachers, and the school are doing. This chapter will
be a great way for you to test your knowledge (so to speak).




xxx  intro

<a id='p33'></a>
<!-- Página 33 -->

```
the intro



```

The technical review team
```
Tanya Reilly Christine
Nate Schutta Schutta
```

Meet our review team!
We were lucky enough to round up a powerhouse
team of people to review this book, including
senior developers, software architects,
renowned public speakers, and prolific
book authors.
These experts read every chapter, did the exercises,
```
Venkat
```

corrected our mistakes, and provided detailed
```
Subramaniam Patrick
```

commentary on every single page of this book. Clare Sudbery
They also acted as our sounding board, letting Viafore
us work through ideas, analogies, and narratives.
They even helped us think through how this book
should be organized.
Every single reviewer here made
huge contributions to this book and
vastly improved its quality. We deeply
appreciate the countless hours they
spent poring over the manuscript. We Marc Loy James Erler Max Schubert
remain indebted to them.

Thank you! Special thanks also to
```
Moataz Sanad for finding
lots of our typos!
Despite our (and our
reviewers’) best efforts, any
and all errors and omissions
are ours and ours alone.




you are here 4  xxxi
```


<a id='p34'></a>
<!-- Página 34 -->

acknowledgments



Joint acknowledgments
This book would not have been possible without the help, guidance, and support from a
number of great individuals. We have a lot of people to thank, so let’s get started!


Our editor:
Our first and foremost acknowledgment goes, along with our utmost thanks, to
our brilliant editor Sarah Grey. Writing a book like Head First Software Architecture
presented a number of unique challenges for us, and Sarah was there to guide us the
entire time. She helped keep us on track when we deviated from the Head First style
of writing (which was quite often) and made constant suggestions about every page’s
layout (really, we mean every page). Sarah took on the role of crossword expert and
helped us out quite a bit with the Make It Stick poetry. We frequently referred to Sarah
as our “fourth author,” and in reality, she deserves much of the credit for the outcome The brilliant
of this book. Sarah Grey


The O’Reilly team:
A big thanks to the entire O’Reilly Media team, including Kristen Brown and Chris
Faucher for making sure that our book was production-worthy, and to Rachel Head for
her keen and astute copyediting eye. And if, like us, you routinely use book indexes, you
have Tom Dinse to thank for this one.
We’d also like to thank Melissa Duffield for her continued support and patience
throughout this process, and for considering us for this long project.
Much appreciation to the O’Reilly online training team, especially Yasmina Greco,
Lindsay Ventimiglia, and all the producers, for giving us a platform to teach
software architecture to thousands of developers and architects around the world.
A shoutout to the Early Release team, who put out raw and unedited chapters as they
were written for the audience on the O’Reilly platform to review. This gave many of our
readers a chance to submit errata and feedback that made this book just that much better.
Finally, we would be remiss if we did not mention series editors Elisabeth Robson and
Eric Freeman, who took the time to review our work and ensure that it aligned with the
vision that is the Head First series—not to mention giving us some really useful InDesign
tips. Thank you!




xxxii  intro

<a id='p35'></a>
<!-- Página 35 -->

```
the intro



```

Individual acknowledgments
From Raju Gandhi:
It’s hard for me to express how much of a privilege it has been to work on this project,
and to be able to work with Mark and Neal—two of the smartest and most wonderful
human beings, who not only were kind enough to consider me as a coauthor, but who
since have spent countless hours teaching me the nuances of software architecture.
Someday I hope I can repay that debt. For now, they have my deepest appreciation. A
shoutout to so many friends, colleagues, unwitting mentors and teachers, and fellow
speakers who’ve been a source of inspiration for me—you all know you who are.
And finally, to my wife Michelle. We had baby Delphine while I was working on this
project, and Michelle has certainly taken on more than her share as I spent many an
hour working on this book. Thank you. I love you both.


```
From Mark Richards:
In addition to the joint acknowledgments, I would like to thank my friends and coauthors
Raju and Neal. Raju brought prior Head First experience to the table from his great book
Head First Git, and helped teach us the Head First style of writing and the ins and outs of
InDesign. This is my third book with Neal, and as usual, working and collaborating with
him was a very rewarding and enjoyable experience. I would also like to thank my lovely
wife Rebecca for her patience and understanding while I was hidden away in my office
for so many evenings writing this book instead of enjoying her company.




```

From Neal Ford:
I would like to thank first and foremost my coauthors, Mark and Raju, both of whom
were a delight to work with and made this book possible. Mark is as always a fantastic
collaborative juggernaut with a good sense of humor, both vital when writing is not our
day job. I’d also like to thank our editor Sarah, who has an outsized role in this book
series, for helping keep us in check. Thanks also to my extended families, both genetic
and chosen, for their support and respite. That includes our weekly neighborhood
cocktail club that moved to the parking lot during the pandemic and stayed there; it’s
great to catch up with what is happening nearby. And finally and primarily, I’d like to Good thing we
thank my wonderful wife Candy, who endures many long hours with me away from her only had three
and our cats, working on stuff like what you hold in your hand. authors, or these
```
acknowledgments
would go on and on
and on...
```

And finally, you, the readers. Your attention is a scarce resource, and we deeply
appreciate the time you’ll spend with this book. Happy learning.



```
you are here 4  xxxiii
```


<a id='p36'></a>
<!-- Página 36 -->


<a id='p37'></a>
<!-- Página 37 -->

1 software architecture demystified
```
Let’s Get Started!




Software architecture is fundamental to the success of your
system. This chapter demystifies software architecture. You’ll gain an understanding
of architectural dimensions and the differences between architecture and design. Why
is this important? Because understanding and applying architectural practices helps
you build more effective and correct software systems—systems that not only function
better, but also meet the needs and concerns of the business and continue to operate
as your business and technical environments undergo constant change. So, without
further delay, let’s get started.




this is a new chapter   1
```


<a id='p38'></a>
<!-- Página 38 -->

software architecture basics



Building your understanding of
software architecture
To better understand software architecture, think about a typical home in your
neighborhood. The structure of the home is its architecture—things like its The building metapho
shape, how many rooms and floors it has, its dimensions, and so on. A house is a very popular on r
is usually represented through a building plan, which contains all the lines and for understanding e
boxes necessary to know how to build the house. Structural things like those software architectu
shown below are hard and expensive to change later and are the important stuff
```
re.
```

about the house.

This house has a Chimney
```
Roof
```

nice architecture.



```
Load-b
Load-bearing wall earing
column
Not only is this house
ugly, it’s not very
functional either.


Dim
ensio
ns

```

Architecture is essential for building a house. Can you imagine building one without
an architecture? It might turn out looking something like the house on the right.
Architecture is also essential for building software systems. Have you ever come
across a system that doesn’t scale, or is unreliable or difficult to maintain? It’s likely
not enough emphasis was placed on that system’s architecture.



```
Exercise
Gardening is another useful metaphor for describing software architecture. Using the space below, can you describe
how planning a garden might relate to software architecture? You can see what we came up with at the end of this
chapter.


Solution on page 29

```

2  Chapter 1

<a id='p39'></a>
<!-- Página 39 -->

```
software architecture demystified



```

Building plans and software architecture
You might be wondering how the building plans of your home relate to software
architecture. Each is a representation of the thing being built. So what does the
“building plan” of a software system look like? Lines and boxes, of course.
```
Fun fac
to be catll—a building plan
```

A building plan specifies the structure of your home—the rooms, walls, stairs, and
```
but that ed a “blueprint used
```

so on—in the same way a software architecture diagram specifies its structure (user
```
obsolete term is now ,”
```

interfaces, services, databases, and communication protocols). Both artifacts provide
```
building a (at least within
```

guidelines and constraints, as well as a vision of the final result.
```
rchitectu
re).




Both of these diagrams
represent building plans.


Sharpen your pencil Did you notice that the floor plan for
the house above doesn’t specify the
details of the rooms—things like the
What features of your home can you list that are structural and related type of flooring (carpet or hardwood),
to its architecture? You can find our thoughts at the end of this chapter. the color of the walls, and where a bed
Use this might go in a bedroom? That’s because
write dowspace to those things aren’t structural. In other
ideas. n your words, they don’t specify something
about the architecture of the house,
but rather about its design.


Don’t worry—you’ll learn
about this distinction latera lot
in
more
chapter. Right now, just focus isth
the structure of something—in on
words, its architecture. other

Solution on page 29

you are here 4  3
```


<a id='p40'></a>
<!-- Página 40 -->

software architecture dimensions



The dimensions of software architecture
```
Length Width
Most things around us are multidimensional.
For example, you might describe a particular
room in your home by saying it is 5 meters long
and 4 meters wide, with a ceiling height of 2.5
```

Height meters. Notice that to properly describe the room
```
you needed to specify all three dimensions—its
height, length, and width.
You can describe software architecture by its
dimensions, too. The difference is that software
architecture has four dimensions.



```

1 Architectural characteristics architectural characteristics
```
This dimension describes what aspects of the




architectural decisions
system the architecture needs to support—things




architectural style
like scalability, testability, availability, and so on.


```

2 Architectural decisions
```
This dimension includes important decisions that
have long-term or significant implications for
the system—for example, the kind of database it
uses, the number of services it has, and how those
services communicate with each other.

```

3 Logical components logical components
```
This dimension describes the building blocks of the system’s
functionality­and how they interact with each other. For
example, an ecommerce system might have components for
inventory management, payment processing, and so on. You’ll le
most comarn about five of
```

4 Architectural style styles lat mon architectur the
```
er in this al
This dimension defines the overall physical shape and structure of a
book.
software system in the same way a building plan defines the overall shape
and structure of your home.




```

4  Chapter 1

<a id='p41'></a>
<!-- Página 41 -->

```
software architecture demystified



```

Puzzling out the dimensions

You can think of software architecture as a puzzle, with each dimension representing a
separate puzzle piece. While each piece has its own unique shape and properties, they must
all fit together and interact to build a complete picture.




```
We’re going to help yo ta
pieces and build a compulet ke the puzzle
e
what software architect picture of
ure is all about.

Everything is interconnected.
Did you notice how the pieces of this puzzle are joined in the
middle? That’s exactly how software architecture works: each
dimension must align.
The architectural style must align with the architectural
characteristics you choose as well as the architectural decisions
you make. Similarly, the logical components you define must
align with the characteristics and the architectural style as well
as the decisions you make.


there are no
Dumb Questions
```

Q: Do you need all four dimensions when creating an architecture, or can you skip some if you don’t have time?

A: Unfortunately, you can’t skip any of these dimensions—they are all required to create and describe an architecture. One common
mistake software architects make is using only one or two of these dimensions when describing their architecture. “Our architecture is
microservices” describes a single dimension—the architectural style—but leaves too many unanswered questions. For example, what
architectural characteristics are critical to the success of the system? What are its logical components (functional building blocks)? What
major decisions have you made about how you’ll implement the architecture?




```
you are here 4  5
```


<a id='p42'></a>
<!-- Página 42 -->

architectural characteristics



The first dimension: Architectural characteristics
```
Architectural characteristics form the foundation of the architecture
in a software system. Without them, you cannot make architectural
decisions or analyze important trade-offs.
Imagine you’re trying to choose between two homes. One home is
roomy but is next to a busy, noisy motorway. The other home is in a
```

nice, quiet neighborhood, but is much smaller. Which characteristic is more important to you—
home size or the level of noise and traffic? Without knowing that, you can’t make the right choice.
The same is true with software architecture. Let’s say you need to decide what kind of database to use
for your new system. Should it be a relational database, a simple key/value database, or a complex
graph database? The answer will be based on what architectural characteristics are critical to you. For
example, you might choose a graph database if you need high-speed search capability (we’ll call that
performance), whereas a traditional relational database might be better if you need to preserve data
relationships (we’ll call that data integrity).

```
it y
ance availabilit scalabilility to maintain
perfor m e it takes The amou
y em’s ab and
unt of tim cess a nt of uptim The syst se time
The amo pro system; usu e of a
n s is te n t respon of users
ystem to ally measu a co e numbe
r
for the s “nines” (s red in te a s t h
reques t o 99.9% w
ould be er ror ra ases
business three “nin
es”) r e q u e sts incre
or

Here are some of the more common architectural
characteristics. You’ll be learning all about these
in Chapter 2.

Exercise
Check the things you think might be considered architectural characteristics—something that the structure of the
software system supports.

Changing the font size in a window on the user interface screen
Making changes quickly
Handling thousands of concurrent users
Encrypting user passwords stored in the database
Interacting with many external systems to complete a business request


Solution on page 30

```

6  Chapter 1

<a id='p43'></a>
<!-- Página 43 -->

```
software architecture demystified




```

The term architectural characteristics might not be familiar
to you, but that doesn’t mean you haven’t heard of them before.
Collectively, things like performance, scalability, reliability, and Ma ke it
availability are also known as nonfunctional requirements, system
quality attributes, and simply “the -ilities” because most end with Stick
the suffix -ility. We like the term architectural characteristics because
these qualities help define the character of the architecture and To architect software
```
you must
```

what it needs to support. first address:
```
Capabilities key to the
ristics are new app’s
Architectural characetecritical or success
capabilities that arsuccess of the system.
important to the




Who Does What
Here’s your chance to see how much you already know about many common architectural characteristics. Can you
match up each architectural characteristic on the left with its definition on the right? You’ll notice there are more
definitions than characteristics, so be careful—not all of the definitions have matches.

Extensibility Taking into account time frames, budgets, and
developer skills when making architectural choices
We did this
one for you. The system’s ability to keep its other parts
Agility functioning when fatal errors occur

The ease with which the system can be enhanced to
support additional features and functionality
Interoperability
The amount of time it takes to get a response to the
user
Fault tolerance
The system’s ability to respond quickly to change
(a function of maintainability, testability, and
deployability)
Feasibility
The system’s ability to interface and interact with
other systems to complete a business request

Solution on page 30

you are here 4  7
```


<a id='p44'></a>
<!-- Página 44 -->

architectural decisions



The second dimension: Architectural decisions
```
Architectural decisions are choices you make about structural
aspects of the system that have long-term or significant
implications. As constraints, they’ll guide your development team
in planning and building the system.
Should your new home have one floor or two? Should the roof
be flat or peaked? Should you build a big, sprawling ranch house?
These are good examples of architectural decisions because they
What should your home look
involve the structural aspect of your home.
like? This kind of decision
is an architectural one.



? ?
```

You might decide that your system’s user interface should not
communicate directly with the database, but instead must go through
the underlying services to retrieve and update data. This architectural
decision places a particular constraint on the development of the user
interface, and also guides the development team about how other
components should access and update data in the database.

Here’s an example
of an architectural This architectural
decision. Architectural decision imposes
```
decision a constraint and
acts as a guide.
The user interface must
go through the data
access service to read
Data
Access
Service
```


## X

```
or write data; it cannot
communicate directly with
the database.
This image
represents a
You’ll be learning a lot service. You’ll be
about architectural seeing it a lot in
decisions in Chapter 3. the book.
This is the
database.

```

8  Chapter 1

<a id='p45'></a>
<!-- Página 45 -->

```
software architecture demystified




Ma ke it
It’s not uncommon to have several dozen or more
documented architectural decisions within any system.

Stick
Generally, the larger and more complicated the
system, the more architectural decisions it will have.

for dev
re s tr u c tu ral guides
a
Decisions
tea m s .
nt themes.
on significa
They o ft e n fo c u s
BE the architect
Your job is to be the architect and identify
as many architectural decisions as you
can in the diagram below. Draw a circle
around anything that you think might be
an architectural decision and write what
that decision might be.
Here’s a hint—do you have questions
about why certain things are done
the way they are?


Order Inventory Payment
Placement Adjuster Mediator




Credit Gift Reward
Card Card Points
Payment Payment Payment
```

Reporting Order Inventory
Database Database Database




```
Payment
Solution on page 31 Database


you are here 4  9
```


<a id='p46'></a>
<!-- Página 46 -->

logical components



The third dimension: Logical components
```
These rooms m
Logical components are the up the buildingake
building blocks of a system, blocks of your
much in the same way rooms are home.
the building blocks of your home.
A logical component performs
some sort of function, such as
processing the payment for an
```

order, managing item inventory, or tracking orders.
Logical components in a system are usually represented through a
directory or namespace. For example, the directory app/order/
payment with the corresponding namespace app.order.
payment identifies a logical component named Payment Processing.
The source code that allows users to pay for an order is stored in this
directory and uses this namespace.


```
Order
Tracking
es
All of these bocaxl components.
represent lo gi


Order Payment Order
We dive into
Placement Processing Shipping details of logtiche
components an al
how to create d
The Payment Processing them in Chapt
er 4.
logical component is app
Inventory identified through this
Management directory structure and is order
implemented through these
three source code files. payment

pay_with_creditcard.py
Architectural
components are pay_with_giftcard.py
language-agnostic. process_refund.py
We just happen to
be using Python
here.



```

10  Chapter 1

<a id='p47'></a>
<!-- Página 47 -->

```
software architecture demystified




Sharpen your pencil A logical component should always have a welldefined role and responsibility in the system—in
other words, a clear definition of what it does.
```

You’ve just created the following two components for a
new system, and your development team wants to start
writing class files to implement them. Can you create
```
This component is responsible
```

a directory structure for them so they can start coding?
```
for “pick and pack.” It locates
```

Flip to the end of the chapter for our solution.
```
items in a warehouse (that’s the Order
“pick” part), then determines Fulfillment
the correct box size for the
Customer items so they can be shipped
Customer (that’s the “pack” part).
Profile Preferences
This is the role and
responsibility statement
Use this for the Order
write dowspace to Fulfillment component.
answer. n your


Ma ke i
t
Stick
Logical
co
conjunc mponents are
tion. blocks
in
They ho
ld the s
busines ou
s functi rce code for e
on. ach
Solution on page 32


there are no
Dumb Questions
```

Q: What is the difference between the system functionality and the domain?

A: The domain is the problem you are trying to solve, and the system functionality is how you are solving that problem. In other
words, the domain is the “what,” and the system’s functionality is the “how.”




```
you are here 4  11
```


<a id='p48'></a>
<!-- Página 48 -->

architectural styles



The fourth dimension: Architectural styles
```
Homes come in all shapes, sizes, and styles. While there
are some wild-looking houses out there, most conform to a
particular style, such as Victorian, ranch, or Tudor. The style Each region
of a home says a lot about its overall structure. For example, world has itsof the
ranch homes typically have only one floor; colonial and of home styles—own set
Tudor homes typically have chimneys; contemporary homes ’em out at ht check
typically have flat roofs. en.wikipedia.ortps://
List_of_hous g/wiki/
e_styles.

me do
t st yle ho
a
```

Wh live in?
you




```
Don’t worry
learning all ab—you’ll be
```

Architectural styles define the overall shape and structure of a software system,
```
architectural out these
```

each with its own unique set of characteristics. For example, the microservices
```
later in the b styles
```

architectural style scales very well and provides a high level of agility—the ability
```
devoted chaptook. We’ve
```

to respond quickly to change—whereas the layered architectural style is less
```
each of them. ers to
```

complex and less costly. The event-driven architectural style provides high levels
of scalability and is very fast and responsive.



```
eve
microser vices ectur e ntarchit dr i v
d en
layere arc
hite
ctu
re




There are a number of different
architectural styles, but fortunately
not as many as there are house styles.


```

12  Chapter 1

<a id='p49'></a>
<!-- Página 49 -->

```
software architecture demystified




```

Because the architectural style defines the overall shape and

```
Ma ke i
```

characteristics of the system, it’s important to get it right the
first time. Why? Can you imagine starting construction on
a one-story ranch home, and in the middle of construction t
changing your mind and deciding you’re going to build a Stick
three-story Victorian house instead? That would be a major
undertaking, and likely exceed your budget and affect when you
can move into the house. Styles s
```
ha
its purp pe the system
```

Software architecture is no different. It’s not easy changing oses. and help
```
You mig serve
from a monolithic layered architecture to microservices. Like
ht choo
```

the house example, this would be quite an undertaking. microse se a mo
```
rvices. nolith o
r




Later in the book, we’ll show you how to
Converting properly select an architectural style based
ranch house ftroom a sprawling on characteristics that are important to you.
story Victoria a multi- Which brings us back to an earlier
very difficult n would be point—all of the dimensions of software
structures are because the architecture are interconnected. You
so different. can’t select an architectural style without
knowing what’s important to you.




Brain
Power The tightly wound tendons and muscles in a lion’s legs enable it to reach
speeds as fast as reach speeds as fast as 50 miles (80 kilometers) per hour
and leap up to 36 feet (11 meters) in a single bound. This characteristic
allows lions to survive by catching fast prey.
Look around you—what else has a structure or shape that defines its
characteristics and capabilities?

Fun fact: A lion doesn’t hav mu
only run fast in short burstse. If ch stamina and can
than the lion chasing you, then youyou can last longer
just might survive.

you are here 4  13
```


<a id='p50'></a>
<!-- Página 50 -->

putting the pieces together




```
Who Does What
```

We were trying to describe our architecture, but all the puzzle pieces got mixed up. Can you help us figure out
which dimension does what by matching the statements on the left with the software architecture dimensions on
the right? Be careful—some of the statements don’t have a match because they are not related to architecture.
```
bility.
This is about availa
This system must be available for our overseas customers.

We did this
```

Customers are complaining about the background color one for you.
of the new user interface.


The product owner insists that we get new features and
bug fixes out to our customers as fast as possible.


Our system uses an event-driven architecture.


```
We need to support up to 300,000 concurrent users in
this system.


```

The single payment service will be broken apart into
separate services, one for each payment type we accept.



We are going to start offering reward points as a new
payment option when paying for an order.




We are breaking up the orderPlacement class into
three smaller class files.


The user interface shall not communicate directly with
the database.


```
Solution on page 33

```

14  Chapter 1

<a id='p51'></a>
<!-- Página 51 -->

```
software architecture demystified




```

If I’m responsible for the
design of a software system,
does that mean I’m responsible
for its architecture as well?
Aren’t those the same thing?




```
No, architecture and design are different.
You see, architecture is less about appearance and more about structure,
while design is less about structure and more about appearance.
The color of a room’s walls, the placement of furniture, and the type of
flooring (carpet or wood) are all aspects of design, whereas the physical
size of the room and the placement of doors and windows are part of
architecture—in other words, the structure of the room.
Think about a typical business application. The architecture, or structure,
is all about how the web pages communicate with backend services and
databases to retrieve and save data, whereas the design is all about what
each page looks like: the colors, the placement of the fields, which design
patterns you use, and so on. Again, it becomes a matter of structure versus
appearance.
Your question is a good one, because sometimes it gets confusing trying to
tell what is considered architecture and what is considered design. Let’s
investigate these differences.




you are here 4  15
```


<a id='p52'></a>
<!-- Página 52 -->

design vs. architecture



A design perspective
Suppose your company wants to replace its outdated order processing system with a new
custom-built one that better suits its specific needs. Customers can place orders and can
view or cancel orders once they have been placed. They can pay for an order using a
credit card, a gift card, or both payment methods.

```
Lucky you. You’ve been put in
charge of building the new ord er
processing system. This is the big
break you’ve been looking for
you’re anxious to get started., and




```

From a design perspective, you might build a Unified Modeling Language (UML) class diagram like the
one below to show how the classes interact with each other to implement the payment functionality.
While you could write source code to implement these class files, this design says nothing about the
physical structure of the source code—in other words, how these class files would be organized and deployed.

```
Orders can have one or
two payment types, and
payment types can be
associated with zero or
more orders.



The CreditCard and
GiftCard classes inherit
behavior from the
PaymentMethod class.




```

16  Chapter 1

<a id='p53'></a>
<!-- Página 53 -->

```
software architecture demystified



```

An architectural perspective
Unlike design, architecture is about the structure of the system—things like services, databases,
and how services communicate with each other and the user interface.
Let’s think about that new order processing system again. What would the system look like?
From an architectural perspective, you might decide to create separate services for each payment
type within the order payment process and have an orchestrator service to manage the
payment processing part of the system, like in the diagram below.

As a gentle reminder, The Paym
each of these boxes service alloent Mediator
represents a “service.” pay for youws you to
```
Order Payment
with a cred r order
Placement Mediator
gift card, it card,
Service Service or both.




Credit Gift
Card Card
Service Service
Each service would have
its own class diagram
representing the design
of the service.




Exercise
Check all of the things that should be included in a diagram from an architectural perspective.

How services communicate with each other
The platform and language in which the services are implemented
Which services can access which databases
How many services and databases there are
Solution on page 34

you are here 4  17
```


<a id='p54'></a>
<!-- Página 54 -->

architecture–design spectrum



The spectrum between architecture and design
Some decisions are certainly architectural (such as deciding which architectural style to use),
and others are clearly design-related (such as changing the position of a field on a screen or
changing the type of a field within a class). In reality, most decisions you encounter will fall
between these two examples, within a spectrum of architecture and design.

```
Things on this side are Things on this side are
more about architecture. more about design.

Don’t worry if you
don’t know all the
```

Architecture Design answers to this
```
You’ll find most of your decisions fall exercise—you’ll
within the spectrum right about here. learn more about
this topic on the
next page.
Sharpen your pencil
Circle all of the things that you think fall somewhere in the middle of the spectrum between
architecture and design. ework
ti n g a u se r interface fram
le Selec
p a class fi atabase
```

Breaking u ec id in g to u se a graph d Migrating to
```
microservic
D Redesignin es
g a web pa
Choosing a Breaking apart a g e
persistence Choosing an XML parsing library
framework service
Solution on page 34

Why should I care
where in the spectrum
between architecture and
design my decision lies?
Does it really matter that
much?



Yes, it matters a lot. You see, knowing where along the spectrum
between architecture and design your decision lies helps determine who
should be responsible for ultimately making that decision. There are some
decisions that the development team should make (such as designing the
classes to implement a certain feature), some decisions that an architect
should make (such as choosing the most appropriate architectural style for
a system), and others that should be made together (such as breaking apart
services or putting them back together).


```

18  Chapter 1

<a id='p55'></a>
<!-- Página 55 -->

```
software architecture demystified



```

Where along the spectrum does your decision fall?
```
Is it strategic or tactical?
Strategic decisions are long term and influence future actions or
decisions. Tactical decisions are short term and generally stand
independent of other actions or decisions (but may be made in the
context of a particular strategy). For example, deciding how big your
new home will be influences the number of rooms and the sizes of those
rooms, whereas deciding on a particular lighting fixture won’t affect
decisions about the size of your dining room table. The more strategic
the decision, the more it sits toward the architecture side of the spectrum.


waking
```

Sometimes morning
up in thea lot of How much effort will it take to construct or change?
requires we’ll call Architectural decisions require more effort to construct or
effort— chitecture” change, while design decisions require relatively less. For
those “ar. example, building an addition to your home generally requires
mornings a high level of effort and would therefore be more on the
```
architecture side of the spectrum, whereas adding an area rug
to a room requires much less effort and would therefore be more
on the design side.




Does it have significant trade-offs?
Trade-offs are the pros and cons you evaluate as you are making a
decision. Decisions that involve significant trade-offs require much more
time and analysis to make and tend to be more architectural in nature.
Decisions that have less-significant trade-offs can be made quicker, with
less analysis, and therefore tend to be more on the design side.

We’re going to walk you through
the details of all three of these
factors in the next several pages.
Brain
Power
Can you think of a decision that doesn’t involve a trade-off, no matter how small or insignificant? Here’s a hint:
if you think you’ve found a decision that doesn’t involve a trade-off, keep looking.




you are here 4  19
```


<a id='p56'></a>
<!-- Página 56 -->

level of planning



Strategic versus tactical
The more strategic a decision is, the more architectural it becomes. This is an important
distinction, because decisions that are strategic require more thought and planning and
are generally long term.



Architecture Design

```
Strategic Tactical

How
can I determine
whether a decision
is more strategic or
more tactical?


Good question. You can use these three questions to help
determine if something is more strategic or tactical. Remember, the
more strategic something is, the more it’s about architecture.


1. How much thought and planning do you need to
put into the decision?
If making the decision takes a couple of minutes to an hour, it’s more
tactical in nature. If thought and planning require several days or weeks,
it’s likely more strategic (hence more architectural).


2. How many people are involved in the decision?
The more people involved, the more strategic the decision. A decision
you can make by yourself or with a colleague is likely to be tactical.
A decision that requires many meetings with lots of stakeholders is
probably more strategic.

3. Does your decision involve a long-term vision or a
short-term action?
If you are making a quick decision about something that is temporary
or likely to change soon, it’s more tactical and hence more about design.
Conversely, if this is a decision you’ll be living with for a very long time,
it’s more strategic and more about architecture.

```

20  Chapter 1

<a id='p57'></a>
<!-- Página 57 -->

```
software architecture demystified



```

Sharpen your pencil
```
Oh dear. We’ve lost all of our marbles and we need your help collecting them and putting them
back in the right spot. Using the three questions on the previous page as a guide, can you figure
out which jar each marble should go in?




Deciding to get Deploying in the
Picking a your first dog cloud or on premises
programming
language for your
new project



Choosing a
parsing library
Migrating Using a design
```

Redesigning your your system to pattern
user interface microservices




```
Strategic Somewhere in Tactical
between
Solution on page 35

you are here 4  21
```


<a id='p58'></a>
<!-- Página 58 -->

level of effort



High versus low levels of effort
Renowned software architect and author Martin Fowler once wrote that “software Martin Fowler’s website
architecture is the stuff that’s hard to change.” You can use Martin’s definition (https://martinfowler.
to help determine where along the spectrum your decision lies. The harder com/architecture) has
something is to change later, the further it falls toward the architecture side of the lots of useful stuff about
spectrum. Conversely, the easier it is to change later, the more it’s probably related architecture.
to design.



Architecture Design

```
High effort Low effort

```

Suppose you are planning on moving from one architectural style to another; say, from a
traditional n-tiered layered architecture to microservices. This migration effort is rather
difficult and will take a lot of time. Because the level of effort is high, this would be on
the far end of the architecture side of the spectrum.
```
Oh dear,
to take a this is going
Changing t lot of effort.
architectu hings that are
ral is diff
icult.



layout
```

Changing thes on a Now suppose you’re rearranging fields on a user interface screen. This
```
ld
```

of the fie more task takes relatively less effort, so it resides on the far end of the design
web page is rance side of the spectrum.
about appea ure—yet
than struct son
another rea uld be
why this wo esign.
considered d




22  Chapter 1

<a id='p59'></a>
<!-- Página 59 -->

```
software architecture demystified



Code Magnets
We had all of these magnets from our to-do list arranged from high effort to low effort, and somehow
they all fell on the floor and got mixed up. Can you help us put them back in the right order based on the
amount of effort it would take to make each change?

rt
r o w s to p ut the high-effdo the High effort
Draw ar op of the pag
e, an
of
tasks at thettones toward the bottom
lower-ef f o r
the page.
Resolv
in
confli g a merge
ct in
Git



user
ng your
```

Replaci ework
```
ce fram
```

interfa


Migrating your
```
system to
```

a cloud environm
```
ent



mustard
g which
```

Decidin
```
to buy


```

Renaming a meth
```
od or
function


single
a ki ng apart a ones
```

Br e parate
rv ic e into se
se


Moving from a relational
```
to a graph database


Low effort
```

Breaking apart
```
a class file


Solution on page 36

you are here 4  23
```


<a id='p60'></a>
<!-- Página 60 -->

significant trade-offs



Significant versus less-significant trade-offs
Some decisions you make might involve significant trade-offs, such as choosing which city
to live in. Others might involve less significant trade-offs, like deciding on the color of
your living room rug. You can use the level of significance of the trade-offs in a particular
decision to help determine whether that decision is more about architecture or design. The
more significant the trade-offs, the more it’s about architecture; the less significant the tradeoffs, the more it’s about design.



Architecture Design

```
More-significant Less-significant
trade-offs Trade-offs

I wonder
if microservices Wow—
might be a good fit serious these are s
for this project. conside trade-offome
about r. This is s to
archit m
ecture ore
.
+ Scalability - Cost
+ Agility - Complexity
+ Elasticity - Performance
+ Fault tolerance - Workflow


Should I break This trad
my class file so significae-off is not
apart? this decisio nt, making
about desig n more
n.


+ Maintainability - More classes
+ Readability




```

24  Chapter 1

<a id='p61'></a>
<!-- Página 61 -->

```
software architecture demystified



Exercise
```

Decisions, decisions, decisions. How can we ever tackle all of these decisions? One thing we think might
help is to identify the decisions that involve significant trade-offs, since those will require more thinking and
will take longer. Can you help us by identifying which decisions have significant trade-offs and which don’t?


Is this a significant trade-off?

```
Yes No Picking out what clothes to wear to work today

Yes No Choosing to deploy in the cloud or on premises

Yes No Selecting a user interface framework

Yes No Naming a variable in a class file

Yes No Choosing between vanilla and chocolate ice cream

Yes No Deciding which architectural style to use

Yes No Choosing between REST and messaging

Yes No Using full data or only keys for the message payload

Yes No Selecting an XML parsing library

Yes No Deciding whether or not to break apart a service

Yes No Choosing between atomic or distributed transactions

Yes No Deciding whether or not to go out to dinner tonight

Solution on page 37




you are here 4  25
```


<a id='p62'></a>
<!-- Página 62 -->

chapter summary



Putting it all together
Now it’s time to put all three of these factors to use to figure out whether a decision is
more about architecture or more about design. This tells development teams when to
collaborate with an architect and when to make a decision on their own.
Let’s say you decide to use asynchronous messaging between the Order Placement
service and the Inventory Management service to increase the system’s responsiveness
when customers place orders. After all, why should the customer have to wait for the
business to adjust and process inventory? Let’s see if we can determine where in the
spectrum this decision lies.

```
ments are sent to
Inventory adjustManagement service
the Inventory eue.
through this qu
Order Inventory
Placement Queue Management
Service Service




Significance of trade-offs Strategic or tactical
Using a queue will increase responsiveness when Not many people need to be
placing an order, but inventory may not be updated The significant involved in this decision, and
in a timely manner, likely creating back-order trade-offs push this it doesn’t involve long-term
conditions. These are pretty significant trade-offs. decision closer to planning, so it’s more tactical.
architecture.




```

Architecture Design


Taking the mean of all three factors puts the decision
right about here, meaning this decision has some
architectural aspects and an architect should probably
be consulted or involved. We needed all three factors Level of effort
to determine whether this decision was more about It doesn’t take a whole lot
architecture or design. of effort to send a message
```
to another service. This is
pretty standard stuff.



```

26  Chapter 1

<a id='p63'></a>
<!-- Página 63 -->

```
software architecture demystified



```

You made it!
Congratulations—you made it through the first part of your journey to understanding
software architecture. But before you roll up your sleeves to dig into further chapters, here’s
a little quiz for you to test your knowledge so far. For each of the statements below, circle
whether it is true or false.



True or False
True False Design is like the structure of a house (walls, roof, layout, and so on), and
```
software architecture is like the furniture and decoration.
```

True False Most decisions are purely about architecture or design. Very few
```
exist along a spectrum between architecture and design.

```

True False The more strategic your decision, the more it’s about architecture;
```
the more tactical, the more it’s about design.

```

True False The more effort it takes to implement or change your decision, the more
```
it’s about design; the less effort, the more it’s about architecture.

```

True False Trade-offs are the pros and cons of a given decision or task. The more
```
significant the trade-offs become, the more it’s about architecture.
Solution on page 38


```

Bullet Points
 Software architecture is less about appearance and  The logical components of a software architecture
```
more about structure, whereas design is more about solution make up the building blocks of the system.
appearance and less about structure. They represent things the system does and are
implemented through class files or source code.
```

 You need to use four dimensions to understand
```
and describe software architecture: architectural  Like with houses, with software there are many
characteristics, architectural decisions, logical different architectural styles you can use. Each style
components, and architectural style. supports a specific set of architectural characteristics,
so it’s important to make sure you select the right one
```

 Architectural characteristics form the foundational
```
(or combination of them) for your system.
aspects of software architecture. You must know
which architectural characteristics are most important  It’s important to know if a decision is about
to your specific system, so you can analyze trade-offs architecture or design, because that helps determine
and make the right architectural decisions. who should be responsible for the decision and how
important it is.
```

 Architectural decisions serve as guideposts to help
```
development teams understand the constraints and
conditions of the architecture.




you are here 4  27
```


<a id='p64'></a>
<!-- Página 64 -->

software architecture crossword




```
Software Architecture Crossword
Congratulations! You made it through the first chapter and learned
about what software architecture is (and isn’t). Now, why don’t you
try architecting the solution to this crossword?




Across Down
2. An architectural style determings the system’s overall 1. Strategic decisions typically involve a lot of these
_____ 3. Building this can be a great metaphor
4. _____-driven is an architectural style 6. Decisions can be strategic of _____
5. Architectural characteristics are sometimes called this 7. How many dimensions it takes to describe a software
10. Architectural decisions are usually _____ term architecture
12. If something takes a lot of _____ to implement, it’s 8. A website’s user _____ involves lots of design decisions
probably architectural 9. The overall shape of a house or a system, like Victorian
13. You’re learning about software _____ or microservices
15. You’ll make lots of architectural _____ 11. It’s important to know whether a decision is about
16. A system’s _____ components are its building blocks architecture or this
18. The number of rooms in your home is part of its 13. You might want to become one after reading this book
_____ 14. You analyze these when making an architectural
19. Architecture and design exist on a _____ decision
17. Trade-offs are about the _____ and cons

Solution on page 39

```

28  Chapter 1

<a id='p65'></a>
<!-- Página 65 -->

```
software architecture demystified



Exercise From page 2
Solution
Gardening is another useful metaphor for describing software architecture. Using the space below, can you
describe how a garden might relate to software architecture?

The overall layout of a garden can be compared to the architectural style, whereas each grouping of
like plants (either by type or color) can represent the architectural components. Individual plants
within a group represent the class files implementing those components.
Gardens are influenced by weather in the same way a software architecture is influenced by changes
in technology, platforms, the deploymnent environment, and so on. Also, if you don’t pay attention
to the garden, weeds grow-just like structural decay within your architecture.




Sharpen your pencil From page 3

Solution
```

What features of your home can you list that are structural and related to its architecture?




```
a n d sh ape of sn’t hHow many floors it W he re the front door is is
e e a y
```

The sizitchen (who dosmall stasir(as you get older, and if the entrancelewa
your k in about how
```
la p r o b
s might be
le a wheelchair accessib
p
```

com itchen is? ) m )
```
s
their k f yo u r T he he ight of your ceilingto
eo ou (especially if you ha
ppen
The sizom closet (if ys)
o
bedr ts of cloth e be very ta ll)
```

How many b h a ve l o
(adding a newathrooms it has An attic for storing all of Outside deck or
hard to do) b at hroom is really the stuff you never use (u nless you live in patio
```
Arctic, of course the
)




you are here 4  29
```


<a id='p66'></a>
<!-- Página 66 -->

exercise solutions


```
Exercise
From page 6
Solution
Check the things you think might be considered architectural characteristics—something that the structure of the
software system supports.

Changing the font size in a window on the user interface screen
This is known as agility in
Making changes quickly architecture.
This is known as elasticity.
Handling thousands of concurrent users
This is known as
interoperability.
Encrypting user passwords stored in the database

Interacting with many external systems to complete a business request



Who Does What From page 7

Solution
```

Here’s your chance to see how much you already know about many common architectural characteristics. Can you
match up each architectural characteristic on the left with its definition on the right? You’ll notice there are more
definitions than characteristics, so be careful—not all of the definitions have matches.


```
Extensibility Taking into account time frames, budgets, and
developer skills when making architectural choices
We did this
one for you. The system’s ability to keep its other parts
Agility functioning when fatal errors occur

The ease with which the system can be enhanced to
support additional features and functionality
Interoperability
The amount of time it takes to get a response to the
user
Fault tolerance The system’s ability to respond quickly to change
(a function of maintainability, testability, and
deployability)
Feasibility
The system’s ability to interface and interact with
other systems to complete a business request


```

30  Chapter 1

<a id='p67'></a>
<!-- Página 67 -->

```
software architecture demystified



From page 9

BE the architect
Solution
Your job is to be the architect and identify
as many architectural decisions as you
can in the diagram below. Draw a circle
around anything that you think might be
an architectural decision and write what
that decision might be.



rder The Invento
```

The Oment service is communicatry service
Place ting to the payment ing with
is wri eporting Why not the service.
the r ase. Why? Placement serOrder
```
datab vice?

Payment
Order Inventory Why do You dec
Placement Adjuster Inventoreys the Mediator
break upided to
have its o service payment the
database wn Why? services.
?


Credit Gift Reward
Card Card Points
Payment Payment Payment
```

Reporting Order Inventory
Database Database Database


```
The Or
is directdlyer Placement se
the paym communicatingrvice are
ent data
base. Whwy ith a y m e n t services t have
ep no
? All of tha database. Whoyr each Payment
sharing ate database f Database
a separ
service?

you are here 4  31
```


<a id='p68'></a>
<!-- Página 68 -->

exercise solutions



```
From page 11
Sharpen your pencil
Solution
You’ve just created the following two components for a new system, and your development team
wants to start writing class files to implement them. Can you create a directory structure for them
so they can start coding?

Customer Customer
Profile Preferences

buy_from_us
customer
profile
source_code_files

preferences
source_code_files




```

32  Chapter 1

<a id='p69'></a>
<!-- Página 69 -->

```
software architecture demystified




Who Does What
From page 14


Solution
```

We were trying to describe our architecture, but all the puzzle pieces got mixed up. Can you help us figure out
which dimension does what by matching the statements on the left with the software architecture dimensions on
the right? Be careful—some of the statements don’t have a match because they are not related to architecture.
```
bility.
This is about availa
```

This system must be available for our overseas customers.

```
We did this
```

Customers are complaining about the background color one for you.
of the new user interface.
```
This is ab
out agility.
```

The product owner insists that we get new features and
bug fixes out to our customers as fast as possible.


Our system uses an event-driven architecture.


We need to support up to 300,000 concurrent users in
this system.
```
This isabout scalability.

```

The single payment service will be broken apart into
separate services, one for each payment type we accept.



We are going to start offering reward points as a new
payment option when paying for an order.
```
This is ab
componentout adding a new
to the arc log
hitectureic. al
```

We are breaking up the orderPlacement class into
three smaller class files.


The user interface shall not communicate directly with
the database.



```
you are here 4  33
```


<a id='p70'></a>
<!-- Página 70 -->

exercise solutions



```
Exercise From page 17
Solution
Check all of the things that should be included in a diagram from an architectural perspective.
How
be im something
How services communicate with each other design plemente should
perspe d is a
The platform and language in which the services are implemented ctive.
Which services can access which databases
How many services and databases there are




From page 18
Sharpen your pencil
Solution
Circle all of the things that you think fall somewhere in the middle of the spectrum between
architecture and design.
This is design. This
archi is
le framework
tect ure.
p a class fi h database ser interface
```

Breaking u se a grap Selecting a u
```
Deciding to u Migrating to
Redesignin microservic
Choosing a g a web pa es
persistence Breaking apart a ge
framework
service Choosing an XML parsing library
These are design.




```

34  Chapter 1

<a id='p71'></a>
<!-- Página 71 -->

```
software architecture demystified



From page 21
Sharpen your pencil
Solution
Oh dear. We’ve lost all of our marbles and we need your help collecting them and putting them back in the right spot.
Using the three questions on page 20 as a guide, can you figure out which jar each marble should go in?

volves This requires a lot of planning, is
This decision ainmily. more visionary, and involves a lot
```

T the entire f of people.
usu hese r
ally eq
```
invo uire
lve som
a f e pl
ew ann Deciding to get
oth ing Picking a Deploying in the
er and your first dog cloud or on premises
peo
programming
ple
language for your
.
new project You can usually make
these decisions alone.


Choosing a
parsing library
Migrating Using a design
Redesigning your
user interface
your system to Good pattern
microservices luck.




Strategic Somewhere in Tactical
between

you are here 4  35
```


<a id='p72'></a>
<!-- Página 72 -->

exercise solutions



```
Code Magnets From page 23

Solution
We had all of these magnets from our to-do list arranged from high effort to low effort, and
somehow they all fell on the floor and got mixed up. Can you help us put them back in the
right order based on the amount of effort it would take to make each change?

High effort
hoice”
ie ve us ? P lu g “paradox of c
Don’t bel vorite search engine. ng which
mustard
into your fa Decidi
to buy



Migrating your
system to
a cloud environm
ent
would
e t a k e a lo t of effort andecture
Thes hit
de on the arc
therefore resispectrum. Replacing your user
side of the interface framework



Moving from a re
lational
to a graph databa
This would fall right about in the middle se
of the spectrum between architecture
and design. Breaking apart a single
service into separate ones


Resolving a merg
e
conflict in Git
These take relatively less eff
would therefore reside more ort and
side of the spectrum. on the design
Breaking apart a class file


Renaming a meth
od or
function


Low effort




```

36  Chapter 1

<a id='p73'></a>
<!-- Página 73 -->

```
software architecture demystified


Exercise From page 25
Solution
```

Decisions, decisions, decisions. How can we ever tackle all of these decisions? One thing we think might help
is to identify the decisions that involve significant trade-offs, since those will require more thinking and will
take longer. Can you help us by identifying which decisions have significant trade-offs and which ones don’t?

```
Okay, so maybe this is a
```

Significant Tradeoffs? difficult decision sometimes.

```
Yes No Picking out what clothes to wear to work today

Yes No Choosing to deploy in the cloud or on premisis
inly tradeThere are certtahis one could go
Yes No Selecting a user interface framework offs here, so
either way.
Yes No Deciding on the name of a variable in a class file

Yes No Choosing between vanilla and chocolate ice cream

scalability,
These can impaact
Yes No Deciding which architectural style to use
rall
pe rformance, nd ove
maintainability.
Yes No Choosing between REST and messaging

Yes No Using full data or only keys for the message payload

Yes No Selecting an XML parsing library

Yes No Deciding whether or not to break apart a service

Yes No Choosing between atomic or distributed transactions

Yes No Deciding whether or not to go out to dinner tonight
Are you gettin
g hungry yet? This can impact data integrity
and data consistency, but also
scalability and performance.


you are here 4  37
```


<a id='p74'></a>
<!-- Página 74 -->

exercise solutions




True or False
```
From page 27

Solution
This is backward
s.
True False Design is like the structure of a house (walls, roof, layout, and so on), and
software architecture is like the furniture and decoration.
Most d
True False Most decisions are purely about architecture or design. Very few within tecisions lie
exist along a spectrum between architecture and design. between he spectrum
and desig architecture
n.
True False The more strategic your decision, the more it’s about architecture;
the more tactical, the more it’s about design.


True False The more effort it takes to implement or change your decision, the more
kwards.
This is bac
it’s about design; the less effort, the more it’s about architecture.


True False Trade-offs are the pros and cons of a given decision or task. The more
significant the trade-offs become, the more it’s about architecture.




```

38  Chapter 1

<a id='p75'></a>
<!-- Página 75 -->

```
software architecture demystified


```

Software Architecture Crossword Solution

```
From page 23




you are here 4  39
```


<a id='p76'></a>
<!-- Página 76 -->


<a id='p77'></a>
<!-- Página 77 -->

2 architectural characteristics
```
Know Your Capabilities




What does your architecture need to support? Architectural
characteristics (the capabilities of an architecture) are the fundamental
building blocks of any system. Without them, you cannot make architectural
decisions, select an architectural style, or in many cases even create a
logical architecture. In this chapter you’ll learn how to define some of the
more common characteristics (like scalability, reliability, and testability), how
they influence a software architecture, how they help you make architectural
decisions, and how to identify which ones are important for your particular
situation. Ready to add some capabilities to your software architecture?




this is a new chapter 4  41
```


<a id='p78'></a>
<!-- Página 78 -->

project requirements



Causing Lafter
Sillycon Symposia is a startup with a Bay Area feel whose business plan combines
technology-themed conferences with comedy. By gathering like minds, Sillycon provides
```
How hard could it
```

unique offerings for each group and keeps them engaged by keeping them laughing.
```
be to start a social
networking site?!
```

Part of the business plan includes building Lafter, a social media network related to (but
not limited to) the conferences Sillycon hosts. The business stakeholders put together a
requirements document for it:
```
The good news is that
they’ve got the logo
figured out. The rest
is up to you.




media network of like-minded
Sillycon Symposia is hosting a social
technologists named Lafter.
```

A pretty standard sands of users
```
Users: Hundreds of speakers, thou
```

level of detail for a
requirements document Requirements:
```
approve the privacy policy
Users can register for usernames and
as a “Joke” (long-form post) or
Users can add new content on Lafter
“Pun” (short-form post)
ng approval) or “Giggle” (a
Followers can “HaHa” (indicating stro
like
milder approval message) content they
have a special icon
Speakers at Sillycon Symposia events
form related to their content
Speakers can host forums on the plat
characters
Users can post messages of up to 281
content
Users can also post links to external
Additional Context:
International support
Very small support staff
ng live conferences
“Bursty” traffic: extremely busy duri




```

42  Chapter 2

<a id='p79'></a>
<!-- Página 79 -->

```
architectural characteristics



```

Mara Sam Alex Cubicle conversation
```
Alex: Look what just landed in my inbox—the Powers That Be want me to
be the architect for the Sillycon Symposia social media app, Lafter.
Sam: You have the requirements? You should jump right into the design of
the system—it seems really straightforward.
Mara: Well, you can really only do that for the simplest of applications,
and I don’t think this one qualifies. Remember the diagram I drew on the
whiteboard the other day?
These are the nonfunctional
requirements.




These are the
These represent decisions we make
the problem domain. after doing a
trade-off analysis.




Architectural characteristics and logical
components together help us decide on
the architectural style.
You need to analyze both architectural characteristics and logical
components before you can choose an architectural style as a starting point.
You can implement just about any application in any architectural style, but
some are more suitable than others. Choosing the style before performing
this type of analysis is a classic case of putting the cart before the horse.
Sam: Can’t we just be super-agile, start with something tiny, and then
keep iterating on it until we have the entire system?
Mara: The iterative approach you talk about doesn’t quite work like that
for architectural characteristics analysis. For example, it’s difficult to make a
system highly scalable if it wasn’t designed for that.
Alex: That makes sense. I guess I need to roll up my sleeves and analyze
some architectural characteristics—thanks!

you are here 4  43
```


<a id='p80'></a>
<!-- Página 80 -->

defining architectural characteristics



What are architectural characteristics?
You have a problem. You decide, “I’m going to write some software to solve this
problem!” The thing you’re writing software about is called the domain, and These make up one of
designing for it will occupy much of your effort—that is, after all, why you’re the dimensions that help
writing software. However, it’s not the only thing an architect must consider—they describe your architecture.
must also analyze architectural characteristics. Here are a few examples of
architectural characteristics that show how different domains have different, but
often overlapping, architectural characteristics.
```
Notice how many of them
end with “-ility”.

Aud ita bili t y
Banks must provide a way Dat a int egr it y
to verify transactions. Financial transactions must
be consistent and accurate.

Sec uri t y
Banks require stringent Bank
security to protect
financial concerns.
Both domains have scalability as
an architectural characteristic
they must support. Scalabilit y Banks must support large
numbers of concurrent users.
Online auctions must support
a large number of bidders.
```

Usabilit y
Auction sites must be
easy to use for quick and
efficient entry of bids.




```
Online auction
Rel iab ilit y
Consistency Auction sites must be
Bids must be captured reliable—users don’t like it if
consistently and in order their connection drops in the
for auctions to work. middle of an auction.

```

44  Chapter 2

<a id='p81'></a>
<!-- Página 81 -->

```
architectural characteristics



```

Defining architectural characteristics
Part of your job as an architect is structural design for software systems,
for which there are two parts: logical components and architectural
characteristics. Logical components represent the domain of the
application—the motivation for writing the software system (we cover these
in Chapter 4). If you combine architectural characteristics with logical
components, you have the structural considerations for an architecture.
Architectural characteristics are the important parts of the construction
process of a software system or application, irrespective of the problem
domain. They represent its operational capabilities, internal structure
decisions, and other necessary characteristics.
We’ll show you lots of examples of architectural characteristics in the
upcoming pages, but first we want to cover the concept itself.
We define architectural characteristics in three parts, as shown here.

```
We cover logical component
design in Chapter 4—stay tuned!




This represents how Some problems (like
architectural characteristics scalability) can only be
differ from the domain. solved via architecture.




Used as filtering criteria
to avoid overengineering.


```

Let’s look at each of these edges one at a time.


```
you are here 4  45
```


<a id='p82'></a>
<!-- Página 82 -->

domain or nondomain



Characteristics are nondomain design
considerations
To define architectural characteristics, we first need to look at what
they are not. The requirements specify what the application should
do; architectural characteristics specify operational and design criteria for
success, how to implement the requirements, and why certain choices
```
lking
```

were made. For example, an application’s level of performance is an We are tais edge here.
important architectural characteristic that often doesn’t appear in about th
requirements documents.
Structural design in architecture can be divided into domain and
non-domain considerations. Architectural characteristics represent
your design effort to create the capabilities necessary for the project to
succeed.




```
Mara: OK, the business analysts and subject matter experts have toiled
away to create both a requirements document and the beginning of
a domain design. But we need to work with them to figure out what
architectural characteristics we need to support.
Sam: Isn’t that part of the domain design? Why does an architect need to
get involved at this point?
Alex: Well, our business analysts have never worked on a software porject,
so they probably won’t understand the impact of one decision versus
another.
Mara: That’s correct—often what seems like a minor difference to a
business person makes a big difference for an architect! What they want
may turn out to be difficult to support in architecture. That’s why it’s
important for architects to be involved early and often in the design process.
Sam: What kinds of things are we looking for?
Alex: Part of the definition of architectural characteristics is “nondomain
design considerations.” Let’s look at what they’ve designed and see if
they’ve considered things like performance and scalability.


```

46  Chapter 2

<a id='p83'></a>
<!-- Página 83 -->

```
architectural characteristics



```

Characteristics influence architectural
structure
```
We’ve moved on to the
```

The primary reason architects try to describe architectural characteristics
```
second edge here.
```

has to do with architectural considerations: does this characteristic
require special structural support to succeed? For example, security is
a concern in virtually every project, and all systems must take baseline
precautions during design and coding. However, security becomes an
architectural characteristic when the architect needs to make a special effort
to accommodate it.
Consider the following potential architecture diagrams for Lafter, which
include functionality for marketing upcoming promotions and rules
for when each promotion applies. An architect could design this as a
monolithic architecture—one with a single deployable unit and
matching database—or as a series of independent services.
For the monolithic architecture, the entire application would have to be
redeployed when the promotion rules change, because monoliths are built
and deployed as a single unit. However, in a distributed architecture,
only the Promotions service would be affected, and it could be redeployed In a distributed
independently. architecture, each
```
service is deployed
independently.
```

This is a monolithic
architecture. Add event
```
Promote Promote user
event Add event event
user




```

If Promotions
needs to fix a bug Promotions
in production, the Post
```
message
```

whole application
needs to be Post Promotions

redeployed. message


```
In this case,
Promotions can
go to production
anytime they like!



```

You must consider many trade-offs when making architectural decisions, such as whether to use a
monolithic versus distributed physical architecture.

```
you are here 4  47
```


<a id='p84'></a>
<!-- Página 84 -->

limiting characteristics



Limit characteristics to prevent
overengineering
Applications could support a huge number of architectural
characteristics…but they shouldn’t. Every architectural characteristic
the system must support adds complexity.
The sheer number and variety of architectural characteristics means
there are many tempting choices. But as architects, we should try to
pick as few architectural characteristics as possible, rather than as
many as possible. This is because architectural characteristics are:
```
We are talking about the
third edge. Almost there!
Impossible to standardize It’s a good idea to cr
Different organizations use different terms for the same architectural a “ubiquitous langua
eate
ge ”
vocabulary) for arch (shared
characteristics. For example, performance and responsiveness might
indicate the same behavior. characteristics withinitectural
organization—this gi your
fighting chance at crves you a
Synergistic usable standard list. eating a
Your takeaway? You Architectural characteristics affect other architectural characteristics
ofte n cann ot choo se and domain concerns. For example, if you want to make an
one arch itec tura l application more secure, the required changes will almost certainly
char acte risti c with out affect performance negatively (more on-the-fly encryption and other
cons ider ing how it may similar changes will lead to performance overhead).
affe ct othe rs.
Even the number of
categories of architectural
Overabundant characteristics has
Possible architectural characteristics are extraordinarily abundant,
increased over the last few
and new ones appear all the time. For example, a few years ago there
years, with additions such
was no such thing as on-demand elasticity via a cloud provider.
as cloud constraints and
capabilities.
```

A common hazard for architects is overengineering: supporting too many We’ll be discussing some
architectural characteristics and complicating the overall design to little or no categories of architectural
benefit. Knowing which architectural characteristics are critical or important characteristics soon.
to application success acts as a filtering tool. It help us eliminate features that
would be nice to have but just end up adding needless complexity to the system.
Beware of resume-driven development (RDD)! It’s fun to play with new stuff,
and we should keep learning, but trying to support too many architectural
characteristics in our systems will not align with larger priorities or help the
application succeed.


48  Chapter 2

<a id='p85'></a>
<!-- Página 85 -->

```
architectural characteristics




Synergy can be dangerous!
Architects would love to design for architectural characteristics irrespective of the domain

```

Watch it!
```
design. Unfortunately, the real world refuses to cooperate. When we say that architectural
characteristics are synergistic, we mean that changes to one might require changes to other
architectural characteristics and/or the domain. No matter how clever you are, no architect can make
every single architecture scalable. Some architectures can’t scale as successfully as others because of
physical constraints such as memory and bandwidth.
Be careful when you change one architectural characteristic; consider how that change may affect other
parts of your architecture. The same applies to making changes to domain design, such as component
boundaries and distribution—changes to the domain may synergistically affect your architectural
characteristics. For example, if you change your application to begin storing users’ payment information,
the security and data integrity architectural characteristics will also change.




Brain
Power
Many things in the the real world are synergistic—that is, combining them yields something different than
the sum of the parts. See if you can think of some real-world examples of synergy. Hint: These might include
things that are still identifiable (like peanut butter and chocolate) or things that merge (such as emulsions like oil
and vinegar). Use this space to
jot down your ideas.




you are here 4  49
```


<a id='p86'></a>
<!-- Página 86 -->

explicit versus implicit



Consider explicit and implicit capabilities
Some things are explicit—stated clearly—whereas others are implicit—
assumed based on context or other knowledge. Imagine if you saw a
bunch of mail and packages piling up outside the door of a home—what
conclusions would you draw?



```
Explicit Implicit
```

Packages are stacked No one is home.
outside a door.
```
This family orders a
bunch of stuff online.
```

The door is locked.

```
Is this family on
vacation?

```

Explicit architectural characteristics are specified in the
requirements for the application.
Implicit architectural characteristics are factors that influence We need to
an architect’s decisions but aren’t explicitly called out in
```
protect the
```

the requirements. Security is often an implicit architectural
```
privacy of users.
t
```

characteristic: even if it isn’t mentioned in the requirements,
```
m u st supporsers!
```

architects know that we shouldn’t design an insecure system. We reds of u
```
hund
```

You must use your knowledge of the problem domain to uncover
these architectural characteristics during the analysis phase. For
example, a high-frequency trading firm may not specify how
critical it is for transactions to complete within milliseconds, but the
architects in that problem domain know how important this is.


```
there are no
Dumb Questions
```

Q: What about important things like good internal structure that no one thinks to ask for?

A: Some implicit architectural characteristics are more subtle, but just as important. For example, architects should pay attention
to the application’s internal structure as developers create it, to ensure that sloppy coding and other deficiencies don’t degrade the
longevity of the application. However, virtually no requirements list will specify “Don’t mess up the internal modularity of the system as
you build it!” or “Make sure the software is maintainable!”



50  Chapter 2

<a id='p87'></a>
<!-- Página 87 -->

```
architectural characteristics



```

The International Zoo of “-ilities” Think this is a big list? Check
```
out https://iso25000.com/
```

Like the animals in a zoo, architectural characteristics exist index.php/en/iso-25000along a broad spectrum. Just as animals range from primates to standards/iso-25010.
reptiles, architectural characteristics range from low-level code scalab ilit y access ibilit y
characteristics, such as modularity, to sophisticated operational obser vabilit y
```
availab ilit y mainta inabili t y
```

concerns, such as scalability and elasticity. Unfortunately, there is testab ilit y
```
interop erabili t y reusab ilit y
```

no “universal list” of architectural characteristics, nor are there any portab ilit y
```
securit y simplic it y
```

real standards for what many of these terms mean (although people fe asibilit y
```
stabili t y reliabi lit y
```

have tried). Instead, each organization interprets these terms for usabili t y
```
agilit y
```

itself. integr it y perfor mance
```
trace abilit y localiz abilit y audita bilit y
```

Additionally, the software ecosystem is constantly adding new
concepts, terms, measures, and verifications, providing new This is not the
opportunities to define even more architectural characteristics. complete list. There
```
is no complete list!
Sam: We’re supposed to define architectural
characteristics for Lafter, but I can’t seem to find a
standard list anywhere.
Alex: Gosh, there are so many possibilities...
Mara: That’s why I like to categorize them. Remember
the old zoo maps that broke the zoo into “houses” and
“enclosures” for each type of animal? That same kind of
categorization can work here. It’s sort of like the genus
and species of architectural characteristics.
Process enclosure
“Ladies
and gentlemen, boys Operational
and girls, children of
```

all ages—welcome to house
the International Zoo
```
of ‘-ilities’!”




Structural
pen Cross-cutting savannah

you are here 4  51
```


<a id='p88'></a>
<!-- Página 88 -->

process characteristics



Process architectural characteristics
Process architectural characteristics are where the software
development process intersects with software architecture. They reflect the
decisions about the mechanics of building software.


```
modularity
The degree to which the testability
software is composed How complete the system’s
of discrete components. testing is and how easy these
Modularity affects how tests are to run, including unit, “Testability” refers
architects partition functional, user acceptance, and to testing at
behavior and organize exploratory tests. development time
logical building blocks. (such as unit testing),
rather than formal
quality assurance.
agility
A composite architectural
characteristic that encompasses
Agility is a composite testability, deployability,
Look out for this on the
architectural characteristic modularity, and a host of other
next page. Many architectural
we’ll discuss later in this architectural characteristics
characteristics cut across
chapter—stay tuned! that facilitate and enable agile
categories, as you’ll see in the
software development practices.
next few pages.

extensibility
How easy it is for developers
deployability to extend the system. This
How easy and efficient it is to may encompass architectural
deploy the software system. structure, engineering
practices, internal design, and
```

This is one of the many governance.
architectural characteristics
that make up “agility.”
```
decouple-ability
Coupling describes how parts of the Yes, we know this is a madesystem are joined together. Some up word. That happens a lot
architectures define how to decouple in software architecture!
parts in specific ways to achieve certain
benefits; this architectural characteristic
measures the extent to which this is
possible in a software system.

```

52  Chapter 2

<a id='p89'></a>
<!-- Página 89 -->

```
architectural characteristics



```

Structural architectural characteristics
Structural architectural characteristics affect the internal structure of the
software system, including factors like the degree of coupling between
components and the relationships between different integration points.



```
Security appears in every
security application, as an implicit
How secure the system is, or explicit architectural
holistically. Does the data characteristic.
need to be encrypted in the
database? How about for maintainability
network communication How easy it is for architects and
between internal systems? developers to apply changes to
What type of authentication enhance the system and/or fix
needs to be in place for bugs.
remote user access?

Portability can apply to any
part of the system, including
the user interface and
This is one of those implementation platform.
characteristics that belong portability
to more than one category. How easy it is to run
the system on more
than one platform (for
extensibility example, Windows
How easy it is for developers and macOS).
to extend the system. This
may encompass architectural
structure, engineering
practices, internal design, and
governance.
localization
Some architectural How well the system
characteristics cover supports multiple languages,
development concerns rather units of measurement,
than purely domain concerns. Another flavor currencies, and other
of localization is factors that allow it to be
internationalization used globally.
(i18n).




you are here 4  53
```


<a id='p90'></a>
<!-- Página 90 -->

operational characteristics



Operational architectural characteristics
Operational architectural characteristics represent how architectural decisions
influence what operational team members can do.



```
availability
What percentage of the time the
system needs to be available and, if
24/7, how easy it is to get the system
up and running quickly after a failure.
recoverability
How quickly the system can
get online again and maintain
Usually represented as a business continuity in case of
number of “nines” (99.999% a disaster. This will affect the
uptime = 5 nines, a bit A good example of the backup strategy and requirements
under 6 minutes/year). axiom that you can take any for duplicated hardware.
adjective and add “-ility”
to make a new architectural
characteristic!
robustness
The system’s ability to
handle errors and boundary
conditions while running, performance
such as if the power, internet How well the system
connection, or hardware fails. achieves its timing
requirements using the
available resources.
As you will see shortly,
“performance” has many
When these are different aspects.
important, they are very
important.

reliability/safety Some “-ilities” are easier to
achieve than others. This
Whether the system needs to be
fail-safe, or if it is mission critical
one is often difficult.
in a way that affects lives. If it fails,
will it endanger people’s lives or cost scalability Our Lafter
the company large sums of money? How well the system application
Common for medical systems, hospital performs and operates as will definitely
software, and airplane applications. the number of users or need this!
requests increases.



```

54  Chapter 2

<a id='p91'></a>
<!-- Página 91 -->

```
architectural characteristics



```

Cross-cutting architectural characteristics
As much as we’d like a nice, orderly zoo of architectural characteristics,
platypuses still show up! Lots of important characteristics defy
categorization. This is on e of
```
architectural chthose
security that are always aracteristics
How secure the system is, happens to be a present. It also
holistically. Does the data concern. cross-cutting
need to be encrypted in the
database? How about for
network communication
between internal systems?
What type of authentication legal
needs to be in place for remote How well the system
user access? complies with local laws
```

Authentication about data protection and
and authorization about how the application
are aspects of should be built or deployed.
security.
```
authentication/authorization
How well the system ensures users are who they say
they are and makes sure they can access only certain privacy
functions within the application (by use case, subsystem, How well the system
web page, business rule, field level, etc.). hides and encrypts
transactions so that
internal employees
Many countries and regions like data operators,
have strict laws governing architects, and
```

Many government agencies privacy, making consistency developers cannot see
around the world require a for international them.
baseline level of accessibility. applications tricky.


```
accessibility
How easy is it for all your usability
users to access the system,
How easy is it for users
including those with
This is a great example of
to achieve their goals. Is
disabilities, like colorblindness
how ambiguous architectural
training required? Usability
or hearing loss.
characteristics can be:
requirements need to be
“usability” can also refer to
treated as seriously as any
user experience design.
other architectural issue.



you are here 4  55
```


<a id='p92'></a>
<!-- Página 92 -->

defining characteristics




```
Who Does What
```

So many architectural characteristics! We had a nice database that listed the ones that are most important for
Lafter, along with their definitions, but somehow the index became corrupted and we lost the linkage. Can you
help restore them by drawing a line from each architectural characteristic to its definition?


```
Describes how well the components in the system create well-defined
scalability groupings and boundaries between components.




The system’s ability to recover from problems such as a power, internet
deployability connection, or hardware failure.




How easy is it for all users to access the system, including those with disabilities
modularity like colorblindness or hearing loss.




How easy it is for architects and developers to apply changes to enhance the
robustness system and/or fix bugs.




Describes how well the system handles a large number of concurrent
accessibility users while maintaining reasonable performance.




Describes the cadence, efficiency, and reproducibility of deployments.
maintainability


Solution on page 74

```

56  Chapter 2

<a id='p93'></a>
<!-- Página 93 -->

```
architectural characteristics




there are no
Dumb Questions
```

Q: Where can I find a standard list of architectural Q: Can I choose any combination of architectural
characteristics? characteristics for my application?

A: No standard list really exists (despite several futile efforts)
because the software development ecosystem constantly shifts
```
A: Some architectural characteristics oppose one another. For
example, architects find it challenging to design for both high
```

and changes. Anyone trying to create a standard list is trying to hit performance and scalability. Determining the most important
a moving target. architectural characteristics for a system is only part of the design

Q: process. Combining them with logical component design will point
```
Isn’t security required for every application? you to an appropriate architectural style.


```

A: It depends! While it’s a common concern, if you design a free
```
Q: What does it mean if you don’t choose an architectural
```

intra-office lunch-ordering system, the only security concern lies characteristic like availability in your requirements?
with others finding out that you order an egg salad sandwich every
day. A: The architectural characteristics you choose provide a

Q: guideline for the appropriate architectural style. If an architect
```
Doesn’t every application require availabilty? doesn’t choose availability, it doesn’t mean they will purposefully
design the system to have poor availability. Rather, it’s an
```

A: You guessed it—it depends! Again, availability is a common
concern for most applications, but if the mythical sandwich-
```
indication of priority: trading off one architectural characteristic for
another.
```

ordering system mentioned above fails, the only real downside is
that everyone has to get their own lunch.




```
you are here 4  57
```


<a id='p94'></a>
<!-- Página 94 -->

prioritizing characteristics




```
Exercise
```

Welcome to “Take It or Leave It!” The rules of this game are simple—we’ll give you a business requirement that might
come up for the Lafter application, and two architectural characteristics. As you know, everything in architecture is a
trade-off, so if you attempt to optimize one, you probably won’t do as well with the other. Your job is to tell us which
characteristic you rate as a higher priority for that requirement. You’ll find our thoughts at the end of the chapter.


“We need to get this to market ASAP!” fault tolerance agility


“Money’s tight, folks!” scalability simplicity


“Oh, wow, this conference is going to be our biggest yet.” high availability maintainability


“We want to start storing users’ credit card information.” security recoverability


“This site is going to be very popular upon launch.” agility elasticity


```
Solution on page 75




Geek Note
```

The software architecture world lacks a standard term for what we call architectural characteristics. Here are some of
the terms people often use, and why we don’t care for them.
Most teams still call them nonfunctional requirements, which is misleading because architectural characteristics
are indeed functional—they just don’t concern the domain. Calling them nonfunctional downplays their
importance. Other teams call them system quality attributes, which implies an activity that happens at the end of the
project rather than the beginning. Another common name is cross-cutting requirements, which is the one we dislike
the least—but it contains the word requirement, which entangles it with domain behaviors, which come from
requirements, as opposed to capabilities, which are defined by architectural characteristics.




58  Chapter 2

<a id='p95'></a>
<!-- Página 95 -->

```
architectural characteristics




I see that there are lots of
architectural characteristics...
but how do I know which ones are
critical or important to my project?




Architectural characteristics don’t just appear out
of thin air. In fact, there are three different sources from which you
should look to derive them.


1 The problem domain
Part of your job is analyzing a problem to determine what
architectural characteristics the system requires. Many structural
design decisions come directly from the problem domain.


2 Environmental awareness
Many requirements come from having a good understanding of
the environment in which you’re operating. For example, are you
working for a fast-moving startup, or a large enterprise with a lot at
stake?
at some tics
```

Recall tchtural characterislicit 3 Holistic domain knowledge
archite licit.” Many impfrom
are “imp eristics emerge Sure, you’re working with a particular problem domain—but we
charact wo sources. can assure you that the domain is a lot bigger than your particular
these t focus. Let’s say you’re building out a payment system. While
```
understanding what’s required of you is important, you’ll reveal
architectural characteristics if you understand the financial world,
finance industry regulations, and customers’ habits.


Let’s look at each of these sources in turn.




you are here 4  59
```


<a id='p96'></a>
<!-- Página 96 -->

sources of characteristics



Sourcing architectural characteristics from
the problem domain
Architects derive many of the necessary architectural characteristics from the
problem domain—it is, after all, the motivation for writing the software in
the first place. That means you must translate the items stated in requirements
documents into their corresponding architectural characteristics. For example,
the Lafter requirements specify “thousands of users.” As an architect, you must
dig deeper to more accurately determine how many users are expected (scalability),
how many of them will be there at the same time (concurrency), and how rapidly
they’ll show up (elasticity).




```
Exercise
Domain requirements are often a rich source of architectural characteristics. For example, our Lafter application
needs to support large numbers of users, so scalability will be one necessary characteristic. Can you uncover
more? Here are the requirements again:
Users: hundreds of speakers, thousands of users
Requirements: Architectural characteristics

Scalability
Users can register for usernames and approve the privacy policy
Users can add new content on Lafter as a “Joke” (long-form
post) or “Pun” (short-form post)
Followers can “HaHa” (indicating strong approval) or “Giggle”
(a milder approval message) content they like
Speakers at Sillycon Symposia events have a special icon
Speakers can host forums on the platform related to their content
Users can post messages of up to 281 characters
Users can also post links to external content
Additional Context:
International support
Very small support staff
“Bursty” traffic: extremely busy during live conferences
Solution on page 76



```

60  Chapter 2

<a id='p97'></a>
<!-- Página 97 -->

```
architectural characteristics



```

Sourcing architectural characteristics
```
from environmental awareness
```

You know a lot about where you work (maybe too much, in some cases!), and
```
Sorry, but this mean
going to have to starst yopau’re
```

that will naturally drive your architectural characteristics analysis. For example,
```
attention in those businesying
```

an architect working for a fast-moving startup will prioritize agility whether it is
```
prioritization meetings! s
```

specified or not.
It is important to understand organizational priorities so we can make more
durable decisions. For example, let’s say we must decide how to integrate two
subsystems. The choices are a customized but highly suited protocol or an
industry-standard protocol that will require a little more effort. In a vacuum, we
might choose the first. However, if we know that the organization’s goal is to
engage heavily in mergers with other companies, that fact could tip our decision
toward the more open solution.
```
Some architects stay within
Architects can’t make particular domains exactly
decisions in a vacuum— because they have the
context is always important. advantage of domain knowledge.
Sourcing architectural characteristics
from holistic domain knowledge
You have also no doubt absorbed a lot of domain knowledge: information
that isn’t explicitly spelled out in the requirements but that you implicitly
understand about important aspects of the domain.
Suppose Lafter has decided to run a promotion at a local university to
entice students to sign up (they go to a lot of conferences, and some of them
have a sense of humor). We need to design an application that handles signups for the promotion day. To make the math easy, assume that the school
has 1,000 students and they have 10 hours to sign up. Should we design the
system using a consistent scale, implicitly assuming that the students will
distribute themselves evenly during the sign-up process? (Have we met any
Never underestimate some university students?)
university students’ ability Based on real-world experience, we can guess that this won’t work. Think
to procrastinate. about what you know about the target demographic. Some students
are hyperdiligent; some tend to procrastinate. Thus, the actual design
must handle an elastic burst of students in the first hour (as the Type A
One of the most individuals rush to get in line), stay mostly idle for the bulk of the day, and
dangerous discoveries in then handle another elastic burst just before the sign-up window closes, to
life is how much you can accommodate all the stragglers.
procrastinate and still Architects must make use of all available information sources to understand
(mostly) get the job done. the full range of trade-offs inherent in our architectural decisions.


you are here 4  61
```


<a id='p98'></a>
<!-- Página 98 -->

solutions or requirements



```
Solutions versus requirements
Customers often come to architects with solutions rather than requirements. For

```

Watch it!
```
example, back in the 1970s, the US Air Force commissioned a fighter jet and included
a requirement that it be capable of achieving speeds up to Mach 2.5. The designers
tried, but the technology of the time just wasn’t sufficient to meet the requirement. They went
back to the Air Force and asked: “Why does it need to go Mach 2.5?” The answer was, “Well,
these things are expensive, so we want it to be able to flee a fight if necessary.” With that
knowledge in mind, they went back and designed the F-16 fighter jet. It had a maximum speed of
Mach 2.1, but it was the most maneuverable and fastest-accelerating jet ever created.
When users bring us solutions rather than requirements, it’s architects’ job to imitate an annoying
toddler and keep asking “But why?!?” enough times to uncover the actual requirements hidden
within the solutions.




Exercise
It’s sometimes difficult to distinguish requirements from solutions. Here are some responses you might get
when you ask “why?” that could indicate something might be one or the other. Can you identify which indicate
requirements and which solutions?

```

“We need a system to track user preferences and customizations, then save them between sessions.”
```
requirement solution
```

“Do we really need to build our own survey service? Surely we can find one that does what we need.”
```
requirement solution

```

“An enterprise service bus would solve some of our current problems (albeit with some changes and work-
```
arounds) and it offers extreme extensibility.”
requirement solution

```

“According to the friendly sales rep, this software package does all the things accounting needs, now and in the
```
near future.”
requirement solution

Solution on page 77


```

62  Chapter 2

<a id='p99'></a>
<!-- Página 99 -->

```
architectural characteristics



```

Composite architectural characteristics
Alex: The business analyst asked if we can make sure
the system is “reliable.” What do they mean?
Sam: Wow, I can think of a lot of ways to define
“reliable” for a piece of software.
Mara: This happens a lot. A composite is a
combination of two or more things, and often
architectural characteristics combine with each
other to create (seemingly) new ones. We call these Average response
composite architectural characteristics. Maximum response time
```
time
```

What does reliable mean? We can measure many
different aspects of reliability, like how available the
system is, how consistent the user interface workflows
are, and how well it handles data integrity.
Alex: How do I identify these?
Mara: To identify composites, ask: “Can I
```
t contentful
Firs
```

objectively measure this architectural characteristic?”
```
paint
```

While we often discuss performance as a single value, Total blocking time
it’s actually a composite—because we have to be …is composed of…
more specific to get to something measurable. An
example of a measurable architectural characteristic
is first contentful paint, which measures the time it takes Performance
for a web page to load on a mobile device.


```
…is composed of…
Usability




you are here 4  63
```


<a id='p100'></a>
<!-- Página 100 -->

concerning context



Priorities are contextual
It’s impossible to choose the same set of architectural characteristics for
every project. The set of architectural characteristics you choose for a
particular application, and how you prioritize each one, will differ based
on context.




```
Sharpen your pencil
Context matters. At the top, we’ve listed several architectural characteristics. Below that
are three application scenarios. For each scenario, rank each characteristic based on how
```

important it is for that type of application. Hint: Some applications won’t need all of them.

```
Scalability Performance

Extensibility

Security
Data integrity



Scenario #1 Scenario #2 Scenario #3
```

An ecommerce site in a A system for an enterprise An application to
competitive market whose goal is to grow via automate standardized
```
mergers testing and grading for
university admissions

```

1 1 1

2 2 2

3 3 3

4 4 4

5 5 5

```
Solution on page 78

```

64  Chapter 2

<a id='p101'></a>
<!-- Página 101 -->

```
architectural characteristics




Wait a minute. None of
```

the Lafter subject matter experts
```
knows what “scalability” and
```

“elasticity” are. How are they going
```
to know to ask for this stuff?




```

Congratulations, you have yet another job.
You’re right to be skeptical about how sophisticated an understanding your
coworkers have of architectural concepts. That means you have one more
job as an architect: translation!
As much as it would be nice for our colleagues to learn our language,
architects are generally the ones who have to translate the business’s goals
into identifiable and measurable architectural characteristics.




```
you are here 4  65
```


<a id='p102'></a>
<!-- Página 102 -->

translating requirements



Lost in translation
It’s not unusual for business experts and analysts to state (or subtly
suggest) a requirement without realizing it, hidden in plain English. It’s
your job, as a software architect, to read between the lines, find the
requirements, and translate them into architectural characteristics. Here
are a few examples.




```
When business analysts and Software architects
subject matter experts say: translate:
Good modularity
• Agility allows for faster
“Lafter is constantly changing to meet new change without
marketplace demands.”
• Modularity rippling side effects.
• Extensibility

• Performance We must perform well
“Due to new regulatory requirements, we must
• Recoverability
but also recover quickly
complete end-of-day processing on time.” in case of error.
• Scalability

• Résumé-ability “The ability to update your
“Our plan is to engage heavily in mergers and résumé.” Many people would
• Integratability
acquisitions in the next three years.” rather not work in a place
• Interoperability undergoing constant mergers.

• Feasibility More of an
“We have a very tight time frame and a fixed
• Simplicity architect-thescope and budget for this project.” person characteristic.
```

Of course, no • Affordability
one would Feasibility—evaluating
ever ask for Architects often
```
whether something have a unique
```

this impossible is possible—is an
combination... perspective of
```
underutilized what’s possible within
```

ahem. architecture “-ility.” a given time frame.


66  Chapter 2

<a id='p103'></a>
<!-- Página 103 -->

```
architectural characteristics




Not only do my business
```

analysts not understand the
technical terms for architectural
characteristics, they ask for way
```
too many things!




```

More requirements are NOT better.
What happens when an architect takes a list of possible architectural
characteristics for Lafter to a group of business users and asks them,
“Which of these do you want for the system?”
They invariably answer: “All of them!”
As nice as it would be to be able to accommodate that request, it’s not a
good idea to try.
Remember, architectural characteristics are synergistic with each other
and with the problem domain. That means the more architectural
characteristics the system must support, the more complex its
design must be.
When undertaking structural design for a system, architects must find a
balance between domain priorities and the architectural characteristics
necessary for success.




```
you are here 4  67
```


<a id='p104'></a>
<!-- Página 104 -->

characteristics and logical components



Architectural characteristics and logical components
Before we tell you how to go about trying to balance architectural characteristics with
each other and the domain, we want to show you how architectural characteristics and
logical components are two sides of the same coin. You see, both of them aim to support
the problem domain (also known as the reason you are writing software to begin with).




```
Architectural characteristics ≈ capabilitie s
Architectural characteristics describe the kinds of capabilities your solution will support,
rather than the behavior of the application, which is based on requirements.




Logical components = behavior
Logical components, covered in depth in Chapter 4, represent
the design of the system you are attempting to implement in
software in order to solve the fundamental problem at hand.




```

68  Chapter 2

<a id='p105'></a>
<!-- Página 105 -->

```
architectural characteristics



```

Balancing domain considerations and architectural characteristics
Architects use architectural characteristics and logical component analysis to determine the
appropriate architectural style, and the Lafter application is no exception. You need to strike a
balance between the two.

```
Imagine the left side to be domain
considerations and the right side to be
architectural characteristics.

No architectural characteristics
Sometimes we don’t take the time to analyze architectural characteristics before
designing the system, leading to expensive and time-consuming rework as we
discover that our system fails to exhibit the necessary architectural characteristics.


Projects that ignore
needed architectural
characteristics can Remember, architectural
deliver failure faster. characteristics are synergistic
with domain and other
architectural characteristics.
```

Good balance between… …architectural
In this scenario, we have achieved a characteristics and
balance in our design decisions between domain considerations
architectural characteristics and domain
considerations. This allows us to achieve operational and
```
structural goals without overengineering.




Too many architectural characteristics
Unfortunately, architects sometimes retreat to an ivory tower and spend
too much time analyzing architectural characteristics, or identifying
too many of them to be useful. This leads to overengineering, wasting
time and effort that could be spent on implementation and ongoing
maintenance.
Many systems that try to
support too many architectural
characteristics end up with too
little space left to support the
domain.

you are here 4  69
```


<a id='p106'></a>
<!-- Página 106 -->

narrowing it down



Limiting architectural characteristics
When the business stakeholders want all of the possible architectural
characteristics, how can you limit their enthusiasm?



The magical number 7
One useful guideline for the conversation between architects and “The Magical N
business analysts is to limit the number of architectural Plus or Minus Tumber Seven,
characteristics they can choose to seven. Why seven? Limits on Our wo: Some
Psychological research indicates that people remember items in chunks Capacity for
```
Processing Inform
```

of seven (one of the reasons that early phone numbers were seven famous paper f ation” is a
digits). It’s also large enough to provide some variety without creating a psychologist Georom 1956 by
paradox of choice by offering too many. rge Miller.
We created a worksheet to help architects work with other stakeholders
to arrive at a reasonable number. This is a demo; you’ll get to use it on
the next page.

Once you’ve settled on the most
important driving characteristics,
you get to pick three. Just put Driving characteristics are
```
Implicit characteristics become
```

1,2, and 3 next to the ones that architectural characteristics that
```
driving characteristics if they
matter the most to you. drive important design decisions.
influence structural decisions.

Top 3 Driving Characteristics Implicit Characteristics
feasibility (cost/time)
security

maintainability

observability

We’ve found these four to
be pretty common implicit
characteristics. Feel free to
replace these with whatever makes
sense for you.



```

70  Chapter 2

<a id='p107'></a>
<!-- Página 107 -->

```
architectural characteristics


```

Sharpen your pencil
```
On page 60, you identified architectural characteristics for Sillycon Symposia’s social media
application, Lafter. To make sure you’ve achieved a good balance, limit your list to seven
characteristics. Then, check the boxes next to the top three most important.

```

Top 3 Driving Characteristics Implicit Characteristics

```
feasibility (cost/time)
security

maintainability

observability
These are implied characteristics. Move
them to the Driving Characteristics
column if you think they are critical to
the success of the system.



Pick the top three most important ones (in any order).


```

Possible Candidate Architectural Characteristics

```
performance data integrity deployability
responsiveness data consistency testability
availability adaptability configurability
fault tolerance extensibility customizability
scalability interoperability recoverability
elasticity concurrency auditability

Solution on page 79



you are here 4  71
```


<a id='p108'></a>
<!-- Página 108 -->

chapter summary




Bullet Points
 Architectural characteristics represent one part of  Some architectural characteristics may appear in
```
the structural analysis that architects use to design multiple categories.
software systems. (We’ll talk abou the other part,
 Many architectural characteristics are cross-cutting:
logical components, in Chapter 4.)
they interact with other parts of (and decisions in) the
```

 Architectural characteristics describe a system’s organization.
```
capabilities.
 Architects must derive many architectural
```

 Some architectural characteristics overlap with characteristics from requirements and other domain
```
operational concerns (such as availability, scalability, design considerations.
and so on).
 Some architectural characteristics come from domain
```

 There are many catagories of architectural and/or environmental knowledge, outside of the
```
characteristics. No one can make a comprehensive requirements of a specific application.
list, because the software development ecosystem is
 Some architectural characteristics are composites:
constantly changing.
they consist of a combination of other architectural
```

 When identifying architectural characteristics, characteristics.
```
architects look for factors that influence structural
 Architects must learn to translate “business speak”
design.
into architectural characteristics.
```

 Architects should be careful not to specify too
```
 Architects should limit the number of architectural
many architectural characteristics, because they are
characteristics they consider to some small number,
synergistic—changing one requires other parts of the
such as seven.
system to change.
```

 Some architectural characteristics are implicit: not
```
explicitly stated in requirements, yet part of an
architect’s design considerations.




```

72  Chapter 2

<a id='p109'></a>
<!-- Página 109 -->

```
architectural characteristics



Characteristics Crossword
Ready to have some fun and test your knowledge about
what you’ve learned? Try this crossword puzzle about
architectural characteristics.




```

Across Down
3. An architectural characteristic that might be implicit 1. Uneven traffic often comes in _____
4. _____ engineering is an architectural problem 2. A Lafter post can be a “joke” or a “_____”
8. Choosing architectural characteristics means assigning each 3. Architectural characteristics influence the system’s _____
one a _____ 5. Architectural characteristics can be explicit or _____
9. Magic number of characteristics to ask for 6. _____ integrity is an architectural characteristic
11. A nonfunctional requirement is also called an architectural 7. A site with large numbers of _____ users might need to be
_____ scalable
15. Some architectural characteristics are _____-cutting 10. Many governments regulate data _____
17. What architects should ask when users suggest solutions 12. An architectural characteristic is critical or important to the
instead of requirements system’s _____
18. A system might need to _____ up and down to meet demand 13. Combining architectural characteristics and logical
19. _____ tolerance is an architectural demand components gives you an architectural _____
```
14. The thing you’re writing software about
16. Web page loading time is often called “first contentful _____”

Solution on page 80

you are here 4  73
```


<a id='p110'></a>
<!-- Página 110 -->

exercise solutions


```
From page 56

Who Does What
Solution
```

So many architectural characteristics! We had a nice database that listed the ones that are most important for
Lafter, along with their definitions, but somehow the index became corrupted and we lost the linkage. Can you
help restore them by drawing a line from each architectural characteristic to its definition?


```
Describes how well the components in the system create well-defined
scalability groupings and boundaries between components.




The system’s ability to recover from problems such as a power, internet
```

deployability connection, or hardware failure.




```
How easy is it for all users to access the system, including those with disabilities
```

modularity like colorblindness or hearing loss.




```
How easy it is for architects and developers to apply changes to enhance the
robustness system and/or fix bugs.




Describes how well the system handles a large number of concurrent
```

accessibility users while maintaining reasonable performance.




```
Describes the cadence, efficiency, and reproducibility of deployments.
```

maintainability




74  Chapter 2

<a id='p111'></a>
<!-- Página 111 -->

```
architectural characteristics


From page 58
Exercise
Solution
```

Welcome to “Take It or Leave It!” The rules of this game are simple—we’ll give you a business requirement that might
come up for the Lafter application, and two architectural characteristics. As you know, everything in architecture is a
trade-off, so if you attempt to optimize one, you probably won’t do as well with the other. Your job is to tell us which
characteristic you rate as a higher priority for that requirement.


“We need to get this to market ASAP!” fault tolerance agility


“Money’s tight, folks!” scalability simplicity


“Oh, wow, this conference is going to be our biggest yet.” high availability maintainability


“We want to start storing users’ credit card information.” security recoverability


“This site is going to be very popular upon launch.” agility elasticity




```
you are here 4  75
```


<a id='p112'></a>
<!-- Página 112 -->

exercise solutions


```
From page 60
Exercise
Solution
```

Domain requirements are often a rich source of architectural characteristics. For example, our Lafter application
needs to support large numbers of users, so scalability will be one necessary characteristic. Can you uncover
more? Here’s what we came up with.

```
Users: hundreds of speakers, thousands of users Architectural characteristics
Scalability
Requirements:
Users can register for usernames and approve the privacy policy
Users can add new content on Lafter as a “Joke” (long-form Elasticity
post) or “Pun” (short-form post)
Followers can “HaHa” (indicating strong approval) or “Giggle” Authorization
(a milder approval message) content they like
Speakers at Sillycon Symposia events have a special icon Authentication
Speakers can host forums on the platform related to their content
Internationalization
Users can post messages of up to 281 characters
Users can also post links to external content Customizability
Additional Context:
International support
Very small support staff
“Bursty” traffic: extremely busy during live conferences




```

76  Chapter 2

<a id='p113'></a>
<!-- Página 113 -->

```
architectural characteristics


From page 62
Exercise
Solution
```

It’s sometimes difficult to distinguish requirements from solutions. Here are some responses you might get when
you ask “why?” that indicate something might be one or the other. Can you identify which indicate requirements
and which solutions?


“We need a system to track user preferences and customizations, then save them between sessions.”

```
requirement solution
```

“Do we really need to build our own survey service? Surely we can find one that does what we need.”

```
requirement solution
```

“An enterprise service bus would solve some of our current problems (albeit with some changes and workarounds)
and it offers extreme extensibility.”

```
requirement solution
```

“According to the friendly sales rep, this software package does all the things accounting needs, now and in the near
future.”

```
requirement solution




you are here 4  77
```


<a id='p114'></a>
<!-- Página 114 -->

exercise solutions



```
Exercise From page 64

Solution
Context matters. At the top, we’ve listed several architectural characteristics. Below that are three application
scenarios. For each scenario, rank each characteristic based on how important it is for that type of application.
Hint: Some applications won’t need all of them. Here are our rankings.

Scalability Performance

Extensibility

Security
Data integrity



Scenario #1 Scenario #2 Scenario #3
```

An ecommerce site in a An application to
```
A system for an enterprise automate standardized
```

competitive market whose goal is to grow via testing and grading for
```
mergers university admissions

```

1 Security 1 Extensibility 1 Data integrity

2 Performance 2 Scalability 2 Security

3 Scalability 3 3 Performance

4 4 4

5 5 5




78  Chapter 2

<a id='p115'></a>
<!-- Página 115 -->

```
architectural characteristics



Exercise From page 71

Solution
```

On page 60, you identified architectural characteristics for the Sillycon Symposia Lafter social media application. To
make sure you have achieved a good balance, limit the number to seven. Then, check the boxes next to the top three
most important.


Top 3 Driving Characteristics Implicit Characteristics

```
Scalability feasibility (cost/time)
Security security
Elasticity maintainability
Responsiveness observability
Performance
Portability Remember, no
answer exists. Tsingle correct
Accessibility can you justify yohe question is:
ur choices?

Possible Candidate Architectural Characteristics

performance data integrity deployability
responsiveness data consistency testability
availability adaptability configurability
fault tolerance extensibility customizability
scalability interoperability recoverability
elasticity concurrency auditability




you are here 4  79
```


<a id='p116'></a>
<!-- Página 116 -->

exercise solutions



```
Characteristics Crossword Solution

From page 73




```

80  Chapter 2

<a id='p117'></a>
<!-- Página 117 -->

3 the two laws of software architecture
```
Everything’s a Trade-Off




What happens when there are no “best practices”? The nice thing about
best practices is that they’re relatively risk-free ways to achieve certain goals. They’re called
“best” (not “better” or “good”) for a reason—you know they work, so why not just use them? But
one thing you’ll quickly learn about software architecture is that it has no best practices. You’ll
have to analyze every situation carefully to make a decision, and you’ll need to communicate not
just the “what” of the decision, but the “why.”

So, how do you navigate this new frontier? Fortunately, you have the laws of software architecture to
guide you. This chapter shows you how to analyze trade-offs as you make decisions. We’ll also show
you how to create architectural decision records to capture the “hows” and “whys” of decisions. By the
end of this chapter, you’ll have the tools to navigate the uncertain territory that is software architecture.




this is a new chapter   81
```


<a id='p118'></a>
<!-- Página 118 -->

sneaker app requirements



It starts with a sneaker app
Archana works for Two Many Sneakers, a company with a very successful
mobile app where shoe collectors (“sneakerheads”) can buy, sell, and trade
collectible sneakers. With millions of shoes listed, customers can find the
shoes they really want or upload photos to help sell the ones they don’t.
The app’s initial architecture was a single service as shown below:
```
Two Many Sneakers’
slogan: You only have two
feet, but you can never
have too many sneakers!
The Two Many
Sneakers app talks to
the trading service.
This is the
database.
Trading
Service




The trading service, in turn,
talks to the database.


```

Two Many Sneakers Two Many Sneakers
mobile app backend




The Two Many Sneakers app knows to talk to the trading service to fetch
and update data (like a photo of a mint-condition pair of Nikes). The
trading service, in turn, fetches data and updates the database.
Business is booming. Sneakerheads are always willing to change up their
collections, and Two Many Sneakers’ customer base has grown quickly.
Now customers are demanding real-time notifications, so they’ll know
whenever someone lists a pristine pair of those Air Jordans they’ve been
pining for.




82  Chapter 3

<a id='p119'></a>
<!-- Página 119 -->

```
the two laws of software architecture




```

Security is always a concern in online sales. Nobody wants knockoffs, and credit
card numbers need to be protected. To stay a few steps ahead of any scammers,
Two Many Sneakers’ management team wants to prioritize improving the app’s
fraud detection capabilities. They plan to use data analytics to help detect fraud by
spotting anomalies in user behavior and filtering out bots.
Work has already begun—all the team needs to do now is set up the trading
service to notify the new notification and analytics services anytime something of
interest happens in the app. Piece of cake! I’ll just
```
use messaging to inform
the notification and
analytics services every
time a new pair of shoes
is listed on the app.
Genius!

The database is New Air Jordans just
still part of the got listed? Inform
architecture. We everyone interested
just left it out in with an update.
this diagram. Notification
Service
Trading
Service

Analytics
Service
Any and all trades
need to be sent to the
analytics service. Nobody
likes being scammed.




Archana




you are here 4  83
```


<a id='p120'></a>
<!-- Página 120 -->

knowns and unknowns



What do we know so far?
We need to figure out how these services will communicate with one
another. Let’s recap what we know (and don’t know) so far:



```
• The current architecture is rather simple—the Notification
trading service talks to its own database, and Service

that’s that. We need the trading service to send Trading
information to the notification service and the Service

analytics service. Analytics
Service




Notification
Service
• Word in the office is that there’s a chance that the finance
department (which is responsible for compliance) will want Trading
Service
updates from the trading service. In other words, whatever
architecture we come up with will need to be extensible. Analytics
Service



What does finance need to
know? Will this even happen? ???




• We don’t know what data to send the notification and {
analytics services—do the two services get the same "sellerId": 12345,
kind of data, or wildly different data? And we don’t What should
know where things stand with finance, so that’s another
"buyerId": 6789, this look like?
unknown. "itemId": 1492092517,
"price": "$125.00"
}




```

To be clear, there are some things we know and plenty we don’t. As the system’s architects, we
Welcome to the world of software architecture. need to identify its architectural
Speaking of architecture, we’ll be done, say, next Thursday— characteristics. (You learned
right? about those in Chapter 2.)


84  Chapter 3

<a id='p121'></a>
<!-- Página 121 -->

```
the two laws of software architecture



Exercise
```

Which of the following architectural characteristics stand out as important for this particular problem? Hint: There
are no right answers here, because there is a lot we don’t know or aren’t sure of yet. Take your best guess—we’ve
provided our solution at the end of this chapter. We’ll get you started:
```
Lots of downstream
services need to know
about sneaker trades. modularity
extensibility This sounds important! upgradability

low coupling
security

```

performance
```
Solution on page 116


there are no
Brain Dumb Questions
Power
```

All the characteristics in the
previous exercise sound pretty
```
Q: Even this simple exercise seems to have a lot of moving parts. We
```

good, right? Seriously, who’d know some things, we think we know some other things, and there’s
say no to upgradability? a lot that we certainly don’t know. How do we go about thinking about
```
architecture?
```

But for each one, ask yourself—
is this characteristic critical to
the project’s success? Or is it a
```
A: You’re right. In almost all real-life scenarios, your list of architectural
characteristics will probably contain a healthy mix of “this is what we want”
```

nice-to-have?
```
and “this is something we might want.” Even your customers can’t answer the
```

What’s more, some question of what they will eventually want. (Wouldn’t that be nice?) This is the
characteristics conflict. A “stuff you don’t know you don’t know,” also known as the “unknown unknowns.”
highly secure application with
```
It’s not unusual for an “unknown unknown” to rear its head midway through
```

loads of encryption and secure
connections probably won’t a project and derail even the best-laid plans. The solution? Embrace agility
be highly performant. Go back and its iterative nature. Realize that nothing, particularly software architecture,
and see if any of your choices remains static. What worked today might prove to be the biggest hurdle to
are at odds. If so, you can only success tomorrow. That’s the nature of software architecture: it constantly
pick one. evolves and changes as you discover more about the problem and as your
```
customers demand more of you.



Flashback to Chapter 2?
You bet it is!


you are here 4  85
```


<a id='p122'></a>
<!-- Página 122 -->

queues and topics



Communicating with downstream services
```
It’s OK if you don’t
```

Our goal is to get the trading system to notify the reporting and analytics systems know much about
automatically. For now, let’s assume we decide to use messaging. But that presents a messaging, queues, or
dilemma—should our messaging use queues or topics? topics. We’ll tell you
Before we go further, let’s make sure we’re on the same page about the differences
```
what you need to know.
```

between queues and topics. Most messaging platforms offer two models for a publisher
of a message (in this case, that’s the trading service) to communicate with one or more
consumers (the downstream services).
The first option is a queue, or a point-to-point communication protocol. Here, the
```
If it helps, think of
```

publisher knows who is receiving the message. To reach multiple consumers, the publisher
```
queues as being like
```

needs to send a message to one queue for each consumer. If the trading service wants to use
```
a group text—you
```

queues to tell the analytics service and the reporting service about trades, this is what the
```
pick everyone you
```

setup will look like:
```
This is a want to inform,
This is a message. consumer. type your message,
Notification and hit “send.”
Queue Service

Trading For every consumer, you
Service need a separate queue.
Analytics
Queue
Service

This is another Topics are similar to posting
consumer. a picture on your go-to
social networking site.
```

When using the second option, topics, you are signing on for a broadcasting model. Anyone following you will
The publisher simply produces and sends a message. If another service downstream see that picture, since
wants to hear from the publisher, it can subscribe to the topic to receive messages. they’ve “subscribed” to
The publisher doesn’t know (or care) how many services are listening. your timeline.

```
The publisher publishes a Notification
message to the topic. Service


Trading Topic Anyone interested in the messages
Service can subscribe to the topic.
The topic, in turn,
Analytics
notifies all subscribers. Service



```

Both options sound good—so how do we pick? Let’s find out.


86  Chapter 3

<a id='p123'></a>
<!-- Página 123 -->

```
the two laws of software architecture



```

Analyzing trade-offs
You can’t have your cake and eat it too. The world is full of
compromises—we often optimize for one thing at the cost of another.
Want to take and store lots of pictures on your phone? Either get more
storage, which costs more, or compress them, which lowers the image
quality.
Software architecture is no different. Every choice you make involves
```
If this sounds familiar, it
```

significant compromises or, as we like to call them, trade-offs. So
```
should be! It was part of
```

what exactly does this mean for you?
```
our discussion of significant
versus less-significant
```

If you know which architectural characteristics are most important trade-offs in Chapter 1.
to your project, you can start thinking of solutions that will maximize
some of those attributes. But if a solution lets you maximize one
characteristic (or more), it will come at the cost of other characteristics.
For example, a solution that allows for great scalability might also make
deployability or reliability harder.
No matter what solution you come up with, it will come with tradeoffs—upsides and downsides.
Your job is twofold: know the trade-offs associated with every solution
```
Rich Hickey, creator of the
```

you come up with, and then pick the solution that best serves the most
```
Clojure programming language,
```

important architectural characteristics.
```
once said, “Programmers know
the benefits of everything and
the trade-offs of nothing.”
We’d like to add: “Architects
need to understand both.”




You can’t have it all. You’ll have to decide
which architectural characteristics are
most important, and choose the solution
that best allows for those characteristics.




you are here 4  87
```


<a id='p124'></a>
<!-- Página 124 -->

queues and topics



Trade-off analysis: Queue edition
Trade-off analysis isn’t just about finding the benefits of a particular
```
Just a friendly reminder
```

approach. It’s also about seeking out the negatives to get the full picture.
```
of what using queues would
```

Let’s look at each option in turn, starting with queues.
```
look like, so you don’t have
to flip back and forth.
```

With queues, for every service that the trading service needs to notify,
we need a separate queue. If the notification service and the analytics
service need different information, we can send different messages to
each queue. The trading service is keenly aware of every system to which
it communicates, which makes it harder for another (potentially rogue)
service to “listen in.” (That’s useful if security is high on our priority list,
right?) Oh, and since each queue is independent, we can monitor them
separately and even scale them independently if needed.
The trading service is tightly coupled to its consumers—it knows exactly
how many there are. But we’re not sure if we’ll need to send messages
to the compliance service, too. If that happens, we’ll have to rework the
trading service to start sending messages to a third queue. In short, if we
choose queues, we’re giving up on extensibility.




```
Whiteboards are great for
Using Queues brainstorming trade-offs
Pros Cons with your team.
```

Heterogeneous - Supports heterogeneous - Higher degree
is just a fancy messages for different of coupling (hurts
way of saying consumers extensibility)
“different.” - Allows independent - Trading service must
```
monitoring and scaling connect to multiple
(helps scalability) queues
- More secure (improves - Requires additional
security) infrastructure




```

See what we mean when we say “trade-off analysis”?


88  Chapter 3

<a id='p125'></a>
<!-- Página 125 -->

```
the two laws of software architecture



```

Trade-off analysis: Topic edition
What about using topics? Well, the upside is clear—the trading service only
delivers messages to a topic, and anyone interested in listening for a message from
```
This is what using a
```

the trading service simply subscribes to that topic. Compliance wants in? They
```
topic looks like.
```

can simply subscribe: no need to make any changes to the trading service. Low
coupling for the win.
But topics have a few downsides, too. For one thing, you can’t customize the message
for any particular service—it’s a one-size-fits-all, take-it-or-leave-it proposition.
Scaling, too, is one-size-fits-all, since you have only one thing to scale. And anyone
can subscribe to the topic without the trading service knowing—which, in some
circumstances, is a potential security risk.
Back to the whiteboard!

```
Using Topics
Pros Cons
- Homogeneous message
- Low coupling (helps for all services
extensibility)
- Can’t monitor or scale
- Trading service only a topic independently
has one place to publish (hurts scalability)
messages
- Less secure (hurts
security)




Sharpen your pencil
Spend a few minutes comparing the results of our trade-off analysis. Notice how both options
support some characteristics but trade off on others? Now we’re going to present you with some
```

requirements—see if you can decide if you’d pick queues or topics to support each one.
```
Requirements
“Security is important to us.”
Queues / Topics
“Different downstream services need different kinds of information.”
Queues / Topics
“We’ll be adding other downstream services in the future.”
Queues / Topics

Solution on page 116

you are here 4  89
```


<a id='p126'></a>
<!-- Página 126 -->

the first law



The first law of software architecture
Queues or topics? Enough with the suspense already. The answer is—it depends!
What’s important to the business? If security is paramount, we should probably go
with queues. Two Many Sneakers is growing by leaps and bounds and has loads of
```
it dep
```

other services interested in its sneaker trades, so extensibility is its biggest priority. ends
That means we should pick the topic option.
Time is also a factor: if we need to get to market quickly, we might pick a simpler
architecture (simplicity) over one that offers high availability. (Having an application that
guarantees three “nines” of uptime only matters if you have customers, right?)
The key takeaway is that in software architecture, you’ll always be balancing trade-offs.
That leads us to the First Law of Software Architecture.

```
One of your authors
often sports this
T-shirt in public. (If
THE FIRST LAW you get any printed,
please send us one
OF medium and two
extra-large!)
```


## SOFTWARE


## E:


## ARCHITECTUR


## IN


## EVERYTHING


## SOFTWARE


## E


## ARCHITECTUR


## IS A


## TRADE-OFF

```
If you find a
decision in software
architecture that
```

In software architecture, nice, clean lines are rare and there are no “best practices.” doesn’t have a
Every choice you make will involve many factors—often conflicting ones. The First trade-off, you
Law is an important lesson, so take it to heart. Write it down on a sticky note and haven’t looked at
put it on your monitor. Get a backwards tattoo of it on your forehead so you’ll see it hard enough.
it in the mirror! Whatever it takes.



90  Chapter 3

<a id='p127'></a>
<!-- Página 127 -->

```
the two laws of software architecture



```

Sharpen your pencil
```
This time, we’d like you to do some trade-off analysis on your own. We chose messaging as the
communication protocol between our trading service and its consumers. Messaging is asynchronous.
```

Choosing between asynchronous and synchronous forms of communication comes with its own set of trade-offs!
We’ve given you two whiteboards, one for each form of communication, and we’ve listed a bunch of “-ilities.” We’d like
you to consider how each architectural characteristic would work in both contexts. Is this characteristic a pro or a con
(or neither) in synchronous communications? What about in asynchronous communications? Place each “-ility” in the
appropriate column. Hint: Not all of them apply to this decision. We put the first pro on the whiteboard for you. When
you’re done, you can see our answers at the end of the chapter.

```
transactions
responsiveness
error handling



consistency
coordination extensibility


deployability
fault tolerance




Using sync communications Using async communication
Cons Pros s
Pros
responsiveness Cons




Solution on page 117

you are here 4  91
```


<a id='p128'></a>
<!-- Página 128 -->

trade-off analysis



```
there are no
Dumb Questions
probably go through the process several times as you discover
```

Q: I’ve heard of the Architecture Tradeoff Analysis Method
```
more and more about the problem and come up with different
scenarios.
```

(ATAM). Is that what you’re talking about?

A: ATAM is a popular method of trade-off analysis. With ATAM,
you start by considering the business drivers, the “-ilities,” and
```
Another popular approach is the Cost Benefit Analysis Method
(CBAM). In contrast to ATAM, CBAM focuses on the cost of
achieving a particular “-ility.”
```

the proposed architecture, which you present to the stakeholders.
Then, as a group, you run through a bunch of scenarios to produce We recommend you look at both methods and perhaps consider
a “validated architecture.” While ATAM offers a good approach, combining them—ATAM can help with trade-off analysis, while
we believe it comes with certain limitations—one being that it CBAM can help you get the best return on investment (ROI).
assumes the architecture is static and doesn’t change.
```
Just remember—the process is not as important as the goal, which
```

Rather than focusing on the process of ATAM, we prefer to focus is to arrive at an architecture that satisfies the business’s needs.
on results. The objective of any trade-off analysis should be
to arrive at an architecture that best serves your needs. You’ll




It always comes back to trade-offs
Some people always pick a particular technique, approach, or tool regardless of the
problem at hand. Often they choose something they’ve had a lot of success with in the
past. Sometimes they have what we affectionately call “shiny object syndrome,” where
they think that some new technology or method will solve all their problems.
Regardless of past achievements or future promises, just remember—for every upside,
there’s a downside. The only questions you need to answer are “Will the upsides help
you implement a successful application?” and “Can you live with the downsides?”
Whenever someone sings the praises of a certain approach, your response should be:
“What are the trade-offs?”


```
To be clear, we aren’t say
you shouldn’t use new toolsingand
techniques. That’s progress, rig
Just don’t forget to consid ht?
trade-offs as you decide. er th e




```

92  Chapter 3

<a id='p129'></a>
<!-- Página 129 -->

```
the two laws of software architecture



```

Making an architectural decision You got it: we’re e
```
talking about thn
```

Debating the pros and cons with your team in front of a whiteboard is fun second dimensio
and all, but at some point, you must make an architectural decision. of software
We mentioned architectural decisions in Chapter 1, but let’s dive a little architecture.
deeper. As you architect and design systems, you will be making lots of
decisions, about everything from the system’s overall structure to what tools
and technologies to use. So what makes a decision an architectural decision?
In most cases, any choice you make that affects the structure of your system
is an architectural decision. Here are a couple of example decisions:

```
To jog your memory,
picking whether you’d
like a one- or twostory house would be an
architectural decision.
I believe we have
We will use a cache to reduce the load on a decision—we’re
the database and improve performance. going to split the
order shipping service
Notice how this decision introd s apart from the order
additional piece of infrastructuuce
re.
an tracking service.
also something the implementing tea It’s
must keep in the back of their min m
when accessing or writing data. ds


We will build the reporting service as a
modular monolith.


This one is pretty obvious—
it literally describes the As we put it in Chapter 1:
structure of a service. “Architectural decisions serve as
guideposts to help development teams
understand the constraints and
conditions of the architecture.”

```

Notice how these decisions act as guides rather than rules. They aid teams
in making choices, without being too specific. Most (but not all) of the
architectural decisions you’ll make will revolve around the structure of your
systems.




```
you are here 4  93
```


<a id='p130'></a>
<!-- Página 130 -->

architectural decisions



What else makes a decision architectural?
Usually, architectural decisions affect the structure of an architecture—are we going
with a monolith, or will we leverage microservices? But every so often, you might
decide to maintain a particular architectural characteristic. If security is paramount,
for example, Two Many Sneakers might make a decision like this:


```
We will use queues for asynchronous communication
Recall that topics are a
between services. broadcasting mechanism,
allowing any service to
subscribe and listen in on a
This decision isn’t about structure—it’s driven by the topic.
need for security. Since there’s a queue for every
subscriber, we know who the consumers are.
```

At other times, you might decide on a specific tool, technology, or process if it
affects the architecture or indirectly helps you achieve a particular architectural
characteristic. For example:


```
Perhaps you need to get to
```

We will use Node.js as the development framework for market quickly, or maybe you
the MVP. have a large pool of engineers
```
with expertise in this
MVP stands for “minimum viable product.” particular technology stack.

```

Everything in this chapter so far has led to this important moment—making an
architectural decision. You start with a trade-off analysis. Then you consider the
pros and cons of each option in light of other constraints, like business and end
user needs, architectural characteristics, technical feasibility, time and budgetary
constraints, and even development concerns. Then, finally, you can make a decision.




```
Geek Note
Michael Nygard, author of the book Release It! (Pragmatic Programmer), defines an architecturally significant
decision as “something that has an effect on how the rest of the project will run” or that can “affect the
structure, non-functional characteristics, dependencies, interfaces, or construction techniques” of the
architecture. To learn more, we recommend reading his blog post, “Documenting Architecture Decisions”
(https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions).




```

94  Chapter 3

<a id='p131'></a>
<!-- Página 131 -->

```
the two laws of software architecture




```

Hold up. Whiteboards are great,
but there has to be a more permanant
way of recording the trade-off analysis,
the decision, and most importantly, why
that choice was made. Whiteboards seem
```
awfully temporary, no?




You bring up several good points. It’s
important to record our decisions in a more permanent way. In
addition, trade-off analysis is an involved process. It’d be a real
waste if we lost all that work just because someone got a little hasty
with the eraser.
But you make another key observation: while the decision itself
is important, why we made that decision might be even more
important. Which leads us to...




you are here 4  95
```


<a id='p132'></a>
<!-- Página 132 -->

the second law



The second law of software architecture
Making decisions is one of the most important things software architects do.
Let’s say you and your team do a trade-off analysis and conclude that you’re going to
use a cache to improve your application’s performance. The result of your analysis is
that your system starts using a cache somewhere. The what is easy to spot.
That decision is important, but so are the circumstances in which you made the
decision, its impact on the team implementing it, and why, of all the options available
to you, you chose what you did.
This leads us to the Second Law of Software Architecture.




## THE SECOND LAW


## OF


## SOFTWARE


## ARCHITECTURE:


## WHY


## IS MORE


## IMPORTANT


## THAN


## HOW


You see, future architects (or even “future you”) might be able to discern what you did
and even how you did it—but it’ll be very hard for them to tell why you did it that way.
Without knowing that, they might waste time exploring solutions you’ve already rejected
for good reasons, or miss a key factor that swayed your decision.
This is why we have the Second Law. You need to understand and record the “why” of
each decision so it doesn’t get lost in the sands of time.
So how do we go about capturing architectural decisions? We’ll dive into that next.




96  Chapter 3

<a id='p133'></a>
<!-- Página 133 -->

```
the two laws of software architecture



```

Architectural decision records (ADRs)
Do you remember everything you did last week? No? Neither do we. This is why it’s
important to document stuff—especially the important stuff.
Thanks to the Second Law of Software Architecture, we know we need a way to
capture not just the decision, but the reason we made it. Architects use architectural We cannot emphasize
decision records (ADRs) to record such decisions because it gives us a specific enough how important
template to work with. keeping these records is.
An ADR is a document that describes a specific architectural decision. You write
one for every architectural decision you make. Over time, they’ll build up into an
architectural decision log. Remember that architectural decisions form the second
dimension to describe your architecture. ADRs are the documentation that supports
this dimension.


```
le a r c h it e ct ural decision
```

A sing ibes what
record descsr made and why. This log serves as a
decision wa Over time, you build the memory store
```
Title up a log of decision of your project,
records—one for every explaining how and why
Status decision. the project got to
where it is.
```

These Context
sections make
up an ADR. Decision over time leads to

```
Consequences
Governance
Notes Together, these
ADRs form the
Don’t worry if this “story” of your
is confusing now—we’ll architecture.
be diving into the
details in the next
few pages.

```

An ADR has seven sections: Title, Status, Context, Decision, Consequences,
Governance, and finally Notes. Every aspect of an architectural decision, including
the decision itself, is captured in one of these sections. Let’s take a look, shall we?




```
you are here 4  97
```


<a id='p134'></a>
<!-- Página 134 -->

writing ADRs



Cubicle conversation
```
Alex




Mara




Sam
Alex: Doing the trade-off analysis between queues and topics took it out of
me.
Mara: Me too. Trade-off analysis can be arduous, but I’m glad we got it
done. This is a big architectural decision. It’s crucial that we understand the
’re going
Guess what? Ytouhe team
pros and cons of every choice.

to be helping DR. Keep Sam: Yeah, yeah. So we decided to use queues, right? Now can we get back
write their A r those to programming?
an eye out fo Mara: Slow down a second. You’re right—we’ve made a decision. Now we
exercises. should record our decision in an ADR.
Sam: But why? We already know what we’re going to do. That seems like a
lot of work.
Alex: Look, we know why we chose to go with queues. It’s the option that
best supports the architectural characteristics we want to maximize in the
system, right?
Mara: Correct. But while we know why we made that decision, what about
anyone else who might come along and wonder why we chose queues over
topics, like future employees? That’s why we should record our thinking.
Sam: I can see that being useful.
Alex: Great! So can we start drafting our ADR?


```

98  Chapter 3

<a id='p135'></a>
<!-- Página 135 -->

```
the two laws of software architecture



```

Writing ADRs: Getting the title right Tit
```
le
Sta
```

Every ADR starts with a title that describes the decision. Craft this title tus
```
Co
nte
```

carefully. It should be meaningful, yet concise. A good title makes it easy to De xt
```
cis
```

figure out what the ADR is about, which is especially handy when you’re Co ion
```
nse
que
```

frantically searching for an answer! Go
```
ver nce
No n a s
tes nce
```

Let’s dive deeper into what a good ADR title looks like. Imagine a team is
writing a service that provides surveys to customers. They’ve done a trade-off
analysis and have decided to use a relational database to store survey results.
Here’s what their ADR title might look like:
```
there are no
These two pieces together Dumb Questions
make up the title.
042: Use relational store for customer survey service Q: What happens if we end up
writing more than 999 ADRs?

A three-digit
numerical prefix,
The title of the ADR A: That’s a lot of ADRs! If that were
to happen, you’d need to revise a bunch
followed by a colon of titles (and potentially filenames). In
our experience, a three-digit prefix is
```

The title should consist mostly of nouns. Keep it terse: you’ll have plenty
```
plenty.
```

of opportunities to go into detail later. It should describe what the ADR is
about, much like the headline of a news article or blog post. Get that right,
and the rest will follow.
```
Q: Can I reuse an ADR number?

```

The title should start with a number—we suggest using three digits, with
leading zeros where needed. This allows you to number your ADRs
```
A: Every ADR should get a unique
identifier. This makes it easier to
```

sequentially, starting with 001 for your first ADR, all the way to 999. Every reference them without confusion.
time you add a new ADR, you increment the number. This makes it easy for
anyone reading your records to know which decisions came before others.
```
More about this
the Status sectiown.hen we discuss

Exercise
In the following exercises, you’re going to help the team at Two Many Sneakers write an ADR. They’ve decided to
use asynchronous messaging, with queues between the trading service and downstream services. Assume this is
the 12th ADR the team is writing. What title would you give this ADR? Don’t forget to number it! Use this space to jot
down your thoughts. You can see what we came up with at the end of this chapter.




Solution on page 118

you are here 4  99
```


<a id='p136'></a>
<!-- Página 136 -->

the status section



Writing ADRs: What’s your status? Title
Great! You’ve settled on a descriptive title. Next, you’ll need to decide on the status of Status
your ADR. The status communicates where the team stands on the decision itself. Contex
```
t
Decisio
```

But wait—isn’t the point of the ADR to record a decision? Well, kinda. But making n
```
Conseq
```

decisions is a process. uences
```
Govern
ance
```

ADRs do record architectural decisions, but they also act as documentation, making Notes
it easier to share and collaborate. Others might need to look at or even sign off on an
ADR. Let’s start by considering the different statuses an ADR can have.


```
This is like planning an evening
out. You know you’d like to
Request for Comment (RFC) go out and which friends you
Use this status for ADRs that need additional input—perhaps from want to invite, but you hope
other teams or some sort of advisory board. Usually, these ADRs they’ll suggest a restaurant.
affect multiple teams or address a cross-cutting concern like security.
An ADR in RFC status is typically a draft, open for commentary and You ask everyone to respond
critique from anyone invited to do so. An ADR in RFC status should by Tuesday so you can make
always have a “respond by” deadline. reservations. (The deadline
is important, since Ted can
never make up his mind about
anything.)
Proposed
After everyone has a chance to comment, the ADR’s status moves to
Proposed. This means the ADR is waiting for approvals. You might You have a plan for the
edit it or even overhaul the decision if you discover a limitation that evening, but you haven’t hit
makes it a no-go. In other words, you still haven’t made a decision, “send” on the invite yet—just
but you’re getting there. in case the weather turns.

Accepted Oh yeah. Everyone has
RSVP’d. Time to find
Does exactly what it says on the tin­­. A decision has been made, and
a cool outfit!
everyone is on board who needs to be. An Accepted status also tells
the team tasked with implementing this decision that they can get
started.

```

If there’s no need for feedback from others, you can set the ADR’s status to
Accepted as soon as the decision is made. Most ADRs stay at Accepted, but there
is one more status to be aware of: Superseded.




100  Chapter 3

<a id='p137'></a>
<!-- Página 137 -->

```
the two laws of software architecture



```

Writing ADRs: What’s your status? (continued)
You’ve arrived at a decision, which you diligently record in an ADR. Signed, sealed, delivered—
you’re done.
But then things change.
Maybe the business is growing and the board decides to focus more on scalability than on time
to market. Maybe the company is entering international markets and needs to comply with EU
data privacy and retention regulations. Whatever the reason, the decision you made is no longer
appropriate. What now?
Well, you write another ADR. The old ADR is superseded by the new one, and you record it as
such. Suppose the customer survey team realizes that a relational database is no longer fulfilling
their needs, so they do another trade-off analysis and decide to switch to a document store. Here
are the titles and statuses of the old and new ADRs:


```
The previous ADR
042: Use relational store for customer survey service
Only an Accepted ADR can
become Superseded.
Status: Accepted Superseded by 068

This updated status mentions the
number of the new ADR.



This ADR overrides Note: We’ll be showing
the previous ADR. you ADR 068 for the
068: Use document store for customer survey service rest of the chapter,
while you help the Two
Status: Accepted, Supersedes 042 Many Sneakers team
with their ADR.
```

Now the new ADR has the Notice how we mention the number
status Accepted. of the superseded ADR here.
```
Linking ADRs is an
important part of a
project’s “memory.”
```

An accepted ADR can move into Superseded status if a future ADR changes the decision it
```
It helps everyone
```

documents. It’s important for both ADRs to highlight which ADR did the superseding and which
```
remember what has
```

ADR has been superseded. This bidirectional linking allows anyone looking at a superseded ADR
```
already been tried.
```

to quickly realize that it’s no longer relevant, and tells them exactly where to look for details
on the new decision. Anyone looking at the superseding ADR can follow the link back to the
superseded ADR to understand everything involved in solving that particular problem.


```
you are here 4  101
```


<a id='p138'></a>
<!-- Página 138 -->

more on statuses


```
there are no
Dumb Questions
Readers might think that the new decision came first. It wouldn’t
```

Q: All this superseding and numbering seems overly
```
convey that you made one decision and then had to change it for
some reason. Giving it a new number makes it clear that the old
```

complicated. Why not just edit the original ADR?
```
ADR 007 was no longer relevant after ADR 013. Confused yet?

```

A: We use a three-digit prefix in the ADR title because it helps
sequence things. Let’s say ADR 007 no longer applies to your
```
Q: So you’re telling me that an Accepted ADR is
immutable: once accepted, it is not permitted to change. Is
```

situation, but you’ve made a bunch of architectural decisions in the
```
that right?
```

meantime. The last ADR in your architectural decision log is ADR
013.
Now you need to reevaluate ADR 007. Say you choose to edit it,
```
A: Look at you! That’s exactly it. Except for when the status of
an ADR goes from Accepted to Superseded, a decision recorded
```

as opposed to superseding it with ADR 014. What would happen? in an ADR is immutable. Sure, you might edit the ADR to include
Chronologically speaking, you amend ADR 007 after accepting additional information, but for the most part, other than the status,
ADR 013. But if someone tried to follow the decision process things shouldn’t change much.
by reading the ADRs, they’d be seeing them in the wrong order!




```
Exercise
```

In the previous exercise, you hashed out the title of Two Many Sneakers’ ADR about using queues for messaging.
Let’s say you get the green light. Write down the title you chose in the space below and give your ADR a status:

```
Title: _________________________________________________________________________

Status: _________________________________________
```

Three months later:
Whoops! The requirements have changed. Your latest trade-off analysis reveals that topics would be a better fit.
Everyone has signed off on this, so you need to supersede your ADR with a new ADR. This is the 21st ADR your team
has worked on. Write down the title and the new status of the old ADR:

```
Title: _________________________________________________________________________

Status: _________________________________________
```

Now write down the title and status of the newly introduced ADR:

```
Title: _________________________________________________________________________

Status: _________________________________________
Solution on page 118

```

102  Chapter 3

<a id='p139'></a>
<!-- Página 139 -->

```
the two laws of software architecture



```

Writing ADRs: What’s your status? (recap)
There’s a lot going on with ADR statuses, so we’ve created a handy visualization to
help you out.




```
Start here.
This could be as easy as
Every ADR starts getting confirmation
in RFC status. from your team.
Does this ADR affect
multiple teams or
projects? Does it need
to be approved by an
advisory board? If yes, go
right; else, go left.

Here, you are
seeking approvals
from others. You
Are all stakeholderscisonion? If are allowed to make
board with this de edits as needed.
yes, continue.


Did something change?
Has a later ADR
rendered this ADR
irrelevant?




End here.




you are here 4  103
```


<a id='p140'></a>
<!-- Página 140 -->

the context section



Writing ADRs: Establishing the context Title
Context matters. Every decision you’ve ever made, you made within a certain Status
context and with certain constraints. When you chose what to have for breakfast this Conte
```
xt
```

morning, the context might have included how hungry you were, how your body Decisio
felt, your lunch plans, and whether you’re trying to increase your fiber intake. It’s no n
```
Conse
```

different for software architecture. quenc
```
es
Gover
nance
```

The Context section in the ADR template is your place to explain the circumstances Notes
that drove you to make the decision the ADR is capturing. It should also capture
any and all factors that influenced your decision. While technological reasons will
usually find their way onto this list, it’s not unusual to include cultural or political
factors to help the reader understand where you’re coming from.

Let’s continue working on the
ADR we started with in the The Cont
Status section. answers theext section
```
“Why did w question,
```

Context make this ce have to
```
e customer survey responses. The
data begin with? hoice to
```

We need to simplify how we stor req uire men ts ”
currently resides in a relational stor
```
e, and its rigi d sch ema Note—we a
```

have become challenging as we evo
```
lve the surveys (for example, intr
oducing
describing oren’t
```

different or extended surveys for
```
our premium customers). just yet! W ur decision
le to us, like the JSONB data type
in a whole sec e have
```

There are various options availab that. tion for
```
such as MongoDB.
```

PostgreSQL or document stores



```
there are no
Sharpen your pencil Dumb Questions
Continue building out the ADR for Two Many
```

Sneakers. Use the space below to write a Context section for the team’s
decision to use queues for communication between the trading service
```
Q: What about all that time and
effort I spent on the whiteboard? Is
```

and other services. (Then compare it with our take at the end of this that part of the context?
chapter.)
```
A: If you need to document your
trade-off analysis, we suggest you
introduce a new section called
“Alternatives.” In it, list all the alternatives
you considered, followed by your lists of
pros and cons.

Using a separate section to detail the
trade-off analysis delineates it cleanly
Solution on page 119 and avoids cluttering the Context section.



```

104  Chapter 3

<a id='p141'></a>
<!-- Página 141 -->

```
the two laws of software architecture



```

Writing ADRs: Communicating the decision Title
We’ve finally arrived at the actual decision. Let’s start by looking at the customer Status
survey team’s completed Decision section: Conte
```
xt
Decisio
n
Conse
quenc
es
Gover
nance
Decision Notice the Notes
authoritative voice!
We will use a document database for the customer survey.
changes
The marketing department requires a faster, more flexible way to make
to the customer surveys. The Decision section
and will covers the “why” of the
Moving to a document database will provide better flexibility and speed, decision itself: remember
e.
better facilitate changes by simplifying the customer survey user interfac the Second Law?



```

If this ADR’s status is RFC or Proposed, the decision hasn’t been made (yet). Even
so, the Decision section starts by clearly expressing the decision being made. In the Context section,
The tone of the writing should reflect that. It’s best to use an authoritative voice you explained why this
```
decision was on the table
The Decision section, .
```

when stating the decision, with active phrases like “we will use” (as opposed to “we
believe” or “we think”).
```
which immediately follows
```

The Decision section is also the place to explain why you’re making this decision, it, explains the decision
paying tribute to the Second Law of Software Architecture: “Why is more itself. Together, they
important than how.” Future you, or anyone else who reads the ADR, will then allow the reader to
understand not just the decision but the justification for it. frame the decision
```
correctly.
This is also a great place to list others
who signed off on this decision. For
example, “The marketing department
requires...” is an example of CYA. “Cover Your Assets”! :)


The ADR is not an opinion piece
Remember that the ADR is not a place for anyone’s opinions on the state of things.

```

Watch it!
```
It’s easy to slip into that mode, especially when justifying a decision. Even when
explaining context, it can sometimes be hard to stay objective.

Treat an ADR like a journalist treats a news article—stick to the facts and keep your tone neutral.




you are here 4  105
```


<a id='p142'></a>
<!-- Página 142 -->

the decision section




```
Exercise
```

It’s time for you to write the Decision section of the ADR for Two Many Sneakers. Here are the main factors the team
considered when making their decision:
```
• Queues allow for heterogeneous messages.
• Security is an important architectural characteristic for the stakeholders.
```

We’ve given you some space to write out a Decision section, including the corresponding justification. This section
should answer the question, “Why queues?” Hint: Be sure to focus on the decision and the “why.” See the solution at
the end of the chapter for our own take.
```
Feel free to gl
the trade-offanance back at
did earlier in the alysis we
to refresh your chapter
memory.




Solution on page 119


there are no
Dumb Questions
```

Q: I’m not entirely clear on the difference between the context and the “justification” we provide in the Decision section.
Aren’t those the same thing?

A: Maybe an example will help. Say it’s your best friend’s birthday, and you and a few others decide to go out to a fancy dinner to
celebrate. That’s the context—the circumstances surrounding the decision you have to make.
Before you decide on the details, you might make a list of possible restaurants (the alternatives available to you), thinking about how
well the cuisines they offer match everyone’s preferences. This would be akin to a trade-off analysis.
You pick a pan-Asian bistro: that’s the decision. You choose that particular restaurant because its menu has vegetarian and gluten-free
options, and it allows anyone with dietary restrictions to make substitutions. That’s the justification for your decision.



106  Chapter 3

<a id='p143'></a>
<!-- Página 143 -->

```
the two laws of software architecture



```

Writing ADRs: Considering the consequences Title
```
Status
```

Every decision has consequences. Did you work out extra hard yesterday? If so,
you might be sore this morning. (But maybe a little bit proud of yourself, too!) Context
```
Decision
```

It’s important to realize the consequences—good and bad—of architectural
decisions and document them. This increases transparency by ensuring that Consequ
```
ences
```

everyone understands what the decision entails, including the team(s) affected by Governan
```
ce
```

it. Most importantly, it allows everyone to assess whether the decision’s positive Notes
consequences will outweigh its negative consequences.
The consequences of an ADR can be limited in scope or have huge ramifications.
Architectural decisions can affect all kinds of things—teams, infrastructure, budgets,
even the implementation of the ADR itself. Here’s an incomplete list of questions to
ask:
 How does this ADR affect the implementing team? For instance, does it change
```
the algorithms? Does it make testing harder or easier? How will we know when
we’re “done” implementing it?
```

 Does this ADR introduce or decommission infrastructure? What does that
```
entail?
Time and money
```

 Are cross-cutting concerns like security or observability affected? If so, what are big—be sure
effects will that have across the organization? to think this one
 How will the decision affect your time and budget? Does it introduce costs or through!
```
save money? Will it take arduous effort to implement or make things easier?
```

 Does the ADR introduce any one-way paths? (For example, using queues means
```
Of course, the ADR might
we can’t control the order of messages.) If so, elaborate on this.
make things simpler and
more cost-effective. If
```

Collaborating with others is a great way to make sure your assessment is so, that’s definitely worth
thorough. No matter how hard you think through the consequences of the ADR, highlighting.
you’re likely to miss a few things; multiple perspectives will reveal more potential
consequences. Here’s a sample Consequences section:



```
Consequences It’s important
```

Highlight the
consequences to note
of the decision Since we will be using a single representation for all surveys, multiple documents consequences
for the will need to be changed when a common survey question is updated, added, or that might
implementation removed. affect
team. The IT team will need to shut down survey functionality during the data migration customers or
```
from the relational database to the document database, causing downtime. users.




you are here 4  107
```


<a id='p144'></a>
<!-- Página 144 -->

the consequences section



```
Sharpen your pencil
```

Help the Two Many Sneakers team iron out the Consequences section of their ADR. Here are a few things to think
about:
¾ A queue introduces a new piece of infrastructure.
```
There are no right or wrong
```

¾ The queues themselves will probably need to be highly available. answers, but if you’d like to see
¾ Queues mean a higher degree of coupling between services. how we approached this, glance at
```
the solution at the end of the
chapter.




Solution on page 120



Brain
Power
Think about an architectural decision made in your current project, or one you’ve worked on in the past. It
might be programming language used, the application’s structure, or even the choice of database. Can you
think of at least two intended consequences and two unintended consequences of that decision?




```

108  Chapter 3

<a id='p145'></a>
<!-- Página 145 -->

```
the two laws of software architecture



```

Writing ADRs: Ensuring governance Title
```
Statu
```

Have you ever made a New Year’s resolution that fizzled out before the end of s
```
Con
```

February? Maybe you joined a gym, only to end up paying but never working out? text
Us too. A decision is only good if you act on it, and if you don’t accidentally stray Deci
```
sion
```

away from it in the future. Con
```
sequ
Gove ence
s
```

Sure, you and your team spent a bunch of time analyzing trade-offs and writing rnan
```
ce
```

an ADR to record the decision. Now what? How do you ensure that the decision is Note
```
s
```

correctly implemented—and that it stays that way?
This is the role of the Governance section, which is vital in any ADR. Here, you
outline how you’ll ensure that your organization doesn’t deviate from the decision—
```
One of your authors ha
```

now or in the future. You could use manual techniques like pair programming or
```
written a book called “Bs uil
```

code reviews, or automated means like specialized testing frameworks.
```
Evolutionary Architectures”ding
that shows you how to
If the word use “fitness functions” fo
“governance” conjures architectural governance. r
up ideas of to pick up a copy. (After Be sure
These two sections done with this book, of coyou’re
aren’t part of the regulatory compliance, urse!)
standard ADR well, this isn’t that.
template, but we think
they add a lot of value.


Title Writing ADRs: Closing notes
Status The Notes section contains metadata about the ADR itself. Here’s a list of fields we
Context like to include in our ADRs:
n
Decisio • Original author
uences This section is handy even
Conseq
ance • Approval date tool you use to store your if the
automatically records thingADRs
Govern

creation and modification s like
Notes • Approved by
• Superseded date Yes, including this informa dates.
may be repetitive, but ma tion
it part of the ADR makeking
• Last modified date
• Modified by easier to discover. s it
• Last modification




you are here 4  109
```


<a id='p146'></a>
<!-- Página 146 -->

bringing it all together




```
Exercise
```

Let’s bring it all together! You’ve been working piecemeal on the ADR for the Two Many Sneakers team. We’d like you
to flip back to the past few exercises and copy your ADR sections onto this page to create a full ADR. We’ve given
you the section titles—all you have to do is fill ’em out. (Assume the status to be “Accepted.”) You can find our version
at the end of the chapter.


Title



Status



Context




Decision




Consequences




And there you have it: a complete ADR in its full glory.
```
They grow up so quickly! :’)
We’ll skip Governance and We’re so proud of you all.
Notes here since they’re
not part of the standard
template. Solution on page 121

```

110  Chapter 3

<a id='p147'></a>
<!-- Página 147 -->

```
the two laws of software architecture


there are no
Dumb Questions
```

Q: I really like the ADR template. But where am I supposed Q: Can you recommend any tools that make it easier to
to store my ADRs? write and manage ADRs?

A: There are lots of options—it all depends on what you and
your team are comfortable with, and who else might be interested
```
A: Oh, sure! There are many options, from command-line tools
to language-specific tools that allow you to record ADRs directly in
```

in reading or contributing to the ADRs. your source code. You can see a list of available tools at https://adr.
```
github.io/#decision-capturing-tools.
```

One option is to store ADRs in plain-text files (or maybe Markdown
or AsciiDoc files) in a version-control system like Git. This way, Most third-party tools make assumptions about the format of the
there’s a commit history showing any changes to the ADRs. The ADR—perhaps they generate Markdown files or store the files in
downside is that nondevelopers don’t always know how to access a specific directory structure. Test-drive a tool a few times to get a
version-controlled documents. If you do choose to store your ADRs feel for it.
this way, we recommend keeping them in a separate repository (as
```
Finally, some age-old advice: keep it simple, silly. We suggest
```

opposed to stuffing them in with your source code). You’ll thank us
```
you start by writing out ADRs without any complicated tooling or
```

later.
```
automation. Get a sense of what works best for your team. Then,
```

Alternatively, you could use a wiki. Most wikis use a WYSIWYG as your needs grow, go find a tool that fits those needs.
(“what you see is what you get”) editor, so they’re accessible


## Q:

to more people. Just be sure that your choice of wiki can track
changes. You wouldn’t want someone to edit an ADR accidentally Do ADRs always belong to a single project, or can they
without everyone knowing. affect multiple projects and teams? How about the whole
Whatever you choose, make sure it’s easy to add, edit, and search organization?
for ADRs. We’ve seen too many honest efforts at recording ADRs
die just because no one could find the ADRs again if their lives
depended on it.
```
A: Yes, yes, and yes. ADRs can be as narrow or as broad as
you’d like them to be. Some ADRs are project-specific, affecting
only one team. Other ADRs affect many or all teams in an

```

Q: organization. At the online retailer Amazon, there’s an ADR
```
My whole team loves Markdown. (Plain text for the win!) affectionately referred to as “the Jeff Bezos API mandate.” It
```

Any advice on file naming conventions? records a decision that company founder Jeff Bezos once made:
```
that all services within Amazon can only talk to other services via
```

A: Recall that ADR titles have a three-digit prefix, followed by
a very succinct description of the ADR. If you store your ADRs as
```
an API. Naturally, this affected the entire organization—no small
feat, given Amazon’s size.
```

plain-text files, we recommend using the title as your filename, Most cross-project or cross-team ADRs require a lot of
including the prefix. For example, an ADR with the title “042: Use collaboration, and often the blessing of a central architecture
queues between the trading and downstream services” should review board. Such ADRs tend to affect cross-cutting concerns,
be stored in a file named 042-use-queues-between-the-trading- like how services should communicate with one another or
and-downstream-services.md. We like using all lowercase letters, which data transfer protocol to use. ADRs related to security or
which avoids any confusion between different operating systems. regulatory compliance often cut across multiple teams or a whole
Replace spaces with hyphens to avoid whitespace. organization.
This forces you to come up with good titles! And the three-digit
prefix means you can simply sort the files in a folder by name to
put them in the right order.




```
you are here 4  111
```


<a id='p148'></a>
<!-- Página 148 -->

why ADRs?



The benefits of ADRs
We hope we’ve convinced you by now that recording your decisions in ADRs need
not be a long, arduous process. We really like the format we’ve shown you in this
chapter, but feel free to tweak or modify it.
Is recording architectural decisions really that important? We certainly think so!
There are tons of benefits to recording these decisions—not just for you and your
team, but for your entire organization. Let’s quickly recap.



```
ADRs are records of
a system, including ADRs answer
how it’s structured question “Whatthe
and how it works, were we think
that anyone can even if no oneinwg?”
review at any time. made the decisioho
Ah! Here’s is still around. n
a Superseded
ADR—apparently
Why don’t we just
use a document
we did at one ADRs are key to building
store?
point. institutional knowledge and
```

ADRs can help prevent memory. Teams can read and
teams from going down learn from each other’s ADRs.
the same road again and
again, encouraging new
solutions instead.

```
Bidirectional linking
between Superseded
and Accepted ADRs
is a huge boon here.



Keep the ADR process as frictionless as possible
It’s tempting to add sections to the ADR template in the hope of being comprehensive.

```

Watch it!
```
While that’s a noble goal, it adds work. If you keep “feeding the beast,” the
documentation process gets harder. That can discourage people, and some might
stop writing ADRs altogether.
Focus on concision and brevity. Keep it simple. You’ll thank us later.




```

112  Chapter 3

<a id='p149'></a>
<!-- Página 149 -->

```
the two laws of software architecture



```

Two Many Sneakers is a success
The team at Two Many Sneakers is ecstatic. Their customers love getting real-time
notifications about new offerings in the app, and the improved analytics are giving
the security team the information they need to sniff out any and all sneaker scams
```
from a mile away.


Just got the email
from the finance
team: they want the
trading service to keep the
compliance service in the
Learning about the know. That should be an
two laws of software easy change.
architecture sure made this
easy. Not only do we know
we’ve made the right decision,
but we’ve also captured it in an
ADR. I feel so much better.




Grokking the two laws of software architecture will serve you well. Now you know
that there are no “best practices” in software architecture—just trade-offs. It’s up to
you (and your team) to find the most viable and best-fitting option. And don’t forget
to record your decision in an ADR!
Onward and upward.



you are here 4  113
```


<a id='p150'></a>
<!-- Página 150 -->

chapter summary



```
Bullet Points
```

 There is nothing “static” about architecture. It’s  Over time, your ADRs will build into a log of
```
constantly changing and evolving. architectural decisions that will serve as the memory
store of your project.
```

 Requirements and circumstances change. It’s up to you
```
to modify your architecture to meet new goals.  An ADR’s title should consist of a three-digit numerical
prefix and a noun-heavy, succinct description of the
```

 For every decision, you will be faced with multiple
```
decision being made.
solutions. To find the best (or least worst), do a trade-off
analysis. This collaborative exercise helps you identify  An ADR can be assigned one of many statuses,
the pros and cons of every possible option. depending on the kind of ADR and its place in the
decision workflow.
```

 The First Law of Software Architecture is: Everything in
```
software architecture is a trade-off.  Once all parties involved in the decision sign off on the
ADR, its status becomes Accepted.
```

 The answer to every question in software architecture
```
is “it depends.” To learn which solutions are best for  If a future decision supplants an Accepted ADR, you
your situation, you’ll need to identify the top priorities should write a new ADR. The supplanted ADR’s status
and goals. What are the requirements? What’s most is marked as Superseded and the new ADR becomes
important to your stakeholders and customers? Are Accepted.
you in a rush to get to market, or hoping to get things
 The Context section of an ADR explains why the
stable in growth mode?
decision needed to be made to begin with.
```

 The product of a trade-off analysis is an architectural
```
 The Decision section documents and justifies the actual
decision: one of the four dimensions needed to
decision being made. It always includes the “why.”
describe any architecture.
 The Consequences section describes the decision’s
```

 An architectural decision involves looking at the pros
```
expected impact, good and bad. This helps ensure
and cons of every choice in light of other constraints—
that the good outweighs the bad, and aids the team(s)
such as cultural, technical, business, and customer
implementing the ADR.
needs—and choosing the option that serves these
constraints best.  The Governance section lists ways to ensure that the
decision is implemented correctly and that future
```

 Making an architectural decision isn’t just about
```
actions do not stray away from the decision.
choosing; it’s also about why you’re choosing that
particular option.  The final section is Notes, which mostly records
metadata about the the ADR itself—like its author and
```

 The Second Law of Software Architecture is: Why is
```
when it was created, approved, and last modified.
more important than how.
 ADRs are important tools for abiding by the Second
```

 To formalize the process of capturing architectural
```
Law of Software Architecture, because they capture the
decisions, use architectural decision records (ADRs).
“why” along with the “what.”
These documents have seven sections: Title, Status,
Context, Decision, Consequences, Governance, and  ADRs are necessary for building institutional
Notes. knowledge and helping teams learn from one another.




```

114  Chapter 3

<a id='p151'></a>
<!-- Página 151 -->

```
the two laws of software architecture




“Two Laws” Crossword
Think you’ve mastered the two laws of software architecture? Why don’t you
document your knowledge by completing this crossword?




```

Across Down
2. Two Many _____ 1. Topics can be independently _____
4. Topics use a fire-and-_____ system 3. An architectural characteristic that’s especially important for
5. A new ADR can _____ an old one financial transactions
7. You can list pros and cons on a _____board 5. Architects are responsible for making architecturally _____
8. You should record every architectural _____ you make decisions
10. Documents made up of seven sections (abbr.) 6. ADR section that tells you why a decision needed to be made
11. Heterogeneous 9. High or low interdependence
13. Important architectural characteristic for a fast-growing 12. Short way to say “not at the same time”
business 14. Two Many Sneakers’ mobile app communicates with the
15. “Everything in software architecture is a trade-off ” is the trading _____
_____ _____ of software architecture (two words) 16. More important than how, according to the Second Law
18. Examples of messaging mechanisms include queues and 17. The _____ of an ADR might be Accepted
_____
19. Best tone to use when writing an ADR
20. If you’re too excited about a new tool, you might have
_____ Object Syndrome Solution on page 122

```
you are here 4  115
```


<a id='p152'></a>
<!-- Página 152 -->

exercise solutions




```
Exercise From page 85

Solution
```

Which of the following architectural characteristics stand out as important for this particular problem? Hint: There are
no right answers here, because there is a lot we don’t know or aren’t sure of yet. Take your best guess—here are our
thoughts: Lots of downstream
```
services need to know
about sneaker trades. modularity
```

Since business is d extensibility This sounds important! upgradability
booming, this coul
be something to low coupling
look out for.
```
performance security




From page 89
Sharpen your pencil
Spend a few minutes comparing the results of our trade-off analysis. Notice how both options
support some characteristics but trade off on others? Now we’re going to present you with some
```

requirements—see if you can decide if you’d pick queues or topics to support each one. Here are our answers:

```
Requirements
“Security is important to us.”
Queues / Topics
“Different downstream services need different kinds of information.”
Queues / Topics
“We’ll be adding other downstream services in the future.”
Queues / Topics




```

116  Chapter 3

<a id='p153'></a>
<!-- Página 153 -->

```
the two laws of software architecture



From page 91
Sharpen your pencil
Solution
```

This time, we’d like you to do some trade-off analysis on your own. We chose messaging as the communication
protocol between our trading service and its consumers. Messaging is asynchronous. Choosing between
asynchronous and synchronous forms of communication comes with its own set of trade-offs! We’ve given you two
whiteboards, one for each form of communication, and we’ve listed a bunch of “-ilities.” We’d like you to consider
how each architectural characteristic would work in both contexts. Is this characteristic a pro or a con (or neither) in
synchronous communications? What about in asynchronous communications? Place each “-ility” in the appropriate
column. Hint: Not all of them apply to this decision. You’ll find our answers below:


```
transactions
responsiveness
error handling



consistency
coordination extensibility


deployability
fault tolerance




Using sync communications Using async communication
Cons s
Pros Pros
consistency extensibility responsiveness Cons
consistency
error handling fault tolerance extensibility
error handling
transactions responsiveness fault tolerance transactions




you are here 4  117
```


<a id='p154'></a>
<!-- Página 154 -->

exercise solutions




```
Exercise From page 99
Solution
```

In the following exercises, you’re going to help the team at Two Many Sneakers write an ADR. They’ve decided to
use asynchronous messaging, with queues between the trading service and downstream services. Assume this is the
12th ADR the team is writing. What title would you give this ADR? Don’t forget to number it! Here’s what we came up
with:

```
012: Use of queues for asynchronous messaging between order and downstream services




Exercise From page 102
Solution
```

In the previous exercise, you hashed out the title of Two Many Sneakers’ ADR about using queues for messaging.
Let’s say you get the green light. Write down the title you chose in the space below and give it a status. Here’s ours:

```
Title: 012: Use of queues for asynchronous messaging between order and downstream services
________________________________________________________________________

Status: Accepted
_________________________________________
```

Three months later:
Whoops! The requirements have changed. Your latest trade-off analysis reveals that topics would be a better fit.
Everyone has signed off on this, so you need to supersede your ADR with a new ADR. This is the 21st ADR your team
has worked on. Write down the title and the new status of the old ADR:

```
Title: 012: Use of queues for asynchronous messaging between order and downstream services
________________________________________________________________________

Status: Superseded by 021
_________________________________________
```

Now write down the title and status of the newly introduced ADR. Here’s ours:

```
Title: 021: Use of topics for asynchronous messaging between order and downstream services
________________________________________________________________________

Status: Accepted, Supersedes 012
_________________________________________




```

118  Chapter 3

<a id='p155'></a>
<!-- Página 155 -->

```
the two laws of software architecture


From page 104
Sharpen your pencil
Solution
Continue building out the ADR for Two Many Sneakers.
Use the space below to write a Context section for
the team’s decision to use queues for communication
between the trading service and other services. Here’s our take:


The trading service must inform downstream services (namely the
notification and analytics services, for now) about new items available
for sale and about all transactions. This can be done through
synchronous messaging (using REST) or asynchronous messaging (using
queues or topics).




Exercise From page 106
Solution
```

It’s time for you to write the Decision section of the ADR for Two Many Sneakers. Here are the main factors the team
considered when making their decision:
```
• Queues allow for heterogeneous messages.
• Security is an important architectural characteristic for the stakeholders.
```

We’ve given you some space to write out a Decision section, including the corresponding justification. This section
should answer the question, “Why queues?” Hint: Be sure to focus on the decision and the “why.” There are no right
answers, but here’s what we came up with:


We will use queues for asynchronous messaging between the trading and downstream services.

Using queues makes the system more extensible, since each queue can deliver a different kind of message.
Furthermore, since the trading service is acutely aware of any and all subscribers, adding a new consumer involves
modifying it—which improves the security of the system.




```
you are here 4  119
```


<a id='p156'></a>
<!-- Página 156 -->

exercise solutions


```
From page 108
Sharpen your pencil
Solution
```

Help the Two Many Sneakers team iron out the Consequences section of their ADR. Here are a few things to think
about:
¾ A queue introduces a new piece of infrastructure.
¾ The queues themselves will probably need to be highly available.
¾ How do queues affect coupling between components?



Queues mean a higher degree of coupling between services.
We will need to provision queuing infrastructure. It will require clustering to provide for high availability.
If additional downstream services (in addition to the ones we know about) need to be notified, we will have to
make modifications to the trading service.

```
Here’s our take.




```

120  Chapter 3

<a id='p157'></a>
<!-- Página 157 -->

```
the two laws of software architecture


Exercise From page 110
Solution
```

Let’s bring it all together! You’ve been working piecemeal on the ADR for the Two Many Sneakers team. We’d like you
to flip back over the past few exercises and copy your ADR sections onto this page to create a full ADR. We’ve given
you the section titles—all you have to do is fill ’em out. (Assume the status to be “Accepted.”) Here’s our version:

Title

012: Use of queues for asynchronous messaging between order and downstream services

Status

Accepted

Context

The trading service must inform downstream services (namely the notification and analytics services, for now)
about new items available for sale and about all transactions. This can be done through synchronous messaging
(using REST) or asynchronous messaging (using queues or topics).


Decision

We will use queues for asynchronous messaging between the trading and downstream services.

Using queues makes the system more extensible, since each queue can deliver a different kind of message.
Furthermore, since the trading service is acutely aware of any and all subscribers, adding a new consumer involves
modifying it—which improves the security of the system.
Consequences
Queues mean a higher degree of coupling between services.
We will need to provision queuing infrastructure. It will require clustering to provide for high availability.
If additional downstream services (in addition to the ones we know about) need to be notified, we will have to
make modifications to the trading service.
And there you have it! A complete ADR in its full glory.




```
you are here 4  121
```


<a id='p158'></a>
<!-- Página 158 -->

exercise solutions




```
“Two Laws” Crossword Solution

From page 115




```

122  Chapter 3

<a id='p159'></a>
<!-- Página 159 -->

4 logical components
```
The Building Blocks




```

Ready to start creating an architecture? It’s not as easy as it sounds—and if you
don’t do it correctly, your software system could come crumbling to the ground, just like a poorly
designed skyscraper or bridge.

In this chapter we’ll show you several approaches for identifying and creating logical components, the
functional building blocks of a system that describe how its pieces all fit together. Using the techniques
described in this chapter will help you to create a solid architecture—a foundation upon which you can
build a successful software system.

Put on your hard hat and gloves, get your tools ready, and let’s get started.




```
this is a new chapter   123
```


<a id='p160'></a>
<!-- Página 160 -->

demystifying logical components



Logical components revisited
Logical components are one of the dimensions of software architecture. They
are the functional building blocks of a system that make up what is known as
the problem domain. In Chapter 1 you learned a bit about them, and in this
chapter we’ll dive deep into what logical components are and how to create
them.
```
es
d e d - e dge boxnts that
oun l compon e Order Re
these r a It’s membe
All of sent the logiclem domain. Tracking
from r th
e
repr ise the pr o b
Cha is exa
compr pter mple
1. ?

Order Payment Order
Placement Processing Shipping



Remember that, in most programming languages, logical components are
Inventory represented through the directory structure of your source code repository. For
Management example, source code located in the app/order/tracking directory would be
contained within a logical component named Order Tracking.

main.
app This is the do
domain.
This is the sub ical
```

The directory structure order This is the log Order
identifies the logical tracking component. Tracking
components and is therefore
part of the architecture. source_code_file

```
source_code_file

source_code_file
source_code_file
This source code implements the
The source code identifies order tracking functionality.
how the logical component is
implemented and is therefore
part of the design.



```

124  Chapter 4

<a id='p161'></a>
<!-- Página 161 -->

```
logical components




Exercise
```

Name that component
It’s your first week on the job as the new architect, and you’ve been assigned to an existing project to build a
trouble ticket system. You want to understand the logical components of the architecture, but your team doesn’t
know anything about logical components—they just started coding. To determine the logical architecture, you
have to look at the existing directory structure. How many individual logical components can you identify from the
codebase below?



```
order_entry_app We did Shopping Draw yo
order this one Cart in this spuar components
for you! ce over he
shopping_cart re.
lots_of_source_code_files

fulfillment
lots_of_source_code_files

history
recent
lots_of_source_code_files

archive
lots_of_source_code_files

Payment
credit_card
lots_of_source_code_files

gift_card
lots_of_source_code_files

customer
profile
lots_of_source_code_files




Solution on page 156

you are here 4  125
```


<a id='p162'></a>
<!-- Página 162 -->

auction application



Adventurous Auctions goes online
Want to go on a safari in Tanzania? Observe wildlife in the Galapagos
Islands? Hike to the base camp of Mount Everest? Adventurous Auctions
is here to help!
You’ve probably seen our ads or attended some of our live auctions
around the country. These kinds of adventures are hard to come by and
can take years to reserve; our company auctions them off at a significant
cost savings.
We want more people around the world to be able to access these great
trips, so we’re taking our adventurous auctions online (in addition to our
in-person auctions). an
```
Let’s go o!n
```

That’s where you come in: we need a new system to support the online
```
adventure
```

auctions of our adventurous trips.


```
This is K
wants to abte. She Here’s what the new system needs to do:
adventure id for an
trip.
Scale up to meet demand, so hundreds or even thousands of
people can participate in each auction.

Include both in-person and online bids in every auction.

Allow online users to register with Adventurous Auctions and
provide us with their credit card details so they can pay if they win
a trip.

Allow online users to view live video streams of in-person auctions,
as well as all bids placed so far, both in person and online.

Allow online users to bid on trips, just like the people in the room.

Determine which online bidder bids the asking price first (this is
called “winning the bid”). If an online bidder bids at the same time
as an in-person bidder, the auctioneer then determines who bid
first.

When the auctioneer announces an online user as the winner, the
system charges the winner’s credit card, notifies the winner, then
moves on to the next trip in the auction.

to show you how to
Pay attention, because we’re goingthis
create a logical architecture for system.


```

126  Chapter 4

<a id='p163'></a>
<!-- Página 163 -->

```
logical components



```

Logical versus physical architecture
A logical architecture shows all of the logical building blocks of a system
```
We’re g
about cooing to be talk
```

and how they interact with each other (known as coupling). A physical

```
in this c mponent coup ing a lot
```

architecture, on the other hand, shows things like the architectural style,
services, protocols, databases, user interfaces, API gateways, and so on. hapter. ling late
```
r
```

The logical architecture of a system is independent of the physical
architecture—meaning the logical architecture doesn’t care about databases,
services, protocols, and so on. Let’s look at an example of what we mean by a
logical architecture.

```
As you remember, Adventurous Auctions needs to create and
schedule online auctions and allow bidders to register, search for
```

Auction auctions, and view the trips that are up for bid. Here are some of
```
Auction
```

Maintenance the components—the functional building blocks—that will help
```
Scheduler
make that happen.

```

Here a
logical cre some of the
Adventu omponents for Auction Auction Bidder Bidder
```
rous Auc Search Sign-on
tions. Viewer Registration



l
```

This physicuare shows
```
See how the logical architecture doesn’t include the various components of physical
e ct
```

archit he services
```
architecture mentioned above? It’s a different view of the system. To see what we mean,

```

some of t ases.
```
compare the diagram above with the following physical architecture diagram. Notice how

```

and datab
```
the physical architecture associates services with components from the logical architecture,
and also shows the services and databases for the system.




Auction Auction Bidder Bidder
Search Maintenance Registration Sign-on


Auction Auction
Viewer Scheduler
Logical components

Service
Database




you are here 4  127
```


<a id='p164'></a>
<!-- Página 164 -->

logical or. physical?



```
Who Does What
```

We had our logical and physical architecture responsibilities all figured out, but somehow they got all mixed up.
Can you help us figure out who does what? Be careful—some responsibilities may not have a match (they aren’t
part of a logical or physical architecture).
Be sure to check the answers (located at the end of this chapter) before moving on.

```
Shows which programming language is used for
each component



Maps components to services
Logical
architecture Shows the logical components within the system
and how they communicate with each other



Shows how many databases there are in the
system and which services access them


We did this
one for you. Shows communication between services and the
protocol they use (like REST)



Physical Shows the source code files used to implement a
component
architecture

Shows the components and their interactions
within the user interface



Shows the API gateways and load balancers used
in the system


Solution on page 157

```

128  Chapter 4

<a id='p165'></a>
<!-- Página 165 -->

```
logical components



```

Creating a logical architecture
Identifying logical components isn’t as easy as it sounds. To help, we’ve created
this flowchart. Don’t worry—we’ll be covering all of these steps in detail in the
following pages.


```
Step 2: Assign Last,
to see iwe check
```

Step 1: Identify
```
requirements to
componef the
initial core
components
the arc nt satisfies
components
charact hitectural
need. eristics we
a k e o u r “bestnitial Then we assign some
em he i responsibilities to those
First, was to what thould be. components.
guess” omponents s
core c
Step 3: Analyze the Step 4: Analyze
Next, we make sure each role and responsibility architectural
component should handle statements characteristics
its new responsibility

Oops—we might need to readjust and refactor our
components. That would happen in these steps.


This flow continues as long as the system is alive.
This flowchart shows a series of steps to begin greenfield
applications (new systems created from scratch) and perform
ongoing maintenance on existing ones.
Ever wonder why it’s so common for a well-designed system
to end up as an unmaintainable mess in no time? It’s because
teams don’t pay enough attention to the logical architecture
of their systems.
Anytime you make a change or add a new feature to the
system, you should always go through each of these steps to
ensure that the logical components are the right size and are Performin
doing what they are meant to do. helps ensurg these four steps
doesn’t ende your architectur
unmaintain up looking like an e
able big ba
ll of mud.


you are here 4  129
```


<a id='p166'></a>
<!-- Página 166 -->

identifying components



Step 1: Identifying initial core components
The first step in creating a logical architecture is identifying the initial
core components. Many times this is purely a guessing game, and you’ll
likely refactor the components you initially identify into others. So don’t
spend a lot of time worrying about how big or small your components
are—we’ll get to that. First, let’s show you what we mean by a “guessing
game.”
```
This road
O of which stepmap shows you
This is Frank, the CIns. you’re on.
Adventurous Auctio

The auction flow is pretty simple. Participants join
a live auction, view the auction, and bid on a trip
they are interested in.




Given this simple description, you can start out by creating three logical
components, one for each of the three major things the system does.



Live Auction Video Bid
Session Streamer Capture
re
g e t — these aices.
for erv
```

Don’t nents, not s This c This c
compo a live aoumponent repr This component is aming is respoomponent
```
and allo ction taking esents responsible for stre online capturinnsible for
join the ws participan place the live auction to g bids.
auction. ts to participants.


```

These components aren’t really doing anything yet. You see, we’ve identified the
initial components, but we haven’t assigned them any responsibility yet. You
could think of them as empty jars. They represent our initial best guess, based
on a major action that takes place in the system. That’s why we call them initial
core components.

```
empty, just
This jar exists but iscomponents you
like the initial core Live Auction
identify. Session

```

130  Chapter 4

<a id='p167'></a>
<!-- Página 167 -->

```
logical components




```

Creating a logical architecture is all a “guessing game”? That’s the
most ridiculous thing I’ve ever heard. Isn’t there some way to take
```
the guesswork out of identifying logical components?




Yes, there is! In fact, you can use several
approaches to remove some of the
guesswork.
You don’t know a lot of details about the system or its requirements yet,
and the components you initially identify are likely to change as you learn
more. That’s why we say it’s a guessing game at this stage—and that’s
perfectly okay!
We’ll show you two common approaches for identifying initial core
components: the workflow approach and the actor/action approach.
There are other approaches that may seem like good ideas initially but that
can lead you down a very bad path. We’ll discuss those after we show you
the good stuff.




you are here 4  131
```


<a id='p168'></a>
<!-- Página 168 -->

modeling the workflow



Workflow approach
The workflow approach is an effective way to identify an initial set of core
components by thinking about the major workflows of the system—in other
```
You
```

words, the journey a user might take through the system. Don’t worry about
```
workfcan model
```

capturing every step; start out with the major processing steps, and then work more lows to c different
your way down to more details. initial reate
```
compo even
nents
```

Let’s use the workflow approach to identify some initial core components for the .
Adventurous Auctions architecture.

```
Register for Join the auction View the Bid on a trip Pay for the
an auction once it starts live auction you like trip if you win



Auction Video
Live Auction Bid Automatic
```

Registration Streamer
```
Session Capture Payment


there are no
Dumb Questions
```

Q: You identified “Video Streamer” as a logical component, Q: Is each step in a workflow always mapped to a single
but what if our team decides to use a third-party library or logical component?
service to stream the auction?

A: Great question! Even though you might not develop the
```
A: Not always. You might have several steps in a workflow
that point to the same logical component, particularly if their
```

functionality yourself, it’s still part of the logical architecture. functionalities are closely related.




Names matter.
Pay close attention to how you name your initial core components. A good name should
succinctly describe what that component does.

```
is
Clearly, this Who knows what th
lets you look catomponent es
component do od ?
being auctioned the trip
Trip Auction
It’s not a very go
Viewer is a good compo off. This component name.
Manager
nent name.



```

132  Chapter 4

<a id='p169'></a>
<!-- Página 169 -->

```
logical components



```

Sharpen your pencil
```
Your company wants a new system to assign workers to construction sites, and it’s your
job as the software architect to identify its initial core components. Using the workflow
approach, identify as many core components as you can, matching each to its associated
workflow step. Remember, a workflow step can have multiple components, and not every
workflow step has to have a unique component.

Step 1: Maintain a list of all construction workers, their skills, and their locations
Step 2: Create a new construction project and specify the work site

Step 3: Create a schedule for when various construction projects start and end
Step 4: When a new project starts, assign workers based on their skills and locations
Step 5: When the project completes, free up workers so they can be reassigned

Draw your logi
this space. Remca
em
l components in
good descriptive ber to give them
names.




Solution on page 158

you are here 4  133
```


<a id='p170'></a>
<!-- Página 170 -->

mapping actors and actions



Actor/action approach
The actor/action approach is particularly helpful if you have multiple actors
(users) in the system. You start by identifying the various actors. Then, you
identify some of the primary actions they might take and assign each action to a
new or existing component.

```
go
e r K at e ? S he wants tro. Returning to our Adventurous Auctions example, let’s use the
Rememb so she’ll be a bidde
on a trip,
actor/action approach to identify some initial core components.

We’ll start with Kate. As a bidder, here
are a few of her primary actions:
Auction
Look for an auction Search
The Bid
View the live video stream componen Capture
Video multiple t handles
Place a bid and send actions
the Bidd s bids to
Streamer

This is Sam. He’s an componen er Tracker
t.
auctioneer.
As an auctioneer, here are a few of Bid
Sam’s actions: Capture
ponent
Receive a bid from an online bidder
e A u ct io n Session comother
The Liv der information to
Enter a live in-person bid into the system
sends bid s.
component
Start the auction
Live Auction
Mark an item as sold Session


We use a “system” actor to represent things that
happen automatically in the system: Automatic
Payment

Charge bidder

Track bidder activity Bidder
Tracker


```

134  Chapter 4

<a id='p171'></a>
<!-- Página 171 -->

```
logical components



Exercise
```

You have a bakery that is ready to expand operations, and you would like a new system that lets customers
view, order, and pay for bakery items online for pickup. Orders are sent to the bakery coordinator, who purchases
ingredients and schedules orders. The baker receives the schedule of items to bake each morning and tells the
system when the items are baked. The system then emails the customers to let them know their items are ready for
pickup.
Using the actor/action approach, identify what actions each actor might take. Then draw as many logical components
as you can for the new bakery system, matching the actions you identified to the components.

We started this
exercise for
you and filled
in some of the
components. Customer
```
Shopping
Browse items Cart
Select items
The Item Checkout
Pay for items Item
Checkout component needs
Receive email that to access the
order is ready Shopping Cart
component.




Solution on page 159

you are here 4  135
```


<a id='p172'></a>
<!-- Página 172 -->

avoiding entities



The entity trap
```
Okay, so if I identify lots of actions that
have to do with bids, then should I put all of
them together in a single component called
the Bid Manager?




Welcome to the entity trap.
We call this approach the entity trap because it’s very easy to
fall into it when identifying the initial core logical components,
and you’ll run into lots of issues if you do this.
First of all, the name “Bid Manager” is too vague. Can you tell
what the component does just by looking at the name? Neither
can we. A name like this doesn’t tell us enough about the
component’s role and responsibilities.
This component will be ha Second, the component has too many responsibilities. All
because it’s doing too mu rd to scale too often, components in the entity trap become convenient
ch.
dumping grounds for all functionality related to those entities.
Bid These are all As a result, they take on too much responsibility and become
Manager the things the too big and difficult to maintain, scale, and make fault tolerant.
component does.
Accept a bid
Display all winning bids ip
Track bids for auditing purposes
Pro T
Watch out for words like manager or supervisor
Determine bid winner when naming your logical components—those are
Notify auctioneer of online bid good indicators that you might be in the entity trap.
Generate bid reports



Sharpen your pencil
```

What other words besides manager can you list that, if they appeared in a component name, might indicate that you’ve
fallen into the entity trap?
```
d this supervisor
```

We di
one for you.

```
Solution on page 160

```

136  Chapter 4

<a id='p173'></a>
<!-- Página 173 -->

```
logical components



Exercise
Can you select the most appropriate approach to identifying initial core components in the following scenarios? In
some cases, more than one approach may be appropriate.

The system has only one type of user Workflow Actor/Action
The system has well-defined entities Workflow Actor/Action
You have minimal functional requirements Workflow Actor/Action

The system has many complex user journeys Workflow Actor/Action
The system has many types of users Workflow Actor/Action

Solution on page 160




there are no
Dumb Questions
```

Q: The actor/action approach reminds me a lot of event Q: Are you telling me I should never use the words
storming. Are they the same thing? manager, supervisor, and so on as part of my component
```
names?
```

A: Great observation, and we’re glad you saw the similarities.
Event storming is a workshop-based approach that is part of A: Not necessarily—there is no hard and fast rule to the entity
domain-driven design (DDD). With this approach, you analyze the trap. Sometimes it’s hard to come up with a name for something
business domain to identify domain events. While both approaches that does a general task. Take, for example, a component that
have the final goal of identifying actions performed within the manages all of the reference data in your application—name/
system, event storming takes identifying components much further value pairs like country codes, store codes, color codes, and so
than the actor/action approach does. You could say that the actor/ on. A good name for such a component would be “Reference Data
action approach identifies the domain event and actor elements of Manager.” However, names like “Order Manager” or “Response
event storming, but doesn’t continue with other elements such as Handler” are too broad and don’t describe what those components
command, aggregate, and view. You can learn more about event actually do.


## Q:

storming at https://en.wikipedia.org/wiki/Event_storming.

Q: Can you combine the workflow approach and actor/
```
When using the actor/action approach, how many
actions should you identify for each actor?
```

action approach, or do you have to choose between them?

A: You can combine them, and in most cases this is a good
```
A: That’s a tough question. The purpose of identifying actions
is to tease out likely logical components and what they might be
```

idea. If you start with the actor/action approach to identify actions, responsible for. We usually look at the primary actions an actor
you can then use the workflow approach to arrange them in the might take, rather than diving into too many details.
order in which they are likely to occur.




```
you are here 4  137
```


<a id='p174'></a>
<!-- Página 174 -->

assigning requirements



Step 2: Assign requirements
Once you’ve identified some initial core components, it’s time to move on to
the next step: assigning requirements to those logical components.
In this step, you’ll take functional user stories or requirements and figure
out which component should be responsible for each one. Remember, each
component is represented by a directory structure. Your source code resides in
that directory, so it contains that requirement.
Let’s go back to the initial set of components we defined based on what Frank
(the CIO) said about the basic workflow of Adventurous Auctions. Now it’s
time to assign some responsibilities to these components.

```
Represents the live
auction currently
taking place
Display the current trip up for bid during the auction
Since the Live Auction Session component is responsible for
Live Auction
controlling the auction currently taking place, it makes sense Session
to assign this requirement to it. Responsible for
receiving and
Mark a trip as sold and move to the next trip storing bids from
This requirement also has to do with controlling the flow of the
Bid the bidders.
Capture
auction session, so let’s assign it to the Live Auction Session
component. Responsible for show
the video feed from ing
Send each online bid to the live auctioneer the auction
as it’s placed, so they can call out the bid Video
Since the Bid Capture component receives the bid from the Streamer
bidder for a trip, it makes sense to have this component also
forward that bid to the live auctioneer.
This is a new component
Record the live video stream for later playback we added to satisfy the
in case a bid is contested last requirement
The Video Streamer component already has the video feed,
so it makes sense to have it record the video feed as well. Trip
Viewer
Allow bidders to view details about the current
trip up for bid
Wait—it doesn’t make sense for any of the other components
Creating new components is known as
we identified earlier to take on this responsibility. Let’s create
evolving the architecture.
a new component to handle it.


```

138  Chapter 4

<a id='p175'></a>
<!-- Página 175 -->

```
logical components



Sharpen your pencil
```

Your company, Going Green Corporation, wants a system to support its new electronics recycling program, where
customers can send in their old electronic devices (like cell phones) and get money. We’ve already identified some
of the initial core components. Your job is to figure out which component should be responsible for each of the
functionalities listed below, or if a new component is needed. You’ll also need to come up with names for any new
components.

```
Physically Assess the Recycle or
receive the device’s resell the old
device from Device condition Device device.
Device
Receiving the customer. Assessment Recycling



```

Locate the nearest safe disposal facility for destroying the device
```
Device Receiving Device Assessment Device Recycling Other:


```

Capture and store customer information (name, address, etc.)
```
Device Receiving Device Assessment Device Recycling Other:


```

Post the device on a third-party site to resell it on the secondary market
```
Device Receiving Device Assessment Device Recycling Other:


```

Pay the customer for their recycled device
```
Device Receiving Device Assessment Device Recycling Other:


```

Record that the device has been received and is ready for assessment and valuation
```
Device Receiving Device Assessment Device Recycling Other:


```

Determine the value (if any) of the recycled device
```
Device Receiving Device Assessment Device Recycling Other:


```

Determine the monthly profit and loss for recycled and resold devices
```
Device Receiving Device Assessment Device Recycling Other:

Going Green Corp. needs to make a profit, afte
r all.
Solution on page 161

you are here 4  139
```


<a id='p176'></a>
<!-- Página 176 -->

analyzing roles and responsibilities



Step 3: Analyze roles and responsibilities
As you start assigning functionality (in other words, user stories or requirements)
to logical components, the roles and responsibilities of each component will start
to naturally grow. The purpose of this step is to make sure that the component
to which you are assigning functionality should actually be responsible for that
functionality and that it doesn’t end up doing too much.
Let’s say we create a component called Live Auction Session that has the following
responsibilities during a live auction:


```
1. Start and stop the auction
Live Auction
2. Show the current trip up for bid
Session
3. Mark a trip as sold and move to the next trip

This is a well-designed component and has just the right amount of
responsibility. However, as iterations move forward, the development team
adds some new requirements to the Live Auction Session component:


4. Display the details of each trip in this auction Hey,
component,
5. Keep track of all the bidders currently in the auction can you wash
6. Keep track of each winning bidder for the auction my car too?
If you’ve ever had too 7. Notify the bidder that they won the trip
much on your plate at
work, you likely gave
some of that work to With this added functionality, this component is now taking on too much
others. Do the same with responsibility. This is a common situation, so don’t be surprised if it happens
components—offload to you. When it does, don’t panic—that’s what this step is here for. Let’s see
some of the responsibility if we can fix this situation by moving some of the responsibility of the Live
to someone else. Auction Session component to other components.




Geek Note
Have you ever created a class file called Utility? What did it do? Chances are it contained a bunch of unrelated
functions that you’d had a hard time placing. The same thing can happen with logical components within software
architecture. Try to avoid components that contain lots of unrelated functions.




```

140  Chapter 4

<a id='p177'></a>
<!-- Página 177 -->

```
logical components



```

Sticking to cohesion
When you analyze a component’s role and responsibility statement
or set of operations, check to see if the functionality is closely related.
This is known as cohesion: the degree and manner to which the Ma ke it
operations of a component are interrelated. Cohesion is a useful tool
for making sure a component has the right responsibilities. Stick
When analyzing the role and responsibilities of a component, it’s
common to find an outlier (an odd piece of functionality) or a Component functions
```
should all be rel
```

component that is doing too much. In these cases, it’s usually a good but if they’re not, do
```
Just start to break then’t get frustrated. ated—
```

idea to shift some of the responsibility to other components. and you’ll be conside component apart,
```
red very smart.
```

Now it’s your turn to fix the Live Auction Session component.




```
Exercise
See if you can offload some of the responsibility of the Live Auction Session component to others by creating new
components to handle the additional functionality. Keep the first three original requirements associated with the Live
Auction Session.

We did this 1. Start and stop the auction
one for you. Live Auction
2. Show the current trip up for bid
Session
3. Mark a trip as sold and move to the next trip

components
Draw your nehwere.
in this space 4. Display the details of each trip in this auction


5. Keep track of all the bidders currently in the auction


6. Keep track of each winning bidder for the auction


7. Notify the bidder that they won the trip

Hint: You might consider combining a few of these
requirements when creating new components.
Solution on page 162

you are here 4  141
```


<a id='p178'></a>
<!-- Página 178 -->

analyzing characteristics



Step 4: Analyze characteristics
The final step in identifying initial core components is to verify that each
component aligns with the driving architectural characteristics that are
critical for success. In most cases this involves breaking apart a component
for better scalability, elasticity, or availability, but it could also involve putting
components together if their functionalities are tightly coupled.
Let’s look once again at our Adventurous Auctions example. We previously
identified a Bid Capture component that is responsible for accepting bids, storing
all bids in a Bid Tracker database, and forwarding the highest bid to the auctioneer. Here is
the overall flow for the Bid Capture component:

```
Sam the
Kate auctioneer
I really want this trip. I see there are
lots of other bidders, so I’m going to We have $2,000
raise my bid to $2,000. from online bidder
Kate. Do I hear
$2,100? Going once,
going twice...
Bid
Capture
Kate’s bid was Let’s
All bids are stored the highest! wins he hope Kate
in this database for r trip.
tracking purposes.




This architecture looks good, but just to be sure, we should make sure the Bid Capture
component supports the system’s critical architectural characteristics (those that are
important for success).
These are all
important to We know the system has to support thousands of bidders per second—that’s scalability.
the success We also know the system must be up and running while auctions are taking place—that’s
Adventurous oAf availability. Finally, the system must accept a bid and get it to the auctioneer as fast as
uctions. possible—that’s performance.
Now it’s your turn to analyze the Bid Capture component against these critical
architectural characteristics.




```

142  Chapter 4

<a id='p179'></a>
<!-- Página 179 -->

```
logical components




BE the architect These are the critical architectural
characteristics for Adventurous Auctions:
Your job is to play architect Scalability: The system has to support
and analyze the Bid Capture thousands of bidders per second
component on the previous Availability: The system must be up and running
page to see if it should be while the auctions are taking place
modified based on the critical Performance: The system must accept a bid and
architectural characteristics get it to the auctioneer as fast as
we identified. Our solution is possible.
on the next page.

```

Hints (things to consider):
```
What if the database goes down?
Can the database keep up with the volume of inserts based on the bids coming in?
Will inserts into the database be fast enough to get the bids to the auctioneer?
Consider the actions the Bid Capture component has to take upon receiving a bid.

ge the Bid
```

Use this area to draw how you might chanarch
Capture component based on the critical itectural
characteristics and considerations above.




```
you are here 4  143
```


<a id='p180'></a>
<!-- Página 180 -->

analyzing characteristics



The Bid Capture component
Let’s work through this exercise by reviewing the current responsibilities of the Bid Capture component:
1. Accept bids from online bidders and from the auctioneer for live bidders.
2. Determine which online bid is the highest.
3. Write all bids to a Bid Tracker database for tracking purposes.
4. Notify the auctioneer of the highest bid.
It makes sense for the Bid Capture component to write the bids to the database, since This is what
it has them. But database connections and throughput are limited, so having Bid analyzing charwe mean by
```
acteristics.
```

Capture do this significantly impacts scalability. It also impacts performance by adding
wait time for writing the data to the database, as well as availability if the database were
ever to go down.

If we assign the last requirement to a new component called Bid Tracker, we can
significantly increase the scalability, performance, and availability of the Bid
Capture component. That lets the system process more bids faster and get the
highest bid to the auctioneer as quickly as possible. The Bid Capture component can You might break apart
send the bids to the Bid Tracker and won’t have to wait for the bid to be written to or combine components
the database. in this step, based on the
```
architectural characteristics
needed.
The Bid Capture
```

Kate has a component can process er, no longer
winning the tbet ter chance of
```
more bids now that it is Sam, the auctiorneonline bids to
ri p
```

bidding process now that the no longer storing them. has to wait fo database.
```
is faster. be saved in the


Bid
Capture
This is a new
component.
Bid
Tracker
The Bid Capture component
can asynchronously send the
bid without having to wait
for it to be stored. The Bid Tracker compon
take as much time as it ent can
save the bids to the dataneeds to
base.



```

144  Chapter 4

<a id='p181'></a>
<!-- Página 181 -->

```
logical components



```

Component coupling



```
I should probably start thinking about
how the logical components interact
with and depend on each other, right?




Yes, and this is the right time to do it.
As you identify the initial core components, it’s important to determine
how they interact. This is known as component coupling: the degree
to which components know about and rely on each other. The more
the components interact, the more tightly coupled the system is and the
harder it will be to maintain.


Remember this diagram from
several pages ago? It’s called a “big
ball of mud” because there are so
many component interactions and
dependencies that the diagram starts
to look like a ball of mud (or maybe
like a bowl of spaghetti).

That’s why it’s so important to pay attention to how components interact
and what dependencies exist between them.
You need to be concerned about two types of coupling when creating
logical components: afferent coupling and efferent coupling. Don’t be
concerned if you’ve never heard these formal terms before—we’re going
to explain them in the following pages.




you are here 4  145
```


<a id='p182'></a>
<!-- Página 182 -->

component coupling



Afferent coupling
Children depend on their parents for a lot of things, like making sure
they have plenty of food to eat and a safe place to live, driving them to
soccer practice, or even giving them an allowance so they can buy candy
or a really cool comic book. As it turns out, parents are afferently coupled
to their children, and even to the family dog, because all of them depend
on the parents for something. Everyone is
Afferent coupling is the degree and manner to which other dependent
components are dependent on some target component (in this case, on Mom.
Mom). It’s sometimes referred to as fan-in, or incoming, coupling. In
most code analysis tools, it’s simply denoted as CA.



```
Responsible for allowing Mom is afferently
bidders to sign up for an coupled to the family.
auction
Responsible for managing
all of the information
about a bidder To see how afferent coupling works, look
Auction at the interaction between three of the
Registration logical components within the Adventurous
Auctions logical architecture on the left.
Bidder
Profile Both the Auction Registration component
and the Automatic Payment component
Automatic depend on the Bidder Profile component
Payment to return bidder profile information. In this
scenario, the Bidder Profile component has
an afferent coupling level of 2, because two
Responsible for charging components depend on it to complete their
the winning bidder’s work.
credit card



Geek Note
Did you know that the odd-sounding word afferent means “carrying toward”? It gets its roots from the Latin words
ad (meaning “to” or “toward”) and ferre (“to carry”). In the medical field, the word afferent refers to nerves that carry
impulses to the brain (your afferent nerves).




```

146  Chapter 4

<a id='p183'></a>
<!-- Página 183 -->

```
logical components



Efferent coupling
These
This is Josh. Josh’s are Now let’s look at things from a young child’s point of
parent view. As a child, you might have been dependent not
s.
only on your parents, but also your teachers, friends,
classmates, and so on. Being dependent on others is
known as efferent coupling.
Josh is dep
on these peeondent Efferent coupling is exactly the opposite of afferent
which means ple, coupling, and it’s measured by the number of
efferently c he’s components on which a target component depends. It’s
to them. oupled also known as fan-out coupling or outgoing coupling. In static
source code analysis tools, it’s usually denoted as CE.

So, what does efferent coupling look like with logical
components? Let’s take a look at Adventurous Auctions again,
this time considering the process of accepting a bid from Kate
This is Josh’s for a trip.
teacher.



Responsible for Responsible
receiving bids, each highestfor streaming
Hello again, determining the
Kate! highest one , and the online bidbid to all
ders
notifying the
auctioneer
Bid
Streamer
Bid
Capture
Bid
Tracker Responsible for storing every
bid received in a database for
future reporting


```

Because the Bid Capture component depends on the Bid Streamer and Bid Tracker
components to process a bid, it is efferently coupled to these components. It has an efferent
coupling level of 2 (in other words, it’s dependent on two other components).




```
you are here 4  147
```


<a id='p184'></a>
<!-- Página 184 -->

coupling level



Measuring coupling
You can measure a particular component’s amount of coupling in three ways:
by considering its total afferent coupling (CA), its total efferent coupling This logical
(CE), and its total coupling (CT), or the sum of the total afferent and efferent architecture has
```
a total couplin
(CT) level of 6.g
```

coupling. These measurements tell you which components have the highest
and lowest coupling, as well as the entire system’s overall coupling level.


## CA + CE = CT


## CA=1 CE=0

```
is
```

You can use ttho track CA=0 CE=1 CA=1 CE=2
```
Bid
n
```

informatio gs are Streamer
whether thin or less Bid Bid CT=1
getting more time. Placer Capture CA=1
```
coupled over CE=0
CT=1 CT=3 Bid
Tracker
```


## CT=1

```
Sharpen your pencil
Given the components below, can you identify the total afferent coupling (CA), total efferent
coupling (CE), and total coupling (CT) for each component? Also, what is the total coupling level
```

for this logical architecture? Does the CT for this architecture seem high or low to you?
```
CA=1 We did this one
fo r you.
```


## CE=0


## CT=1

```
Component
A Component Component
B Component H
```


## G



```
Component
D Component
Component
```


## K


## C

```
Component
```


## I


```
Component
Component
```


## L


## F

```
Component Component
```


## E J



```
Total system coupling level:
Solution on page 163

```

148  Chapter 4

<a id='p185'></a>
<!-- Página 185 -->

```
logical components




Okay, now I get coupling and how
to measure it. But how do I reduce
component coupling to create loosely
coupled systems?




```

Great question. Developers are taught to strive for loosely
coupled systems, but not how to do it. We’ll show you how by
introducing a technique called the Law of Demeter.
The Law of Demeter, also known as the Principle of Least
Knowledge, is named after Demeter, the Greek goddess of
agriculture. She produced all grain for mortals to use, but she had
no knowledge of what they did with the grain. Because of this,
Demeter was loosely coupled to the mortal world.
Logical components work in the same way. The more knowledge
a component has about other components and what needs to
happen in the system, the more coupled it is to those components.
By reducing its knowledge of other components, we reduce that
component’s level of coupling.
On the next few pages, we’ll show you more about the Law of
Demeter and how it can be used to decouple systems.




```
you are here 4  149
```


<a id='p186'></a>
<!-- Página 186 -->

tight coupling



A tightly coupled system
Let’s see how the Law of Demeter can be used to decouple systems by taking a
```
The com
architectpuonents in this
```

look at the logical architecture of a typical order entry system.
```
defined in re are well
individual terms of their
responsibil
The Order Placement CA=1
ities.
component sure does know a CE=4
lot about placing an order. CT=5
```


## CT=1


```
Order Decrement inventory Inventory
Place an order
Placement Management
Sto
ck l
ow?
Notify the Ord
Stock er m
customer ore
low?
Raise CT=1
CT=1 the price Now
that’s Supplier
CT=1 not nice.
Email Ordering
Notification Item
Pricing Total System Coupling = 9




Brain
Power
What possible issues do you see with the logical architecture above? We’ve provided some (but not all)
potential problems. Check off the ones you think might be an issue, and write down any other possible issues
you see with this logical architecture.

The customer might not be available to get their email when it’s sent.
The supplier might not have stock on hand.
The Order Placement component knows too much about the steps involved in placing an order.




```

150  Chapter 4

<a id='p187'></a>
<!-- Página 187 -->

```
logical components



```

Applying the Law of Demeter
The total system coupling level didn’t bother us that much. What does bother us is how tightly
coupled the Order Placement component is (CT=5), how unbalanced the component coupling
is, and how much knowledge the Order Placement component has about the order placement
```
The Ord
Placementer
```

process.
Let’s apply the Law of Demeter to fix these problems by moving the “low stock” knowledge to compone
the Inventory Management component. taking chnat is
```
rge.

```


## CA=1

```
CA=1 We reduced coupling for this
```


## CE=2

```
CE=2 component, but increased it here.
```


## CT=3


## CT=3

```
Order Decrement inventory Inventory
Place an order
Placement Management
Notify the e
customer p ric
Less knowledge, e the
CT=1 hence less coupling. R ais Stock low?
o w? Order more
c kl
Sto
Email
Notification CT=1
```


## CT=1

```
Item
Pricing Supplier
Ordering


```

By moving the knowledge of actions to take for a Total System Coupling = 9
“low stock” condition to Inventory Management,
we reduced the amount of knowledge about
the system, and hence the coupling, of the
Order Placement component However, we
increased the knowledge of the Inventory Geek Note
Management component, and thus increased
its coupling. This is what the Law of Demeter Did you notice that while we reduced the coupling of the
is all about—less knowledge, less coupling; Order Placement component, the total system coupling level
more knowledge, more coupling. remained the same? That’s because we didn’t remove the
```
knowledge from the system, we just moved it to another
h
about how muc
```

Coupling is aollmponents have
```
component—Inventory Management.

```

knowledge c st of the system.
```
about the re

you are here 4  151
```


<a id='p188'></a>
<!-- Página 188 -->

reducing coupling



```
Test Drive
```

Now it’s time to take the Law of Demeter for a test drive to see if you can decouple a logical architecture. Below is
a logical architecture for a system where customers who have purchased a support plan with an electronic item can
submit a trouble ticket and have an expert come out to fix the item. Here’s how it currently works:
```
1 A customer creates a ticket.
2 The ticket gets assigned to an available expert in the field.
3 The ticket is uploaded to an app on the expert’s mobile device (that’s Ticket Routing).
4 The customer is notified that the expert is on their way to fix the problem.
5 Once the expert fixes the problem, they mark the ticket as completed.
```

Keeping the components the same, how can you make this architecture more loosely coupled?

```
find an expert
Ticket Ticket This is the expe
Creation sen
d tic Assignment device with an aprt’s mobile
to e
ket p on it..
xpe
notify the customer rt
that the expert is Ticket upload ticket problem fixed Ticket
on their way Routing Completion
solutio n
Customer Draw your
Notification here.




Solution on page 164

```

152  Chapter 4

<a id='p189'></a>
<!-- Página 189 -->

```
logical components



```

A balancing act
Do you remember the First Law of Software Architecture? Here it is again
(because it’s so important):

Everything in software architecture is a trade-off.
Loose coupling is no exception. Let’s compare the two architectures we’ve just
seen and analyze their trade-offs.


```
Tightly coupled
With the tightly coupled architecture, if
you want to know what happens when a
customer places an order, you only have to
look at the Order Placement component to
understand the workflow.
However, in this case, the Order Placement
component is dependent on four other
components. If any one of those
components changes, it could break the
Centralized workflow, but more risk with each change Order Placement component.


```

These are the trade-offs for tight coupling.
```
Loosely coupled
```

With loose coupling, you distribute the
knowledge about what needs to happen, so
that no one component knows all the steps.
If you want to understand the workflow of
placing an order, you have to go to multiple
components to get the full picture.
However, changing the Item Pricing
and Supplier Ordering components will
no longer affect the Order Placement
component.
```
Distributed workflow, but less risk with each change

These are the trade-offs for tight coupling.
This is a good
rule to remember.
Two components are coupled if a change in one component
might cause a change in the other component.

you are here 4  153
```


<a id='p190'></a>
<!-- Página 190 -->

chapter summary



Some final words about components
Congratulations! Now that you can identify logical components and the dependencies
between them, you’re on your way to creating a software architecture. We know this was
a long chapter, but it’s also an important one. Thinking about a system as a collection of
logical components helps you, as an architect, better understand its overall structure and
how it works.
In the next part of your software architectural journey, you’ll be focusing on the
technical details of the system—things like architecture styles, services, databases, and
communication protocols. But before you go, review the following bullet points to make
sure you fully understand everything about logical components.



Bullet Points
 Logical components are the functional building blocks  Coupling happens when components depend on one
```
of a system. other to perform a business function.
```

 A logical component is represented by a directory  Afferent coupling, also known as incoming coupling,
```
structure—the folder where you put your source code. occurs when other components are dependent on a
target component.
```

 When naming a component, be sure to provide
```
a descriptive name to clearly identify what the  Efferent coupling, also known as outgoing coupling,
component does. occurs when a target component is dependent on
other components.
```

 Creating a logical architecture involves four
```
continuous steps: identify components, assign  Components having too much knowledge about what
requirements, analyze component responsibilities, needs to happen in the system increases component
and analyze architectural characteristics. coupling.
```

 You can use the workflow approach to identify initial  The Law of Demeter states that services or
```
core logical components by assigning the steps in a components should have limited knowledge of other
primary customer journey to components. services or components. This law is useful for creating
loosely coupled systems.
```

 You can use the actor/action approach to identify
```
initial core logical components by identifying the  While loose coupling reduces dependencies between
actors in the system and assigning their actions to components, it also distributes workflow knowledge,
components. making it harder to manage and control that
knowledge.
```

 The entity trap is an approach that models
```
components after major entities in the system. Avoid  Determining the total coupling (CT) of a logical
using this approach, because it creates ambiguous architecture involves adding the afferent and efferent
components that are too large and have too much coupling levels for each component (CA + CE).
responsibility.
```

 When assigning requirements to components, review
```
each component’s role and responsibilities to make
sure it should be performing that function.




```

154  Chapter 4

<a id='p191'></a>
<!-- Página 191 -->

```
logical components



Logical Components Crossword
Now’s your chance to have a little fun and see how much knowledge you’ve gained.
See if you can fill in this crossword puzzle with clues about logical components.




```

Across Down
3. Each component performs a _____ 1. A component’s _____ is about how interrelated its operations
4. _____ gateways appear in a physical architecture but not a are
logical one 2. Give each component a descriptive _____
6. A physical architecture associates _____ with components 5. Afferent and efferent coupling are both forms of _____
7. One system component might be a live video _____ coupling
9. Avoid building a big ball of _____ 8. The Principle of Least Knowledge is also called the Law of
11. Be sure to avoid the _____ trap _____
12. Coupling might be _____ or efferent 10. A good place to look for components is the codebase’s _____
13. Logical _____ are the functional building blocks of a system structure
16. Early on, you’ll identify _____ core components 12. Step 2 is to _____ requirements to logical components
19. A user’s journey through the system is called their _____ 14. An architecture diagram can show the logical or _____
20. Each logical component has a _____ and a responsibility architecture
```
15. Adventurous Auctions lets users _____ on trips
17. You can identify components with an _____/action
approach
18. Identifying logical components may involve taking your best
Solution on page 165 _____


you are here 4  155
```


<a id='p192'></a>
<!-- Página 192 -->

exercise solutions


```
Exercise From page 125
Solution
Name that component
It’s your first week on the job as the new architect, and you’ve been assigned to an existing project to build a
trouble ticket system. You want to understand the logical components of the architecture, but your team doesn’t
know anything about logical components—they just started coding. To determine the logical architecture, you
have to look at the existing directory structure. How many individual logical components can you identify from the
codebase below? Here are our answers.



order_entry_app We did Shopping
order this one Cart

shopping_cart for you!
lots_of_source_code_files

fulfillment Order
Fulfillment
lots_of_source_code_files

history
Recent Order
recent
History
lots_of_source_code_files

archive
Archived
lots_of_source_code_files Order History

Payment
credit_card Credit Card
Payment
lots_of_source_code_files

gift_card
lots_of_source_code_files Gift Card
Payment
customer
profile Customer
lots_of_source_code_files Profile




```

156  Chapter 4

<a id='p193'></a>
<!-- Página 193 -->

```
logical components



Who Does What From page 128


Solution
```

We had our logical and physical architecture responsibilities all figured out, but somehow they got all mixed up.
Can you help us figure out who does what? Be careful—some responsibilities may not have a match (they aren’t
part of a logical or physical architecture).



```
This is part of implementation, Shows which programming language is used for
not architecture. each component



Logical Maps components to services

```

architecture
```
Shows the logical components within the system
and how they communicate with each other



Shows how many databases there are in the
system and which services access them



Shows communication between services and the
protocol they use (like REST)

Physical
architecture Shows the source code files used to implement a
component



Shows the components and their interactions
within the user interface



Shows the API gateways and load balancers used
in the system


you are here 4  157
```


<a id='p194'></a>
<!-- Página 194 -->

exercise solutions


```
From page 133
Sharpen your pencil
Solution
Your company wants a new system to assign workers to construction sites, and it’s your
job as the software architect to identify its initial core components. Using the workflow
approach, identify as many core components as you can, matching each to its associated
workflow step. Remember, a workflow step can have multiple components, and not every
workflow step has to have a unique component.

Step 1: Maintain a list of all construction workers, their skills, and their locations
Step 2: Create a new construction project and specify the work site

Step 3: Create a schedule for when various construction projects start and end
Step 4: When a new project starts, assign workers based on their skills and locations
Step 5: When the project completes, free up workers so they can be reassigned

Draw your logi
this space. Remca
em
l components in
good descriptive ber to give them
names.




Step 1 Step 2 Step 3 Step 4 Step 5




Contractor Contractor Create Schedule Contractor
Profile Site Location Project Project Assignment



It makes sense to have two The Contractor Assignment
components because the profile component can handle both
is relatively static, whereas the assigning contractors (step 4) and
location changes a lot. unassigning them (step 5).




```

158  Chapter 4

<a id='p195'></a>
<!-- Página 195 -->

```
logical components


Exercise From page 135
Solution
```

You have a bakery that is ready to expand operations, and you would like a new system that lets customers view,
order, and pay for bakery items online for pickup. Orders are sent to the bakery coordinator, who purchases
ingredients and schedules orders. The baker receives the schedule of items to bake each morning, and tells the
system when the items are baked. The system then emails the customers to let them know their items are ready
for pickup.
Using the actor/action approach, identify what actions each actor might take, then draw as many logical
components as you can for the new bakery system, matching the actions you identified to the components.



```
Item
Browser

Customer
Shopping
Browse items Cart
Select items

Pay for items Item
Checkout
Receive email that
order is ready
Email
Notification
Bakery Coordinator
Receive order
Determine ingredients Item
Recipes
Check current stock
Schedule order
Ingredients
Stock



Baker Schedule
Order
Receive baking
schedule

Mark order as ready Order
for pickup Status




you are here 4  159
```


<a id='p196'></a>
<!-- Página 196 -->

exercise solutions




```
From page 136
Sharpen your pencil
Solution
What other words besides manager can you list that, if they appeared in a component name, might indicate that
you’ve fallen into the entity trap?
agent Add th
We did this
supervisor the fronetword “Order” t
one for you.
handler
and you’ll of these word o
see what s
controller service
we mean.
utility
engine

worker mediator orchestrator
coordinator processor




Exercise From page 137
Solution
Can you select the most appropriate approach to identifying initial core components in the following scenarios? In
some cases, more than one approach may be appropriate.

The system has only one type of user Workflow Actor/Action
The system has well-defined entities Workflow Actor/Action
the
You have minimal functional requirements Workflow Remember to avoidif
entity trap, even llActor/Action
The system has many complex user journeys Workflow Actor/Action the system has we.
The system has many types of users Workflow Actor/Action
defined entities
Neither approach
requires lots of
functionality to
create initial logical
components.




```

160  Chapter 4

<a id='p197'></a>
<!-- Página 197 -->

```
logical components




From page 139
Sharpen your pencil
Solution
```

Your company, Going Green Corporation, wants a system to support its new electronics recycling program, where
customers can send in their old electronic devices (like cell phones) and get money. We’ve already identified some
of the initial core components. Your job is to figure out which component should be responsible for each of the
functionalities listed below, or if a new component is needed. You’ll also need to come up with names for any new
components.

```
Physically Assess the Recycle or
receive the device’s resell the old
device from Device condition Device device.
Device
Receiving the customer. Assessment Recycling

```

Locate the nearest safe disposal facility for destroying the device
```
Device Receiving Device Assessment Device Recycling Other:


```

Capture and store the customer information (name, address, etc.)
```
Device Receiving Device Assessment Device Recycling Other: Customer Profile


```

Post the device on a third-party site to resell it on the secondary market
```
Device Receiving Device Assessment Device Recycling Other:


```

Pay the customer for their recycled device
```
Device Receiving Device Assessment Device Recycling Other: Accounts Payable


```

Record that the device has been received and is ready for assessment and valuation
```
Device Receiving Device Assessment Device Recycling Other:


```

Determine the value (if any) of the recycled device
```
Device Receiving Device Assessment Device Recycling Other:


```

Determine the monthly profit and loss for recycled and resold devices
```
Device Receiving Device Assessment Device Recycling Other: Financial Reporting

Going Green Corp. needs to make a profit, afte
r all.


you are here 4  161
```


<a id='p198'></a>
<!-- Página 198 -->

exercise solutions



```
Exercise From page 141
Solution
```

See if you can offload some of the responsibility of the Live Auction Session component to others by creating new
components to handle the additional functionality. Keep the first three original requirements associated with the Live
Auction Session.


```
We did this 1. Start and stop the auction
one for you. Live Auction
2. Show the current trip up for bid
Session
3. Mark a trip as sold and move to the next trip

components
```

Draw your nehwere.
in this space


```
Trip 4. Display the details of each trip in this auction
Viewer



5. Keep track of all the bidders currently in the auction
Bidder
Tracker
ese two ha ve to do wit h tracking bidders, so they
Th gether.
should probably be placed to
6. Keep track of each winning bidder for the auction


Winner
Notification
7. Notify the bidder that they won the trip



Hint: You might consider combining a few of these
requirements when creating new components.


```

162  Chapter 4

<a id='p199'></a>
<!-- Página 199 -->

```
logical components




From page 148
Sharpen your pencil
Solution
Given the components below, can you identify the total afferent coupling (CA), total efferent
```

coupling (CE), and total coupling (CT) for each component? Also, what is the total coupling level for this logical
architecture? Does the CT for this architecture seem high or low to you?

CA=0 CA=1 We did this one CA=0
CE=1 fo r you. CE=0

## CE=0

CT=1 CT=1 CT=0
```
Component CA=0 Component
A Component CE=1
B Component H
```


## CT=1


## G


## CA=1

```
CA=2 CA=2 CE=0
CE=0 Component CE=3 CT=1
CT=2 Component D CT=5 Component
```


## CA=0 K


## C

```
CE=2 Component
```


## CT=2 I


## CA=1

```
CE=0 Component CA=0
Component
```


## CT=1 F


## L

```
Component CE=2 Component
E CT=2 J CA=1 CA=1
```


## CE=0 CE=0


## CT=1 CT=1

```
Total system coupling level: 18. This seems high to us.




you are here 4  163
```


<a id='p200'></a>
<!-- Página 200 -->

exercise solutions


```
From page 152
Test Drive Solution
```

It’s time to take the Law of Demeter for a test drive to see if you can decouple a logical architecture. Below is a logical
architecture for a system where customers who have purchased a support plan with an electronic item can submit a
trouble ticket and have an expert come out to fix the item. Here’s how it currently works:
```
1 A customer creates a ticket.
2 The ticket gets assigned to an available expert in the field.
3 The ticket is uploaded to an app on the expert’s mobile device (that’s Ticket Routing).
4 The customer is notified that the expert is on their way to fix the problem.
5 Once the expert fixes the problem, they mark the ticket as completed.
```

Keeping the components the same, how can you make this architecture more loosely coupled?



```
Ticket find an expert Ticket This is the expe
Creation sen
d tic Assignment device with an aprt’s mobile
ket
to e
p on it.
xpe
notify the customer rt
that the expert is Ticket upload ticket problem fixed Ticket
on their way Routing Completion
Customer
solution in
Draw youer here.
Notification

this spac



find an expert The Ticket Creat
Ticket Ticket
less knowledge ab ion component has
Creation Assignment
happen, and thereout what needs to
fore lower couplin
g.
send ticket to expert



Customer Ticket upload ticket problem fixed Ticket
Notification notify the customer Routing Completion
that the expert is
on their way



```

164  Chapter 4

<a id='p201'></a>
<!-- Página 201 -->

```
logical components


```

Logical Components Crossword Solution
```
From page 155




you are here 4  165
```


<a id='p202'></a>
<!-- Página 202 -->


<a id='p203'></a>
<!-- Página 203 -->

5 Categorization and
```
architectural styles


Philosophies




```

There are lots of different architectural styles out there. Each one exists
for a reason and has its own philosophy about how and when it should be used. Understanding
a style’s philosophy will help you judge whether it’s the right one for your domain. This chapter
gives you a framework for the different kinds of architectural styles (which we’ll be diving into for
the remainder of this book), to help you make sense of these and all the other architectural styles
you’ll encounter as a software architect.

Let’s fill in that final piece of the puzzle, shall we?




```
this is a new chapter   167
```


<a id='p204'></a>
<!-- Página 204 -->

architectural style fundamentals



There are lots of architectural styles
You’ve learned a lot about software architecture so far, but there’s one
thing we still haven’t talked about: architectural styles. That's what
we'll do in this chapter—in fact, the rest of this book is dedicated to
architectural styles!
```
There’s a piece
missing.
```

Before we get started: look around your neighborhood, then watch a
show or movie set in a different part of the world. How many styles of
homes do you see? There are literally hundreds—all influenced by the
locale, weather, and the owners’ personal preferences. New styles are
created every day.




```
Each one of these
styles exists for a
reason—be that
historical, cultural, or
technical.


And there’s our
missing piece!
```

That’s true for architectural styles in software, too. There are so many out there that
even in a book this big, try as we might, we’ll barely scratch the surface of all the
available styles.
This chapter will give you a framework for thinking about architecture and
architectural styles in general. Then, in the chapters that follow, we’ll dive deep into
a handful of specific architectural styles and examine their philosophies, using what
you learn in this chapter. Understanding a few crucial styles will leave you with a good
foundation to understand others as you encounter them.
Let’s do this.




168  Chapter 5

<a id='p205'></a>
<!-- Página 205 -->

```
architectural styles



```

The world of architectural styles
If you’ve done software development for any length of time, you may have heard
about different architectural styles, like monoliths and microservices. To help us think
systematically about them, we place them into two categories. The first deals with how
the code is divided: either by technical concerns or by domain (business) concerns.
The second category is about how the system is deployed: is all the code in the system Recall from Chapter
delivered as one unit, or as multiple units? 2 that the domain is
```
“the thing you’re writing
software about.”
these axes
```

We’ll describweing pages.
in the follo st let it wash
For now, ju
```
Partitioning

```

over you. We have entire
```
Technical Domain
chapters dedicated to
each style mentioned
Layered here.



Deployment model
Monolith Modular monolith
Microkernel


Distributed
Event-driven Microservices




```

As you can see, there are multiple ways to slice and dice architectural styles. This We won’t spend time
doesn’t cover everything, of course—there are domain-specific architectures that are on domain-specific
built explictly for certain problems—but a book can only be so long. architectures in this
```
book. Let’s just say
```

Each category reveals some of the architectural characteristics of its styles. For example, they don’t appeal to a
architectural styles delivered as one unit are easier to understand, but those delivered as broad audience.
multiple units tend to scale better.
Let’s examine each category.




```
you are here 4  169
```


<a id='p206'></a>
<!-- Página 206 -->

partitioning types



Partitioning: Technical versus domain
Think back to the last time you had dinner at a fancy restaurant. When you walked in,
a host probably greeted you and escorted you to a table. A server offered you drinks and
menus and explained the specials. The chef and other cooks prepared your food for you.
When you finished your meal, a busser cleaned and reset the table.
These restaurant workers’ duties are separated by technical concern. A busser’s role
isn’t to welcome you, and you probably don’t want the server cooking your food.
Now, think back to the last application you worked on. Did it have a controller layer?
Did it have services? How about a persistence tier? If so, congratulations: you’ve
already worked on a technically partitioned architecture.
In a technically partitioned architecture, code is divvied up by technical concerns— Another analogy that might
there might be a presentation tier, a business (services) layer, and so on. The principle at help is a burger, with two
play here is separation by concern—which most people think about in horizontal layers. halves of a bun, condiments,
```
veggies, and a patty—each
layer has a distinct and
separate role.
Presentation
Each layer serves
a particular Services
technical concern.
Persistence


Each of these restaurants
```

On the other hand, imagine a food court. It has lots of restaurants, each specializing in might have servers and
a particular kind of food: pizza, salads, stir-fry, burgers. In other words, each restaurant bussers. But at a high level,
has a specific domain. the restaurant specializes in
In domain-partitioned architectures, the structure of the system is aligned with the
```
a particular kind of food.
```

domain. Rather than by roles, the code (and systems) are separated in ways that align
with the problem you’re attempting to solve.
```
We’ll dive into a lot
of these details in
future chapters.
payment
customer shipping


In domain-partitioned
architectures, your code is
divided with the domain in mind.



```

170  Chapter 5

<a id='p207'></a>
<!-- Página 207 -->

```
architectural styles


there are no
Dumb Questions
```

Q: In a domain-partitioned architecture, where do the Q: Domain partitioning is pretty logical. Frankly, it
presentation and services layers reside? sounds better. So why would anyone use technical
```
partitioning?
```

A: In a domain-partitioned architecture, you are making
the domain the “first-class citizen,” leaving the technical A: We prefer not to use value judgments such as “better” and
implementation as just that: implementation. The logical “best” when discussing architectural styles. (You’re going to get
components that make up your architecture are organized tired of us saying this!) Your choice of architectural style will
around the domain, as opposed to the role they perform. always be driven by a variety of factors, as you know, including
```
the domain and the required architectural characteristics.
```

A technically partitioned architecture’s components might
be organized in namespaces like app.presentation. Technical partitioning is great if your teams tend to specialize—
customer or app.services.customer. Note how the say, if you have teams of frontend experts, backend developers,
customer domain appears within the technical partition. However, and database administrators. But domain partitioning better
in a domain-partitioned architecture, you’ll have namespaces like aligns your system with the actual problem at hand.
app.customer.presentation and app.customer.
services.




```
Exercise
```

A short-order cook pretty much does everything. They can cook everything on the menu, from fries to sandwiches, as
well as blending smoothies and plating desserts. Often, they also serve food, take payments, and even clean tables
after customers leave. Would you categorize a short-order cook’s work as partitioned technically or by domain? Why?
Jot down your thoughts here.




```
Solution on page 182

you are here 4  171
```


<a id='p208'></a>
<!-- Página 208 -->

deployment model types



Deployment model: Monolithic
versus distributed
Let’s play a game—we say a word, and you respond with the first thing that pops
into your mind. Ready? Monolith.
We don’t know about you, but this word makes us think of something like a boulder
or a glacier—something big. That’s exactly what monolithic architectures represent.
```
This would be like packag
and deploying your entir ing
```

In a monolithic architecture, you deploy all the logical components that make up
```
application as a single WAe
```

your application as one unit. This also means that your entire applications runs as one
```
or JAR file in the Java R
```

process.
```
ecosystem, or as an ex
This is a monolithic in the .NET world. ecutable
application, Customer
containing all the
logical components Payment
in one deployment
unit. Recall that architect
Shipping
characteristics influencureal
the structure of the
application.
```

In a distributed architecture, by contrast, you split up the logical components
that make up the application across many (usually smaller) units. These units each
run in their own process and communicate with each other over the network.




Distributed
architectures Customer Shipping

deploy lots of Payment
smaller units.


There’s a lot to this distinction, so let’s talk about the pros and cons of both types.




172  Chapter 5

<a id='p209'></a>
<!-- Página 209 -->

```
architectural styles




Exercise
```

Take a moment and consider your smartphone. It does it all—it lets you take pictures and videos, browse the web,
post to your favorite social networking site, track your fitness activity, and navigate via GPS. And somewhere,
embedded deep within the settings, there’s even a phone! As you can see, your phone is a monolithic system. We’d
like you to jot down the pros and cons of such a system. Think in terms of architectural characteristics, like availability,
upgradability, cost, and ease of use.


```
Monolithic
Pros Cons




```

Just a few years ago, people used separate devices for all those functions your phone performs today. Phones were,
well, just phones, maybe with text messaging. We used laptop or desktop computers to browse the web and post to
social networking sites; we could buy fitness trackers to help track workouts and GPS devices to install in cars for
navigation help. Each of these “services” was deployed separately.
Just like you did above, jot down the pros and cons of such a system. Again, think in terms of architectural
characteristics.
```
Distributed
Pros Cons




Solution on page 183

you are here 4  173
```


<a id='p210'></a>
<!-- Página 210 -->

monolith advantages



Monolithic deployment models: The pros
In Chapter 2, you learned that architectural characteristics always influence
some structural aspect of the design. Monoliths support some characteristics better
than distributed systems, and knowing where they shine can help you decide
when to use them.
Because monolithic systems run in one process, they make development easier—
at least initially. And since they’re deployed as one unit, tracing errors is a lot
easier.
Let’s take a look at the pros and cons of both deployment models, starting with
monoliths. Here are the pros:

```
simplicity
Typically, monolithic
applications have a single
codebase, which makes them feasibility
easier to develop and to Rushing to market? Monoliths
understand. are simple and relatively cheap,
freeing you to experiment and
deliver systems faster.
cost
Monoliths are cheaper to build
and operate because they tend
to be simpler and require less
infrastructure.
These are just a
things monoliths arfeew of the many
good at.
debuggability
If you spot a bug or get an error
reliability stack trace, debugging is easy,
since all the code is in one place.
A monolith is an island. It makes
few or no network calls, which
usually means more reliable
applications.
Keep an eye out for this point
when we discuss cons on the
next page.
```

Now for the cons...




174  Chapter 5

<a id='p211'></a>
<!-- Página 211 -->

```
architectural styles



```

Monolithic: The cons
Some of monoliths’ strengths can become problematic as an application grows.
Many of the operational characteristics we discussed in Chapter 2, like scalability
and reliability, suffer as a monolithic application grows bigger and more complex.



```
scalability
If you ever need to scale
one part of the application
independently of the others, evolvability
well, you’re in trouble. It’s all or
nothing with monoliths. As monolithic applications grow,
making changes becomes harder.
Furthermore, since the whole
Again, this isn’t the entire application is one codebase, you
list—just a few cons we can’t adapt different technology
reliability thought we’d point out. stacks to different domains if
you need to.
Because monolithic applications
deploy as a single unit, any bug
that degrades the service will
affect the whole monolith.
deployability
There’s reliability again! Implementing any change
will require redeploying the
whole application, which could
```

Next, we'll look at the pros and cons of distributed architectures. introduce a lot of risk.



```
Brain
Power
Spend a few minutes thinking about your industry. Does your organization have any special regulatory,
security, or compliance needs? How might using a monolithic architecture help or hurt its ability to achieve
the architectural characteristics that address those needs? List any ways you can think of here:

Pros Cons




Hint: Think about things like auditability,
reportability, the “right to be forgotten,” etc.


you are here 4  175
```


<a id='p212'></a>
<!-- Página 212 -->

distributed advantages



Distributed deployment models: The pros
With distributed architectures, you deploy your logical components as separate
units. This makes it easy to scale some parts of your application separately
```
from others. And since logical components are physically separate, distributed
```

architectures encourage low coupling.
So, what architectural characteristics are distributed architectures good for?
Here’s a sampling:


```
scalability
Distributed architectures deploy
different logical components
separately from one another. modularity
Need to scale one? Go ahead! Distributed architectures
encourage a high degree of
testability modularity because their logical
components must be loosely
Each deployment only serves coupled.
a select group of logical
components. This makes
testing a lot easier—even as the
application grows.
Distributed architectures
are a lot more testable deployability
than monolithic Distributed architectures
applications. encourage lots of small units.
They evolved after modern
fault tolerance engineering principles like
continuous integration,
Even if one piece of the system
continuous deployments, and
fails, the rest of the system can
automated testing became the
continue functioning.
norm.

Having lots of small units
with good testability
reduces the risk associated
with deploying changes.

```

As you might have noticed, distributed architectures do better on many of
monolithic architectures’ weak points. But is the opposite true? Let’s find out.




176  Chapter 5

<a id='p213'></a>
<!-- Página 213 -->

```
architectural styles



```

Distributed deployment models: The cons
Can’t have pros without cons. Trade-offs, right? It’s all about trade-offs.



```
performance
Distributed architectures
involve lots of small services
that communicate with each
other over the network to do
their work. This can affect
cost
performance, and although there Deploying multiple units means
are ways to improve this, it’s more servers. Not to mention,
certainly something you should these services need to talk to one
keep in mind. another—which entails setting
up and maintaining network
infrastructure.

Debugging distributed system
involves thinking deeply about s
simplicity logging, and usually requires
Distributed systems are the aggregating logs. This also
opposite of simple. Everything adds to the cost.
from understanding how they
work to debugging errors debuggability
becomes challenging. Errors could happen in any
service involved in servicing
We cannot emphasize a request. Since logical
enough how complex components are deployed in
distributed architectures separate units, tracing errors can
can be! get very tricky.


```

Distributed architectures make some things easy, while making others very hard.



```
It’s easy to underestimate how hard distributed computing is!
For all their benefits, distributed architectures depend on the network. Software

```

Watch it!
```
architects often underestimate the complexities that arise from this dependency. Look
up “The Fallacies of Distributed Computing,” a list compiled in the 1990s by L. Peter
Deutsch and others at Sun Microsystems, to get a sense of what to watch out for.




you are here 4  177
```


<a id='p214'></a>
<!-- Página 214 -->

monolithic vs. distributed




```
Brain
Power
Let’s repeat the exercise you did earlier, this time for distributed architecture. Does your organization have
any special regulatory, security, or compliance needs? How might using a distributed architecture help or hurt
your organization’s ability to achieve the architectural characteristics that address those needs? List any ways
you can think of here:

Pros Cons




Fireside Chats
Tonight’s talk: Monolithic and distributed architectures
answer the question: “Who’s more relevant?”


Monolithic Architecture Distributed Architecture


```

It’s a good thing I’m still around. Boy, do you make
things complicated.

```
I don’t like that attitude. Sure, you might be “simpler” to
develop, but you can’t keep up. Businesses need to move
fast, and you just don’t deliver the goods.

```

I might be simple, but I’m also faster to develop. I can’t
imagine anyone building a minimum viable product with
you—they’d never launch!
```
I might give you that—but I’ll make sure they make it to
the finish line. And if their product is a smash hit, will
you help or just get in the way? I can ensure success
even at scale.


```

Oh! And I’m way cheaper. You realize that most
businesses don’t want to waste money, right? I can’t
imagine anyone using you to create a proof of concept.




178  Chapter 5

<a id='p215'></a>
<!-- Página 215 -->

```
architectural styles




Monolithic Architecture Distributed Architecture


Businesses also like making money. Once their
applications grow, you’re just a money pit. I personify
agility—I help teams and organizations scale as they
grow.
I also make testing easier, while you just rack up the
technical debt.

```

It’s a good thing you can be tested easily—ever seen a
useful error stack trace? Of course you haven’t. You’re all
over the place. Good luck trying to trace why and where
an error actually happened.
At least when I get an error, you get a nice, clear stack
trace.
```
Riiiight. And when you fail, you just topple over. I provide
a high degree of fault tolerance. Need a service to scale?
Just scale that service. Scaling you is arduous.
```

At least I’m just one process. No unnecessary network
traffic here. You’re all talk, man—so much chatter. All
your services are constantly talking to one another.
And that’s only if the network is always reliable, because
without it, you have nothing! Heaven help you if the
network should fail.
Plus, with me, you don’t need a whole bunch of network
infrastructure. Do you know how expensive that stuff is
to maintain?!

```
Hey, that’s the cost of doing business at scale. Teams
might start with you, but if they want to keep growing,
they’ll come to me—and leave you in the rearview
mirror.
```

What? Are you saying I’m old news? Well, the next time
a team needs to get to market quickly, don’t call me—and
then we’ll see how tough you really are.
```
Feeling’s mutual, bud. Don’t call me when your
team’s minimum viable product is a success and their
architecture can’t handle all the attention.




you are here 4  179
```


<a id='p216'></a>
<!-- Página 216 -->

chapter summary



And that’s a wrap!
Now you know how to categorize the tons of architectural styles out there.
Having a framework can help you make sense of them. And remember—
each quadrant of the framework represents both the pros and cons of those
architectural styles.
In the next chapter, we’ll start our deep dive into individual styles.




```
Bullet Points
```

 There are a lot of architectural styles—in fact, too  As monolithic applications grow, scaling them up
```
many to count. can become arduous. It’s an all-or-nothing scenario:
you either scale up the whole application or nothing
```

 There are multiple ways to categorize architectural
```
at all.
styles. One is by their partitioning style. Architectural
styles can be either technically partitioned or  Monolithic applications can also be unreliable—a
domain partitioned. bug can make the entire application unusable.
```

 In technically partitioned architectural styles, the  Distributed architectures are highly scalable since
```
code is split up by technical concern. For example, their logical components are deployed separately,
there might be a presentation layer and a services allowing different parts of the application to scale
layer. independently of one another.
```

 In domain-partitioned architectural styles, the code is  Distributed architectures encourage a high degree of
```
instead split up by problem domain. modularity, which means testing them is easier.
```

 Another way to categorize architectural styles is by  Distributed architectures are extremely expensive to
```
their deployment model. Monolithic architectural develop, maintain, and debug.
styles deploy all the logical components that make
 Distributed architectures use the network so
up an application as a single unit. Distributed
that different services can talk to one another
architectural styles deploy the logical components
to complete work. This introduces even more
separately from one another, as multiple units.
complexity.
```

 Monolithic architectures are easier to understand
```
and debug and are often cheaper to build (at least
initially). This makes them great candidates if there is
a rush to bring a product to market.




```

180  Chapter 5

<a id='p217'></a>
<!-- Página 217 -->

```
architectural styles




Stylin’ Architectures Crossword
Now that you can make sense of architectural styles,
see if you can make sense of this crossword.




```

Across Down
2. You can _____ systems technically or by domain 1. Layers are separated by _____
3. L. Peter _____ helped compile “The Fallacies of Distributed 2. Each architectural style has its own _____
Computing” 4. Monolithic architectures tend to have a fast _____ to market
7. Monoliths are good for creating a _____ 5. A system deployed as one big unit
10. Regardless of the physical architecture, a _____ system 6. If you change anything in a monolith, you’ll need to _____
provides more confidence in correct outcomes 8. An architecture’s organization is reflected in its _____ spaces
14. Distributed and monolithic are both deployment _____ 9. Services in a distributed architecture use this to communicate
15. Minimum viable _____ 11. Distributed systems consist of many _____ deployment units
17. Monolithic systems are easier to _____ 12. Nothing about distributed deployment models is _____
18. Monolithic architectures have _____ deployment units 13. Architectures often have more than one _____
```
16. Distributed systems usually _____ more than monolithic
ones do
Solution on page 184

you are here 4  181
```


<a id='p218'></a>
<!-- Página 218 -->

exercise solutions




```
Exercise From page 171
Solution
```

A short-order cook pretty much does everything. They can cook everything on the menu, from fries to sandwiches, as
well as blending smoothies and plating desserts. Often, they also serve food, take payments, and even clean tables
after customers leave. Would you categorize a short-order cook’s work as partitioned technically or by domain? Why?
Jot down your thoughts here.

```
Because a short-order cook does everything needed to get customers their meals, from setting the tables
to prepping and cooking to cleaning up, they own the whole “domain” of food preparation. This makes their
job domain-partitioned.




```

182  Chapter 5

<a id='p219'></a>
<!-- Página 219 -->

```
architectural styles



Exercise From page 173
Solution
```

Take a moment and consider your smartphone. It does it all—it lets you take pictures and videos, browse the web,
post to your favorite social networking site, track your fitness activity, and navigate via GPS. And somewhere,
embedded deep within the settings, there’s even a phone! As you can see, your phone is a monolithic system. We’d
like you to jot down the pros and cons of such a system. Think in terms of architectural characteristics, like availability,
upgradability, cost, and ease of use.
```
Monolithic
Pros Cons


```

Convenience—I only need to carry one device. Availability—If my phone dies or is damaged, I
Upgradability—I don’t have to deal with can’t do any of these functions.
patching and upgrading multiple devices. Cost—Smartphones can be expensive to replace.
Ease of use—If I’m in a rush or going on a trip, Portability—I can only use apps that work on my
I only need to carry one device. phone’s operating system.



Just a few years ago, people used separate devices for all those functions your phone performs today. Phones were,
well, just phones, maybe with text messaging. We used laptop or desktop computers to browse the web and post to
social networking sites; we could buy fitness trackers to help track workouts and GPS devices to install in cars for
navigation help. Each of these “services” was deployed separately.
Just like you did above, jot down the pros and cons of such a system. Again, think in terms of architectural
characteristics.
```
Distributed
Pros Cons

```

Coupling—If my phone’s camera breaks, I can still Upgradability—Everything has to be managed
make calls or track my workout. separately, like upgrading.
Modularity—Each device does one thing and one Complexity—There’s much more to manage (I need
thing only, so it’s easier to test. multiple batteries, chargers, and so on).
Evolvability—I can buy an SLR camera if I want Reliability—Network connectivity can be unreliable;
to take really nice pictures. devices might drop connections or have spotty
```
connections.




you are here 4  183
```


<a id='p220'></a>
<!-- Página 220 -->

crossword solution




```
Stylin’ Architectures Crossword Solution

From page 181




```

184  Chapter 5

<a id='p221'></a>
<!-- Página 221 -->

6 layered architecture
```
Separating
Concerns




What if your problem is simple and time is of the essence? Should you
even bother with architecture? It depends on how long you want to keep what you build. If it’s
disposable, throw caution to the wind. If not, then choose the simplest architecture that still provides
some measurable organization and benefit, without imposing many constraints on speed of delivery.
The layered architecture has become that architecture because it’s easy to understand and implement,
leveraging design patterns developers already know. Let’s peel back the layers of this architecture.




this is a new chapter   185
```


<a id='p222'></a>
<!-- Página 222 -->

sandwich shop requirements



Naan & Pop: Gathering requirements
Sangita likes simple meals, so she created an Indian-inspired mom-and-
```
&
```

pop restaurant called Naan & Pop, specializing in flatbread sandwiches
and sodas.
The restaurant needs a website where customers can place orders online.
Since Naan & Pop is a startup with a small budget, it needs to be simple
and created quickly.
Sangita has some specific requirements.



```
Time to market
The restaurant is already open. The
faster they can get the site online,
the faster they can start making This is Archana,
money. The site should be simple. restaurateur and
aspiring project manager.



Separation of responsibilities
The company has part-time help with specialized
skills, such as user interface (UI) specialists and
database administrators (DBAs). Thus, it would
help to keep each part of the system separate.




Simple, yet extensible
While this is Sangita’s first foray into software
architecture, she would like to keep building on
the company’s online presence and find ways to
extend and reuse parts of the system.




```

Sangita has some software development experience and realizes that many of these
goals require a good separation of responsibilities. She passes these requirements to the
development team she’s hired for this project. You’re a part of that team, so pay close
attention.



186  Chapter 6

<a id='p223'></a>
<!-- Página 223 -->

```
layered architecture



```

Cubicle conversation

```
Alex
Alex: Our project manager just sent the requirements
and goals for Naan & Pop’s web application. It’s so simple.
Couldn’t we just find an existing framework or library to
handle most of it?
Mara: That would solve the simplicity goal. But Sangita
also wants extensibility, and existing frameworks tend to be
a bit rigid.
Sam: What kind of extensibility does she want?
Mara: If the restaurant is a success, we might want the
Mara site to support different kinds of user interfaces, or we
could build integration points for delivery services.
Alex: Yeah—existing simple applications might not handle
the separation of responsibilities Sangita would need for
Sam that kind of extensibility.
Sam: But we don’t have time to build a fancy architecture!
```

Alex: This seems impossible—how can we build a proper architecture with specializations under these time
constraints?
Sam: Fortunately, we’ve already worked with other team members to define the architectural characteristics (for the
application’s capabilities) and domain design (for its behavior). We just need to choose the appropriate architecture.
Mara: Those are some serious trade-offs and conflicting goals. We need a simple architectural style that lets us
separate responsibilities around technical areas, such as user interface, data, business logic, and so on. That way,
adding a new user interface will only affect one layer.
Alex: “Separate responsibilities...” I just read that phrase in the book Head First Design Patterns! I was reading about
the Model-View-Controller design pattern.
Sam: Yeah, but that’s a design pattern—how would you translate that to architecture?
Mara: Lots of design patterns end up in architecture, because often their goals overlap. But, while design patterns
can focus just on design elements, architecture has to account for real-world constraints. Let’s crack open the book
and see if we can map Model-View-Controller into architecture.




```
you are here 4  187
```


<a id='p224'></a>
<!-- Página 224 -->

design patterns



Design patterns redux
To illustrate the concept of design patterns, the influential book Head First
Design Patterns uses the Model-View-Controller (MVC) design pattern,
```
A “design pattern”
```

which separates capabilities based on their purpose.
```
is a contextualized
solution to a
```

In MVC, the model represents business logic and entities in the common problem in
application; the view represents the user interface; and the controller software design.
handles the workflow, stitching model elements together to provide the
application’s functionality, as shown here:
```
You can learn
more about design
The model contains patterns from this
business logic and book.
domain entities.

The controller represents
the workflow of the
application, combining model
elements and facilitating
The view their translation into view
represents the elements.
user interface
of the system.




The user interacts with the
application through the user
interface, using the workflow
defined by the controller to
manipulate the model elements.
Brain
Power
The MVC design pattern separates logical responsibilities, but software architecture must also deal
with physical systems, like browsers and databases. How would you split the responsibilities covered by
MVC within the constraints of software architecture, while maintaining the overall goal of separating
responsibilities and concerns?




```

188  Chapter 6

<a id='p225'></a>
<!-- Página 225 -->

```
layered architecture



```

Layering MVC
Design patterns represent logical solutions to problems, but architecture
must deal with real-world constraints like databases, user interfaces, and
other implementation details. Presentation
```
The V for “view” in MVC
concerns the UI and how the
Typical layered architecture user interacts with the system.
In a layered architecture,
UI elements appear in the
presentation layer.



Presentation
Workflow
The workflow layer contains
Workflow most of the application’s code.
Business logic, workflows,
validations, and other domain
Persistence activities reside in this layer.




Like most layers, this one is Persistence
optional, depending on the Many teams use a special
application’s requirements. persistence layer in their
architecture to map code-based
hierarchies (such as objectoriented languages) into setbased relational databases.


```

This dotted
box represents “Monolith” implies Database
the monolith. that this is a single While it’s optional, the “model”
```
deployment unit. from MVC usually maps to a
database or other persistence
mechanism.
Layered Monolith
The monolithic deployment model, discussed in Chapter 5, is Not all applications use a
often combined with layered architectures. While it’s common database, but they may
for different teams to work on the code and on the database, a persist information elsewhere:
monolithic architecture releases both database and code changes a file system, the cloud, and
together. so on.


you are here 4  189
```


<a id='p226'></a>
<!-- Página 226 -->

interview with a layer




```
Layering it on with an architecture star:
the Layer


```

Head First: Welcome, Layer, to our luxurious studio. I Head First: Do you have a good example of how teams
know you have a busy schedule, so thanks for making the have leveraged you, Layer?
time.
```
Layer: You bet! I worked with a team that handled
```

Layer: You’re welcome. As you say, I’m a pretty big deal. loyalty programs for a hotel. Every purchase a user
They even named an architecture after me! made could qualify for bonus points, depending on their
```
membership status, years of membership, and a bunch
```

Head First: Let’s dig into that, Layer. Why base a whole
```
of other complicated stuff. The team successfully used a
```

architecture on you?
```
bonus layer to keep all the calculations in a single place.
```

Layer: Great question. I make everything nice and
```
Head First: OK, that sounds useful. Can you address
```

understandable in an application’s architecture, since each
```
the recent controversy about your chilly relationship with
```

layer has a specific responsibility.
```
Domain-Driven Design?
```

Head First: So, this architecture is just for neat freaks?
```
Layer: What kind of interview is this? There’s no
```

Layer: No! Putting all the similar functionality in credence to those rumors that we can’t get along. Well, as
separate layers makes it easier to find it again to make you know, I specialize in technical separation. My friend
changes. For example, if the team needs to add a different DDD focuses more on domain or business separation. I’m
database, they only have to change the persistence layer. happy to host a domain in my architecture, but it’ll likely
```
have to split across the layers.
```

Head First: Ah. So organizing everything allows for
easier discovery and updating. Seems like a good reason Head First: Isn’t it true that you’re older than other
for an architecture. architectural styles?
Layer: While unified organization is nice, it’s not the only Layer: The idea of layers in architecture predates just
reason to base an architecture on me. about any other concept. And is that really surprising?
```
When architects start thinking about how to organize
```

Head First: What do you mean?
```
things, I just make sense.
```

Layer: I hate to brag, but us layers are quite flexible—we
```
Head First: We’re nearly out of time, but can you tell us
```

can be used for all sorts of things!
```
about your cozy relationship with the monolith? You seem
```

Head First: Well, I know you often show up for user to be hosted by it a lot.
interfaces and provide a place to put all the business logic.
```
Layer: No comment.
```

Layer: Sure, we do the heavy lifting for those. But teams
can mold us into all kinds of UIs. For instance, a services
layer can provide an interface to other applications that
need to interact with this one.




190  Chapter 6

<a id='p227'></a>
<!-- Página 227 -->

```
layered architecture




But I still don’t
understand how it
works. How does a user
request fit into the
layered structure we’ve
been building?


Great question. Requests and
responses flow through the
layers.
In a layered monolithic architecture, when a user asks the
system to do something, the user interface initiates the
request. Then that request flows through each layer in
the architecture. If the database is involved in persisting
something, then the request goes from top to bottom and
back.




…and eventually gets
a response.
```

The user makes
a request of the Request Response
application...


```
Presentation

Workflow

Persistence



Database



you are here 4  191
```


<a id='p228'></a>
<!-- Página 228 -->

layer fundamentals



Layering it on
For an application like the Naan & Pop site, your team will build logical components
to match the problem. But how will you implement those components?
Layers, in this type of architecture, are created with packages or namespaces, just
like domain components. However, to maintain the separation of concerns, the
layers’ package structures typically reflect their place within the partitioning:



com.naanpop.orderapp.presentation
com.naanpop.orderapp.workflow
```
The fully qualified names of
```

com.naanpop.orderapp.model these layers will appear as
com.naanpop.orderapp.persistence
```
packages in Java, namespaces in
.NET, or whatever namespacing
mechanism your language of
choice uses.

```

Like the logical components, the architectural layers use the component
implementation of the underlying platform, which often maps to the
underlying filesystem:


```
“naanpop” is the
naanpop system scope.
“orderapp” is the
orderapp application scope.
```

Just like for our domain presentation
components, the directory lots_of_source_code_files
structure corresponds to the
layers. workflow
```
The layers of
lots_of_source_code_files the architecture
are represented
model
as packages or
lots_of_source_code_files namespaces.
persistence
lots_of_source_code_files




```

192  Chapter 6

<a id='p229'></a>
<!-- Página 229 -->

```
layered architecture



```

Translating layers into code
Once your team has built the component packages (or namespaces), you’ll
need to assist the developers in implementing the architecture. Here’s an
example in Python-like pseudocode to illustrate how the layers translate to
code.

```
The user interface layer, or presentation layer, is
the topmost layer. It’s responsible for interacting with the
user, serving the same purpose as the view part of MVC.


def UI_layer(request): Get the request
from the user. there are no
data = request.get_data() Dumb Questions
return business_logic_layer(data)
Pass the request to
the workflow layer. Q: You said in Chapter 5 that every
architectural style has a category and
The workflow layer (sometimes called the business a philosophy. Where does the layered
architecture fit in?
rules layer) is responsible for processing each request
from the UI layer and returning a response.
Process the data A: We’re glad you’re thinking about that.
As we said in Chapter 5, understanding
def business_logic_layer(data): from the UI layer. the categories reveals a lot about what
characteristics a particular architectural style
processed_data = process_data(data)
will support.
return data_access_layer(processed_data)
The layered architecture is a technically
Pass the processed data to partitioned architectural style, typically
the data access layer. deployed as a monolith. (We say typically
because we’ll discuss some variations on this
model soon.)
The persistence layer (or data access layer) is
responsible for accessing the data from the database and
returning it to the workflow layer.
Access the data in
def data_access_layer(data):
the database.
retrieved_data = retrieve_data(data)
return retrieved_data


Return the retrieved data to
the workflow layer.


you are here 4  193
```


<a id='p230'></a>
<!-- Página 230 -->

domains in layered architecture




```
Wait. We went through
a logical component analysis to
determine the application’s behavior.
Where do those components reside
within the layers of this architecture?




This is an important point—the
domain behavior lives across the
layers in this architecture.
The domain, as you’ll recall, represents logical components
based on the problem you’re trying to solve. However, the
layers in this architecture represent technical capabilities—
user interface, business logic, and so on.
The domain maps onto the layered architecture, sometimes
spreading between layers.




there are no
Dumb Questions
```

Q: Why these particular layers—presentation, workflow, Q: Was the layered architecture inspired by the Modeland persistence? View-Controller design pattern?

A: These are common layers, but they are by no means
required. Most applications have at least some of this separation:
```
A: The opposite is likely true. Layered architectures, which
have existed as long as people have been building software
```

for instance, the UI is often distinct from the core logic of the from different parts, may well have inspired the design pattern.
system, which in turn is separate from the database development. Design patterns are often harvested from observations of common
```
occurrences, and the layered architecture has been around for
quite some time in many forms.




```

194  Chapter 6

<a id='p231'></a>
<!-- Página 231 -->

```
layered architecture



```

Domains, components, and layers
In a simple restaurant ordering system like Naan & Pop’s, we might come
up with the following components based on the problem domain:



```
Place Order Deliver Order Manage Manage
Recipes Inventory

```

“Place order” includes
concepts like payment.
But there’s a problem. These components are based on the logical behavior
of the domain, but the layered architecture splits things by capabilities. So,
we need to separate the logical components (which include workflows
and entities) into components that match what we need for the layered
architecture:


```
Sandwich Recipe Customer Delivery
Order Location

```

Once we’ve split the logical components into workflow and entities, we can
overlay the components over the layers in this architecture: This is an important point,
```
Domains are typically so take a moment and let
The concept of an “order” smeared across it soak in. We’ll come back
cuts across physical layers. physical layers in to this at the end of the
layered architectures. chapter.
Sandwich Recipe Inventory
Order Domain Domain
Domain


Place Order Recipes UI Inventory UI Presentation



Place Order Manage Manage
Deliver Order Recipes Inventory
Workflow



Order Customer Delivery Recipe Ingredients Persistence
Location


you are here 4  195
```


<a id='p232'></a>
<!-- Página 232 -->

components and layers



```
Sharpen your pencil
Naan & Pop’s lead architects have designed a layered architecture. Today, though, they’re off
at a daylong breadmaking seminar to learn more about their problem domain, leaving you to
```

sort out which components go where. Can you decide in which layer (or layers) each component should reside?
Draw the components below on the layer(s) to which they should map.

```
Hint: Some components may end
up in several layers.
Components

Delivery Billing Sales
Address Address Promotion



Frequent
Blacklisted
Diner
Customers
Rewards




Presentation

Employee Workflow
Employee
Information
info
Persistence



The typical implementation of We did one for you. Employee
this architecture assumes that information, like drivers’ details,
anything in the persistence may be needed by workflows and
layer ends up in the database. persisted, yet not be part of
the presentation layer.



Solution on page 210

```

196  Chapter 6

<a id='p233'></a>
<!-- Página 233 -->

```
layered architecture




It seems like every
architecture provides some
benefits but also imposes some
restrictions. If only I could have an
architecture that maps perfectly
to my problem domain, without
any pesky trade-offs! But that’s
only a dream...




there are no
Dumb Questions
```

Q: Why go to the trouble of identifying logical components Q: Why is the layered architecture so popular?
if we have to break them apart to fit them into this
architecture? A: This architecture shows up a lot. First, it’s simple, without

A: The logical components represent the problem you’re trying
to solve. Mapping that to any architecture means applying real-
```
many moving parts. Second, as you’ve seen, it maps closely to the
MVC design pattern, making it easy to understand. Third, it’s so
common that teams can build simple projects quickly in this style.
```

world constraints (and trade-offs). We’ll show you a more direct Fourth, many companies separate their employees by skill set,
domain-to-architecture mapping in the next chapter, but it has which facilitates an architecture with similar partitions.
trade-offs, too.




```
you are here 4  197
```


<a id='p234'></a>
<!-- Página 234 -->

layered architecture drivers



Drivers for layered architecture
We’ve put together a list of the things the layered architecture is really good at—that is,
the things that might drive us toward picking this particular architectural style.




```
Specialization
Using a layered architecture
allows organizations to
split teams into specialists,
sharing their capabilities
between different projects. Ease of (technical) reuse
Splitting the architecture by
The ability to specialize technical capabilities allows better
makes this architecture opportunities to reuse code. For
popular in organizations example, if all persistence code
that need to share special resides in a single layer, it’s easier
skills across multiple for developers to find, update, and
projects. reuse it.
The ability to reuse
components within a layer is
one of the key advantages
Matches physical separation of this architecture for
The layered architecture typically many organizations.
separates the logical components
to match the physical separation.
For example, it’s common for
teams to implement different
layers in different technology
stacks (such as JavaScript, Java,
and MySQL).
Conceptual twin of MVC
Often, the real world prevents Simplicity and concerns about
architects from designing what feasibility are driving forces in
they want, instead forcing many architectures. Developers
them to design with what they find it easier to understand and
have. work within an architecture that
matches familiar design patterns,
such as MVC.


Feasibility and simplicity
for the win!

```

198  Chapter 6

<a id='p235'></a>
<!-- Página 235 -->

```
layered architecture



```

Layers, meet the real world: Physical architectures
The layered monolith describes a logical architecture, but architects may
implement that logical architecture in a variety of physical architectures.


```
Example: corporate Two-Tier
accounting software Presentation A two-tier architecture places the
that runs as a rich presentation, business rules, and persistence
desktop application Business rules layers into a single deployment unit,
using a shared communicating with the database via a
local network. This physical architecture
database Persistence
is common in desktop and client/server
applications.




Example: a high-scale Presentation
web application with
a rich web-based UI,
like a streaming video
service
Three-Tier Business rules
A three-tier architecture places each of the
responsibilities into its own physical layer. A good
example of this architecture would be a web-based Persistence
application, with an application server to handle the
middle tier and a presentation layer often written
using a different technology stack. For example, the
development team might write the business rules and
persistence in Java while the UI consists of HTML
and JavaScript, all using a relational database for
persistence.



Presentation Embedded/Mobile
Often, because of physical constraints, all the logical layers end up in a
single physical deployment. This physical architecture commonly appears
Business rules in embedded systems and mobile applications, where a network connection
may not be consistent or even possible.
Persistence
Examples: a mobile
Database game or soda-machine
software

you are here 4  199
```


<a id='p236'></a>
<!-- Página 236 -->

physical architecture



Physical architecture trade-offs
Which physical architecture should you choose? Well, they all have tradeoffs, like everything in software architecture.


```
Two-Tier
Pros Cons
```

+ Rich user interface Presentation - Medium scalability Reliability is only
```
medium, because this
```

+ High performance - Becomes complex
```
Business rules architecture relies on
when it gets big the network for data
```

+ Simple
```
Persistence
- Medium reliability access.
```

These architectures
are simple because
everything can typically
be implemented as a
single project.
```
Three-Tier
Pros Cons
Presentation
+ Detached UI - Least reliability
(typically web) More complex
- More complex because it has the
+ Highest scalability
- Distributed most moving parts
+ Distributed Business rules architecture
architecture headaches
benefits Persistence
Distributed architectures
Distributed architectures are more complex, with
offer higher scalability more moving parts and
and similar benefits. failure modes. While a single stack
is nice, it isn’t
always portable to
other platforms.
Embedded/Mobile
Pros Cons
+ Self-contained - Least scalable
A single tech Presentation
stack can be an + Single tech stack - Resourceadvantage for + Highly tunable to
Business rules constrained
simplicity. hardware devices Persistence - Often tied to
implementation
Database
platform


```

200  Chapter 6

<a id='p237'></a>
<!-- Página 237 -->

```
layered architecture


Exercise
```

Generic trade-offs are one thing, but software architecture is always based on a real system. The architects at Naan
& Pop need some help evaluating the trade-offs for each physical architecture as they decide which one to use. Can
you help them figure out which specific trade-offs the Naan & Pop application will face for each physical architecture?

```
Two-Tier
Pros We’ll help you get Cons
started.
Simplicity Scalability




Three-Tier

Pros Cons




Embedded/Mobile
Pros Cons




Solution on page 211




you are here 4  201
```


<a id='p238'></a>
<!-- Página 238 -->

additional layers



Cubicle conversation
Alex: Is Naan & Pop generic enough to only use the standard layers? When
do teams add layers?
Sam: Why add layers to the architecture?
Mara: Each layer in a layered architecture has a specific responsibility
within the system, so when they’re needed, we add layers.
Sam: What kinds of layers?
Alex: It’s common to add a services layer, which provides access for
business-to-business integration, or integration layers for other internal
systems. Each request goes through each layer, so layers need to be things Mara Sam Alex
that happen to every request.
```
No need to be stingy with
layers—you can have as many as
Presentation you need, as long as each layer
Business rules applies to each request.
Service
Mara: That’s right—architects can add whatever layers we need to support some
Persistence
new behavior. For example, the site needs integration with third-party delivery
services, so maybe we should add an integration layer. Here, let me draw what I
have in mind for our layered architecture on the whiteboard...

Presentation The integration layers allow
interaction with third-party
Business rules
delivery services.
Integration
Alex: Adding an integration layer for our delivery hooks would make things easier,
Persistence
wouldn’t it? It looks like all the code pertaining to that integration lives in the same
place, which would make it easy to find and update.
Mara: Yes, and that’s true for the user interface layer, too. In fact, one of the next
requirements we have to implement is an additional UI to support mobile.
Sam: So, if we add a separate mobile UI, we’d only have to change one layer?
Mara: That’s one of the best things about layered architecture!


Browser Android iOS
Presentation
Business rules
None of the other layers (or The presentation layer can
Integration the database) needs to change change to accommodate new UI
Persistence when the team adds a new UI. types.


```

202  Chapter 6

<a id='p239'></a>
<!-- Página 239 -->

```
layered architecture



```

One final caveat about domain changes
One of the primary advantages of a layered architecture is that it lets us group
similar technical things together. For example, in the Naan & Pop application,
separating the UI into its own set of components allows the team to add new UI
types without affecting the other layers.
Let’s pause for a second and think about this—what about changes to the problem
domain? If Naan & Pop wanted to add something other than sandwiches to the
menu, like pizza, would every layer have to change?
The power to change things in isolation is the layered architecture’s superpower,
but it’s not a silver bullet. This architectural style’s big trade-off is that the
problem domain is smeared across the layers in the architecture. For
example, the Place Order logical component in the Naan & Pop architecture
requires a UI (presentation), code to implement the workflow (workflow), and a
data schema (persistence).
That means that technical capabilities are easy to change and enhance, but domain
changes can create side effects that ripple through the layers. We alluded to this
```
earlier in the chapter.


Layered architectures facilitate technical changes
but make domain changes more difficult.
Take a deep breath. The next
```

So, what to do? Well, there’s a reason why we started this book by showing you chapter will introduce you to
how to identify the architectural characteristics your application needs to support. an architectural style that is
If continual, significant domain changes are expected or suddenly become a better suited to accommodating
higher priority, there are other architectural styles to consider. domain changes. Oh, the
All that said, let’s quickly summarize the good and bad of the layered architecture. suspense!



```
there are no
Dumb Questions
```

Q: That’s a rather large caveat. Why would I even consider the layered architectural style?

A: Remember the First Law of Software Architecture—everything’s a trade-off. Sure, other architectural styles might allow for easier
changes to the domain, but they have their own caveats. Align the strengths and weaknesses of every architectural style with your
requirements, and then choose. There’s no one right choice, just the choice that works best for your particular set of circumstances.




```
you are here 4  203
```


<a id='p240'></a>
<!-- Página 240 -->

layered superpowers




Layered architecture superpowers
Layered architectures have been demonstrating their powers for many, many
years—this is one of the oldest recognizable architectural styles.




```
If your whole company runs on
investment dollars, feasibility is
especially important.
```

Feasibility
```
gly
```

If time and budget are overwhelmin
important, the simp licit y of this
architecture is quite appealing.


```
Performance
Well-designed layered monoliths can
demonstrate high performance—makin
g
no network calls and processing data
in
a single place (the monolithic database
)
```

Technical partitioning means there’s no need for network calls
Architects design components around that could decrease performance.
technical capabilities, making it easier for
them to reuse common capabilities. For
example, if several teams need the same
data functionality, they could implement
it once in a persistence layer and then Quick to build
share it across teams. Simplicity plus a single work/deployme
```
nt
In general, the less a unit means that teams can build sma
ll
system needs to access
tensiveta-level
systems quite rapidly.
```

Data-indo a lot of da
```
data over the network,
```

Systems that
```
nefit from a laye
red the more efficient it
```

processing may be s data can be.
```
use it isolate
```

architecture beca ’s
```
gle database that
```

processing in a sin
```
e task. Lean and m
```

optimized for th Keeping these syste ean
```
ms small helps avoi
some of the krypto d
nite on the next pa
ge.




```

204  Chapter 6

<a id='p241'></a>
<!-- Página 241 -->

```
layered architecture




Layered architecture kryptonite
This architecture is pervasive and popular, but it can be overused and even
abused. While feasibility may be a superpower, many teams default to this
architecture because of its simplicity, long history, and widespread use, without
considering if it’s really the most suitable option.

Scalability
Probably the biggest problem with
monoliths is that when you only have
one
bucket and you keep adding things to
it,
it will eventually fill up. The same is
true
for monoliths generally, which eventual
ly
become constrained by some resource
(memory bandwidth, and so on).


Elasticity
A single process has a harder time dealing
with sudden bursts of users.


```

Deployability
As monolithic systems get bigger,
deployments tend to become more
```
rs
```

complex—especially when develope
keep adding behavior.
```
Testability
High coupling and a large codebase
make testing harder and harder over
time.

d
```

Big ball of munect ed to
Because everything is con
everything else, this architecture can
become a highly coupled mess without
careful governance.




```
you are here 4  205
```


<a id='p242'></a>
<!-- Página 242 -->

strengths and weaknesses



Layered architecture star ratings
The Naan & Pop architecture team decides to use a rating chart they found in the
book Fundamentals of Software Architecture (O’Reilly), written by two of your authors,
that describes the layered architecture in a convenient way. One star means that the
architectural characteristic is not well supported; five stars means the architectural
characteristic is very well supported.
```
Just like movie reviews.

Testing isn’t especially
easy, but the team
has been dealing with
layered architectures
so long that they’ve
Architectural Characteristic Star Rating built up many
techniques.
Maintainability Studio




Testability Studio
Studio




```

Layered
architectures are Deployability
nice and simple.
```
Studio




Well-designed layered
Simplicity Studio Studio Studio Studio Studio




architectures can
```

Monoliths in general boast quite high
don’t handle Evolvability performance.
scalability and
```
Studio




```

elasticity well, and
layered ones even Performance Studio
```
Studio
Studio




```

less so.
```
Scalability Studio




Simplicity, in this
Elasticity Studio




case, leads to
affordability.
Fault Tolerance Studio




Overall Cost $




```

206  Chapter 6

<a id='p243'></a>
<!-- Página 243 -->

```
layered architecture




Exercise
```

Which of the following systems might be well suited for the layered monolithic architectural style, and why? Hint: Take
into account its superpowers, its kryptonite, and the nature of the system.


```
An online auction system where users can bid on items Well suited for layered monolith
Why? Might be a fit for layered monolith
Not well suited for layered monolith




A large backend financial system for processing and Well suited for layered monolith
settling international wire transfers overnight Might be a fit for layered monolith
Why?
Not well suited for layered monolith




A company entering a new line of business that Well suited for layered monolith
expects constant changes to its system Might be a fit for layered monolith
Why? Not well suited for layered monolith




A small bakery that wants to start taking online orders Well suited for layered monolith
Why? Might be a fit for layered monolith
Not well suited for layered monolith




A trouble ticket system for electronics purchased Well suited for layered monolith
with a support plan, in which field technicians Might be a fit for layered monolith
come to customers to fix problems
Not well suited for layered monolith
Why?




Solution on page 212

you are here 4  207
```


<a id='p244'></a>
<!-- Página 244 -->

chapter summary



Wrapping it up
Congratulations! The Naan & Pop team looked at several architectural styles,
but after considering the business’s priorities, you chose a layered architecture.
This paid off handsomely, allowing the business to grow without any problems.




Bullet Points
 A layered architecture is monolithic: the entire system  Each request in this architecture goes through each
```
(code and database) is deployed as a single unit. layer.
```

 The layers are separated by technical capabilities.  A layered architecture’s capabilities degrade over time
```
Typical layers in this architecture include presentation if teams continue to add functionality due to eventual
(for the user interface), business rules (for the workflow resource limits (for example, they run out of capacity).
and logic of the application), and persistence (facilities
 The layered architecture provides excellent support
to support databases for systems that need persistent
for specialization (user interface designers, coders,
data).
database experts, and so on).
```

 The layered architecture supports feasibility well; it is
```
 Logical components represent the problem domain,
easy to understand and it lets you build simple systems
yet layers focus on technical capabilities, requiring
fast.
translation between the domain and architecture layers.
```

 The layered architecture supports excellent separation
```
 A layered architecture may manifest in several physical
of technical concerns, making it easy to add new
architectures, including two-tier (also known as client/
capabilities like user interfaces or databases.
server), three-tier (web), and embedded/mobile.
```

 The layered architecture mimics some of the same
```
 Changing and adding to the technical capabilities
concerns as the Model-View-Controller design pattern,
represented in layers is easy; the layered architecture
but translated into physical layers and subject to realfacilitates this.
world constraints.
 Changing the problem domain requires coordination
```

 User requests flow through the user interface and
```
across the layers of the architecture, making domain
through each layer before a response is returned to the
changes more difficult.
user.




```

208  Chapter 6

<a id='p245'></a>
<!-- Página 245 -->

```
layered architecture




Layered Architecture Crossword
Ready to add learning on top of learning by solving the
layers of this crossword?




```

Across Down
3. Layered architectures use familiar design _____ 1. The integration layer lets the system _____ with third parties
5. Kind of layered architecture often found in smartphone apps 2. Layered architectures facilitate _____
6. Type of architecture covered in this chapter 4. The _____ domain spreads across all of the layers
8. _____ can be confined to one layer 7. Logical and _____ components are usually separated in the
9. Namespaces and packages correspond to the directory _____ same way
11. Too much coupling can lead to a big ball of _____ 10. Logical _____ reside in layers
14. Layer that maps object models to relational models for 12. Domain-driven _____
databases 13. Layer that applies business rules
17. Depending on the network for data access makes an 15. The user _____ is part of the presentation layer
architecture _____ reliable 16. The MVC pattern and layered architecture both _____
19. Kind of database often used for persistence responsibilities
21. Layered architectures might have two or more _____ 18. A user’s request and its response _____ through the layers
```
20. Model-_____-Controller design pattern
Solution on page 213

you are here 4  209
```


<a id='p246'></a>
<!-- Página 246 -->

exercise solutions




```
From page 196
Sharpen your pencil
Solution
```

Naan & Pop’s lead architects have designed a layered architecture. Today, though, they’re off at a daylong
breadmaking seminar to learn more about their problem domain, leaving you to sort out which components go
where. Can you decide in which layer (or layers) each component should reside? Draw the components below on
the layer(s) to which they should map.
```
Hint: Some components may end
up in several layers.
Components
Delivery Billing Sales
Address Address Promotion



Frequent
Blacklisted
Diner
Customers
Rewards




Frequent
Billing Sales
Presentation
Delivery Diner
Rewards Address Promotion
Address

Blacklisted Employee Employee
Workflow
Customers information
info
Persistence


Example: Employee
information like drivers’ The typical implementation of
details may be needed by this architecture assumes that
workflows and persisted but anything in the persistence
not part of presentation. layer ends up in the database.




```

210  Chapter 6

<a id='p247'></a>
<!-- Página 247 -->

```
layered architecture



Exercise From page 201
Solution
```

Generic trade-offs are one thing, but software architecture is always based on a real system. The architects at Naan
& Pop need some help evaluating the trade-offs for each physical architecture as they decide which one to use. Can
you help them figure out which specific trade-offs the Naan & Pop application will face for each physical architecture?

```
Two-Tier Fewer tiers tends
Pros Simplicity facilitates Cons to result in poorer
short time to market. scalability.
Simplicity Scalability
While performance
Performance isn’t a driving concern,
fewer tiers tends
to lead to better
performance.
```

Separation supports
one of the driving Three-Tier
goals.
```
Pros More tiers creates
more parts to Cons
Architectural separation the architecture, Complexity
complicating …which leads to...
Scalability dependencies and Slower time to market
communication...
```

Better scalability
supports more users. It’s hard to extend
```
Embedded/mobile an embedded system,
Pros Cons counter to one of
A pure monolith has the stated goals.
Self-contained the fewest parts. Less extensible
Scalability
It’s hard to make Performance
a self-contained
monolith with high
scalability and/or
performance.




you are here 4  211
```


<a id='p248'></a>
<!-- Página 248 -->

exercise solutions



```
Exercise From page 207
Solution
Which of the following systems might be well suited for the layered monolithic architectural style, and why?
Hint: Take into account its superpowers, its kryptonite, and the nature of the system.



An online auction system where users can bid on items Well suited for layered monolith
Why? An online auction will require more Might be a fit for layered monolith
scalability and performance than most Not well suited for layered monolith
layered architectures can support.

A large backend financial system for processing and Well suited for layered monolith
settling international wire transfers overnight
Might be a fit for layered monolith
Why? This system requires high throughput
Not well suited for layered monolith
and high availability, both difficult for
layered monoliths.

A company entering a new line of business that Well suited for layered monolith
expects constant changes to its system Might be a fit for layered monolith
Why? Layered architectures separate concerns
Not well suited for layered monolith
by technical capabilities, making some
changes easier.

A small bakery that wants to start taking online orders Well suited for layered monolith
Why? A small bakery has a simple problem Might be a fit for layered monolith
and small scale, well suited for a simple Not well suited for layered monolith
architecture.

A trouble ticket system for electronics purchased Well suited for layered monolith
with a support plan, in which field technicians
Might be a fit for layered monolith
come to customers to fix problems
Not well suited for layered monolith
Why? A trouble ticket system will need to support
different architectural characteristics (for
users and technicians, for example), which is
difficult in monolithic architectures.


```

212  Chapter 6

<a id='p249'></a>
<!-- Página 249 -->

```
layered architecture




```

Layered Architecture Crossword Solution
```
From page 209




you are here 4  213
```


<a id='p250'></a>
<!-- Página 250 -->


<a id='p251'></a>
<!-- Página 251 -->

7 modular monoliths
```
Driven by the
Domain




There’s more than one way to build a monolith. So far, you’ve encountered
the layered architecture, which aligns things technically. You can go a long way with a layered
monolith, but when changes begin to involve lots of communication and coordination between different
teams, you might need a little more horsepower under the hood—and perhaps even a different
architectural style.

This chapter looks at the modular monolith architectural style, which divides applications up by
business concerns as opposed to technical concerns. You’ll learn what this means, what to look out for,
and all the trade-offs associated with this style. Let’s take the modular monolith for a spin, shall we?




this is a new chapter   215
```


<a id='p252'></a>
<!-- Página 252 -->

pizza menu requirements




```
By popular demand, we’re
introducing pizzas to our
menu! Before I announce
it, I think I should talk to
our software development
group...




Remember Archana, founder of
Naan & Pop and aspiring project
manager from Chapter 6?




As a reminder, Naan & Pop’s sandwich shop has a small development team,
and its requirements haven’t changed a whole lot since the team built their
layered application in Chapter 6. The competition is stiff, and time to
market remains a concern. The system should remain simple.

Be sure to review
```


## Chapter 6 if you need

```
to refresh your memory.

```

216  Chapter 7

<a id='p253'></a>
<!-- Página 253 -->

```
modular monoliths




Exercise
```

Cast your mind back to the layered architecture we built for Naan & Pop in Chapter 6. The following diagram shows its
layers and logical components. Adding a new category to the menu (say, pizza) means changing a bunch of moving
parts. Grab a marker and put a triangle ( ) next to everything this new requirement will affect.

```
Order Recipe Inventory
Domain Domain Domain


Place Order Recipes UI Inventory UI Presentation



Place Order Manage Manage
Deliver Order Recipes Inventory
Business rules


Delivery Recipe
```

Order Customer Recipe Item Persistence
```
Location


Use this
down yourspace to jot
thoughts.




Solution on page 240




you are here 4  217
```


<a id='p254'></a>
<!-- Página 254 -->

modular monolith vs. layered architecture



Cubicle conversation

```
Sam Alex Mara




Alex: Pfft! This is easy. We’ve already delivered a working and extensible system. Let’s get to it.
Mara: Hold your horses. This might be our first rodeo with such a change, but I doubt it’ll be our last.
Sam: So what? We’ve built an extensible system. Why are you being so reticent?
Mara: Let’s think this through—we have to add pizzas to the menu. Not only will we have to add new
recipes and ingredients, but we’ll also need to allow patrons to order pizzas online. So where will we have
to make changes?
Sam: Lots of places! It’ll at least affect ordering and recipe management. I still don’t see a concern.
Alex: I think I do. We’ve built a layered architecture, and we have specialists working on each layer. A
change like this means coordinating changes across all of those folks.
Mara: Bingo! The layered architecture smears the domain across all the layers. So, implementing
anything that changes the domain can be arduous.
Alex: You’re telling me that choosing the layered architecture was a mistake?
Mara: The layered architecture was simple and quick to build. It allowed us to launch quickly. But now
we need to think about maturing the architecture to support modularity, so changes like these will be
easier in the future.
Alex: So where do we start?
Mara: Allow me to introduce you to the modular monolith. Rather than partitioning by technical
concern, we’ll partition by business domain, using modules—hence the word modular. I’ll show you
what this looks like as I explain it.
Sam: Ooh, I’m so excited. Let’s do it!




```

218  Chapter 7

<a id='p255'></a>
<!-- Página 255 -->

```
modular monoliths



```

Modular monolith?
A modular monolithic architecture, like a layered architecture, is deployed as a
single unit, usually with its own database. Think back to Chapter 5.
```
Architectural styles can
Layered architecture be separated by how the
is a monolithic code is partitioned and by
deployment model...
Presentation deployment model.
Workflow
Persistence
...backed by a
monolithic database.

Heads up—you’ll find the
```

That’s where the similarity ends. In a modular monolith, rather than partitioning terms domain and subdomain
your application by technical concerns, you partition it by functionality. Every used interchangeably. As
business operates within a certain domain—like banking, education, or retail. long as you understand that
Online stores usually have several subdomains, like Order Placement, Payment, and both terms represent business
Inventory Management. Together, they make up the Online Store domain. You concerns, you’re good.
organize your application according to these subdomains, separating them into
modules.


```
Modular monolith Rather than organizing
is also a monolithic the application by
deployment model. Order Inventory
technical concerns,
Placement Management
we organize them by
business domain.
Payment



Modular monoliths
also use a monolithic
database.

```

What is a module? At a high level, it’s just how you organize your code. In some languages,
you might have support like packages or namespaces. But it doesn’t start or stop there.
Partitioning your code using modules has implications for how you’ll go about separating
concerns between modules and how modules will interact with each other. We have a lot
more to say about this, so stay tuned. For now, we just want you to be able to distinguish
between the layered and modular monolith architectural styles.

```
you are here 4  219
```


<a id='p256'></a>
<!-- Página 256 -->

modules and components


```
there are no
Dumb Questions
```

Q: Can you explain more about what you mean when you say module?

A: A module is a software design element representing an independent unit that fulfills one piece of functionality. Technically, every
layer in a layered architecture is a module—these modules just happen to be divided by technical concern.
In a modular monolith, on the other hand, each module represents a particular piece of the domain—that is, a subdomain. Each module
contains all the business functionality needed for that particular subdomain.




```
Who Does What
Identifying which components should belong to a particular module can be tricky.
In this game of “Who Does What?”—or rather, “What Goes Where?”—we’d
like you to match each component to the module where it fits best. Multiple
components can belong to one module.




Shopping Cart Order

Credit Card Form


Primary Email Payment
Preference

Fulfillment
Workflow
Customer

Order History




Solution on page 241

```

220  Chapter 7

<a id='p257'></a>
<!-- Página 257 -->

```
modular monoliths



```

Domain pains changes
Naan & Pop wants to add a new food category (pizza) to the menu. Which parts
of the architecture need to change to make this happen? Let’s take a look.
```
Components
That Change
Order Recipe Inventory
Domain Domain Domain


Place Order Recipes UI Inventory UI Presentation


Manage Manage
Place Order Deliver Order Business rules
Recipes Inventory

Delivery Recipe
Order Customer Recipe Persistence
Location Item


```

Introducing a new menu category primarily affects the Order domain. The menu
needs to allow customers to order pizzas and customize their toppings. That might
require changing or adding new business rules to support customization and perhaps
delivery, since pizzas need to be delivered hot. It could also change how the system
stores orders (since customers may ask for customizations.)
As you can see, introducing new menu items can affect multiple components across
multiple layers. This is because, as mentioned in the previous chapter, in a technically
partitioned architecture the business domain gets “smeared” across multiple layers.
This is great if you’re implementing a technical change, like changing the view No one ever woke
technology or swapping out the database. But it’s not so great if the change affects and said, “How canup
the domain—you’ll have to round up folks from multiple teams to figure out how to I add yet another
implement it. meeting to my
This is where modular monoliths can really help. calendar?”


```
Geek Note
It’s not unusual for teams to start with a layered architecture, then refactor it into a modular monolith over time as the
application grows.




you are here 4  221
```


<a id='p258'></a>
<!-- Página 258 -->

modular monolith basics



Why modular monoliths?
```
Every layer in a burger
```

When you eat a burger (or a veggie burger!), do you take a bite of the top bun first, serves a specific purpose—
then bite into the gooey cheese, then take a bite of the patty? Or do you take one so it tastes best if you
bite that slices vertically through every layer of the burger? The latter, right? bite through all the layers
That’s exactly how you can think of a modular monolith. You don’t organize the together.
application in horizontal layers separated by technical concern, but in vertical slices
scoped by business concern. Each vertical slice aligns with a piece of the domain and Yum!
is encapsulated in a module. Every module contains a set of business functions—for
example, order placement, order completion, and order delivery would all be part of
the Order Placement module.
```
Individual domains
make up the modules
of your application.

Order Recipe Inventory
domain domain domain




Receipe management Inventory management
Order placement
Presentation Presentation Presentation

Business rules Business rules Business rules

Persistence Persistence Persistence




These “slices” represent a particular set
of business functions within a domain.



```

What does this mean? Changes to the domain that affect many or all layers
require lots of coordination between different teams. You’ll need to ensure that
everybody’s changes work with everybody else’s. This isn’t business-word
Now, rather than having teams that specialize in the presentation layer or the bingo! It’s not always easy
persistence layer, you have cross-functional teams, each specializing in a to build out cross-functional
domain. The result? It’s far easier to coordinate domain changes when one team teams that work in multiple
takes full ownership. different technical stacks.



222  Chapter 7

<a id='p259'></a>
<!-- Página 259 -->

```
modular monoliths




Hold up. I still see
```

layers in each module.
Is this some kind of Jedi
mind trick? How is this any
different from a layered
```
architecture?




```

How astute of you! You’re absolutely right that each
module here still consists of layers—but they don’t have to. The
important thing is that your application is organized by domain.
Your system still needs to process and respond to each request,
though. So you’ll need an entry point (presentation layer), some
business processing (workflow layer), and maybe a data store to
write to (persistence layer). Even within a modular architecture, it
makes sense to separate those responsibilities, much like the layered
architecture does.
However, if you zoom out and look at the whole architecture, you’ll
see that the application is carved up into subdomains. The fact that
each module is composed of a bunch of technically partioned layers
becomes an implementation detail, as opposed to an architectural
concern. In other words, how a module is laid out internally
isn’t how the architecture is partitioned. Modular monoliths are
domain-partitioned.
Let’s get a bit more concrete by seeing what this looks like in code.




```
you are here 4  223
```


<a id='p260'></a>
<!-- Página 260 -->

modular monolith code



Show me the code!
You’ve probably recognized that modular monoliths solve the problem you are
working on differently from a layered architecture, by organizing applications
by domain rather than technical concern. But how does this translate to your
code?
Let’s first talk about the modules themselves. They represent parts of the
domain. Naan & Pop’s namespaces look like this:
```
Flip back to page 192 in the
previous chapter and compare
com.naanpop.orderapp.order these to the namespaces for
com.naanpop.orderapp.recipe the layered architecture.
com.naanpop.orderapp.inventory

```

Remember, we’re still working with a monolith—that is, it’s still one
deployment. Typically, one deployment would translate to one codebase, with
the code organized in different namespaces. Each namespace represents a
separate module, like so:
```
Ah, I see! The layers are an
implementation detail, not
naanpop an architectural concern.

orderapp
There’s one module.
order

presentation
lots_of_source_code_files

workflow
lots_of_source_code_files
persistence
lots_of_source_code_files
recipe There’s another module.
presentation
lots_of_source_code_files
...
We aren’t showing the
entire structure here, but
we know you get it.



```

224  Chapter 7

<a id='p261'></a>
<!-- Página 261 -->

```
modular monoliths




Exercise
```

A critical piece of successfully developing modular monoliths is understanding the domain well enough that you can
break it into individual modules. One way to do that (and there are many) is to really listen to your business experts.
Say you are working for a startup that’s creating an expense-tracking app for small to medium-sized businesses. Here
are the business requirements:
 There are users and auditors. Users add expenses, and auditors review expense reports to ensure they align with policy
```
guidelines.
```

 When a user adds an expense, it is recorded in the database for that user.
 The app creates an audit trail that the auditors can use to ensure that everything is in order.

```
Can you identify the subdomains that should make up this application? Hint: Not everything your business users say will
translate into a module.




Solution on page 242




you are here 4  225
```


<a id='p262'></a>
<!-- Página 262 -->

modular communication




Cubicle conversation, continued...
```
Does the modular
monolith make more
sense now? Sam Alex
Mara




Alex: I get it. We’re increasing the modularity of the codebase because our
application is divided up by modules.
Sam: That sounds great in theory, but it’s not like they can all work
independently of each other. Doesn’t the ordering side of things need to know
what ingredients we have in our inventory? God forbid the kitchen should run
out of mushrooms!
Mara: You’re both right. Splitting the application up by business concern
means we’re increasing its modularity. But on the flip side, different parts of the
application might also need to talk to each other.
Alex: But it’s one codebase. I can just have the ordering side make an API call to
the inventory module, right?
Sam: Oh, brilliant. I can already see the big ball of mud forming! Soon every
module will be talking to every other module, and then there goes our modularity.
Mara: Right. If you just start making calls between modules willy-nilly, soon
enough there won’t be any boundaries left. Everything will just start referencing
everything else. And that would be, well, a big ball of mud.
Alex: So how do we maintain separate modules, but still have them talk to one
another?
Mara: Let me show you.




```

226  Chapter 7

<a id='p263'></a>
<!-- Página 263 -->

```
modular monoliths



```

Keeping modules modular
```
The auto-impo
```

Modular monoliths are, well, monoliths, so they’re generally contained your IDE is notrtyofeature in
in one codebase. That makes it easy for someone working in one module here! It’s way too ur friend
to inadvertently reach into another module and end up coupling the two accidentally refereeasy to
modules together.
```
These arrows represent calls module without re nce another
alizing it.
from one layer in a module
to a layer in another module.
One Second Another
domain domain domain

Presentation Presentation Presentation

Business rules Business rules Business rules

Persistence Persistence Persistence


If left unchecked, each module’s
code becomes more closely coupled
with the other modules’ code, and
their boundaries start to disappear. You got it!
```

The philosophy of the modular monolith centers on partitioning by domain
```
Callback to
```

within a monolithic deployment model. Your objective should be to

## Chapter 5.

create loosely coupled modules so that changing one doesn’t affect others. So
how do you avoid the big ball of mud? Read on.



```
Brain
Power
Can you think of any mechanisms to help you ensure that one part of your application won’t accidentally
access another? For example, does your favorite programming language provide any support at compile time
to keep modules separate? Jot down any ideas that come to mind here. You can see some of our ideas at the
end of the chapter.




Solution on page 242

you are here 4  227
```


<a id='p264'></a>
<!-- Página 264 -->

module separation



Keeping modules modular (continued)
From a code design perspective, it’s best to think of each module as a separate service.
Just to be clear, though, they aren’t really separate—they all still constitute one
monolithic deployment. Each “service” exposes a public API while shielding
its internal implementation from the other modules.


```
Calls to any module
happen only to their
respective APIs.
Order Recipe Inventory
domain domain domain

API API API

Implementation Implementation Implementation
(private) (private) (private)




```

As long as modules only talk to one another through their public APIs, you can
safely change one module without affecting others—thereby reducing their
coupling.
Of course, this sounds like a great idea in theory. But how can you maintain
module boundaries so well that you can sleep peacefully at night? Let’s look at
a few possibilities.


```
there are no
Dumb Questions
```

Q: Dividing my application into modules sure seems like a Do modular monoliths require more thought and discipline, and
lot of trouble. Are modular monoliths really the better option? maybe even more tooling (as we’ll see in a minute)? Absolutely.

A: We’ve said this before, and we’ll say it again—we don’t like
words like better. It’s always about trade-offs. So far, we’ve tried to
```
But the trade-off is a much more modular architecture that allows
cross-functional teams to work independently and thus move faster.

```

highlight some of the benefits of modular monoliths (and we aren’t
done yet), while also pointing out some of the challenges.




228  Chapter 7

<a id='p265'></a>
<!-- Página 265 -->

```
modular monoliths



```

Keeping modules modular (last time!)
Keeping your modules modular isn’t as easy as it seems, but don’t lose hope
just yet. You have options, depending on your technical stack—especially if
you apply some creative thinking and elbow grease.

```
Some languages, like Java, have built-in support to build
modules. The Java Platform Module System (JPMS) allows
you to build modules that are isolated from one another.
The .NET platform, meanwhile, offers namespaces that use
the internal keyword for this purpose.


Another approach is to break up your project code so
Gradle, the Java that each module is a separate folder in your repository.
build tool, supports These subprojects (or, as many build systems call them,
subprojects. multimodule projects) force isolation by virtue of being different
projects. You might even consider creating different
repositories to contain individual modules, then stitching the
complete application together at build time.
Of course, you are still deploying a monolith, so you’ll
probably need to bring all the modules together using your
build tool of choice. A monolithic deployment model doesn’t
have to mean a monolithic codebase!



Architectural governance tools, like ArchUnit for Java
projects and ArchUnitNET for the .NET platform, can Check out ts-arch
help maintain module boundaries as a project grows. for TypeScript and
JavaScript projects!
And none of these options needs to stand alone: you can
use one or more together.



there are no
Dumb Questions
```

Q: Am I way off base here, or could these techniques be useful even for layered architectures?

A: Give us a moment to wipe away the tears—you’ve grown up so fast! Absolutely; they can be useful whether your project is
partitioned technically or by domain. It’s a great idea to use tools (like ArchUnit) and language features (like JPMS) to enforce module
boundaries, regardless of architectural style.



```
you are here 4  229
```


<a id='p266'></a>
<!-- Página 266 -->

modularizing data




```
You’ve given me some great
ideas for how to modularize the
code by business concern. But if all
modules share the same database,
aren’t they still coupled at the
data level? Should I think about
modularizing the database too?




That would be the logical end of
modularization, wouldn’t it? Modularizing the
code may not be enough. If all your data is still intertwined, then
you’ve just moved your ball of mud into the database!
Before we go further, a caveat: most developers are not used to
thinking vertically along business concern lines or breaking up
their code into separate modules. Extending that modularity all
the way to the database sounds like a great idea—it is—but it
may be too much to take on all at once. Feel free to evolve your
architecture over time when needed, rather than trying to get it all
right the first time around.
Put all the lessons you’ve learned in this book at work. Do
your architectural characteristics push you to pick the modular
monolith architecture? If so, start by modularizing your code first.
Once your team gets the hang of thinking modularly, then see if it
helps to take that approach all the way into the database.
Next, let’s see what modularizing your database might look like.




```

230  Chapter 7

<a id='p267'></a>
<!-- Página 267 -->

```
modular monoliths



```

Taking modularity all the way to the database
The modular monolith is still a monolithic deployment, typically with a
monolithic database backing it. There is a lot of power here: having a
single database can make things a lot simpler. You don’t have to worry about
transactions or eventual consistency, and most developers are very comfortable
working with just one database. However, if you intend to maintain modularity
at all levels, then you should consider modularizing your data.
The rule is simple: every module should access only its own tables. Here’s how
you’d accomplish this for Naan & Pop:




```
Order Inventory
Still a modular
monolith.
Recipe



We still only have one
Each of the lettered boxeems a database for the
represents a separate scheach O I
modular monolith.
to house the tables for der,
module. (O stands for Or R
and so on.)

```

For every module in your application, you define a
schema and a set of tables. Any and all data that
belongs to a particular module will reside only in the
tables for that module.
As you can see, you can extend modularity all the
way to the database by separating data that belongs
to different modules into different tables (and maybe
even different schemas).
```
Brain
Power
Take a few moments and think about the
implications of modularizing your database.
What pros and cons can you think of?




you are here 4  231
```


<a id='p268'></a>
<!-- Página 268 -->

modularizing exercise




```
Sharpen your pencil

```

Take a look at the following table names and see if you can identify which tables belong to the schemas we’ve
identified for the Naan & Pop database. Draw an arrow from each table to its schema.

```
This is a table.
customers order_history




recipes


ingredients


delivery_addresses




order_schema recipe_schema inventory_schema




These are the schemas
we’ve identified.


Solution on page 243



```

232  Chapter 7

<a id='p269'></a>
<!-- Página 269 -->

```
modular monoliths



```

Beware of joins
Keeping different tables, perhaps even in different schemas, does partition the data
belonging to different modules—but it’s easy to slip up and accidentally perform a SQL
join across tables that belong to different modules. Then you’re back to tight coupling!
It’s OK to store the IDs of records that belong to one module in another module’s tables.
For example, the Naan & Pop Order domain is allowed to store “recipe item” IDs in its
```
Read th
This is noatt again!
```

tables within the order_schema. If it ever needs more information about a particular item,
it calls the Recipe module’s API and provides it with the recipe item’s ID.
```
key refere a foreign
nce.


I need the details
Hold on! Let
for recipe_item_id 2.
me look this up
I’m going to reach out
for you.
to the Recipe domain.



Order
Invoke the Recipe
module API by passing Recipe
domain in recipe_item_id. domain

```


## API API


```
Implementation Implementation
(private) (private)

The Recipe module
responds with
the recipe details
order_schema requested. recipe_schema
orders recipes
id recipe_item_id ... id ingredients ...




```

And there you have it. Now, as we’ve done before, we’ll show you some of the
strengths and weaknesses of modular monoliths, followed by our star rating chart.




```
you are here 4  233
```


<a id='p270'></a>
<!-- Página 270 -->

modularity superpowers



Modular monolith superpowers
Here are some good reasons to use modular monoliths:




```
Domain partitioning
Architects can design components
around domain concerns, then build
teams that specialize in one or more of
these domains (as opposed to a technical
specialization). Domain partitioning is
the key superpower of this architectural
style.


Domain-based alignment
Modular monoliths encourage crossfunctional teams, which are better aligned
with the domain than the technically
partitioned teams used in layered
Performance
architectures. Performance is usually very good, like
for
most monolithic architectures. There
are
no network calls between modules, and
all data processing happens in a sing
le
place.

Maintainability
Modular monoliths separate business
concerns from one another, with crossfunctional teams each specializing in
a subdomain. This makes it easier to
maintain the code, as long as changes
don’t cross into other domains.



```

Testability
Since the scope of changes is limited to one module,
testing is much easier. And since a cross-functional
team’s members understand their subdomain
really well, they can build out an entire testing suite,
including integration, smoke, and end-to-end tests.



234  Chapter 7

<a id='p271'></a>
<!-- Página 271 -->

```
modular monoliths



Modular monolith kryptonite
Of course, there are always trade-offs. Here are some reasons not to
use a modular monolith architecture:


Hard to reuse
Modular organization makes it hard to
reuse logic and utilities across modules.
For example, you can’t share common
functionality between modules without
extracting it as a dependency, increasing
the coupling between the modules.




(Still) a single set of
architectural characteristics
Even though modular monoliths are
organized by modules, you still get a
single set of architectural characteristics
for the entire application—even if one
business concern has a different set of
needs than others.



```

Modularity can be fragile
It’s easy to dilute module boundaries
accidentally. Avoiding the big ball of Operational characteristics
mud takes a lot of governance—and the Despite its focus on business concerns,
database is even harder to govern. a modular monolith is still, well, a
```
monolith. And as with any monolith,
It’s particularly operational characteristics like elasticity
hard to avoid joins and fault tolerance tend to be hard to
in SQL via tooling. attain.




you are here 4  235
```


<a id='p272'></a>
<!-- Página 272 -->

strengths and weaknesses



Modular monolith star ratings
We’ve created a star rating chart for modular monoliths, just like the one we
showed you for layered architectures in the previous chapter. One star means
that the architectural characteristic is not well supported; five stars means it’s
```
s.
Just like movie review
```

very well supported.




```
Architectural Characteristic Star Rating

Maintainability Studio Studio Studio




These fare
better than Testability
in the layered
Studio Studio Studio




architectural Deployability
style.
Studio Studio Studio




Simplicity Studio Studio Studio Studio




Evolvability
```

Most monolithic
```
Studio Studio Studio




```

architectures perform
well, especially if well Performance Studio Studio Studio




designed.
```
Scalability Studio




Elasticity Studio




```

Overall, more Fault Tolerance
expensive than layered
```
Studio




```

architectures. Modular
monoliths require more Overall Cost $$
planning, thought, and
long-term maintainance.
```
You’ll notice that our ratings for modular monoliths’ operational characteristics
aren’t all that different from those for layered architectures. From a process
perspective (that is, in terms of maintainability, testability, and deployability),
however, the modular monolith does a lot better than the layered architecture.
That’s because changes to a particular module only affect that module and can
be tested in isolation, which reduces the risks involved in deploying software.
Modular monoliths cost a little more than layered architectures because they
require the team to be vigilant. They also involve additional governance and
tooling to maintain module boundaries.


```

236  Chapter 7

<a id='p273'></a>
<!-- Página 273 -->

```
modular monoliths




Exercise
```

Which of the following systems might be well suited for the modular monolith architectural style, and why? Hint: Take
into account its superpowers, its kryptonite, and the problem domain.


An online auction system where users can bid on items Well suited for modular monoliths
```
Why? Might be a fit for modular monoliths
Not well suited for modular monoliths




A large backend financial system for processing and Well suited for modular monoliths
settling international wire transfers overnight Might be a fit for modular monoliths
Why?
Not well suited for modular monoliths




```

A company entering a new line of business that Well suited for modular monoliths
expects constant changes to its system Might be a fit for modular monoliths
```
Why? Not well suited for modular monoliths




A small bakery that wants to start taking online orders Well suited for modular monoliths
Why? Might be a fit for modular monoliths
Not well suited for modular monoliths




```

A trouble ticket system for electronics purchased Well suited for modular monoliths
with a support plan, in which field technicians Might be a fit for modular monoliths
come to customers to fix problems
```
Not well suited for modular monoliths
Why?




Solution on page 244

you are here 4  237
```


<a id='p274'></a>
<!-- Página 274 -->

chapter summary



Naan & Pop is delivering pizza!
The development team has finally grokked modular monoliths! With a modular
codebase and a modular database, they now feel ready for any other big changes
to Naan & Pop’s menu. Rumor has it that the owners plan to introduce a full
Mediterranean menu next. We can’t wait, and we wish them a lot of luck!




Bullet Points
 A modular monolith is a monolithic architectural style  You can govern a modular monolith using a variety of
```
that is partitioned by domains and subdomains that techniques. Some languages have built-in support for
reflect business concerns, not technical concerns. building modules.
```

 Each subdomain makes up one module of the  Another approach is to physically break up the
```
application. Each module can contain multiple codebase into separate subprojects or even different
business use cases. repositories. This usually involves using a build tool to
bring all the modules back together when you build
```

 Each module can be made up of layers to provide
```
the monolith.
better organization. A module may be technically
partitioned as a means to organize its functionality.  Third-party tools can also help with architectural
governance.
```

 Avoid having code in one module directly access any
```
functionality in other modules. Allowing this can  You may choose to use several techniques in
reduce or eliminate the boundaries between modules. combination to ensure the boundaries of individual
modules are maintained.
```

 Each module should have a public API that
```
communicates with other modules while shielding  You can extend modularity all the way to the
the module’s internal implementation from the rest of database, keeping the data for each module separate.
the world.
 Watch that you don’t accidentally couple modules
```

 Avoiding intermodule communication allows when inserting or fetching data (for example, when
```
modules to change internally without affecting other using a SQL join statement across tables that belong
modules. to different modules).
```

 It takes time and effort to ensure that the modules in
```
a modular monolith remain separate and distinct.




```

238  Chapter 7

<a id='p275'></a>
<!-- Página 275 -->

```
modular monoliths



Modular Monolith Crossword
Modular monoliths are about separating business concerns. Take a look at
these separate clues and test your knowledge about this architectural style.




```

Across Down
1. Java _____ Module System 1. The latest addition to Naan and Pop’s menu
6. _____ to one module don’t require _____ to the others 2. In a domain-partitioned architecture, each domain gets its
8. The Recipes _____ interface is part of the Recipes domain own _____
9. Each module exposes a public _____ 3. If something is an implementation _____, it’s not an
10. Modular monoliths are good when many teams need to _____ architectural concern
their work 4. If technical concerns are like horizontal “slices” of a monolith,
13. Monoliths generally have one big _____base business concerns are ____ slices
15. Highly rated characteristic in most monolithic architectures 5. “Spaghetti code” is too closely ____
18. Each domain in this style represents a _____ concern 7. This system is for ____ & Pop
19. With a modular monolith, _____ are often cross-functional 11. A challenging kind of architectural characteristic for
20. Smaller bits of functionality can reside in their own _____ monoliths
domains 12. Modules use ID references in ____ to look things up
21. It’s important to maintain _____ between modules 14. Monolithic and distributed are two kinds of deployment ____
22. Style of monolithic architecture first used in this system 16. Example of a language that supports creating modules
23. Databases can show modularity by representing an entity via 17. Modules communicate indirectly, through their ____ APIs
a _____ 19. Databases build schemas from related ____

```
Solution on page 242

you are here 4  239
```


<a id='p276'></a>
<!-- Página 276 -->

exercise solutions



```
Exercise From page 217
Solution
```

Cast your mind back to the layered architecture we built for Naan & Pop in Chapter 6. The following diagram shows its
layers and logical components. Adding a new category to the menu (say, pizza) means changing a bunch of moving
parts. Grab a marker and put a triangle ( ) next to everything this new requirement will affect.

```
Order Recipe Inventory
Domain Domain Domain


Place Order Recipes UI Inventory UI Presentation



Place Order Manage Manage
Deliver Order Recipes Inventory
Business rules


Delivery Recipe
Order Customer Recipe Item Persistence
Location



```

Here’s some space for you to explain your thought process:

Offering pizzas probably means the menu will need a new listing. We might need to allow for customized toppings,
which would affect the presentation layer and the associated pricing and could introduce new rules. There
might be time constraints on deliveries (no one wants a cold pizza). The customizations might also affect how
we persist pizza orders (as opposed to other kinds of orders).
However, the recipe and inventory domains won’t be affected. A recipe is a recipe is a recipe—a list of
ingredients with a set of steps to follow. And while there may be new ingredients, the inventory domain will
manage them just like it would any other ingredients.




240  Chapter 7

<a id='p277'></a>
<!-- Página 277 -->

```
modular monoliths




Who Does What From page 220


Solution
```

Identifying which components should belong to a particular module can be tricky.
In this game of “Who Does What?”—or rather, “What Goes Where?”—we’d
like you to match each component to the module where it fits best. Multiple
components can belong to one module.




Shopping Cart Order

Credit Card Form


Primary Email Payment
Preference

Fulfillment
Workflow
```
Customer

```

Order History




```
you are here 4  241
```


<a id='p278'></a>
<!-- Página 278 -->

exercise solutions



```
Exercise From page 225
Solution
```

A critical piece of successfully developing modular monoliths is understanding the domain well enough that you can
break it into individual modules. One way to do that (and there are many) is to really listen to your business experts.
Say you are working for a startup that’s creating an expense-tracking app for small to medium-sized businesses. Here
are the business requirements:
 There are users and auditors. Users add expenses, and auditors review expense reports to ensure they align with
```
policy guidelines.
```

 When a user adds an expense, it is recorded in the database for that user.
 The app creates an audit trail that the auditors can use to ensure that everything is in order.

```
Can you identify the subdomains that should make up this application? Hint: Not everything your business users
say will translate into a module.

Expense Audit User
domain domain domain


This could be
Both users and a n
auditors could be dom“Iadentity”
managed as “users.” in as well.




Brain From page 227

Power
Can you think of any mechanisms to help you ensure that one part of your application won’t accidentally
access another? For example, does your favorite programming language provide any support at compile time
to keep modules separate? Jot down any ideas that come to mind here.
•<insert your favorite programming language> feature
• Repository structure
• Build tool capabilities
•Third-party libraries and governance frameworks



```

242  Chapter 7

<a id='p279'></a>
<!-- Página 279 -->

```
modular monoliths




From page 232
Sharpen your pencil
Solution
```

Take a look at the following table names and see if you can identify which tables belong to the schemas we’ve
identified for the Naan & Pop database. Draw an arrow from each table to its schema.


```
This is a table.
customers order_history




recipes


ingredients


delivery_addresses




order_schema recipe_schema inventory_schema




These are the schemas
we’ve identified.




you are here 4  243
```


<a id='p280'></a>
<!-- Página 280 -->

exercise solutions



```
Exercise From page 237
Solution
```

Which of the following systems might be well suited for the modular monolith architectural style, and why? Hint: Take
into account its superpowers, its kryptonite, and the problem domain.


```
An online auction system where users can bid on items Well suited for modular monoliths
Why? This system probably needs high degrees Might be a fit for modular monoliths
of scaling and elasticity. Monoliths aren’t Not well suited for modular monoliths
ideal for such systems.

A large backend financial system for processing and Well suited for modular monoliths
settling international wire transfers overnight Might be a fit for modular monoliths
Why? Financial systems have rich domains;
Not well suited for modular monoliths
scalability and elasticity don’t sound like
concerns here.

A company entering a new line of business that Well suited for modular monoliths
expects constant changes to its system Might be a fit for modular monoliths
Why? A high degree of modularity is good for Not well suited for modular monoliths
handling changes, but it certainly depends
on what kinds of changes are expected.

A small bakery that wants to start taking online orders Well suited for modular monoliths
Why? Ha! We kinda gave this one away, didn’t we? Might be a fit for modular monoliths
Not well suited for modular monoliths




A trouble ticket system for electronics purchased Well suited for modular monoliths
with a support plan, in which field technicians Might be a fit for modular monoliths
come to customers to fix problems
Not well suited for modular monoliths
Why? Lots of moving parts; this system probably
needs high degrees of elasticity and
scalability.


```

244  Chapter 7

<a id='p281'></a>
<!-- Página 281 -->

```
modular monoliths




```

Modular Monolith Crossword Solution



```
From page 239




you are here 4  245
```


<a id='p282'></a>
<!-- Página 282 -->


<a id='p283'></a>
<!-- Página 283 -->

8 microkernel architecture
```
Crafting
Customizations




You can craft custom experiences, one capability at a
time. Some architectural styles are particularly well suited for some capabilities,
and the microkernel architecture is the world champion at customization. But it’s
also useful for a bewildering range of applications. Once you understand this
architectural style, you’ll start seeing it everywhere!

Let’s dig into an architecture that lets your users have it their way.



this is a new chapter   247
```


<a id='p284'></a>
<!-- Página 284 -->

going green requirements



The benefits of Going Green
What does everyone have lying around? Old electronics! Going Green is a fastmoving startup that plans to capitalize on the market for buying and recycling old
cell phones, music players, and other small electronics.
After analyzing the architectural characteristics required, the architects have
designed a three-part system, and each part of which needs different capabilities.
They’d like your help. Ready? Here’s the system so far:

```
The public-facing parts
of the architecture are
Public user a website and in-store
Get quote interfaces kiosks.


Device
assessment
Good offer,
Going Green
send device If Going Green accepts the evaluates the
device, it pays the customer device based on its
```

If the device will based on the quote. age and condition
yield a good return, and determines its
Going Green will $$$
```
$$$
```

resell it... value.
```
Resell
Recycling/
accounting
Recycle

Based on its resale
…otherwise, Going potential, Going Green will
Green will recycle it. either resell or recycle the
device.
Brain
Power
Based on what we know about Going Green’s business model and the corresponding separation of
responsibilities in its system, would it be easier for this company to build a monolithic or a distributed
architecture? Why?




```

248  Chapter 8

<a id='p285'></a>
<!-- Página 285 -->

```
microkernel architecture




```

BE the architect
```
Architects just can’t stop analyzing
stuff. Can you determine
three important architectural
characteristics for each of the
three services in the new Going
Green architecture?



Fill in some
Architectural characteristics architectural
characteristics
```

Public user Scalability for each service.
interfaces




```
Architectural characteristics
Device
assessment




Architectural characteristics

```

Recycling/
accounting



```
Solution on page 272

you are here 4  249
```


<a id='p286'></a>
<!-- Página 286 -->

microkernel basics



Cubicle conversation Mara Alex

Sam




Mara: We need to split up the architecture work for the Going Green application.
Mara, you and Alex should work on the device assessment service.
Alex: Great! That’s the service that assesses the devices users send us to determine
value, right? Seems like one of the more interesting parts of the application.
Sam: How often will we need to add new device configurations to the assessment
service?
Mara: At least a few times a month, sometimes even a few times a week. This is
especially important, because how fast we can update the device assessment service
directly affects the company’s profitability.
Sam: Why such a direct connection?
Mara: Going Green makes a profit when it resells the highest-value electronics it
receives. Generally, newer devices are in better shape and are worth more. The faster
we can add new device assessments, the more money the company makes.
Alex: Wow, so rapid change is a BIG deal for this service.
Mara: It is! And don’t forget, we have to make sure that supporting new devices
won’t affect the system’s support for the existing ones. Are y’all up for it?
Sam and Alex: You bet!
Mara: I think we should consider using a microkernel architecture. That style makes
it easier to design and add new capabilities using plugins.




250  Chapter 8

<a id='p287'></a>
<!-- Página 287 -->

```
microkernel architecture



```

The two parts of microkernel architectures
The microkernel architecture derives its name from operating system design. The
kernel, or core, of an operating system is very small, offering only the most basic
capabilities. A microkernel architecture consists of two primary parts: its core and its
plugins (any number of them).


```
The core is singular and
static.

The plugins in Plugin The components can reside
a microkernel Plugin
in either a monolithic or a
architecture are distributed architecture—
plentiful and volatile. Plugin Core Plugin more about this soon.
Plugin Plugin
```

There’s only one core
in a microkernel
architecture.
```
The core in a microkernel: Plugins in a microkernel:
Plugin
• provides minimal functionality • provide all custom behavior
• rarely changes after its initial implementation • work in isolation from one another
Core Plugin
• does not provide custom behavior • are deployed independently

Plugin
How many plugins
in a microkernel?
… Anywhere from one
to many.
there are no
Dumb Questions
```

Q: Is the microkernel architecture technically or domain-partitioned?

A: Flashback to Chapter 5! Most microkernel architectures are technically partitioned. You could divide the core into layers—perhaps
one for presentation, another for business or workflow logic, and so on. However, microkernel is one of those strange architectural styles
that can also be domain-partitioned, depending on how you design your plugins.

As for deployment models, microkernel architectures are usually monolithic. As you’ll see in this chapter, however, in some scenarios a
distributed model might make more sense.



```
you are here 4  251
```


<a id='p288'></a>
<!-- Página 288 -->

“microkern-ality”




```
Wait a minute. Just about all the
software I use supports plugins
one way or another. Are you
telling me that all those systems
use the microkernel architectural
style?




Not quite. Every microkernel has plugins,
but not all plugins belong to microkernels.
Unfortunately, there is no definitive dividing line between
microkernel systems and systems that support plugins. Mostly,
we evaluate how “microkernel-y” an architecture is (let’s call
that “microkern-ality”) by how functional its core is without
any plugins and how volatile its core is (how often it needs to
change).




```

252  Chapter 8

<a id='p289'></a>
<!-- Página 289 -->

```
microkernel architecture



```

The spectrum of “microkern-ality”
Lots of software supports plugins: IDEs, web browsers, build tools, you name it. But simply A browser is perfectly
supporting plugins doesn’t make a system a microkernel—it’s all about the core. In extreme useful without any plugins,
microkernels, the core can do very little useful work without plugins installed. so it’s not much of a
```
microkernel.

Eclipse IDE Insurance application Web browser
```

The Eclipse IDE is desgined as An insurance application has standard rules for Web browsers support plugins but
a “pure” microkernel, facilitating each policy yet allows customization for unique don’t rely on them to function.
different languages and tools via local rules and regulations, so it has a medium
plugins. level of functionality without plugins.




```
less more
functional
Degree of “microkern-ality” functional
Functionality/volatility of core


Continuous Insurance claims
Linter
```

Linters are tools that use integration tool processing system
```
These systems are a common
```

plugins to parse source code (like Jenkins) example of customization. They
and apply style and syntax Jenkins works as a standalone usually handle most claims in a
rules to it. Most programming continuous integration (CI) tool, but standard way but allow developers
languages have linters; for it supports a number of plugins for to build custom rules for specific
example, JavaScript has extensibility. situations.
esLint.

```
there are no
Dumb Questions
```

Q: Is every system that supports Q: Is this architectural style only Q: Are microkernel and
plugins a microkernel? useful for software development tools? microservices the same thing?

A: Not at all. Lots of systems support
plugins. How much of a microkernel it is
```
A: A lot of development tools use this
architecture because it lets them offer
A: No, the similarity in the names is just
a coincidence. Microkernel’s name comes
```

(and no one is actually grading you on this) programmatic customization, but many from operating system design, whereas
depends on the volatility and functionality business and other applications use it microservices is named for its relatively
of its core. too. It works for any problem domain that small and separate deployment units in a
```
requires customization and in which each distributed architecture.
change acts in isolation.



you are here 4  253
```


<a id='p290'></a>
<!-- Página 290 -->

“microkern-ality” exercise




```
Exercise
```

The microkernel architectural style shows up in lots of places. See if you can place the specific tools and
categories below in the correct place on the spectrum, by determining how much of a microkernel each one is.
Hint: Each system’s degree of “microkern-ality” depends on how useful it is without plugins.


We did one for you. Eclipse Not familiar with the BFF pattern?
is an example of a product Check out https://samnewman.io/
defined by its “microkern- patterns/architectural/bff/.
ality.”
```
IDE with plugin Backend for Frontend
support (BFF) design pattern
(not Eclipse)
Eclipse IDE Web browser
Device
Mobile device
assessment
operating system
service for a
recyling business


```

less more
functional
```
Functionality/volatility of core functional



Degree of “microkern-ality”


Solution on page 273




```

254  Chapter 8

<a id='p291'></a>
<!-- Página 291 -->

```
microkernel architecture



```

Device assessment service core
You and your team all agree to use a microkernel architecture for the new
device assessment service.
The core system includes the criteria needed to assess a device, like its age,
condition, and model number. For each type of device, it defers to a devicespecific plugin that executes the rules to determine how the system will assess
the device’s resale value.


```
The stable core holds
the assessment steps
(but not the details).



Device 3
Device 1


Assessment Device 4
Device 2 ser vice

The plugins use Device 5
synchronous communication
to interact with the core.
Plugins are
independently deployed
and are decoupled
from each other.

```

You decide to use a distributed physical architecture for the plugins, for better
scalability. This also gives Going Green the option to add plugins in other
languages in the future.
Finally, you decide on synchronous communication, because the service
is sufficiently responsive that there’s no need to add the complexity of
asynchronous communication.
Let’s dig into those decisions a little further.




```
you are here 4  255
```


<a id='p292'></a>
<!-- Página 292 -->

distributed plugins




```
I can see that it’s common
to implement plugins as components
within a monolithic architecture. But doesn’t
having everything in one deployment make
it harder to hot-deploy plugins? It would be
easier if they were distributed. Could we
build distributed plugins?




Yes, we could! The architecture’s
capabilities determine whether to
encapsulate or distribute the plugins.
Some microkernel architectures include both the core system and the
plugins in a single monolithic architecture; others are distributed, as you
might recall from Chapter 5.
The microkernel style exists in the shadowy netherworld between
monolithic and distributed architectures. Architects can implement it with
either deployment model.




there are no
Dumb Questions
```

Q: Does a microkernel architecture’s Q: How do I implement plugins? Q: Can I implement plugins in
core system have to be a monolith? different tech stacks than the stack in

A: A: You can implement your own plugin which the core is written?
```
Not necessarily—microkernels often
```

feature in hybrid architectures. When
it makes sense (such as for a desktop
```
designs using interfaces, but virtually all
platforms and technology stacks have
libraries and frameworks to help out.
A: One of the advantages of using
distributed plugins is that you can write
```

application), you might implement the core them using any platform you can call via a
as a single system; other times, you might network connection.
distribute parts of the core as well as the
plugins.



256  Chapter 8

<a id='p293'></a>
<!-- Página 293 -->

```
microkernel architecture



```

Encapsulated versus distributed plugins
The core system in a microkernel is where the plugins, well, plug in. Generally,
we implement that connection via an interface. The plugin implements the
interface, while the core system supports that component via that interface.
If we design a microkernel as a monolithic architecture, we’ll implement each
plugin as a component that connects to the core through the interface.




```
Plugin
Monolithic implementations of
Plugin
microkernel architectures embed
Plugin Core system Plugin the plugins as components within
the overall monolith.
Plugin Plugin




```

In other implementations of microkernel architectures, plugins are
distributed: web endpoints, event queues, and so on. In addition,
we can decide whether to call the plugins synchronously or
asynchronously. (We’ll cover this in much more depth in Chapter 11.)


```
Distributed plugins
can communicate
with synchronous
or asynchronous
calls.
Plugin
Plugin


Plugin
Core system
Plugin


Solid lines indicate Plugin

synchronous calls;
dashed lines are
async calls.



you are here 4  257
```


<a id='p294'></a>
<!-- Página 294 -->

plugin exercise




```
Exercise
```

The assessment service team at Going Green must decide whether the microkernel’s physical architecture should
be monolithic (core and plugins in the same deployment unit) or distributed (plugins deployed separately from
the core). They need your help with the trade-off analysis. Can you list some pros and cons for each option?
We’ll get you started. Hint: Consider how each option would affect things like architectural characteristics.

```
Most monoliths only
```

Monoliths generally provide load plugins on startup,
better performance because which can complicate
they make fewer network calls. deployment.
```
Monolithic
Pros Cons
Performance Single deployment

Plugin Plugin
Core
Plugin
system Plugin

Plugin Plugin




Distributed
Pros Cons
Plugin
Plugin


Core Plugin
Plugin
system
Plugin




Solution on page 274

```

258  Chapter 8

<a id='p295'></a>
<!-- Página 295 -->

```
crafting customizations



```

Plugin communication
To be useful, plugins must communicate with the core system. For example,
the core will call a method (based on an interface) and utilize the results. This
communication can be implemented in a couple of different ways, based on
factors like physical architecture.



```
iPhone15 The core system can call any
component that implements the
```

iPhone15 implements DeviceIntf Core system DeviceIntf interface.
```
The iPhone15 device plugin
implements the DeviceIntf
interface, allowing calls between
the plugin and the core.

```

How the actual call happens between the core and a plugin depends on
the physical architecture you use to implement the plugins. In monolithic
architectures, we implement plugins in the same technology stack as the core
and deploy them as native components for the platform (like JAR files for Java,
DLLs for .NET, or GEMs for Ruby).
As for distributed plugins, the core can call them with synchronous or
asynchronous calls. Developers aren’t restricted to the core’s implementation
platform, either—they can write plugins in a variety of languages.




```
Plugin

Plugin access can be asynchronous,
synchronous, or mixed within the Core system
same application.
Plugin REST


Architects can implement plugins
in different tech stacks.

you are here 4  259
```


<a id='p296'></a>
<!-- Página 296 -->

interview with a plugin




```
Plugging into the star attraction of the
microkernel: the Plugin


```

Head First: Let’s see... let me get my microphone Head First: OK, fair enough. But let’s talk about
plugged in. Testing, testing... OK, welcome, Plugin! working with overly volatile cores.
Plugin: How appropriate! All sorts of things use me to Plugin: Alas, that’s one of the downsides to starring in
function. I’m happy to be here—and excited to clear up a microkernel architecture—when the core decides to
some controversies. change all the time. Change is my job! The more the core
```
changes, the more it’s likely to interfere with what I’m
```

Head First: Everyone says you’re the star of the
```
doing. I strive for professionalism, so I prefer to work with
```

microkernel architecture, yet the core gets more press
```
nice, stable cores with no drama.
```

time and attention. Is that fair?
```
Head First: You get a lot of press because of your ability
```

Plugin: Well, that may be true, but what good is the core
```
to handle customization, but do you have other roles?
```

without me? It may be bigger, but without me, the core is
```
What else you can handle?
```

boring.
```
Plugin: Thanks for asking, Head First. It’s always
```

Head First: You certainly show up in lots of places.
```
annoying to be pigeonholed into my best-known role. I
```

What about your controversial role in non-microkernel
```
can handle customizations without ugly, long switch
```

architectures? Lots of systems support plugins that aren’t
```
statements, using an elegant architectural style, without
```

microkernels...
```
even batting an eye. We plugins can be used for all kinds
```

Plugin: I’m happy wherever I appear. To be truthful, of things—really, anything that needs good isolation.
though, I prefer microkernels. For other architectures, For example, I show up all the time in A/B testing. The
plugins are just condiments—we’re not necessary, but we architects keep the old behavior in PluginA, add the new
add some nice flavors. In a microkernel, though, I’m the behavior in PluginB, and decide which to call. I also have
main course! The whole architecture is based on me. I starring roles in integration hubs, developer tools, and lots
appreciate that level of importance. of other places.
Head First: Let’s dig into something that seems to Head First: Before we finish up, is there anything you’d
appear in trade-off analyses all the time. Your distributed like to plug?
version has some performance issues, no?
```
Plugin: You bet! Look for me in an architecture near you,
```

Plugin: Hey, you can’t say bad things about all either as an integral part of a monolith or as an endpoint
plugins just because we have some trade-offs! Yes, it’s for a distributed microkernel.
true that when we use network calls to communicate,
performance does take a hit. But you know what else?
Those distributed plugins can scale better, and you can
write them in a variety of languages. Different strokes
for different folks, right? And different plugin physical
architectures for different trade-offs.


260  Chapter 8

<a id='p297'></a>
<!-- Página 297 -->

```
microkernel architecture



```

Cubicle conversation
```
Alex Sam

Mara: Hi, all. Just stopping by to take a look
at your trade-off analysis for the Going Green
assessment service. Have you decided yet between a
monolithic and a distributed physical architecture?
Sam: We’re working on it. I did the trade-off
analysis for the distributed version, and personally,
I’m a big fan. Here’s our summary:
Mara


Pros Cons
Plugin

Availability Plugin
Less performant
Plugin
Core system
Deployability Plugin
More complex
Scalability Plugin




```

Mara: Can you explain how you arrived at these conclusions?
Alex: Sure. For the distributed version, we don’t have to restart the core system to add
new devices. That gives us better availability than the monolithic version, since that
requires a restart to load new device plugins. Also, it’s simpler to deploy a single plugin
than to redeploy the whole assessment service. Since the plugins don’t run in the same
process as the core, we can make the whole system more scalable. But that would take a
toll on its performance—after all, network calls take a lot longer than in-process ones.
Mara: That sounds like a good trade-off. The business agrees that scalability is very
important for the new system.




```
you are here 4  261
```


<a id='p298'></a>
<!-- Página 298 -->

microkernel Q&A




```
there are no
Dumb Questions
```

Q: Where is the user interface in a microkernel Q: Is the microkernel style the only way to handle
architecture? customization?

A: It depends! If the system is monolithic, architects commonly
include the UI as part of the core system. However, when you
```
A: Not at all. It’s one of many ways. A microkernel architecture
is useful when the structure of your system—its core capabilities
```

design a service in a distributed architecture as a microkernel, that rarely change—requires discrete customization via plugins.
other parts of the system typically handle the UI. For systems without that kind of structure, other architectural

Q: styles may be more appropriate.
```
Can the UI utilize a microkernel?
Q: What’s the internal structure of the core system? Is it
```

A: You bet it can. In fact, lots of UI patterns (like the BFF just one big logical component?
pattern we mentioned earlier) use the microkernel structure to
handle customized UI endpoints such as iOS, Android, and web
browsers.
```
A: In the microkernel style, we design the core system based
on how we want to organize the logical components in the system.
For example, if we want to separate capabilities within the core,
```

Q: Isn’t a microkernel really just the Decorator design
pattern?
```
we might choose to implement the core via layers, as we would
in the layered architectural style. On the other hand, we might
follow DDD and design the core around a bounded context, as
```

A: Good catch! While their purposes are mostly the same, the
microkernel architecture is one way to implement the Decorator
```
in the modular monolith style. The microkernel style is often
used in hybrid architectures where customizability is a driving
characteristic.
```

design pattern. Compared to design patterns, architecture
requires more thought about physical limitations and possibilities.
For example, design patterns don’t account for capabilities like
scalability.




262  Chapter 8

<a id='p299'></a>
<!-- Página 299 -->

```
microkernel architecture




```

I’m thinking it would
be a bad idea to allow
plugins to talk to one
another. Am I right?




```
Plugins can talk to one another in a
microkernel through the core system. But
should they?
Plugins typically communicate with the core system by implementing
an interface that the core supports. That makes it possible for plugins to
communicate with each other “through” the core system. For example, the
Eclipse IDE, which supports multiple languages, allows language-based
tools (like compilers and debuggers) to interact with each other in this way.
Be cautious about allowing inter-plugin communication, though! It has
some serious negative trade-offs. First, it requires consistent contracts
between the core and the plugins, which eventually involves versioning.
(More about contracts on the next page.) For example, one thing that
makes Eclipse complex is the transitive dependencies between its
components, which can cause versioning headaches. Second, dependencies
between plugins create availability issues, because you must guarantee that
all necessary plugins are present at runtime.
To understand the problems with letting plugins chat amongst themselves,
we have to look at the two ways the core communicates with plugins.




you are here 4  263
```


<a id='p300'></a>
<!-- Página 300 -->

plugin communication



Plugin contracts
When architects implement microkernel architectures, we usually ensure that the core
calls plugins using a contract (another word for interface). That communication is solely
between the plugin and the core, not between plugins. If you allow communication between
plugins, the core has to act as their intermediary.
In the example system below, PluginA doesn’t know or care about other plugins; it
communicates only with the core. However, PluginX needs to communicate with
PluginY, and that communication must be mediated by the core system.


```
When architects allow inter-plugin
communication, the core system
must act as an integration hub.

Core system
PluginA
PluginA doesn’t
care about anything
in the world except
Translation
itself and its core.

PluginY PluginX



PluginX and PluginY call each
other, so changes to one or the
other, or to the mediation layer
within the core system, will
affect both plugins.
Brain
Power
You know you have to worry about intermediary communication through the core system, but consider this:
what happens when you update PluginY in a way that changes the contract between PluginX and PluginY? If
you don’t want to change PluginX when you change PluginY, how could you manage that communication?




```

264  Chapter 8

<a id='p301'></a>
<!-- Página 301 -->

```
microkernel architecture



```

Going Green goes green
After considering how best to implement the plugin interaction with the core,
the team decides to define an interface (called DeviceInterface) for each plugin to
implement. Now Going Green can add new devices just by implementing the
interface and customizing the valuation process for that specific device.




```
Assessment steps (but
The DeviceInterface not the details) exist
provides a common way for in the stable core.
plugins to communicate with
the device assessment core.


Device 1 Device 3


Assessment
Device 4
ser vice
Device 2
Device 5
The plugins use
synchronous communication
to interact with the core. Plugins are independently
deployed and decoupled from
each other.


```

Your device assessment engine is a success. Well done!
To wrap up, let’s quickly summarize the strong and weak points of this style of
architecture.




```
you are here 4  265
```


<a id='p302'></a>
<!-- Página 302 -->

microkernel architecture superpowers




Microkernel superpowers
The microkernel is a common architectural style. It’s also one of the most
common styles you’ll find within hybrid architectures that require customization.




```
Who you gonna call to customize
part of your application?
Microkernel to the rescue!
```

Custom behavior
```
best
```

The microkernel is “shaped” in the
way to handle customi zatio ns.




```
Adaptability
Adaptability, as an architectural
characteristic, implies the ability to keep
existing functionalities and continue
adding more. A microkernel supports
```

Evolvability this well; you can keep old plugins as
```
you
```

Evolvability, as an architectural implement new ones.
```
can
```

characteristic, means that architects
make fundame ntal und erly ing chan ges
that gradually evolve the system awa
```
y Simplicity for the win!
avio rs. Unl ike ada ptab le
from its old beh
```

architectures, evol vabl e arch itect ures Simple structure
```
short
```

only support the old behaviors for a A microkernel has two basic moving
```
parts
offe r an exce llen t way to (the core and plugins), making it easy
```

time. Plugins for
implement this capability. developers to understand and implem
```
ent.


Par titiornnelin g The microkernel is a
, you can handle great example of an
In a microke
ith design or with architectural approach
customization w sign,
ever, if you use de to customization.
architecture. How t
ust be very diligen
the developers m co rrec tly. If
the design
about following ou nd pl ug ins,
tured ar
the system is struc
clearer.
the distinction is

```

266  Chapter 8

<a id='p303'></a>
<!-- Página 303 -->

```
microkernel architecture




Microkernel kryptonite
The microkernel architecture’s weaknesses mostly appear when architects use
it improperly: for example, when the core changes too much or when plugins
must communicate heavily with one another.



Misaligned volatility
In a microkernel, the core system shou
ld
change very little once it is implemente
d. If
it changes a lot, that is likely a sign that
this
is not the ideal architectural solution
or you
have made the wrong things plugins.


One of the most common
mistakes in a microkernel is
a too-volatile core, due to
frequent domain changes.

Sharing betwee n plugins
sharing
While it’s often tempting,
dependencies (such as shared libraries)
between plugins is generally a bad idea
because it creates headaches around
coupling and deployment.
To keep a microkernel from Chatty plugins
devolving into a big ball of mud, Allowing plugins to interact may be
keep an close eye on coupling via tempting, but it comes with a host of
sharing. difficult trade-offs. Successful systems
that
use this approach (for example, Eclipse)
```

Performance
```
do so at the cost of high complexity.
```

When using distributed plugins for a
```
ce
```

physical architecture, you might noti
```
, dep end ing on
```

an impact on performance
the communication prot ocol s and how
much information passes between the
core and the plugins.




```
you are here 4  267
```


<a id='p304'></a>
<!-- Página 304 -->

strengths and weaknesses



Microkernel star ratings
We’ve created a chart of star ratings, like the ones we showed you for layered
and modular monolith architectures, to indicate how well microkernel
architectures do with each of the architectural characteristics listed. One star
```
s.
```

means that the architectural characteristic is not well supported; five stars
```
Just like movie review
```

means it’s very well supported.




```
Testing is
straightforward
Star Rating in a microkernel;
Architectural Characteristic teams can test
Maintainability the core and
plugins separately.
Studio Studio Studio




Testability Studio Studio Studio




Deployability Studio Studio Studio




```

A microkernel has a Performance
easy-to-understand Simplicity Studio Studio Studio Studio




```
is better with
```

structure. embedded plugins.
```
Evolvability Studio Studio Studio




Performance
```

Scalability is
```
Studio Studio Studio




```

better when using Scalability
distributed plugins.
```
Studio




Elasticity Studio




Fault Tolerance Studio




Simplicity, in
Overall Cost this case, leads
to affordability.




```

268  Chapter 8

<a id='p305'></a>
<!-- Página 305 -->

```
microkernel architecture




Exercise
```

Which of the following systems might be well suited for the microkernel architectural style, and why? Hint: Take into
account its superpowers, its kryptonite, and the nature of each system.


```
An online auction system where users can bid on items Well suited for microkernel
Why? Might be a fit for microkernel
Not well suited for microkernel




A large backend financial system for processing and Well suited for microkernel
settling international wire transfers overnight
Might be a fit for microkernel
Why?
Not well suited for microkernel




A company entering a new line of business that Well suited for microkernel
expects constant changes to its system Might be a fit for microkernel
Why?
Not well suited for microkernel




A small bakery that wants to start taking online orders Well suited for microkernel
Why? Might be a fit for microkernel
Not well suited for microkernel




A trouble ticket system for electronics purchased Well suited for microkernel
with a support plan, in which field technicians
Might be a fit for microkernel
come to customers to fix problems
Not well suited for microkernel
Why?




Solution on page 275

you are here 4  269
```


<a id='p306'></a>
<!-- Página 306 -->

chapter summary



Wrapping it up
Thanks to your efforts, Going Green is assessing devices quickly and accurately, and
profitability has never been better. This case shows just how useful microkernel architectures
can be. For problems that need a customizable, stable system, a microkernel is hard to beat.




Bullet Points
 The microkernel architectural style provides a structured  Monolithic plugins generally offer better performance
```
way to handle customizations via plugins. because calls take place in the same process.
```

 Microkernel architectures consist of two main parts: the  Monolithic microkernels suffer from the typical limitations
```
core and one or more plugins. of all monoliths, including limited operational capabilities
such as scalability and elasticity.
```

 The core system in a microkernel contains minimal
```
functionality and has low volatility.  Microkernels that use distributed plugins may offer better
scalability, because they use multiple processes and
```

 Architects design plugins to customize and/or add
```
offer scalable communications (events).
behaviors to a system.
 Microkernel architectures are best suited for problems
```

 Generally, plugins only communicate with the core
```
with distinct categories of volatility.
system, not with each other.
 If a microkernel’s core system changes often, its
```

 If plugins do need to communicate with each other, the
```
architects may have chosen the wrong architectural style
core must mediate the communication and handle issues
or may have partitioned the work incorrectly.
like versions and dependencies. It essentially serves as
an integration layer.  The microkernel style shows up in lots of places: IDEs,
text processing tools, build and deployment tools,
```

 Microkernel architectures can be monolithic architectures
```
integrations, translation layers, insurance applications,
or can be implemented as services in a distributed
and electronics recycling applications, just to name a few.
architecture.
```

 When built as a monolithic architecture, the core and
```
plugins must be written in the same language.
```

 Plugin calls may be synchronous (for example, using
```
REST in a distributed architecture) or asynchronous
(using threads in a monolithic architecture or messaging
in a distributed one). Whether remote calls are
synchronous or asynchronous, architects can implement
the plugins in a variety of technology stacks.




```

270  Chapter 8

<a id='p307'></a>
<!-- Página 307 -->

```
microkernel architecture

Microkernel Crossword
Ready to see how much you’ve learned about microkernel
architecture? Plug into this crossword puzzle!




```

Across Down
3. Design pattern often used to implement microkernel 1. When plugins can talk to each other, their dependencies are
architectures _____
6. With inter-plugin communication, the core serves as an 2. Example of an IDE that uses interacting plugins
integration _____ 4. _____ plugins provide better performance
9. You can add new capabilities to a system by using these 5. Number of primary component types in a microkernel
10. Microkernel architectures can _____ to include new architecture
functionalities 7. Constantly changing
11. Abbr. for a tool used to write code 8. Microkernel architectures often support several programming
13. Monolithic architectures _____ both plugins and core _____
14. Plugins are usually _____ independently from each other 12. When most monoliths load plugins
16. A microkernel is great for creating systems with _____ rules 15. A tool that applies style and syntax rules to code
and behaviors 16. Plugins make _____ to talk to the core
17. You can use plugins written in more than one tech _____ 18. What plugins are plugged into

```
Solution on page 276

you are here 4  271
```


<a id='p308'></a>
<!-- Página 308 -->

exercise solutions




```
BE the architect Solution From page 249
Architects just can’t stop analyzing
stuff. Can you determine a
few important architectural
characteristics for each of the
three services in the new Going
Green architecture?




Architectural characteristics
Public user Scalability
interfaces
Availability




Architectural characteristics
Agility (deployability, testability, etc.) Device
Maintainability assessment
```

Going Green needs to
test and deploy new
device assessments
quickly, without
breaking existing ones.
```
Architectural characteristics
Security
Recycling/
accounting Data integrity
Auditability




```

272  Chapter 8

<a id='p309'></a>
<!-- Página 309 -->

```
microkernel architecture



Exercise From page 254
Solution
The microkernel architectural style shows up in lots of places. See if you can place the specific tools and
categories below in the correct place on the spectrum, by determining how much of a microkernel each
one is. Hint: Each system’s degree of “microkern-ality” depends on how useful it is without plugins.



```

Selections toward this end rely on Selections toward this end have more
plugins for significant functionality. standalone functionality, without the
```
need for plugins.
Backend for Frontend
IDE with plugin
(BFF) design pattern
support
(not Eclipse) Device
```

Eclipse IDE Web browser
```
assessment
Mobile device
service for a
operating system
recyling business




```

less more
functional
```
Functionality/volatility of core functional



Degree of “microkern-ality”




you are here 4  273
```


<a id='p310'></a>
<!-- Página 310 -->

exercise solutions



```
Exercise From page 258
Solution
```

The assessment service team at Going Green must decide whether the microkernel’s physical architecture
should be monolithic (core and plugins in the same deployment unit) or distributed (plugins deployed
separately from the core). They need your help with the trade-off analysis. Can you list some pros and cons for
each option? Hint: Consider how each option would affect things like architectural characteristics.




```
Monolithic
Pros Cons
Performance Single deployment

Simplicity Plugin Plugin Scalability
Plugin
Core Plugin
```

Single-platform monoliths system It’s harder to scale a
are much simpler than Plugin Plugin
```
monolithic architecture.
```

distributed architectures.



```
Distributed
Pros Cons
Scalability Plugin
Plugin
Performance
```

Choice of communication Core Complexity
```
Plugin
```

styles (sync/async) Plugin
```
system
Plugin


Distributed architectures Distributed architectures
offer more choices of are more complex, as you
communication styles (and learned in Chapter 5.
trade-offs).




```

274  Chapter 8

<a id='p311'></a>
<!-- Página 311 -->

```
microkernel architecture


Exercise From page 269
Solution
```

Which of the following systems might be well suited for the microkernel architectural style, and why? Hint: Take
into account its superpowers, its kryptonite, and the nature of each system.


An online auction system where users can bid on items Well suited for microkernel
Why? This system requires high scalability but Might be a fit for microkernel
```
not a lot of customization, making it less Not well suited for microkernel
suitable for a microkernel architecture.

```

A large backend financial system for processing and Well suited for microkernel
settling international wire transfers overnight
```
Might be a fit for microkernel
Why? Rules for wire transfers are likely to
Not well suited for microkernel
differ by country of origin. A microkernel
is one way to address this problem.
(However, scalability may be a concern for
a monolithic microkernel.)
```

A company entering a new line of business that Well suited for microkernel
expects constant changes to its system Might be a fit for microkernel
Why? If the company can partition changes to
```
Not well suited for microkernel
plugins and avoid having a volatile core, a
microkernel will allow it to bring out new
features in isolation.
```

A small bakery that wants to start taking online orders Well suited for microkernel
Why? With no compelling reason for customization Might be a fit for microkernel
```
and a simple problem, a microkernel isn’t a Not well suited for microkernel
terrific fit here.

```

A trouble ticket system for electronics purchased Well suited for microkernel
with a support plan, in which field technicians
come to customers to fix problems Might be a fit for microkernel

Why? If customers, devices, or other parts Not well suited for microkernel

```
of the system require customizations, a
microkernel is one way to implement them.

you are here 4  275
```


<a id='p312'></a>
<!-- Página 312 -->

crossword solution


```
Microkernel Crossword Solution

From page 271




```

276  Chapter 8

<a id='p313'></a>
<!-- Página 313 -->

9 do it yourself
```
The TripEZ Travel App




```

Ready to extend your journey into software architecture? In this chapter,
you’re the software architect. You’ll be determining architectural characteristics, building a logical
architecture, making architectural decisions, and deciding whether to use a layered, modular, or
microkernel architecture. The exercises in this chapter will give you an end-to-end view of what a
software architect does and show you how much you’ve learned. Get ready to create an architecture
for a startup company building a travel integration convenience site. Bon voyage—we hope you have a
good trip building your architecture.




```
this is a new chapter   277
```


<a id='p314'></a>
<!-- Página 314 -->

TripEZ requirements



Making travel easier
You’ve just been hired as a software architect by an exciting new startup called
TripEZ (pronounced like “trapeze”) that wants to make travel easier, especially
for “road warriors” who travel frequently. The TripEZ app will be an online
trip management dashboard that allows travelers to see all of their existing
reservations organized by trip, through either a web browser or their mobile
devices.
```
document
TripEZ requirements
emails.
ount for travel-related
sho uld con tin ua lly poll the user’s email acc
The system s, book ing
ers (like travel agencie
st int erf ace wit h the systems of travel partn tai ls. Th ese inc lude delays,
The system mu com pa nie s) to update travel de in the app
apps, airlines, hotels, an
d car ren tal , updates must appear
, an d ga te cha ng es. To beat the competition
cancellations, updates
within five minutes. nually.
existing reservations ma
add, update, or delete
Users should be able to the trip is complete, the
items
gro up ite ms in the da shboard by trip. Once
Users should be able to oard.
removed from the dashb
should automatically be with standard social me
dia sites
to sha re the ir trip inf ormation by interfacing
Users should be able
specific people.
and by sharing it with oss all deployment pla
tforms.
ha ve the ric he st use r interface possible, acr
The system should range of metrics about
users’
e en d-o f-y ear sum ma ry reports with a wide
vid
The system should pro
travel that year. s, airline and hotel ven
dor
aly tic al da ta— suc h as travel trends, location iou s pu rpo ses .
TripEZ should gather an users’ trips for var
d can cel lat ion an d up date frequency—from
preferences, an with an important trade
show.
like to shi p Tri pE Z in six months, to coincide
The company would

Meet Travis, former pilot and
consultant to TripEZ. He has a
few more important requirements
for the system.
Pay attention, because “TripEZ must integrate seamlessly with the existing standard interface systems
these things are important. used across the travel industry, including internationally.
It must integrate with the user’s preferred travel agency (if any) to resolve
problems quickly.
Finally, users must be able to access the system at all times. Unplanned
downtime should be limited to a maximum of five minutes per month.”




```

278  Chapter 9

<a id='p315'></a>
<!-- Página 315 -->

```
do it yourself



```

TripEZ’s user workflow
Now that we have the requirements, let’s get a better understanding of them by
looking at the primary workflow for travelers using TripEZ.

```
TripEZ The TripEZ system
Confirmation emails dashboard keeps the dashboard
from travel partners up to date with
changes made by
travel partners and by
users.


```

The user grants TripEZ
```
+- An API layer handles
```

access to their email The user can make integration with the
account so it can find changes, additions, travel vendors.
travel-related information. or deletions.


```
Travel partner
integration points
Each travel
partner publishes
updates for its
information.


Sharpen your pencil
Given the requirements for TripEZ, list some challenges that you will need to address when
creating an architectural solution.




Solution on page 294

you are here 4  279
```


<a id='p316'></a>
<!-- Página 316 -->

preparing to build an architecture



Planning the architecture

```
I’ve given you
the requirements, so
what’s the big delay? Why
aren’t you developing the
system? We only have six
months!




Even though Travis is
impatient to see some
progress, don’t let that
stop you from creating a
solid, well-thought-out
architecture.

```

We have to create an architecture first.
As you’ve learned, architecture is a critical and necessary part of any
software system. Without it, the system will likely fail to achieve any of its
goals.
Before we start developing code, we have to create an architecture. This
means going back to Chapter 1, where you learned about the four
dimensions of software architecture.
Don’t worry—we’ll get the system done. But first, it’s important to know
what we’re building.




280  Chapter 9

<a id='p317'></a>
<!-- Página 317 -->

```
do it yourself



```

The architects’ roadmap
Let’s get the TripEZ architecture started. You’ll use the steps you’ve learned in
previous chapters to translate the requirements into an architecture.


```
Read the numbered
notes in counterclockwise order. 1 Start here.



Finally, y
2 5 your softou’ll diagram
```

Then you’ll need to architectuwrare 4
get logical. these dimen e using all
```
sions. Next, you’ll
document your
brilliant decision.




You now know enough to
pick a style. 3




```

This diagram will serve as your roadmap as you make your way through each of
the exercises, so get used to seeing it. The next few pages will walk you through
each of these steps.
Good luck on your journey—TripEZ is counting on you.




```
you are here 4  281
```


<a id='p318'></a>
<!-- Página 318 -->

driving characteristics



Step 1:
Identify architectural characteristics You are here.




```
“TripEZ must integrate seamlessly with the existing standard
interface systems used across the travel industry, including
internationally.
It must integrate with the user’s preferred travel agency (if any) We copied the requirements
to resolve problems quickly. here to make it easier for
Finally, users must be able to access the system at all times. you to use them to identify
Unplanned downtime should be limited to a maximum of five the driving architectural
minutes per month.” characteristics.

document
TripEZ requirements
.
for travel-related emails
uld con tin ua lly po ll the user’s email account
The system sho agencies, book ing
ace sys tem s of tra vel partners (like travel
ace with the int erf include delays,
The system must interf pa nie s) to up date travel details. These app
apps, airlines, hotels, an
d car ren tal com dates must appear in the
d ga te cha ng es. To be at the competition, up
, an
cancellations, updates
within five minutes. nually.
existing reservations ma
be ab le to add, update, or delete ms
Us ers sho uld trip is complete, the ite
up ite ms in the da shb oard by trip. Once the
gro
Users should be able to oard.
tom ati cal ly be removed from the dashb sites and
sho uld au h standard social media
sha re the ir trip inf orm ation by interfacing wit
Users should be able to
c people.
by sharing it with specifi all deployment platform
s.
ve the ric he st use r int erface possible, across
The system should ha range of metrics about
users’
e en d-o f-y ear sum ma ry reports with a wide
vid
The system should pro
travel that year. s, airline and hotel ven
dor
aly tic al da ta— suc h as travel trends, location iou s pu rpo ses .
TripEZ should gather an d up da te frequency—from use
rs’ trips for var
can cel lat ion an
preferences, and with an important trade
show.
like to shi p Tri pE Z in six months, to coincide
The company would



```

282  Chapter 9

<a id='p319'></a>
<!-- Página 319 -->

```
do it yourself




Exercise
```

In Chapter 2, we showed you how to use this template to limit the number of architectural characteristics.
Flip back to page 70 if you need a refresher on how to use it.


Top 3 Driving Characteristics Implicit Characteristics
```
feasibility (cost/time)
security

maintainability

observability
These are implied characteristics. Move
them to the Driving Characteristics
column if you think they are critical to
the success of the system.

Go back
2 if you nto Chapter
Pick the top three most important ones (in any order). refresher eed a
definition on the
common ars of these
character chitectural
istics.
Common Candidate Architectural Characteristics
performance data integrity deployability
responsiveness data consistency testability
availability adaptability configurability
fault tolerance extensibility customizability
scalability interoperability recoverability
elasticity concurrency auditability
Solution on page 293

you are here 4  283
```


<a id='p320'></a>
<!-- Página 320 -->

creating components



Step 2:
Identify logical components
Good job! Now that you’ve identified the critical architectural You are here.
characteristics for TripEZ, it’s time to apply what you’ve learned to create
logical components.
Referring to the requirements and primary workflow on the previous
pages, use the actor/action approach described in Chapter 4 to identify
actors and their actions. Then identify as many logical components as
you can on the next page.
Here’s some additional information you might find useful for this exercise:

When users sign up for TripEZ, they provide credentials to allow the different travel
services to provide up-to-date status reports on delays, cancellations, and so on.
If a travel partner’s integration point won’t supply updates within the required fiveminute window, the system should query the vendor. This allows the system
Updates, especially to the mobile application, should use as little data as to work with travel
possible to accommodate potentially spotty cell signals in remote places. partners that can’t
TripEZ can’t be held responsible for integration point availability; if the call fails, meet its agreed-upon
the system must return an error rather than failing silently (which would mislead thresholds.
the user into thinking no update was sent).




```
Sharpen your pencil
Using the actor/action approach, identify actions for each of the actors below.




Traveler System Travel partner Social media




Sign in




We did this one for you, but
the traveler might perform
other actions, too. Solution on page 294

```

284  Chapter 9

<a id='p321'></a>
<!-- Página 321 -->

```
do it yourself




Exercise
```

Using the space below, draw your logical components and their interactions.
```
Use this key fo
logical architectr your
Integration
ure.
```

Component point


```
Actor
Data Information
entity flow




Solution on page 295

you are here 4  285
```


<a id='p322'></a>
<!-- Página 322 -->

deciding on a style



Step 3:
Choose an architectural style
Leveraging what you’ve learned about the layered, modular monolith,
and microkernel architectural styles, use the next page to analyze their
pros and cons with respect to the TripEZ system. You’ll also need to refer
to the requirements, your logical architecture, and the star rating charts
```
You are here.
```

for each architectural style (we’ve added those below for you). Choose an
architectural style based on your analysis.



```
Layered Modular Monolith Microkernel
```

Architectural Characteristic Star Rating Architectural Characteristic Star Rating Architectural Characteristic Star Rating

Maintainability Studio




```
Maintainability Studio
Studio Studio




Maintainability Studio Studio Studio




```

Testability Studio
```
Studio




Testability Studio
Studio Studio




Testability Studio Studio Studio




```

Deployability Studio




```
Deployability Studio
Studio Studio




Deployability Studio Studio Studio




```

Simplicity Studio Studio Studio Studio Studio




```
Simplicity Studio Studio Studio Studio




Simplicity Studio Studio Studio




Studio




```

Evolvability Studio




```
Evolvability Studio
Studio Studio




Evolvability Studio Studio Studio




```

Performance Studio
```
Studio
Studio




Performance Studio
Studio Studio




Performance Studio Studio Studio




```

Scalability Studio




```
Scalability Studio




Scalability Studio




```

Elasticity Studio




```
Elasticity Studio




Elasticity Studio




```

Fault Tolerance Studio




```
Fault Tolerance Studio




Fault Tolerance Studio




```

Overall Cost Overall Cost Overall Cost

```
The more stars, Apologies for the tiny font, but
the better that remember—you can always flip back to
characteristic is individual chapters to see the star ratings
supported. for a particular style.
```

Here are some considerations that might help you decide which
architectural style would be better suited for TripEZ:

```
Go back to your logical architecture diagram and see if you can identify distinct
technical or business concerns. If so, a layered or modular monolith architecture might
be a good choice.
Think about different points of integration. If there are many, each with specific logic,
then a microkernel architecture might be a good fit.




```

286  Chapter 9

<a id='p323'></a>
<!-- Página 323 -->

```
do it yourself



Exercise
```

Outline the pros and cons of each architectural style to help you make a choice about which one might be most
appropriate for TripEZ.
```
Layered Monolith Architecture Analysis
Pros Cons




Modular Monolith Architecture Analysis
Pros Cons




Microkernel Architecture Analysis
Pros Cons




```

List your winning choice here:
```
Solution on page 296

you are here 4  287
```


<a id='p324'></a>
<!-- Página 324 -->

writing the ADR



Step 4:
Document your decision
Congratulations on choosing which architectural style to use for TripEZ. You are here.
Now’s your chance to explain why you made the choice you did and
document your architectural decision.
As you learned in Chapter 3, an architectural decision record, or
ADR, is an effective way to document your architectural decisions. Use
the ADR on the next page to document your architectural style decision.
Assume this is your 11th architectural decision.
```
Revisit Chapter 3 if you
need a refresher on
architectural decision records.



What should I put
in the Consequences
section of my ADR if my
architectural decision
doesn’t have any
consequences?




Every architectural decision has
consequences.
Maybe it’s about cost, or maybe it’s sacrificing a little bit of
performance to have better security. Regardless, every architectural
decision has consequences.
Think about the trade-off analysis you just did. Each one of those
trade-offs implies a consequence—something you were willing to
give up (or accept) to get something better. The Consequences
section of an ADR is a great place to document your trade-off
analysis and the corresponding consequences of your decision.
If you can’t find any consequences in your architectural decision,
keep looking, because they’re there.




```

288  Chapter 9

<a id='p325'></a>
<!-- Página 325 -->

```
do it yourself




Exercise
Architectural Decision Record

```

Title:

```
We did this
```

Status: Proposed one for you.
Context:




Decision:




```
What is the impact of your isio
```

Consequences: trade-offs are you willing todec n? What
```
accept?




Solutions on pages 297–299

you are here 4  289
```


<a id='p326'></a>
<!-- Página 326 -->

drawing your architecture diagram



Step 5:
Diagram your architecture You
```
are h
```

Now it’s time to combine all four dimensions of software architecture and ere.
show us your vision of the TripEZ architecture. In this last exercise, you’ll
diagram your architecture on the following page using the key on this page.
We didn’t give you a lot of room to diagram your architecture, and that’s
on purpose. While many architecture diagrams are very detailed, what
we’re asking you to do here is to sketch out a high-level physical view
of the user interfaces, databases, and components that make up your
architecture and how they all connect to each other.


Physical Architecture Key
```
User Interface Draw a computer screen to represent the user interface and
indicate which types of users are interacting with it. For example,
if you have separate user interfaces for desktops and mobile devices, Feel free to
show two computer screens. annotate your
diagram to clarify
points or describe
things.
Use a rounded box to represent a component. These should match
the logical components you identified in the previous exercise. Be sure
Component to give your components a meaningful and descriptive names.



Use a box to a represent a layer (if your architecture needs layers).
Layer Again, be sure to give each layer a meaningful name.


Database Draw a cylinder to represent each physical database in your solution.




Arrows represent communication to and from the user interface and
database.




```

290  Chapter 9

<a id='p327'></a>
<!-- Página 327 -->

```
do it yourself


Exercise
```

Use this space and refer to the key on the previous page to sketch your physical architecture for TripEZ.




```
Solutions on pages 300–302


you are here 4  291
```


<a id='p328'></a>
<!-- Página 328 -->

chapter summary



There are no right (or wrong) answers
Congratulations—you’ve just created an architecture!
What we’re about to show you are the exercise “solutions.” We’ve used quotes there because the
solutions we present here are just some of many possible solutions. You see, there are no right or
wrong answers in software architecture: it’s all about analyzing trade-offs and being able to justify
your decisions.
Compare your answers with the ones we’re about to show you to see how your solutions differ.
You can think about what you might have done differently, or confirm that you made what seems
to you to be the most appropriate choice. We’ll show you our TripEZ architectures for layered,
modular monolith, and microkernel architectures, since all of these styles are viable options.

Software architecture is always a learning process. Each new problem brings a whole
new set of conditions, constraints, and business and technical concerns. There is no
one-size-fits-all architecture—it’s up to you, the architect, to come up with the most
appropriate architecture for your situation.


Bullet Points
 When analyzing requirements for a business problem,  When choosing an architectural style, make sure you
```
always gather additional information from the consider the characteristics of the architectural style,
business stakeholders or project sponsor. the problem domain, and the driving architectural
characteristics you identified.
```

 While there’s no “checklist” for creating an
```
architecture, the four dimensions of software  Hybrid architectures (those combining two or more
architecture (introduced in Chapter 1) provide a good different architectural styles) are very common. If
roadmap. you use one, be sure to verify that it addresses your
critical architectural characteristics.
```

 Identifying driving architectural characteristics
```
requires you to analyze the business requirements  Architectural decision records (ADRs) are a great way
and technical constraints. to document your choices. They communicate the
reasons for your architectural decisions as well as your
```

 Implicit architectural characteristics become driving
```
trade-off analyses.
characteristics if they are critical or important to the
success of the system.  When diagramming your physical architecture, be
sure to include all the components you identified in
```

 Make sure you can tie each driving characteristic back
```
your logical architecture.
to some sort of requirement or business need.
 Remember, there are no right or wrong answers in
```

 When identifying logical components and creating
```
software architecture. As long as you can provide
a corresponding logical architecture, try to avoid
a reasonable justification for your architectural
adding physical details such as services, databases,
decisions, you’re on the right track.
queues, and user interfaces—those artifacts go into
the physical architecture.




```

292  Chapter 9

<a id='p329'></a>
<!-- Página 329 -->

```
do it yourself



Exercise From page 283
Solution
In Chapter 2, we showed you how to use this template to limit the number of architectural characteristics.
Flip back to page 70 if you need a refresher on how to use it.



```

Top 3 Driving Characteristics Implicit Characteristics
```
We only have
six
feasibility months. feasibility (cost/time)
performance security

scalability maintainability

elasticity observability
extensible/evolvable TripEZ is going to need
lots of integrations
with email providers
availability and social media sites.




Common Candidate Architectural Characteristics

performance data integrity deployability
responsiveness data consistency testability
availability adaptability configurability
fault tolerance extensibility customizability
scalability interoperability recoverability
elasticity concurrency auditability




you are here 4  293
```


<a id='p330'></a>
<!-- Página 330 -->

exercise solutions




```
From page 279
Sharpen your pencil
Solution
```

Given the requirements for TripEZ, list some challenges that you will need to address when creating an architectural
solution.
```
• Making sure that we can deliver alerts in time
• Supporting a sufficient number of users
• Finding a way to manage all the different integration points
• Integrating with social media accounts




From page 284
Sharpen your pencil
Solution
```

Using the actor/action approach, identify actions for each of the actors below.




```
System Social media
Traveler Travel partner




Sync trip information Trip segment Trip updates
Sign in
Add trip from email status
Edit trip Send alerts
```

Delete trip
Receive alerts




294  Chapter 9

<a id='p331'></a>
<!-- Página 331 -->

```
do it yourself



Exercise From page 285
Solution
```

Using the space below, draw your logical components and their interactions.

```
Integration
Component point


Actor
Data Information
entity flow

Transport includes local
```

These entities are used Transport transportation, such as rental
with all related components. cars and metro systems, but
```
Flights
not flights.
Lodging
Merge
trips

Traveler
Trip identification/
grouping
```

The email Manual Alerts
```
Social
```

gateway reads entry media
emails and
identifies
upcoming trips.
```
Email Travel API Data
gateway integrations analytics

The system will either
receive or need to Push updates.
request updates from
travel partners.
Email Travel Analytics Social
provider(s) integrations service media

The analytics service provides thirdparty support for reporting and
other business intelligence.

you are here 4  295
```


<a id='p332'></a>
<!-- Página 332 -->

exercise solutions



```
Exercise From page 287
Solution
```

Outline the pros and cons of each architectural style to help you make a choice about which one might be most
appropriate for TripEZ.
```
Layered Monolith Architecture Analysis
Pros Cons
```

A layered architecture, being a monolith, is fairly Making changes to the domain in a layered
simple, so it provides a high degree of feasibility. architecture can be cumbersome because the domain
Partitioning by technical concerns makes adding is smeared across multiple layers.
third-party integrations easier. As TripEZ grows, the system will need to be
Monolithic architectures lend themselves to better monitored continuously to ensure that it can scale.
performance, which is one of TripEZ’s priorities.

```
Modular Monolith Architecture Analysis
Pros Cons
```

A modular monolith architecture, being a monolith, Adding more integration partners may require
is fairly simple, so it provides a high degree of changes to a large number of domains.
feasibility.
```
As TripEZ grows, the system will need to be
```

Partitioning by domains fits better here, because monitored continuously to ensure that it can scale.
it eliminates the need to split domain parts out by
their technical capabilities.
Monolithic architectures lend themselves to better
performance, which is one of TripEZ’s priorities.
```
Microkernel Architecture Analysis
Pros Cons
```

A monolithic microkernel architecture is fairly simple, Any changes that affect the core must be
so it provides a high degree of feasibility. considered carefully.
A microkernel is well suited to the job, given As TripEZ grows, the system will need to be
TripEZ’s need for integration flexibility. monitored continuously to ensure that it can scale.
Monolithic microkernel architectures lend themselves
to better performance, which is one of TripEZ’s
priorities.
```
to
We’re goingADRs and
Turns out any of these would work; show you ure diagrams
```

List your winning choice here: they’d just have different trade-offs. architect ree!
```
for all th

```

296  Chapter 9

<a id='p333'></a>
<!-- Página 333 -->

```
do it yourself



Exercise From page 289
Solution

Architectural Decision Record

```

Title: 011: Use of the layered monolith architectural style for the TripEZ system

Status: Proposed

Context:
TripEZ is a fast-growing startup that requires a simple architecture to ensure feasibility. Additionally, the
company needs to ensure extensibility to accommodate multiple third-party integrations.




Decision:
We will use the layered monolith architectural style. Since TripEZ doesn’t need separate architectural
characteristics for different parts of its system, a layered monolith will suffice for the required
architectural characteristics. The main constraint is scalability.
Additionally, separating the system by technical capabilities makes extensibility easier.




Consequences:
Because we chose a monolithic architecture, scalability may eventually grow to be a concern.
Building a layered architecture makes some domain-centric changes harder because the effort will affect
multiple layers.
Architects will be able to change technical capabilities (such as adding support for new user interfaces)
easily thanks to this architectural style’s technical partitioning.




```
you are here 4  297
```


<a id='p334'></a>
<!-- Página 334 -->

exercise solutions



```
Exercise From page 289
Solution

Architectural Decision Record

```

Title: 011: Use of the modular monolith architectural style for the TripEZ system

Status: Proposed

Context:
```
TripEZ is a fast-growing startup that wants to make sure to model its architecture in a way that allows
for the easiest possible migration to a distributed architecture, while still being simple enough to build on a
tight schedule.



```

Decision:
```
We will use the modular monolith architectural style. We’ve chosen a development process that aligns well with the
domain partitioning exhibited by this architecture.
Keeping each bounded context within a component boundary helps developers understand the system’s
organization. Additionally, the system can grow in a similar way to the problem domain.
Our organization has adopted domain-driven design, and this architectural style aligns nicely with that approach.




```

Consequences:
```
Because we’ve chosen a monolithic architecture, scalability may eventually grow to be a concern.
Holistic changes to technical capabilities (such as user interfaces) are more difficult in this architecture,
since the UI is handled by a part of each bounded context.




```

298  Chapter 9

<a id='p335'></a>
<!-- Página 335 -->

```
do it yourself



Exercise From page 289
Solution

Architectural Decision Record

```

Title: 011: Use of the microkernel architectural style for the TripEZ system.
```
You may have noticed that the context
```

Status: Proposed is slightly different, even though it’s the
```
same system. This reflects differing team
```

Context: priorities.
TripEZ is essentially an integration architecture, managing similar information from a variety of integration
partners. This architecture will easily facilitate both isolation and customization for each integration point
via plugins.



Decision:
We will use the microkernel architectural style.
Time to market and extensibility are important to the company, so modeling the architecture around a
simple core with plugins for future additional integration partners will make it easy for developers to
understand and implement.
We decided that the simplicity of a monolithic system outweighed the benefits (but added complexity) of
distributed plugins.




Consequences:
In a monolithic architecture, scalability may eventually grow to be a concern. The team may consider
distributing the plugins in the future, but we decided that it would be overengineering for now.
The core can be split so that the UI is handled by another microkernel, with different plugins for different
UI types.
We should avoid adding fast-changing requirements to the core. It should be as stable as possible.



```
you are here 4  299
```


<a id='p336'></a>
<!-- Página 336 -->

exercise solutions



```
Exercise From page 291
Solution
```

Use this space and refer to the key on page 290 to sketch your physical architecture for TripEZ.


```
Layered monolithic architecture diagram




Web browser iOS Android Presentation


Identify and Merge Manual
group trips trips entry Alerts Business rules


Email Travel API Social media Integration
gateway

Flights Lodging Transport Persistence




```

300  Chapter 9

<a id='p337'></a>
<!-- Página 337 -->

```
do it yourself



Exercise From page 291
Solution
```

Use this space and refer to the key on the page 290 to sketch your physical architecture for TripEZ.


```
Modular monolithic architecture diagram
All of these domains might have
layers just like those in the
```

Remember, this is a monolith Identify and Group Trips domain.
with one backing database. We just aren’t showing them.

```
Identify and Merge Manual Email Social
group trips trips entry Alerts gateway Travel API
media




Add/edit/delete trips Handle manual entry Emails from partners Receive/poll travel APIs Update social media
Merge trips
Presentation



Alert user
Business rules

Persistence




The persistence layer
in the Manual Entry
domain will manage alle
the data entities, lik
Flights, Lodging, etc.
You could decide
a separate schematofocreate
each of the domains r
the database. in




you are here 4  301
```


<a id='p338'></a>
<!-- Página 338 -->

exercise solutions



```
Exercise From page 291
Solution
```

Use this space and refer to the key on the prior page to sketch your physical architecture for TripEZ.


```
Microkernel architecture diagram

```

The entities that appear
in the persistence layer Web iOS Android
in a layered architecture
become part of the larger
domain’s components,
including persistence logic. Identify and Merge Manual
```
group trips trips entry

Email
Email
Email Email
providers
providers gateway
Alerts
providers

Travel
Travel
Travel Social media
Social media
partners Travel API Social media Social media
sites
partner
partner site

Analytics

Core system
The core system includes
all the non-integration
parts of the system.




```

302  Chapter 9

<a id='p339'></a>
<!-- Página 339 -->

10 Bit by Bit
```
microservices architecture




```

How do you make an architecture easier to change? Business is changing
faster than ever, and software architectures need to keep up. In this chapter you’ll learn how to
create a flexible architecture that can change as your business changes, scale as your business
grows, and remain operational even when system failures occur. Intrigued? We hope so, because
in this chapter we’re going to show you microservices—an architectural style that solves all of
these problems and more. Let’s get started on our journey through microservices, bit by bit.




```
this is a new chapter   303
```


<a id='p340'></a>
<!-- Página 340 -->

monitoring system requirements



Are you feeling okay?
StayHealthy, Inc., is a company that specializes in medical
monitoring systems for patients in hospitals. Using its systems, Let’s hope you don’t get
doctors and nurses can monitor a patient’s heart rate, oxygen “sick” of the project and
levels, body temperature, blood sugar levels, and more, and even end up here.
determine whether the patient is sleeping or awake. If something
goes wrong, a doctor or nurse is notified right away.
Recent advances in medicine have given rise to a new set of needs
for medical monitoring. As a result, StayHealthy plans to leverage
newer technology to replace its current patient medical monitoring
software with a new system called MonitorMe. Guess what? You’re
the architect they chose for the new project.
Below are the requirements for the new system. You’ll need to figure
out what kind of architecture would be best suited for the job.




```
me nts document
StayHealthy MonitorMe require
ipment and sends the results to a
Healthy ’s patient monitoring equ
The system reads inputs from Stay
single monitoring screen.
professional if it detects a change
ent’s vital signs and aler t a medical
MonitorMe must analyze each pati
that reaches a preset threshold.
ments for the past five minutes. A
each vita l sign , the syst em mus t record all readings and measure
For
to review this five -minute history.
medical professional should be able be
ng goes wrong. Notifications can
they ’d like to be notified if somethi
Medical professionals select how ion.
cell phone or to a central nurses’ stat
sent to an assigned nurse or doc tor’s
that if any of these fails, the other
t different input sources. It is vital
MonitorMe reads inputs from eigh
recorded.
inputs will still be monitored and
blood pressure, oxygen level,
itorMe system include heart rate,
The vital signs monitored by the Mon p status (sleep or awake).
irati on rate , elec troc ardi ogra m (ECG), body temperature and slee
,
blood sugar, resp
) within a single hospital, meaning
signs of multiple patients (up to 500
The system can measure the vital em (inc luding the data).
its own copy of the complete syst
each physical hospital location has




```

304  Chapter 10

<a id='p341'></a>
<!-- Página 341 -->

```
microservices architecture



```

Sharpen your pencil
Based on the problem domain and requirements document on the previous page, check off the top five
architectural characteristics you think are critical to the MonitorMe architecture and indicate why you think they
are critical.

Testability (the ease and completeness of testing)
Reason:


Responsiveness (the time it takes to get a response to the medical professional)
Reason:


Deployability (the difficulty and ceremony involved in releasing changes)
Reason:


Abstraction (the level of isolation and knowledge between parts of the system)
Reason:


Scalability (the system’s ability to grow to accommodate more users or patients)
Reason:


Fault tolerance (the system’s ability to continue operating when parts of the system fail)
Reason:


Data integrity (the data is consistent and correct across the system and there is no data loss)
Reason:


Workflow (the system’s ability to handle complex business workflows)
Reason:


Concurrency (the system’s ability to process concurrent requests or operations)
Reason:

```
Solution on page 338

you are here 4  305
```


<a id='p342'></a>
<!-- Página 342 -->

microservices basics



Cubicle conversation
```
Alex




Mara




Sam
Sam: I think we can all agree that microservices is a perfect fit for the new
MonitorMe system.
Mara: Hold on—what brought you to that conclusion so quickly?
Sam: It’s obvious, isn’t it? From a domain perspective, we have independent
monitoring functions, and we need high fault tolerance and comprehensive

e this are
testability. Microservices does all this and more.
Assumptions likp. We’ll show
a common tra oid it by
Alex: Slow down a second. I’m not familiar with microservices, and I have

you how to avstanding the
no idea how it supports all the things you say it does.

better under architectural Mara: I agree with Alex. I know that we need a distributed architecture, so
microservices trade-offs. microservices might be a fit here. But let’s back up and take a closer look
style and its before we jump to any conclusions.
Sam: Okay, I see your point—what might seem obvious to me might not be
obvious to you. It’s important that you both understand what microservices
is all about, and then together we can decide if it’s the right fit for MonitorMe.
So let’s get started.




```

306  Chapter 10

<a id='p343'></a>
<!-- Página 343 -->

```
microservices architecture



```

What’s a microservice?
What’s in a name? When it comes to microservices, plenty. We’ll show you what
a microservice is and how it differs from other types of services.



```
Generally, a service is a separately deployed unit of
software that performs some business or infrastructure
process. For example, a single Monitor All Vital Signs
Monitor
All Vital service in MonitorMe might perform a lot of functions,
Signs including monitoring the patient’s heart rate, blood pressure,
temperature, and so on. This service does quite a bit, but we
still call it a service. This is quite a
because it only small service
This large service monitors all single function—performs a
of a patient’s vital signs. a “micro”-servic let’s call it
e.

```

The prefix micro- in microservice refers not to physical size, but to what the service
```
Monitor
```

does. For example, a Monitor Heart Rate service is single-purpose and does one Heart
thing really well—it monitors a heart rate. That’s the idea behind microservices. Rate
By contrast, the larger Monitor All Vital Signs service performs many vital sign
monitoring functions.



```
A microservice is a single-purpose, separately deployed
unit of software that does one thing really well.


Exercise
We’re having trouble determining what single-purpose means. Can you help us by checking off all the functions
below that you would consider single-purpose and therefore possible microservices?

Add a movie to your personal “to watch” list
Pay for an order using your credit card
Generate sales-forecasting and financial-performance reports
Submit and process a loan application to get that new car you’ve always wanted
Determining the shipping cost for an online order
Solution on page 339

you are here 4  307
```


<a id='p344'></a>
<!-- Página 344 -->

data ownership



It’s my data, not yours
Another feature that makes microservices special is that they own their own data. In other words,
each microservice is the only one that can directly access its data.

```
Same with
```

The Monitor the Monitor
Heart Rate Temperature Monitor
microservice is
```
Monitor Monitor
Heart Rate and Monitor Blood
```

the only one
```
Temperature
Blood Pressure Pressure
```

that can read microservices.
or update heart
rate data.



Why? The primary reason is to manage change control. Say you have 50 microservices, all
sharing the same data. If one microservice changes the structure of its data, which the
other 49 microservices are also accessing, all of those other services will need to change at A physical bounded context
the same time. (Is your head exploding yet?) includes the microservice
```
and all of its data.
```

Physically associating a microservice with its data is known as creating a physical
bounded context. Physical bounded contexts help manage change and coupling. If
other microservices need access to data they don’t own, they must ask the owning service
for it.
```
The Monitor Heart Rate
microservice doesn’t access the
```

The Monitor Heart Sleep Status database directly.
Rate microservice “Raju’s heart rate seems low. Is he
doesn’t have to currently awake or asleep?”
change when the
Sleep Status Monitor Sleep Changing the
database changes. Heart Rate
```
“Raju is asleep.”
Status data structure
of a table
only affects
the owning
microservice.
```

This box
represents the
physical bounded
context. In the example above, the Monitor Heart Rate microservice is asking for the data rather
```
than directly accessing the data. This way, even if the Sleep Status data structures change,
the Monitor Heart Rate microservice doesn’t have to. This is the whole idea behind
physical bounded contexts.


```

308  Chapter 10

<a id='p345'></a>
<!-- Página 345 -->

```
microservices architecture



Sharpen your pencil
We created the following services for an ecommerce site, but we need your help in figuring
out the data ownership and bounded contexts. Can you associate the database tables below
with the corresponding microservices that should own the data?
```

This is a
microservice.

```
Customer Customer Product Inventory Order
Wishlist Profile Catalog Control Shipping



This is a
database table.
We did this
Contains customer one for you. Used to
bill-to and ship-to calculate
addresses Contains all shipping costs
Shipping
Customer product details Pricing
Address
Item
Detail



Contains items a
customer may want
to buy later Holds credit card
Wishlist and payment Contains the
Items Customer
information number of items
Wallet currently in stock
Inventory




Contains customer
Contains the ID, name, email, and
warehouse in which phone number Contains all
each product is Customer shipping details
Item located Name for an order
Location Shipment
Manifest


Solution on page 340

you are here 4  309
```


<a id='p346'></a>
<!-- Página 346 -->

microservices granularity



How micro is “micro”?
Figuring out how big or small a microservice should be is hard. By now you know that a
microservice is a single-purpose service that’s separately deployed. But how do
you determine the scope of that single purpose?
As an example, let’s take a look at the MonitorMe functionality for blood pressure.
Monitoring a vital sign involves capturing the input from the medical device attached to the
patient, recording the input, analyzing the measurements, and alerting a nurse or doctor if
something is wrong. We can model this functionality in one of three ways:
• Option 1: Create a single monitoring microservice that performs all monitoring
```
and alerting functions.
“Single-purpose” here
means analyzing the
```

• Option 2: Create two separate microservices—one that captures and records vital blood pressure data
```
signs data, and one that analyzes the data and alerts staff if necessary. and alerting staff if
```

• Option 3: Create four separate microservices, each one performing a specific blood
```
something is wrong.
pressure monitoring function.

Option 1 Option 2
```

“Single-purpose”
here means
monitoring Capture Blood Analyze Blood
blood pressure, Monitor Blood Pressure Pressure

which includes Pressure
```
Capture Analyze
```

all four of
these functions. Capture
```
Record Alert
Record
The white
boxes are
Analyze
the logical “Single-purpose” here
components. only means recordin
Alert the blood pressure. g
Option 3
Capture Blood Record Blood
Pressure Pressure

Relax Capture Record

You don’t have to choose yet. At
this point, we’re only showing
you the different options you
can choose from to create a Analyze Blood Alert Staff
Pressure
microservice. Keep reading to find out how
to make the right choice for your situation. Analyze Alert



```

310  Chapter 10

<a id='p347'></a>
<!-- Página 347 -->

```
microservices architecture




Okay, so how am I supposed to
know which of those options to use
for monitoring blood pressure? Is
this another one of those “guessing
games,” like with logical components?




```

No, granularity is not a guessing game.
Granularity—the scope of what a microservice does—is an important factor
when identifying microservices. Microservices that are too fine-grained
tend to communicate more with each other to complete business functions,
leading to high levels of coupling, poor performance, and overall reliability
issues. This is commonly referred to as the Grains of Sand antipattern, in
which services are so small that they start to resemble sand on a beach.
However, microservices that are too coarse-grained are harder and more
expensive to maintain, test, and scale (which defeats the whole purpose of
using microservices).
So how do you determine the most appropriate level of granularity for
a microservice? By applying forces called granularity disintegrators and
granularity integrators. Granularity disintegrators are forces that tell
you to make your service smaller (meaning it’s doing less work), whereas
granularity integrators are forces that tell you to make the service bigger
(meaning it’s doing more work). Let’s see how these forces work.

```
Granularity Disintegrators
When should you consider making your
services smaller, with less functionality? Disintegrators
force services to
break apart.


? ? ?
```

How granular should
your service be? Integrators force
```
services to come
Granularity Integrators together.
When should you consider making your
services bigger, with more functionality?




you are here 4  311
```


<a id='p348'></a>
<!-- Página 348 -->

increasing granularity



Granularity disintegrators
Granularity disintegrators are forces that help you decide whether you
should break a service apart into several smaller ones. To show you how these
forces can influence your decision to break a service apart, we’ll take a look at
MonitorMe’s Monitor Basic Vital Signs functionality.
The three basic vital signs are blood pressure, temperature, and heart rate. Since Granularity
they’re all related, we could put them all in the same microservice or create disintegrator
separate microservices, one for each basic vital sign. forces make
```
services smaller.


Code Cohesion
Monitor Blood
volatility Pressure

Blood Pressure
```

These are the
granularity
disintegrator forces. Monitor Basic
```
Vital Signs
Monitor
Blood Pressure Temperature
```

Access
```
Temperature
```

control Temperature


```
Heart Rate

Monitor
Heart Rate

Heart Rate
Scalability
and throughput
Fault
tolerance


```

Let’s analyze each of these forces to see how it might help you decide whether to
break the monitoring functionality into separate microservices.




312  Chapter 10

<a id='p349'></a>
<!-- Página 349 -->

```
microservices architecture



```

Why should you make microservices smaller?

```
Cohesion This is also referred
A single-purpose microservice has to as “volatility-based
functionality that is highly cohesive— decomposition.”
meaning all the things it does are closely
related to each other. If the functionalities
of a microservice lack cohesion, then Code volatility
Does one part of the microservice change
it might be a good idea to break that
faster than others? Constant changes to
microservice apart.
one part of a large microservice mean you
have to test the entire microservice, including
functionalities you didn’t change. That’s a
lot of extra work.
Fault tolerance and Moving a frequently changing function
availability into its own separate microservice isolates
Do certain functions in a microservice those changes from other functions,
frequently produce fatal errors? In larger making it much easier to maintain and test
microservices, all functionalities become functionality.
unavailable when a part of the microservice
fails. However, if the faulty functionality is
in its own separate microservice, it won’t Scalability and
affect other functions. throughput
Do some parts of the microservice need
more scalability than others? If so, breaking
the service apart allows better control over
Access control which portions need to scale and which do
not.
The larger the service, the more
difficult it is to control access to For example, suppose the heart rate
sensitive information. For example, a monitoring function accepts sensor
Patient Profile microservice containing readings every second, but the temperature
functionality to access medical history monitoring function accepts sensor
might inadvertently allow unauthorized readings once every 5 minutes. Separating
staff to access this sensitive (and these monitoring functions into distinct
protected) information. services allows each one to accommodate a
Moving sensitive functionalities (like different throughput rate.

Smaller microservices start up much faster
access to medical history) into their
than larger ones, making much-needed
own microservices isolates them,
functionality available to the user sooner.
making it easier to control access to that
information.




you are here 4  313
```


<a id='p350'></a>
<!-- Página 350 -->

decreasing granularity



Granularity integrators
Granularity integrators work in the opposite direction from disintegrators—
they help you decide when to make services bigger and combine their
functionalities. We’ll use the same Monitor Basic Vital Signs microservice we
broke apart earlier to illustrate why you might want to consider combining
separate microservices into one larger microservice.


```
Database
transactions

Granularity
Monitor Blood integrator forces
Pressure make services bigger.
Blood Pressure
```

Shared
code Monitor Basic
```
Vital Signs

```

These are the granularity Monitor Blood Pressure
integrator forces. Temperature

```
Temperature Temperature


```

Data Heart Rate
dependencies
```
Monitor
Heart Rate

Heart Rate




Workflow and
choreography



```

Let’s analyze each of these forces to see how they might help you determine whether
you should put all this monitoring functionality into a single larger microservice.




314  Chapter 10

<a id='p351'></a>
<!-- Página 351 -->

```
microservices architecture



```

Why should you make microservices bigger?


```
Database transactions
When requests involve multiple
microservices, you can’t perform a single
database commit or rollback for all updates.
Since each microservice update is in its
Workflow and
own separate transaction, it must instead choreography
be committed or rolled back separately.
If a single business request requires
If data consistency and integrity separate microservices to communicate
are more important than any of the with each other, that’s coupling. Too much
disintegrator forces, then it makes sense coupling between microservices can have
to combine the functionality into a single many negative effects on the system.
microservice so that operations take place
in a single database transaction. For example, performance is affected
by network, security, and data latency.
Data dependencies are Scalability is affected because each
one of the most common microservice in the call chain must scale as
integration drivers. the other microservices scale (something
that is hard to coordinate). Fault
tolerance is affected because if one of
the microservices in the chain becomes
Data dependencies unresponsive or unavailable, the request
When you break a microservice apart, you cannot be processed.
also have to break its data apart. However,
If your workflow involves a lot of
if the data is highly coupled, it will be
coordination between your microservices
very difficult to break it apart and form
and these characteristics are important to
new physical bounded contexts.
you, consider combining them.
An example of data coupling is when
one database table refers to the key of
another database table (known as a foreign
Too much communication between
key constraint). Another example of data
microservices can make an
coupling is when an entity (like customer
architecture look like spaghetti.
information) is spread across multiple tables.
If your data is highly coupled and
functions in the microservice need to
share that data, it makes sense to keep
the microservice large and combine the
functions.




you are here 4  315
```


<a id='p352'></a>
<!-- Página 352 -->

balancing granularity



It’s all about balance
Determining the appropriate level of granularity for a
microservice isn’t easy. You have to balance the trade-offs
```
Ma ke it
```

associated with each granularity disintegrator and integrator,
and determine which trade-offs are more important. This
```
Stick
```

usually involves collaborating with your product owner or
business stakeholder, particularly if the trade-offs are significant. How small should a mi
```
croservice be?
Use this tip and you wi
ll see.
Keep them coarse-grai
You guessed it—there are trade- Then move to fine-grai
ned when you begin,
offs between these two forces, ned for the win!
which is why you have to find
the right balance between them.


Granularity disintegrators Granularity integrators
When should you consider making When should you consider making
your services smaller and separating your services bigger and combining
functionalities? functionalities?


Making our
microservices
smaller would give Making our
us better scalability, microservices bigger
which is important would give us better
to us. data integrity, which is
important to us.




Good job! The next step is figuring out
which is more important: scalability or
data integrity. As the saying goes, you
can’t have your cake and eat it too.




```

316  Chapter 10

<a id='p353'></a>
<!-- Página 353 -->

```
microservices architecture




Exercise
```

Now it’s your turn to apply granularity disintegrators and granularity integrators to decide whether to implement
the Monitor Basic Vital Signs functionality (which covers blood pressure, temperature, and heart rate) as a single
microservice or three separate services. Here is some additional information:
* A patient’s heart rate and blood pressure are the two most critical basic vital signs to monitor. If something
should go wrong with temperature monitoring, heart rate and blood pressure monitoring must continue to
work.
* All three basic vital signs share an alert functionality to notify medical professionals if something goes wrong.
* The heart rate monitoring functionality accepts sensor readings once a second, whereas the temperature and
blood pressure monitoring functions only accept sensor readings once every 5 minutes.
* Each basic vital sign’s data is recorded and stored separately, as simple JSON name/value pairs in a single
document database. For example, the heart rate readings are stored as follows:
```
{"patient_id": "123",
BPM stands for "timestamp": "10452955668",
“beats per minute.” "bpm": "64"}


Option 1: Single Option 2: Separate
microservice microservices
Both options contain all
monitoring functionalities Monitor Blood
Monitor Basic (monitor, record, analyze, Pressure
Vital Signs and alert). Blood Pressure
Blood Pressure


Temperature Monitor Monitor
Temperature Heart Rate

Heart Rate Temperature Heart Rate



```

Which of the two options would you choose, and why?




```
Solution on page 341

you are here 4  317
```


<a id='p354'></a>
<!-- Página 354 -->

shared services and libraries




```
If microservices is all
about breaking business
functionalities into separate
services, what do you do with
shared functionalities like logging,
authorization, and date utilities?




You can still share code in microservices.
Code reuse is a necessary part of software development. Without it, you
would have duplicate functionality almost everywhere in your system.
Functions like logging, metrics streaming, user authorization, and basic
utilities like transforming date formats are common in most (if not all)
systems.
In monolithic systems, this is easy—you write the common functionality
once and use it everywhere in the system, because it’s all compiled
together as one unit. But in distributed architectures like microservices, it’s
not that easy. That’s because each microservice is a separately deployed
unit of software.
So where does all that common functionality go in microservices? Usually
into either a shared library or a shared service. In the following pages, we’ll
show you the trade-offs between these choices.




```

318  Chapter 10

<a id='p355'></a>
<!-- Página 355 -->

```
microservices architecture



```

Sharing functionality
All of MonitorMe’s vital-sign monitoring microservices have shared functionality
to alert a medical professional if something is wrong with the patient. Let’s look
at the code:

```
package monitorme.common; Temperature This is Java code.
```

public class AlertNurse {
public static void sendAlert(AlertType type, String data) {
```
...
```

}
} “41 degrees Celsius”

Let’s say we create three separate microservices for monitoring blood pressure,
temperature, and heart rate. Each one needs this common alert functionality.


```
The patient’s b The patient’s heart rate
pressure is dropplood is going up—alert the
alert the nurse! ing— nurse!
Monitor Blood
Pressure
Monitor
Heart Rate
Blood Pressure
Monitor
Temperature Heart Rate

Temperature


“Replication” means that each
```

Where should the source code for the common alert functionality go? We could microservice has its own copy
replicate the code in each microservice, but that would lead to issues if anyone of the source code. This is
changed it to fix a bug or add new functionality. That leaves us with two choices only useful for truly static
for where to put the code: in a shared service or in a shared library. Let’s look at source code.
both options.

```
Sharpen your pencil
Besides alerting a medical professional, can you list other common functionalities that the
MonitorMe services might need?




Solution on page 342

you are here 4  319
```


<a id='p356'></a>
<!-- Página 356 -->

code reuse options



Code reuse with a shared service
A shared service is a separate microservice that contains a shared functionality
that other microservices can call remotely.
If we put the MonitorMe alert functionality in its own separate shared service,
each monitoring microservice will need to call that shared service if it detects
something wrong with the patient.


```
Monitor Blood This microservice contains
Pressure
shared functionality to
alert medical staff of any
Blood Pressure
anomalies. Something’s wrong with
the patient!




!
Monitor Alert
Temperature Staff

Temperature Alert




Monitor Heart Like everything in software architecture, shared services
Rate have advantages and disadvantages.

Heart Rate




Pros Cons

Changing common code in a shared service Changing a shared service is risky because it
doesn’t require changing other microservices. can immediately affect other microservices that
call it.
The shared service can be written in any
language and on any platform, which Because the shared functionality is remote,
is handy when you have microservices network latency can slow its performance.
implemented in multiple languages.
If the shared service is unavailable,
microservices that need the shared functions
those
This is another one ofs. cannot operate.
bad coupling problem The shared service must scale whenever other
microservices that call it scale.

```

320  Chapter 10

<a id='p357'></a>
<!-- Página 357 -->

```
microservices architecture



```

Code reuse with a shared library
A more common approach to shared functionality is to put it in a custom Most platf
shared library. A shared library is an independent artifact (like a JAR file programminogrms and
in Java or a DLL in C#) that is included with each microservice at compile their own sh languages have
time. This means that once the microservice is deployed, each microservice formats. ared-library file
has all of the shared functionality available to it.
Let’s see how the shared MonitorMe alerting functionality might look if we
were to use a shared library rather than a shared service.

```
This is the Alert shared
library that contains the
Monitor Blood
Pressure
shared alerting functionality. Monitor
Temperature




```

!
```
Blood Pressure




!
Temperature
Alert

Alert Alert




no longer
```

This serviclle a remote
```
Do you see how the shared alert functionality is included as part of each

```

has to ca ice to alert
```
microservice’s deployment unit? This means each microservice can simply

```

microserv . Cool!
```
use the shared code to alert a medical professional, without having to make a

```

the nurse
```
remote call to a separate service.




Pros Cons


Performance, availability, and scalability are You’ll need multiple shared libraries if your
better because the shared functionality is not microservices are written in different programming
remote. Instead, it’s bound at compile time to languages or use different platforms.
each microservice.
Managing dependencies between microservices
Changing code in a shared library is less and shared libraries can become difficult if you
risky, because shared libraries can be have a lot of microservices (which is typical in this
versioned to provide agility and backward architectural style).
compatibility.
If you change a shared functionality, you must
Because shared libraries can be versioned, retest and redeploy the microservices that use it.
you don’t have to do this all at once.

you are here 4  321
```


<a id='p358'></a>
<!-- Página 358 -->

shared services vs. shared libraries



```
Fireside Chats
Tonight’s talk: A shared service and a shared library answer the
question: “Who’s cooler?”



Shared Service Shared Library
```

Hey there, “old school.” You still around?
```
“Old school?” Let me tell you something—not only am
I still around, I’ll outlive you by a long shot.
```

Not a chance, bud. Don’t you get it? In the distributed
architecture world, I’m king. Everything is services—
including me, the shared functionality. Need to
reauthorize a user? Need to alert a nurse that the
patient is having issues? Just call me. What could be
easier?
```
Right. And when you aren’t around, what then? You
see, unlike you, I’m always around, right by each
microservice’s side.
```

Fine, you got me there. But when I have to change, I
just do it. No one else has to be involved. When you
change, every service you’re attached to has to retest
and redeploy. How disruptive you are!
```
Oh please! I can clone myself into multiple versions.
That makes me a lot safer to change. You, on the other
hand, are full of risk—you can break the entire system
when you redeploy! You really like to live dangerously,
don’t you?
```

At least I’m not a conformist. Face it—for every
programming language in your environment, you
have to replicate yourself. I, on the other hand, am
independent. I can be implemented in any language
or platform because I don’t have the same attachment
problem you have.

```
Attachment problem? Really? Listen—my attachment
to services means I’m faster, more available, more
scalable, and more reliable than you.
```

Whatever. Later, conformist—I’m gonna go find
someone to hang out with who appreciates me.
```
And... now you’re not available. See what I mean?


```

322  Chapter 10

<a id='p359'></a>
<!-- Página 359 -->

```
microservices architecture




Sharpen your pencil
```

Now that you’ve seen the two main options for sharing functionality in the microservices architectural style, it’s your
turn to decide—should the alert functionality in MonitorMe be a shared library or a shared service? Make sure you
consider external forces (like the problem domain) in addition to the pros and cons of each option, and justify your
choice.
```
Option 1: Shared service Option 2: Shared library

```

Monitor Blood
```
Monitor Blood Monitor
Pressure
Pressure Temperature

Blood Pressure Blood Pressure
Alert Temperature
Staff

Alert Alert Alert
Monitor
Temperature
Something’s wrong


!
Temperature
with the patient!

! !
```

Put your decision and reasoning here.


```
Option 1: Shared service
Option 2: Shared library
Reason:




Solution on page 343

you are here 4  323
```


<a id='p360'></a>
<!-- Página 360 -->

workflow management




```
Suppose I need
information from multiple
services. Can I do that in a
microservices architecture?




Yes, you can! This is called
workflow management.
A workflow is when fulfilling a single business request—a
task request that comes from a user interface—needs
more than one microservice. You can manage a workflow
in microservices by using either of two techniques:
orchestration or choreography. In the next couple of
pages, we’ll show you how these work and discuss their pros
and cons.




there are no
Dumb Questions
```

Q: If I make a request involving a workflow that needs multiple microservices to give me an answer, why break those
microservices apart? Wouldn’t it be better to make a single service and avoid workflows in the first place?

A: Great question. Remember the granularity disintegrators from several pages ago? Some of those factors—like scalability, fault
tolerance, code volatility, and better, more secure access control—might be important enough to warrant keeping the microservices
separate, even if it means you’ll have to add a bit of complexity later to tie those services together with a workflow.




324  Chapter 10

<a id='p361'></a>
<!-- Página 361 -->

```
microservices architecture



```

Managing workflows
A workflow is required when two or more microservices are needed to complete
a single business request. The request might be a nurse (say, Juan) asking “How is
the patient doing today?” To answer, the system must gather information about
the patient’s temperature, heart rate, and blood pressure. This means calling
multiple microservices, one for each vital sign.
```
Juan is in charge
```

However, Juan doesn’t want to make three the patient today.of
separate requests to the MonitorMe system.
He would like to make a single request to get all Let’s
the vital signs information. This means the see how the patient
three monitoring microservices need to be is doing today...
coordinated in a workflow.
Let’s look at how to make this happen in
microservices by using either orchestration Juan wants to get this data
(centralized workflow management) or with a single request.
choreography (decentralized workflow
management).




```
Juan needs information vices,
from all three microser to
Monitor Monitor Monitor Blood

which means they need
Heart Rate Temperature Pressure

Heart Rate Temperature Blood Pressure be in a workflow.




Exercise
```

Can you think of any workflows involving multiple microservices that might exist for the MonitorMe patient vital signs
monitoring system? List them in the space below. We did this one for you.
```
Get the status of a patient’s basic vital signs (temperature, blood pressure,
and heart rate).




Solution on page 344

you are here 4  325
```


<a id='p362'></a>
<!-- Página 362 -->

orchestrating workflows



Orchestration: Conducting microservices
When you go to a symphony concert, who do you see in the front,
leading all the musicians? The conductor, of course. This is a
great way to think about orchestration in microservices.
Orchestration is about coordinating all the microservices needed
for a workflow. A centralized microservice—the orchestrator—
does this, very much like a conductor coordinates all the musicians
performing in a symphony orchestra.
An orchestration service is a separate microservice that is
responsible for calling all the microservices involved in the
workflow. It also handles errors and passes consolidated data back
to the caller (usually the user interface).

```
Now there’s a This is the data, consolidated
healthy patient. Temp: 98F
BPressure: 120/80
into a single response that is
Heart Rate: 63bpm passed back to Juan.

```

This is the Usually there’s one orchest
data passed Monitor
```
per request or major wo rator
```

back to the Vital Signs rk
```
so expect a lot of these. w,flo
```

orchestrator. Orchestrator

```
Heart Rate: 63bpm
Temp: 98F BPressure: 120/80




Monitor Monitor Monitor Blood
Heart Rate Temperature Pressure

Heart Rate Temperature Blood Pressure



hestrator
Job Posting: Microservices Orc
basic vital signs.
tor to manage monitoring a patient’s
Looking for a microservices orchestra
Duties and responsibilities include:
```

That’s a lot to  Call the right microser vices in
```
the right order.
```

manage. I hope the of the workflow and what happen
```
s next.
```

job pays well.  Always know the current state
```
microser vice.
 Consolidate all the data from each
oser vices fails.
 Handle errors if any of the micr



```

326  Chapter 10

<a id='p363'></a>
<!-- Página 363 -->

```
microservices architecture




```

Like everything, orchestration has trade-offs. Let’s be positive and start with the
good.


```
The good...
Centralized workflow Error handling
Request workflows are Error handling is consolidated
centralized and well understood. into the orchestrator, so each
You only need to go to the microservice doesn’t need to
orchestrator to understand the worry about what to do if an
complete workflow. error occurs—the orchestrator
handles it.

Workflow state
Since the orchestrator always Workflow changes
knows where the request is in It’s easy to change the workflow
the workflow, if there’s a failure, because all changes occur in one
restarting the request where the central place.
Sort of like a GPS—
knows where you are. it always
workflow left off is much easier.




```

Performance Tight coupling The bad...
Orchestration tends to be slowed Because the orchestrator
by communication between the and microservices need to
orchestrator and the microservices, communicate constantly,
and because the orchestrator orchestration tends to be highly
typically saves the workflow state coupled.
to a database each time something
changes. Availability
```
If the conductor leaves the
orchestra, the concert is over.
Similarly, if the orchestration
```

Scalability microservice is unavailable, the
The central orchestrator can
```
request cannot be processed.
```

become a bottleneck as requests
```
This single point of failure is
```

increase, because every request
```
usually addressed by creating Sort of like having an
```

must go through it before reaching
```
multiple instances of the understudy conductor
```

any microservices.
```
orchestrator. backstage in case the
conductor gets sick.

you are here 4  327
```


<a id='p364'></a>
<!-- Página 364 -->

choreographing workflows



Choreography: Let’s dance
Whereas orchestras are conducted, dances are choreographed.
Rarely do you see a conductor leading a group of classical or
modern dancers—instead, the dancers learn their parts and then
communicate with each other. This is a great way to think about
choreography in microservices.
Let’s say the MonitorMe system’s blood pressure monitoring
functionality is separated into four separate microservices, which
communicate to complete the workflow of the monitoring
operation.



```
Capture Blood Record Blood
Pressure Pressure

Capture Record


This is called a If the blood pressure drops se.
sphygmomanometer—otherwise below 100/60, alert the nur
known as a blood pressure cuff.



!
Analyze Blood Alert Staff
```

Like dancers, the microservices communicate Pressure
with each other. Each performs its function,
then calls the next microservice to perform its Analyze Alert
function, until the workflow is complete.



```
Don’t lead the dancers!
When using choreography, make sure you don’t fall into the trap of turning one of the

```

Watch it!
```
microservices into an orchestrator. This is known as the Front Controller pattern. This
pattern is useful for orchestration, but not for choreography.



Capture Blood This service is now playing two
Pressure roles: blood pressure monitor and
orchestrator.

Record Blood Analyze Blood Alert Staff
Pressure Pressure



```

328  Chapter 10

<a id='p365'></a>
<!-- Página 365 -->

```
microservices architecture




```

Guess what? Choreography has trade-offs as well.



```
The good...
Responsiveness Scalability
Since there’s no central Each microservice can scale to
orchestrator to communicate with meet its throughput demands,
continually, responsiveness and independent of other microservices
performance tend to be better. in the workflow.


Loose coupling
Fast, scalable systems usually
use choreography. However, s.
Since microservices don’t depend
watch out for the trade-off
on a central orchestration service to
direct them, the system tends to be
less coupled.




```

Error handling State management The bad...
Each microservice is responsible It’s hard to know what state
for managing the error workflow if the workflow is in when using
an error occurs. This can lead to choreography, because there’s
too much communication between no central conductor controlling
services. the workflow. Usually, one of the
```
microservices (typically the first
one in the call chain) is designated
```

Recoverability the state owner, and other
When a user retries a request that microservices send it their state.
has failed or is still in progress, it’s
really hard for the system to know
where to restart. That’s because Be careful—state ma ge
no single service is responsible for can lead to the FrontnaCo ment
directing the request to a specific pattern, described in th ntroller
microservice in the workflow— it!” box on the previous e “Watch
each one only sends it to the next page.
microservice in the call chain.




```
you are here 4  329
```


<a id='p366'></a>
<!-- Página 366 -->

choreography vs. orchestration




```
Exercise
```

StayHealthy, Inc., stands behind MonitorMe and its monitoring devices and display screens. If a problem occurs with
any software or physical hardware, someone from the medical facility can go online and create a trouble ticket. A field
technician will receive the trouble ticket on their mobile phone, come to the medical facility, fix the problem, and mark
the ticket as fixed.
It’s up to you: Would you manage the microservices for the trouble ticket system workflow using orchestration or
choreography? Be sure to include the reasons for your choice.
```
These are
Choreography the steps.

Create 3 Assign Ticket to 4 Upload Ticket to Mark Ticket as
Ticket Expert App Fixed

5 6
1 2
Which workflow should The expert uses their
Juan use to submit a mobile device to mark
trouble ticket? a ticket as fixed.

1 Orchestration
Ticket
Orchestrator
3
8
2 4 5

Create Assign Ticket to Upload Ticket to Mark Ticket as
Ticket Expert App Fixed



6
7
Choreography The expert uses their
Orchestration mobile app to tell
the orchestrator the
Reason: ticket is fixed.



Solution on page 345

```

330  Chapter 10

<a id='p367'></a>
<!-- Página 367 -->

```
microservices architecture




The microservices
```

architectural style seems overly
complex to me. There are so
many hard decisions to make.
Why would I ever bother to use
```
microservices?




You’re right—the microservices
architectural style is complex.
But it’s also powerful.
Using microservices helps us address complex business
problems. Not only does this architectural style excel at
supporting operational characteristics such as scalability,
reliability, availability, and fault tolerance, but it also allows
the system to respond quickly to changes in both business
and technology (known as agility).
That said, the microservices architectural style may not be
a fit for every system. In the next few pages we’ll show you
some of the superpowers of microservices as well as its
weaknesses.




you are here 4  331
```


<a id='p368'></a>
<!-- Página 368 -->

microservices superpowers



Microservices architecture superpowers
Every architectural style has its superpowers. Here are some
reasons to use the microservices architectural style.



```
lity
Maintainabiare single-purpose
Because microservices
e
and separately deployed, you can mor
cod e that need s to chan ge
easily locate
for a particular function.



Testability
A microservice’s testing scope is muc
h smaller than
that of a larger monolithic application
or a system with
large services. This limited scope mak
es it easier to
fully test a microservice’s functionality
.


Evolvability
It’s relatively easy to add
Deployability functionality to a microservices
Because microservices are deployed architecture: you create a new
as separate units of software, there service, test it, and deploy
are fewer risks involved with it alongside other existing
releasing a microservice than with microservices in your system.
large monolithic systems. You can
also deploy microservices more
frequently—sometimes daily.


```

Scalability Fault tolerance
```
If a particular microservice fails, it doesn’t bring
```

Microservices scale at a function level
```
down the entire system—only that function.
```

rather than a system level. This means that
```
Users can continue to use other functions.
```

you scale only the functionalities you need
to meet increased user load and demand,
saving resources and lowering costs.




332  Chapter 10

<a id='p369'></a>
<!-- Página 369 -->

```
microservices architecture



Microservices architecture kryptonite
Are there reasons not to use the microservices architectural style? You
bet there are. Just like kryptonite diminishes a superhero’s powers,
certain business and architectural characteristics diminish the case for
using microservices. Watch out for them!




Complexity
Microservices is one of the most complex architectural styles. It
involves so many hard decisions—about granularity, transactions,
workflow, contracts, shared code, communication protocols,
team topologies, and deployment strategies, just to name a few.




Complex workflows
```

Performance Workflows occur when you need to call
The more microservices communicate
```
multiple microservices for a single
```

with each other, the worse their
```
business request. If the functionality
```

performance will be. They may have
```
to of your system is too tightly coupled,
```

wait for the network, undergo addition
```
al breaking it into separately deployed
```

security checks, and make extra data
```
base services will only result in a big ball of
```

calls.
```
distributed mud. Yuck!

Remember—a
physical bounded
context includes
```

Monolithic databases the microservice as Technically
Each microservice must own its own data well as all of its
and form a physical bounded context.
```
data.
partitioned teams
```

If your data can’t be broken apart for Does your organization consist of siloed
whatever reason, stay away from this teams of user interface developers, backend
architectural style. developers, and database people? If so,
```
microservices won’t work for you (a reflection
of Conway’s Law). Microservices architecture
requires cross-functional teams. Each team
owns its own group of microservices, all the way
from the user interface to the database.




you are here 4  333
```


<a id='p370'></a>
<!-- Página 370 -->

strengths and weaknesses



Microservices star ratings
Below is a useful chart for understanding what microservices architecture is
good at and what it’s not so good at. One star means that the architectural
characteristic is not well supported; five stars means the characteristic is very
well supported. Just like movie reviews.



```
Architectural Characteristic Star Rating

Maintainability Studio
Studio Studio Studio Studio




```

These characteristics
contribute to Testability
agility—the ability
```
Studio Studio Studio Studio
Studio




```

to respond quickly to Deployability
change. Microservices are
```
Studio Studio Studio Studio
Studio




```


## HARD.

```
Simplicity Studio




Evolvability Studio
Studio Studio Studio Studio




We can scale a Performance
microservices at
Studio
Studio




function level. Too much tween
Scalability communication be s
Studio Studio Studio Studio
Studio




microservices slow
Elasticity Studio
Studio Studio Studio




down requ ests .

Fault Tolerance Studio
Studio Studio Studio Studio




Overall Cost $$$$$
As you can see, the microservices architectural style is pretty good in terms
due
Overall cost is hi,ghbreaking of agility (maintainability, testability, and deployability) and operational
to licensing feestimizing characteristics. However, it’s not so great when it comes to performance,
apart data, op lines, and simplicity, and cost.
deployment pipeams. You might be wondering about the low performance rating. This is because of
reorganizing te latency as services communicate with each other. This latency takes on three
forms: network latency (the time it takes the request to get to the service),
security latency (the time it takes to reauthorize a user, for example), and data
latency (since each microservice makes its own database calls).




```

334  Chapter 10

<a id='p371'></a>
<!-- Página 371 -->

```
microservices architecture




Exercise
```

Which of the following systems might be well suited for the microservices architectural style, and why? Hint: Take into
account microservices’ superpowers, its kryptonite, and the problem domain.


```
An online auction system where users can bid on items Well suited for microservices
Why? Might be a fit for microservices
Not well suited for microservices




A large backend financial system for processing and Well suited for microservices
settling international wire transfers overnight Might be a fit for microservices
Why?
Not well suited for microservices




A company entering a new line of business that Well suited for microservices
expects constant changes to its system Might be a fit for microservices
Why? Not well suited for microservices




A small bakery that wants to start taking online orders Well suited for microservices
Why? Might be a fit for microservices
Not well suited for microservices




A trouble ticket system for electronics purchased Well suited for microservices
with a support plan, in which field technicians Might be a fit for microservices
come to customers to fix problems
Not well suited for microservices
Why?




Solution on page 346

you are here 4  335
```


<a id='p372'></a>
<!-- Página 372 -->

chapter summary



Wrapping it up
Congratulations! The MonitorMe system is up and running, and it’s a success. It’s all
thanks to your understanding of microservices and what types of systems this approach
is good for.
You’ve learned that while microservices can be a complicated architectural style, it also
has superpowers that can help solve complex business problems (like the MonitorMe
system we’ve been working on). Let’s close this chapter by reviewing some key points
about microservices.

Bullet Points
 A microservice is a single-purpose, separately  A shared library is an independent artifact (like a
```
deployed unit of software that does one thing really JAR or DLL file) that is bound to a microservice at
well. compile time. Shared libraries offer better operational
characteristics, like scalability, performance, and
```

 A physical bounded context means that a microservice
```
fault tolerance, but make it harder to manage
owns its own data and is the only microservice that
dependencies and control changes.
can access that data. If a microservice needs data that
is owned by another microservice, it must ask for it.  A workflow is when multiple microservices are needed
for a single business request or business process.
```

 The granularity of a microservice is a measure of its
```
size—not physically, but the scope of what it does.  Workflows that use orchestration require a central
orchestrator microservice, which works like a
```

 Forces that guide you to make your microservices
```
conductor in a symphony orchestra.
smaller are called granularity disintegrators.
 In workflows that use choreography, the services talk
```

 Forces that guide you to make your microservices
```
to each other, like dancers performing together.
bigger are called granularity integrators.
 Scalability, fault tolerance, evolvability, and overall
```

 Balance granularity disintegrators and integrators to
```
agility (maintainability, testability, and deployability)
find the most appropriate level of granularity for a
are the superpowers of the microservices
microservice.
architectural style.
```

 You can make microservices coarse-grained to start
```
 Performance, complexity, cost, monolithic databases
with, then finer-grained as you learn more about
that can’t be broken apart, and high semantic
them.
coupling are kryptonite to microservices.
```

 Two techniques for sharing functionality in
```
 Microservices should be as independent as possible;
microservices are shared services and shared libraries.
too much communication between them will degrade
```

 A shared service is a microservice that contains a the benefits of this architectural style.
```
functionality shared by multiple microservices. It’s
deployed separately and each microservice calls it
remotely. Shared services are more agile overall and
are good for heterogeneous environments. However,
they are not good for scalability, fault tolerance, or
performance.




```

336  Chapter 10

<a id='p373'></a>
<!-- Página 373 -->

```
microservices architecture



Microservices Crossword
Ready to have some fun and test your knowledge about
what you’ve learned?




```

Across Down
1. Microservices make it easier for a system to do this 1. _____ handling is part of an orchestrator’s job
5. When you make a service smaller, you make it more _____ 2. Kind of component found within a microservice
7. Each microservice _____ its own data 3. Kind of force that pushes you to make a microservice bigger
11. Workflow where microservices communicate with each other 4. Watch out for the _____ Controller pattern
14. A _____service does one thing really well 6. Each microservice is a separately deployed _____ of software
15. Microservices is this type of architecture 8. Code resource that’s often shared
17. _____ tolerance keeps a problem from bringing down the 9. A context that restricts data access
whole system 10. Workflow where one microservice rules all the others
18. Microservices are _____-purpose 12. Type of bounded context or architecture diagram
19. When you need more than one microservice to do the job, it’s 13. Good security includes restricting _____ to data
a _____ 16. A bad design pattern is an _____pattern

```
Solution on page 347

you are here 4  337
```


<a id='p374'></a>
<!-- Página 374 -->

exercise solutions




```
From page 305
Sharpen your pencil
Solution
```

Based on the problem domain and requirements document on page 304, check off the top five architectural
characteristics you think are critical to the MonitorMe architecture and indicate why you think they are critical.

```
Testability (the ease of and completeness of testing)
Reason: Because this is a critical medical system, we can’t let bugs get into the system (completeness)


Responsiveness (the time it takes to get a response to the medical professional)
Reason: A patient’s life could depend on how fast the medical professional is notified of a problem


Deployability (the frequency and ceremony involved with releasing changes)
Reason: Not critical—there are no requirements stating there will be many changes in the system


Abstraction (the level of isolation and knowledge between parts of the system)
Reason: Not critical—there are no requirements regarding abstraction


Scalability (the system’s ability to grow to accommodate more users or patients)
Reason: Not critical—the system is scoped to a single hospital only (hospital beds are the limiting factor)


Fault tolerance (the system’s ability to continue operating when parts of the system fail)
Reason: One vital sign monitoring failure can’t stop the other vital signs functions from monitoring the patient


Data integrity (the data is consistent and correct across the system and there is no data loss)
Reason: The data about a patient’s health must be as accurate as possible


Workflow (the system’s ability to handle complex business workflows)
Reason: Not critical—each vital sign is monitored separately and no complex workflows are required


Concurrency (the system’s ability to process concurrent requests or operations)
Reason: The system must be able to monitor many different vital signs at the exact same time



```

338  Chapter 10

<a id='p375'></a>
<!-- Página 375 -->

```
microservices architecture



Exercise From page 307
Solution
```

We’re having trouble determining what single-purpose means. Can you help us by checking off all the functions
below that you would consider single-purpose and therefore possible microservices?

```
Add a movie to your personal “to watch” list
These are complex processes with
Pay for an order using your credit card lots of different functions.
Generate sales forecasting and financial performance reports
Submit and process a loan application to get that new car you’ve always wanted
Determining the shipping cost for an online order




you are here 4  339
```


<a id='p376'></a>
<!-- Página 376 -->

exercise solutions


```
From page 309

Sharpen your pencil
Solution
```

We created the following services for an ecommerce site, but we need your help in figuring out the data ownership
and bounded contexts. Can you associate the database tables below with the corresponding microservices that should
own the data?



```
Customer Customer Product Inventory Order
Wishlist Profile Catalog Control Shipping



This is a
database table.
We did this
Contains customer one for you. Used to
bill-to and ship-to calculate
addresses Contains all shipping costs
Shipping
Customer product details. Pricing
Address
Item
Detail



Contains items a
customer may want
to buy later Holds credit card
Wishlist and payment Contains the
Items Customer
information number of items
Wallet currently in stock
Inventory




Contains customer
Contains the ID, name, email, and
warehouse in which phone number Contains all
each product is Customer shipping details
Item located Name for an order
Location Shipment
Manifest




```

340  Chapter 10

<a id='p377'></a>
<!-- Página 377 -->

```
microservices architecture


Exercise From page 317
Solution
```

Now it’s your turn to apply granularity disintegrators and granularity integrators to decide whether to implement
the Monitor Basic Vital Signs functionality (which covers blood pressure, temperature, and heart rate) as a single
microservice or three separate services. Here is some additional information:
* A patient’s heart rate and blood pressure are the two most critical basic vital signs to monitor. If something
should go wrong with temperature monitoring, heart rate and blood pressure monitoring must continue to work.
* All three basic vital signs share an alert functionality to notify medical professionals if something goes wrong.
* The heart rate monitoring functionality accepts sensor readings once a second, whereas the temperature and
blood pressure monitoring functions only accept sensor readings once every 5 minutes.
Each basic vital sign’s data is recorded and stored separately, as simple JSON name/value pairs in a single document
database. For example, the heart rate readings are stored as follows:

```
{"patient_id": "123",
BPM stands for "timestamp": "10452955668",
beats per minute. "bpm": "64"}


Option 1: Single Option 2: Separate
microservice microservices
Both options contain all
monitoring functionalities Monitor Blood
Monitor Basic (monitor, record, analyze, Pressure
Vital Signs and alert). Blood Pressure
Blood Pressure


Temperature Monitor Monitor
Temperature Heart Rate

Heart Rate Temperature Heart Rate

Here’s our take.

```

Which of these two options would you choose, and why? Option 2: Separate microservices.
Having separate services provides better fault tolerance in case one of the monitoring functions causes the
service to go down. Also, data is recorded and stored separately, which works well with physical bounded
contexts in separate databases to provide better fault tolerance. Finally, each separate service can scale
as needed based on the varying input rates (once a second for heart rate, every 5 minutes for others).



```
you are here 4  341
```


<a id='p378'></a>
<!-- Página 378 -->

exercise solutions




```
Sharpen your pencil From page 319

Solution
Besides alerting a medical professional, can you list other common functionalities that the
MonitorMe services might need?
Observability—streaming service response times, errors, uptime, and other metrics and measurements
Logging—reporting on errors and other service functionality alerts
Auditing—recording when an alert was sent and which medical professional received it
Security—restricting access to a monitoring service to authorized medical professionals only




```

342  Chapter 10

<a id='p379'></a>
<!-- Página 379 -->

```
microservices architecture




From page 323
Sharpen your pencil
Solution
```

Now that you’ve seen the two main options for sharing functionality in the microservices architectural style, it’s your
turn to decide—should the alert functionality in MonitorMe be a shared library or a shared service? Make sure you
consider external forces (like the problem domain) in addition to the pros and cons of each option, and justify your
choice.
```
Option 1: Shared service Option 2: Shared library

```

Monitor Blood
```
Monitor Blood Monitor
Pressure
Pressure Temperature

```

Blood Pressure Blood Pressure
```
Alert Temperature
Staff

Alert Alert Alert
Monitor
Temperature
Something’s wrong


!
Temperature
with the patient!



```

This is our decision and reasoning.
```
! !
Option 1: Shared service
Option 2: Shared library
Reason: We chose option 2 (shared library) because it provides:
-better performance (the medical professional will be alerted faster)
-better reliability and fault tolerance (if the Alert Staff shared service went down, the
system couldn’t alert the medical professional)
-better concurrency (if multiple problems occur at the same time)




you are here 4  343
```


<a id='p380'></a>
<!-- Página 380 -->

exercise solutions


```
Exercise From page 325
Solution
```

Can you think of any workflows involving multiple microservices that might exist for the MonitorMe patient vital signs
monitoring system? Here are our ideas.

Get the status of a patient’s basic vital signs (temperature, blood pressure,
and heart rate)
Find out which vital signs are being monitored for a given patient (requires queries to multiple monitoring
services)
Register a new patient to be monitored—lots of different information is gathered, like name, identity,
demographics, medical history, and so on, all of which could be separate microservices




344  Chapter 10

<a id='p381'></a>
<!-- Página 381 -->

```
microservices architecture


Exercise From page 330
Solution
```

StayHealthy, Inc., stands behind MonitorMe and its monitoring devices and display screens. If a problem occurs with
any software or physical hardware, someone from the medical facility can go online and create a trouble ticket. A field
technician will receive the trouble ticket on their mobile phone, come to the medical facility, fix the problem, and mark
the ticket as fixed.
It’s up to you: would you manage the microservices for the trouble ticket system workflow using orchestration or
choreography? Be sure to include the reasons for your choice.
```
These are
Choreography the steps.

Create 3 Assign Ticket to 4 Upload Ticket to Mark Ticket as
Ticket Expert App Fixed

5 6
1 2
Which workflow should The expert uses their
Juan use to submit a mobile device to mark
trouble ticket? a ticket as fixed.

1 Orchestration
Ticket
Orchestrator
3
8
2 4 5

Create Assign Ticket to Upload Ticket to Mark Ticket as
Ticket Expert App Fixed



6
7
The expert uses their
Choreography mobile app to tell
the orchestrator the
Orchestration ticket is fixed.
Reason: Choreography is a simpler solution with less overall service
communication. Also, this is not a complicated workflow with lots
of error conditions, so using orchestration seems like overkill.


you are here 4  345
```


<a id='p382'></a>
<!-- Página 382 -->

exercise solutions


```
Exercise From page 335
Solution
```

Which of the following systems might be well suited for the microservices architectural style, and why? Hint: Take into
account microservices’ superpowers, its kryptonite, and the problem domain. Here are our answers.



```
An online auction system where users can bid on items Well suited for microservices
Why? High scalability and elasticity needs; high Might be a fit for microservices
concurrency; independent functions Not well suited for microservices




A large backend financial system for processing and Well suited for microservices
settling international wire transfers overnight Might be a fit for microservices
Why? Microservices’ superpowers aren’t needed
Not well suited for microservices
in this kind of complex system


A company entering a new line of business that Well suited for microservices
expects constant changes to its system Might be a fit for microservices
Why? High agility and evolvability mean Not well suited for microservices
microservices could fit, but we need more info


A small bakery that wants to start taking online orders Well suited for microservices
Why? The high cost and complexity of microservices Might be a fit for microservices
would be too much for a small bakery Not well suited for microservices




A trouble ticket system for electronics purchased Well suited for microservices
with a support plan, in which field technicians Might be a fit for microservices
come to customers to fix problems
Not well suited for microservices
Why? Independent functions; good scalability
and elasticity; simple workflows




```

346  Chapter 10

<a id='p383'></a>
<!-- Página 383 -->

```
microservices architecture



```

Microservices Crossword Solution

```
From page 337




you are here 4  347
```


<a id='p384'></a>
<!-- Página 384 -->


<a id='p385'></a>
<!-- Página 385 -->

11 event-driven architecture
```
Asynchronous Adventures




```

What if your architecture could do lots of things at the same time? As
businesses grow and become more successful, they need to be able to handle more and more users,
without slowing down or crashing systems. In this chapter, you’ll learn how to design high-performance
systems that can scale as a business grows. Get ready for event-driven architecture, a highly popular
distributed architectural style. It’s very fast, highly scalable, and easy to extend—but it’s also quite
complex. You’ll be learning about lots of new concepts in this chapter, including things like events,
messages, and asynchronous communication, so you can create an architecture that can do many
things at once. Fasten your seatbelt, and let’s go on an asynchronous adventure through event-driven
architecture.




```
this is a new chapter   349
```


<a id='p386'></a>
<!-- Página 386 -->

diner workflows



Too slow
Imagine going to your favorite diner to order their famous grilled cheese
sandwich, crispy fries, and a chocolate milkshake. Sounds easy, right? But what
if the person taking your order had to make all of those things one at a time,
without any help? Not only would everything take longer, but the diner wouldn’t
be able to serve as many customers. Let’s visualize that workflow:




```
1. Take the next customer’s lunch order (1 minute)

2. Accept payment from the customer (1 minute)

3. Cook the grilled cheese sandwich (4 minutes)

4. Cook the french fries (5 minutes)
This custom
5. Make the chocolate milkshake (4 minutes) isn’t happy wer
her cold lunc ith
6. Plate the food and serve the customer h.


Each order takes 15 minutes,
meaning the diner can only
serve four customers during
the lunch-hour rush.


```

This is no way to run a diner! Let’s see if we can make things go a little faster so
they can serve more customers.




```
Brain
Power Write your
Pretend you are a customer of this diner. How would you suggest they speed things up? ideas here.




```

350  Chapter 11

<a id='p387'></a>
<!-- Página 387 -->

```
event-driven architecture



```

Speeding things up
If the diner hires three more workers (one to make the sandwiches, one to cook the
french fries, and one to make milkshakes) and they prepare all parts of the meal at
once, completing orders will take half as long. That effectively doubles the number
of customers the diner can serve during the lunch hour.


```
1. Take the next customer’s lunch order (1 minute)
2. Accept payment from the customer (1 minute)
Now each order only takes 7 minutes,
meaning the diner can serve more
customers.
3. Cook the grilled cheese sandwich (4 minutes)
4. Cook the french fries (5 minutes) These are done at the same
5. Make the chocolate milkshake (4 minutes) time, only taking 5 minut
because of the fries. es
6. Plate the food and serve the customer
Note: we’ll be referring
to event-driven
```

Doing all three activities at the same time significantly reduces customers’ wait time architecture as EDA
(we’ll call that responsiveness). Because meals can be made faster, the server taking going forward, because
orders can now handle more customers (we’ll call that scalability). we’re cool like that (and,
This is the fundamental concept behind event-driven architecture (EDA)— thankfully, we don’t get
breaking up processing into separate services, with each of those services performing its paid by the word).
```
function at the same time by responding to an event (something that just happened).
```

In EDA, services communicate asynchronously through an event channel, meaning
they don’t wait for responses from other services to complete their work. Don’t worry—
```
we’ll cover all
of these terms.
This is
```

This is a service the event. Grilled
that triggers Cheese
an event. Lunch Order
```
Placed Ser vice
Lunch These are services
Order that respond to
Ser vice an event.
This is the event channel French
where the event is sent. Fries
Ser vice


```

We know this is a lot to take in at once, so we’ll take it step by step. But before we jump
in, let us introduce you to Der Nile, a large German online-ordering company that is
having growing pains and needs your help.

```
you are here 4  351
```


<a id='p388'></a>
<!-- Página 388 -->

online ordering requirements



Der Nile flows faster than ever
Der Nile is Germany’s largest online retailer, selling everything from
diapers to hair-growth supplements.
Business is booming—so much, as a matter of fact, that the company’s
online ordering system is stressed to the breaking point. Der Nile’s
customers demand fast systems and quick order fulfillment, and the
current system simply can’t handle the volume of orders coming in.
Processing orders takes too long, and fulfillment times are increasing.
Der Nile would like to create a new ordering system from scratch to
handle this growth—and needs your help in designing it.
Here is the basic flow of the legacy online-ordering system currently in
place:

```
Der Nile wants to make
online shopping fun.

This is Ana—she’s going to
be our Der Nile customer.
The customer Validate the order Charge the Adjust the If the stock
submits an order and generate customer’s current gets too low,
and waits order ID credit card inventory order more


Email the Send the order
customer the to the fulfillment
order ID department to pack


Email the customer
that the order is ready The order is packed
to ship and ready to ship




Email the customer
Ship the order to
when the order is
the customer
delivered


Mark the order
as complete


```

352  Chapter 11

<a id='p389'></a>
<!-- Página 389 -->

```
event-driven architecture




Exercise
```

As the architect, how can you modify the current workflow (shown on the previous page) to speed things up a bit?
Draw your ideas for a new workflow in the space below. Hint: What can you do at the same time?
```
Start here.

The customer
submits an order
and waits




Solution on page 391

you are here 4  353
```


<a id='p390'></a>
<!-- Página 390 -->

understanding events



What is an event?
Back in the late 1950s, a journalist asked Prime Minister Harold Macmillan
of the United Kingdom what troubled him the most. “Events, my dear boy,
events,” was his famous reply. Events may have troubled Harold Macmillan, but
they can be a lot of help to us in solving complex business problems.
```
Publishing this bo
```

An event is something that happens, especially something of importance. Things an important evenokt was
like the World Cup, musical concerts, big promotions at work, weddings, and the authors. for
birthday celebrations are all important events.
In software systems, certain user actions trigger events—things that happen, like
placing a bid for an item up for auction, filing an insurance claim, or making a
purchase.

```
These are the things the system
This is the This is an event that does as a response to the event.
user action. is generated from the
user action.
```

Submit an Charge customer ’s credit
online order card

```
Order
Adjust current inventor y
Submit ted


Prepare the order

Friendly reminder:
```

Events are a way for a service to let the rest of the system EDA is event-driven
know that something important has just happened. In EDA, architecture.
events are the means of passing information to other services.
An event usually contains data, like all the details of an Order Order
online order. On occasion, it might only have key information Submit ted Submit ted
(like the order ID). In the latter case, services that must do Order ID: 123 Order ID: 123
something when they receive the event will have go to a data Customer ID: 99876
store to get additional information about it. This event Date Placed: 22 May
```
only passes Item List: [Items]
The data inside an Street: 123 Main St
along the City: Anytown
event is referred to order ID. ...
as its payload.
This event passes
along all the
information about
the order that was
just submitted.

```

354  Chapter 11

<a id='p391'></a>
<!-- Página 391 -->

```
event-driven architecture




Hold on—in Chapter 3 you talked
about using messages to pass
information from one service to
another. Now you’re talking about
using events. Is an event is the same
thing as a message?




No, an event is not the same thing as
a message. Although they both deliver information to other
parts of the system, there are some important differences between
them.
```

This is often An event is used to broadcast some action that a service just
referred to as performed to other services in the system. For example, a service
“fire-and-forget.” might tell the rest of the system: A customer just placed an order. A service
```
sending an event never waits for a response. The service generally
has no knowledge about what other services (if any) are listening for
that event, or what they’ll do with that information if they respond to
More on this it.
soon.
A message, on the other hand, is a command, such as Apply the
payment for this order, or a request, like Give me shipping options for this
customer. Because messages are only meant to reach one other service,
the other services in the system are unaware of the message. Services
sometimes stop and wait for a response (for instance, if they are
sending a request for information). Other times, the service might just
issue a command and trust that the receiving service will do its job.
Turn the page to see more differences between an event and a
message.




you are here 4  355
```


<a id='p392'></a>
<!-- Página 392 -->

distinguishing events from messages



Events versus messages
Here are two really important differences between events and messages:

1. Events are broadcast to other ser vices using topics, where as messages
are sent to a single ser vice using queues.


```
Ser vice
Both these
Ser vice Event services receive
Topic the same event.
Ser vice
You learned
about these in
```


## Chapter 3.

```
This is the only
Ser vice Message Ser vice service that
Queue receives the
message.


```

2. Events always broadcast some thing that has alre ady happened,
where as message s reque st some thing that needs to be done.

```
These are events. These are messages.

Order
Order Order
Apply
Placement Placement
Ser vice Placed Payment
Ser vice


Payment Payment Packing Ship
Ser vice Rejected Ser vice Order


Shipping Order Shipping Notif y
Ser vice Shipped Ser vice Customer

Events are always Messages are always
stated in past tense. stated as commands.

```

356  Chapter 11

<a id='p393'></a>
<!-- Página 393 -->

```
event-driven architecture



Sharpen your pencil
```

It’s time to test your knowledge about events and messages. For each of the quotes below, mark whether it is more
likely an event or a message, and indicate why.

```
“Adventurous Air flight 12, turn lef t, he ading 230 degrees.”
Event Message
Reason:


“In other ne ws, a winter storm f ront has just moved into the are a.”

Event Message
Reason:


“Ok ay, class, turn to page 42 in your workbooks.” Be careful—this one’s
tricky!
Event Message
Reason:


“Hello, ever yone! Sorr y I’m late.”

Event Message
Reason:


“Oh no! I just missed my train!“

Event Message
Reason:



“Excuse me, sir—do you have the time?“
Event Message
Reason:



Solution on page 392

you are here 4  357
```


<a id='p394'></a>
<!-- Página 394 -->

event types



Initiating and deri ved events
Events that originate from a customer or end user are called initiating events.
These are a special type of event that kicks off a business process.
Once a service responds to an initiating event, it might in turn broadcast what
it did to the rest of the system, within the scope of that initiating event. These
events are called derived events because they are internal events generated in
response to the initiating event.

```
This is the initiating
event that kicks
everything off.


Order Order
```

Customer Submit ted Placement
submits an Ser vice These are derived
```
order events triggered
by the Order
Submitted
Order
initiating event.
Placed

Email
Credit Card
Services can respond to Notification
Expired
an event and in turn Ser vice
trigger more events. These are all the things that
Payment can possibly happen in the
Ser vice Payment service.
Payment Order
Fulfillment
Applied
Ser vice




```

Did you notice that the Payment service generates two different derived events?
This is typical in EDA. Anything a service generates or causes to happen can be
a derived event.




358  Chapter 11

<a id='p395'></a>
<!-- Página 395 -->

```
event-driven architecture



Exercise
```

Based on the Credit Card Charged initiating event and the corresponding processing below, can you identify what the
derived events should be for each service? Think of as many possible outcomes as you can.

```
Customer makes This is the
a credit card initiating event
purchase
Credit Card
Charged




Fraud Credit
De tection Limit
Ser vice Ser vice

Check for Use as many of these Verif y credit
f raud as you need. You may limit These are the
not need all of them. derived events.
Fill in what you think
the derived events
might be for each of
these services.




Solution on page 393

you are here 4  359
```


<a id='p396'></a>
<!-- Página 396 -->

architectural extensibility



Is anyone listening?
When you post something on social media, you often get a reaction—someone
liking or commenting on your post. But how many times have you posted
something only to get no reaction? Maybe you wondered: Did anyone see my
post? Did anyone care?
```
Extensibility is one
```

In EDA, any action a service performs should trigger a derived event. However, of the archite
```
ctural
```

there is a chance that no one cares about certain events. So why publish those characteristic
```
s you learned
```

events? Because this provides architectural extensibility—the ability to about in Chapter 2.
extend the system to add new functionality.
Let’s say customers in the Der Nile online ordering system get notified
when an order is shipped and also when it has been delivered. The Email
Notification service handles this by sending the customer an email. That event
in turn triggers a Customer Notified derived event.


```
Services can respond to
more than one event. My order is
on its way!
Order Shipped
Event
Email
Notification
Ser vice
```

Order Deli vered
```
Event

No services are Customer
interested in this Notified Event
derived event, so it
just disappears. It’s a
very lonely event.
```

Now let’s suppose Der Nile wants to do some analytics to learn what times
of the day the system sends the most customer notification emails. Since
the Customer Notified derived event is already being published, you can simply
create a new Notification Analytics service and tell it to listen for that event. This new service ca
You don’t need to modify any other parts of the system. simply subscribe to n
```
the existing Custo
This event is no Notified event. mer
longer lonely. Notification
Customer
Notified Event Analytics
Ser vice


```

360  Chapter 11

<a id='p397'></a>
<!-- Página 397 -->

```
event-driven architecture



```

Asynchronous communication

```
I thought you said
this architecture
was really fast. How
is this any faster than
microservices?


Event-driven architecture is fast
because it uses mostly asynchronous
(or “async” for short) communication.
You’re probably most familiar with communication styles such as REST or
HTTP, particularly when you need to call an API or another service. These
are forms of synchronous communication. With synchronous (or “sync”)
communication, when a service sends information, it must sit and wait for
a response from the receiving service before doing anything else (even if it’s
just acknowledging receipt of the information). This slows systems down and
makes them less scalable. It’s like calling a friend­—you have to wait for your
phone to make a connection to your friend’s phone, let it ring, and wait for
your friend to answer before you can talk.


Having to wait
for a response
Asynchronous communication is a

is really slow.
fancy way of saying that services don’t
wait for a response or acknowledgment
from other services when sending them
information. This creates systems that are
highly decoupled and very fast. It’s one
of the unique features of event-driven
architecture. It’s like sending your friend
a text—you can do other things while you
wait for their response.




Not having to wait
means you can go
do other things.




you are here 4  361
```


<a id='p398'></a>
<!-- Página 398 -->

synchronous vs. asynchronous




```
Fireside Chats
Tonight’s talk: Asynchronous and synchronous communication
debate: Who’s more useful?



Asynchronous Communication Synchronous Communication
```

Well, it’s about time you showed up.
```
Sorry I’m late. I can’t seem to multitask, so everything I
do takes such a long time.

```

Yeah, I’ve noticed. You’re as slow as a herd of snails
traveling through peanut butter.
```
Now, wait just one minute!

```

Wait? You want me to wait? That’s your whole
problem—you’re always waiting around for answers.
No one has to wait when I’m around. And that makes
me fast—really fast.
```
That may be so, but your problem is that you never
know what’s going on. You ask others to do things, but
you never find out whether those things actually got
done or not.
```

I trust others to get the job done, unlike you. You need
verification for everything, all the time.
```
Yeah, right. Tell me: when an error occurs downstream,
how do you deal with it?

```

I don’t. I can’t be responsible for everyone, you
know. I let others deal with their own issues.
```
And what if you need information from someone else
before you can finish your work? What do you do then?

```

Oh, I’m sorry—did you say something? I wasn’t
listening.
```
That’s exactly my point! You never listen to anyone
else. I may be slow, but at least I pay attention to what’s
going on and communicate with others.
```

Sorry—I wasn’t paying attention. What was that?

```
Sigh...


```

362  Chapter 11

<a id='p399'></a>
<!-- Página 399 -->

```
event-driven architecture



```

Fire-and-forge t
Asynchronous communication is one of the foundations of event-driven
architecture. When a service broadcasts information to other services, it doesn’t
wait for a response, nor does it care whether the services are available or not. This
is known as fire-and-forget communication—the event is sent (that’s the fire part),
and the service moves on to do other things (that’s the forget part). Architects usually
use a dotted line to represent async communication between services.



```
Dotted lines The Payment service
signify asynchronous eventually receives th
Order communication. event and responds e
Payment when it’s ready.
Placement Ser vice
Ser vice

The Order Placement service
doesn’t wait for a response
from the Payment service
once it sends an event..
Synchronous communication, on the other hand, means that the sending
service must stop and wait for a response from the service it’s calling before
continuing its work. This means that the service being called must be available
to respond, or an error occurs. Architects usually represent synchronous
communication using a solid line.



Solid lines indicate
synchronous
Order communication.
Payment
Placement Stop
Ser vice
Ser vice


The Order Placement service must stop and The Payment service must
wait for a response from the Payment service be available when the Order
before it can complete its work. Placement service sends it
information.

Event-driven architecture relies on
asynchronous communication when sending and receiving
events.

you are here 4  363
```


<a id='p400'></a>
<!-- Página 400 -->

sync or async?



```
Sharpen your pencil
For each of these tasks, would you use asynchronous or synchronous communication?


Gi ve me the shipping options for this order.

Asynchronous Synchronous Either one would work


Apply payment for this order and le t me know if the payment goes through.
Asynchronous Synchronous Either one would work


Fulfill this order for me by picking the items of f the shelf and packing them in a box.
Asynchronous Synchronous Either one would work


Gi ve me the current status of this order.
Asynchronous Synchronous Either one would work


Our inventor y of this item is ge t ting low—ple ase order more stock .
Asynchronous Synchronous Either one would work


Tell the customer that their order has been shipped and is on its way.
Asynchronous Synchronous Either one would work



Update the customer ’s profile picture.
Asynchronous Synchronous Either one would work


Post a customer ’s revie w on the product page.
Asynchronous Synchronous Either one would work



Solution on page 394

```

364  Chapter 11

<a id='p401'></a>
<!-- Página 401 -->

```
event-driven architecture



```

Asynchronous for the win
Communicating between services asynchronously has a lot of advantages. The
first is better responsiveness—in async, it takes less time to complete a request.
Suppose a customer places an online order in Der Nile. It takes 600
milliseconds (ms), or just over half a second, for the Order Placement service to
validate and place the order, and 1,200 ms for the Payment service to apply the
payment. With async, the customer would wait 600 ms to get a response. With
sync, however, they would have to wait 1,800 ms (just shy of 2 seconds). That’s
a big difference in response times.

```
Wow, that
was fast—only half
a second to place an Although this step
order! occurs, the user
doesn’t have to
wait for it.
4
1 Order
Placement Payment
Ser vice
Ser vice 3
2
600 ms Async means the Order 1,200 ms
Placement service doesn’t
need to wait for a response.
That took
a long time. Two
seconds to place an
order is too slow for
me.
Sync means the
Order Placement
service must stop
and wait for the
Payment service to 3
finish its work.
1 2
Order
Stop Payment
Placement
Ser vice
5 Ser vice
600 ms 4 1,200 ms


you are here 4  365
```


<a id='p402'></a>
<!-- Página 402 -->

sync and async trade-offs



Asynchronous for the win (continued)
The other big advantage of async is availability. Let’s see what happens with
async and sync if the Payment service is unavailable or becomes unresponsive.



```
Nice! I’ve
placed my The Payment
order. service is down
and unavailable.

Async
1 Order
communication
Payment
Placement
Ser vice
Ser vice 3
2
The Order Placement service doesn’t
care whether the Payment service is
available or not.



What do you mean, “Error, try
again”? All I want to do is place
my order!


3
Sync
1 2 communication
Order Stop Payment
Placement The Order Placement Ser vice
ERROR! 3 Ser vice service can’t
function properly
when the Payment
service is unavailable.

Remember the
Law—everythingFirst
```

Have we convinced you that asynchronous communication is great?
```
software architecin
```

Let’s take a look at its trade-offs next.
```
a trade-off. ture is


```

366  Chapter 11

<a id='p403'></a>
<!-- Página 403 -->

```
event-driven architecture



```

Synchronous for the win
The main disadvantage of async communication is error handling. With sync
communication, if there’s a problem with the payment method, the customer knows
right away and has a chance to fix it and resubmit the order. However, with async,
the customer thinks everything is fine because the system hasn’t told them otherwise—
but the Order Placement service can’t process the order until the customer corrects
the payment problem. This makes error handling much more complex.


```
Oops. Let me
try a different
credit card.




Synchronous 3
1 2 communication
Order Payment
Stop
Placement Ser vice
ERROR—Credit Ser vice
Card Expired
4
5 ERROR—Credit
Card Expired




My card is
expired? Why couldn’t you
have told me that when I
placed the order?
4
Asynchronous
1 Order
communication ERROR—
Payment Credit Card
Placement Ser vice
Ser vice 3 Expired
2
5
“Ple ase update your credit card This is getting
information so we can process your order.” complicated.
6 Email
Notification
Ser vice



you are here 4  367
```


<a id='p404'></a>
<!-- Página 404 -->

async error handling



```
Sharpen your pencil
```

Now’s your chance to test what you’ve learned so far about event-driven architecture, events, and asynchronous
processing. Der Nile’s inventory occasionally gets out of sync, as shown below. When this happens, the order cannot
be fulfilled and goes into a back-order state. Der Nile never makes a customer pay for items that are back-ordered,
and the customer can choose whether to wait or cancel the order.
As the architect for Der Nile, what additional events and services would you create to address this situation?




```
1
Order 3 Order Payment
Placement Placed Ser vice
Ser vice
2
4
Payment
Applied Oh dear!
What would
you do now?
5
Order ERROR—No Stock
Fulfillment on Hand, Cannot
Ser vice Fulfill Order


Draw your
solution in
this space.




Solution on page 395

```

368  Chapter 11

<a id='p405'></a>
<!-- Página 405 -->

```
event-driven architecture



```

Database topologies


```
Hang on. All you’ve talked about so
far are events and services. Data matters
too, ya know. When are you going to
start talking about databases in eventdriven architecture?




We’re glad you brought that up.
Data can be a complex topic in EDA. Because EDA
is so asynchronous, services are highly decoupled from
one another. However, if all the services share a single
database, then they end up being highly coupled to
the database. On the other hand, if each service
owns its own data, like with microservices (discussed
in the previous chapter), then services become
highly coupled to each other because they need to
synchronously ask each other for the data. In either
case, data forms a coupling point—something we try
to avoid in EDA.
In the next couple of pages we’re going to show you
various ways for dealing with databases in EDA:
monolithic databases, domain-partitioned
databases, and the database-per-service pattern.
We’ll talk about their trade-offs to help you decide
which one is most appropriate for your situation.




you are here 4  369
```


<a id='p406'></a>
<!-- Página 406 -->

monolithic topology



Monolithic database
In the monolithic database topology, all services share a single database.
The main advantage is that when services need data they don’t own,
they can go directly to the database. This means they don’t have to make
synchronous calls to other services to get data. For example, if the Order
Placement service needs the current inventory and shipping options for a
customer’s order, it can simply query that information from the database.
```
Services are
decoupled from each
other when using a
monolithic database...

Order Order Payment Fulfillment
Payment
Placement Placed Applied Ser vice
Ser vice
```

Order Placemenrr t Ser vice
```
cu ent
```

can get the
inventory an d
shipping optionsthe Order
directly from t’s Fulfilled
database. Tha.
easy and fast Inventor y
```
Ser vice

Shipping
Ser vice




A single, monolithic
database to serve
all services
...but the single database
```

However, this decoupling comes with a steep price: managing database cause issues with scalabil can
changes. Because all services share the same database, when you make fault tolerance, and chanity,
a change to the structure of one table, it’s difficult to identify all the control. That’s bad. ge
services that change will affect. Testing and releasing becomes a tricky
game—one you will all too often lose. This leads to brittle systems that
are difficult to maintain.
What’s more, the shared database becomes a single point of failure, and
one that may not be able to scale as the system grows.



370  Chapter 11

<a id='p407'></a>
<!-- Página 407 -->

```
event-driven architecture



```

Monolithic database topology scorecard
Here’s a scorecard for the monolithic database topology. Monolithic databases are not
```
necessarily good or bad—it all
depends on what’s important to you.

Monolithic Database Topology Scorecard


Service coupling: Low High
GOOD Services are highly decoupled because they don’t need to
synchronously communicate with each other to get data.


Performance: Low High
GOOD Data retrieval is fast because services are accessing the database
directly, not through synchronous remote calls to other services.


Simplicity: Low High
GOOD The monolithic database is a simple topology. Complex joins and
queries are done in the database rather than in the services.


Ease of change: Low High
BAD Changing the structure of a database table can affect lots of
distributed services, making systems hard to test.


Fault tolerance: Low High
BAD If the single monolithic database goes down, the entire system goes
down, impacting overall fault tolerance and availability.


Scalability: Low High
BAD It’s harder to scale and provide elasticity because the database must
scale along with the services, and because services could run out of
connections to the database.



you are here 4  371
```


<a id='p408'></a>
<!-- Página 408 -->

domain-partitioned topology



Domain-partitioned database s
With domain-partitioned databases, each domain in the system has its own
database. This means any service that belongs to a particular domain will share
the database for that domain. For example, the Order Placement, Payment, and
Inventory services are all part of the Order Placement domain, so they all share the See Chapter 10 for
same physical database. review of the physicaal
However, since each domain forms its own broad physical bounded context, a bounded context.
service in one domain can’t directly access a database to get data from another
domain. This means it must make a synchronous call to another service to get The Order Placement
the data—and now these services are coupled. service must synchronously
```
call the Shipping service
```

Dotted lines to get the shipping
represent separate options.
domains.
```
Order Order
Placement Fulfillment

Order Order Payment
Payment Fulfillment
Placement Placed Applied
Ser vice Ser vice
Ser vice



Order
Fulfilled
Inventor y
Ser vice

Shipping
Ser vice




All services in the
Order Placement
domain can access This topology is a well-balanced, middle-of-the-road solution within
their domain’s event-driven architecture.
database directly.


```

372  Chapter 11

<a id='p409'></a>
<!-- Página 409 -->

```
event-driven architecture



```

Domain-partitioned database s topology scorecard
Here’s a scorecard for the domain-partitioned databases topology. The domain-partitioned databases
```
topology provides a good balance.


Domain-Partitioned Databases Topology Scorecard


Service coupling: Low High
BAD While services within a domain are still highly decoupled because
of shared data, services must make synchronous calls to other
services to get data from outside their domain.

Performance: Low High

GOOD Data retrieval is fast for services within a domain because they are
accessing the database directly. However, performance becomes
slower when services access data synchronously outside their domain.

Simplicity: Low High
GOOD Since most data is naturally partitioned by domain, this topology is not
overly complex (but it’s still not as simple as a monolithic topology).


Ease of change: Low High
BAD Changing the structure of a database table only affects services within
the domain, limiting the number of services impacted.


Fault tolerance: Low High

BAD Database failures only affect services within the domain, making this
topology a little more fault tolerant than the monolithic topology.


Scalability: Low High

BAD While still a con, scalability is a little better here than in the monolithic
topology. Databases only need to scale at the domain level, rather
than across the entire system.




you are here 4  373
```


<a id='p410'></a>
<!-- Página 410 -->

database-per-service topology



Database-per-ser vice
Remember the database-per-service pattern from Chapter 10? It isn’t just for
microservices—you can use it for EDA as well.
The database-per-service pattern is just what it sounds like. Every service has We hope you have
its own database, forming an even tighter physical bounded context than with plenty of money!
the domain-partitioned topology. Here, making database changes is a breeze, This can get
because the only service affected is the one that owns the data (that is, does expensive.
writes to the database). You get better fault tolerance and better scalability, too.
What’s not to like?
Unfortunately, plenty. You see, whenever services need additional data they
don’t have, they have to ask for that data from the service that owns it using
synchronous calls. That results in a lot of coupling and communication between
services, not to mention much slower performance.


```
The Order Placement
service must
synchronously call the
Wow—that’s a Shipping service to get
lot of service the shipping options.
coupling!


Order
Placement Order Payment Payment Fulfillment
Ser vice Placed Ser vice Applied Ser vice



Order
Fulfilled
Inventor y
Ser vice

Shipping
The Order Placement Ser vice
service must synchronously Each service and data
call the Inventory service combination forms its ow
to get the current physical bounded context,n
inventory. just like in microservices
.



```

374  Chapter 11

<a id='p411'></a>
<!-- Página 411 -->

```
event-driven architecture



```

Database-per-ser vice topology scorecard
```
This topology is the exact opposite of the monolith
```

Here’s a scorecard for the database-per-service topology.
```
topology, from a pros-and-cons perspective. ic



Database-Per-Service Topology Scorecard

Service coupling: Low High
BAD Since services only have access to data they own, they must make
synchronous calls to other services to get additional data. This highly
couples services in a highly decoupled architecture. That’s bad.

Performance: Low High

BAD Because services must make synchronous calls to retrieve other data,
performance becomes much slower than in the other topologies.


Simplicity: Low High
BAD Breaking data apart into small physical bounded contexts is very
hard, due to coupling between data tables and artifacts (such as
foreign keys, triggers, views, and stored procedures).

Ease of change: Low High
GOOD Changing the structure of a database table only affects a single
service within the physical bounded context, making database
changes much easier than in other topologies.

Fault tolerance: Low High
GOOD Database failures only affect the owning service, making this the
most fault tolerant of the three topologies.


Scalability: Low High
GOOD Databases scale at the service level, making this a great topology for
high scalability and elasticity needs.




you are here 4  375
```


<a id='p412'></a>
<!-- Página 412 -->

choosing a topology




```
Exercise
```

For each of these business needs, select which topologies you would consider. You can select more than one
topology.

We e xpect any where be t ween 20 and 300,000 customers to be on the system at once.
```
Monolithic Database Domain-Partitioned Database-Per-Service
Databases

```

The system must be as fast as possible.
```
Monolithic Database Domain-Partitioned Database-Per-Service
Databases
```

This medical monitoring system can never comple tely fail—parts of it must always stay
running.
```
Monolithic Database Domain-Partitioned Database-Per-Service
Databases

```

We’re anticipating changing the database a lot in this ne w line of business.
```
Monolithic Database Domain-Partitioned Database-Per-Service
Databases

```

We have to ge t the ne w system up and running as soon as possible.
```
Monolithic Database Domain-Partitioned Database-Per-Service
Databases

Our data model is e xtremely large and comple x, with lots of interrelated data.
Monolithic Database Domain-Partitioned Database-Per-Service
Databases




Solution on page 396




```

376  Chapter 11

<a id='p413'></a>
<!-- Página 413 -->

```
event-driven architecture




Event-driven architecture using
the database-per-service topology
looks a lot like microservices to me.
What’s the difference?




Even though they may appear
simliar, EDA and microservices
are very different.
We’re glad you noticed some similarities between
the two architectural styles. Both are distributed
architectures good for scalability, agility, elasticity, and
fault tolerance.
Over the next few pages, we’ll show you some important
differences. But before we move on, how about trying
the short exercise below to see if you can spot any
yourself ?




If you don’t know, that’s
okay—keep reading!


```

Sharpen your pencil
```
List any differences you can think of between event-driven architecture and microservices.




Solution on page 397

you are here 4  377
```


<a id='p414'></a>
<!-- Página 414 -->

architecture differences countdown



EDA versus microser vices
Welcome to the EDA versus microservices Top Six Differences countdown!
Over the next few pages, we’re going to count down six important differences
between these architectural styles, starting with number 6. Ready? Let’s go! It’s time for the Head
```
First differences
```

Number 6: Performance countdown!
The first difference in our countdown, at number 6, is
performance.
In their book Fundamentals of Software Architecture (O’Reilly), two
of your authors created star ratings for each architectural
style. We gave microservices only two stars out of five for
performance, but we gave EDA five stars. Why? Event-Driven Architecture
Well, EDA combines asynchronous processing with the ability
to do multiple things at once, creating very fast systems.
Microservices, however, because of their bounded contexts
and fine-grained nature, frequently need to communicate
synchronously. This creates a lot of latency, which slows the
system down considerably.
```
Microservices Architecture



```

Number 5: Physical bounded contexts
Coming in at number 5 in our countdown is physical bounded contexts.
Microservices won’t work without these.
In EDA, however, while a physical bounded context is nice to have, it’s certainly
not foundational (or even required). Because data sharing is pretty typical in EDA,
this architecture doesn’t restrict data ownership as strictly as microservices does.
```
These services and their
data are each in a physical
bounded context.
There are no
physical bounded
contexts here.




Event-Driven Architecture Microservices Architecture

```

378  Chapter 11

<a id='p415'></a>
<!-- Página 415 -->

```
event-driven architecture




You can refres
```

Number 4: Data granularity your memory ofh
```
restriction and wthis
```

Another constraint with microservices that doesn’t exist in EDA is data it exists by goin hy
granularity. back to Chapterg
```
10.
```

By definition, a microservices architecture requires each service to own its own
data. This means you have to break apart your data into fine-grained databases
or database schemas—collections of tables that a service owns (writes to).
But in EDA, you can choose a single monolithic database, domain-partitioned
databases, or the database-per-service pattern.




```
Event-Driven Architecture Microservices Architecture



```

Number 3: Service granularity
Number 3 in our differences countdown has to do with service granularity.
Recall from Chapter 10 that a microservice is a single-purpose service that does one
thing really well. As a result, microservices tend to be fine-grained.
EDA has no such restrictions. Services in an event-driven architecture (formally
called event processors) can be whatever size they need to be—fine-grained, These services are all required
coarse-grained, it doesn’t matter. to be single-purpose—hence
```
the name “micro.”
These services
can be any size.
Event
Microser vice
```

Processor
```
Event
Microser vice
Processor Event
Microser vice
Event Processor
Processor


Event-Driven Architecture Microservices Architecture

you are here 4  379
```


<a id='p416'></a>
<!-- Página 416 -->

architecture differences countdown




Number 2: Event versus request processing
We’re almost there. Coming in at number 2 is another fundamental difference:
event processing versus request processing. Event-driven architecture is
built on event processing—responding to something that has happened, and in
turn triggering more events. Microservices architecture, on the other hand, is
built on request processing—responding to something that needs to happen, like a This is something
command or a request, and processing that request. that needs to happen.


```
Order Order Order Apply
Placement Placed Placement Payment
Ser vice Ser vice
This is
Event-Driven Architecture something that Microservices Architecture
has already
happened.



```

Number 1: Communication style
And finally, coming in at number 1 is the most fundamental difference
between EDA and microservices: communication style. EDA typically uses
asynchronous communication between services, whereas microservices typically
rely on synchronous communication using REST. EDA can occasionally use In microservices, communication
synchronous calls for things like retrieving data it doesn’t have access to, and is usually done using REST,
microservices can use asynchronous communication when commands don’t which needs a response to
require a response. But those are exceptions rather than the rule. continue processing.

```
Async Sync
Order Order
Payment Payment
Placement Placement
Ser vice Ser vice
Ser vice Ser vice

Event-Driven Architecture Microservices Architecture




```

380  Chapter 11

<a id='p417'></a>
<!-- Página 417 -->

```
event-driven architecture


Who Does What
```

Oh dear! We tried to organize these facts , but got them all mixed up. Can you help us figure out which
statements are about EDA and which are about microservices? Careful—some facts apply to both.




```
I require a bounded context.


I can use the database-per-service pattern.

Event-Driven I create systems that can scale.
Architecture

I mostly use synchronous communication.


I create high-performance systems.


I save you money because I don’t cost a lot.
We did this
one for you. I rely mainly on asynchronous communication.
Microservices
Architecture I communicate to services using events.


I’m really good at fault tolerance.


I can use a monolithic database.




Solution on page 398

you are here 4  381
```


<a id='p418'></a>
<!-- Página 418 -->

hybrid architectures



Hybrids: Event-dri ven microser vice s
Even with all the differences between EDA and microservices, there’s no reason
you can’t combine them. Doing this creates a hybrid architecture called eventdriven microservices.
You might have observed that the EDA database-per-service pattern for Der Nile A hybrid architecture
looks a lot like microservices. However, just using the database-per-service pattern combines multiple
doesn’t make it event-driven microservices. To see what we mean, take a look at architectural styles.
this EDA.

```
That’s a big service.
We’ll call it Papa This event processor
Bear... ...and this one’s fulfills the order, then
Mama Bear... ships and tracks it.


Order
Order Order Fulfillment
Order
Submission Submit ted Ser vice
Shipped
Ser vice ...and this one is
Baby Bear.

Email
This event processor accepter,s Ser vice
the order from the custom
validates it, applies payment All this event
for the order, and adjusts processor does
the inventory. is email the
customer when
the order is
shipped.


Sharpen your pencil
```

The above architecture is an acceptable and well-formed EDA, but not a well-formed microservices architecture. Two
fundamental principles are missing that would make it event-driven microservices. Can you list what those two missing
things are?

1. 2.


```
Solution on page 399

```

382  Chapter 11

<a id='p419'></a>
<!-- Página 419 -->

```
event-driven architecture




```

To make this architecture an event-driven microservices hybrid, we have to
apply two very important principles of microservices: single-purpose services
and physical bounded contexts.
The Order Submission service has to accept an order, validate it, apply the
payment, and adjust the inventory. It’s certainly not a single-purpose service.
That’s perfectly acceptable in EDA, but not in microservices. The same is true
of the Order Fulfillment service. To make this an event-driven microservices This is a physical bounded
architecture, we’d have to split these services into separate single-purpose services, context, meaning no
each triggering its own events. one else can access the
```
payment data directly.



Order Order
Placement Placed Payment Payment
Ser vice Ser vice Applied

Order
Submission
Ser vice




Inventor y Inventor y
Ser vice Updated



These services are now
microservices that use events,
creating an event-driven
microservices architecture.

You might have noticed on the previous page that the Email service is accessing the
Order Submission database directly. In microservices, this isn’t allowed because of the
physical bounded context. In the new hybrid architecture, to retrieve the order data, the
Email service needs to call the Order Submission service (now the Order Placement
service, since we broke that service up). The implementation of tight physical bounded
contexts isolates data access to the owning service.


you are here 4  383
```


<a id='p420'></a>
<!-- Página 420 -->

EDA superpowers



Event-dri ven architecture superpowers
It’s time to check out the superpowers of the EDA style.




```
Maintainability
d,
Services in EDA are highly decouple
making them fairly inde pen den t and
therefore easier to maintain.




```

Performance
Because EDA mostly uses
asynchronous communication and
can multitask, it’s very fast.
```
Evolvability
EDA services always trigger
derived events, onto which we
can easily add functionality. This
makes EDA highly evolvable.




Scalability
Event-driven architectures are highly
scalable because of asynchronous
processing and service decoupling. Each
Fault tolerance
service can scale independently of others, Because services are highly decoupled in EDA,
with the event channels acting as pressure if one service goes down, it doesn’t bring down
release valves if bottlenecks occur. other services in the workflow.




```

384  Chapter 11

<a id='p421'></a>
<!-- Página 421 -->

```
event-driven architecture



Event-dri ven architecture kr yptonite
Kryptonite diminishes a superhero’s powers, just like these system
features and characteristics diminish the power of EDA. Watch out
for them!




Complexity
EDA is highly complex because it typically uses asynchronous
communication and parallel event processing, and because of its
varied database topologies and their trade-offs.




```

Testability Synchronous calls
```
If you have lots of synchronous calls
```

It’s really hard to test asynchronous between services and workflows that
processing and parallel tasks, making require synchronously dependent
testability a weakness in EDA. services, EDA is not for you.




We know you need a Databases
database—what we’re Regardless of the database topology you
saying here is that choose, services are coupled: either to the
databases can couple database or to each other. There are not
an otherwise highly a lot of good trade-offs here.
decoupled system.




```
you are here 4  385
```


<a id='p422'></a>
<!-- Página 422 -->

strengths and weaknesses



Event-dri ven architecture star ratings
Below is a useful chart for better understanding what EDA is good at and what
it’s not so good at. One star means that the architectural characteristic is not
well supported; five stars means it’s very well supported.

```
Just like movie reviews.


Architectural Characteristic Star Rating

```

While it’s easy Maintainability Studio
```
Studio Studio Studio




```

to find where Things like error
to change code, Testability Studio
```
Studio




handling and
```

testing and asynchronous
deployment are Deployability communication
```
make EDA
Studio Studio




```

risky and hard.
```
Studio




complex.
Simplicity Studio




Evolvability Studio
Studio Studio Studio Studio




```

Less service
coupling means ty Performance
better scalabili
```
Studio Studio Studio Studio
Studio




and elasticity. Finally, an
Scalability Studio
Studio Studio Studio Studio




architectural
style that
Elasticity Studio
Studio Studio
Studio




performs well!

Fault Tolerance Studio
Studio Studio Studio Studio




Overall Cost $ $ $
```

Because most things are
asynchronous and decoupled,
fault tolerance is really high.
```
EDA is great for operational characteristics like performance, scalability,
elasticity, evolvability, and fault tolerance, but struggles when it comes to
simplicity and testing. Asynchronous communication is hard to test, and it’s also
hard to verify that a change in one service or event hasn’t affected other services.




```

386  Chapter 11

<a id='p423'></a>
<!-- Página 423 -->

```
event-driven architecture




Exercise
```

Which of the following systems might be well suited for the event-driven architectural style, and why? Hint: Think
about EDA’s superpowers, its kryptonite, and the problem domain.
```
An online auction system where users can bid on
items Well suited for event-driven architecture
Why? Might be a fit for event-driven architecture
Not well suited for event-driven architecture




A large backend financial system for processing and
Well suited for event-driven architecture
se t tling international wire transfers overnight
Why? Might be a fit for event-driven architecture
Not well suited for event-driven architecture



A company entering a ne w line of business that
e xpects constant changes to its system Well suited for event-driven architecture
Why? Might be a fit for event-driven architecture
Not well suited for event-driven architecture


A small baker y that wants to start taking online
orders Well suited for event-driven architecture
Why? Might be a fit for event-driven architecture
Not well suited for event-driven architecture



A social media site where users can post and respond
to comments Well suited for event-driven architecture
Why? Might be a fit for event-driven architecture
Not well suited for event-driven architecture




Solution on page 400

you are here 4  387
```


<a id='p424'></a>
<!-- Página 424 -->

chapter summary



Put ting it all toge ther
Now, the part you’ve been waiting for—the complete picture of the Der
Nile online ordering system using event-driven architecture. Since there are
lots of database topologies to choose from, we’ll focus on the core parts of Lots of errors can occur in
the system: event processors (services) and events. this architecture, which would
```
generate corresponding error
events. We’re not showing
What those events here—only the
a great online “happy path” events.
ordering system!




Order
Order Payment Payment Fulfillment
Placement
Placed Ser vice Applied Ser vice
Ser vice



Order
Inventor y Fulfilled
Ser vice



Shipping
Warehouse Inventor y Ser vice
Ser vice Adjusted



Order
Stock Shipped
Replenished



Email
Notification
Ser vice



Customer
Notified



```

388  Chapter 11

<a id='p425'></a>
<!-- Página 425 -->

```
event-driven architecture



```

Wrapping up
Well done! Thanks to your diligent work and EDA knowledge, Der Nile is scaling up and
performing to meet its high customer demand, with room to grow even more. Let’s close
this chapter by reviewing some key points about event-driven architecture.



Bullet Points
 An event is something that happens in the  Event-driven architecture and microservices are very
```
system. Events are the fundamental way services different architectural styles:
communicate with each other in EDA.
 EDA relies mostly on asynchronous
```

 Events are not the same thing as messages—events communication between services, whereas
```
broadcast some action a service just performed to microservices typically rely on synchronous
other services in the system, whereas messages are communication using REST.
commands or requests directed to a single service.
 EDA is built on event processing—processing
```

 An initiating event originates from a customer or end things that have already happened. A
```
user and kicks off a business process. microservices architecture is built on request
processing— processing a command or request
```

 A derived event is generated by a service in response
```
about something that needs to happen.
to an initiating event.
 Microservices are fine-grained and single-
```

 Any action a service performs should trigger a derived
```
purpose, whereas services in EDA can be any
event to provide architectural extensibility—the ability
size.
to extend the system to add new functionality.
 Microservices requires each service to own its
```

 EDA is fast because it generally uses asynchronous
```
own data, whereas in EDA services can (and
(async) communication—services don’t wait for a
usually do) share data.
response or acknowledgment from other services
when sending them information.  You can combine microservices and EDA to create a
hybrid architecture called event-driven microservices.
```

 Asynchronous communication is sometimes called
```
fire-and-forget.  EDA is very complex because it uses asynchronous
communication and parallel event processing, and
```

 Architects usually use a dotted line to represent async
```
has varied database topologies.
communication between services and a solid line to
represent sync communication.  It’s really hard to test asynchronous processing and
parallel tasks, making testability a weakness in EDA.
```

 Unlike microservices, event-driven architecture can
```
use a variety of database topologies:  Derived events provide hooks to add functionality,
making EDA highly evolvable.
 With the monolithic database topology, all
services share a single database.  EDA is highly scalable because of asynchronous
processing and service decoupling.
 With the domain-partitioned databases
topology, each domain in the system has its
own database, shared by all of the services
within that domain.
 In the database-per-service pattern, each service
has its own database in a bounded context.


you are here 4  389
```


<a id='p426'></a>
<!-- Página 426 -->

event-driven crossword




```
Event-Driven Crossword
Ready to have some fun and test your knowledge about events,
asynchronous communication, event processors, and multitasking?
Try this crossword puzzle about the event-driven architectural style.




```

Across Down
2. How each part of a process is completed and in what order 1. A way of organizing databases in an architecture
3. _____-and-forget communication 4. Something important that happens
5. When you combine a service with a database, you get a 7. Type of event that kicks off a business process
physical bounded _____ 9. Type of event that flows from other events
6. Reducing users’ wait time is the goal of making a system 10. Abbr. for an external communication hub that an app may
more _____ call
8. Async communications don’t _____ for a response 11. An event is used to _____ news that something has
12. Type of communication that requires a response happened
13. Architectural characteristic that deals with speed 12. Part of an architecture that performs a function
18. Some architectures are easier to _____ with new features 14. _____-partitioned databases
19. These communications are sent to a single service using 15. Events are delivered via an event _____
queues 16. A message can be a command or a _____
20. Certain conditions may _____ an event 17. Services can _____ for event notifications

```
Solution on page 401

```

390  Chapter 11

<a id='p427'></a>
<!-- Página 427 -->

```
event-driven architecture


Exercise From page 353
Solution
```

As the architect, how can you modify the current workflow shown on page 352 to speed things up a bit? Draw your
ideas for a new workflow in the space below. Hint: What can you do at the same time? Here’s our solution.

```
These happen at the same
Validate the asynchronously (dotted time,
The customer
line).
submits an order
order and
and waits
generate order ID

Charge the Adjust current
Email the customer’s inventory
customer the credit card No need for
order ID async here

Send the order If the stock
to the fulfillment gets too low,
department order more

Email the customer The order is packed
that the order is and ready to go
ready to ship

Email the customer
when the order is Ship the order No need to wait
delivered to the customer for the item to be
shipped (async again)

Mark the order
as complete




you are here 4  391
```


<a id='p428'></a>
<!-- Página 428 -->

exercise solutions


```
From page 357
Sharpen your pencil
Solution
```

It’s time to test your knowledge about events and messages. For each of the quotes below, mark whether it is more
likely an event or a message, and indicate why.


```
“Adventurous Air flight 12, turn lef t, he ading 230 degrees.“
Event Message
Reason: This is a command sent to only one airplane about something that needs to
happen.
“In other ne ws, a winter storm f ront has just moved into the are a.”
Event Message
Reason: This is being broadcast to lots of people about something that has just happened.


“Ok ay, class, turn to page 42 in your workbooks.”
Be careful—this
one’s tricky!
Event Message
Reason: Even though this is being broadcast to lots of students, it’s a command about
something that needs to happen.

“Hello, ever yone! Sorr y I’m late.”
Event Message
Reason: This is something that happened that is being broadcast to many people.
No response is expected.

“Oh no! I just missed my train!“
Event Message
Reason: Even though no one might be listening, this is something that just happened.
It isn’t directed toward any one individual.

“Excuse me, sir—do you have the time?“
Event Message
Reason: This is a request made to a single individual about something that needs to happen.




```

392  Chapter 11

<a id='p429'></a>
<!-- Página 429 -->

```
event-driven architecture


Exercise From page 359
Solution
```

Based on the Credit Card Charged initiating event and the corresponding processing below, can you identify what the
derived events should be for each service? Think of as many possible outcomes as you can. Here’s our take.
```
Customer makes This is the
a credit card initiating event
purchase
Credit Card
Charged




Fraud Credit
De tection Limit
Ser vice Ser vice
Check for Verif y credit
f raud limit These are the
derived events.


Fraud Detected Credit Limit
Reached

No Fraud Credit Limit
Detected Exceeded

Credit Limit
Okay

Credit Limit
Warning
Notify the customer
that they’re close to
their credit limit.

you are here 4  393
```


<a id='p430'></a>
<!-- Página 430 -->

exercise solutions


```
From page 364
Sharpen your pencil
Solution
```

For each of these tasks, would you use asynchronous or synchronous communication?


```
Gi ve me the shipping options for this order.

Asynchronous Synchronous Either one would work


Apply payment for this order and le t me know if the payment goes through.
Asynchronous Synchronous Either one would work


Fulfill this order for me by picking the items of f the shelf and packing them in a box.
Asynchronous Synchronous Either one would work


Gi ve me the current status of this order.
Asynchronous Synchronous Either one would work


Our inventor y of this item is ge t ting low—ple ase order more stock .
Asynchronous Synchronous Either one would work


Tell the customer that their order has been shipped and is on its way.
Asynchronous Synchronous Either one would work



Update the customer ’s profile picture.
Asynchronous Synchronous Either one would work


Post a customer ’s revie w on the product page.
Asynchronous Synchronous Either one would work




```

394  Chapter 11

<a id='p431'></a>
<!-- Página 431 -->

```
event-driven architecture


From page 368
Sharpen your pencil
Solution
```

Now’s your chance to test what you’ve learned so far about event-driven architecture, events, and asynchronous
processing. Der Nile’s inventory occasionally gets out of sync, as shown below. When this happens, the order cannot
be fulfilled and goes into a back-order state. Der Nile never makes a customer pay for items that are back-ordered,
and the customer can choose whether to wait or cancel the order.
As the architect for Der Nile, what additional events and services would you create to address this situation?




```
1 Order 9
Placement
3 Order
Payment Payment
Ser vice Refunded
Ser vice Placed
2
4
Payment
Applied Oh dear!
What would
you do now?
5
Order ERROR—No Stock
Fulfillment on Hand, Cannot
Ser vice Fulfill Order

6
Backorder


7
8 Email
Notification
Ser vice




Backorder
Email Sent


you are here 4  395
```


<a id='p432'></a>
<!-- Página 432 -->

exercise solutions


```
Exercise From page 376
Solution
```

For each of these business needs, select which topologies you would consider. You can select more than one
topology.

```
We e xpect any where be t ween 20 and 300,000 customers to be on the system at once.
Monolithic Database Domain-Partitioned Database-Per-Service
Databases

The system must be as fast as possible.
Monolithic Database Domain-Partitioned Database-Per-Service
Databases
This medical monitoring system can never comple tely fail—parts of it must always stay
running.
Monolithic Database Domain-Partitioned Database-Per-Service
Database

We’re anticipating changing the database a lot in this ne w line of business.
Monolithic Database Domain-Partitioned Database-Per-Service
Databases

We have to ge t the ne w system up and running as soon as possible.
Monolithic Database Domain-Partitioned Database-Per-Service
Databases

Our data model is e xtremely large and comple x, with lots of interrelated data.
Monolithic Database Domain-Partitioned Database-Per-Service
Databases




```

396  Chapter 11

<a id='p433'></a>
<!-- Página 433 -->

```
event-driven architecture


From page 377
Sharpen your pencil
Solution
```

List any differences you can think of between event-driven architecture and microservices.

Performance
Physical bounded contexts These are
```
ones we camsome of the
```

Data granularity e up with.

Service granularity
Event vs. request processing
Asynchronous versus synchronous processing




```
you are here 4  397
```


<a id='p434'></a>
<!-- Página 434 -->

exercise solutions


```
From page 381
Who Does What
Solution
```

Oh dear! We tried to organize these facts, but got them all mixed up. Can you help us figure out which
statements are about EDA and which are about microservices? Careful—some facts apply to both.




```
I require a bounded context.


I can use the database-per-service pattern.
Event-Driven
Architecture I create systems that can scale.


I mostly use synchronous communication.


I create high-performance systems.


I save you money because I don’t cost a lot.


I rely mainly on asynchronous communication.
Microservices
Architecture I communicate to services using events.


I’m really good at fault tolerance.


I can use a monolithic database.




```

398  Chapter 11

<a id='p435'></a>
<!-- Página 435 -->

```
event-driven architecture


From page 382
Sharpen your pencil
Solution
```

The architecture on page 382 is an acceptable and well-formed EDA, but not a well-formed microservices architecture.
Two fundamental principles are missing that would make it event-driven microservices. Can you list what those two
missing things are?


1. Single-purpose services 2. Physical bounded context (data ownership)




```
you are here 4  399
```


<a id='p436'></a>
<!-- Página 436 -->

exercise solutions


```
Exercise From page 387
Solution
```

Which of the following systems might be well suited for the event-driven architectural style, and why? Hint: Think
about EDA’s superpowers, its kryptonite, and the problem domain.


```
An online auction system where users can bid on items
Well suited for event-driven architecture
Why? The problem domain fits EDA, and this system Might be a fit for event-driven architecture
needs high levels of scalability, elasticity, and Not well suited for event-driven architecture
responsiveness.

A large backend financial system for processing and
Well suited for event-driven architecture
se t tling international wire transfers overnight
Why? None of EDA’s superpowers are needed for Might be a fit for event-driven architecture
this problem. Not well suited for event-driven architecture



A company entering a ne w line of business that
e xpects constant changes to its system Well suited for event-driven architecture
Why? EDA might be a possibility, since it makes Might be a fit for event-driven architecture
change easier. Not well suited for event-driven architecture


A small baker y that wants to start taking online
orders Well suited for event-driven architecture
Why? EDA is too complex and expensive for a small Might be a fit for event-driven architecture
bakery. Not well suited for event-driven architecture



A social media site where users can post and respond
to comments Well suited for event-driven architecture
Why? The async and broadcast capabilities of EDA Might be a fit for event-driven architecture
are a good fit here. Not well suited for event-driven architecture




```

400  Chapter 11

<a id='p437'></a>
<!-- Página 437 -->

```
event-driven architecture




```

Event-Driven Crossword Solution

```
From page 390




you are here 4  401
```


<a id='p438'></a>
<!-- Página 438 -->


<a id='p439'></a>
<!-- Página 439 -->

12 Testing Your Knowledge
```
do it yourself




```

Ready to test your skills in creating a distributed architecture? In this
chapter, you’re the software architect. You’ll be determining architectural characteristics, building a
logical architecture, making architectural decisions, and deciding whether to use microservices or
event-driven architecture. The exercises in this chapter will give you an end-to-end view of what a
software architect does and show you how much you’ve learned. Get ready to create an architecture
for a student standardized test–taking system called Make the Grade. Good luck—we hope you get an
A on your architecture!




```
this is a new chapter   403
```


<a id='p440'></a>
<!-- Página 440 -->

testing system requirements



Welcome to Make the Grade
Congratulations­—you’ve just been hired by Dataville Public Schools to build a
new system for standardized testing. All students in a specific grade level will take
the same test to determine how well students, teachers, and the schools are doing.



```
irements document
Make the Grade requ m teacher.
ctored by their homeroo
e a we b-b ase d tes t in their homeroom, pro as fas t as po ssi ble.
Students will tak sent questions
ts are tim ed (2 ho urs ), the system must pre
Because tes y answer it,
on the screen. Once the
pre sen ted wit h a mu ltiple- choice question nts ma y ski p questions,
Each student is
er an d de live rs the ne xt question. Stude
answ
the system captures the g for ward is allowed.
no t go ba ck to prior ones— only movin
bu t ma y ) and the results are
tom ati cal ly gra ded (correct or incorrect le.
Once captured, each an
sw er is au ase connections availab
ati on al da tab ase , wh ich has only 300 datab
stored in a central rel e time.
ing tests at the exact sam
re fro m 20 to 20 0,0 00 students could be tak
Anyw he uling tests and for
g ad mi nis tra tor is responsible for sched
The Dataville Public Sch
ools tes tin students sign in to the
er key s, an d the list of students (used when
maintaining tests, answ
system). teacher
nerate student reports,
tav ille Pu bli c Sch oo ls, uses the system to ge
Rita, the head of Da g is complete.
l reports after all testin
evaluations, and schoo uled.
t when tests are sched
s the system to find ou
The proctor (teacher) use


```

Meet Rita,
head of Rita has some other
Dataville important requirements
Public Schools. for the system.

```
Pay attention, “It’s imperative that no student answers are lost, even if the system
because these crashes.”
things are
“We need this system in place for the start of the next term, which is
important.
in six months.”
“You absolutely have to make sure that students cannot hack into the
system and steal the test answer keys.”
“Testing doesn’t occur every day. Some days there are only 20
students taking a test; other days there could be 200,000 at the exact
same time. Sometimes tests might be staggered throughout the day.”




```

404  Chapter 12

<a id='p441'></a>
<!-- Página 441 -->

```
do it yourself



```

Student testing workflow
Now that you have the requirements, let’s take a look at the primary workflow of
the Make the Grade system so you can better understand those requirements.



```
1 2 { "student_id": "45",
```

1. What is your quest?
A. To cross the Bridge of Death Get question Submit answer "question": "1",
B. To seek the Holy Grail "answer": "B" }
C. To answer your silly questions
```
Student



Get next question
4
Auto grade
3


6
Generate reports once 5 { "student_id": "45",
all testing is complete Store results "question": "1",
"answer": "B",
"grade": "Correct" }
Test Answer
Database




Sharpen your pencil
```

Given the requirements for Make the Grade, list some challenges that you will need to address when creating an
architectural solution.




```
Solution on page 420

you are here 4  405
```


<a id='p442'></a>
<!-- Página 442 -->

planning architecture



Planning the architecture

```
I’ve given you the
requirements, so what’s the
big delay? Why aren’t you
developing the system? We only
have six months.




Even though Rita is impatient
to see some progress, don’t let
that sway you from creating
a solid and well-thought-out
architecture.
```

We have to create an architecture first.
As you’ve learned, architecture is a critical part of any software system.
Without it, the system will likely fail to achieve any of its goals.
Before you start developing code, you have to create an architecture.
This means going back to what you learned in Chapter 1 about the four
dimensions of software architecture.
Don’t worry—we’ll get the system done. But first, it’s important to know
what we’re building.




406  Chapter 12

<a id='p443'></a>
<!-- Página 443 -->

```
do it yourself



```

The architects’ roadmap
Let’s get the Make the Grade architecture started. You’ll use the steps you’ve
learned to translate requirements into an architecture.




```
1 Start here.


Finally, y
your softowu’ll diagram
2 5 archit are
ecture using
```

Then you’ll need to all four o 4
get logical. dimensionsf. these Next, you’ll
```
document your
brilliant decision.




You now know enough to
pick a style. 3




```

This diagram will serve as your roadmap as you make your way through each of the
exercises, so get used to seeing it. The next few pages will walk you through these steps.
Good luck on your journey—Dataville Public Schools is counting on you.




```
you are here 4  407
```


<a id='p444'></a>
<!-- Página 444 -->

identifying architectural characteristics



Step 1:
Identify architectural characteristics You are here.
In this first step, you’ll use the requirements below to identify the
architectural characteristics that are critical for the success of the Make
the Grade student test-taking system. On the next page, identify up to
seven driving characteristics. Then select the three you think are the
most critical for the system to be successful.
Remember, implicit characteristics are those that are implied in
virtually every software architecture. (Would you ever not worry about
security?) If you see one you feel is critical for the success of the system,
move it over to the driving characteristics area.

“It’s imperative that no student answers are lost, even if the system
crashes.”
“We need this system in place for the start of the next term, which is
```
We copied the requirements e
```

in six months.”
```
make it easier for you to useher
the
to
```

“You absolutely have to make sure that students cannot hack into the to identify the driving architect m
system and steal the test answer keys.” characteristics. ural
“Testing doesn’t occur every day. Some days there are only 20
students taking a test; other days there could be 200,000 at the exact
same time. Sometimes tests might be staggered throughout the day.”


```
irements document
Make the Grade requ cher.
by their homeroom tea
we b-b ase d tes t in the ir homeroom, proctored t as po ssi ble .
a fas
Students will take st present questions as
(2 hours), the system mu
Because tests are timed y answer it,
on the screen. Once the
pre sen ted wit h a mu ltiple- choice question nts ma y ski p questions,
Each student is
er an d de live rs the ne xt question. Stude
answ
the system captures the for ward is allowed.
no t go ba ck to pri or ones— only moving
but ma y ) and the results are
tom ati cal ly gra ded (correct or incorrect le.
Once captured, each an
swer is au ase connections availab
ati on al da tab ase , wh ich has only 300 datab
stored in a central rel e time.
ing tests at the exact sam
re fro m 20 to 20 0,0 00 students could be tak
Anyw he uling tests and for
g ad mi nis tra tor is responsible for sched
The Dataville Public Sch
ools tes tin students sign in to the
er key s, an d the list of students (used when
maintaining tests, answ
system). cher
rate student reports, tea
ille Pu bli c Sch oo ls, uses the system to gene
Rita, the head of Datav g is complete.
l reports after all testin
evaluations, and schoo uled.
t when tests are sched
s the system to find ou
The proctor (teacher) use




```

408  Chapter 12

<a id='p445'></a>
<!-- Página 445 -->

```
do it yourself




Exercise
```

In Chapter 2, we showed you how to use this template to limit the number of architectural characteristics. Flip back to
page 70 if you need a refresher on how to use it.

Top 3 Driving Characteristics Implicit Characteristics

```
feasibility (cost/time)

security

maintainability

observability
These are implied characteristics. Move
them to the Driving Characteristics
column if you think they are critical to
the success of the system.

Go back
you need ato Chapter 2 if
the definit refresher on
Pick the top three most important ones (in any order). common ar ions of these
character chitectural
istics.
Possible Candidate Architectural Characteristics
performance data integrity deployability
responsiveness data consistency testability
availability adaptability configurability
fault tolerance extensibility customizability
scalability interoperability recoverability
elasticity concurrency auditability
Solution on page 421

you are here 4  409
```


<a id='p446'></a>
<!-- Página 446 -->

identifying logical components



Step 2:
Identify logical components
Good job! Now that you’ve identified the critical architectural You are here.
characteristics for Make the Grade, it’s time to apply what you learned in

## Chapter 4 to create logical components.

Using the requirements and primary workflow on the previous pages,
use the actor/action approach to identify the users and their actions. Then
identify as many logical components as you can on the next page.

Here’s some additional information you might find useful for this exercise:
```
Students sign in to the system using their student ID. The system will verify the date,
student ID, test, and teacher when a student signs in.

Rita, the head of Dataville Public Schools, will wait at least one day after testing has This gives the system time
finished before generating reports. to record all the answers
in the database.
The classroom teacher acts as the proctor for the test, watching the students to make
sure they don’t cheat and providing assistance. The teachers use the system to find
out when a test is scheduled for their class.

When a test is created, the questions and answers are sent to the test administrator,
who enters them into the system. The same goes for any modifications to existing
tests.


Sharpen your pencil
Using the actor/action approach, identify the actions for each of these actors.




Student System Test Teacher Head of Dataville
Administrator (Proctor) Public Schools




Sign in



We did this
one for you.

Solution on page 420

```

410  Chapter 12

<a id='p447'></a>
<!-- Página 447 -->

```
do it yourself




Exercise
```

Using the space below, draw your logical components and their interactions.


```
ur
```

Logical Architecture Key Use this key for yo re .
```
logical ar ch it ectu
Component


Actor
Data
Entity

Report
Async
Sync




Solution on page 422

you are here 4  411
```


<a id='p448'></a>
<!-- Página 448 -->

choosing an architectural style



Step 3:
Choose an architectural style
We know that this system will have separate parts that require different
architectural characteristics, so it makes sense to use a distributed
architecture, such as microservices or event-driven architecture.
Leveraging what you’ve learned about both styles, use the next page to
analyze their pros and cons with respect to the Make the Grade test- You are here.
taking system. You will also need to go back to the requirements, your
logical architecture, and the star rating charts for each architectural style
(we’ve added those for you below). Choose an architectural style based on
your analysis.

The more Microservices Event-Driven Architecture
stars, the
better that
characteristic
is supported.


Both of
these styles
are complex. These three
Welcome to characteristics
distributed are the same
architecture. for both styles.

Here are some considerations that might help you decide which
architectural style would be better suited for Make the Grade:


```
Go back to your logical architecture diagram and count the actions you identified
that you would consider events. If you find there aren’t many events, event-driven
architecture might not be the right choice.

Think about the nature of the data in the system. If most of the data is shared, then
microservices probably isn’t the right choice.

Think about how many actions you identified are synchronous and how many are
asynchronous. If you have a lot of synchronous actions, event-driven architecture
might not be a good fit.




```

412  Chapter 12

<a id='p449'></a>
<!-- Página 449 -->

```
do it yourself




Exercise
```

Outline the pros and cons of each architectural style to help you make a choice about which one might be most
appropriate for Make the Grade.
```
Microservices Architecture Analysis
Pros Cons




Event-Driven Architecture Analysis
Pros Cons




```

List your winning choice here:



```
Solution on page 423

you are here 4  413
```


<a id='p450'></a>
<!-- Página 450 -->

documenting architectural decisions



Step 4:
Document your decision
Good work: you’ve just chosen which architectural style you are going
to use for Make the Grade. Now’s your chance to explain why you made You are here.
the choice you did and document your architectural decision.
As you learned in Chapter 3, an architectural decision record, or
ADR, is an effective way to document your architectural decisions. Use
the ADR on the next page to document your architectural style decision.
Assume that this is your 11th architectural decision.

```
Revisit Chapter 3 if you
need a refresher on
architectural decision records.


What should I put in the
Consequences section of
my ADR if my architectural
decision doesn’t have any
consequences?



Every architectural decision has
consequences.
Maybe it’s cost, or maybe it’s sacrificing a little bit of performance
to have better security. Regardless, every architectural decision has
consequences.
Think about the trade-off analysis you just did. Each one of those
trade-offs implies a consequence—something you were willing to
give up (or accept) to get something better. The Consequences section
of an ADR is a great place to document your trade-off analysis
and the corresponding consequences of your decision.
If you can’t find any consequences in your architectural decision,
keep looking, because they’re there.




```

414  Chapter 12

<a id='p451'></a>
<!-- Página 451 -->

```
do it yourself




Exercise
Architectural Decision Record

```

Title:

Status: Proposed We did this
```
one for you.
```

Context:




Decision:




```
What is the impact of your isio
```

Consequences: trade-offs are you willing todec n? What
```
accept?




Solution on page 424

you are here 4  415
```


<a id='p452'></a>
<!-- Página 452 -->

diagramming the architecture



Step 5:
Diagram your architecture You
```
are h
```

Now it’s time to combine all four dimensions of software architecture
```
ere.
```

and show us your vision of the Make the Grade architecture. In this last
exercise, you’ll diagram your architecture on the following page using the
key on this page.
There’s not a lot of room to diagram your architecture, but that’s
intentional. While a lot of detail can go into architecture diagrams, what
we’re asking you to do is sketch out a high-level physical view showing the
user interfaces, services, databases, communication type (sync or async),
and how all of these architectural artifacts connect to each other.

Physical Architecture Key
```
User Interface Draw a computer screen to represent the user interface, and
indicate which type(s) of users are interacting with it. For example,
if you have separate user interfaces for the test administrator and the
education department (for generating reports), show two computer
screens. If they share a single user interface, show one computer Feel free to
screen with multiple actors interacting with it. annotate your
diagram to clarify
Use a box to represent a service. Be sure to include the components points or describe
Service
Name
that the services implement, which should match the logical things.
components you identified in the prior exercise. Also, indicate
Component which user interfaces access the service and which other services
communicate with the service. Last, give your service a meaningful
and descriptive name.

Database Draw a cylinder to represent each physical database in your solution.
Your label should indicate what type of data it stores (for example,
Student Answers). Show which services write to the database and which
services are read-only by drawing arrows to indicate the data flow to
and from the services. (Writes assume reads.)


Async Draw dotted lines to represent asynchronous communication (such as
using a queue, topic, or stream), and solid lines to represent synchronous
Sync
(blocking) communication between services and user interfaces.


If your architecture uses messages or events, draw a box or an
envelope to indicate the data being passed (for example, Student
Answer) or the event being triggered (for example, Answer Submitted).
Event or Message



```

416  Chapter 12

<a id='p453'></a>
<!-- Página 453 -->

```
do it yourself




Exercise
```

Use this space and refer to the key on the previous page to sketch your physical architecture for Make the Grade.




```
Solutions on pages 425–426

you are here 4  417
```


<a id='p454'></a>
<!-- Página 454 -->

chapter summary



There are no right (or wrong) answers!
Congratulations—you’ve just created an architecture!
What we’re about to show you are the exercise “solutions.” We’ve used quotes there because
our answers are not the only ones possible. You see, there are no right or wrong answers in
software architecture: it’s all about analyzing trade-offs and being able to justify your decisions.
Compare your answers with the ones we’re about to show you. See how your solutions differ
and think about what you might have done differently, or confirm that you made what seems
to you to be the most appropriate choice. We’ll show you our Make the Grade architectures
for microservices and event-driven architecture, since both these styles are viable options.
Software architecture is always a learning process. Each new problem brings a whole new set
of conditions, constraints, and business and technical concerns. There is no one-size-fits-all
architecture—it’s up to you, the architect, to come up with the most appropriate architecture
for your situation.




Bullet Points
 When analyzing requirements for a business problem,  When choosing an architectural style, make sure
```
always gather additional information from the you take into account the characteristics of the
business stakeholders or project sponsor. architectural style, the problem domain, and the
driving architectural characteristics you identified.
```

 While there’s no “checklist” for creating an
```
architecture, the four dimensions of software  Hybrid architectures (those combining two or more
architecture (introduced in Chapter 1) provide a good different architectural styles) are very common. Just
roadmap. be sure to verify that the hybrid architecture still
addresses your critical architectural characteristics.
```

 Identifying driving architectural characteristics
```
requires you to analyze the business requirements  Architectural decision records (ADRs) are a great way
and technical constraints. to document your choices. They communicate the
reasons for your architectural decisions as well as your
```

 Implicit architectural characteristics become driving
```
trade-off analyses.
characteristics if they are critical or important to the
success of the system.  When diagramming your physical architecture, be
sure to include all the components you identified in
```

 Make sure you can tie each driving characteristic back
```
your logical architecture.
to some sort of requirement or business need.
 Remember that there are no right or wrong answers
```

 When identifying logical components and creating
```
in software architecture. As long as you can provide
a corresponding logical architecture, try to avoid
a reasonable justification for your architectural
adding physical details such as services, databases,
decisions, you are on the right track for success.
queues, and user interfaces—those artifacts go into
the physical architecture.




```

418  Chapter 12

<a id='p455'></a>
<!-- Página 455 -->

```
do it yourself




You got through the
entire book? Including all
the exercises? Well, then—
we want you!




You are well on your way to
thinking architecturally!
We are going to assume that you actually read this book all
the way through and didn’t just jump to the end. If so, we
congratulate you for it! Job well done.




Congratulations!
You’ve made it to the end.
```

Though there is still the appendix.

And the index.

And there’s a website...

You aren’t getting away that easily!

(Go ahead, you can admit it—you just can’t get
enough of software architecture, can you?)




```
you are here 4  419
```


<a id='p456'></a>
<!-- Página 456 -->

exercise solutions



```
From page 405
Sharpen your pencil
Solution
```

Given the requirements for Make the Grade, list some challenges that you will need to address when creating an
architectural solution.
```
Storing up to 200,000 simultaneous student answers in a relational database that has only 300 connections.
Delivering the next question to each student as fast as possible while making sure student answers are not lost.
Coming up with a viable solution that can be delivered within a six-month time frame.
Making the system elastic to reduce cost and resource use when testing is not happening or there are only a
few students taking a test.

From page 410
Sharpen your pencil
Solution
Using the actor/action approach, identify the actions for each of these actors.




Student System Test Teacher Head of Dataville
Administrator (Proctor) Public Schools

Grade Write to
answer database Generate
Get test
schedule reports
Get next
question Schedule
tests

```

Sign in Maintain
```
Maintain list
tests
of students
```

We did this
one for you. Submit
```
answer



```

420  Chapter 12

<a id='p457'></a>
<!-- Página 457 -->

```
do it yourself



Exercise From page 409
Solution
```

In Chapter 2, we showed you how to use this template to limit the number of architectural characteristics. Flip back to
page 70 if you need a refresher on how to use it.

Top 3 Driving Characteristics Implicit Characteristics
```
We only have
Feasibility six months! feasibility (cost/time)
Need to protect
Security the answer key. security
There can be 20 to 200,000 students—
Elasticity the very definition of elasticity. maintainability
We have to deliver the
Responsiveness next question right away. observability
If the system isn’t available,
Availability students can’t take a test.
We absolutely cannot
Data integrity lose student answers.
We don’t want the students to have to
Recoverability start the test over if the system crashes.


Possible Candidate Architectural Characteristics

performance data integrity deployability
responsiveness data consistency testability
availability adaptability configurability
fault tolerance extensibility customizability
scalability interoperability recoverability
elasticity concurrency auditability



you are here 4  421
```


<a id='p458'></a>
<!-- Página 458 -->

exercise solutions


```
Exercise From page 411
Solution
```

Using the space below, draw your logical components and their interactions.

```
Logical Architecture Key

Component These components are
part of the testStudent
taking functionality
Actor
Data interacts interacts
Entity interacts
Report
Async Capture
Student Next Test
Sync Sign-in Question Answer

This is async so the
reads student doesn’t
reads have to wait.

Test Student Test Test Answer
reads Automatic
Schedule Information Questions Key Grading


writes
writes writes writes
Student
Answers

Test Student Test
Scheduler Maintenance Maintenance reads

interacts interacts Test
interacts Reporting
interacts
The proctor needs generates
to know when the This is the
test is taking place. administrative
Test
Administrator
functionality. Report
Proctor (Teacher) Head of Dataville
Public Schools




```

422  Chapter 12

<a id='p459'></a>
<!-- Página 459 -->

```
do it yourself


Exercise From page 413
Solution
```

Outline the pros and cons of each architectural style to help you make a choice about which one might be most
appropriate for Make the Grade.
```
Microservices Architecture Analysis
Pros Cons
```

A microservices architecture provides good Microservices gets a low performance rating, but we
elasticity, scalability, and fault tolerance—things could address this by using caching and minimizing
Make the Grade needs. communication between services.
```
The test administrator’s functionalities write to
```

Partitioning data, so that each microservice a database that other services need to read (for
owns its own data, provides a good level of fault test questions, student sign-on information, answer
tolerance and data access control. keys, and so on). This implies that we need to share
```
data, something for which microservices is not well
```

Make the Grade has lots of separate, independent suited. However, this data is fairly static and can
parts—test taking, grading, maintenance, and be shared through in-memory caching.
reporting—so it lends itself well to separately
deployed, single-purpose services that don’t require
much interaction.

```
Event-Driven Architecture Analysis
Pros Cons
```

Event-driven architecture (EDA) is highly responsive The test administrator’s functionalities (student
and provides the elasticity, scalability, and fault and test maintenance and test scheduling and
tolerance Make the Grade needs. reporting) are not really suited for EDA.
A student submitting an answer can be considered There aren’t many events in this system—mostly,
an event; the responses would be to deliver the next requests are being made to the system. The only
question and automatically grade the answer. However, event we identified was a student submitting
this is a fairly isolated event—really the only one in an answer, but that event only has one listener
the system. (the auto-grading functionality).

```
the only
Remember, this isnch’toice based on our
answer, just our
analysis.
```

List your winning choice here: Based on our analysis, we selected microservices for Make the Grade.




```
you are here 4  423
```


<a id='p460'></a>
<!-- Página 460 -->

exercise solutions


```
Exercise From page 415
Solution
Architectural Decision Record

```

Title: 011: Use of the microservices architectural style for the Make the Grade system

Status: Proposed

Context:
Make the Grade is a test-taking system that needs high levels of responsiveness, fault tolerance, elasticity, and
data integrity. Because there are separate parts of the system (admin, reporting, grading, and test taking) that
require different architectural characteristics, a distributed architecture is appropriate. The two choices are
microservices and event-driven architecture.

Decision:
We will use the microservices architectural style.
Microservices provides the necessary fault tolerance, elasticity, and scalability.
Performance deficiencies and high responsiveness needs are addressed through minimal inter-service communication,
caching to minimize data retrieval needs (student information, test questions, and test answer keys), and
asynchronous communication for automatic grading and storing students’ answers.
Data integrity (preventing data loss) is addressed by using persistent queues between the Capture Answer and
Automatic Grading components, along with client acknowledgment mode in the Automatic Grading component, to
make sure that each student answer stays on the queue until it is persistent in the Student Answer Database.
The test administration functionality will be a single microservice that combines the test scheduling, test
maintenance, and student maintenance functionalities. Reporting will be a single microservice as well.

Consequences:
Technically partitioned teams will need to be reorganized into cross-functional teams and will work in parallel
in order to finish the system in six months.
We will need to use in-memory caching to address the system’s performance, elasticity, and data sharing needs.
We will need additional infrastructure to support microservices: specifically, a service orchestrator like
Kubernetes and a more effective CI/CD deployment pipeline.




424  Chapter 12

<a id='p461'></a>
<!-- Página 461 -->

```
do it yourself


Exercise From page 417
Solution
```

Use this space and refer to the key on the page 416 to sketch your physical architecture for Make the Grade.

```
Microservices Architecture Diagram
Once the answer is on the
persisted queue, the next
question is presented.
The data each
service needs is annels
We’ll use multipledch
Student Interface
stored in an inmemory cache. for elasticity an tolerance.
additional fault
```

Student Information
```
Sign-in
Database Test Taker Auto Grader
Student
Automatic
Sign-in Next Test
Grading
Question
Cache
Cache
Capture
Student Answer
Information Student
Cache Answers
Student
```

Maintenance

```
Test
Information

Test Contains questions,
Maintenance
answer key, and
Test test schedule.
Scheduling
Student Answer
Test Database Database


```

Test Administration
```
Interface Reporting

Proctors use this the Test
interface to get Reporting
test schedule. Reporting Interface


you are here 4  425
```


<a id='p462'></a>
<!-- Página 462 -->

exercise solutions


```
Exercise From page 417
Solution
```

Use this space and refer to the key on page 416 to sketch your physical architecture for Make the Grade.

```
Event-Driven Architecture Diagram
Proctors use this
interface to get .
the test schedule
Submit
Answer

Capture
Student Interface Answer


Test Administration
The next
Interface
question is
Sign-in pushed to
the student
Student interface. Answer
Sign-in Submitted
Event
Cache

This event delivers.
Administrative

Student the first question
Maintenance
Auto Grader
Next Question
Test Automatic
Signed-in Next Test
Maintenance Grading
Event Question
Cache
Test Cache
Scheduling
All data is cached on
startup for each service.

This database
contains everything Central Database
except the student
answers.
Reporting

Test
Reporting
Student Answer
Reporting Interface Database


```

426  Chapter 12

<a id='p463'></a>
<!-- Página 463 -->

A The Top Six Topics
```
appendix: leftovers


We Didn’t Cover




```

There’s a lot more to be said about software architecture. We promise,
you’re done with this book. But reading this book is just the first step in your journey to thinking
architecturally, and we couldn’t in good conscience let you go without a little more preparation. So,
we’ve gathered a few additional juicy bits into this appendix. Each of the topics that follow deserves as
much attention as the other topics we’ve covered. However, our goal here is just to give you a highlevel idea of what they’re all about. And yes, this really is the end of the book. Except for the index, of
course—it’s a real page-turner!



```
this is a new chapter   427
```


<a id='p464'></a>
<!-- Página 464 -->

coding as an architect



#1 The coding architect


```
After reading this book,
I’m interested in becoming
a software architect—but I also
really like writing source code. Can
I still do that as an architect?




Yes! We firmly believe that software architects
should still write source code. Not only does it help
you maintain your technical skills, but it also shows you how your
architectural decisions play out in real life.
However, it’s not always easy to balance hands-on coding with
software architecture. As you’ve seen, there’s a lot to software
architecture. It will take up most (if not all) of your time.
Don’t worry though—we’ll share some tips and techniques for
writing software while being an effective software architect.




```

428  Chapter 13

<a id='p465'></a>
<!-- Página 465 -->

```
appendix: leftovers




```

Don’t become a bottleneck
Be careful not to take ownership of code that is on the product’s critical path.
Leave things like the underlying framework code and really complex or crucial
parts of the system to your development team. That way, if you get pulled away
by architecture-related stuff, you won’t hold up your team.




```
Write proof-of-concept code
Having trouble making an architectural decision? How about writing some
code to demonstrate each option? Writing proof-of-concept code is a great
way to better understand the implications of your architectural decisions while
maintaining your technical expertise. A word of advice, however—unless you
know for sure you’re going to throw it away, take the time to write the best
```

Here are some more production-ready code you can. It could very well end up in production.
ways to make sure
you don’t become a
bottleneck.

Pay back some technical debt
Almost every development team accumulates technical debt (needed changes
that are deferred to a later time). Help your team out by addressing some of it.
They’ll appreciate it, and if you get called away, it won’t hold them up.




```
Get involved during production outages
When an outage strikes, step in to assist, if you can. Help your development
team identify the root cause and make the code changes needed to get the
system back up and running. This also gives you an opportunity to see the
detailed implementation of your architecture.
And here are
some ways to
stay continuously
```

Do lots of code reviews involved.
No one likes doing code reviews. But it’s a good way to stay involved, and it
helps you make sure the source code stays aligned with your architectural
decisions.


```
you are here 4  429
```


<a id='p466'></a>
<!-- Página 466 -->

expectations of the role



#2 Expectations for architects
We’ve talked a lot in this book about architecture, but not so much
about the role of a software architect. While the specifics will vary
```
from company to company, here are some things any software
```

architect will be expected to do, regardless of title.




Make architectural
decisions
An architect is expected to define architectural
decisions and design principles and use them to
guide technology decisions within the team, the
department, and/or across the enterprise. Continually analyze the
```
architecture
An architect is expected to always be analyzing
the current architecture and technology
environment and making recommendations
for solutions and improvements. This
continuous analysis is a way of checking for
architectural vitality—that is, how viable
```

Keep current with the the architecture still is, given constant changes
```
in business and technology.
```

latest trends
To remain relevant (and retain a job!),
developers must keep up to date on
technical and industry trends. For architects,
it’s even more critical to keep current. Doing
so helps you prepare for the future and
make correct decisions. Ensure compliance with
```
the architecture
Architects should continually verify that the
development teams are following the approved
architectural decisions and design principles.
This is called architectural governance.
Regardless of how good the architecture is, the
system won’t work unless everyone adheres to
your architectural decisions.




```

430  Chapter 13

<a id='p467'></a>
<!-- Página 467 -->

```
appendix: leftovers




As an architect, it’s important to
```

Cultivate diverse exposures know a little about a lot of things.
and experiences More about this in a few!
An architect is expected to be familiar with
technologies, frameworks, platforms, and
environments of all sorts. This doesn’t mean you
need to be an expert in all of them, but you should
have some knowledge of what’s out there.

```
Know the business
domain
Effective software architects understand the
business domain of a problem space. Without
knowing what the business does and how, it’s
difficult to understand the problem, goals, and
```

Possess exceptional requirements well enough to design an effective
```
architecture.
```

interpersonal skills
Having exceptional leadership and interpersonal
skills is important. Typically, technologists,
developers, and architects prefer to solve technical
problems, not people problems. But an architect
is expected to provide technical guidance to the
team and lead them through implementing the
architecture. Leadership skills are at least half of
what it takes to become an effective software
architect, regardless of your role or title.

```
The American computer scientist Understand and
Gerald Weinburg is famous for saying, navigate office politics
“No matter how it looks at first, it’s
always a people problem” (https:// Many people will challenge your decisions.
oreil.ly/wyDB8). Product owners, project managers, and
business stakeholders may see a solution as
too costly or not fast enough to implement.
Developers and other architects may
challenge your approach if they feel theirs is
better. You’ll be expected to make a case for
what you propose. You must navigate office
politics and apply basic negotiation skills to
get your decisions approved.


you are here 4  431
```


<a id='p468'></a>
<!-- Página 468 -->

soft skills



#3 The soft skills of architecture
Like we said on the last page, at least half of being a software architect
is having great people skills. You’ll need them to lead and guide your
development team, gain the respect of your peers, and get everyone to
agree to a common vision and direction.
We call these “soft” skills, but they are hard skills to acquire. Using
them effectively requires years of practice and trial and error. Here are
some soft skill techniques to help you become a more effective software
architect.




Demonstrate, don’t discuss
Rather than arguing a point with another architect or development team,
demonstrate it. Every environment is different, which is why simply
Googling never yields correct answers. When you compare the options in
a production-like environment and show the results, there’s little room for
argument.
```
Say it with us:
“Demonstration defeats
discussion.”


Know when to fight and when to let go
Choosing your battles wisely is the mark of a great leader and makes you a
reasonable person to work with. It gains you respect. Fight to the death for
something that’s crucial to making the architecture work, but let things go if
they’re not so important.
Choosing your battles is
good advice, even outside of
software architecture. You’re
welcome.

```

Focus on business value
When talking with business stakeholders, describe your decision or solution
in terms of its business value. Business stakeholders aren’t interested in
things like fault tolerance or testability—they care about things like time
to market, regulatory compliance, and mergers and acquisitions. Translate
your technical concerns into business ones and you’ll be speaking their
language.
```
$$$

```

432  Chapter 13

<a id='p469'></a>
<!-- Página 469 -->

```
appendix: leftovers



Involve developers in your architectural decisions
We have learned two basic leadership rules over the years:
Rule Number 1: If developers don’t know why you made a decision, they are less likely to
agree with it.
Rule Number 2: If developers aren’t involved in a decision, they are less likely to follow it.
Keep your developers involved. Collaborate by asking their opinions about a particular
decision, involving them in a risk-storming exercise, or using the Request for Comment
status in an ADR. Always justify your architectural decisions—and make sure everyone on
the development team understands that justification.
```

This is the ADR
```
from Chapter 12.

```

Divide and conquer
In the book The Art of War, the ancient Chinese warrior Sun Tzu advises, “If
your enemy’s forces are united, separate them.” You can use this tactic when
faced with all-or-nothing situations. Do all parts of the system need 400 ms
response times or 99.999% availability? Dividing the problem into parts can
help you identify what’s hard to achieve, which makes negotiation easier.




```
Keep things simple, clear, and concise
Nothing helps an architect gain respect and trust better than being able to
explain things in clear, concise terms. It makes you more approachable. People
will want to ask you things and get you involved. We call this the “four Cs” of
architecture—be Clear, be Concise, Communicate, and Collaborate. You need
all four to become an effective software architect.




```

Be available to your development team
Nothing is more frustrating for a developer or business stakeholder than having
a critical question come up when you aren’t around to answer it. Make sure not
to spread yourself too thin—be there for your team.
Blocking out your calendar early in the morning or late in the afternoon is a
great way to ensure you don’t get cooped up in meetings all day. Use that time
to collaborate with your development team and be available to answer their
questions. They’ll be grateful for it, and you will gain a lot of respect.



```
you are here 4  433
```


<a id='p470'></a>
<!-- Página 470 -->

tips and tricks for diagramming



#4 Diagramming techniques
Back in Chapter 3, we discussed ADRs as the best way to document the analysis
process that leads to a decision. Another common method architects use to Communication
document architecture is diagrams. Architecture diagrams illustrate many Patterns by
important details that team members benefit from visualizing, such as structure, Jacqui Read is a
topology, communication, dependencies, and integration points. great resource,
This topic can (and does) fill entire books. We’re just here to provide some quick if you’d like to
tips to make your diagrams better, regardless of how you create them. learn more.

Keep it simple
Don’t try to create comprehensive architecture diagrams that include
every detail. If you do, your diagrams will suffer from the “hairball effect”— Trading platform:
becoming too complex and dense to understand.
```
Major information
flows
```

Always include a title Use clear titles for
Most architecture diagrams represent a view or perspective, and your title your diagrams.
should make yours explicit.

Use unidirectional arrows to represent
communication
Double-headed arrows are ambiguous. Did the author intend to indicate
two-way communications, or is just that the default arrow?
Using unidirectional arrows removes all ambiguity and makes Single-headed
documentation more explicit. arrows remove
```
ambiguity.
Trades Originating trades
PM ATP PM ATP
Adjusted trades


Did the architect mean Don’t use mysterious
that this is two-way acronyms, either!
communication?
Originating trades Advanced
Portfolio
Trading
```

Use real labels, not acronyms Manager Adjusted trades Platform
Only insiders understand acronyms. Spell
things out whenever possible to avoid confusion
```
Use real labels.
```

and eliminate the need for extra documentation.
```
Isn’t this much
clearer than “PM”
and “ATP”?

```

434  Chapter 13

<a id='p471'></a>
<!-- Página 471 -->

```
appendix: leftovers



```

Use solid lines for sync and dotted for async This is a
```
synchronous
```

communication (blocking) call.
Architects need a way to specify whether communication is
synchronous (blocking) or asynchronous (nonblocking). A solid Originating trades Advanced
line is common shorthand for synchronous communication, and a Portfolio
```
Trading
```

dotted one represents the asynchronous alternative. Manager Adjusted trades Platform


```
And this is an
```

Use consistent shapes and colors asynchronous
Don’t use arbitrary shapes to try to save room; consistent (nonblocking) call.
shapes and colors cut down on the visual “noise” created by
needless inconsistency.



```
Record- Transactions Originating trades Advanced The Advanced Trading
Portfolio Platform calls the
Keeping Trading
Manager Adjusted trades Platform Adjustment Rules
System
service and waits
The Advanced Trading (blocks) for the result.
Platform writes to
the database.
Stock Rating Ratings
System
Rebalancing Adjustment
Tool Rules



Key These services only read
from the database.
Event Event handler written and
handler maintained by internal team


Always include a key
External External system accessed Just about the only universal shape in software
system through a standard API diagrams is the database cylinder. Pretty much
everything else is up for grabs. Don’t make your
Asynchronous call viewers guess! Adding an explicit key makes the
diagram accessible to a broader audience, with less
Synchronous call extra documentation.
Operational database



you are here 4  435
```


<a id='p472'></a>
<!-- Página 472 -->

growing your knowledge



#5 Knowledge depth versus breadth
```
The knowledge base of
```

An unexpected thing happens to your brain when you a super-excited junior
become a software architect—the new role changes the Stuff developer—“I can’t
kinds of things you seek out and learn. Consider this you know believe I get paid to
structure, which categorizes all the information in the do this!”
world, as far as you know at the beginning of your career. Stuff you know
```
you don’t know

Early in your career,
there’s a lot you Stuff you don’t know
don’t know that you don’t know
you’ll need to know.
Junior developer knowledge pyramid

Paying attention to
projects over time makes As you move along in your career from a junior
you proficient with more software developer to a tech lead, the “stuff you
technical stuff. know” grows—things like programming languages,
Stuff
you know frameworks, tools, and platforms. You’re also able to
help and mentor other developers in this role.
Stuff you know
you don’t know

Stuff you don’t know
you don’t know

Senior developer/tech lead

```

Over time, as you gather more expertise and become
the go-to person, you start to grow the middle part
of the pyramid—the “stuff you know you don’t Stuff We can tell you—
know.” Because you’re maintaining your hardcore you know finding out about
technical skills as well (the “stuff you know”), it takes this stuff is a
a lot of effort to get to this point. Congratulations! pretty humbling
```
Stuff you know experience.
you don’t know


Stuff you don’t know
you don’t know

Junior architect


```

436  Chapter 13

<a id='p473'></a>
<!-- Página 473 -->

```
appendix: leftovers



Technical breadth Your technical depth consists of every topic on
which you have expertise.
Stuff you Remaining an expert in any technology requires
Technical
have to investing time to keep up with constant change.
depth maintain Thus, maintaining technical depth takes time.
Your technical breadth includes the areas in
which you have expertise, what you know about
the existence of other solutions, and what you
know about some of these solutions’ trade-offs.
As an architect, knowing that there are five
different ways to solve a problem is better than
deeply knowing one way to solve it.
```

Technical depth versus breadth




New architects’ knowledge pyramids start out Stuff
looking like those of tech leads, but you should you know
make an effort to broaden your experience base.
If you have expertise in .NET, for example, see Stuff you know
if you can do some work on a Java project, a user you don’t know
interface–heavy Javascript project, or a hard data
architecture problem… you get the idea.
```
Stuff you don’t know
you don’t know
Junior architect

Losing expertise is a
necessary but painful part
of shifting your focus
from depth to breadth.
```

The sweet spot for Stuff
architects is great you know
breadth: knowing the Over time, your expertise will slowly fade a bit
options and trade-offs (which is extraordinarily painful), but this will
for a variety of situations have the benefit of increasing your breadth of
```
Stuff you know
```

and implementations. knowledge. Remember, software architecture
```
you don’t know decisions are all about trade-offs.


Stuff you don’t know you don’t know
Senior architect


you are here 4  437
```


<a id='p474'></a>
<!-- Página 474 -->

architectural katas



#6 Practicing architecture with katas How do you get
```
better at anything
```

The legendary martial artist and actor Bruce Lee once said, “I fear not in life? Practice,
the man who has practiced 10,000 kicks once, but I fear the man who practice, practice.
has practiced one kick 10,000 times.” So how do you attain that kind of
proficiency with software architecture? Glad you asked! We recommend
architectural katas.
A kata is an individual form of exercise used in many martial arts to
practice moves until they’re perfected. In the same spirit, architectural
katas simulate the process of designing a real architecture.
Architectural katas are intended for several small groups of three to five
people. Each group becomes a project team and works on a different kata.
(We sometimes get two teams to do each kata, just to see what differences
arise.) A moderator keeps track of time and facilitates the exercise.
The moderator assigns each group a project needing development. The
team meets for a while, asking questions of the “customer” (the moderator)
for clarification. They discuss technology options that could work and
sketch out a rough vision of their solution. Then they present their solution
to the other project teams and answer challenges (hard but fair questions).
Choosing an overall winner is optional.




```
The key to getting better at soft ware
architecture is to practice it—even in a
simulated exercise.
Do we have your attention?
Keep reading to find out more.




```

438  Chapter 13

<a id='p475'></a>
<!-- Página 475 -->

```
appendix: leftovers



```

How to run katas
Katas are meant to be an adaptable exercise, so follow the rules
below when they make sense for your organization, context,
and needs. Any questions not covered by these rules are the
domain of the moderator.



Preparation
Gather several teams of three to five people. (We prefer odd numbers, so disputes
can be decided by a majority.) Generally, people who work together in the real
world should not be on the same teams; this exercise stresses collaborating with
other architects you don’t already know.
Gather supplies like poster paper or whiteboards. The artifacts you produce may
be very low-tech, depending on the time, complexity, and resources you commit.
Speaking of time, a kata exercise could take as little as 45 minutes or last as long as
several weeks! Your authors have done
```
several katas for real
companies that gave teams
eight weeks to work out a
solution.
Discussion
The teams get together and work through the exact process
outlined in this book: analyzing architectural characteristics,
determining logical components, choosing an architectural style,
and documenting their decisions.
Any technology is fair game, although you should honor
reasonable constraints (you won’t have an unlimited budget or get
to hire new developers). The focus is on architecture and trade-off
analysis.



Presentation
Each team presents its solution and answers questions.
When you are listening to another project team presenting, your
job is to ask questions. Try to keep them constructive. Don’t focus
on only the good parts of the solution or only the deficiencies.
Strive for balanced feedback.




you are here 4  439
```


<a id='p476'></a>
<!-- Página 476 -->

```
I feel like there’s so much
more to know. Are there
are any other resources I
can reach for?

You don’t know
about the website? It has
updates, interesting links
and posts, and much more!




Don’t worry.
This isn’t goodbye.
Congratulations on reading all the way to the
end and doing all the exercises! Job well done.
In case you haven’t noticed, you’ve come a long
way in this book—and your software architecture
journey is just getting started. We’d like to
suggest some next steps.
First, point your browser to
https://www.headfirstsoftwarearchitecture.com to learn
what’s next! Then check out the books below.


What’s next? So much more!

```

Start here. While
some of the
material may seem
familiar, it’s a
worthy successor to
this book. This title is most
```
apropos. Dive deep
into the really hard
parts of software
architecture with
this book.


```

440  Chapter 13

<a id='p477'></a>
<!-- Página 477 -->

```
Index
```


## A

```
accessibility 55, 56, 74
architectural style and 43
auditability 44
```

Accepted status (ADRs) 100 balancing 69
access control 313 capabilities and 68
accessibility 55, 56, 74 categories 48
actor/action approach to logical architecture 135, 137 composite 63
```
consistency 44
```

ADRs (architectural decision records) 97, 114, 292 cross-cutting 55
benefits of 112 data integrity 44
collaboration and 107 defining 45, 46
Consequences section 107, 114, 120, 288 deployability 56, 74
Context section 104, 114 domain requirements 60
context versus justification 106 domains 44
decision-capturing tools 111 driving 292
Decision section 105, 114, 119 explicit 50
documentation and 414 from environmental awareness and 61
editing 102 from holistic domain knowledge 61
exercises 297–299 from problem domain 60
file naming 111 implicit 50, 292, 408
Governance section 109, 114 limiting 48, 70
immutability 102 maintainability 56, 74
multiple projects 111 modularity 56, 74
Notes section 109, 114 modular monolithic architecture 235
opinion and 105 numbers 69
Status section 100–101 operational 54
storage 111 overengineering and 48
Title section 99, 114 planning stages 281
visualization flowchart 103 priorities 64
afferent coupling (CA) 146, 154 privacy 55
```
measuring 148–149 process 52
```

agility 52, 85 reliability 44
architects robustness 56, 74
```
scalability 44, 56, 74
```

coding architects 428–429
```
security 44
```

development team and 433
```
sources 59
```

soft skills 432
```
structural 53
```

architectural characteristics 4, 6–7, 27
```
synergy 48–49
```

abundance 48
```
this is the index 441
```


<a id='p478'></a>
<!-- Página 478 -->

the index


usability 44, 55 spectrum with design 18–19
zoo metaphor 51 structure 3
architectural decision records (ADRs). See ADRs (architec- Architecture Tradeoff Analysis Method (ATAM) 92
```
tural decision records) asynchronous communication 361, 389
```

architectural decisions 4–5, 8, 27, 114. See also ADRs architecture style selection and 412
```
(architectural decision records) benefits 365–366
```

architecture/design spectrum 20–21 diagramming 435
as guides versus rules 93 EDA and 363
examples 93 versus synchronous communication 362–366
planning stages 281 ATAM (Architecture Tradeoff Analysis Method) 92
Second Law of Software Architecture 96
```
authentication 55
```

strategic 19
strategic versus tactical 20–21 authorization 55


## B

tactical 19
trade-offs 19, 24
Two Many Sneakers 94
whys 96 behavior of logical components 68
architectural perspective 17 blueprints 3
architectural styles 4, 12–13, 27, 168 broadcasting model 86
architectural characteristics and 43 building plans 3
distributed. See distributed architectures
event-driven architecture 12
hybrid 292

## C

layered architecture 12 capabilities, architectural characteristics 68
logical components and 43 CBAM (Cost Benefit Analysis Method) 92
microkernel 286–287 choreography 328–331
microservices 12, 169 granularity and 314–317
monolithic. See monolithic architecture
```
code
```

planning documentation 288–289
```
proof-of-concept code 429
```

planning stages 281
```
reviews, coding architects and 429
```

selecting 13, 286–287, 412
```
shared libraries 320
```

architecture shared services 320–321
building plans 3 volatility, microservices and 313
versus design 15
```
code sharing
```

distributed 47
```
microservices and 318
```

gardening exercise 2
```
shared libraries 321
```

house 2
interconnectedness 5 coding architects 428
logical versus physical 127–128 cohesion, microservices and 313
monolithic 47 collaboration, ADRs and 107
need for 2
```
communications, EDA versus microservices 380
```

planning 280–286

442 index

<a id='p479'></a>
<!-- Página 479 -->

```
the index

```

compliance 55 design 18
component coupling 144, 154. See also logical components spectrum with architecture 18–21
afferent coupling (CA) 146 versus architecture 15
choreography 329 design perspective 16
efferent coupling (CE) 147, 154 device-assessment service core 255
First Law of Software Architecture and 153
```
diagramming
```

Law of Demeter and 148–152
```
asynchronous communications 435
```

measuring 148–149
```
communications 434
```

orchestration and 327
```
key 435
```

tightly coupled systems 150–153
```
labels 434
```

total coupling (CT) 148
```
microservices architecture 425
```

composite architectural characteristics 63 physical architecture 290–291
Cost Benefit Analysis Method (CBAM) 92 physical architecture key 416
cross-cutting requirements 58 shapes and colors, consistency 435
```
title 434
```

D dimensions 4, 14
```
distributed architectures 47, 172, 180
```

Database layer 189
```
deployment models
```

database-per-service pattern 374–375, 389 pros and cons 174, 176–177
databases relevance 178–179
diagramming 290 distributed physical architecture
domain-partitioned 389 plugins 255
EDAs 385 pros and cons 274
foreign keys 315 distributed plugins 257
modular monolithic architecture 231 calls 259
topologies 369–374, 389
```
documentation 288–289
```

transactions, granularity and 314–317
data coupling 315 domain-based alignment 234

data dependencies 314–317 domain-driven design (DDD) 137

data ownership 308–309 domain-partitioned architecture 170–171

DDD (domain-driven design) 137 domain-partitioned databases 372–373, 389

deployability 52, 56, 74 domains 11
layered architecture 205 characteristics 46
microservices architecture 332 holistic domain knowledge 61
```
partitioning
```

deployment models 169, 180
```
modular monoliths 234
```

distributed systems subdomains 238
pros and cons 174, 176–177
```
driving characteristics 418
```

monolithic architectures
pros and cons 174–175 implicit characteristics 292
derived events 356–357, 389


```
you are here� 443
```


<a id='p480'></a>
<!-- Página 480 -->

the index



## E

```
events
compared to messages 356–357, 389
derived events 356–357, 389
```

Eclipse IDE 253
```
initiating events 356–357, 389
```

EDA (event-driven architecture) 12, 351 event storming 137
analysis 423
```
evolvability
```

asynchronous communication 361, 363, 389
complexity 385 EDAs 384
databases 385 microservices architecture 332
drawbacks 385 explicit architectural characteristics 50
events 354, 389 extensibility 52, 53, 389
evolvability 384 EDAs 356
extensibility 356
fault tolerance 384
maintainability 384

## F

messages, events 355 fault tolerance
versus microservices 380–382, 412 EDAs 384
Notification Analytics 356 microservices and 313
performance 384 microservices architecture 332
scalability 384 file naming, ADRs 111
star ratings 206, 386 fire-and-forget 389. See also asynchronous communication
superpowers 384
synchronous calls 385 First Law of Software Architecture 90, 114
testability 385 component coupling and 153
```
layered architecture and 203
```

efferent coupling (CE) 147, 154
```
measuring 148–149 foreign keys 315

```

elasticity, layered architecture 205 Fowler, Martin 22

electronics recycling program 139 Front Controller pattern 328

embedded/mobile architecture 199
encapsulated plugins 257

## G

encryption 55 Grains of Sand pattern 311
entity trap 136 granularity, microservices 311, 336
```
balance 316, 336
```

environmental awareness 61
```
disintegrators 311–313, 316
```

error handling integrators 314–317, 336
```
choreography 329
orchestration and 327
```

event-driven architecture (EDA). See EDA (event-driven

## H

```
architecture heterogeneous 88
```

event-driven microservices 382–383 house architecture 2–13
event processing 389 hybrid architecture 292, 418
EDA versus microservices 380 event-driven microservices 382–383, 389

444 index

<a id='p481'></a>
<!-- Página 481 -->

```
the index



```


## I

```
Persistence layer 189
physical architecture 198–200
Presentation layer 189
```

implicit characteristics 50, 408 quick builds 204
driving characteristics 292, 418 reasons for layers 202
infrastructure, queues and 108 scalability 205
initiating events 356–357, 389 specialization 198
inventory management 26, 124 technically partitioned 193, 204
```
testability 205
```

iterative approach 43 Workflow layer 189

J layered monolithic architecture
```
analysis 296
```

Jenkins (continuous integration) 253 planning stage 286–287
```
uses 300
```

joins between databases 233
```
libraries, shared 321, 322, 336, 343
```

JPMS (Java Platform Module System) 229
```
linters 253
```

K localization 53
```
logical architecture
```

katas 438–439
```
actor/action approach 134–135, 137
```

knowledge pyramid 436 assigning requirements 138


## L

```
characteristics analysis 142
cohesion 141
components 127, 130–131, 144–147
```

Law of Demeter 148–152, 154
```
creating 129
```

layered architecture 12 entity trap 136
```
capabilities, sorting by 195 roles and responsibilities 140–141
component placement 196 versus physical architecture 127–128, 157
components 192 workflow approach 132, 137
Database layer 189 logical components 4, 10–11, 27, 154
data-intensiveness 204 afferent coupling (CA) 146–148
deployability 205 architectural style and 43
diagramming layers 290 behavior and 68
domain changes 203 characteristics analysis 142
downsides 205 cohesion 141
ease of reuse 198 component coupling 144
elasticity 205 design and 45
feasibility 204 efferent coupling (CE) 147
First Law of Software Architecture 203 entity trap and 136, 154
MVC and 188, 198 identifying 284–285, 410
namespaces 192 measuring 148
packages 192 monolithic architectures 172
performance 204 names 137

you are here� 445
```


<a id='p482'></a>
<!-- Página 482 -->

the index
planning stages 281 balance 316, 336
requirements 138 choreography 328–331, 345
roles and responsibilities 11 code sharing 318–321
source code repository directory 124–125 common functionality 318
splitting by capability 195 complexity 333
logical component system 45 data ownership 308–309
```
deployability 332
```

M diagramming 425
```
drawbacks 333
```

maintainability 53, 56, 74 versus EDA 412
EDAs 384 evolvability 332
microservices architecture 332 fault tolerance 332
microkernel architecture Grains of Sand pattern 311
adaptability 266 granularity 311, 336
analysis 296 granularity disintegrators 311–313, 336
core 251 granularity integrators 314–315, 336
Decorator design pattern 262 maintainability 332
device-assessment service core 255 monolithic databases 333
distributed 258 orchestration 326–327, 336, 345
distributed physical architecture 255, 274 performance 333
drawbacks 267 physical bounded contexts 308–309
Eclipse IDE 253 reasons to use 306
evolvability 266 scalability 332
insurance application 253 services 307, 310–311, 316
Jenkins Continuous Integration (CI) tool 253 star ratings 334
linters 253 superpowers 332
monoliths 256, 258, 270, 274 technically partitioned teams 333
partitions 266 testability 332
performance 267 workflow 324–325, 333, 336
planning stages 286–287 modularity 52, 56, 74
plugins 251–252, 257–259, 267–268 modular monolithic architecture 219, 220, 238
simplicity 266 analysis 296
star ratings 268 architectural characteristics 235
synchronous communication 255 databases 231
user interface 262 domain-based alignment 234
uses 299, 302 domain changes and 222–223
volatility 267 domain partitioning 234
web browsers 253 drawbacks 235
microservices 169 intermodule communication 238
defined 336 maintainability 234
versus EDA 378–380 maintaining modularity 227–229
event-driven microservices 382–383, 389 modularity fragility 235
microservices architecture 12 namespaces 224
analysis 423 operational characteristics 235

446 index

<a id='p483'></a>
<!-- Página 483 -->

```
the index
partitioning by technical concerns 219 partitioning 169, 180
performance 234 microkernel architecture 251, 266
planning stages 286–287 modular monolithic architecture 219, 234
reasons to use 222–223 modules 219
reuse in 235 technically partitioned teams 333
star ratings 236 performance 6, 54
testability 234 EDAs 384
uses 298, 301 EDA versus microservices 378
```

monolithic architecture 47, 169, 172, 180, 208 orchestration and 327
deployment models 174–175 Persistence layer 189, 193
layered 286–287, 296, 300
```
physical architecture
```

analysis 296
microkernel architecture 256, 274 components 127
modular 298, 301. See modular monolithic architecture diagramming 290–291, 416
analysis 296 distributed 255
relevance 178 pros and cons 274
smartphone as 173 embedded/mobile 199–200
```
versus logical architecture 127–128, 157
```

monolithic databases 333, 370–371, 389
```
tiered 199–200
```

MVC (Model-View-Controller) pattern 188–189, 193, 198
```
physical bounded context

```

N EDA versus microservices 378
```
microservices 308–309, 336
```

namespaces 192 planning architecture 280
modular monolithic architecture 224 architectural characteristics 281–283
non-domain design 46 architectural decisions 281
```
architectural style 281
```

nonfunctional requirements 43, 58
```
logical components 281
```

notifications stakeholders input 292
trade-off analysis 88 plugins
Two Many Sneakers 83 as components 256

O calling 259
```
communication 259, 267
```

operational architectural characteristics 54 contracts 264
```
design 270
```

orchestration 326–327, 336
```
distributed 257
```

outages 429 encapsulated 257
overengineering 48 implementing 256
```
sharing between 267
```

P portability 53
```
Presentation layer 189, 193
```

packages 192
```
priorities 64
```

partitioned architecture
domain-partitioned 170–171 privacy 55
technically partitioned 170–171 process architectural characteristics 52
```
you are here� 447
```


<a id='p484'></a>
<!-- Página 484 -->

the index
proof-of-concept code 429 Second Law of Software Architecture 96, 114
Proposed status (ADRs) 100 security 53, 55


## Q

```
implicit characteristic 50
queues and 90
service granularity, microservices versus EDA 379
```

queues 86. See also messages; topics
infrastructure and 108 shared code, granularity and 314–317
security and 90 shared libraries 322, 336, 343
trade-off analysis 88–91 code sharing 321


## R

```
shared services 322, 336, 343
code reuse 320
```

RDD (resume-driven development) 48 single-purpose 307

recoverability 54 smartphone as monolith 173
choreography and 329 soft skills for architects 432–433
reliability/safety 54 solutions versus requirements 62
request for comment (RFC) 100 source code repository 124–125
request processing 380 SQL (Structured Query Language) joins 233
requirements stakeholders
documents 42, 278, 282, 304–305, 404 planning stages and 292
interpreting/translating 66 requirements documents 42
non-functional 43 standardization, characteristics and 48
versus solutions 62 state management, choreography and 329
resume-driven development (RDD) 48
```
strategic decisions 19–21
```

return on investment (ROI) 92
```
structural architectural characteristics 53
```

RFC (request for comment) 100
```
structural design
```

roadmap for planning 281 domain considerations 46
robustness 54, 56, 74 internal 50
ROI (return on investment) 92 non-domain considerations 46
```
Superseded status (ADRs) 101
```

S synchronous calls, EDAs 385

scalability 4, 6, 54, 56, 74 synchronous communication
```
choreography 329 architecture style selection and 412
EDAs 384 versus asynchronous communication 362–366
layered architecture 205 benefits 367
microservices and 313, 332 system functionality 11
orchestration and 327 system quality attributes 58




```

448 index

<a id='p485'></a>
<!-- Página 485 -->

```
the index

```


## T U

tactical decisions 19–21 UML (Unified Modeling Language) class diagram 16
technical debt, coding architect and 429 unknown unknowns 85
technical depth of knowledge 437 usability 55
technically-partitioned architecture 170–171, 180 user interface. See also MVC (Model-View-Controller)
testability 4, 52 pattern
```
EDAs 385 diagramming 290
layered architecture 205 field arrangement 22
microservices architecture 332 integration 282
modular monoliths 234 microkernel architecture 262
public-facing 248
```

three-tier architectures 199
```
requests and 191
```

tightly coupled systems 150 scalability and 60
topics 86. See also events; messages; queues UI layer 193


## V

trade-off analysis 89
topologies
```
databases 389 version-control system 111
database-per-service 374–375
domain-partitioned 372–373
monolithic 370–371 W
```

trade-off analysis whiteboards 95, 104
```
architectural decisions 114
wikis 111
ATAM (Architecture Tradeoff Analysis Method) 92
EDA (event-driven architecture) 385 workflow
First Law of Software Architecture 90 amount 333
layered architecture 205 analysis 279
microkernel architecture 267 granularity and 314–317
microservices architecture 333 management 324–325
modular monolithic architecture 235 orchestration and 327
queues 88–91 workflow approach to logical architecture 132, 154
selections and 87 actor/action approach and 137
topics 89 Workflow layer 189, 193
```

translating/interpreting requirements 66
two-tier architectures 199




```
you are here� 449
```


<a id='p486'></a>
<!-- Página 486 -->

Learn from experts.
Become one yourself.
Books | Live online courses
Instant answers | Virtual events
Videos | Interactive learning

Get started at oreilly.com.



```
©2023 O’Reilly Media, Inc. O’Reilly is a registered trademark of O’Reilly Media, Inc. 175_8 x 9.25
```