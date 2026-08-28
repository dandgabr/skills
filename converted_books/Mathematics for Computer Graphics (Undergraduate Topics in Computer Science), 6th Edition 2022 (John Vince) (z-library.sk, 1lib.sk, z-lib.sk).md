# Mathematics for Computer Graphics (Undergraduate Topics in Computer Science), 6th Edition 2022 (John Vince) (z-library.sk, 1lib.sk, z-lib.sk)

> Documento convertido de PDF para Markdown para referência de skills.


<a id='p1'></a>
<!-- Página 1 -->


<a id='p2'></a>
<!-- Página 2 -->

Undergraduate Topics in Computer
Science


Series Editor
Ian Mackie, University of Sussex, Brighton, UK

Advisory Editors
Samson Abramsky , Department of Computer Science, University of Oxford,
Oxford, UK
Chris Hankin , Department of Computing, Imperial College London, London, UK
Mike Hinchey , Lero – The Irish Software Research Centre, University of
Limerick, Limerick, Ireland
Dexter C. Kozen, Department of Computer Science, Cornell University, Ithaca,

## NY, USA

Andrew Pitts , Department of Computer Science and Technology, University of
Cambridge, Cambridge, UK
Hanne Riis Nielson , Department of Applied Mathematics and Computer Science,
Technical University of Denmark, Kongens Lyngby, Denmark
Steven S. Skiena, Department of Computer Science, Stony Brook University, Stony
Brook, NY, USA
Iain Stewart , Department of Computer Science, Durham University, Durham,

## UK


<a id='p3'></a>
<!-- Página 3 -->

‘Undergraduate Topics in Computer Science’ (UTiCS) delivers high-quality
instructional content for undergraduates studying in all areas of computing and
information science. From core foundational and theoretical material to final-year
topics and applications, UTiCS books take a fresh, concise, and modern approach
and are ideal for self-study or for a one- or two-semester course. The texts are all
authored by established experts in their fields, reviewed by an international advisory
board, and contain numerous examples and problems, many of which include fully
worked solutions.
The UTiCS concept relies on high-quality, concise books in softback format, and
generally a maximum of 275–300 pages. For undergraduate textbooks that are
likely to be longer, more expository, Springer continues to offer the highly regarded
Texts in Computer Science series, to which we refer potential authors.


More information about this series at https://link.springer.com/bookseries/7592

<a id='p4'></a>
<!-- Página 4 -->

John Vince




Mathematics for Computer
Graphics
Sixth Edition

<a id='p5'></a>
<!-- Página 5 -->

John Vince
Breinton, UK




ISSN 1863-7310 ISSN 2197-1781 (electronic)
Undergraduate Topics in Computer Science
ISBN 978-1-4471-7519-3 ISBN 978-1-4471-7520-9 (eBook)
https://doi.org/10.1007/978-1-4471-7520-9

1st –5th editions: © Springer-Verlag London Ltd. 2001, 2006, 2010, 2014, 2017
6th edition: © Springer-Verlag London Ltd., part of Springer Nature 2022
The author(s) has/have asserted their right(s) to be identified as the author(s) of this work in accordance
with the Copyright, Designs and Patents Act 1988.
This work is subject to copyright. All rights are reserved by the Publisher, whether the whole or part of
the material is concerned, specifically the rights of translation, reprinting, reuse of illustrations, recitation,
broadcasting, reproduction on microfilms or in any other physical way, and transmission or information
storage and retrieval, electronic adaptation, computer software, or by similar or dissimilar methodology
now known or hereafter developed.
The use of general descriptive names, registered names, trademarks, service marks, etc. in this publication
does not imply, even in the absence of a specific statement, that such names are exempt from the relevant
protective laws and regulations and therefore free for general use.
The publisher, the authors and the editors are safe to assume that the advice and information in this book
are believed to be true and accurate at the date of publication. Neither the publisher nor the authors or
the editors give a warranty, expressed or implied, with respect to the material contained herein or for any
errors or omissions that may have been made. The publisher remains neutral with regard to jurisdictional
claims in published maps and institutional affiliations.

This Springer imprint is published by the registered company Springer-Verlag London Ltd. part of Springer
Nature.
The registered company address is: The Campus, 4 Crinan Street, London, N1 9XW, United Kingdom

<a id='p6'></a>
<!-- Página 6 -->

This book is dedicated to my wife, Heidi.

<a id='p7'></a>
<!-- Página 7 -->

Preface




The first edition of this book began life as part of Springer’s Essential series and
contained ten chapters and approximately 220 pages. This sixth and last edition has
twenty chapters and approximately 600 pages. Over the intervening editions, I have
revised and extended previous descriptions and introduced new chapters on subjects
that I believe are relevant to computer graphics, such as differential calculus and
interpolation, and new subjects that I had to learn about, such as quaternions and
geometric algebra. Hopefully, this edition explores enough mathematical ideas to
satisfy most people working in computer graphics.
```
Although the first edition of this book was produced on a humble PC using WORD,
```

subsequent editions were produced on an Apple iMac using LATEX. I recommend to
any budding authors that they should learn LATEX and use Springer’s templates to
create their first manuscript. Furthermore, today’s computers are so fast that I often
compile the entire book for the sake of changing a single character—it only takes 5
or 6 seconds!
```
I have used colour in the text to emphasise the patterns behind certain numbers
```

and in the illustrations to clarify the mathematics.
```
It is extremely difficult to ensure that there are no spelling mistakes, missing
```

brackets, spurious punctuation marks and, above all, mathematical errors. I truly
have done my best to correct the text and associated equations, but if I have missed
some, then I apologise now.
```
In all of my books, I try to mention the names of important mathematicians
```

associated with an invention or discovery and the period over which they were alive.
In this book, I mention 50 such people, and the relevant dates are attached to the first
citation.
```
Whilst writing this book I have borne in mind what it was like for me when I
```

was studying different areas of mathematics for the first time. In spite of reading and
rereading an explanation several times, it could take days before ‘the penny dropped’
and a concept became apparent. Hopefully, the reader will find the following explanations useful in developing their understanding of these specific areas of mathematics
and enjoy the sound of various pennies dropping!



```
vii
```


<a id='p8'></a>
<!-- Página 8 -->

viii Preface

I would like to thank Helen Desmond, Editor for Computer Science, for allowing
me to give up holidays and hobbies in order to complete another book!

Breinton, UK John Vince
May 2022

<a id='p9'></a>
<!-- Página 9 -->

Contents




1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
```
1.1 Mathematics for Computer Graphics . . . . . . . . . . . . . . . . . . . . . . . 1
1.2 Understanding Mathematics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.3 What Makes Mathematics Difficult? . . . . . . . . . . . . . . . . . . . . . . . 2
1.4 Background to This Book . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.5 How to Use This Book . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.6 Symbols and Notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
```

2 Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
```
2.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.2 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.3 Counting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.4 Sets of Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2.5 Zero . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.6 Negative Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.6.1 The Arithmetic of Positive and Negative
Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2.7 Observations and Axioms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2.7.1 Commutative Law . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2.7.2 Associative Law . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2.7.3 Distributive Law . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2.8 The Base of a Number System . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2.8.1 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2.8.2 Octal Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.8.3 Binary Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
2.8.4 Hexadecimal Numbers . . . . . . . . . . . . . . . . . . . . . . . . . 13
2.8.5 Adding Binary Numbers . . . . . . . . . . . . . . . . . . . . . . . . 16
2.8.6 Subtracting Binary Numbers . . . . . . . . . . . . . . . . . . . . 18




ix
```


<a id='p10'></a>
<!-- Página 10 -->

x Contents

```
2.9 Types of Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
2.9.1 Natural Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
2.9.2 Integers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
2.9.3 Rational Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
2.9.4 Irrational Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
2.9.5 Real Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
2.9.6 Algebraic and Transcendental Numbers . . . . . . . . . . . 20
2.9.7 Imaginary Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
2.9.8 Complex Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
2.9.9 Transcendental and Algebraic Numbers . . . . . . . . . . . 26
2.9.10 Infinity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
2.10 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
2.11 Worked Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
2.11.1 Algebraic Expansion . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
2.11.2 Binary Subtraction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
2.11.3 Complex Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
2.11.4 Complex Rotation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
```

3 Algebra . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
```
3.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
3.2 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
3.2.1 Solving the Roots of a Quadratic Equation . . . . . . . . 33
3.3 Indices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
3.3.1 Laws of Indices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
3.4 Logarithms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
3.5 Further Notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
3.6 Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
3.6.1 Explicit and Implicit Equations . . . . . . . . . . . . . . . . . . 41
3.6.2 Function Notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
3.6.3 Intervals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
3.6.4 Function Domains and Ranges . . . . . . . . . . . . . . . . . . 43
3.6.5 Odd and Even Functions . . . . . . . . . . . . . . . . . . . . . . . . 44
3.6.6 Power Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
3.7 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
3.8 Worked Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
3.8.1 Algebraic Manipulation . . . . . . . . . . . . . . . . . . . . . . . . 46
3.8.2 Solving a Quadratic Equation . . . . . . . . . . . . . . . . . . . 47
3.8.3 Factorising . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
```

4 Trigonometry . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
```
4.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
4.2 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
4.3 Units of Angular Measurement . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
```


<a id='p11'></a>
<!-- Página 11 -->

Contents xi

```
4.4 The Trigonometric Ratios . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
4.4.1 Domains and Ranges . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
4.5 Inverse Trigonometric Ratios . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
4.6 Trigonometric Identities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
4.7 The Sine Rule . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
4.8 The Cosine Rule . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
4.9 Compound-Angle Identities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
4.9.1 Double-Angle Identities . . . . . . . . . . . . . . . . . . . . . . . . 61
4.9.2 Multiple-Angle Identities . . . . . . . . . . . . . . . . . . . . . . . 62
4.9.3 Half-Angle Identities . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
4.10 Perimeter Relationships . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
4.11 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
```

5 Coordinate Systems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
```
5.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
5.2 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
5.3 The Cartesian Plane . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
5.4 Function Graphs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
5.5 Shape Representation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
5.5.1 2D Polygons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
5.5.2 Area of a Shape . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
5.6 Theorem of Pythagoras in 2D . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
5.7 3D Cartesian Coordinates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
5.7.1 Theorem of Pythagoras in 3D . . . . . . . . . . . . . . . . . . . 70
5.8 Polar Coordinates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70
5.9 Spherical Polar Coordinates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
5.10 Cylindrical Coordinates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72
5.11 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73
5.12 Worked Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73
5.12.1 Area of a Shape . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73
5.12.2 Distance Between Two Points . . . . . . . . . . . . . . . . . . . 73
5.12.3 Polar Coordinates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74
5.12.4 Spherical Polar Coordinates . . . . . . . . . . . . . . . . . . . . . 74
5.12.5 Cylindrical Coordinates . . . . . . . . . . . . . . . . . . . . . . . . 75
Reference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
```

6 Determinants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
```
6.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
6.2 Linear Equations with Two Variables . . . . . . . . . . . . . . . . . . . . . . . 78
6.3 Linear Equations with Three Variables . . . . . . . . . . . . . . . . . . . . . 81
6.3.1 Sarrus’s Rule . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
6.4 Mathematical Notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
6.4.1 Matrix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
6.4.2 Order of a Determinant . . . . . . . . . . . . . . . . . . . . . . . . . 89
```


<a id='p12'></a>
<!-- Página 12 -->

xii Contents

```
6.4.3 Value of a Determinant . . . . . . . . . . . . . . . . . . . . . . . . . 89
6.4.4 Properties of Determinants . . . . . . . . . . . . . . . . . . . . . . 91
6.5 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91
6.6 Worked Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92
6.6.1 Determinant Expansion . . . . . . . . . . . . . . . . . . . . . . . . . 92
6.6.2 Complex Determinant . . . . . . . . . . . . . . . . . . . . . . . . . . 92
6.6.3 Simple Expansion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
6.6.4 Simultaneous Equations . . . . . . . . . . . . . . . . . . . . . . . . 93
```

7 Vectors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
```
7.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
7.2 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
7.3 2D Vectors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96
7.3.1 Vector Notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96
7.3.2 Graphical Representation of Vectors . . . . . . . . . . . . . . 97
7.3.3 Magnitude of a Vector . . . . . . . . . . . . . . . . . . . . . . . . . . 98
7.4 3D Vectors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99
7.4.1 Vector Manipulation . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
7.4.2 Scaling a Vector . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
7.4.3 Vector Addition and Subtraction . . . . . . . . . . . . . . . . . 101
7.4.4 Position Vectors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
7.4.5 Unit Vectors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
7.4.6 Cartesian Vectors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
7.4.7 Products . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
7.4.8 Scalar Product . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
7.4.9 The Dot Product in Lighting Calculations . . . . . . . . . 105
7.4.10 The Scalar Product in Back-Face Detection . . . . . . . . 106
7.4.11 The Vector Product . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
7.4.12 The Right-Hand Rule . . . . . . . . . . . . . . . . . . . . . . . . . . 112
7.5 Deriving a Unit Normal Vector for a Triangle . . . . . . . . . . . . . . . 112
7.6 Surface Areas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113
7.6.1 Calculating 2D Areas . . . . . . . . . . . . . . . . . . . . . . . . . . 114
7.7 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
7.8 Worked Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
7.8.1 Position Vector . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
7.8.2 Unit Vector . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
7.8.3 Vector Magnitude . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
7.8.4 Angle Between Two Vectors . . . . . . . . . . . . . . . . . . . . 116
7.8.5 Vector Product . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
```

8 Matrix Algebra . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119
```
8.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119
8.2 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119
```


<a id='p13'></a>
<!-- Página 13 -->

Contents xiii

```
8.3 Matrix Notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
8.3.1 Matrix Dimension or Order . . . . . . . . . . . . . . . . . . . . . 122
8.3.2 Square Matrix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
8.3.3 Column Vector . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
8.3.4 Row Vector . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
8.3.5 Null Matrix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
8.3.6 Unit Matrix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
8.3.7 Trace . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
8.3.8 Determinant of a Matrix . . . . . . . . . . . . . . . . . . . . . . . . 125
8.3.9 Transpose . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
8.3.10 Symmetric Matrix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126
8.3.11 Antisymmetric Matrix . . . . . . . . . . . . . . . . . . . . . . . . . . 128
8.4 Matrix Addition and Subtraction . . . . . . . . . . . . . . . . . . . . . . . . . . 130
8.4.1 Scalar Multiplication . . . . . . . . . . . . . . . . . . . . . . . . . . . 130
8.5 Matrix Products . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130
8.5.1 Row and Column Vectors . . . . . . . . . . . . . . . . . . . . . . . 131
8.5.2 Row Vector and a Matrix . . . . . . . . . . . . . . . . . . . . . . . 131
8.5.3 Matrix and a Column Vector . . . . . . . . . . . . . . . . . . . . 132
8.5.4 Square Matrices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133
8.5.5 Rectangular Matrices . . . . . . . . . . . . . . . . . . . . . . . . . . 134
8.6 Inverse Matrix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134
8.6.1 Inverting a Pair of Matrices . . . . . . . . . . . . . . . . . . . . . 141
8.7 Orthogonal Matrix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141
8.8 Diagonal Matrix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
8.9 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143
8.10 Worked Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143
8.10.1 Matrix Inversion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143
8.10.2 Identity Matrix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144
8.10.3 Solving Two Equations Using Matrices . . . . . . . . . . . 144
8.10.4 Solving Three Equations Using Matrices . . . . . . . . . . 145
8.10.5 Solving Two Complex Equations . . . . . . . . . . . . . . . . 146
8.10.6 Solving Three Complex Equations . . . . . . . . . . . . . . . 147
8.10.7 Solving Two Complex Equations . . . . . . . . . . . . . . . . 148
8.10.8 Solving Three Complex Equations . . . . . . . . . . . . . . . 149
```

9 Complex Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151
```
9.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151
9.2 Definition of a Complex Number . . . . . . . . . . . . . . . . . . . . . . . . . . 151
9.2.1 Addition and Subtraction of Complex Numbers . . . . 152
9.2.2 Multiplying a Complex Number by a Scalar . . . . . . . 153
9.2.3 Product of Complex Numbers . . . . . . . . . . . . . . . . . . . 153
9.2.4 Square of a Complex Number . . . . . . . . . . . . . . . . . . . 154
9.2.5 Norm of a Complex Number . . . . . . . . . . . . . . . . . . . . 154
9.2.6 Complex Conjugate of a Complex Number . . . . . . . . 154
9.2.7 Quotient of Complex Numbers . . . . . . . . . . . . . . . . . . 155
```


<a id='p14'></a>
<!-- Página 14 -->

xiv Contents

```
9.2.8 Inverse of a Complex Number . . . . . . . . . . . . . . . . . . . 156
9.2.9 Square-Root of ±i . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156
9.3 Ordered Pairs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158
9.3.1 Addition and Subtraction of Ordered Pairs . . . . . . . . 158
9.3.2 Multiplying an Ordered Pair by a Scalar . . . . . . . . . . 159
9.3.3 Product of Ordered Pairs . . . . . . . . . . . . . . . . . . . . . . . 159
9.3.4 Square of an Ordered Pair . . . . . . . . . . . . . . . . . . . . . . 160
9.3.5 Norm of an Ordered Pair . . . . . . . . . . . . . . . . . . . . . . . 161
9.3.6 Complex Conjugate of an Ordered Pair . . . . . . . . . . . 161
9.3.7 Quotient of an Ordered Pair . . . . . . . . . . . . . . . . . . . . . 161
9.3.8 Inverse of an Ordered Pair . . . . . . . . . . . . . . . . . . . . . . 162
9.3.9 Square-Root of ±i . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163
9.4 Matrix Representation of a Complex Number . . . . . . . . . . . . . . . 164
9.4.1 Adding and Subtracting Complex Numbers . . . . . . . 165
9.4.2 Product of Two Complex Numbers . . . . . . . . . . . . . . . 166
9.4.3 Norm Squared of a Complex Number . . . . . . . . . . . . 166
9.4.4 Complex Conjugate of a Complex Number . . . . . . . . 167
9.4.5 Inverse of a Complex Number . . . . . . . . . . . . . . . . . . . 167
9.4.6 Quotient of a Complex Number . . . . . . . . . . . . . . . . . . 168
9.4.7 Square-Root of ±i . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 169
9.5 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170
9.6 Worked Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170
9.6.1 Adding and Subtracting Complex Numbers . . . . . . . 170
9.6.2 Product of Complex Numbers . . . . . . . . . . . . . . . . . . . 171
9.6.3 Multiplying a Complex Number by i . . . . . . . . . . . . . 172
9.6.4 The Norm of a Complex Number . . . . . . . . . . . . . . . . 173
9.6.5 The Complex Conjugate of a Complex Number . . . . 173
9.6.6 The Quotient of Two Complex Numbers . . . . . . . . . . 174
9.6.7 Divide a Complex Number by i . . . . . . . . . . . . . . . . . . 175
9.6.8 Divide a Complex Number by −i . . . . . . . . . . . . . . . . 176
9.6.9 The Inverse of a Complex Number . . . . . . . . . . . . . . . 177
9.6.10 The Inverse of i . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 178
9.6.11 The Inverse of −i . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 178
Reference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 179
```

10 Geometric Transforms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 181
10.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 181
10.2 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 181
10.3 2D Transforms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 182
```
10.3.1 Translation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 182
10.3.2 Scaling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 182
10.3.3 Reflection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 183
```

10.4 Transforms as Matrices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 184
```
10.4.1 Systems of Notation . . . . . . . . . . . . . . . . . . . . . . . . . . . 184
```


<a id='p15'></a>
<!-- Página 15 -->

Contents xv

```
10.5 Homogeneous Coordinates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 184
10.5.1 2D Translation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 186
10.5.2 2D Scaling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 186
10.5.3 2D Reflections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 187
10.5.4 2D Shearing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 189
10.5.5 2D Rotation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 190
10.5.6 2D Scaling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 192
10.5.7 2D Reflection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 193
10.5.8 2D Rotation About an Arbitrary Point . . . . . . . . . . . . 194
10.6 3D Transforms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 194
10.6.1 3D Translation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 195
10.6.2 3D Scaling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 195
10.6.3 3D Rotation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 196
10.6.4 Gimbal Lock . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 199
10.6.5 Rotating About an Axis . . . . . . . . . . . . . . . . . . . . . . . . 200
10.6.6 3D Reflections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 202
10.7 Change of Axes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 202
10.7.1 2D Change of Axes . . . . . . . . . . . . . . . . . . . . . . . . . . . . 202
10.7.2 Direction Cosines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 204
10.7.3 3D Change of Axes . . . . . . . . . . . . . . . . . . . . . . . . . . . . 205
10.8 Positioning the Virtual Camera . . . . . . . . . . . . . . . . . . . . . . . . . . . . 205
10.8.1 Direction Cosines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 206
10.8.2 Euler Angles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 208
10.9 Rotating a Point About an Arbitrary Axis . . . . . . . . . . . . . . . . . . . 211
10.9.1 Matrices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 211
10.10 Transforming Vectors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 218
10.11 Determinants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 220
10.12 Perspective Projection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 222
10.13 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 224
10.14 Worked Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 224
10.14.1 2D Scaling Transform . . . . . . . . . . . . . . . . . . . . . . . . . . 224
10.14.2 2D Scale and Translate . . . . . . . . . . . . . . . . . . . . . . . . . 224
10.14.3 3D Scaling Transform . . . . . . . . . . . . . . . . . . . . . . . . . . 225
10.14.4 2D Rotation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 225
10.14.5 2D Rotation About a Point . . . . . . . . . . . . . . . . . . . . . . 226
10.14.6 Determinant of the Rotate Transform . . . . . . . . . . . . . 227
10.14.7 Determinant of the Shear Transform . . . . . . . . . . . . . . 227
10.14.8 Yaw, Pitch and Roll Transforms . . . . . . . . . . . . . . . . . 227
10.14.9 3D Rotation About an Axis . . . . . . . . . . . . . . . . . . . . . 228
10.14.10 3D Rotation Transform Matrix . . . . . . . . . . . . . . . . . . 228
10.14.11 2D Change of Axes . . . . . . . . . . . . . . . . . . . . . . . . . . . . 229
10.14.12 3D Change of Axes . . . . . . . . . . . . . . . . . . . . . . . . . . . . 230
10.14.13 Rotate a Point About an Axis . . . . . . . . . . . . . . . . . . . . 231
10.14.14 Perspective Projection . . . . . . . . . . . . . . . . . . . . . . . . . . 232
```


<a id='p16'></a>
<!-- Página 16 -->

xvi Contents

11 Quaternion Algebra . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 233
11.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 233
11.2 Some History . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 233
11.3 Defining a Quaternion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 237
```
11.3.1 The Quaternion Units . . . . . . . . . . . . . . . . . . . . . . . . . . 239
11.3.2 Example of Quaternion Products . . . . . . . . . . . . . . . . . 241
```

11.4 Algebraic Definition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 241
11.5 Adding and Subtracting Quaternions . . . . . . . . . . . . . . . . . . . . . . . 241
11.6 Real Quaternion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 242
11.7 Multiplying a Quaternion by a Scalar . . . . . . . . . . . . . . . . . . . . . . 242
11.8 Pure Quaternion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 243
11.9 Unit Quaternion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 244
11.10 Additive Form of a Quaternion . . . . . . . . . . . . . . . . . . . . . . . . . . . . 245
11.11 Binary Form of a Quaternion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 245
11.12 The Complex Conjugate of a Quaternion . . . . . . . . . . . . . . . . . . . 246
11.13 Norm of a Quaternion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 247
11.14 Normalised Quaternion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 248
11.15 Quaternion Products . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 248
```
11.15.1 Product of Pure Quaternions . . . . . . . . . . . . . . . . . . . . 249
11.15.2 Product of Unit-Norm Quaternions . . . . . . . . . . . . . . . 249
11.15.3 Square of a Quaternion . . . . . . . . . . . . . . . . . . . . . . . . . 250
11.15.4 Norm of the Quaternion Product . . . . . . . . . . . . . . . . . 251
```

11.16 Inverse Quaternion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 252
11.17 Matrices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 253
```
11.17.1 Orthogonal Matrix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 254
```

11.18 Quaternion Algebra . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 254
11.19 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 255
```
11.19.1 Summary of Definitions . . . . . . . . . . . . . . . . . . . . . . . . 255
```

11.20 Worked Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 256
```
11.20.1 Adding and Subtracting Quaternions . . . . . . . . . . . . . 256
11.20.2 Norm of a Quaternion . . . . . . . . . . . . . . . . . . . . . . . . . . 257
11.20.3 Unit-norm Quaternions . . . . . . . . . . . . . . . . . . . . . . . . . 257
11.20.4 Quaternion Product . . . . . . . . . . . . . . . . . . . . . . . . . . . . 257
11.20.5 Square of a Quaternion . . . . . . . . . . . . . . . . . . . . . . . . . 258
11.20.6 Inverse of a Quaternion . . . . . . . . . . . . . . . . . . . . . . . . . 258
```

References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 258
12 Quaternions in Space . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 261
12.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 261
12.2 Some History . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 261
12.3 Quaternion Products . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 261
```
12.3.1 Special Case . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 263
12.3.2 General Case . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 266
12.3.3 Double Angle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 268
```


<a id='p17'></a>
<!-- Página 17 -->

Contents xvii

```
12.4 Quaternions in Matrix Form . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 271
12.4.1 Vector Method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 272
12.4.2 Geometric Verification . . . . . . . . . . . . . . . . . . . . . . . . . 274
12.5 Multiple Rotations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 276
12.6 Rotating About an Off-Set Axis . . . . . . . . . . . . . . . . . . . . . . . . . . . 277
12.7 Converting a Rotation Matrix to a Quaternion . . . . . . . . . . . . . . . 279
12.8 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 280
12.8.1 Summary of Definitions . . . . . . . . . . . . . . . . . . . . . . . . 281
12.9 Worked Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 281
12.9.1 Special Case Quaternion . . . . . . . . . . . . . . . . . . . . . . . . 281
12.9.2 Rotating a Vector Using a Quaternion . . . . . . . . . . . . 282
12.9.3 Evaluate qpq −1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 282
12.9.4 Evaluate qpq −1 Using a Matrix . . . . . . . . . . . . . . . . . . 282
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 283
```

13 Interpolation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 285
13.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 285
13.2 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 285
13.3 Linear Interpolation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 286
13.4 Non-Linear Interpolation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 288
```
13.4.1 Trigonometric Interpolation . . . . . . . . . . . . . . . . . . . . . 288
13.4.2 Cubic Interpolation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 289
```

13.5 Interpolating Vectors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 294
13.6 Interpolating Quaternions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 297
13.7 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 299
14 Curves and Patches . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 301
14.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 301
14.2 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 301
14.3 The Circle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 302
14.4 The Ellipse . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 302
14.5 Bézier Curves . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 303
```
14.5.1 Bernstein Polynomials . . . . . . . . . . . . . . . . . . . . . . . . . 303
14.5.2 Quadratic Bézier Curves . . . . . . . . . . . . . . . . . . . . . . . . 306
14.5.3 Cubic Bernstein Polynomials . . . . . . . . . . . . . . . . . . . . 307
```

14.6 A Recursive Bézier Formula . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 310
14.7 Bézier Curves Using Matrices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 311
```
14.7.1 Linear Interpolation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 312
```

14.8 B-Splines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 315
```
14.8.1 Uniform B-Splines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 315
14.8.2 Continuity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 317
14.8.3 Non-uniform B-Splines . . . . . . . . . . . . . . . . . . . . . . . . . 318
14.8.4 Non-uniform Rational B-Splines . . . . . . . . . . . . . . . . . 319
```


<a id='p18'></a>
<!-- Página 18 -->

xviii Contents

```
14.9 Surface Patches . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 319
14.9.1 Planar Surface Patch . . . . . . . . . . . . . . . . . . . . . . . . . . . 319
14.9.2 Quadratic Bézier Surface Patch . . . . . . . . . . . . . . . . . . 320
14.9.3 Cubic Bézier Surface Patch . . . . . . . . . . . . . . . . . . . . . 322
14.10 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 324
```

15 Analytic Geometry . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 325
15.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 325
15.2 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 325
```
15.2.1 Angles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 325
15.2.2 Intercept Theorems . . . . . . . . . . . . . . . . . . . . . . . . . . . . 326
15.2.3 Golden Section . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 327
15.2.4 Triangles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 327
15.2.5 Centre of Gravity of a Triangle . . . . . . . . . . . . . . . . . . 328
15.2.6 Isosceles Triangle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 328
15.2.7 Equilateral Triangle . . . . . . . . . . . . . . . . . . . . . . . . . . . . 329
15.2.8 Right Triangle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 329
15.2.9 Theorem of Thales . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 329
15.2.10 Theorem of Pythagoras . . . . . . . . . . . . . . . . . . . . . . . . . 329
15.2.11 Quadrilateral . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 330
15.2.12 Trapezoid . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 330
15.2.13 Parallelogram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 331
15.2.14 Rhombus . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 331
15.2.15 Regular Polygon . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 332
15.2.16 Circle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 332
```

15.3 2D Analytic Geometry . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 334
```
15.3.1 Equation of a Straight Line . . . . . . . . . . . . . . . . . . . . . 334
15.3.2 The Hessian Normal Form . . . . . . . . . . . . . . . . . . . . . . 335
15.3.3 Space Partitioning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 337
15.3.4 The Hessian Normal Form from Two Points . . . . . . . 337
```

15.4 Intersection Points . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 338
```
15.4.1 Intersecting Straight Lines . . . . . . . . . . . . . . . . . . . . . . 338
15.4.2 Intersecting Line Segments . . . . . . . . . . . . . . . . . . . . . 339
```

15.5 Point Inside a Triangle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 341
```
15.5.1 Area of a Triangle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 341
15.5.2 Hessian Normal Form . . . . . . . . . . . . . . . . . . . . . . . . . . 343
```

15.6 Intersection of a Circle with a Straight Line . . . . . . . . . . . . . . . . . 345
15.7 3D Geometry . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 347
```
15.7.1 Equation of a Straight Line . . . . . . . . . . . . . . . . . . . . . 347
15.7.2 Intersecting Two Straight Lines . . . . . . . . . . . . . . . . . . 348
```

15.8 Equation of a Plane . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 351
```
15.8.1 Cartesian Form of the Plane Equation . . . . . . . . . . . . 351
15.8.2 General Form of the Plane Equation . . . . . . . . . . . . . . 353
15.8.3 Parametric Form of the Plane Equation . . . . . . . . . . . 354
```


<a id='p19'></a>
<!-- Página 19 -->

Contents xix

```
15.8.4
Converting from the Parametric to the General
Form . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 355
15.8.5 Plane Equation from Three Points . . . . . . . . . . . . . . . . 357
15.9 Intersecting Planes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 359
15.9.1 Intersection of Three Planes . . . . . . . . . . . . . . . . . . . . . 363
15.9.2 Angle Between Two Planes . . . . . . . . . . . . . . . . . . . . . 365
15.9.3 Angle Between a Line and a Plane . . . . . . . . . . . . . . . 366
15.9.4 Intersection of a Line with a Plane . . . . . . . . . . . . . . . 368
15.10 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 370
```

16 Barycentric Coordinates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 371
16.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 371
16.2 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 371
16.3 Ceva’s Theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 372
16.4 Ratios and Proportion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 373
16.5 Mass Points . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 374
16.6 Linear Interpolation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 380
16.7 Convex Hull Property . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 387
16.8 Areas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 387
16.9 Volumes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 396
16.10 Bézier Curves and Patches . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 398
16.11 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 399
Reference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 399
17 Geometric Algebra . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 401
17.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 401
17.2 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 401
17.3 Symmetric and Antisymmetric Functions . . . . . . . . . . . . . . . . . . . 402
17.4 Trigonometric Foundations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 403
17.5 Vectorial Foundations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 405
17.6 Inner and Outer Products . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 405
17.7 The Geometric Product in 2D . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 407
17.8 The Geometric Product in 3D . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 409
17.9 The Outer Product of Three 3D Vectors . . . . . . . . . . . . . . . . . . . . 411
17.10 Axioms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 412
17.11 Notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 413
17.12 Grades, Pseudoscalars and Multivectors . . . . . . . . . . . . . . . . . . . . 413
17.13 Redefining the Inner and Outer Products . . . . . . . . . . . . . . . . . . . . 415
17.14 The Inverse of a Vector . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 415
17.15 The Imaginary Properties of the Outer Product . . . . . . . . . . . . . . 417
17.16 Duality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 419
17.17 The Relationship Between the Vector Product
```
and the Outer Product . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 420
```

17.18 The Relationship Between Quaternions and Bivectors . . . . . . . . 421

<a id='p20'></a>
<!-- Página 20 -->

xx Contents

```
17.19 Reflections and Rotations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 422
17.19.1 2D Reflections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 422
17.19.2 3D Reflections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 423
17.19.3 2D Rotations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 424
17.20 Rotors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 426
17.21 Applied Geometric Algebra . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 429
17.22 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 435
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 435
```

18 Calculus: Derivatives . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 437
18.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 437
18.2 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 437
18.3 Small Numerical Quantities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 437
18.4 Equations and Limits . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 439
```
18.4.1 Quadratic Function . . . . . . . . . . . . . . . . . . . . . . . . . . . . 439
18.4.2 Cubic Equation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 440
18.4.3 Functions and Limits . . . . . . . . . . . . . . . . . . . . . . . . . . . 442
18.4.4 Graphical Interpretation of the Derivative . . . . . . . . . 444
18.4.5 Derivatives and Differentials . . . . . . . . . . . . . . . . . . . . 445
18.4.6 Integration and Antiderivatives . . . . . . . . . . . . . . . . . . 445
```

18.5 Function Types . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 447
18.6 Differentiating Groups of Functions . . . . . . . . . . . . . . . . . . . . . . . . 448
```
18.6.1 Sums of Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 448
18.6.2 Function of a Function . . . . . . . . . . . . . . . . . . . . . . . . . 450
18.6.3 Function Products . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 454
18.6.4 Function Quotients . . . . . . . . . . . . . . . . . . . . . . . . . . . . 458
```

18.7 Differentiating Implicit Functions . . . . . . . . . . . . . . . . . . . . . . . . . 460
18.8 Differentiating Exponential and Logarithmic Functions . . . . . . . 463
```
18.8.1 Exponential Functions . . . . . . . . . . . . . . . . . . . . . . . . . 463
18.8.2 Logarithmic Functions . . . . . . . . . . . . . . . . . . . . . . . . . 465
```

18.9 Differentiating Trigonometric Functions . . . . . . . . . . . . . . . . . . . . 467
```
18.9.1 Differentiating tan . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 467
18.9.2 Differentiating csc . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 468
18.9.3 Differentiating sec . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 469
18.9.4 Differentiating cot . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 470
18.9.5 Differentiating arcsin, arccos and arctan . . . . . . . . . . 470
18.9.6 Differentiating arccsc, arcsec and arccot . . . . . . . . . . 471
```

18.10 Differentiating Hyperbolic Functions . . . . . . . . . . . . . . . . . . . . . . . 472
```
18.10.1 Differentiating sinh, cosh and tanh . . . . . . . . . . . . . . . 474
```

18.11 Higher Derivatives . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 475
18.12 Higher Derivatives of a Polynomial . . . . . . . . . . . . . . . . . . . . . . . . 475
18.13 Identifying a Local Maximum or Minimum . . . . . . . . . . . . . . . . . 477

<a id='p21'></a>
<!-- Página 21 -->

Contents xxi

```
18.14 Partial Derivatives . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 480
18.14.1 Visualising Partial Derivatives . . . . . . . . . . . . . . . . . . . 483
18.14.2 Mixed Partial Derivatives . . . . . . . . . . . . . . . . . . . . . . . 485
18.15 Chain Rule . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 486
18.16 Total Derivative . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 488
18.17 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 489
Reference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 490
```

19 Calculus: Integration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 491
19.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 491
19.2 Indefinite Integral . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 491
19.3 Integration Techniques . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 492
```
19.3.1 Continuous Functions . . . . . . . . . . . . . . . . . . . . . . . . . . 492
19.3.2 Difficult Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 493
19.3.3 Trigonometric Identities . . . . . . . . . . . . . . . . . . . . . . . . 493
19.3.4 Exponent Notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 495
19.3.5 Completing the Square . . . . . . . . . . . . . . . . . . . . . . . . . 497
19.3.6 The Integrand Contains a Derivative . . . . . . . . . . . . . . 498
19.3.7 Converting the Integrand into a Series
of Fractions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 500
19.3.8 Integration by Parts . . . . . . . . . . . . . . . . . . . . . . . . . . . . 501
19.3.9 Integration by Substitution . . . . . . . . . . . . . . . . . . . . . . 505
19.3.10 Partial Fractions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 510
```

19.4 Area Under a Graph . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 512
19.5 Calculating Areas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 513
19.6 Positive and Negative Areas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 521
19.7 Area Between Two Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 523
19.8 Areas with the y-Axis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 524
19.9 Area with Parametric Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . 525
19.10 The Riemann Sum . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 527
19.11 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 529
20 Worked Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 531
20.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 531
20.2 Area of Regular Polygon . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 531
20.3 Area of Any Polygon . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 532
20.4 Dihedral Angle of a Dodecahedron . . . . . . . . . . . . . . . . . . . . . . . . 533
20.5 Vector Normal to a Triangle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 534
20.6 Area of a Triangle Using Vectors . . . . . . . . . . . . . . . . . . . . . . . . . . 535
20.7 General Form of the Line Equation from Two Points . . . . . . . . . 535
20.8 Angle Between Two Straight Lines . . . . . . . . . . . . . . . . . . . . . . . . 536
20.9 Test if Three Points Lie on a Straight Line . . . . . . . . . . . . . . . . . . 537
20.10 Position and Distance of the Nearest Point on a Line
```
to a Point . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 538
```


<a id='p22'></a>
<!-- Página 22 -->

xxii Contents

```
20.11 Position of a Point Reflected in a Line . . . . . . . . . . . . . . . . . . . . . . 540
20.12 Intersection of a Line and a Sphere . . . . . . . . . . . . . . . . . . . . . . . . 543
20.13 Sphere Touching a Plane . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 547
20.14 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 549

```

Appendix A: Limit of (sin θ )/θ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 551
Appendix B: Integrating cosn θ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 555
Index . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 557

<a id='p23'></a>
<!-- Página 23 -->


## Chapter 1

Introduction




1.1 Mathematics for Computer Graphics

Computer graphics contains many areas of specialism such as data visualisation, computer animation, film special effects, computer games and virtual reality. Fortunately,
not everyone working in computer graphics requires a knowledge of mathematics,
but those that do, often look for a book that introduces them to some basic ideas
of mathematics, without turning them into mathematicians. This is the objective of
this book. Over the following chapters I introduce the reader to some useful mathematical topics that will help them understand the software they work with, and how
to solve a wide variety of geometric and algebraic problems. These topics include
numbers systems, algebra, trigonometry, 2D and 3D geometry, vectors, equations,
matrices, complex numbers, determinants, transforms, quaternions, interpolation,
curves, patches and calculus. I have written about some of these topics to a greater
level of detail in other books, which you may be interested in exploring.



1.2 Understanding Mathematics

One of the problems with mathematics is its incredible breadth and depth. It embraces
everything from geometry, calculus, topology, statistics, complex functions to number theory and propositional calculus. All of these subjects can be studied superficially or to a mind-numbing complexity. Fortunately, no one is required to understand
everything, which is why mathematicians tend to specialise in one or two areas and
develop a specialist knowledge. If it’s any comfort, even Einstein asked friends and
colleagues to explain branches of mathematics to help him with his theories.




© Springer-Verlag London Ltd., part of Springer Nature 2022 1
J. Vince, Mathematics for Computer Graphics, Undergraduate Topics
in Computer Science, https://doi.org/10.1007/978-1-4471-7520-9_1

<a id='p24'></a>
<!-- Página 24 -->

2 1 Introduction

1.3 What Makes Mathematics Difficult?

‘What makes mathematics difficult?’ is a difficult question to answer, but one that
has to be asked and answered. There are many answers to this question, and I believe
that problems begin with mathematical notation and how to read it; how to analyse
a problem and express a solution using mathematical statements. Unlike learning a
foreign language—which I find very difficult—mathematics is a language that needs
to be learned by discovering facts and building upon them to discover new facts.
Consequently, a good memory is always an advantage, as well as a sense of logic.
Mathematics can √ be difficult for anyone, including mathematicians. For example,
when the idea of −1 was originally proposed, it was criticised and looked down
upon by mathematicians, mainly because its purpose was not fully understood. Eventually, it transformed the entire mathematical landscape, including physics. Similarly,
when the German mathematician Georg Cantor (1845–1919), published his papers
on set theory and transfinite sets, some mathematicians hounded him in a disgraceful
manner. The German mathematician Leopold Kronecker (1823–1891), called Cantor
a ‘scientific charlatan’, a ‘renegade’, and a ‘corrupter of youth’, and did everything
to hinder Cantor’s academic career [1]. Similarly, the French mathematician and
physicist Henri Poincaré (1854–1912), called Cantor’s ideas a ‘grave disease’ [2],
whilst the Austrian-British philosopher and logician Ludwig Wittgenstein (1889–
1951), complained that mathematics is ‘ridden through and through with the pernicious idioms of set theory’ [3]. How wrong they all were. Today, set theory is a
major branch of mathematics and has found its way into every math curriculum. So
don’t be surprised to discover that some mathematical ideas are initially difficult to
understand—you are in good company.



1.4 Background to This Book

During my working life in computer animation I came across a wide range of students
with an equally wide range of mathematical knowledge. Some students possessed a
rudimentary background in mathematics, while others had been taught calculus and
supporting subjects. Teaching such a cohort the mathematics of computer graphics
was a challenge, to say the least, but somehow I did. By the end of a three-year
undergraduate course they were competent programmers and could program a wide
variety of mathematical techniques. The first-edition of this book employed much of
my teaching material and has been revised and extended.



1.5 How to Use This Book

Initially, I’d recommend to any reader to start at the beginning and start reading
chapters on subjects with which they are familiar. One never knows what may be

<a id='p25'></a>
<!-- Página 25 -->

1.5 How to Use This Book 3

learnt from reading about a familiar subject by a non-mathematician. For those
readers with a good background in mathematics, should quick read chapters on
topics covered else-where, and settle down on new topics. However you approach
this book, I sincerely hope that you discover something new that increases your
knowledge of the subject.



1.6 Symbols and Notation

One of the reasons why many people find mathematics inaccessible is due to its
symbols and notation. Let’s look at symbols first. The English alphabet possesses a
reasonable range of familiar character shapes:

```
a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z
```


## A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z


which find their way into every branch of mathematics and physics, and permit us
to write equations such as
```
E = mc2

```

and
```
A = πr 2 .

```

It is important that when we see an equation, we are able to read it as part of the
text. In the case of E = mc2 , this is read as ‘E equals m, c squared’, where E stands
for energy, m for mass, c the speed of light, which is multiplied by itself. In the
case of A = πr 2 , this is read as ‘A equals pi, r squared’, where A stands for area, π
the ratio of a circle’s circumference to its diameter, and r the circle’s radius. Greek
symbols, which happen to look nice and impressive, have also found their way into
many equations, and often disrupt the flow of reading, simply because we don’t
know their English names. For example, the English theoretical physicist Paul Dirac
(1902–1984), derived an equation for a moving electron using the symbols αi and
β, which are 4 × 4 matrices, where

```
αi β + βαi = 0

```

and is read as

```
‘the sum of the products alpha-i beta, and beta alpha-i, equals zero.’
```

Although we do not come across moving electrons in this book, we do have to be
familiar with the following Greek symbols:
```
α alpha ν nu
β beta ξ xi
```


<a id='p26'></a>
<!-- Página 26 -->

4 1 Introduction

```
γ gamma o omicron
δ delta π pi
epsilon ρ rho
ζ zeta σ sigma
η eta τ tau
θ theta υ upsilon
ι iota φ phi
κ kappa χ chi
λ lambda ψ psi
μ mu ω omega
```

and some upper-case symbols:
```
Γ Gamma  Sigma
Δ Delta ϒ Upsilon
Θ Theta  Phi
Λ Lambda Psi
Ξ Xi Omega
Π Pi
```

Being able to read an equation does not mean that we understand it—but we are a
little closer than just being able to stare at a jumble of symbols! Therefore, in future,
when I introduce a new mathematical object, I will tell you how it should be read.



References

1. Dauben JW (1979) Georg Cantor his mathematics and philosophy of the infinite. Princeton
University Press, Princeton
2. Dauben JW (2004) Georg Cantor and the battle for transfinite set theory (PDF). In: Proceedings
of the 9th ACMS conference (Westmont College, Santa Barbara, Calif.), pp 1–22
3. Rodych V (2007) Wittgenstein’s philosophy of mathematics. In: Zalta EN (ed) The Stanford
encyclopedia of philosophy. Metaphysics Research Lab, Stanford University

<a id='p27'></a>
<!-- Página 27 -->


## Chapter 2

Numbers




2.1 Introduction

This chapter revises some basic ideas about counting and number systems, and how
they are employed in the context of mathematics for computer graphics. Omit this
chapter, if you are familiar with the subject.



2.2 Background

Over the centuries mathematicians have realised that in order to progress, they must
give precise definitions to their discoveries, ideas and concepts, so that they can
be built upon and referenced by new mathematical inventions. In the event of any
new discovery, these rrrdefinitions have to be occasionally changed or extended. For
example, once upon a time integers, rational and irrational numbers, satisfied all the
needs of mathematicians, until imaginary quantities were invented. Today, complex
numbers have helped shape the current number system hierarchy. Consequently,
there must be clear definitions for numbers, and the operators that act upon them.
Therefore, we need to identify the types of numbers that exist, what they are used
for, and any problems that arise when they are stored in a computer.



2.3 Counting

Our brain’s visual cortex possesses some incredible image processing features. For
example, children know instinctively when they are given less sweets than another
child, and adults know instinctively when they are short-changed by a Parisian taxi
driver, or driven around the Arc de Triumph several times, on the way to the airport!
Intuitively, we can assess how many donkeys are in a field without counting them,

© Springer-Verlag London Ltd., part of Springer Nature 2022 5
J. Vince, Mathematics for Computer Graphics, Undergraduate Topics
in Computer Science, https://doi.org/10.1007/978-1-4471-7520-9_2

<a id='p28'></a>
<!-- Página 28 -->

6 2 Numbers

and generally, we seem to know within a second or two, whether there are just a few,
dozens, or hundreds of something. But when accuracy is required, one can’t beat
counting. But what is counting?
Well normally, we are taught to count by our parents by memorising first, the
counting words ‘one, two, three, four, five, six, seven, eight, nine, ten, ..’ and second,
associating them with our fingers, so that when asked to count the number of donkeys
in a picture book, each donkey is associated with a counting word. When each
donkey has been identified, the number of donkeys equals the last word mentioned.
However, this still assumes that we know the meaning of ‘one, two, three, four, ..’
etc. Memorising these counting words is only part of the problem—getting them in
the correct sequence is the real challenge. The incorrect sequence ‘one, two, five,
three, nine, four, ..’ etc., introduces an element of randomness into any calculation,
but practice makes perfect, and it’s useful to master the correct sequence before going
to university!



2.4 Sets of Numbers

A set is a collection of arbitrary objects called its elements or members. For example,
each system of number belongs to a set with given a name, such as N for the natural
numbers, R for real numbers, and Q for rational numbers. When we want to indicate
that something is whole, real or rational, etc., we use the notation:

```
n∈N

```

which reads ‘n is a member of (∈) the set N’, i.e. n is a whole number. Similarly:

```
x ∈R

```

stands for ‘x is a real number.’
A well-ordered set possesses a unique order, such as the natural numbers N.
Therefore, if P is the well-ordered set of prime numbers and N is the well-ordered
set of natural numbers, we can write:


## P = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, . . .}


## N = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, . . .}.


```
By pairing the prime numbers in P with the numbers in N, we have:

{{2, 1}, {3, 2}, {5, 3}, {7, 4}, {11, 5}, {13, 6}, {17, 7}, {19, 8}, {23, 9}, . . .}

```

and we can reason that 2 is the 1st prime, and 3 is the 2nd prime, etc. However, we
still have to declare what we mean by 1, 2, 3, 4, 5, . . . etc., and without getting too
philosophical, I like the idea of defining them as follows. The word ‘one’, represented

<a id='p29'></a>
<!-- Página 29 -->

2.4 Sets of Numbers 7

by 1, stands for ‘oneness’ of anything: one finger, one house, one tree, one donkey,
etc. The word ‘two’, represented by 2, is ‘one more than one’. The word ‘three’,
represented by 3, is ‘one more than two’, and so on.
We are now in a position to associate some mathematical notation with our numbers by introducing the + and = signs. We know that + means add, but it also can
stand for ‘more’. We also know that = means equal, and it can also stand for ‘is the
same as’. Thus the statement:
```
2=1+1

```

is read as ‘two is the same as one more than one.’
```
We can also write:
3=1+2

```

which is read as ‘three is the same as one more than two.’ But as we already have a
definition for 2, we can write

```
3=1+2
= 1 + 1 + 1.

```

Developing this idea, and including some extra combinations, we have:

```
2=1+1
3=1+2
4=1+3=2+2
5=1+4=2+3
6=1+5=2+4=3+3
7=1+6=2+5=3+4
etc.

```

and can be continued without limit. These numbers, 1, 2, 3, 4, 5, 6, etc., are called
natural numbers, and are the set N.



2.5 Zero

The concept of zero has a well-documented history, which shows that it has been used
by different cultures over a period of two-thousand years or more. It was the Indian
mathematician and astronomer Brahmagupta (598-c.–670), who argued that zero
was just as valid as any natural number, with the definition: the result of subtracting
any number from itself. However, even today, there is no universal agreement as to
whether zero belongs to the set N, consequently, the set N0 stands for the set of
natural numbers including zero.

<a id='p30'></a>
<!-- Página 30 -->

8 2 Numbers

In today’s positional decimal system, which is a place value system, the digit
0 is a placeholder. For example, 203 stands for: two hundreds, no tens and three
units. Although 0 ∈ N0 , it does have special properties that distinguish it from other
members of the set, and Brahmagupta also gave rules showing this interaction.
If x ∈ N0 , then the following rules apply:

```
addition: x + 0 = x
subtraction: x − 0 = x
multiplication: x × 0 = 0 × x = 0
division: 0/x = 0
undefined division: x/0.

```

The expression 0/0 is called an indeterminate form, as it is possible to show that
under different conditions, especially limiting conditions, it can equal anything. So
for the moment, we will avoid using it until we cover calculus.



2.6 Negative Numbers

When negative numbers were first proposed, they were not accepted with open arms,
as it was difficult to visualise −5 of something. For instance, if there are 5 donkeys
in a field, and they are all stolen to make salami, the field is now empty, and there
is nothing we can do in the arithmetic of donkeys to create a field of −5 donkeys.
However, in applied mathematics, numbers have to represent all sorts of quantities
such as temperature, displacement, angular rotation, speed, acceleration, etc., and
we also need to incorporate ideas such as left and right, up and down, before and
after, forwards and backwards, etc. Fortunately, negative numbers are perfect for
representing all of the above quantities and ideas.
Consider the expression 4 − x, where x ∈ N0 . When x takes on certain values,
we have

```
4−1=3
4−2=2
4−3=1
4−4=0

```

and unless we introduce negative numbers, we are unable to express the result of
4 − 5. Consequently, negative numbers are visualised as shown in Fig. 2.1, where
the number line shows negative numbers to the left of the natural numbers, which
are positive, although the + sign is omitted for clarity.
Moving from left to right, the number line provides a numerical continuum
```
from large negative numbers, through zero, towards large positive numbers. In any
```


<a id='p31'></a>
<!-- Página 31 -->

2.6 Negative Numbers 9


```
-6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6

```

Fig. 2.1 The number line showing negative and positive numbers



calculations, we could agree that angles above the horizon are positive, and angles
below the horizon, negative. Similarly, a movement forwards is positive, and a movement backwards is negative. So now we are able to write:

```
4 − 5 = −1
4 − 6 = −2
4 − 7 = −3
etc.,

```

without worrying about creating impossible conditions.



2.6.1 The Arithmetic of Positive and Negative Numbers

Once again, Brahmagupta compiled all the rules, Tables 2.1 and 2.2, supporting the
addition, subtraction, multiplication and division of positive and negative numbers.
The real fly in the ointment, being negative numbers, which cause problems for
children, math teachers and occasional accidents for mathematicians. Perhaps, the
one rule we all remember from our school days is that two negatives make a positive.
Another problem with negative numbers arises when we employ the square-root
function. As the product of two positive or negative numbers results in a positive
result, the square-root of √a positive number gives rise to a positive and a negative answer. For example, 4 = ±2. This means that the square-root function only
applies to positive numbers. Nevertheless, it did not stop the invention of the imaginary object i, where i 2 = −1. However, i is not a number, but behaves like an
operator, and is described later.

Table 2.1 Rules for adding and subtracting positive and negative numbers
+ b −b − b −b
a a+b a−b a a−b a+b
−a b−a −(a + b) −a −(a + b) b−a



Table 2.2 Rules for multiplying and dividing positive and negative numbers
× b −b / b −b
a ab −ab a a/b −a/b
−a −ab ab −a −a/b a/b

<a id='p32'></a>
<!-- Página 32 -->

10 2 Numbers

2.7 Observations and Axioms

The following axioms or laws provide a formal basis for mathematics, and in
the following descriptions a binary operation is an arithmetic operation such as
+, −, ×, / which operate on two operands.



2.7.1 Commutative Law

The commutative law in algebra states that when two elements are linked through
some binary operation, the result is independent of the order of the elements.

The commutative law of addition is

```
a+b =b+a
e.g. 1 + 2 = 2 + 1.

```

The commutative law of multiplication is

```
a×b =b×a
e.g. 1 × 2 = 2 × 1.

```

Note that subtraction is not commutative:

```
a − b = b − a
e.g. 1 − 2 = 2 − 1.



```

2.7.2 Associative Law

The associative law in algebra states that when three or more elements are linked
together through a binary operation, the result is independent of how each pair of
elements is grouped.

The associative law of addition is

```
a + (b + c) = (a + b) + c
e.g. 1 + (2 + 3) = (1 + 2) + 3.

```

The associative law of multiplication is

```
a × (b × c) = (a × b) × c
```


<a id='p33'></a>
<!-- Página 33 -->

2.7 Observations and Axioms 11

```
e.g. 1 × (2 × 3) = (1 × 2) × 3.

```

However, note that subtraction is not associative:

```
a − (b − c) = (a − b) − c
e.g. 1 − (2 − 3) = (1 − 2) − 3,

```

which may seem surprising, but at the same time confirms the need for clear axioms.



2.7.3 Distributive Law

The distributive law in algebra describes an operation, which when performed on a
combination of elements is the same as performing the operation on the individual
elements. The distributive law does not work in all cases of arithmetic. For example,
multiplication over addition holds:

```
a(b + c) = ab + ac
e.g. 2(3 + 4) = 6 + 8

```

whereas addition over multiplication does not:

```
a + (b × c) = (a + b) × (a + c)
e.g. 3 + (4 × 5) = (3 + 4) × (3 + 5).

```

Although these laws are natural for numbers, they do not necessarily apply to all
mathematical objects. For instance, the vector product, which multiplies two vectors
together, is not commutative. The same applies for matrix multiplication.



2.8 The Base of a Number System

2.8.1 Background

Over recent millennia, mankind has invented and discarded many systems for representing number. People have counted on their fingers and toes, used pictures (hieroglyphics), cut marks on clay tablets (cuneiform symbols), employed Greek symbols
(Ionic system) and struggled with, and abandoned Roman numerals (I, V, X, L, C,
D, M, etc.), until we reach today’s decimal place system, which has Hindu-Arabic
and Chinese origins. And since the invention of computers we have witnessed the
emergence of binary, octal and hexadecimal number systems, where 2, 8 and 16
respectively, replace the 10 in our decimal system.

<a id='p34'></a>
<!-- Página 34 -->

12 2 Numbers

The decimal number 23 stands for ‘two tens and three units’, and in English
is written ‘twenty-three’, in French ‘vingt-trois’ (twenty-three), and in German
‘dreiundzwanzig’ (three and twenty). Let’s investigate the algebra behind the decimal
system and see how it can be used to represent numbers to any base. The expression:

```
a × 1000 + b × 100 + c × 10 + d × 1

```

where a, b, c, d take on any value between 0 and 9, describes any whole number
between 0 and 9999. By including

```
e × 0.1 + f × 0.01 + g × 0.001 + h × 0.0001

```

where e, f, g, h take on any value between 0 and 9, any decimal number between
0 and 9999.9999 can be represented.
Indices bring the notation alive and reveal the true underlying pattern:

```
. . . a103 + b102 + c101 + d100 + e10−1 + f 10−2 + g10−3 + h10−4 . . . .

```

Remember that any number raised to the power 0 equals 1. By adding extra terms
both left and right, any number can be accommodated.
In this example, 10 is the base, which means that the values of a to h range between
0 and 9, 1 less than the base. Therefore, by substituting B for the base we have

```
. . . a B 3 + bB 2 + cB 1 + d B 0 + eB −1 + f B −2 + g B −3 + h B −4 . . .

```

where the values of a to h range between 0 and B − 1.



2.8.2 Octal Numbers

The octal number system has B = 8, and a to h range between 0 and 7:

```
. . . a83 + b82 + c81 + d80 + e8−1 + f 8−2 + g8−3 + h8−4 . . .

```

and the first 17 octal numbers are:

```
18 , 28 , 38 , 48 , 58 , 68 , 78 , 108 , 118 , 128 , 138 , 148 , 158 , 168 , 178 , 208 , 218 .

```

The subscript 8 reminds us that although we may continue to use the words ‘twentyone’, it is an octal number, and not a decimal. But what is 148 in decimal? Well, it
stands for:
```
1 × 81 + 4 × 80 = 12.

```

Thus 356.48 is converted to decimal as follows:

<a id='p35'></a>
<!-- Página 35 -->

2.8 The Base of a Number System 13

```
(3 × 82 ) + (5 × 81 ) + (6 × 80 ) + (4 × 8−1 )
(3 × 64) + (5 × 8) + (6 × 1) + (4 × 0.125)
(192 + 40 + 6) + (0.5)
238.5.

```

Counting in octal appears difficult, simply because we have never been exposed to
it, like the decimal system. If we had evolved with 8 fingers, instead of 10, we would
be counting in octal!



2.8.3 Binary Numbers

The binary number system has B = 2, and a to h are 0 or 1:

```
. . . a23 + b22 + c21 + d20 + e2−1 + f 2−2 + g2−3 + h2−4 . . .

```

and the first 13 binary numbers are:

12 , 102 , 112 , 1002 , 1012 , 1102 , 1112 , 10002 , 10012 , 10102 , 10112 , 11002 , 11012 .

Thus 11011.112 is converted to decimal as follows:
             
1 × 24 + 1 × 23 + 0 × 22 + 1 × 21 + 1 × 20 + 1 × 2−1 + 1 × 2−2
```
(1 × 16) + (1 × 8) + (0 × 4) + (1 × 2) + (1 × 0.5) + (1 × 0.25)
(16 + 8 + 2) + (0.5 + 0.25)
26.75.

```

The reason why computers work with binary numbers—rather than decimal—is due
to the difficulty of designing electrical circuits that can store decimal numbers in
a stable fashion. A switch, where the open state represents 0, and the closed state
represents 1, is the simplest electrical component to emulate. No matter how often
it is used, or how old it becomes, it will always behave like a switch. The main
advantage of electrical circuits is that they can be switched on and off trillions of
times a second, and the only disadvantage is that the encoded binary numbers and
characters contain a large number of bits, and humans are not familiar with binary.



2.8.4 Hexadecimal Numbers

The hexadecimal number system has B = 16, and a to h can be 0 to 15, which presents
a slight problem, as we don’t have 15 different numerical characters. Consequently,
we use 0 to 9, and the letters A, B, C, D, E, F to represent 10, 11, 12, 13, 14, 15
respectively:

<a id='p36'></a>
<!-- Página 36 -->

14 2 Numbers

```
. . . a163 + b162 + c161 + d160 + e16−1 + f 16−2 + g16−3 + h16−4 . . .

```

and the first 17 hexadecimal numbers are:

116 , 216 , 316 , 416 , 516 , 616 , 716 , 816 , 916 , A16 , B16 , C16 , D16 , E 16 , F16 , 1016 , 1116 .

Thus 1E.816 is converted to decimal as follows:


## (1 × 16) + (E × 1) + (8 × 16−1 )

```
(16 + 14) + (8/16)
30.5.

```

Although it is not obvious, binary, octal and hexadecimal numbers are closely related,
which is why they are part of a programmer’s toolkit. Even though computers work
with binary, it’s the last thing a programmer wants to use. So to simplify the manmachine interface, binary is converted into octal or hexadecimal. To illustrate this,
let’s convert the 16-bit binary code 1101011000110001 into octal.
```
Using the following general binary integer

a28 + b27 + c26 + d25 + e24 + f 23 + g22 + h21 + i20

```

we group the terms into threes, starting from the right, because 23 = 8:
```
 8     
a2 + b27 + c26 + d25 + e24 + f 23 + g22 + h21 + i20 .

```

Simplifying:
```
     
26 a22 + b21 + c20 + 23 d22 + e21 + f 20 + 20 g22 + h21 + i20
     
82 a22 + b21 + c21 + 81 d22 + e21 + f 20 + 80 g22 + h21 + i20
```


## 82 R + 81 S + 80 T


where

```
R = a22 + b21 + c
S = d22 + e21 + f
T = g22 + h21 + i

```

and the values of R, S, T vary between 0 and 7. Therefore, given 1101011000
110001, we divide the binary code into groups of three, starting at the right, and
adding two leading zeros:

```
(001)(101)(011)(000)(110)(001).
```


<a id='p37'></a>
<!-- Página 37 -->

2.8 The Base of a Number System 15

For each group, multiply the zeros and ones by 4, 2, 1, right to left:

```
(0 + 0 + 1)(4 + 0 + 1)(0 + 2 + 1)(0 + 0 + 0)(4 + 2 + 0)(0 + 0 + 1)
(1)(5)(3)(0)(6)(1)
1530618 .

```

Therefore, 11010110001100012 ≡ 1530618 , (≡ stands for ‘equivalent to’) which
is much more compact. The secret of this technique is to memorise these patterns:

```
0002 ≡ 08
0012 ≡ 18
0102 ≡ 28
0112 ≡ 38
1002 ≡ 48
1012 ≡ 58
1102 ≡ 68
1112 ≡ 78 .

```

Here are a few more examples, with the binary digits grouped in threes:

```
1112 ≡ 78
101 1012 ≡ 558
100 0002 ≡ 408
111 000 111 000 1112 ≡ 707078 .

```

It’s just as easy to reverse the process, and convert octal into binary. Here are some
examples:

```
5678 ≡ 101 110 1112
238 ≡ 010 0112
17418 ≡ 001 111 100 0012 .

```

A similar technique is used to convert binary to hexadecimal, but this time we
divide the binary code into groups of four, because 24 = 16, starting at the right, and
adding leading zeros, if necessary. To illustrate this, let’s convert the 16-bit binary
code 1101 0110 0011 0001 into hexadecimal.
Using the following general binary integer number

a211 + b210 + c29 + d28 + e27 + f 26 + g25 + h24 + i23 + j22 + k21 + l20

```
from the right, we divide the binary code into groups of four:
```

     
a211 + b210 + c29 + d28 + e27 + f 26 + g25 + h24 + i23 + j22 + k21 + l20 .

<a id='p38'></a>
<!-- Página 38 -->

16 2 Numbers


Simplifying:
```
   3   
28 a23 + b22 + c21 + d20 + 24 e2
 + f 22 + g21 + h20 + 20 i23 + j22 + k21 + l20
162 a23 + b22 + c21 + d + 161 e23 + f 22 + g21 + h + 160 i23 + j22 + k21 + l
```


## 162 R + 161 S + 160 T


where

```
R = a23 + b22 + c21 + d
S = e23 + f 22 + g21 + h
T = i23 + j22 + k21 + l

```

and the values of R, S, T vary between 0 and 15. Therefore, given
11010110001100012 , we divide the binary code into groups of fours, starting at
the right:
```
(1101)(0110)(0011)(0001)

```

For each group, multiply the zeros and ones by 8, 4, 2, 1 respectively, right to left:

```
(8 + 4 + 0 + 1)(0 + 4 + 2 + 0)(0 + 0 + 2 + 1)(0 + 0 + 0 + 1)
(13)(6)(3)(1)
```


## D63116 .


Therefore, 1101 0110 0011 00012 ≡ D63116 , which is even more compact than its
octal value 1530618 .
I have deliberately used whole numbers in the above examples, but they can all be
extended to include a fractional part. For example, when converting a binary number
such as 11.11012 to octal, the groups are formed about the binary point:

```
(011).(110)(100) ≡ 3.648 .

```

Similarly, when converting a binary number such as 101010.1001102 to hexadecimal,
the groups are also formed about the binary point:


## (0010)(1010).(1001)(1000) ≡ 2 A.9816 .


Table 2.3 shows the first twenty decimal, binary, octal and hexadecimal numbers.



2.8.5 Adding Binary Numbers

When we are first taught the addition of integers containing several digits, we are
advised to solve the problem digit by digit, working from right to left. For example,
to add 254 to 561 we write:

<a id='p39'></a>
<!-- Página 39 -->

2.8 The Base of a Number System 17

Table 2.3 The first twenty decimal, binary, octal, and hexadecimal numbers
decimal binary octal hex decimal binary octal hex
1 1 1 1 11 1011 13 B
2 10 2 2 12 1100 14 C
3 11 3 3 13 1101 15 D
4 100 4 4 14 1110 16 E
5 101 5 5 15 1111 17 F
6 110 6 6 16 10000 20 10
7 111 7 7 17 10001 21 11
8 1000 10 8 18 10010 22 12
9 1001 11 9 19 10011 23 13
10 1010 12 A 20 10100 24 14



Table 2.4 Addition of two decimal integers showing the carr y
+ 0 1 2 3 4 5 6 7 8 9
0 0 1 2 3 4 5 6 7 8 9
1 1 2 3 4 5 6 7 8 9 10

2 2 3 4 5 6 7 8 9 10 11

3 3 4 5 6 7 8 9 10 11 12

4 4 5 6 7 8 9 10 11 12 13

5 5 6 7 8 9 10 11 12 13 14

6 6 7 8 9 10 11 12 13 14 15

7 7 8 9 10 11 12 13 14 15 16

8 8 9 10 11 12 13 14 15 16 17

9 9 10 11 12 13 14 15 16 17 18




Table 2.5 Addition of two binary integers showing the carr y
+ 0 1
0 0 1
1 1 10




```
561
254
815


```

where 4 + 1 = 5, 5 + 6 = 1 with a carr y = 1, 2 + 5 + carr y = 8.
```
Table 2.4 shows all the arrangements for adding two digits with the carr y shown
```

as carr y n. However, when adding binary numbers, the possible arrangements collapse
to the four shown in Table 2.5, which greatly simplifies the process.

<a id='p40'></a>
<!-- Página 40 -->

18 2 Numbers

For example, to add 124 to 188 as two 16-bit binary integers, we write, showing
the status of the carr y bit:

```
0000000011111000 carr y
0000000010111100 = 188
0000000001111100 = 124
0000000100111000 = 312


```

Such addition is easily undertaken by digital electronic circuits, and instead of having
separate circuitry for subtraction, it is possible to perform subtraction using the
technique of two’s complement.



2.8.6 Subtracting Binary Numbers

Two’s complement is a technique for converting a binary number into a form such
that when it is added to another binary number, it results in a subtraction. There are
two stages to the conversion: inversion, followed by the addition of 1. For example,
24 in binary is 0000000000110000, and is inverted by switching every 1 to 0, and
vice versa: 1111111111100111. Next, we add 1: 1111111111101000, which now
represents −24. If this is added to binary 36: 0000000000100100, we have

```
0000000000100100 = +36
1111111111101000 = −24
0000000000001100 = +12


```

Note that the last high-order addition creates a carr y of 1, which is ignored. Here is
another example, 100 − 30:

```
0000000000011110 = +30
inversion 1111111111100001
add 1 0000000000000001
1111111111100010 = −30
add 100 0000000001100100 = +100
0000000001000110 = +70




```

2.9 Types of Numbers

As mathematics evolved, mathematicians introduced different types of numbers to
help classify equations and simplify the language employed to describe their work.
These are the various types and their set names.

<a id='p41'></a>
<!-- Página 41 -->

2.9 Types of Numbers 19

2.9.1 Natural Numbers

The natural numbers {1, 2, 3, 4, . . .} are used for counting, ordering and labelling
and represented by the set N. When zero is included, N0 or N0 is used:


## N0 = N0 = {0, 1, 2, . . .}.


Note that negative numbers are not included. Natural numbers are used to subscript
a quantity to distinguish one element from another, e.g. x1 , x2 , x3 , x4 , . . ..



2.9.2 Integers

Integer numbers include the natural numbers, both positive and negative, and zero,
and are represented by the set Z:


## Z = {. . . , −2, −1, 0, 1, 2, 3, . . .}.


The reason for using Z is because the German for whole number is ganzen Zahlen.
Leopold Kronecker apparently criticised Georg Cantor for his work on set theory
with the jibe: ‘Die ganzen Zahlen hat der liebe Gott gemacht, alles andere ist Menschenwerk’, which translates: ‘God made the integers, and all the rest is man’s
work’, implying that the rest are artificial. However, Cantor’s work on set theory and
transfinite numbers proved to be far from artificial.



2.9.3 Rational Numbers

Any number that equals the quotient of one integer divided by another non-zero
```
√
```

integer, is a rational number, and represented by the set Q. For example, 2, 16,
0.25 are rational numbers because

```
2 = 4/2
√
16 = ±4 = ±8/2
0.25 = 1/4.

```

Some rational numbers can be stored accurately inside a computer, but many others
can only be stored approximately. For example, 4/3 produces an infinite sequence
of threes 1.333333 . . . and is truncated when stored as a binary number.

<a id='p42'></a>
<!-- Página 42 -->

20 2 Numbers

2.9.4 Irrational Numbers

An irrational number cannot be expressed as the quotient of two integers. Irrational
numbers never terminate, nor contain repeated sequences of digits, consequently, they
are always subject to a small error when stored within a computer. Examples are:
```
√
2 = 1.41421356 . . .
φ = 1.61803398 . . . (golden section)
e = 2.71828182 . . .
π = 3.14159265 . . .



```

2.9.5 Real Numbers

Rational and irrational numbers comprise the set of real numbers R. Examples are
1.5, 0.004, 12.999 and 23.0.



2.9.6 Algebraic and Transcendental Numbers

Polynomial equations with rational coefficients have the form:

```
f (x) = ax n + bx n−1 + cx n−2 . . . + C

```

such as
```
y = 3x 2 + 2x − 1

```

and their roots belong to the set of algebraic numbers A. A consequence of this
definition implies that all rational numbers are algebraic, since if
```
p
x=
q

```

then
```
qx − p = 0

```

which is a polynomial. Numbers that are not roots to polynomial equations
```
√ are
```

transcendental numbers and include most irrational numbers, but not 2, since if
```
√
x= 2

```

then

<a id='p43'></a>
<!-- Página 43 -->

2.9 Types of Numbers 21

```
x2 − 2 = 0

```

which is a polynomial.



2.9.7 Imaginary Numbers

Imaginary numbers were invented to resolve problems where an equation such as
x 2 + 16 = 0, has no real solution (roots). The simple idea of declaring the existence
of a quantity i, such that i 2 = −1, permits the solution to be expressed as

```
x = ±4i.

```

For example, if x = 4i we have

```
x 2 + 16 = 16i 2 + 16
= −16 + 16
=0

```

and if x = −4i we have

```
x 2 + 16 = 16i 2 + 16
= −16 + 16
= 0.

```

But what is i? In 1637, the French mathematician René Descartes (1596–1650), √
published La Géométrie, in which he stated that numbers incorporating −1 were
‘imaginary’, and for centuries this label has stuck. Unfortunately, it was a derogatory remark, as there is nothing ‘imaginary’ about i—it simply is an object that when
introduced into various algebraic expressions, reveals some amazing underlying patterns. i is not a number in the accepted sense, it is a mathematical object or construct
that squares to −1. In some respects it is like time, which probably does not really
exist, but is useful in describing the universe. However, i does lose its mystery when
interpreted as a rotational operator, which we investigate below.
As i 2 = −1 then it must be possible to raise i to other powers. For example,

```
i 4 = i 2i 2 = 1

```

and
```
i 5 = ii 4 = i.

```

Table 2.6 shows the sequence up to i 6 .

<a id='p44'></a>
<!-- Página 44 -->

22 2 Numbers

Table 2.6 Increasing powers of i
i0 i1 i2 i3 i4 i5 i6
1 i −1 −i 1 i −1



```
Imaginary

5i

4i

3i
2i
1i


-5 -4 -3 -2 -1 0 1 2 3 4 5 Real
-1i

-2i

-3i
-4i

-5i



```

Fig. 2.2 The complex plane



```
This cyclic pattern is quite striking, and reminds one of a similar pattern:

(x, y, −x, −y, x, . . .)

```

that arises when rotating around the Cartesian axes in a anticlockwise direction.
Such a similarity cannot be ignored, for when the real number line is combined with
a vertical imaginary axis, it creates the complex plane, as shown in Fig. 2.2.
The above sequence is summarised as

```
i 4n = 1
i 4n+1 = i
i 4n+2 = −1
i 4n+3 = −i

```

where n ∈ N0 .
But what about negative powers? Well they, too, are also possible. Consider i −1 ,
which is evaluated as follows:
```
1 1(−i) −i
i −1 = = = = −i.
i i(−i) 1
```


<a id='p45'></a>
<!-- Página 45 -->

2.9 Types of Numbers 23

Table 2.7 Decreasing powers of i
i0 i −1 i −2 i −3 i −4 i −5 i −6
1 −i −1 i 1 −i −1

Similarly,
```
1 1
i −2 = = = −1
i2 −1

```

and
```
i −3 = i −1 i −2 = −i(−1) = i.

```

Table 2.7 shows the sequence down to i −6 .
This time the cyclic pattern is reversed and is similar to the pattern

```
(x, −y, −x, y, x, . . .)

```

that arises when rotating around the Cartesian axes in a clockwise direction.
Now let’s investigate how a real number behaves when it is repeatedly multiplied
by i. Starting with the number 3, we have:

```
i × 3 = 3i
i × 3i = −3
i × (−3) = −3i
i × (−3)i = 3.

```

So the cycle is (3, 3i, −3, −3i, 3, 3i, −3, −3i, 3, . . .), which has four steps, as
shown in Fig. 2.3.


Fig. 2.3 The cycle of points Imaginary
created by repeatedly
multiplying 3 by i 5i

```
4i
3i

2i

1i


-5 -4 -3 -2 -1 0 1 2 3 4 5 Real
-1i

-2i

-3i
-4i

-5i
```


<a id='p46'></a>
<!-- Página 46 -->

24 2 Numbers

Imaginary objects occur for all sorts of reasons. For example, consider the statements


## AB = −B A


## B A = −AB


where A and B are two undefined objects that obey the associative law, but not the
commutative law, and A2 = B 2 = 1. The operation (AB)2 reveals


## (AB)(AB) = A(B A)B


## = −A(AB)B


## = −(A2 )(B 2 )

```
= −1

```

which means that the product AB is imaginary. Such objects, which can be matrices,
are useful in describing the behaviour of sub-atomic particles.



2.9.8 Complex Numbers

A complex number has a real and imaginary part: z = a + ib, and represented by
the set C:

```
z = a + bi z ∈ C, a, b ∈ R, i 2 = −1.

```

Some examples are

```
z =1+i
z = 3 − 2i
√
z = −23 + 23i.

```

Complex numbers obey all the normal laws of algebra. For example, if we multiply
(a + bi) by (c + di) we have

```
(a + bi)(c + di) = ac + adi + bci + bdi 2 .

```

Collecting up like terms and substituting −1 for i 2 we get

```
(a + bi)(c + di) = ac + (ad + bc)i − bd

```

which simplifies to

<a id='p47'></a>
<!-- Página 47 -->

2.9 Types of Numbers 25

```
(a + bi)(c + di) = ac − bd + (ad + bc)i

```

which is another complex number.
Something interesting happens when we multiply a complex number by its complex conjugate, which is the same complex number but with the sign of the imaginary
part reversed:
```
(a + bi)(a − bi) = a 2 − abi + bai − b2 i 2 .

```

Collecting up like terms and simplifying we obtain

```
(a + bi)(a − bi) = a 2 + b2

```

which is a real number, as the imaginary part has been cancelled out by the action of
the complex conjugate.
Figure 2.4 shows how complex numbers are represented graphically using the
complex plane.
For example, the complex number P = 4 + 3i in Fig. 2.4 is rotated 90◦ to Q by
multiplying it by i. Let’s do this, and remember that i 2 = −1:

```
i(4 + 3i) = 4i + 3i 2
= 4i − 3
= −3 + 4i.

```

The point Q = −3 + 4i is rotated 90◦ to R by multiplying it by i:

```
i(−3 + 4i) = −3i + 4i 2
= −3i − 4
= −4 − 3i.


```

Fig. 2.4 The complex plane Imaginary
showing four complex
numbers 5i
```
Q 4i

3i P
2i

1i


-5 -4 -3 -2 -1 0 1 2 3 4 5 Real
-1i

-2i
-3i
```


## R

```
-4i
```


## S

```
-5i
```


<a id='p48'></a>
<!-- Página 48 -->

26 2 Numbers

The point R = −4 − 3i is rotated 90◦ to S by multiplying it by i:

```
i(−4 − 3i) = −4i − 3i 2
= −4i + 3
= 3 − 4i.

```

Finally, the point S = 3 − 4i is rotated 90◦ back to P by multiplying it by i:

```
i(3 − 4i) = 3i − 4i 2
= 3i + 4
= 4 + 3i.

As you can see, complex numbers are intimately related to Cartesian coordinates,
```

in that the ordered pair (x, y) ≡ (x + yi).



2.9.9 Transcendental and Algebraic Numbers

Given a polynomial built from integers, for example

```
y = 3x 3 − 4x 2 + x + 23,

```

if the result is an integer, it is called an algebraic number, otherwise it is a transcendental number. Familiar examples of the latter being π = 3.141 592 653 . . ., and
e = 2.718 281 828 . . ., which can be represented as various continued fractions:

```
4
π=
12
1+
32
2+
52
2+
72
2+
2 + ...

1
e =2+
1
1+
1
2+
1
1+
1
1+
4 + ...
```


<a id='p49'></a>
<!-- Página 49 -->

2.9 Types of Numbers 27

2.9.10 Infinity

The term infinity is used to describe the size of unbounded systems. For example,
there is no end to prime numbers: i.e. they are infinite; so, too, are the sets of other
numbers. Consequently, no matter how we try, it is impossible to visualise the size of
infinity. Nevertheless, this did not stop Georg Cantor from showing that one infinite
set could be infinitely larger than another.
```
Cantor distinguished between those infinite number sets that could be ‘counted’,
```

and those that could not. For Cantor, counting meant the one-to-one correspondence
of a natural number with the members of another infinite set. If there is a clear
correspondence, without leaving any gaps, then the two sets shared a common infinite
size, called its cardinality using the first letter of the Hebrew alphabet aleph: ℵ. The
cardinality of the natural numbers N is ℵ0 , called aleph-zero.
```
Cantor discovered a way of representing the rational numbers as a grid, which
```

is traversed diagonally, back and forth, as shown in Fig. 2.5. Some ratios appear
several times, such as 22 , 33 etc., which are not counted. Nevertheless, the one-toone correspondence with the natural numbers means that the cardinality of rational
numbers is also ℵ0 .
```
A real surprise was that there are infinitely more transcendental numbers than
```

natural numbers. Furthermore, there are an infinite number of cardinalities rising to
ℵℵ . Cantor had been alone working in this esoteric area, and as he published his
results, he shook the very foundations of mathematics, which is why he was treated
so badly by his fellow mathematicians.


Fig. 2.5 Rational number
```
1 1 1 1 1
```

grid
```
1 2 3 4 5
2 2 2 2 2
1
1 2 3 4 5
1
3 3 3 3 3
1 2 3 4 5
4 4 4 4 4
1 2 3 4 5
5 5 5 5 5
1 2 3 4 5
```


<a id='p50'></a>
<!-- Página 50 -->

28 2 Numbers

2.10 Summary

Apart from the natural numbers, integers, rational, irrational, prime, real and complex
numbers, there are also Fermat, Mersenne, amicable, chromic, cubic, Fibonacci,
pentagonal, perfect, random, square and tetrahedral numbers, which although equally
interesting, don’t concern us in this text.
Now that we know something about some important number sets, let’s revise
some ideas behind algebra.



2.11 Worked Examples

2.11.1 Algebraic Expansion

Expand (a + b)(c + d), (a − b)(c + d), and (a − b)(c − d).

```
(a + b)(c + d) = a(c + d) + b(c + d)
= ac + ad + bc + bd.
(a − b)(c + d) = a(c + d) − b(c + d)
= ac + ad − bc − bd.
(a − b)(c − d) = a(c − d) − b(c − d)
= ac − ad − bc + bd.



```

2.11.2 Binary Subtraction

Using two’s complement, subtract 12 from 50.

```
0000000000001100 = +12
inversion 1111111111110011
add 1 0000000000000001
1111111111110100 = −12
add 50 0000000000110010 = +50
0000000000100110 = +38




```

2.11.3 Complex Numbers

Compute (3 + 2i) + (2 + 2i) + (5 − 3i) and (3 + 2i)(2 + 2i)(5 − 3i).

<a id='p51'></a>
<!-- Página 51 -->

2.11 Worked Examples 29

```
(3 + 2i) + (2 + 2i) + (5 − 3i) = 10 + i.

(3 + 2i)(2 + 2i)(5 − 3i) = (3 + 2i)(10 − 6i + 10i + 6)
= (3 + 2i)(16 + 4i)
= 48 + 12i + 32i − 8
= 40 + 44i.



```

2.11.4 Complex Rotation

Rotate the complex point (3 + 2i) by ±90◦ and ±180◦ .
To rotate +90◦ (anticlockwise) multiply by i.

```
i(3 + 2i) = (3i − 2) = (−2 + 3i).

```

To rotate −90◦ (clockwise) multiply by −i.

```
−i(3 + 2i) = (−3i + 2) = (2 − 3i).

```

To rotate +180◦ (anticlockwise) multiply by −1.

```
−1(3 + 2i) = (−3 − 2i).

```

To rotate −180◦ (clockwise) multiply by −1.

```
−1(3 + 2i) = (−3 − 2i).
```


<a id='p52'></a>
<!-- Página 52 -->


## Chapter 3

Algebra




3.1 Introduction

Some people, including me, find learning a foreign language a real challenge; one
of the reasons being the inconsistent rules associated with its syntax. For example,
why is a table feminine in French, ‘la table’, and a bed masculine, ‘le lit’? They both
have four legs! The rules governing natural language are continuously being changed
by each generation, whereas mathematics appears to be logical and consistent. The
reason for this consistency is due to the rules associated with numbers and the way
they are combined together and manipulated at an abstract level. Such rules, or
axioms, generally make our life easy, however, as we saw with the invention of
negative numbers, extra rules have to be introduced, such as ‘two negatives make
a positive’, which is easily remembered. However, as we explore mathematics, we
discover all sorts of inconsistencies, such as there is no real value associated with
the square-root of a negative number. It’s forbidden to divide a number by zero. Zero
divided by zero gives inconsistent results. Nevertheless, such conditions are easy
to recognise and avoided. At least in mathematics, we don’t have to worry about
masculine and feminine numbers!
As a student, I discovered Principia Mathematica [1], a three-volume work written
by the British philosopher, logician, mathematician and historian Bertrand Russell
(1872–1970), and the British mathematician and philosopher Alfred North Whitehead (1861–1947), in which the authors attempt to deduce all of mathematics using
the axiomatic system developed by the Italian mathematician Giuseppe Peano (1858–
1932). The first volume established type theory, the second was devoted to numbers,
and the third to higher mathematics. The authors did intend a fourth volume on
geometry, but it was too much effort to complete. It made extremely intense reading.
In fact, I never managed to get pass the first page! It took the authors almost 100
pages of deep logical analysis in the second volume to prove that 1 + 1 = 2!




© Springer-Verlag London Ltd., part of Springer Nature 2022 31
J. Vince, Mathematics for Computer Graphics, Undergraduate Topics
in Computer Science, https://doi.org/10.1007/978-1-4471-7520-9_3

<a id='p53'></a>
<!-- Página 53 -->

32 3 Algebra

```
Russell wrote in The Principles of Mathematics [2]:
The fact that all Mathematics is Symbolic Logic is one of the greatest discoveries of our
age; and when this fact has been established, the remainder of the principles of mathematics
consists in the analysis of Symbolic Logic itself.

```

Unfortunately, this dream cannot be realised, for in 1931, the Austrian-born, and
later American logician and mathematician Kurt Gödel (1906–1978), showed that
even though mathematics is based upon a formal set of axioms, there will always be
statements involving natural numbers that cannot be proved or disproved. Furthermore, a consistent axiomatic system cannot demonstrate its own consistency. These
theorems are known as Gödel’s incompleteness theorems.
Even though we start off with some simple axioms, it does not mean that everything
discovered in mathematics is provable, which does not mean that we cannot continue
our every-day studies using algebra to solve problems. So let’s examine the basic
rules of algebra and prepare ourselves for the following chapters.



3.2 Background

Modern algebraic notation has evolved over thousands of years where different civilisations developed ways of annotating mathematical and logical problems. The word
‘algebra’ comes from the Arabic ‘al-jabr w’al-muqabal’ meaning ‘restoration and
reduction’. In retrospect, it does seem strange that centuries passed before the ‘equals’
sign (=) was invented, and concepts such as ‘zero’ (CE 876) were introduced, especially as they now seem so important. But we are not at the end of this evolution,
because new forms of annotation and manipulation will continue to emerge as new
mathematical objects are invented.
One fundamental concept of algebra is the idea of giving a name to an unknown
quantity. For example, m is often used to represent the slope of a 2D line, and c is the
line’s y-coordinate where it intersects the y-axis. René Descartes formalised the idea
of using letters from the beginning of the alphabet (a, b, c, . . . ) to represent arbitrary
quantities, and letters at the end of the alphabet ( p, q, r, s, t, . . . , x, y, z) to
represent quantities such as pressure ( p), time (t) and coordinates (x, y, z).
With the aid of the basic arithmetic operators: +, −, ×, / we can develop expressions that describe the behaviour of a physical process or a logical computation. For
example, the expression ax + by − d equals zero for a straight line. The variables x
and y are the coordinates of any point on the line and the values of a, b and d determine the position and orientation of the line. The = sign permits the line equation to
be expressed as a self-evident statement:

```
0 = ax + by − d.

```

Such a statement implies that the expressions on the left- and right-hand sides of
the = sign are ‘equal’ or ‘balanced’, and in order to maintain equality or balance,

<a id='p54'></a>
<!-- Página 54 -->

3.2 Background 33

whatever is done to one side, must also be done to the other. For example, adding d
to both sides, the straight-line equation becomes

```
d = ax + by.

```

Similarly, we could double or treble both expressions, divide them by 4, or add 6,
without disturbing the underlying relationship. When we are first taught algebra, we
are often given the task of rearranging a statement to make different variables the
subject. For example, (3.1) can be rearranged such that x is the subject:

```
x +4
y= (3.1)
1
2−
z
 
1
y 2− = x +4
z
 
1
x = y 2− − 4.
z

```

Making z the subject requires more effort:

```
x +4
y=
1
2−
z
 
1
y 2− = x +4
z
y
2y − = x + 4
z
y
2y − x − 4 =
z
y
z= .
2y − x − 4

```

Parentheses are used to isolate part of an expression in order to select a subexpression that is manipulated in a particular way. For example, the parentheses
in c(a + b) + d ensure that the variables a and b are added together before being
multiplied by c, and finally added to d.



3.2.1 Solving the Roots of a Quadratic Equation

Problem solving is greatly simplified if one has solved it before, and having a good
memory is always an advantage. In mathematics, we keep coming across problems that have been encountered before, apart from different numbers. For example,

<a id='p55'></a>
<!-- Página 55 -->

34 3 Algebra

(a + b)(a − b) always equals a 2 − b2 , therefore factorising the following is a trivial
exercise:

```
a 2 − 16 = (a + 4)(a − 4)
x 2 − 49 = (x + 7)(x − 7)
 √  √ 
x2 − 2 = x + 2 x − 2 .

A perfect square has the form:

a 2 + 2ab + b2 = (a + b)2 .

```

Consequently, factorising the following is also a trivial exercise:

```
a 2 + 4ab + 4b2 = (a + 2b)2
x 2 + 14x + 49 = (x + 7)2
x 2 − 20x + 100 = (x − 10)2 .

```

Now let’s solve the roots of the quadratic equation ax 2 + bx + c = 0, i.e. those
values of x that make the equation equal zero. As the equation involves an x 2 term,
we will exploit any opportunity to factorise it. We begin with the quadratic where
a = 0:
```
ax 2 + bx + c = 0.

Step 1: Subtract c from both sides to begin the process of creating a perfect square:

ax 2 + bx = −c.

Step 2: Divide both sides by a to create an x 2 term:

b c
x2 + x =− .
a a

Step 3: Add b2 /4a 2 to both sides to create a perfect square on the left side:

b b2 b2 c
x2 + x+ 2 = 2− .
a 4a 4a a
Step 4: Factorise the left side:
 2
b b2 c
x+ = 2
− .
2a 4a a
```


<a id='p56'></a>
<!-- Página 56 -->

3.2 Background 35

Step 5: Make 4a 2 the common denominator for the right side:
```
 2
b b2 − 4ac
x+ = .
2a 4a 2

```

Step 6: Take the square root of both sides:
```
√
b ± b2 − 4ac
x+ = .
2a 2a
```

Step 7: Subtract b/2a from both sides:
```
√
± b2 − 4ac b
x= − .
2a 2a
```

Step 8: Rearrange the right side:
```
√
−b ± b2 − 4ac
x=
2a
```

which provides the roots
```
√ for any quadratic equation.
```

The discriminant b2 − 4ac may be positive, negative or zero. A positive value
reveals two real roots:
```
√ √
−b + b2 − 4ac −b − b2 − 4ac
x1 = , x2 = . (3.2)
2a 2a
```

A negative value reveals two complex roots:
```
 
−b + i |b2 − 4ac| −b − i |b2 − 4ac|
x1 = , x2 = .
2a 2a
```

And a zero value reveals a single root:

```
−b
x= .
2a

```

For example, Fig. 3.1 shows the graph of y = x 2 + x − 2, where we can see that
y = 0 at two points: x = −2 and x = 1. In this equation

```
a=1
b=1
c = −2
```


<a id='p57'></a>
<!-- Página 57 -->

36 3 Algebra

Fig. 3.1 Graph of
y = x2 + x − 2 2

```
1


-3 -2 -1 0 1 2 3

-1

-2



```

Fig. 3.2 Graph of
y = x2 + x + 1 2

```
1


-3 -2 -1 0 1 2 3

-1

-2




```

which when plugged into (3.2) confirms the graph:
```
√
−1 + 1+8
x1 = =1
2
√
−1 − 1+8
x2 = = −2.
2

```

Figure 3.2 shows the graph of y = x 2 + x + 1, where at no point does y = 0. In
this equation

```
a=1
b=1
c=1

```

which when plugged into (3.2) confirms the graph by giving complex roots:

<a id='p58'></a>
<!-- Página 58 -->

3.2 Background 37
```
√
−1 +1−4 √
x1 = = − 21 + i 23
2
√
−1 − 1 − 4 √
x2 = = − 21 − i 23 .
2
```

Let’s show that x1 satisfies the original equation:

```
y = x12 + x1 + 1
 √ 2 √
= − 21 + i 23 − 21 + i 23 + 1
√ √
= 41 − i 23 − 34 − 21 + i 23 + 1
= 0.

```

x2 also satisfies the same equation.
Algebraic expressions also contain a wide variety of functions, such as
```
√
x = square root of x
√
n
x = nth root of x
x n = x to the power n
sin θ = sine of θ
cos θ = cosine of θ
tan θ = tangent of θ
log x = logarithm of x
ln x = natural logarithm of x.

```

Trigonometric functions are factorised as follows:

```
sin2 θ − cos2 θ = (sin θ + cos θ )(sin θ − cos θ )
sin2 θ − tan2 θ = (sin θ + tan θ )(sin θ − tan θ )
sin2 θ + 4 sin θ cos θ + 4 cos2 θ = (sin θ + 2 cos θ )2
sin2 θ − 6 sin θ cos θ + 9 cos2 θ = (sin θ − 3 cos θ )2 .



```

3.3 Indices

Indices are used to imply repeated multiplication and create a variety of situations
where laws are required to explain how the result is to be computed.

<a id='p59'></a>
<!-- Página 59 -->

38 3 Algebra

3.3.1 Laws of Indices

The laws of indices are expressed as follows:

```
a m × a n = a m+n
am
= a m−n
an
 m n
a = a mn

```

and are verified using some simple examples:

```
23 × 22 = 25 = 32
24
= 22 = 4
22
 2 3
2 = 26 = 64.

```

From the above laws, it is evident that

```
a0 = 1
1
a− p = p
a
1 √
aq = q a
p √
a q = a p.
q




```

3.4 Logarithms

Two people are associated with the invention of logarithms: the Scottish theologian and mathematician John Napier (1550–1617), and the Swiss clockmaker and
mathematician Joost Bürgi (1552–1632). Both men were frustrated by the time they
spent multiplying numbers together, and both realised that multiplication could be
replaced by addition using logarithms. Logarithms exploit the addition and subtraction of indices shown above, and are always associated with a base. For example,
if a x = n, then loga n = x, where a is the base. Where no base is indicated, it is
assumed to be 10. Two examples bring the idea to life:

```
102 = 100 then log 100 = 2
103 = 1000 then log 1000 = 3

```

which is interpreted as ‘10 has to be raised to the power (index) 2 to equal 100.’ The
log operation finds the power of the base for a given number. Thus a multiplication

<a id='p60'></a>
<!-- Página 60 -->

3.4 Logarithms 39

Fig. 3.3 Graph of log x log x

```
2


1



0 10 20 30 40 50 60 70 80 90 100

-1




```

Fig. 3.4 Graph of ln x ln x

```
4
3
2
1

0 10 20 30 40 50 60 70 80 90 100
-1




```

is translated into an addition using logs. Figure 3.3 shows the graph of log x, up to
x = 100, where we see that log 20 ≈ 1.3 and log 50 ≈ 1.7. Therefore, given suitable
software, logarithm tables, or a calculator with a log function, we can compute the
product 20 × 50 as follows:

```
log(20 × 50) = log 20 + log 50 ≈ 1.3 + 1.7 = 3
103 = 1000.

```

In general, the two bases used in calculators and software are 10 and
e = 2.718 281 846 . . . . To distinguish one type of logarithm from the other, a logarithm to the base 10 is written as log, and a natural logarithm to the base e is written ln.
```
Figure 3.4 shows the graph of ln x, up to x = 100, where we see that ln 20 ≈ 3
```

and ln 50 ≈ 3.9. Therefore, given suitable software, a set of natural logarithm tables
or a calculator with a ln function, we can compute the product 20 × 50 as follows:

```
ln(20 × 50) = ln 20 + ln 50 ≈ 3 + 3.9 = 6.9
e6.9 ≈ 1000.
```


<a id='p61'></a>
<!-- Página 61 -->

40 3 Algebra

From the above notation, it is evident that

```
log(ab) = log a + log b
 
a
log = log a − log b
b
log(a n ) = n log a.



```

3.5 Further Notation

All sorts of symbols are used to stand in for natural language expressions; here are
some examples:

```
< less than
> greater than
≤ less than or equal to
≥ greater than or equal to
≈ approximately equal to
≡ equivalent to
= not equal to
|x| absolute value of x.

```

For example, 0 ≤ t ≤ 1 is interpreted as: t is greater than or equal to 0, and is less
than or equal to 1. Basically, this means t varies between 0 and 1.



3.6 Functions

The theory of functions is a large subject, and at this point in the book, I will only
touch upon some introductory ideas that will help you understand the following
chapters.
The German mathematician Gottfried von Leibniz (1646–1716) is credited with
an early definition of a function, based upon the slope of a graph. However, it was
the Swiss mathematician Leonhard Euler (1707–1783) who provided a definition
along the lines: ‘A function is a variable quantity, whose value depends upon one or
more independent variables.’ Other mathematicians have introduced more rigorous
definitions, which are examined later on in the chapter on calculus.

<a id='p62'></a>
<!-- Página 62 -->

3.6 Functions 41

3.6.1 Explicit and Implicit Equations

The equation
```
y = 3x 2 + 2x + 4

```

associates the value of y with different values of x. The directness of the equation:
‘y =’, is why it is called an explicit equation, and their explicit nature is extremely
useful. However, simply by rearranging the terms, creates an implicit equation:

```
4 = y − 3x 2 − 2x

```

which implies that certain values of x and y combine to produce the result 4. Another
implicit form is
```
0 = y − 3x 2 − 2x − 4

```

which means the same thing, but expresses the relationship in a slightly different
way.
An implicit equation can be turned into an explicit equation using algebra. For
example, the implicit equation
```
4x + 2y = 12

```

has the explicit form:
```
y = 6 − 2x

```

where it is clear what y equals.



3.6.2 Function Notation

The explicit equation
```
y = 3x 2 + 2x + 4

```

tells us that the value of y depends on the value of x, and not the other way around.
For example, when x = 1, y = 9; and when x = 2, y = 20. As y depends upon the
value of x, it is called the dependent variable; and as x is independent of y, it is
called the independent variable.
```
We can also say that y is a function of x, which can be written as

y = f (x)

```

where the letter ‘ f ’ is the name of the function, and the independent variable is
enclosed in brackets. We could have also written y = g(x), y = h(x), etc.

<a id='p63'></a>
<!-- Página 63 -->

42 3 Algebra

```
Eventually, we have to identify the nature of the function, which in this case is

f (x) = 3x 2 + 2x + 4.

```

Nothing prevents us from writing

```
y = f (x) = 3x 2 + 2x + 4

```

which means: y equals the value of the function f (x), which is determined by the
independent variable x using the expression 3x 2 + 2x + 4.
An equation may involve more than one independent variable, such as the volume
of a cylinder:
```
V = πr 2 h

```

where r is the radius, and h, the height, and is written:

```
V (r, h) = πr 2 h.



```

3.6.3 Intervals

An interval is a continuous range of numerical values associated with a variable,
which can include or exclude the upper and lower values. For example, a variable
such as x is often subject to inequalities like x ≥ a and x ≤ b, which can also be
written as
```
a≤x ≤b

```

and implies that x is located in the closed interval [a, b], where the square brackets
indicate that the interval includes a and b. For example,

```
1 ≤ x ≤ 10

```

means that x is located in the closed interval [1, 10], which includes 1 and 10.
When the boundaries of the interval are not included, then we would state x > a
and x < b, which is written
```
a<x <b

```

and means that x is located in the open interval ]a, b[, where the reverse square
brackets indicate that the interval excludes a and b. For example,

```
1 < x < 10

```

means that x is located in the open interval ]1, 10[, which excludes 1 and 10.

<a id='p64'></a>
<!-- Página 64 -->

3.6 Functions 43

Fig. 3.5 Closed, open and
half-open intervals. The
```
half-open interval [a, b[
```

filled circles indicate that a
or b are included in the
interval half-open interval ]a, b]
```
open interval ]a, b[

closed interval [a, b]

a b

The filled circles indicate that a or b are included in the interval.


```

Closed and open intervals may be combined as follows. If x ≥ a and x < b then

```
a≤x <b

```

and means that x is located in the half-open interval [a, b[. For example,

```
1 ≤ x < 10

```

means that x is located in the half-open interval [1, 10[, which includes 1, but not 10.
Similarly, if
```
1 < x ≤ 10

```

means that x is located in the half-open interval ]1, 10], which includes 10, but not 1.
An alternative notation employs parentheses instead of reversed brackets:

```
]a, b[ = (a, b)
[a, b[ = [a, b)
]a, b] = (a, b].

```

Figure 3.5 shows open, closed and half-open intervals diagrammatically.


3.6.4 Function Domains and Ranges

The following descriptions of domains and ranges only apply to functions with one
independent variable: f (x).
Returning to the above function:

```
y = f (x) = 3x 2 + 2x + 4

```

the independent variable x, can take on any value from −∞ to ∞, which is called
the domain of the function. In this case, the domain of f (x) is the set of real numbers

<a id='p65'></a>
<!-- Página 65 -->

44 3 Algebra

R. The notation used for intervals, is also used for domains, which in this case is

```
] − ∞, ∞[

```

and is open, as there are no precise values for −∞ and ∞.
```
As the independent variable takes on different values from its domain, so the
```

dependent variable, y or f (x), takes on different values from its range. Therefore,
if the domain of the linear function f (x) = 3x + 4 is [−4, 4], the range of f (x) is
calculated by finding f (−4) and f (4):

```
f (−4) = −12 + 4 = −8
f (4) = 12 + 4 = 16

```

and the range is [−4, 4].
Although calculating the range of linear functions is simple, other types of functions require a knowledge of calculus.
The domain of log x is
```
]0, ∞[

```

which is open, because x = 0. Whereas, the range of log x is

```
] − ∞, ∞[.
√
The domain of x is
[0, ∞[
√
```

which is √
```
half-open, because 0 = 0, and ∞ has no precise value. Similarly, the
```

range of x is
```
[0, ∞[.

```

Sometimes, a function is sensitive to one specific number. For example, in the function

```
1
y = f (x) = ,
x −1

```

when x = 1, there is a divide by zero, which is meaningless. Consequently, the
domain of f (x) is the set of real numbers R, apart from 1.



3.6.5 Odd and Even Functions

An odd function satisfies the condition:

```
f (−x) = − f (x)
```


<a id='p66'></a>
<!-- Página 66 -->

3.6 Functions 45

where x is located in a valid domain. Consequently, the graph of an odd function is
symmetrical relative to the origin. For example, sin(θ ) is odd because

```
sin(−θ ) = − sin θ

```

as illustrated in Fig. 3.6. Other odd functions include:

```
f (x) = ax
f (x) = ax 3 .

```

An even function satisfies the condition:

```
f (−x) = f (x)

```

where x is located in a valid domain. Consequently, the graph of an even function is
symmetrical relative to the f (x) axis. For example, cos θ is even because

```
cos(−θ ) = cos θ

```

as illustrated in Fig. 3.7. Other even functions include:

```
f (x) = ax 2
f (x) = ax 4 .

```

Fig. 3.6 The sine function is
an odd function sin




Fig. 3.7 The cosine function
is an even function cos

<a id='p67'></a>
<!-- Página 67 -->

46 3 Algebra

3.6.6 Power Functions

Functions of the form f (x) = x n are called power functions of degree n and are
either odd or even. If n is an odd natural number, then the power function is odd, else
if n is an even natural number, then the power function is even.



3.7 Summary

The above description of algebra should be sufficient for the reader to understand the
following chapters. However, one should remember that this is only the beginning
of a very complex subject.



3.8 Worked Examples

3.8.1 Algebraic Manipulation

Rearrange the following equations to make y the subject.

```
x +4 x + 68 x + 68
7= , 23 = , 23 = .
3−y 1 3 − sin y
3+ y
e
x +4
7=
3−y
x +4
3−y =
7
x +4 17 − x
y =3− = .
7 7

x + 68
23 =
1
3+ y
e
1 x + 68
3+ y =
e 23
1 x + 68
= −3
ey 23
x −1
=
23
23
ey =
x −1
```


<a id='p68'></a>
<!-- Página 68 -->

3.8 Worked Examples 47
```
 
23
y = ln .
x −1

x + 68
23 =
3 − sin y
x + 68
3 − sin y =
23
x + 68
sin y = 3 −
23
1−x
=
23
 
1−x
y = arcsin .
23



```

3.8.2 Solving a Quadratic Equation

Solve the following quadratic equations, and test the answers.

```
0 = x 2 + 4x + 1, 0 = 2x 2 + 4x + 2, 0 = 2x 2 + 4x + 4.

```

0 = x 2 + 4x + 1
```
√
−b ± b2 − 4ac
x=
2a
√
−4 ± 16 − 4
=
2
√
−4 ± 12
=
2√
= −2 ± 3.
√
```

Test with x = −2 + 3.
```
 √ 2  √ 
x 2 + 4x + 1 = −2 + 3 + 4 −2 + 3 + 1
√ √
=4−4 3+3−8+4 3+1
= 0.
√
```

Test with x = −2 − 3.
```
 √ 2  √ 
x 2 + 4x + 1 = −2 − 3 + 4 −2 − 3 + 1
```


<a id='p69'></a>
<!-- Página 69 -->

48 3 Algebra
```
√ √
=4+4 3+3−8−4 3+1
= 0.

```

0 = 2x 2 + 4x + 2
```
√
−b ±b2 − 4ac
x=
2a
√
−4 ± 16 − 16
=
4
−4
=
4
= −1.

```

Test with x = −1.

```
2x 2 + 4x + 2 = 2 − 4 + 2
= 0.

```

0 = 2x 2 + 4x + 4
```
√
−b ± b2 − 4ac
x=
2a
√
−4 ± 16 − 32
=
√4
−4 ± −16
=
4√
= −1 ± −1
= −1 ± i.

```

Test with x = −1 + i.

```
2x 2 + 4x + 4 = 2(−1 + i)2 + 4(−1 + i) + 4
= 2(1 − 2i − 1) − 4 + 4i + 4
= −4i + 4i
= 0.

```

Test with x = −1 − i.

```
2x 2 + 4x + 4 = 2(−1 − i)2 + 4(−1 − i) + 4
= 2(1 + 2i − 1) − 4 − 4i + 4
= 4i − 4i
= 0.
```


<a id='p70'></a>
<!-- Página 70 -->

3.8 Worked Examples 49

3.8.3 Factorising

Factorise the following equations:

```
4 sin2 θ − 4 cos2 θ
9 sin2 θ + 6 sin θ cos θ + cos2 θ
25 sin2 θ + 10 sin θ cos θ + cos2 θ.


4 sin2 θ − 4 cos2 θ = (2 sin θ + 2 cos θ )(2 sin θ − 2 cos θ )
9 sin2 θ + 6 sin θ cos θ + cos2 θ = (3 sin θ + cos θ )2
25 sin2 θ + 10 sin θ cos θ + cos2 θ = (5 sin θ + cos θ )2 .




```

References

1. Russell B, Whitehead AN (1903) Principia mathematica. Cambridge University Press
2. Russell B (1938) [First published 1903]. Principles of mathematics, 2nd edn. WW Norton &
Company

<a id='p71'></a>
<!-- Página 71 -->


## Chapter 4

Trigonometry




4.1 Introduction

This chapter covers some basic features of trigonometry such as angular measure,
trigonometric ratios, inverse ratios, trigonometric identities and various rules, with
which the reader should be familiar.



4.2 Background

The word ‘trigonometry’ divides into three parts: ‘tri’, ‘gon’, ‘metry’, which means
the measurement of three-sided polygons, i.e. triangles. It is an ancient subject and
is used across all branches of mathematics.



4.3 Units of Angular Measurement

The measurement of angles is at the heart of trigonometry, and today two units of
angular measurement are part of modern mathematics: degrees and radians. The
degree (or sexagesimal) unit of measure derives from defining one complete rotation
as 360◦ . Each degree divides into 60 min, and each minute divides into 60 s. The
number 60 has survived from Mesopotamian days and appears rather incongruous
when used alongside today’s decimal system—nevertheless, it is still convenient to
work with degrees even though the radian is a natural feature of mathematics.
```
The radian of angular measure does not depend upon any arbitrary constant, and
```

is often defined as the angle created by a circular arc whose length is equal to the
circle’s radius. And because the perimeter of a circle is 2πr , 2π rad correspond to
one complete rotation. As 360◦ corresponds to 2π rad, 1 rad equals 180◦ /π , which
is approximately 57.3◦ . The following relationships between radians and degrees are

© Springer-Verlag London Ltd., part of Springer Nature 2022 51
J. Vince, Mathematics for Computer Graphics, Undergraduate Topics
in Computer Science, https://doi.org/10.1007/978-1-4471-7520-9_4

<a id='p72'></a>
<!-- Página 72 -->

52 4 Trigonometry

worth remembering:
```
π
[rad] ≡ 90◦ , π [rad] ≡ 180◦
2
3π
[rad] ≡ 270◦ , 2π [rad] ≡ 360◦ .
2
```

To convert x ◦ to radians:
```
π x◦
[rad].
180
```

To convert x [rad] to degrees:

```
180x
[degrees].
π
```

For those readers wishing to know the background to radians we need to use
power series. We start with the power series for eθ , sin θ and cos θ :

```
θ1 θ2 θ3 θ4 θ5 θ6 θ7 θ8 θ9
eθ = 1 + + + + + + + + + + ···
1! 2! 3! 4! 5! 6! 7! 8! 9!
θ3 θ5 θ7 θ9
sin θ = θ − + − + + ···
3! 5! 7! 9!
θ2 θ4 θ6 θ8
cos θ = 1 − + − + + ··· .
2! 4! 6! 8!
```

Euler proved that these three power series are related, and when θ = π , sin θ = 0,
and cos θ = −1. Figure 4.1 shows curves of the sine power series for 3, 5, 7 and 9
terms, and when θ = 2π , the graph reaches zero.


Fig. 4.1 The sine power
series for different number of 1
terms


```
0 2




-1
```


<a id='p73'></a>
<!-- Página 73 -->

4.4 The Trigonometric Ratios 53

4.4 The Trigonometric Ratios

Ancient civilisations knew that triangles—whatever their size—possessed some
inherent properties, especially the ratios of sides and their associated angles. This
means that if these ratios are known in advance, problems involving triangles with
unknown lengths and angles, can be discovered using these ratios.
Figure 4.2 shows a point P with coordinates (base, height), on a unit-radius
circle rotated through an angle θ . As P is rotated, it moves into the 2nd quadrant,
3rd quadrant, 4th quadrant and returns back to the first quadrant. During the rotation,
the sign of height and base change as follows:
```
1st quadrant: height (+), base (+)
2nd quadrant: height (+), base (−)
3rd quadrant: height (−), base (−)
4th quadrant: height (−), base (+).
```

Figures 4.3 and 4.4 plot the changing values of height and base over the four
quadrants, respectively. When radius = 1, the curves vary between 1 and −1. In
the context of triangles, the sides are labelled as follows:

```
hypotenuse = radius
opposite = height
adjacent = base.

```

Thus, using the right-angle triangle shown in Fig. 4.5, the trigonometric ratios:
sine, cosine and tangent are defined as

```
opposite adjacent opposite
sin θ = , cos θ = , tan θ = .
hypotenuse hypotenuse adjacent



```

Fig. 4.2 The four quadrants +
for the trigonometric ratios P
```
2nd quadrant radius 1st quadrant

height
_ +
base



3rd quadrant 4th quadrant
_
```


<a id='p74'></a>
<!-- Página 74 -->

54 4 Trigonometry

Fig. 4.3 The graph of 1
height over the four
quadrants
```
height 1st 2nd
quadrant quadrant

=2

3rd 4th
quadrant quadrant




-1


```

Fig. 4.4 The graph of base 1
over the four quadrants

```
base 1st 4th
quadrant quadrant



=2
2nd 3rd
quadrant quadrant




-1


```

Fig. 4.5 Sides of a
right-angle triangle



```
hypotenuse
opposite




adjacent




```

The reciprocals of these functions, cosecant, secant and cotangent are also useful:

```
1 1 1
csc θ = , sec θ = , cot θ = .
sin θ cos θ tan θ
```

As an example, Fig. 4.6 shows a triangle where the hypotenuse and an angle are
known. The other sides are calculated as follows:

<a id='p75'></a>
<!-- Página 75 -->

4.4 The Trigonometric Ratios 55

Fig. 4.6 A right-angle
triangle with two unknown
side lengths

```
10
opposite



40o
adjacent

```

Fig. 4.7 Graph of the tan
```
4
```

tangent function
```
3
2
1

-2 - 2
-1
-2
-3
-4




opposite
= sin 40◦
10
opposite = 10 sin 40◦ ≈ 10 × 0.64278 = 6.4278
adjacent
= cos 40◦
10
adjacent = 10 cos 40◦ ≈ 10 × 0.7660 = 7.660.

```

The theorem of Pythagoras confirms that these lengths are correct:

```
6.42782 + 7.6602 ≈ 102 .

```

Figure 4.7 shows the graph of the tangent function, which, like the sine and cosine
functions, is periodic, but with only a period of π radians.



4.4.1 Domains and Ranges

The periodic nature of sin θ , cos θ and tan θ , means that their domains are infinitely
large. Consequently, it is customary to confine the domain of sin θ to
```
 
π π
− ,
2 2
```


<a id='p76'></a>
<!-- Página 76 -->

56 4 Trigonometry

and cos θ to
```
[0, π ].

```

The range for both sin θ and cos θ is

```
[−1, 1].

```

The domain for tan θ is the open interval
```
 
π π
− ,
2 2

```

and its range is the open interval:

```
] − ∞, ∞[.




```

4.5 Inverse Trigonometric Ratios

The functions sin θ , cos θ , tan θ , csc θ , sec θ and cot θ provide different ratios for the
angle θ , and the inverse trigonometric functions convert a ratio back into an angle.
These are arcsin, arccos, arctan, arccsc, arcsec and arccot, and are sometimes written
as sin−1 , cos−1 , tan−1 , csc−1 , sec−1 and cot −1 . For example, sin 30◦ = 0.5, therefore,
arcsin 0.5 = 30◦ . Consequently, the domain for arcsin is the range for sin:

```
[−1, 1]

```

and the range for arcsin is the domain for sin:
```
 
π π
− ,
2 2

```

as shown in Fig. 4.8. Similarly, the domain for arccos is the range for cos:

```
[−1, 1]

```

and the range for arccos is the domain for cos:

```
[0, π ]

```

as shown in Fig. 4.9.

<a id='p77'></a>
<!-- Página 77 -->

4.5 Inverse Trigonometric Ratios 57

Fig. 4.8 Graph of the arcsin arcsin x
function
```
/2



-1
x
1



- /2

```

Fig. 4.9 Graph of the arccos arccos x
function




```
x
-1 0 1


```

The domain for arctan is the range for tan:

```
] − ∞, ∞[

```

and the range for arctan is the domain for tan:
```
 
π π
− ,
2 2

```

as shown in Fig. 4.10.
Various programming languages include the atan2 function, which is an arctan
```
function with two arguments: atan2(y, x). The signs of x and y provide sufficient
```

information to locate the quadrant containing the angle, and gives the atan2 function
a range of [0, 2π ].

<a id='p78'></a>
<!-- Página 78 -->

58 4 Trigonometry

Fig. 4.10 Graph of the arctan x
arctan function /2




```
x




- /2



```

4.6 Trigonometric Identities

The sin and cos curves are identical, apart from being displaced by 90◦ , and are
related by  π
```
cos θ = sin θ + .
2
```

Also, simple algebra and the theorem of Pythagoras can be used to derive other
formulae such as
```
sin θ
= tan θ
cos θ
sin2 θ + cos2 θ = 1
1 + tan2 θ = sec2 θ
1 + cot 2 θ = csc2 θ.



```

4.7 The Sine Rule

Figure 4.11 shows a triangle labeled such that side a is opposite angle A, side b is
opposite angle B, etc. The sine rule states:

```
a b c
= =
sin A sin B sin C
```

which can be used to compute the length of an unknown length or angle. For example,
if A = 60◦ , B = 40◦ , C = 80◦ , and b = 10, then

```
a 10
◦
=
sin 60 sin 40◦
```


<a id='p79'></a>
<!-- Página 79 -->

4.7 The Sine Rule 59

Fig. 4.11 An arbitrary
triangle

## C



```
b a




```


## A B

```
c



```

rearranging, we have
```
10 sin 60◦
a= ≈ 13.47.
sin 40◦
```

Similarly:
```
c 10
◦
=
sin 80 sin 40◦
```

therefore
```
10 sin 80◦
c= ≈ 15.32.
sin 40◦




```

4.8 The Cosine Rule

The cosine rule expresses the sin2 θ + cos2 θ = 1 identity for the arbitrary triangle
shown in Fig. 4.11. In fact, there are three versions:

```
a 2 = b2 + c2 − 2bc cos A
b2 = c2 + a 2 − 2ca cos B
c2 = a 2 + b2 − 2ab cos C.

```

Three further relationships also hold:

```
a = b cos C + c cos B
b = c cos A + a cos C
c = a cos B + b cos A.
```


<a id='p80'></a>
<!-- Página 80 -->

60 4 Trigonometry

4.9 Compound-Angle Identities

Trigonometric identities are useful for solving various mathematical problems, but
apart from this, their proof often contains a strategy that can be used else where. In
the first example, watch out for the technique of multiplying by 1 in the form of a
ratio, and swapping denominators. The technique is rather elegant and suggests that
the result was known in advance, which probably was the case. Let’s begin by finding
a way of representing sin(α + β) in terms of sin α, cos α, sin β, cos β.
```
With reference to Fig. 4.12:

```


## FD BC + E D

```
sin(α + β) = =
```


## AD AD


## BC AC ED CD

```
= +
```


## AD AC AD C D


## BC AC ED CD

```
= +
```


## AC AD C D AD

```
sin(α + β) = sin α cos β + cos α sin β. (4.1)

```

To find sin(α − β), reverse the sign of β in (4.1):

```
sin(α − β) = sin α cos β − cos α sin β. (4.2)

```

Now let’s expand cos(α + β) with reference to Fig. 4.12:


## AE AB − EC

```
cos(α + β) = =
```


## AD AD


## AB AC EC C D

```
= −
```


## AD AC AD C D


## AB AC EC C D

```
= −
```


## AC AD C D AD

```
cos(α + β) = cos α cos β − sin α sin β. (4.3)


```

Fig. 4.12 The geometry to D
expand sin(α + β)



## E C






## A F B


<a id='p81'></a>
<!-- Página 81 -->

4.9 Compound-Angle Identities 61

To find cos(α − β), reverse the sign of β in (4.3):

```
cos(α − β) = cos α cos β + sin α sin β.

```

To expand tan(α + β), divide (4.1) by (4.3):

```
sin(α + β) sin α cos β + cos α sin β
=
cos(α + β) cos α cos β − sin α sin β
sin α cos β cos α sin β
+
cos α cos β cos α cos β
=
cos α cos β sin α sin β
−
cos α cos β cos α cos β
tan α + tan β
tan(α + β) = . (4.4)
1 − tan α tan β

```

To find tan(α − β), reverse the sign of β in (4.4):

```
tan α − tan β
tan(α − β) = .
1 + tan α tan β




```

4.9.1 Double-Angle Identities

By making β = α, the three compound-angle identities

```
sin(α ± β) = sin α cos β ± cos α sin β
cos(α ± β) = cos α cos β ∓ sin α sin β
tan α ± tan β
tan(α ± β) =
1 ∓ tan α tan β

```

provide the starting point for deriving three corresponding double-angle identities:

```
sin(α ± α) = sin α cos α ± cos α sin α
sin(2α) = 2 sin α cos α.

```

Similarly,

```
cos(α ± α) = cos α cos α ∓ sin α sin α
cos(2α) = cos2 α − sin2 α

```

which can be further simplified using sin2 α + cos2 α = 1:

<a id='p82'></a>
<!-- Página 82 -->

62 4 Trigonometry

```
cos(2α) = cos2 α − sin2 α
cos(2α) = 2 cos2 α − 1
cos(2α) = 1 − 2 sin2 α.

```

And for tan(2α), we have:

```
tan α ± tan α
tan(α ± α) =
1 ∓ tan α tan α
2 tan α
tan(2α) = .
1 − tan2 α



```

4.9.2 Multiple-Angle Identities

The French mathematician Abraham de Moivre (1667–1754) published an equation
in 1707, which implied

```
cos α = 21 (cos(nα) + i sin(nα))1/n + 21 (cos(nα) − i sin(nα))1/n

```

for all positive, integer values of n. Fifteen years later, de Moivre proved that

```
(cos α + i sin α)n = cos(nα) + i sin(nα)

```

which is known as de Moivre’s Formula. Euler proved in 1749 that this formula held
for n ∈ R using his own discovery:

```
cos α + i sin α = eiα .

```

Using de Moivre’s formula, one can show that

```
sin(3α) = 3 sin α − 4 sin3 α
cos(3α) = 4 cos3 α − 3 cos α
3 tan α − tan3 α
tan(3α) =
1 − 3 tan2 α
sin(4α) = 4 sin α cos α − 8 sin3 α cos α
cos(4α) = 8 cos4 α − 8 cos2 α + 1
4 tan α − 4 tan3 α
tan(4α) =
1 − 6 tan2 α + tan4 α
sin(5α) = 16 sin5 α − 20 sin3 α + 5 sin α
cos(5α) = 16 cos5 α − 20 cos3 α + 5 cos α
5 tan α − 10 tan3 α + tan5 α
tan(5α) = .
1 − 10 tan2 α + 5 tan4 α
```


<a id='p83'></a>
<!-- Página 83 -->

4.9 Compound-Angle Identities 63

4.9.3 Half-Angle Identities

Every now and then, it is necessary to compute the sine, cosine or tangent of a halfangle from the corresponding whole-angle functions. To do this, we rearrange the
double-angle identities as follows.

```
cos(2α) = 1 − 2 sin2 α
1 − cos(2α)
sin2 α =
2
 α  1 − cos α
sin2 =
2 2
α  1 − cos α
sin =± . (4.5)
2 2

```

Similarly,

```
1 + cos(2α)
cos2 α =
2
 α  1 + cos α
cos2 =
2 2
α  1 + cos α
cos =± . (4.6)
2 2

```

Dividing (4.5) by (4.6) we have

```
α  
1 − cos α
tan =± .
2 1 + cos α




```

4.10 Perimeter Relationships

Finally, with reference to Fig. 4.11, we come to the relationships that integrate angles
with the perimeter of a triangle:

```
s = 21 (a + b + c)
  
A (s − b)(s − c)
sin =±
2 bc
  
B (s − c)(s − a)
sin =±
2 ca
```


<a id='p84'></a>
<!-- Página 84 -->

64 4 Trigonometry

```
  
C (s − a)(s − b)
sin =±
2 ab
  
A s(s − a)
cos =±
2 bc
  
B s(s − b)
cos =±
2 ca
  
C s(s − c)
cos =±
2 ab
2
sin A = ± s(s − a)(s − b)(s − c)
bc
2
sin B = ± s(s − a)(s − b)(s − c)
ca
2
sin C = ± s(s − a)(s − b)(s − c).
ab


```

4.11 Summary

No derivations have been given for the formulae in this chapter, and the reader who
is really interested, will find plenty of books that show their origins. Hopefully, the
formulae will be a useful reference when studying the rest of the book, and perhaps
will be of some use when solving problems in the future.
```
I would like to draw the reader’s attention to two books I have found a source of
```

information and inspiration [1, 2].



References

1. Harris JW, Stocker H (1998) Handbook of mathematics and computational science. Springer,
New York
2. Gullberg J (1997) Mathematics from the birth of numbers. WW Norton & Co., New York

<a id='p85'></a>
<!-- Página 85 -->


## Chapter 5

Coordinate Systems




5.1 Introduction

In this chapter we revise Cartesian coordinates, axial systems, the distance between
two points in space, and the area of simple 2D shapes. It also covers polar, spherical
polar and cylindrical coordinate systems.



5.2 Background

René Descartes is often credited with the invention of the xy-plane, but the French
lawyer and mathematician Pierre de Fermat (1601–1665) was probably the first
inventor. In 1636 Fermat was working on a treatise titled Ad locus planos et solidos
isagoge, which outlined what we now call ‘analytic geometry’. Unfortunately, Fermat
never published his treatise, although he shared his ideas with other mathematicians
such as Blaise Pascal (1623–1662). At the same time, Descartes devised his own
system of analytic geometry and in 1637 published his results in the prestigious
journal Géométrie. In the eyes of the scientific world, the publication date of a
technical paper determines when a new idea or invention is released into the public
domain. Consequently, ever since this publication Descartes has been associated with
the x y-plane, which is why it is called the Cartesian plane.
The Cartesian plane is such a simple idea that it is strange that it took so long
to be discovered. However, although it is true that René Descartes showed how
an orthogonal coordinate system could be used for graphs and coordinate geometry,
coordinates had been used by ancient Egyptians, almost 2000 years earlier! If Fermat
had been more efficient in publishing his research results, the x y-plane could have
been called the Fermatian plane! [1].




© Springer-Verlag London Ltd., part of Springer Nature 2022 65
J. Vince, Mathematics for Computer Graphics, Undergraduate Topics
in Computer Science, https://doi.org/10.1007/978-1-4471-7520-9_5

<a id='p86'></a>
<!-- Página 86 -->

66 5 Coordinate Systems

Fig. 5.1 The Cartesian
plane 3

## P(3, 2)

```
2

1


-5 -4 -3 -2 -1 0 1 2 3 4 5

-1

-2
```


## Q(-4, -2)

```
-3



```

5.3 The Cartesian Plane

The Cartesian plane provides a mechanism for locating points with a unique, ordered
pair of numbers (x, y) as shown in Fig. 5.1, where P has coordinates (3, 2) and
Q has coordinates (−4, −2). The point (0, 0) is called the origin. As previously
mentioned, Descartes suggested that the letters x and y should be used to represent
variables, and letters at the other end of the alphabet should stand for numbers. Which
is why equations such as y = ax 2 + bx + c, are written this way.
The axes are said to be oriented as the x-axis rotates anticlockwise towards the
y-axis. They could have been oriented in the opposite sense, with the y-axis rotating
anticlockwise towards the x-axis.


5.4 Function Graphs

When functions such as
```
linear: y = mx + c,
quadratic: y = ax 2 + bx + c,
cubic: y = ax 3 + bx 2 + cx + d,
trigonometric: y = a sin x,
```

are drawn as graphs, they create familiar shapes that permit the function to be easily identified. Linear functions are straight lines; quadratics are parabolas; cubics,
generally, have an ‘S’ shape; and trigonometric functions often possess a wave-like
trace. Figure 5.2 shows examples of each type of function.


5.5 Shape Representation

The Cartesian plane also provides a way to represent 2D shapes numerically, which
permits them to be manipulated mathematically. Let’s begin with 2D polygons and
show how their internal area can be calculated.

<a id='p87'></a>
<!-- Página 87 -->

5.5 Shape Representation 67

```
4 3 2 1 1 2 3 4 5
```

Fig. 5.2 Graphs of four
```
function types
linear

quadratic


cubic


sinusoid



```

Fig. 5.3 A simple polygon y
```
(1, 3)
```

created by a chain of vertices
```
3

(3, 2)
2


1 (1, 1) (3, 1)


1 2 3 4 5 x



```

5.5.1 2D Polygons

A polygon is formed from a chain of vertices (points) as shown in Fig. 5.3. A straight
line is assumed to connect each pair of neighbouring vertices; intermediate points
on the line are not explicitly stored. There is no convention for starting a chain
of vertices, but software will often dictate whether polygons have a clockwise or
anticlockwise vertex sequence.
```
We can now subject this list of coordinates to a variety of arithmetic and mathe-
```

matical operations. For example, if we double the values of x and y and redraw the
vertices, we discover that the shape’s geometric integrity is preserved, but its size
is doubled relative to the origin. Similarly, if we divide the values of x and y by 2,
the shape is still preserved, but its size is halved relative to the origin. On the other
hand, if we add 1 to every x-coordinate, and 2 to every y-coordinate, and redraw the
vertices, the shape’s size remains the same but is displaced 1 unit horizontally and 2
units vertically.



5.5.2 Area of a Shape

The area of a polygonal shape is readily calculated from its list of coordinates. For
example, using the list of coordinates shown in Table 5.1: the area is computed by

<a id='p88'></a>
<!-- Página 88 -->

68 5 Coordinate Systems

Table 5.1 A polygon’s coordinates
x y
x0 y0
x1 y1
x2 y2
x3 y3



```
area = 21 [(x0 y1 − x1 y0 ) + (x1 y2 − x2 y1 ) + (x2 y3 − x3 y2 ) + (x3 y0 − x0 y3 )].

```

You will observe that the calculation sums the results of multiplying an x by the
next y, minus the next x by the previous y. When the last vertex is selected, it is
paired with the first vertex to complete the process. The result is then halved to reveal
the area. As a simple test, let’s apply this formula to the shape described in Fig. 5.3:

area = 21 [(1 × 1 − 3 × 1) + (3 × 2 − 3 × 1) + (3 × 3 − 1 × 2) + (1 × 1 − 1 × 3)]
area = 21 [−2 + 3 + 7 − 2] = 3.

which, by inspection, is the true area. The beauty of this technique is that it works
with any number of vertices and any arbitrary shape. The origin of this technique is
revealed in Chap. 7.
Another feature of the technique is that if the set of coordinates is clockwise,
the area is negative, which means that the calculation computes vertex orientation as
well as area. To illustrate this feature, the original vertices are reversed to a clockwise
sequence as follows:

area = 21 [(1 × 3 − 1 × 1) + (1 × 2 − 3 × 3) + (3 × 1 − 3 × 2) + (3 × 1 − 1 × 1)]
area = 21 [2 − 7 − 3 + 2] = −3.

The minus sign confirms that the vertices are in a clockwise sequence.



5.6 Theorem of Pythagoras in 2D

The theorem of Pythagoras is used to calculate the distance between two points.
Figure 5.4 shows two arbitrary points P1 (x1 , y1 ) and P2 (x2 , y2 ). The distance x =
x2 − x1 and y = y2 − y1 . Therefore, the distance d between P1 and P2 is given by
```

d= (x)2 + (y)2 .
√
```

For example, given P1 (1, 1), P2 (4, 5), then d = 32 + 42 = 5.

<a id='p89'></a>
<!-- Página 89 -->

5.7 3D Cartesian Coordinates 69

Fig. 5.4 Calculating the y
distance between two points
```
y2 P2


y d

```


## P1

```
y1



x1 x x2 x




```

5.7 3D Cartesian Coordinates

Two coordinates are required to locate a point on the 2D Cartesian plane, and three
coordinates are required for 3D space. The corresponding axial system requires three
mutually perpendicular axes; however, there are two ways to add the extra z-axis.
Figure 5.5 shows the two orientations, which are described as left- and right-handed
axial systems. The left-handed system permits us to align our left hand with the
axes such that the thumb aligns with the x-axis, the first finger aligns with the yaxis, and the middle finger aligns with the z-axis. The right-handed system permits
the same system of alignment, but using our right hand. The choice between these
axial systems is arbitrary, but one should be aware of the system employed by commercial computer graphics packages. The main problem arises when projecting 3D
points onto a 2D plane, which has an oriented axial system. A right-handed system
is employed throughout this book, as shown in Fig. 5.6, which also shows a point P
with its coordinates. It also worth noting that handedness has no meaning in spaces
with 4 dimensions or more. Also note that the choice of axis as the vertical axis is a
matter of personal preference.



Fig. 5.5 a A left-handed y
axial system b A
right-handed axial system
```
y


(b)
z x

(a)
x z
```


<a id='p90'></a>
<!-- Página 90 -->

70 5 Coordinate Systems

Fig. 5.6 A right-handed y
axial system showing the
coordinates of a point P P



```
y


z x z x



```

5.7.1 Theorem of Pythagoras in 3D

The theorem of Pythagoras in 3D is a natural extension of the 2D rule. In fact, it
even works in higher dimensions. Given two arbitrary points P1 (x1 , y1 , z 1 ) and
P2 (x2 , y2 , z 2 ), we compute x = x2 − x1 , y = y2 − y1 and z = z 2 − z 1 , from
which the distance d between P1 and P2 is given by
```

d= (x)2 + (y)2 + (z)2

```

and the distance from the origin to a point P(x, y, z) is simply
```

d= x 2 + y2 + z2.
√
```

Therefore, the point (3, 4, 5) is 32 + 42 + 52 ≈ 7.07 from the origin.



5.8 Polar Coordinates

Polar coordinates are used for handling data containing angles, rather than linear
offsets. Figure 5.7 shows the convention used for 2D polar coordinates, where the


Fig. 5.7 2D polar
coordinates Q(4, 0.8 ) 3 P( , ) P(x, y)

```
2
1

-4 -3 -2 -1 0 1 2 3 4
-1
-2
-3
```


<a id='p91'></a>
<!-- Página 91 -->

5.8 Polar Coordinates 71

point P(x, y) has equivalent polar coordinates P(ρ, θ ), where:

```
x = ρ cos θ
y = ρ sin θ

ρ = x 2 + y2
y
θ = arctan .
x

```

For example, the point Q(4, 0.8π ) in Fig. 5.7 has Cartesian coordinates:

```
x = 4 cos(0.8π ) ≈ −3.24
y = 4 sin(0.8π ) ≈ 2.35

```

and the point (3, 4) has polar coordinates:
```

ρ= 32 + 42 = 5
 
θ = arctan 43 ≈ 53.13◦ .

```

These conversion formulae work only for the first quadrant. The atan2 function
should be used in a software environment, as it works with all four quadrants.



5.9 Spherical Polar Coordinates

Figure 5.8 shows one convention used for spherical polar coordinates, where the
point P(x, y, z) has equivalent polar coordinates P(ρ, φ, θ ), where:

```
x = ρ sin φ cos θ
y = ρ sin φ sin θ


```

Fig. 5.8 Spherical polar
coordinates

<a id='p92'></a>
<!-- Página 92 -->

72 5 Coordinate Systems

```
z = ρ cos φ

ρ = x 2 + y2 + z2
 
z
φ = arccos
ρ
y
θ = arctan .
x

```

For example, the point (3, 4, 0) has spherical polar coordinates (5, 90◦ , 53.13◦ ):
```

ρ= 32 + 42 + 02 = 5
 
φ = arccos 05 = 90◦
 
θ = arctan 43 ≈ 53.13◦ .

```

Take great care when using spherical coordinates, as authors often swap φ with θ , as
well as the alignment of the Cartesian axes; not to mention using a left-handed axial
system in preference to a right-handed system!



5.10 Cylindrical Coordinates

Figure 5.9 shows one convention used for cylindrical coordinates, where the point
P(x, y, z) has equivalent cylindrical coordinates P(ρ, θ, z), where

```
x = ρ cos θ
y = ρ sin θ
z=z

ρ = x 2 + y2
y
θ = arctan .
x

```

Fig. 5.9 Cylindrical
coordinates

<a id='p93'></a>
<!-- Página 93 -->

5.10 Cylindrical Coordinates 73

For example, the point (3, 4, 6) has cylindrical coordinates (5, 53.13◦ , 6):
```

ρ= 32 + 42 = 5
 
θ = arctan 43 ≈ 53.13◦
z = 6.

```

Again, be careful when using cylindrical coordinates to ensure compatibility.


5.11 Summary

All of the above coordinate systems are used in computer graphics. Unfortunately,
there are no rigid standards, so be prepared to adjust the formulae used in other books
and technical papers.


5.12 Worked Examples

5.12.1 Area of a Shape

Compute the area and orientation of the shape defined by the coordinates in Table 5.2.

area = 21 [(2 × 2 − 0 × 2) + (2 × 2 − 2 × 1) + (1 × 1 − 2 × 1) + (1 × 1 − 1 × 0)]
```
= 21 (4 + 2 − 1 + 1)
= 3.

```

The shape is oriented anticlockwise, as the area is positive.



5.12.2 Distance Between Two Points

Find the distance d12 between P1 (1, 1) and P2 (6, 7), and d34 between P3 (1, 1, 1)
and P4 (7, 8, 9).
```
 √
d12 = (6 − 1)2 + (7 − 1)2 = 61 ≈ 7.81
 √
d34 = (7 − 1)2 + (8 − 1)2 + (9 − 1)2 = 149 ≈ 12.21.


```

Table 5.2 Coordinates of a shape
x 0 2 2 1 1 0
y 0 0 2 2 1 1

<a id='p94'></a>
<!-- Página 94 -->

74 5 Coordinate Systems

5.12.3 Polar Coordinates
```
 
```

Convert the 2D polar coordinates 3, π2 to Cartesian form, and the point (4, 5) to
polar form.

```
ρ=3
θ = π2 [rad]
 
x = ρ cos θ = 3 cos π2 = 0
 
y = ρ sin θ = 3 sin π2 = 3
 
```

therefore, 3, π2 ≡ (0, 3).

```
x =4
y=5
 
ρ = x 2 + y 2 = 42 + 52 ≈ 6.4
y  
θ = arctan = arctan 45 ≈ 51.34◦
x

```

therefore, (4, 5) ≈ (6.4, 51.34◦ ).



5.12.4 Spherical Polar Coordinates
```
 
```

Convert the spherical polar coordinates 10, π2 , 45◦ to Cartesian form, and the
point (3, 4, 5) to spherical form.

```
ρ = 10
φ = π2 [rad] = 90◦
θ = 45◦
√
x = ρ sin φ cos θ = 10 sin 90◦ cos 45◦ = 10 22 ≈ 7.07
√
y = ρ sin φ sin θ = 10 sin 90◦ sin 45◦ = 10 22 ≈ 7.07
z = ρ cos φ = 10 cos 90◦ = 0
 
```

therefore, 10, π2 , 45◦ ≈ (7.07, 7.07, 0).

```
x =3
y=4
z=5
 
ρ = x 2 + y 2 + z 2 = 32 + 42 + 52 ≈ 7.07
```


<a id='p95'></a>
<!-- Página 95 -->

5.12 Worked Examples 75
```
 
z  5 
φ = arccos ≈ arccos 7.07 = 45◦
ρ
y  
θ = arctan = arctan 43 ≈ 53.13◦
x

```

therefore, (3, 4, 5) ≈ (7.07, 45◦ , 53.13◦ ).



5.12.5 Cylindrical Coordinates
```
 
```

Convert the 3D cylindrical coordinates 10, π2 , 5 to Cartesian form, and the point
(3, 4, 5) to cylindrical form.

```
ρ = 10
θ = π2 [rad]
z=5
 
x = ρ cos θ = 10 cos π2 = 0
 
y = ρ sin θ = 10 sin π2 = 10
z=5
 
```

therefore, 10, π2 , 5 ≡ (0, 10, 5).
Given the point (3, 4, 5), then
```

ρ= 32 + 42 = 5
 
θ = arctan 43 ≈ 53.13◦

```

therefore, (3, 4, 5) ≈ (5, 53.13◦ , 5).



Reference

1. Merzbach UC, Boyer CB (1989) A history of mathematics. Wiley

<a id='p96'></a>
<!-- Página 96 -->


## Chapter 6

Determinants




6.1 Introduction

When patterns of numbers or symbols occur over and over again, mathematicians
often devise a way to simplify their description and assign a name to them. For
example,
```
 α
4
pi i
i=1

```

is shorthand for
```
p1α1 p2α2 p3α3 p4α4

```

and
```

4
piαi
i=1

```

is shorthand for
```
p1α1 + p2α2 + p3α3 + p4α4 .

```

A determinant is another example of this process, and is a value derived from a
square matrix of terms, often associated with sets of equations. Such problems were
studied by the Babylonians around 300 BC and by the Chinese between 200 BC and
100 BC. Since then many mathematicians have been associated with the evolution of
determinants and matrices, including Augustin-Louis Cauchy (1789–1857), Arthur
Cayley (1821–1895), Girolamo Cardano (1501–1576), Johann Gauss (1777–1855),
Pierre-Simon Laplace (1749–1827), Gottfried von Leibniz, Guillaume de L’Hôpital
(1661–1704), Takakazu Seki (1642–1708) and Jan de Witt (1625–1672). To understand the rules used to compute a determinant’s value, we need to understand their
origin, which is in the solution of sets of linear equations.


© Springer-Verlag London Ltd., part of Springer Nature 2022 77
J. Vince, Mathematics for Computer Graphics, Undergraduate Topics
in Computer Science, https://doi.org/10.1007/978-1-4471-7520-9_6

<a id='p97'></a>
<!-- Página 97 -->

78 6 Determinants

6.2 Linear Equations with Two Variables

Consider the following linear equations where we want to find values of x and y that
satisfy both equations:

```
7 = 3x + 2y (6.1)
10 = 2x + 4y. (6.2)

```

A standard way to resolve this problem is to multiply (6.1) by 2 and subtract (6.2)
```
from (6.1), which removes the y-terms:

14 = 6x + 2y
10 = 2x + 4y
4 = 4x
x = 1.

```

Substituting x = 1 in (6.1) reveals the value of y:

```
7 = 3 + 2y
4 = 2y
y = 2.

```

Therefore, x = 1 and y = 2, solves (6.1) and (6.2).
The equations must be linearly independent, otherwise we only have one equation.
For example, starting with

```
7 = 3x + 2y
14 = 6x + 4y

```

is a futile exercise, as the second equation is double the first, and does not provide
any extra information.
```
To find a general solution to this problem, we start with

d1 = a1 x + b1 y (6.3)
d2 = a2 x + b2 y. (6.4)

```

Multiply (6.3) by b2 and (6.4) by b1 :

```
d1 b2 = a1 b2 x + b1 b2 y (6.5)
b1 d2 = b1 a2 x + b1 b2 y. (6.6)

```

Subtract (6.6) from (6.5):

<a id='p98'></a>
<!-- Página 98 -->

6.2 Linear Equations with Two Variables 79

```
d1 b2 − b1 d2 = a1 b2 x − b1 a2 x
= (a1 b2 − b1 a2 )x
d1 b2 − b1 d2
x= . (6.7)
a1 b2 − b1 a2

```

To find y, multiply (6.3) by a2 and (6.4) by a1 :

```
d1 a2 = a2 a1 x + b1 a2 y (6.8)
a1 d2 = a2 a1 x + a1 b2 y. (6.9)

```

Subtract (6.8) from (6.9):

```
a1 d2 − d1 a2 = a1 b2 y − b1 a2 y
= (a1 b2 − b1 a2 )y
a1 d2 − d1 a2
y= . (6.10)
a1 b2 − b1 a2

```

Observe that both (6.7) and (6.10) share the common denominator: a1 b2 − b1 a2 .
Furthermore, note the positions of a1 , b1 , a2 and b2 in the original equations:

```
a1 b1
a2 b2

```

and the denominator is formed by cross-multiplying the diagonal terms a1 b2 and
subtracting the other cross-multiplied terms b1 a2 . Placing the four terms between
two vertical lines creates a second-order determinant whose value equals:
```
 
 a1 b1 
 
 a2 b2  = a1 b2 − b1 a2 .

```

Although the name was originally given by Johann Gauss, it was Augustin-Louis
Cauchy who clarified its current modern identity.
If the original equations are linearly related by a factor λ, the determinant equals
zero:  
```
 a1 b1 
 
 λa1 λb1  = a1 λb1 − b1 λa1 = 0.

```

Observe that the numerators of (6.7) and (6.10) are also second-order determinants:
```
 
 d1 b1 
 
 d2 b2  = d1 b2 − b1 d2

```

and

<a id='p99'></a>
<!-- Página 99 -->

80 6 Determinants
```
 
 a1 d1 
 
 a2 d2  = a1 d2 − d1 a2

```

which means that Eqs. (6.7) and (6.10) can be written using determinants:
```
   
 d1 b1   a1 d1 
   
 d2 b2   a2 d2 
x= , y= .
 a1 b1   a1 b1 
   
 a2 b2   a2 b2 

```

And one final piece of algebra permits the solution to be written as

```
x y 1
 = = . (6.11)
 d1 b1   a1 d1   a1 b1 
     
 d2 b2   a2 d2   a2 b2 

```

Observe another pattern in (6.11) where the determinant is
```
 
 a1 b1 
 
 a2 b2 

```

but the d-terms replace the x-coefficients:
```
 
 d1 b1 
 
 d2 b2 

```

and then the y-coefficients  
```
 a1 d1 
 
 a2 d2  .

Returning to the original equations:

7 = 3x + 2y
10 = 2x + 4y

```

and substituting the constants in (6.11), we have

```
x y 1
 = = 
 7 2 3 7  3 2
     
 10 4   2 10  2 4

```

which, when expanded reveals

```
x y 1
= =
28 − 20 30 − 14 12 − 4
```


<a id='p100'></a>
<!-- Página 100 -->

6.2 Linear Equations with Two Variables 81


```
x y 1
= =
8 16 8
```

making x = 1 and y = 2.
Let’s try another example:

```
11 = 4x + y
5=x+y

```

and substituting the constants in (6.11), we have

```
x y 1
 = = 
 11 1   4 11  4 1
     
 5 1 1 5  1 1

```

which, when expanded reveals

```
x y 1
= =
11 − 5 20 − 11 4−1

x y 1
= =
6 9 3
```

making x = 2 and y = 3.
Now let’s see how a third-order determinant arises from the coefficients of three
equations in three unknowns.



6.3 Linear Equations with Three Variables

Consider the following set of three linear equations:

```
13 = 3x + 2y + 2z (6.12)
20 = 2x + 3y + 4z (6.13)
7 = 2x + y + z. (6.14)

```

A standard way to resolve this problem is to multiply (6.12) by 2 and subtract (6.13),
which removes the z-terms:

```
26 = 6x + 4y + 4z
20 = 2x + 3y + 4z
6 = 4x + y (6.15)
```


<a id='p101'></a>
<!-- Página 101 -->

82 6 Determinants

leaving (6.15) with two unknowns.
Next, we take (6.13) and (6.14) and remove the z-term by multiplying (6.14) by
4 and subtract (6.13):

```
28 = 8x + 4y + 4z
20 = 2x + 3y + 4z
8 = 6x + y (6.16)

```

leaving (6.16) with two unknowns. We are now left with (6.15) and (6.16):

```
6 = 4x + y
8 = 6x + y

```

which can be solved using (6.11):

```
x y 1
 = = 
6 1 4 6 4 1
     
8 1 6 8 6 1

```

therefore,

```
6−8
x= =1
4−6
32 − 36
y= = 2.
4−6

```

Substituting x = 1 and y = 2 in (6.12) reveals that z = 3.
We can generalise (6.11) for three equations using third-order determinants:

```
x y z 1
 = = = . (6.17)
 d1 b1 c1   a1 d1 c1   a1 b1 d1   a1 b1 c1 
       
 d2 b2 c2   a2 d2 c2   a2 b2 d2   a2 b2 c2 
       
 d3 b3 c3   a3 d3 c3   a3 b3 d3   a3 b3 c3 

```

Once again, there is an important pattern in (6.17) where the underlying determinant
is  
```
 a1 b1 c1 
 
 a2 b2 c2 
 
 a3 b3 c3 

```

but the d-terms replace the x-coefficients:

<a id='p102'></a>
<!-- Página 102 -->

6.3 Linear Equations with Three Variables 83
```
 
 d1 b1 c1 
 
 d2 b2 c2 
 
 d3 b3 c3 

```

the d-terms replace the y-coefficients:
```
 
 a1 d1 c1 
 
 a2 d2 c2 
 
 a3 d3 c3 

```

and the d-terms replace the z-coefficients:
```
 
 a1 b1 d1 
 
 a2 b2 d2  .
 
 a3 b3 d3 


```

We must now find a way of computing the value of a third-order determinant, which
requires the following algebraic analysis of three equations in three unknowns. We
start with three linear equations:

```
d1 = a1 x + b1 y + c1 z (6.18)
d2 = a2 x + b2 y + c2 z (6.19)
d3 = a3 x + b3 y + c3 z (6.20)

```

and derive one equation in two unknowns from (6.18) and (6.19), and another from
(6.19) and (6.20).
We multiply (6.18) by c2 , (6.19) by c1 and subtract them:

```
c2 d1 = a1 c2 x + b1 c2 y + c1 c2 z
c1 d2 = c1 a2 x + b2 c1 y + c1 c2 z
c2 d1 − c1 d2 = (a1 c2 − c1 a2 )x + (b1 c2 − b2 c1 )y. (6.21)

```

Next, we multiply (6.19) by c3 , (6.20) by c2 and subtract them:

```
c3 d2 = a2 c3 x + b2 c3 y + c2 c3 z
c2 d3 = a3 c2 x + b3 c2 y + c2 c3 z
c3 d2 − c2 d3 = (a2 c3 − a3 c2 )x + (b2 c3 − b3 c2 )y. (6.22)

```

Simplify (6.21) by letting

```
e1 = c2 d1 − c1 d2
f 1 = a1 c2 − c1 a2
g1 = b1 c2 − b2 c1
```


<a id='p103'></a>
<!-- Página 103 -->

84 6 Determinants

therefore,
```
e1 = f 1 x + g1 y. (6.23)

```

Simplify (6.22) by letting

```
e2 = c3 d2 − c2 d3
f 2 = a2 c3 − a3 c2
g2 = b2 c3 − b3 c2

```

therefore,
```
e2 = f 2 x + g2 y. (6.24)

```

Now we have two equations in two unknowns:

```
e1 = f 1 x + g1 y
e2 = f 2 x + g2 y

```

which are solved using
```
x y 1
= = (6.25)
```


## A B C

where
```
   
 e1 g1   c2 d1 − c1 d2 b1 c2 − b2 c1 

```


## A =  =   (6.26)

```
e2 g2   c3 d2 − c2 d3 b2 c3 − b3 c2 
   
 f 1 e1   a1 c2 − c1 a2 c2 d1 − c1 d2 

```


## B =  =   (6.27)

```
f 2 e2   a2 c3 − a3 c2 c3 d2 − c2 d3 
   
 f 1 g1   a1 c2 − c1 a2 b1 c2 − b2 c1 

```


## C =  =   (6.28)

```
f 2 g2   a2 c3 − a3 c2 b2 c3 − b3 c2 

```

We first compute A, from which we can derive B, because the only difference between
(6.26) and (6.27) is that d1 , d2 , d3 become a1 , a2 , a3 respectively, and b1 , b2 , b3
become d1 , d2 , d3 respectively.
```
We can derive C from A, as the only difference between (6.26) and (6.28) is that
```

d1 , d2 , d3 become a1 , a2 , a3 respectively. Starting with A:

<a id='p104'></a>
<!-- Página 104 -->

6.3 Linear Equations with Three Variables 85

```
A = (c2 d1 − c1 d2 )(b2 c3 − b3 c2 ) − (b1 c2 − b2 c1 )(c3 d2 − c2 d3 )
= b2 c2 c3 d1 − b3 c22 d1 − b2 c1 c3 d2 + b3 c1 c2 d2
− b1 c2 c3 d2 + b1 c22 d3 + b2 c1 c3 d2 − b2 c1 c2 d3
= b2 c2 c3 d1 − b3 c22 d1 + b3 c1 c2 d2 − b1 c2 c3 d2 + b1 c22 d3 − b2 c1 c2 d3
= c2 (b2 c3 d1 − b3 c2 d1 + b3 c1 d2 − b1 c3 d2 + b1 c2 d3 − b2 c1 d3 )
 
A = c2 d1 (b2 c3 − c2 b3 ) − b1 (d2 c3 − c2 d3 ) + c1 (d2 b3 − b2 d3 ) . (6.29)

```

Using the substitutions described above we can derive B and C from (6.29):
```
 
B = c2 a1 (d2 c3 − c2 d3 ) − b1 (a2 c3 − c2 a3 ) + c1 (a2 d3 − d2 a3 ) (6.30)
 
C = c2 a1 (b2 c3 − c2 b3 ) − b1 (a2 c3 − c2 a3 ) + c1 (a2 b3 − b2 a3 ) . (6.31)

```

We can now rewrite (6.29)–(6.31) using determinant notation. At the same time, we
can drop the c2 terms as they cancel out when computing x, y and z:
```
     
b c  d c  d b 
A = d1  2 2  − b1  2 2  + c1  2 2  (6.32)
b3 c3 d3 c3 d3 b3
     
 d2 c2   a2 c2   a2 d2 
B = a1   − d1   + c1   (6.33)
d3 c3   a3 c3   a3 d3 
     
b c  a c  a b 
C = a1  2 2  − b1  2 2  + c1  2 2  . (6.34)
b3 c3 a3 c3 a3 b3

```

As (6.17) and (6.25) refer to the same x and y, then
```
 
 d1 b1 c1       
       
 d2 b2 c2  = d1  b2 c2  − b1  d2 c2  + c1  d2 b2  (6.35)
   b3 c3   d3 c3   d3 b3 
 d3 b3 c3 
 
 a1 d1 c1       
       
 a2 d2 c2  = a1  d2 c2  − d1  a2 c2  + c1  a2 d2  (6.36)
   d3 c3   a3 c3   a3 d3 
 a3 d3 c3 
 
 a1 b1 c1       
       
 a2 b2 c2  = a1  b2 c2  − b1  a2 c2  + c1  a2 b2  . (6.37)
   b3 c3   a3 c3   a3 b3 
 a3 b3 c3 

```

As a consistent algebraic analysis has been pursued to derive (6.35)–(6.37), a consistent pattern has surfaced in Fig. 6.1 which shows how the three determinants are
evaluated. This pattern comprises taking each entry in the top row, called a cofactor,
and multiplying it by the determinant of entries in rows 2 and 3, whilst ignoring the
column containing the original term, called a first minor. Observe that the second
term of the top row is switched negative, called an inversion correction factor.

<a id='p105'></a>
<!-- Página 105 -->

86 6 Determinants


```
d1 b1 c1 d1 b1 c1 d1 b1 c1 d1 b1 c1

d2 b2 c2 = d2 b2 c2 - d2 b2 c2 + d2 b2 c2

d3 b3 c3 d3 b3 c3 d3 b3 c3 d3 b3 c3



a1 d1 c1 a1 d1 c1 a1 d1 c1 a1 d1 c1

a2 d2 c2 = a2 d2 c2 - a2 d2 c2 + a2 d2 c2

a3 d3 c3 a3 d3 c3 a3 d3 c3 a3 d3 c3



a1 b1 c1 a1 b1 c1 a1 b1 c1 a1 b1 c1

a2 b2 c2 = a2 b2 c2 - a2 b2 c2 + a2 b2 c2

a3 b3 c3 a3 b3 c3 a3 b3 c3 a3 b3 c3

```

Fig. 6.1 Evaluating the determinants shown in (6.35)–(6.37)



Let’s repeat (6.31) again without the c2 term, as it has nothing to do with the
calculation of the determinant.

```
C = a1 (b2 c3 − c2 b3 ) − b1 (a2 c3 − c2 a3 ) + c1 (a2 b3 − b2 a3 ). (6.38)

```

It is possible to arrange the terms of (6.38) as a square matrix such that each row and
column sums to C:

```
a1 (b2 c3 − c2 b3 ) − b1 (a2 c3 − c2 a3 ) + c1 (a2 b3 − b2 a3 )
−a2 (b1 c3 − c1 b3 ) + b2 (a1 c3 − c1 a3 ) − c2 (a1 b3 − b1 a3 )
a3 (b1 c2 − c1 b2 ) − b3 (a1 c2 − c1 a2 ) + c3 (a1 b2 − b1 a2 )

```

which means that there are six ways to evaluate the determinant C: summing the rows,
or summing the columns. Figure 6.2 shows this arrangement with the cofactors in
blue, and the first minor determinants in green. Observe how the signs alternate
between the terms.
Having discovered the origins of these patterns, let’s evaluate the original equations declared at the start of this section using (6.11)

```
13 = 3x + 2y + 2z
20 = 2x + 3y + 4z
7 = 2x + y + z.
```


<a id='p106'></a>
<!-- Página 106 -->

6.3 Linear Equations with Three Variables 87


```
a1 b1 c1 C C C

```

C = a2 b2 c2 = = =

```
a3 b3 c3 -

a1 b1 c1 a1 b1 c1 a1 b1 c1

C = a2 b2 c2 - a2 b2 c2 + a2 b2 c2

a3 b3 c3 a3 b3 c3 a3 b3 c3

- + -

a1 b1 c1 a1 b1 c1 a1 b1 c1

C = - a2 b2 c2 + a2 b2 c2 - a2 b2 c2

a3 b3 c3 a3 b3 c3 a3 b3 c3

+ - +

a1 b1 c1 a1 b1 c1 a1 b1 c1

C = a2 b2 c2 - a2 b2 c2 + a2 b2 c2

a3 b3 c3 a3 b3 c3 a3 b3 c3

```

Fig. 6.2 The patterns of multipliers with their respective second-order determinants


```
x y z 1
 = = = 
 d1 b1 c1   a1 d1 c1   a1 b1 d1   a1 b1 c1 
       
 d2 b2 c2   a2 d2 c2   a2 b2 d2   a2 b2 c2 
       
 d3 b3 c3   a3 d3 c3   a3 b3 d3   a3 b3 c3 

```

therefore,
```
x y z 1
 = = = 
 13 2 2   3 13 2   3 2 13  3 2 2
       
 20 3 4   2 20 4   2 3 20  2 3 4
       
 7 1 1 2 7 1 2 1 7  2 1 1

```

computing the determinants using the top row entries as cofactors:

```
x y z 1
= = =
−13 + 16 − 2 −24 + 78 − 52 3 + 52 − 52 −3 + 12 − 8

x y z 1
= = =
1 2 3 1
```

therefore, x = 1, y = 2 and z = 3.

<a id='p107'></a>
<!-- Página 107 -->

88 6 Determinants


```
a1 b1 c1 a1 b1 c1 a1 b1 b1 c1 a1 b1 c1
a2 b2 c2 = a2 b2 c2 a2 b2 - b2 c2 a2 b2 c2
a3 b3 c3 a3 b3 c3 a3 b3 b3 c3 a3 b3 c3

```

Fig. 6.3 The pattern behind Sarrus’s rule



6.3.1 Sarrus’s Rule

The French mathematician Pierre Sarrus (1798–1861) discovered another way to
compute the value of a third-order determinant, that arises from (6.38):

```
C = a1 (b2 c3 − c2 b3 ) − b1 (a2 c3 − c2 a3 ) + c1 (a2 b3 − b2 a3 )
= a1 b2 c3 − a1 c2 b3 − b1 a2 c3 + b1 c2 a3 + c1 a2 b3 − c1 b2 a3
= a1 b2 c3 + b1 c2 a3 + c1 a2 b3 − a1 c2 b3 − b1 a2 c3 − c1 b2 a3 . (6.39)

```

The pattern in (6.39) becomes clear in Fig. 6.3, where the first two columns of the
matrix are repeated, and comprises two diagonal sets of terms: on the left in blue,
we have the products a1 b2 c3 , b1 c2 a3 , c1 a2 b3 , and on the right in red and orange,
the products a1 c2 b3 , b1 a2 c3 , c1 b2 a3 . These diagonal patterns provide a useful aidemémoire when computing the determinant. Unfortunately, this rule only applies to
third-order determinants.



6.4 Mathematical Notation

Having discovered the background of determinants, now let’s explore a formal
description of their structure and characteristics.



6.4.1 Matrix

In the following definitions, a matrix is a square array of entries, with an equal number
of rows and columns. The entries may be numbers, vectors, complex numbers or even
partial differentials, in the case of a Jacobian. In general, each entry is identified by
two subscripts r ow col:
```
ar ow col .
```


<a id='p108'></a>
<!-- Página 108 -->

6.4 Mathematical Notation 89

A matrix with n rows and m columns has the following entries:

```
a11 a12 . . . a1m
a21 a22 . . . a2m
.. .. . . ..
. . . .
an1 an2 . . . anm

```

The entries lying on the two diagonals are identified as follows: a11 and anm lie on
the main diagonal, and a1m and an1 lie on the secondary diagonal.



6.4.2 Order of a Determinant

The order of a square determinant equals the number of rows or columns. For example, a first-order determinant contains a single entry; a second-order determinant has
two rows and two columns; and a third-order determinant has three rows and three
columns.



6.4.3 Value of a Determinant

A determinant posses a unique, single value derived from its entries. The algorithms
used to compute this value must respect the algebra associated with solving sets of
linear equations, as discussed above.
Pierre-Simon Laplace developed a way to expand the determinant of any order.
The Laplace expansion is the idea described above and shown in Fig. 6.1, where
cofactors and first minors or principal minors are used. For example, starting with
a fourth-order determinant, when any row and column are removed, the remaining entries create a third-order determinant, called the first minor of the original
determinant.
The following equation is used to control the sign of each cofactor:

```
(−1)r ow+col

```

which, for a fourth-order determinant creates:
```
 
+ − + −
 
− + − +
 
+ − + −.
 
− + − +
```


<a id='p109'></a>
<!-- Página 109 -->

90 6 Determinants

The Laplace expansion begins by choosing a convenient row or column as the source
of cofactors. Any zeros are particularly useful, as they cancel out any contribution by
the first minor determinant. It then sums the products of every cofactor in the chosen
row or column, with its associated first minor, including an appropriate inversion
correction factor to adjust the sign changes. The final result is the determinant’s
value.
A first-order determinant:  
```
 a11  = a11 .

A second-order determinant:
 
 a11 a12 
 
 a21 a22  = a11 a22 − a12 a21 .

A third-order determinant using the Laplace expansion with cofactors from the
```

first row:
```
 
 a11 a12 a13       
       
 a21 a22 a23  = a11  a22 a23  − a12  a21 a23  + a13  a21 a22  .
   a32 a33   a31 a33   a31 a32 
 a31 a32 a33 

A fourth-order determinant using the Laplace expansion with cofactors from the
```

first row:
```
   
 a22 a23 a24   a21 a23 a24 
   
a11  a32 a33 a34  − a12  a31 a33 a34  +
 a42 a43 a44   a41 a43 a44 
 
     
 a21 a22 a24   a21 a22 a23   a11 a12 a13 a14 
     a21 a22 a23 a24 
a13  a31 a32 a34  − a14  a31 a32 a33  =  

 a41 a42 a44   a41 a42 a43   a31 a32 a33 a34 
 a41 a42 a43 a44 

Sarrus’s rule is useful to compute a third-order determinant:
 
 a11 a12 a13 
 
 a21 a22 a23  =a11 a22 a33 + a12 a23 a31 + a13 a21 a32 −
 
 a31 a32 a33 
a11 a23 a32 − a12 a21 a33 + a13 a22 a31

```

The Laplace expansion works with higher-order determinants, as any first minor
can itself be expanded using the same expansion.

<a id='p110'></a>
<!-- Página 110 -->

6.4 Mathematical Notation 91

6.4.4 Properties of Determinants

If a determinant contains a row or column of zeros, the Laplace expansion implies
that the value of the determinant is zero.
```
 
3 0 2
 
 2 0 4  = 0.
 
2 0 1

```

If a determinant’s rows and columns are interchanged, the Laplace expansion also
implies that the value of the determinant is unchanged.
```
   
 3 12 2   3 2 2 
   
 2 10 4  =  12 10 8  = −2.
   
2 8 1  2 4 1

```

If any two rows, or columns, are interchanged, without changing the order of their
entries, the determinant’s numerical value is unchanged, but its sign is reversed.
```
 
 3 12 2 
 
 2 10 4  = −2
 
2 8 1
 
 12 3 2 
 
 10 2 4  = 2.
 
 8 2 1

```

If the entries of a row or column share a common factor, the entries may be adjusted,
and the factor placed outside.
```
   
 3 12 2  3 6 2
   
 2 10 4  = 2  2 5 4  = −2.
   
2 8 1 2 4 1



```

6.5 Summary

This chapter has explored the background of determinants and why they exist. In
later chapters we discover their role in matrix algebra.

<a id='p111'></a>
<!-- Página 111 -->

92 6 Determinants

6.6 Worked Examples

6.6.1 Determinant Expansion

Evaluate this determinant using the Laplace expansion and Sarrus’s rule.
```
 
1 4 7
 
2 5 8.
 
3 6 9

```

Using the Laplace expansion:
```
 
1 4 7      
       
2 5 8 = 15 8 − 24 7 + 34 7
  6 9 6 9 5 8
3 6 9
= 1(45 − 48) − 2(36 − 42) + 3(32 − 35)
= −3 + 12 − 9
= 0.

```

Using Sarrus’s rule:
```
 
1 4 7
 
2 5 8 = 1 × 5 × 9 + 4 × 8 × 3 + 7 × 2 × 6 − 7 × 5 × 3 − 1 × 8 × 6 − 4 × 2 × 9
 
3 6 9
= 45 + 96 + 84 − 105 − 48 − 72
= 0.




```

6.6.2 Complex Determinant

Evaluate the complex determinant
```
 
 4 + i2
 1 + i 
.
 2 − i3 3 + i3 
```


<a id='p112'></a>
<!-- Página 112 -->

6.6 Worked Examples 93

Using the Laplace expansion:
```
 
 4 + i2
 1 + i 
= (4 + i2)(3 + i3) − (1 + i)(2 − i3)
 2 − i3 3 + i3 
= (12 + i18 − 6) − (2 − i + 3)
= 6 + i18 − 5 + i
= 1 + i19.



```

6.6.3 Simple Expansion

Write down the simplest expansion of this determinant with its value:
```
 
1 2 3
 
4 5 0.
 
6 7 0

```

Using the Laplace expansion with cofactors from the third column:
```
 
1 2 3  
   
 4 5 0  = 3  4 5  = −6.
  6 7
6 7 0



```

6.6.4 Simultaneous Equations

Solve the following equations using determinants:

```
3 = 2x + y − z
12 = x + 2y + z
8 = 3x − 2y + 2z.

```

Using (6.17):

```
x y z 1
 = = = .
 3 1 −1   2 3 −1  2 1 3  2 1 −1 
       
 12 2 1   1 12 1   1 2 12  1 2 1
       
 8 −2 2  3 8 2  3 −2 8   3 −2 2 
```


<a id='p113'></a>
<!-- Página 113 -->

94 6 Determinants

Therefore,
```
 
 3 1 −1 

 
 12 2 1 

 
 8 −2 2 18 − 16 + 40 42
x=    = = = 2,
2 1 −1  12 + 1 + 8 21
 
1 2 1 

 
 3 −2 2
 
 2 3 −1 
 
 
 1 12 1 
 
 
3 8 2 32 + 3 + 28 63
y =   = = = 3,
2 1 −1  12 + 1 + 8 21
 
1 2 1 

 
 3 −2 2
 
2 1 3 

 
1 2 12 

 
 3 −2 8  80 + 28 − 24 84
z =   = = = 4.
2 1 −1  24 + 1 + 8 21
 
1 2 1 

 
 3 −2 2
```


<a id='p114'></a>
<!-- Página 114 -->


## Chapter 7

Vectors




7.1 Introduction

This chapter provides a comprehensive introduction to vectors. It covers 2D and
3D vectors, unit vectors, position vectors, Cartesian vectors, vector magnitude, vector products, and area calculations. It also shows how vectors are used in lighting
calculations and back-face detection.



7.2 Background

Vectors are a relative new invention in the world of mathematics, dating only from
the 19th century. They enable us to solve complex geometric problems, the dynamics
of moving objects, and problems involving forces and fields.
```
We often only require a single number to represent quantities used in our daily
```

lives such as height, age, shoe size, waist and chest measurement. The magnitude of
these numbers depends on our age and whether we use metric or imperial units. Such
quantities are called scalars. On the other hand, there are some things that require
more than one number to represent them: wind, force, weight, velocity and sound
are just a few examples. For example, any sailor knows that wind has a magnitude
and a direction. The force we use to lift an object also has a value and a direction.
Similarly, the velocity of a moving object is measured in terms of its speed (e.g.
miles per hour), and a direction such as north-west. Sound, too, has intensity and a
direction. Such quantities are called vectors.
```
Complex numbers seemed to be a likely candidate for representing forces, and
```

were being investigated by the Norwegian-Danish mathematician Caspar Wessel
(1745–1818), the French amateur mathematician Jean-Robert Argand (1768–1822)
and the English mathematician John Warren (1796–1852). At the time, complex
numbers were two-dimensional, and their 3D form was being investigated by the
Irish mathematician Sir William Rowan Hamilton (1805–1865) who invented them

© Springer-Verlag London Ltd., part of Springer Nature 2022 95
J. Vince, Mathematics for Computer Graphics, Undergraduate Topics
in Computer Science, https://doi.org/10.1007/978-1-4471-7520-9_7

<a id='p115'></a>
<!-- Página 115 -->

96 7 Vectors

in 1843, calling them quaternions. In 1853, Hamilton published his book Lectures on
Quaternions [1] in which he described terms such as vector, transvector and provector. Hamilton’s vectors were not widely accepted until in 1901, when the American
mathematician Edwin Bidwell Wilson (1879–1964) published Vector Analysis [2],
describing modern vector analysis. This was based upon a series of lectures delivered
earlier by the American scientist Josiah Gibbs (1839–1903).
Gibbs was not a fan of the imaginary quantities associated with Hamilton’s quaternions, but saw the potential of creating a vectorial system from the imaginary i, j and
k into the unit basis vectors i, j and k, which is what we use today.
Some mathematicians were not happy with the direction mathematics had taken.
The German mathematician Hermann Gunther Grassmann (1809–1877), believed
that his own geometric calculus was far superior to Hamilton’s quaternions, but
he died without managing to convince any of his fellow mathematicians. Fortunately, the English mathematician and philosopher William Kingdon Clifford (1845–
1879), recognised the brilliance of Grassmann’s ideas, and formalised what today
has become known as geometric algebra.
With the success of Gibbs’ vector analysis, quaternions faded into obscurity, only
to be rediscovered in the 1970s when they were employed by the flight simulation
community to control the dynamic behaviour of a simulator’s motion platform. A
decade later they found their way into computer graphics where they are used for
rotations about an arbitrary axis.
Now this does not mean that vector analysis is dead—far from it. Vast quantities
of scientific software depends upon the vector mathematics developed over a century
ago, and will continue to employ it for many years to come. Nevertheless, geometric
algebra is destined to emerge as a powerful mathematical framework that could
eventually replace vector analysis one day.
Readers interested in the history of vector analysis should read Michael Crowe’s
book A History of Vector Analysis [3].



7.3 2D Vectors

7.3.1 Vector Notation

A scalar such as x represents a single numeric quantity. However, as a vector contains
two or more numbers, its symbolic name is printed using a bold font to distinguish
it from a scalar variable. Examples being n, i and q.
```
When a scalar variable is assigned a value, we use the standard algebraic notation:

x = 3.

```

However, a vector has one or more numbers enclosed in brackets, written as a column
or as a row—in this text column vectors are used:

<a id='p116'></a>
<!-- Página 116 -->

7.3 2D Vectors 97
```
 
3
n= .
4

```

The numbers 3 and 4 are the components of n, and their sequence within the brackets
is important. A row vector places the components horizontally:

```
n = [3 4].

```

The difference between the two, is appreciated in the context of matrices. Sometimes
it is convenient—for presentation purposes—to write a column vector as a row vector,
in which case, it is written
```
n = [3 4]T ,

```

where the superscript T reminds us that n is really a transposed column vector.



7.3.2 Graphical Representation of Vectors

An arrow is used to represent a vector as it possesses length and direction, as shown
in Fig. 7.1. By assigning coordinates to the arrow it is possible to translate the arrow’s
length and direction into two numbers. For example, in Fig. 7.2 the vector r has its
tail defined by (x1 , y1 ) = (1, 2), and its head by (x2 , y2 ) = (3, 4). Vector s has
its tail defined by (x3 , y3 ) = (5, 3), and its head by (x4 , y4 ) = (3, 1). The x- and
y-components for r are computed as follows

```
xr = x 2 − x 1 = 3 − 1 = 2
yr = y2 − y1 = 4 − 2 = 2

```

and the components for s are computed as follows

```
xs = x4 − x3 = 3 − 5 = −2
ys = y4 − y3 = 1 − 3 = −2.


```

Fig. 7.1 An arrow with y
magnitude and direction
```
3


2


1


1 2 3 4 5 x
```


<a id='p117'></a>
<!-- Página 117 -->

98 7 Vectors

Fig. 7.2 Two vectors r and s y (x2, y2)
have the same magnitude but 4
opposite directions
```
r (x3, y3)
3
s
2 (x1, y1)

1 (x4, y4)

1 2 3 4 5 6 x




```

It is the negative value of xs and ys that encode the vector’s direction. In general, if
the coordinates of a vector’s head and tail are (x h , yh ) and (xt , yt ) respectively, its
components x and y are given by

```
x = x h − xt
y = yh − yt .

```

One can readily see from this notation that a vector does not have an absolute position.
It does not matter where we place a vector, so long as we preserve its length and
orientation, its components are unaltered.



7.3.3 Magnitude of a Vector

The magnitude or length of a vector r is written r and computed using the theorem
of Pythagoras: 
```
r = (x)2 + (y)2

```

and used as follows. Consider a vector defined by

```
(x h , yh ) = (4, 5)
(xt , yt ) = (1, 1)

```

where the
```
√ x- and y-components are 3 and 4 respectively. Therefore its magnitude
```

equals 32 + 42 = 5. The magnitude of a vector is also written as |r|, with single
vertical lines.
Figure 7.3 shows eight vectors, and their geometric properties are listed in
Table 7.1.

<a id='p118'></a>
<!-- Página 118 -->

7.4 3D Vectors 99

Fig. 7.3 Eight vectors y
whose coordinates are shown 2
in Table 7.1
```
1


-3 -2 -1 1 2 3 x

-1

-2




```

Table 7.1 Values associated with the eight vectors in Fig. 7.3
xh yh xt yt x y vector
2 0 0 0 2 0 2
0 2 0 0 0 2 2
−2 0 0 0 −2 0 2
0 −2 0 0 0 −2 2
```
√
```

1 1 0 0 1 1 2
```
√
```

−1 1 0 0 −1 1 2
```
√
```

−1 −1 0 0 −1 −1 2
```
√
```

1 −1 0 0 1 −1 2




7.4 3D Vectors

The above vector examples are in 2D, but it is easy to extend this notation to embrace
an extra dimension. Figure 7.4 shows a 3D vector r with its head, tail, components
and magnitude annotated. The vector, its components and magnitude are given by

```
r = [x y z]T


```

Fig. 7.4 The vector r has
components x, y, z

<a id='p119'></a>
<!-- Página 119 -->

100 7 Vectors

```
x = x h − xt
y = yh − yt
z = z h − z t

r = (x)2 + (y)2 + (z)2 .

```

All future examples are three-dimensional.



7.4.1 Vector Manipulation

As vectors are different to scalars, there are rules to control how the two mathematical
entities interact with one another. For instance, we need to consider vector addition,
subtraction and products, and how a vector is scaled.



7.4.2 Scaling a Vector

Given a vector n, 2n means that the vectors components are scaled by a factor of 2.
For example, given ⎡ ⎤ ⎡ ⎤
```
3 6
n = ⎣4⎦ , then 2n = ⎣ 8 ⎦
5 10

```

which seems logical. Similarly, if we divide n by 2, its components are halved. Note
that the vector’s direction remains unchanged—only its magnitude changes.
In general, given
```
⎡ ⎤ ⎡ ⎤
n1 λn 1
n = ⎣n 2 ⎦ , then λn = ⎣λn 2 ⎦ , where λ ∈ R.
n3 λn 3

```

There is no obvious way we can resolve the expression 2 + n, for it is not clear
which component of n is to be increased by 2. However, if we can add a scalar to an
imaginary (e.g. 2 + 3i), why can’t we add a scalar to a vector (e.g. 2 + n)? Well, the
answer to this question is two-fold: First, if we change the meaning of ‘add’ to mean
‘associated with’, then there is nothing to stop us from ‘associating’ a scalar with
a vector, like complex numbers. Second, the axioms controlling our algebra must
be clear on this matter. Unfortunately, the axioms of traditional vector analysis do
not support the ‘association’ of scalars with vectors in this way. However, geometric
algebra does! Furthermore, geometric algebra even permits division by a vector,
which does sound strange. Consequently, whilst reading the rest of this chapter keep
an open mind about what is permitted, and what is not permitted. At the end of the

<a id='p120'></a>
<!-- Página 120 -->

7.4 3D Vectors 101

day, virtually anything is possible, so long as we have a well-behaved axiomatic
system.



7.4.3 Vector Addition and Subtraction

Given vectors r and s, r ± s is defined as
```
⎡ ⎤ ⎡ ⎤ ⎡ ⎤
xr xs xr ± x s
r = ⎣ yr ⎦ , s = ⎣ ys ⎦ , then r ± s = ⎣ yr ± ys ⎦ .
zr zs zr ± z s

```

Vector addition is commutative:

```
a+b=b+a
⎡ ⎤ ⎡ ⎤ ⎡ ⎤ ⎡ ⎤
1 4 4 1
e.g. ⎣2⎦ + ⎣5⎦ = ⎣5⎦ + ⎣2⎦ .
3 6 6 3

```

However, like scalar subtraction, vector subtraction is not commutative:

```
a − b = b − a
⎡ ⎤ ⎡ ⎤ ⎡ ⎤ ⎡ ⎤
4 1 1 4
e.g. ⎣5⎦ − ⎣2⎦ = ⎣2⎦ − ⎣5⎦ .
6 3 3 6

```

Let’s illustrate vector addition and subtraction with two examples. Figure 7.5 shows
the graphical interpretation of adding two vectors r and s. Note that the tail of
vector s is attached to the head of vector r. The resultant vector t = r + s is defined
by adding the corresponding components of r and s together. Figure 7.6 shows a
graphical interpretation for r − s. This time, the components of vector s are reversed


Fig. 7.5 Vector addition
r+s

<a id='p121'></a>
<!-- Página 121 -->

102 7 Vectors

Fig. 7.6 Vector subtraction
r−s




to produce an equal and opposite vector. Then it is attached to r and added as described
above.



7.4.4 Position Vectors

Given any point P(x, y, z), a position vector p is created by assuming that P is
the vector’s head and the origin is its tail. As the tail coordinates are (0, 0, 0) the
vector’s
 components are x, y, z. Consequently, the vector’s magnitude p equals
x 2 + y2 + z2.



7.4.5 Unit Vectors

By definition, a unit vector has a magnitude of 1. A simple example is i, where

```
i = [1 0 0]T , where i = 1.

```

Unit vectors are extremely useful in the product of two vectors, where their magnitudes are required; and if these are unit vectors, the computation is greatly simplified.
Converting a vector into a unit form is called normalising, and is achieved by
dividing its components by the vector’s magnitude. To  formalise this process, consider a vector r = [x y z]T , with magnitude r = x 2 + y 2 + z 2 . The unit form
of r is given by
```
1
r̂ = [x y z]T
r

```

This is confirmed by showing that the magnitude of r̂ is 1:

```
2 2 2
x y z
r̂ = + +
r r r
```


<a id='p122'></a>
<!-- Página 122 -->

7.4 3D Vectors 103

```
1  2
= x + y2 + z2
r
r̂ = 1.



```

7.4.6 Cartesian Vectors

A Cartesian vector is constructed from three unit vectors: i, j and k, aligned with
the x-, y- and z-axis, respectively:

```
i = [1 0 0]T , j = [0 1 0]T , k = [0 0 1]T .

```

Therefore, any vector aligned with the x-, y- or z-axis is a scalar multiple of the
associated unit vector. For example, 10i is aligned with the x-axis, with a magnitude
of 10. 20k is aligned with the z-axis, with a magnitude of 20. By employing the rules
of vector addition and subtraction, we can compose a vector r by summing three
scaled Cartesian unit vectors as follows

```
r = ai + bj + ck

```

which is equivalent to
```
r = [a b c]T

```

where the magnitude of r is
```

r = a 2 + b2 + c2 .

```

Any pair of Cartesian vectors, such as r and s, can be combined as follows

```
r = ai + bj + ck
s = di + ej + f k
r ± s = (a ± d)i + (b ± e)j + (c ± f )k.



```

7.4.7 Products

The product of two scalars is very familiar: for example, 6 × 7 or 7 × 6 = 42. We
often visualise this operation as a rectangular area, where 6 and 7 are the dimensions
of a rectangle’s sides, and 42 is the area. However, a vector’s qualities are its length
and orientation, which means that any product must include them in any calculation.
The length is easily calculated, but we must know the angle between the two vectors as
this reflects their relative orientation. Although the angle can be incorporated within

<a id='p123'></a>
<!-- Página 123 -->

104 7 Vectors

the product in various ways, two particular ways lead to useful results. For example,
the product of r and s, separated by an angle θ could be rs cos θ or rs sin θ .
It just so happens that cos θ forces the product to result in a scalar quantity, and
sin θ creates a vector. Consequently, there are two products to consider: the scalar
product, and the vector product, which are written as r · s and r × s respectively.



7.4.8 Scalar Product

Figure 7.7 shows two vectors r and s that have been drawn, for convenience, with their
tails touching. Taking s as the reference vector—which is an arbitrary choice—we
compute the projection of r on s, which takes into account their relative orientation.
The length of r on s is r cos β. We can now multiply the magnitude of s by the
projected length of r: sr cos β This scalar product is written

```
r · s = rs cos β. (7.1)

```

Because of the dot symbol ‘·’, the scalar product is also called the dot product.
Fortunately, everything is in place to perform this task. To begin with, we define
two Cartesian vectors r and s, and proceed to multiply them together using (7.1):

```
r =ai + bj + ck
s =di + ej + f k
r · s =(ai + bj + ck) · (di + ej + f k)
=ai · (di + ej + f k)
+ bj · (di + ej + f k)
+ ck · (di + ej + f k)
=adi · i + aei · j + a f i · k
+ bdj · i + bej · j + b f j · k
+ cdk · i + cek · j + c f k · k.


```

Fig. 7.7 The projection of r
on s

<a id='p124'></a>
<!-- Página 124 -->

7.4 3D Vectors 105

Before we proceed any further, we can see that we have created various dot product
terms such as i · i, i · j, i · k , etc. These terms can be divided into two groups: those
that reference the same unit vector, and those that reference different unit vectors.
```
Using the definition of the dot product (7.1), terms such as i · i, j · j and
```

k · k = 1 , because the angle between i and i, j and j, or k and k, is 0◦ ; and cos 0◦ = 1.
But as the other vector combinations are separated by 90◦ , and cos 90◦ = 0, all
remaining terms collapse to zero, and we are left with

```
r · s = adi · i + bej · j + c f k · k.

```

But as the the magnitude of a unit vector is 1, we can write

```
r · s = rs cos θ = ad + be + c f

```

which confirms that the dot product is indeed a scalar quantity.
It is worth pointing out that the angle returned by the dot product ranges between
0◦ and 180◦ . This is because, as the angle between two vectors increases beyond
180◦ the returned angle θ is always the smallest angle associated with the geometry.



7.4.9 The Dot Product in Lighting Calculations

Lambert’s law states that the intensity of illumination on a diffuse surface is proportional to the cosine of the angle between the surface normal vector and the light
source direction. Figure 7.8 shows a scenario where a light source is located at (20,
20, 40), and the illuminated point is (0, 10, 0). In this situation we are interested
in calculating cos β, which, when multiplied by the light source intensity, gives the
incident light intensity on the surface. To begin with, we are given the normal vector
n̂ to the surface. In this case n̂ is a unit vector: i.e. n̂ = 1:

```
n̂ = [0 1 0]T

```

The direction of the light source from the surface is defined by the vector s:
```
⎡ ⎤ ⎡ ⎤
20 − 0 20
s = ⎣20 − 10⎦ = ⎣10⎦
40 − 0 40

```

Fig. 7.8 The geometry n̂
associated with Lambert’s
```
s
```

law Light Source

```
β
```


<a id='p125'></a>
<!-- Página 125 -->

106 7 Vectors
```

s = 202 + 102 + 402 ≈ 45.826
n̂s cos β = 0 × 20 + 1 × 10 + 0 × 40 = 10
1 × 45.826 × cos β = 10
10
cos β = ≈ 0.218.
45.826
```

Therefore the light intensity at the point (0, 10, 0) is 0.218 of the original light
intensity at (20, 20, 40), but does not take into account the attenuation due to the
inverse-square law of light propagation.



7.4.10 The Scalar Product in Back-Face Detection

A simple way to identify back-facing polygons relative to the virtual camera, is to
compute the angle between the polygon’s surface normal and the line of sight between
the camera and the polygon. If this angle is less than 90◦ , the polygon is visible; if it
equals or exceeds 90◦ , the polygon is invisible. This geometry is shown in Fig. 7.9.
Although it is obvious from Fig. 7.9 that the right-hand polygon is invisible to the
camera, let’s prove algebraically that this is so.
```
For example, if the virtual camera is located at (0, 0, 0) and the polygon’s vertex
```

is (10, 10, 40). The normal vector is n = [5 5 − 2]T .

```
n = [5 5 − 2]T

n = 52 + 52 + (−2)2 ≈ 7.348.

```

The camera vector c is
```
⎡ ⎤ ⎡ ⎤
0 − 10 −10
c = ⎣0 − 10⎦ = ⎣−10⎦
0 − 40 −40

c = (−10)2 + (−10)2 + (−40)2 ≈ 42.426


```

Fig. 7.9 Back-face detection
```
visible


< 90◦
≥ 90◦


invisible

virtual camera
```


<a id='p126'></a>
<!-- Página 126 -->

7.4 3D Vectors 107

therefore,

```
nc cos β = 5 × (−10) + 5 × (−10) + (−2) × (−40)
7.348 × 42.426 × cos β = −20
−20
cos β = ≈ −0.0634
7.348 × 42.426
β = cos−1 (−0.0634) ≈ 93.64◦

```

which shows that the polygon is invisible for the camera.



7.4.11 The Vector Product

As mentioned above, the vector product r × s creates a third vector whose magnitude
equals rs sin θ , where θ is the angle between the original vectors. Figure 7.10
reminds us that the area of a parallelogram formed by r and s equals rs sin θ .
Because of the cross symbol ‘×’, the vector product is also called the cross product.

```
r×s=t (7.2)
t = rs sin θ.


```

We will discover that the vector t is normal (90◦ ) to the plane containing the vectors
r and s, as shown in Fig. 7.11, which makes it an ideal way of computing the vector
normal to a surface. Once again, let’s define two vectors and this time multiply them
together using (7.2):

```
r =ai + bj + ck
s =di + ej + f k
r × s =(ai + bj + ck) × (di + ej + f k)
=ai × (di + ej + f k)


```

Fig. 7.10 The area of the r
parallelogram formed by r
and s s
```
s

|s|sin




r
```


<a id='p127'></a>
<!-- Página 127 -->

108 7 Vectors

Fig. 7.11 The vector
product




```
+ bj × (di + ej + f k)
ck × (di + ej + f k)
=adi × i + aei × j + a f i × k
+ bdj × i + bej × j + b f j × k
+ cdk × i + cek × j + c f k × k.

```

As we found with the dot product, there are two groups of vector terms: those that
reference the same unit vector, and those that reference different unit vectors.
Using the definition for the cross product (7.2), operations such as i × i, j × j and
k × k result in a vector whose magnitude is 0. This is because the angle between
the vectors is 0◦ , and sin 0◦ = 0. Consequently these terms disappear and we are left
with

```
r × s = aei × j + a f i × k + bdj × i + b f j × k + cdk × i + cek × j. (7.3)

```

Sir William Rowan Hamilton struggled for many years when working on quaternions
to resolve the meaning of a similar result. At the time, he was not using vectors, as
they had yet to be defined, but the imaginary terms i, j and k. Hamilton’s problem was to resolve the products i j, jk, ki and their opposites ji, k j and ik. What
did the products mean? He reasoned that i j = k, jk = i and ki = j, but could not
resolve their opposites. One day in 1843, when he was out walking, thinking about
this problem, he thought the impossible: i j = k, but ji = −k, jk = i, but k j = −i,
and ki = j, but ik = − j. To his surprise, this worked, but it contradicted the commutative multiplication law of scalars where 6 × 7 = 7 × 6. We now accept that the
commutative multiplication law is there to be broken!
Let’s continue with Hamilton’s rules and reduce the cross product terms of (7.3)
to
```
r × s = aek − a f j − bdk + b f i + cdj − cei. (7.4)

```

Equation (7.4) can be tidied up to bring like terms together:

<a id='p128'></a>
<!-- Página 128 -->

7.4 3D Vectors 109

```
r × s = (b f − ce)i + (cd − a f )j + (ae − bd)k. (7.5)

```

Now let’s repeat the original vector equations to see how Eq. (7.5) is computed:

```
r = ai + bj + ck
s = di + ej + f k
r × s = (b f − ce)i + (cd − a f )j + (ae − bd)k. (7.6)

To compute the i scalar term we consider the scalars associated with the other
```

two unit vectors, i.e. b, c, e, and f , and cross-multiply and subtract them to form
(b f − ce).
```
To compute the j scalar term we consider the scalars associated with the other
```

two unit vectors, i.e. a, c, d, and f , and cross-multiply and subtract them to form
(cd − a f ).
```
To compute the k scalar term we consider the scalars associated with the other
```

two unit vectors, i.e. a, b, d, and e, and cross-multiply and subtract them to form
(ae − bd).
```
The middle operation seems out of step with the other two, but in fact it pre-
```

serves a cyclic symmetry often found in mathematics. Nevertheless, some authors
reverse the sign of the j scalar term and cross-multiply and subtract the terms to
produce −(a f − cd) which maintains a visual pattern for remembering the crossmultiplication. Equation (7.6) now becomes

```
r × s = (b f − ce)i − (a f − cd)j + (ae − bd)k. (7.7)

```

However, we now have to remember to introduce a negative sign for the j scalar term!
We can write (7.7) using determinants as follows:

```
b c a c ab
r×s= i− j+ k.
e f d f d e

```

or

```
b c c a ab
r×s= i+ j+ k.
e f f d d e

```

Therefore, to derive the cross product of two vectors we first write the vectors in the
correct sequence. Remembering that r × s does not equal s × r. Second, we compute
the three scalar terms and form the resultant vector, which is perpendicular to the
plane containing the original vectors.
So far, we have assumed that

```
r×s=t
t = rs sin θ
```


<a id='p129'></a>
<!-- Página 129 -->

110 7 Vectors

where θ is the angle between r and s, and t is perpendicular to the plane containing
r and s. Now let’s prove that this is the case:

```
r · s = rs cos θ = xr xs + yr ys + zr z s
(xr xs + yr ys + zr z s )2
cos2 θ =
r2 s2
t = rs sin θ
t2 = r2 s2 sin2 θ

= r2 s2 1 − cos2 θ
(xr xs + yr ys + zr z s )2
= r2 s2 1 −
r2 s2
= r2 s2 − (xr xs + yr ys + zr z s )2
 
= xr2 + yr2 + zr2 xs2 + ys2 + z s2 − (xr xs + yr ys + zr z s )2
  
= xr2 ys2 + z s2 + yr2 xs2 + z s2 + zr2 xs2 + ys2
− 2xr xs yr ys − 2xr xs zr z s − 2yr ys zr z s
= xr2 ys2 + xr2 z s2 + yr2 xs2 + yr2 z s2 + zr2 xs2 + zr2 ys2
− 2xr xs yr ys − 2xr xs zr z s − 2yr ys zr z s
= (yr z s − zr ys )2 + (zr xs − xr z s )2 + (xr ys − yr xs )2

```

which in determinant form is
```
2 2 2
yr zr z r xr xr yr
t2 = + +
ys z s z s xs xs ys

```

and confirms that t is the vector

```
yr zr z x x y
t= i + r r j + r r k.
ys z s z s xs xs ys

```

All that remains is to prove that t is orthogonal (perpendicular) to r and s, which is
achieved by showing that r · t = s · t = 0:

```
r = xr i + yr j + zr k
s = xs i + ys j + z s k
t = (yr z s − zr ys )i + (zr xs − xr z s )j + (xr ys − yr xs )k
r · t = xr (yr z s − zr ys ) + yr (zr xs − xr z s ) + zr (xr ys − yr xs )
= xr yr z s − xr ys zr + xs yr zr − xr yr z s + xr ys zr − xs yr zr = 0
s · t = xs (yr z s − zr ys ) + ys (zr xs − xr z s ) + z s (xr ys − yr xs )
= xs yr z s − xs ys zr + xs ys zr − xr ys z s + xr ys z s − xs yr z s = 0
```


<a id='p130'></a>
<!-- Página 130 -->

7.4 3D Vectors 111

Fig. 7.12 Vector t is normal
to the vectors r and s




Table 7.2 Coordinates of the vertices used in Fig. 7.12
Vertex x y z

## P1 0 0 1


## P2 1 0 0


## P3 0 1 0





and we have proved that r × s = t, where t = rs sin θ and t is orthogonal to
the plane containing r and s.
Let’s now consider two vectors r and s and compute the normal vector t. The
vectors are chosen so that we can anticipate approximately the answer. For the sake
of clarity, the vector equations include the scalar multipliers 0 and 1. Normally,
these are omitted. Figure 7.12 shows the vectors r and s and the normal vector t,
and Table 7.2 contains the coordinates of the vertices forming the two vectors which
confirms what we expected from Fig. 7.12.

```
r = [(x3 − x2 ) (y3 − y2 ) (z 3 − z 2 )]T
s = [(x1 − x2 ) (y1 − y2 ) (z 1 − z 2 )]T
```


## P1 = (0, 0, 1)


## P2 = (1, 0, 0)


## P3 = (0, 1, 0)

```
r = −1i + 1j + 0k
s = −1i + 0j + 1k
r × s = [1 × 1 − 0 × 0]i
− [−1 × 1 − (−1) × 0]j
+ [−1 × 0 − (−1) × 1]k
t =i+j+k
```


<a id='p131'></a>
<!-- Página 131 -->

112 7 Vectors

Now let’s reverse the vectors to illustrate the importance of vector sequence.

```
s = −1i + 0j + 1k
r = −1i + 1j + 0k
s × r = [0 × 0 − 1 × 1]i
− [−1 × 0 − (−1) × 1]j
+ [−1 × 1 − (−1) × 0]k
t = −i − j − k

```

which is in the opposite direction to r × s and confirms that the vector product is
non-commutative.



7.4.12 The Right-Hand Rule

The right-hand rule is an aide mémoire for working out the orientation of the cross
product vector. Given the operation r × s, if the right-hand thumb is aligned with r,
the first finger with s, and the middle finger points in the direction of t. However, we
must remember that this only holds in 3D. In 4D and above, it makes no sense.



7.5 Deriving a Unit Normal Vector for a Triangle

Figure 7.13 shows a triangle with vertices defined in an anticlockwise sequence from
its visible side. This is the side from which we want the surface normal to point.
Using the following information we will compute the surface normal using the cross
product and then convert it to a unit normal vector.



Fig. 7.13 The normal vector
t is derived from the cross
product r × s

<a id='p132'></a>
<!-- Página 132 -->

7.5 Deriving a Unit Normal Vector for a Triangle 113

Create vector r between P3 and P1 , and vector s between P3 and P2 :

```
r = −1i + 1j + 0k
s = −1i + 0j + 2k
r × s = (1 × 2 − 0 × 0)i
− (−1 × 2 − 0 × −1)j
+ (−1 × 0 − 1 × −1)k
t = 2i + 2j + 1k
 √
t = 22 + 22 + 12 = 5
t̂u = √25 i + √25 j + √15 k.

```

The unit vector t̂ u can now be used for illumination calculations in computer graphics,
and as it has unit length, dot product calculations are simplified.



7.6 Surface Areas

Figure 7.14 shows two vectors r and s, where the height h = |s| sin θ . Therefore the
area of the associated parallelogram is

```
area = r h = rs sin θ.


```

But this is the magnitude of the cross product vector t. Thus when we calculate r × s,
the length of the normal vector t equals the area of the parallelogram formed by r
and s; which means that the triangle formed by halving the parallelogram is half the
area.

```
area of parallelogram = t
area of triangle = 21 t.


```

Fig. 7.14 The area of the
parallelogram formed by two
vectors r and s

<a id='p133'></a>
<!-- Página 133 -->

114 7 Vectors

Fig. 7.15 The area of the
triangle formed by the
vectors r and s




This makes it relatively easy to calculate the surface area of an object constructed
```
from triangles or parallelograms. In the case of a triangulated surface, we simply
```

sum the magnitudes of the normals and halve the result.



7.6.1 Calculating 2D Areas

Figure 7.15 shows a triangle with vertices P0 (x0 , y0 ), P1 (x1 , y1 ) and P2 (x2 , y2 )
formed in an anticlockwise sequence. The vectors r and s are computed as follows:

```
r = (x1 − x0 )i + (y1 − y0 )j
s = (x2 − x0 )i + (y2 − y0 )j
r × s = (x1 − x0 )(y2 − y0 ) − (x2 − x0 )(y1 − y0 )
= x1 (y2 − y0 ) − x0 (y2 − y0 ) − x2 (y1 − y0 ) + x0 (y1 − y0 )
= x1 y2 − x1 y0 − x0 y2 + x0 y0 − x2 y1 + x2 y0 + x0 y1 − x0 y0
= x1 y2 − x1 y0 − x0 y2 − x2 y1 + x2 y0 + x0 y1
= (x0 y1 − x1 y0 ) + (x1 y2 − x2 y1 ) + (x2 y0 − x0 y2 ).

```

But the area of the triangle formed by the three vertices is 21 r × s. Therefore

```
area = 21 [(x0 y1 − x1 y0 ) + (x1 y2 − x2 y1 ) + (x2 y0 − x0 y2 )]

```

which is the formula disclosed in Chap. 5!



7.7 Summary

Vectors are extremely useful and relatively easy to use. They are vital to rendering
algorithms and shaders, and most of the time we only need to use the scalar and cross
products.

<a id='p134'></a>
<!-- Página 134 -->

7.7 Summary 115

I have tried to prepare you for an alternative algebra for vectors: geometric algebra. As we shall see later on, geometric algebra shows that mathematics may have
taken the wrong direction when it embraced Gibbs’ vector analysis. Hermann Grassmann could have been right all along. If the mathematicians of the day had adopted
Grassmann’s ideas, today we would be familiar with vectors, bivectors, trivectors,
quaternions, etc. But we are where we are, and we must prepare ourselves for some
new ideas.
Even if you already knew something about vectors, I hope that this chapter has
introduced some new ideas and illustrated the role vectors play in computer graphics.



7.8 Worked Examples

7.8.1 Position Vector

Calculate the magnitude of the position vector p, for the point P(4, 5, 6):
```

p = [4 5 6]T , therefore, p = 42 + 52 + 62 ≈ 8.77.



```

7.8.2 Unit Vector

Convert r to a unit vector.

```
r = [1 2 3]T
 √
r = 12 + 22 + 32 = 14
r̂ = √114 [1 2 3]T ≈ [0.267 0.535 0.802]T .



```

7.8.3 Vector Magnitude

Compute the magnitude of r + s.

```
r = 2i + 3j + 4k
s = 5i + 6j + 7k
r + s = 7i + 9j + 11k

r + s = 72 + 92 + 112 ≈ 15.84.
```


<a id='p135'></a>
<!-- Página 135 -->

116 7 Vectors

7.8.4 Angle Between Two Vectors

Find the angle between r and s.

```
r = [2 0 4]T
s = [5 6 10]T

r = 22 + 02 + 42 ≈ 4.472

s = 52 + 62 + 102 ≈ 12.689.

```

Therefore,

```
rs cos θ = 2 × 5 + 0 × 6 + 4 × 10 = 50
12.689 × 4.472 × cos θ = 50
50
cos θ = ≈ 0.8811
12.689 × 4.472
θ = arccos 0.8811 ≈ 28.22◦ .

```

The angle between the two vectors is approximately 28.22◦ .



7.8.5 Vector Product

To show that the vector product works with the unit vectors i, j and k. We start with

```
r = 1i + 0j + 0k
s = 0i + 1j + 0k

```

and then compute (7.7):

```
r × s = (0 × 0 − 0 × 1)i − (1 × 0 − 0 × 0)j + (1 × 1 − 0 × 0)k.

```

The i scalar and j scalar terms are both zero, but the k scalar term is 1, which makes
i × j = k.
Let’s see what happens when we reverse the vectors. This time we start with

```
r = 0i + 1j + 0k
s = 1i + 0j + 0k

```

and then compute (7.7)

```
r × s = (1 × 0 − 0 × 0)i − (0 × 0 − 0 × 1)j + (0 × 0 − 1 × 1)k.
```


<a id='p136'></a>
<!-- Página 136 -->

7.8 Worked Examples 117

The i scalar and j scalar terms are both zero, but the k scalar term is −1, which makes
j × i = −k. So we see that the vector product is antisymmetric, i.e. there is a sign
reversal when the vectors are reversed. Similarly, it can be shown that

```
j×k =i
k×i=j
k × j = −i
i × k = −j.




```

References

1. Hamilton WR (1853) Lectures on quaternions. Macmillan & Co., Cambridge
2. Wilson EB (1901) Vector analysis. Yale University Press, New Haven
3. Crowe MJ (1994) A history of vector analysis. Dover Publications Inc., New York

<a id='p137'></a>
<!-- Página 137 -->


## Chapter 8

Matrix Algebra




8.1 Introduction

This chapter introduces matrix algebra, which is a notation widely used in computer
graphics. Matrices are used to scale, translate, reflect, shear and rotate 2D shapes
and 3D objects, and like determinants, have their background in algebra and offer
another way to represent and manipulate equations. Matrices can be added, subtracted
and multiplied together, and even inverted, however, they must give the same result
obtained through traditional algebraic techniques. Once you have understood the
idea behind matrix notation, feel free to go to the next chapter and study their role
in geometric transforms, and come back to the more advanced ideas in this chapter.


8.2 Background

Matrix notation was researched by Arthur Cayley around 1858. Cayley formalised
matrix algebra, along with the American mathematicians Charles Peirce (1839–1914)
and his father, Benjamin Peirce (1809–1880). Previously, Johann Gauss had shown
that transforms were not always commutative, i.e. T1 T2 = T2 T1 , (where T1 and T2
are transforms) and matrix notation clarified such observations.
Consider the linear transform T1 , where x and y are transformed into x  and y 
respectively:
```

x  = ax + by
```


## T1 = (8.1)

```
y  = cx + dy

```

and a second linear transform T2 , where x  and y  are transformed into x  and y 
respectively:
```

x  = Ax  + By 
```


## T2 = . (8.2)

```
y  = C x  + Dy 
```

© Springer-Verlag London Ltd., part of Springer Nature 2022 119
J. Vince, Mathematics for Computer Graphics, Undergraduate Topics
in Computer Science, https://doi.org/10.1007/978-1-4471-7520-9_8

<a id='p138'></a>
<!-- Página 138 -->

120 8 Matrix Algebra

Substituting (8.1) in (8.2) we get
```

x  = A(ax + by) + B(cx + dy)
```


## T3 =

```
y  = C(ax + by) + D(cx + dy)

```

which simplifies to
```

x  = (Aa + Bc)x + (Ab + Bd)y
```


## T3 = . (8.3)

```
y  = (Ca + Dc)x + (Cb + Dd)y

```

Having derived the algebra for T3 , let’s examine matrix notation, where constants
are separated from the variables. For example, the transform (8.4)

```
x  = ax + by
(8.4)
y  = cx + d y

```

can be written in matrix form as:
```
    
x ab x
= (8.5)
y cd y

```

where (8.5) contains two different structures: two single-column matrices or column
vectors    
```
x x
and ,
y y

```

and a 2 × 2 matrix:  
```
ab
.
cd

```

Algebraically, (8.4) and (8.5) are identical, which dictates the way (8.5) is converted
to (8.4). Therefore, using (8.5) we have x  followed by the ‘=’ sign, and the sum of
the products of the top row of constants a and b with the x and y in the last column
vector:
```
x  = ax + by.

```

Next, we have y  followed by the ‘=’ sign, and the sum of the products of the bottom
row of constants c and d with the x and y in the last column vector:

```
y  = cx + d y.

```

As an example,
```
    
x 34 x
=
y 56 y
```


<a id='p139'></a>
<!-- Página 139 -->

8.2 Background 121

is equivalent to

```
x  = 3x + 4y
y  = 5x + 6y.

```

We can now write T1 and T2 using matrix notation:
```
 
  
x x ab
```


## T1 = = (8.6)

```
y y cd
     
x A B x
```


## T2 = = (8.7)

```
y  C D y

```

and substituting (8.6) in (8.7) we have
```
     
x  A B ab x
```


## T3 = = . (8.8)

```
y  C D cd y

```

But we have already computed T3 (8.3), which in matrix form is:
```
    
x  Aa + Bc Ab + Bd x
```


## T3 = = (8.9)

```
y  Ca + Dc Cb + Dd y

```

which implies that
```
    
A B ab Aa + Bc Ab + Bd
=
C D cd Ca + Dc Cb + Dd

```

and demonstrates how matrices must be multiplied. Here are the rules for matrix
multiplication:     
```
A B a ··· Aa + Bc · · ·
= .
··· ··· c ··· ··· ···

```

1: The top left-hand corner element Aa + Bc is the product of the top row of the
first matrix by the left column of the second matrix.
```
    
A B ··· b · · · Ab + Bd
= .
··· ··· ··· d ··· ···

```

2: The top right-hand element Ab + Bd is the product of the top row of the first
matrix by the right column of the second matrix.
```
    
··· ··· a ··· ··· ···
= .
C D c ··· Ca + Dc · · ·

```

3: The bottom left-hand element Ca + Dc is the product of the bottom row of the
first matrix by the left column of the second matrix.

<a id='p140'></a>
<!-- Página 140 -->

122 8 Matrix Algebra
```
    
··· ··· ··· b ··· ···
= .
C D ··· d · · · Cb + Dd

```

4: The bottom right-hand element Cb + Dd is the product of the bottom row of the
first matrix by the right column of the second matrix.
```
Let’s multiply the following matrices together:
      
24 35 (2 × 3 + 4 × 7) (2 × 5 + 4 × 9) 34 46
= = .
68 79 (6 × 3 + 8 × 7) (6 × 5 + 8 × 9) 74 102



```

8.3 Matrix Notation

Having examined the background to matrices, we can now formalise their notation.
A matrix is an array of numbers (real, imaginary, complex, etc.) organised in m
rows and n columns, where each entry ai j belongs to the ith row and jth column:
```
⎡ ⎤
a11 a12 a13 · · · a1n
⎢ a21 a22 a23 · · · a2n ⎥
⎢ ⎥
⎢ ⎥
A = ⎢ a31 a32 a33 · · · a3n ⎥ .
⎢ .. .. .. . . .. ⎥
⎣ . . . . . ⎦
am1 am2 am3 · · · amn

```

It is also convenient to express the above definition as

```
A = [ai j ]m n .



```

8.3.1 Matrix Dimension or Order

The dimension or order of a matrix is the expression m × n where m is the number
of rows, and n is the number of columns.



8.3.2 Square Matrix

A square matrix has the same number of rows as columns:
```
⎡ ⎤
a11 a12 . . . a1n ⎡ ⎤
⎢ a21 a22 . . . a2n ⎥ 1 −2 4
⎢ ⎥
A = [ai j ]n n = ⎢ . . . . ⎥ , e.g. ⎣ 6 5 7 ⎦ .
⎣ .. .. . . .. ⎦ 4 31
an1 an2 . . . ann
```


<a id='p141'></a>
<!-- Página 141 -->

8.3 Matrix Notation 123

8.3.3 Column Vector

A column vector is a matrix with a single column:
```
⎡ ⎤
a11 ⎡ ⎤
⎢ a21 ⎥ 2
⎢ ⎥
⎢ .. ⎥ , e.g. ⎣ 3 ⎦ .
⎣ . ⎦ 23
am1


```

8.3.4 Row Vector

A row vector is a matrix with a single row:

```
a11 a12 · · · a1n , e.g. 235 .


```

8.3.5 Null Matrix

A null matrix has all its elements equal to zero:
```
⎡ ⎤
0 0 ··· 0 ⎡ ⎤
⎢0 0 ··· 0⎥ 000
⎢ ⎥
θn = [ai j ]n n = ⎢ . . . . ⎥ , e.g. θ3 = ⎣ 0 0 0 ⎦ .
⎣ .. .. . . .. ⎦ 000
0 0 ··· 0

```

The null matrix behaves like zero when used with numbers, where we have, 0 + n =
n + 0 = n and 0 × n = n × 0 = 0, and similarly, θ + A = A + θ = A and θ A =
Aθ = θ . For example,
```
⎡ ⎤⎡ ⎤ ⎡ ⎤⎡ ⎤ ⎡ ⎤
000 123 123 000 000
⎣0 0 0⎦⎣4 5 6⎦ = ⎣4 5 6⎦⎣0 0 0⎦ = ⎣0 0 0⎦.
000 789 789 000 000


```

8.3.6 Unit Matrix

A unit matrix In , is a square matrix with the elements on its diagonal a11 to ann equal
to 1: ⎡ ⎤
```
1 0 ··· 0 ⎡ ⎤
⎢0 1 ··· 0⎥ 100
⎢ ⎥
In = [ai j ]n n = ⎢ . . . . ⎥ , e.g. I3 = ⎣ 0 1 0 ⎦ .
⎣ .. .. . . .. ⎦ 001
0 0 ··· 1
```


<a id='p142'></a>
<!-- Página 142 -->

124 8 Matrix Algebra

The unit matrix behaves like the number 1 in a conventional product, where we have,
1 × n = n × 1 = n, and similarly, IA = AI = A. For example,
```
⎡ ⎤⎡ ⎤ ⎡ ⎤⎡ ⎤ ⎡ ⎤
100 123 123 100 123
⎣0 1 0⎦⎣4 5 6⎦ = ⎣4 5 6⎦⎣0 1 0⎦ = ⎣4 5 6⎦.
001 789 789 001 789



```

8.3.7 Trace

The trace of a square matrix is the sum of the elements on its diagonal a11 to ann :
```
n
Tr(A) = aii .
i=1

```

For example, given
```
⎡ ⎤
123
A = ⎣ 4 5 6 ⎦ , then Tr(A) = 1 + 5 + 9 = 15.
789

```

The trace of a rotation matrix can be used to compute the angle of rotation. For
example, the matrix to rotate a point about the origin is
```
 
cos θ − sin θ
```


## A=

```
sin θ cos θ

```

where
```
Tr(A) = 2 cos θ

```

which means that  
```
Tr(A)
θ = arccos .
2

```

The three matrices for rotating points about the x-, y- and z-axis are respectively:
```
⎡ ⎤
1 0 0
Rα,x = ⎣ 0 cos α − sin α ⎦
0 sin α cos α
⎡ ⎤
cos α 0 sin α
Rα,y = ⎣ 0 1 0 ⎦
− sin α 0 cos α
```


<a id='p143'></a>
<!-- Página 143 -->

8.3 Matrix Notation 125
```
⎡ ⎤
cos α − sin α 0
Rα,z = ⎣ sin α cos α 0 ⎦
0 0 1

```

and it is clear that

```
Tr(Rα,x ) = Tr(Rα,y ) = Tr(Rα,z ) = 1 + 2 cos α

```

therefore,  
```
Tr(Rα,x ) − 1
α = arccos .
2



```

8.3.8 Determinant of a Matrix

The determinant of a matrix is a scalar value computed from the elements of the
matrix. The different methods for computing the determinant are described in Chap. 6.
For example, using Sarrus’s rule:
```
⎡ ⎤
123
A = ⎣ 4 5 6 ⎦ then, det A = 45 + 84 + 96 − 105 − 48 − 72 = 0.
789



```

8.3.9 Transpose

The transpose of a matrix exchanges all row elements for column elements. The
transposition is indicated by the letter ‘T’ outside the right-hand bracket.

## ⎡ ⎤T ⎡ ⎤

```
a11 a12 a13 a11 a21 a31
⎣ a21 a22 a23 ⎦ = ⎣ a12 a22 a32 ⎦ .
a31 a32 a33 a13 a23 a33

```

For example,

## ⎡ ⎤T ⎡ ⎤

```
124 164
⎣6 5 7⎦ = ⎣2 5 3⎦,
431 471

```

and ⎡ ⎤T
```
2
⎣3⎦ = 2 3 5 .
5
```


<a id='p144'></a>
<!-- Página 144 -->

126 8 Matrix Algebra

To prove that (AB)T = BT AT , we could develop a general proof using n × n matrices,
but for simplicity, let’s employ 3 × 3 matrices and assume the result generalises to
higher dimensions. Given
```
⎡ ⎤ ⎡ ⎤
a11 a12 a13 a11 a21 a31
A = ⎣ a21 a22 a23 ⎦ , AT = ⎣ a12 a22 a32 ⎦
a31 a32 a33 a13 a23 a33

```

and ⎡ ⎤ ⎡ ⎤
```
b11 b12 b13 b11 b21 b31
B = ⎣ b21 b22 b23 ⎦ , BT = ⎣ b12 b22 b32 ⎦
b31 b32 b33 b13 b23 b33

```

then,
```
⎡ ⎤
a11 b11 + a12 b21 + a13 b31 a11 b12 + a12 b22 + a13 b32 a11 b13 + a12 b23 + a13 b33
AB = ⎣ a21 b11 + a22 b21 + a23 b31 a21 b12 + a22 b22 + a23 b32 a21 b13 + a22 b23 + a23 b33 ⎦
a31 b11 + a32 b21 + a33 b31 a31 b12 + a32 b22 + a33 b32 a31 b13 + a32 b23 + a33 b33
⎡ ⎤
a11 b11 + a12 b21 + a13 b31 a21 b11 + a22 b21 + a23 b31 a31 b11 + a32 b21 + a33 b31
```

(AB) = a11 b12 + a12 b22 + a13 b32 a21 b12 + a22 b22 + a23 b32 a31 b12 + a32 b22 + a33 b32 ⎦

## T ⎣

```
a11 b13 + a12 b23 + a13 b33 a21 b13 + a22 b23 + a23 b33 a31 b13 + a32 b23 + a33 b33

```

and
```
⎡ ⎤
b11 a11 + b21 a12 + b31 a13 b11 a21 + b21 a22 + b31 a23 b11 a31 + b21 a32 + b31 a33
```

BT A T = ⎣ b 12 a11 + b22 a12 + b32 a13 b12 a21 + b22 a22 + b32 a23 b12 a31 + b22 a32 + b32 a33 ⎦
```
b13 a11 + b23 a12 + b33 a13 b13 a21 + b23 a22 + b33 a23 b13 a31 + b23 a32 + b33 a33

```

which confirms that (AB)T = BT AT .


8.3.10 Symmetric Matrix

A symmetric matrix is a square matrix that equals its transpose: i.e., A = AT . For
example, A is a symmetric matrix:

## ⎡ ⎤ ⎡ ⎤T

```
124 124
```


## A = ⎣2 5 3⎦ = ⎣2 5 3⎦ .

```
436 436

```

In general, a square matrix A = S + Q, where S is a symmetric matrix, and Q is an
antisymmetric matrix. The symmetric matrix is computed as follows. Given a matrix
A and its transpose AT
```
⎡ ⎤ ⎡ ⎤
a11 a12 . . . a1n a11 a21 . . . an1
⎢ a21 a22 . . . a2n ⎥ ⎢ a12 a22 . . . an2 ⎥
⎢ ⎥ ⎢ ⎥
```


## A=⎢ . . . . ⎥ , AT = ⎢ . . . . ⎥

```
⎣ .. .. . . .. ⎦ ⎣ .. .. . . .. ⎦
an1 an2 . . . ann a1n a2n . . . ann
```


<a id='p145'></a>
<!-- Página 145 -->

8.3 Matrix Notation 127

their sum is
```
⎡ ⎤
2a11 a12 + a21 . . . a1n + an1
⎢ a12 + a21 2a22 . . . a2n + an2 ⎥
⎢ ⎥
```


## A + AT = ⎢ .. .. . . .. ⎥.

```
⎣ . . . . ⎦
a1n + an1 a2n + an2 . . . 2ann

```

By inspection, A + AT is symmetric, and if we divide throughout by 2 we have
```
 
```


## S = 21 A + AT


which is defined as the symmetric part of A. For example, given
```
⎡ ⎤ ⎡ ⎤
a11 a12 a13 a11 a21 a31
A = ⎣ a21 a22 a23 ⎦ , AT = ⎣ a12 a22 a32 ⎦
a31 a32 a33 a13 a23 a33

```

then
```
 
```


## S = 21 A + AT

```
⎡ ⎤
a11 (a12 + a21 )/2 (a13 + a31 )/2
= ⎣ (a12 + a21 )/2 a22 (a23 + a32 )/2 ⎦
(a13 + a31 )/2 (a23 + a32 )/2 a33
⎡ ⎤
a11 s3 /2 s2 /2
= ⎣ s3 /2 a22 s1 /2 ⎦
s2 /2 s1 /2 a33

```

where

```
s1 = a23 + a32
s2 = a13 + a31
s3 = a12 + a21 .

```

Using a real example:
```
⎡ ⎤ ⎡ ⎤
014 034
```


## A = ⎣ 3 1 4 ⎦ , AT = ⎣ 1 1 2 ⎦

```
426 446
⎡ ⎤
024
```


## S = ⎣2 1 3⎦

```
436

```

which equals its own transpose.

<a id='p146'></a>
<!-- Página 146 -->

128 8 Matrix Algebra

8.3.11 Antisymmetric Matrix

An antisymmetric matrix is a matrix whose transpose is its own negative:


## AT = −A


and is also known as a skew-symmetric matrix.
As the elements of A and AT are related by

```
ar ow,col = −acol,r ow .

```

When k = r ow = col:
```
ak,k = −ak,k

```

which implies that the diagonal elements must be zero. For example, this is an
antisymmetric matrix

## ⎡ ⎤ ⎡ ⎤T

```
0 −2 4 0 −2 4
```


## A = ⎣ 2 0 −3 ⎦ = − ⎣ 2 0 −3 ⎦ .

```
−4 3 0 −4 3 0

```

The antisymmetric part is computed as follows. Given a matrix A and its transpose

## AT ⎡ ⎤ ⎡ ⎤

```
a11 a12 . . . a1n a11 a21 . . . an1
⎢ a21 a22 . . . a2n ⎥ ⎢ a12 a22 . . . an2 ⎥
⎢ ⎥ ⎢ ⎥
```


## A=⎢ . . . . ⎥ , AT = ⎢ . . . .. ⎥

```
.
⎣ . . . . .
. . ⎦ .
⎣ . . . . . . ⎦
an1 an2 . . . ann a1n a2n . . . ann

```

their difference is
```
⎡ ⎤
 0  a12 − a21 . . . a1n − an1
⎢ − a12 − a21 0 . . . a2n − an2 ⎥
⎢ ⎥
```


## A − AT = ⎢ .. .. .. .. ⎥.

```
⎣ . ⎦
 .   .  .
− a1n − an1 − a2n − an2 . . . 0

```

It is clear that A − AT is antisymmetric, and if we divide throughout by 2 we have
```
 
```


## Q = 21 A − AT .


For example:
```
⎡ ⎤ ⎡ ⎤
a11 a12 a13 a11 a21 a31
A = ⎣ a21 a22 a23 ⎦ , AT = ⎣ a12 a22 a32 ⎦
a31 a32 a33 a13 a23 a33
```


<a id='p147'></a>
<!-- Página 147 -->

8.3 Matrix Notation 129
```
⎡     ⎤
 0  a12 − a21 /2 a13 − a31 /2
Q = ⎣ a21 − a12 /2  0  a23 − a32 /2 ⎦
a31 − a13 /2 a32 − a23 /2 0

```

and if we maintain some symmetry with the subscripts, we have
```
⎡     ⎤
 0  a12 − a21 /2 − a31 − a13 /2
Q = ⎣ − a12 − a21 /2  0  a23 − a32 /2 ⎦
a31 − a13 /2 − a23 − a32 /2 0
⎡ ⎤
0 q3 /2 −q2 /2
= ⎣ −q3 /2 0 q1 /2 ⎦
q2 /2 −q1 /2 0

```

where

```
q1 = a23 − a32
q2 = a31 − a13
q3 = a12 − a21 .

```

Using a real example:
```
⎡ ⎤ ⎡ ⎤
014 034
```


## A = ⎣ 3 1 4 ⎦ , AT = ⎣ 1 1 2 ⎦

```
426 446
⎡ ⎤
0 −1 0
```


## Q = ⎣1 0 1⎦.

```
0 −1 0

```

Furthermore, we have already computed
```
⎡ ⎤
024
```


## S = ⎣2 1 3⎦

```
436

```

and ⎡ ⎤
```
014
```


## S + Q = ⎣ 3 1 4 ⎦ = A.

```
426
```


<a id='p148'></a>
<!-- Página 148 -->

130 8 Matrix Algebra

8.4 Matrix Addition and Subtraction

As equations can be added and subtracted together, it follows that matrices can also
be added and subtracted, as long as they have the same dimension. For example,
given ⎡ ⎤ ⎡ ⎤
```
11 22 2 1
A = ⎣ 14 −15 ⎦ and B = ⎣ −4 5 ⎦
27 28 1 8

```

then ⎡ ⎤ ⎡ ⎤
```
13 23 9 21
```


## A + B = ⎣ 10 −10 ⎦ , A − B = ⎣ 18 −20 ⎦ .

```
28 36 26 20



```

8.4.1 Scalar Multiplication

As equations can be scaled and factorised, it follows that matrixes can also be scaled
and factorised.
```
⎡ ⎤ ⎡ ⎤
a11 a12 . . . a1n λa11 λa12 . . . λa13
⎢ a21 a22 . . . a2n ⎥ ⎢ λa21 λa22 . . . λa23 ⎥
⎢ ⎥ ⎢ ⎥
λA = λ ⎢ . . . . ⎥=⎢ . .. . . .. ⎥ .
⎣ .. .. . . .. ⎦ ⎣ .. . . . ⎦
am1 am2 . . . amn λam1 λam2 . . . λamn

```

For example,    
```
123 2 4 6
2 = .
456 8 10 12



```

8.5 Matrix Products

We have already seen that matrices can be multiplied together employing rules that
maintain the algebraic integrity of the equations they represent. And as matrices
may be vectors, rectangular or square, we need to examine the products that are
permitted. To keep the notation simple, the definitions and examples are restricted
to a dimension of 3 or 3 × 3.
We begin with row and column vectors.

<a id='p149'></a>
<!-- Página 149 -->

8.5 Matrix Products 131

8.5.1 Row and Column Vectors

Given ⎡ ⎤
```
α
A= a b c and B = ⎣ β ⎦
γ

```

then ⎡ ⎤
```
α
AB = a b c ⎣ β ⎦ = aα + bβ + cγ
γ

```

which is a scalar and equivalent to the dot or scalar product of two vectors.
For example, given
```
⎡
⎤
10
A= 234 and B = ⎣ 30 ⎦
20

```

then ⎡ ⎤
```
10
```


## AB = 2 3 4 ⎣ 30 ⎦ = 20 + 90 + 80 = 190.

```
20

```

Whereas,
```
⎡⎤ ⎡ ⎤
b11 b11 a11 b11 a12 b11 a13
BA = ⎣ b21 ⎦ a11 a12 a13 = ⎣ b21 a11 b21 a12 b21 a13 ⎦ .
b31 b31 a11 b31 a12 b31 a13

```

For example, ⎡ ⎤ ⎡ ⎤
```
10 20 30 40
```


## BA = ⎣ 30 ⎦ 2 3 4 = ⎣ 60 90 120 ⎦ .

```
20 40 60 80

```

The products AA and BB are not permitted.



8.5.2 Row Vector and a Matrix

Given ⎡ ⎤
```
b11 b12 b13
A = a11 a12 a13 and B = ⎣ b21 b22 b23 ⎦
bm1 bm2 b33
```


<a id='p150'></a>
<!-- Página 150 -->

132 8 Matrix Algebra

then
```
⎡ ⎤
 b11 b12 b13
⎢ ⎥
```

AB = a11 a12 a13 ⎣ b21 b22 b23 ⎦
```
bm1 bm2 b33
 
= (a11 b11 + a12 b21 + a13 b31 ) (a11 b12 + a12 b22 + a13 b32 ) (a11 b13 + a12 b23 + a13 b33 ) .


```

The product BA is not permitted.
For example, given
```
⎡ ⎤
123
A= 2 3 4 and B = ⎣ 3 4 5 ⎦
456

```

then
```
⎤ ⎡
123
```


## AB = 2 3 4 ⎣ 3 4 5 ⎦

```
456
= (2 + 9 + 16) (4 + 12 + 20) (6 + 15 + 24)
= 27 36 45 .



```

8.5.3 Matrix and a Column Vector

Given ⎡ ⎤ ⎡ ⎤
```
a11 a12 a13 b11
A = ⎣ a21 a22 a23 ⎦ and B = ⎣ b21 ⎦
a31 a32 a33 b31

```

then ⎡ ⎤⎡ ⎤ ⎡ ⎤
```
a11 a12 a13 b11 a11 b11 + a12 b21 + a13 b31
AB = ⎣ a21 a22 a23 ⎦ ⎣ b21 ⎦ = ⎣ a21 b11 + a22 b21 + a23 b31 ⎦ .
a31 a32 a33 b31 a31 b11 + a32 b21 + a33 b31

```

The product BA is not permitted.
For example, given
```
⎡ ⎤ ⎡ ⎤
123 2
A = ⎣ 3 4 5 ⎦ , and B = ⎣ 3 ⎦
456 4
```


<a id='p151'></a>
<!-- Página 151 -->

8.5 Matrix Products 133

then ⎡ ⎤⎡ ⎤ ⎡ ⎤ ⎡ ⎤
```
123 2 2 + 6 + 12 20
```


## AB = ⎣ 3 4 5 ⎦ ⎣ 3 ⎦ = ⎣ 6 + 12 + 20 ⎦ = ⎣ 38 ⎦ .

```
456 4 8 + 15 + 24 47



```

8.5.4 Square Matrices

To clarify the products, lower-case Greek symbols are used with lower-case letters.
Here are their names:

```
α = alpha, β = beta, γ = gamma,
λ = lambda, μ = mu, ν = nu,
ρ = rho, σ = sigma, τ = tau.

```

Given ⎡ ⎤ ⎡ ⎤
```
a b c αβγ
A = ⎣ p q r ⎦ and B = ⎣ λ μ ν ⎦
u vw ρσ τ

```

then
```
⎡ ⎤⎡ ⎤ ⎡ ⎤
a b c αβ γ aα + bλ + cρ aβ + bμ + cσ aγ + bν + cτ
```

AB = ⎣ p q r ⎦ ⎣ λ μ ν ⎦ = ⎣ pα + qλ + r ρ pβ + qμ + r σ pγ + qν + r τ ⎦
```
u vw ρσ τ uα + vλ + wρ uβ + vμ + wσ uγ + vν + wτ
```

and
```
⎡ ⎤⎡ ⎤ ⎡ ⎤
αβ γ a b c αa + β p + γ u αb + βq + γ v αc + βr + γ w
```

BA = ⎣ λ μ ν ⎦ ⎣ p q r ⎦ = ⎣ λa + μp + νu λb + μq + νv λc + μr + νw ⎦ .
```
ρσ τ u vw ρa + σ p + τ u ρb + σ q + τ v ρc + σ r + τ w
```

For example, given
```
⎡ ⎤ ⎡ ⎤
123 234
A = ⎣ 3 4 5 ⎦ and B = ⎣ 4 5 6 ⎦
567 678

```

then ⎡ ⎤⎡ ⎤ ⎡ ⎤
```
123 234 28 34 40
```


## AB = ⎣ 3 4 5 ⎦ ⎣ 4 5 6 ⎦ = ⎣ 52 64 76 ⎦

```
567 678 76 92 112
```


<a id='p152'></a>
<!-- Página 152 -->

134 8 Matrix Algebra

and ⎡ ⎤⎡ ⎤ ⎡ ⎤
```
234 123 31 40 49
```


## BA = ⎣ 4 5 6 ⎦ ⎣ 3 4 5 ⎦ = ⎣ 49 64 89 ⎦ .

```
678 567 67 88 109



```

8.5.5 Rectangular Matrices

Given two rectangular matrices A and B, where A has a dimension m × n, the product
AB is permitted, if and only if, B has a dimension n × p. The resulting matrix has a
dimension m × p. For example, given
```
⎡ ⎤
a11 a12  
b b b b
A = ⎣ a21 a22 ⎦ and B = 11 12 13 14
b21 b22 b23 b24
a31 a32

```

then
```
⎡ ⎤
a11 a12  
b b b b
```

AB = ⎣ a21 a22 ⎦ 11 12 13 14
```
b21 b22 b23 b24
a31 a32
⎡ ⎤
(a11 b11 + a12 b21 ) (a11 b12 + a12 b22 ) (a11 b13 + a12 b23 ) (a11 b14 + a12 b24 )
```

= ⎣ (a21 b11 + a22 b21 ) (a21 b12 + a22 b22 ) (a21 b13 + a22 b23 ) (a21 b14 + a22 b24 ) ⎦ .
```
(a31 b11 + a32 b21 ) (a31 b12 + a32 b22 ) (a31 b13 + a32 b23 ) (a31 b14 + a32 b24 )



```

8.6 Inverse Matrix

A square matrix Ann that is invertible satisfies the condition:

```
Ann A−1 −1
nn = Ann Ann = In ,


```

where A−1
```
nn is unique, and is the inverse matrix of Ann . For example, given
 
43
```


## A=

```
54

```

then  
```
4 −3
```


## A−1 =

```
−5 4

```

because     
```
−1 43 4 −3 10
```


## AA = = .

```
54 −5 4 01
```


<a id='p153'></a>
<!-- Página 153 -->

8.6 Inverse Matrix 135

A square matrix whose determinant is 0, cannot have an inverse, and is known as a
singular matrix.
We now require a way to compute A−1 , which is rather easy.
Consider two linear equations:
```
    
x ab x
= . (8.10)
y cd y

```

Let the inverse of  
```
ab
cd

```

be  
```
e f
g h

```

therefore,     
```
e f ab 10
= . (8.11)
g h cd 01

```

From (8.11) we have

```
ae + c f = 1 (8.12)
be + d f = 0 (8.13)
ag + ch = 0 (8.14)
bg + dh = 1. (8.15)

```

Multiply (8.12) by d and (8.13) by c, and subtract:

```
ade + cd f = d
bce + cd f = 0
ade − bce = d

```

therefore,
```
d
e= .
ad − bc

```

Multiply (8.12) by b and (8.13) by a, and subtract:

```
abe + bc f = b
abe + ad f = 0
ad f − bc f = −b
```


<a id='p154'></a>
<!-- Página 154 -->

136 8 Matrix Algebra

therefore,
```
−b
f = .
ad − bc

```

Multiply (8.14) by d and (8.15) by c, and subtract:

```
adg + cdh = 0
bcg + cdh = c
adg − bcg = −c

```

therefore,
```
−c
g= .
ad − bc

```

Multiply (8.14) by b and (8.15) by a, and subtract:

```
abg + bch = 0
abg + adh = a
adh − bch = a

```

therefore,
```
a
h= .
ad − bc

```

We now have values for e, f , g and h, which are the elements of the inverse matrix.
Consequently, given
```
   
ab e f
A= and A−1 = ,
cd g h

```

then  
```
−1 1 d −b
```


## A = .

```
det A −c a

```

The inverse matrix permits us to solve a pair of linear equations as follows. Starting
with       
```
x ab x x
```


## = =A

```
y cd y y

```

multiply both sides by the inverse matrix:
```
 
 
x x
```


## A−1 = A−1 A

```
y y
      
x 10 x x
```


## A−1  = =

```
y 01 y y
```


<a id='p155'></a>
<!-- Página 155 -->

8.6 Inverse Matrix 137
```
   
x x
```


## = A−1 

```
y y
    
x 1 d −b x
= .
y det A −c a y

```

Although the elements of A−1 come from A, the relationship is not obvious. However,
if A is transposed, a pattern is revealed. Given
```
   
ab a c
A= then AT =
cd bd

```

and placing A−1 alongside AT , we have
```
   
e f a c
A−1 = and AT = .
g h bd

```

The elements of A−1 share a common denominator (det A), which is placed outside
the matrix, therefore, the matrix elements are taken from AT as follows. For any entry
ai j in A−1 , mask out the ith row and jth column in AT , and the remaining entry is
copied to the i jth entry in A−1 . In the case of e, it is d. For f , it is b, with a sign
reversal. For g, it is c, with a sign reversal, and for h, it is a. The sign change is
computed by the same formula used with determinants:

```
(−1)i+ j .

```

which generates this pattern:  
```
+−
.
−+

```

You may be wondering what happens when a 3 × 3 matrix is inverted. Well, the
same technique is used, but when the ith row and jth column in AT is masked out,
it leaves behind a 2 × 2 determinant, whose value is copied to the i jth entry in A−1 ,
with the appropriate sign change. We investigate this later on.
```
Let’s illustrate this with an example. Given

42 = 6x + 2y
28 = 2x + 3y

let  
62
```


## A=

```
23

```

then det A = 14, therefore,

<a id='p156'></a>
<!-- Página 156 -->

138 8 Matrix Algebra
```
    
x 3 −2 42
= 14
1
y −2 6 28
 
70
= 14
1
84
 
5
= .
6

```

which is the solution.
Now let’s investigate how to invert a 3 × 3 matrix. Given three simultaneous
equations in three unknowns:

```
x  = ax + by + cz
y  = d x + ey + f z
z  = gx + hy + j z

```

they can be written using matrices as follows:
```
⎡ ⎤ ⎡ ⎤⎡ ⎤ ⎡ ⎤
x ab c x x
⎣ y ⎦ = ⎣ d e f ⎦ ⎣ y ⎦ = A ⎣ y ⎦ .
z gh j z z

```

Let ⎡ ⎤
```
l mn
A−1 = ⎣ p q r ⎦
s t u

```

therefore, ⎡ ⎤⎡ ⎤ ⎡ ⎤
```
l mn ab c 100
⎣ p q r ⎦⎣d e f ⎦ = ⎣0 1 0⎦. (8.16)
s t u gh j 001

```

From (8.16) we can write:

```
la + md + ng = 1 (8.17)
lb + me + nh = 0 (8.18)
lc + m f + n j = 0. (8.19)

```

Multiply (8.17) by e and (8.18) by d, and subtract:

```
ael + dem + egn = e
bdl + dem + dhn = 0
ael − bdl + egn − dhn = e
l(ae − bd) + n(eg − dh) = e. (8.20)
```


<a id='p157'></a>
<!-- Página 157 -->

8.6 Inverse Matrix 139

Multiply (8.18) by f and (8.19) by e, and subtract:

```
b f l + e f m + f hn = 0
cel + e f m + ejn = 0
b f l − cel + f hn − ejn = 0
l(b f − ce) + n( f h − ej) = 0. (8.21)

```

Multiply (8.20) by ( f h − ej) and (8.21) by (eg − dh), and subtract:

```
l(ae − bd)( f h − ej) + n(eg − dh)( f h − ej) = e( f h − ej)
l(b f − ce)(eg − dh) + n(eg − dh)( f h − ej) = 0
l(ae − bd)( f h − ej) − l(b f − ce)(eg − dh) = e f h − e2 j
```

l(ae f h − ae2 j − bd f h + bdej − be f g + bd f h + ce2 g − cdeh) = e f h − e2 j
```
l(ae f h − ae2 j + bdej − be f g + ce2 g − cdeh) = e f h − e2 j
l(a f h + bd j + ceg − aej − cdh − b f g) = f h − ej
l(aej + b f g + cdh − a f h − bd j − ceg) = ej − f h

```

but (aej + b f g + cdh − a f h − bd j − ceg) is the Sarrus expansion for det A, therefore
```
ej − f h
l= .
det A
```

An exhaustive algebraic analysis reveals:

```
ej − f h bj − ch b f − ce
l= , m=− , n=
det A det A det A
dj − gf a j − gc a f − dc
p=− , q= , r =−
det A det A det A
dh − ge ah − gb ae − bd
s= , t =− , u=
det A det A det A
```

where ⎡ ⎤ ⎡ ⎤
```
l mn ab c
A−1 = ⎣ p q r ⎦ A = ⎣ d e f ⎦ .
s t u gh j

```

However, there does not appear to be an obvious way of deriving A−1 from A. But,
as we discovered with the 2 × 2 matrix, the transpose AT resolves the problem:
```
⎡ ⎤ ⎡ ⎤
l mn a d g
A−1 = ⎣ p q r ⎦ , AT = ⎣ b e h ⎦ .
s t u c f j
```


<a id='p158'></a>
<!-- Página 158 -->

140 8 Matrix Algebra

The elements for A−1 share a common denominator (det A), which is placed outside
the matrix, therefore, the matrix elements are taken from AT as follows. For any entry
ai j in A−1 , mask out the ith row and jth column in AT , and the remaining elements,
in the form of a 2 × 2 determinant, is copied to the i jth entry in A−1 . In the case of l,
it is (ej − h f ). For m, it is (bj − hc), with a sign reversal, and for n, it is (b f − ec).
The sign change is computed by the same formula used with determinants:

```
(−1)i+ j ,

```

which generates the pattern: ⎡ ⎤
```
+−+
⎣− + −⎦.
+−+

```

With the above aide-mémoire, it is easy to write down the inverse matrix:
```
⎡ ⎤
ej − f h −(bj − ch) b f − ce
1 ⎣ −(d j − g f ) a j − gc −(a f − dc) ⎦ .
```


## A−1 =

```
det A dh − ge −(ah − gb) ae − bd

```

This technique is known as the Laplacian expansion or the cofactor expansion, after
Pierre-Simon Laplace. The matrix of minor determinants is called the cofactor matrix
of A, which permits the inverse matrix to be written as:

```
(cofactor matrix of A)T
```


## A−1 = .

```
det A
```

Let’s illustrate this solution with an example. Given

```
18 = 2x + 2y + 2z
20 = x + 2y + 3z
7= y+z

```

therefore, ⎡ ⎤ ⎡ ⎤⎡ ⎤ ⎡ ⎤
```
18 222 x x
⎣ 20 ⎦ = ⎣ 1 2 3 ⎦ ⎣ y ⎦ = A ⎣ y ⎦ .
7 011 z z

```

and

```
det A = 4 + 2 − 2 − 6 = −2
⎡ ⎤
210
```


## AT = ⎣ 2 2 1 ⎦

```
231
```


<a id='p159'></a>
<!-- Página 159 -->

8.6 Inverse Matrix 141

therefore, ⎡ ⎤
```
−1 0 2
```


## A−1 = − 21 ⎣ −1 2 −4 ⎦

```
1 −2 2

```

and ⎡ ⎤ ⎡ ⎤⎡ ⎤ ⎡ ⎤
```
x −1 0 2 18 2
⎣ y ⎦ = − 1 ⎣ −1 2 −4 ⎦ ⎣ 20 ⎦ = ⎣ 3 ⎦
2
z 1 −2 2 7 4

```

which is the solution.


8.6.1 Inverting a Pair of Matrices

Having seen how to invert a single matrix, let’s investigate how to invert of a pair of
matrices.
Given two matrices T and R, the product TR and its inverse (TR)−1 must equal
the identity matrix I:

## (TR)(TR)−1 = I


and multiplying throughout by T−1 we have


## T−1 TR(TR)−1 = T−1

```
c(TR)−1 = T−1 .

```

Multiplying throughout by R−1 we have

```
R−1 c(TR)−1 = R−1 T−1
```


## (TR)−1 = R−1 T−1 .


Therefore, if T and R are invertible, then


## (TR)−1 = R−1 T−1 .


Generalising this result to a triple product such as STR we can reason that


## (STR)−1 = R−1 T−1 S−1 .




8.7 Orthogonal Matrix

A matrix is orthogonal if its transpose is also its inverse, i.e., matrix A is orthogonal if


## AT = A−1 .


For example,

<a id='p160'></a>
<!-- Página 160 -->

142 8 Matrix Algebra
```
 1 
√ − √12
```


## A= 2

```
√1 √1
2 2


```

and  
```
√1 √1
```


## AT = 2 2

```
− √12 √12

```

and  1    
```
√ − √1 √1 √1 10
```


## AA =T 2 2 2 2 =

```
√1
2
√1
2
− √12 √12 01

```

which implies that AT = A−1 .
The following matrix is also orthogonal
```
 
cos β − sin β
```


## A=

```
sin β cos β

```

because  
```
cos β sin β
```


## AT =

```
− sin β cos β

```

and     
```
cos β − sin β cos β sin β 10
```


## AAT = = .

```
sin β cos β − sin β cos β 01

```

Orthogonal matrices play an important role in rotations because they leave the origin
fixed and preserve all angles and distances. Consequently, an object’s geometric
integrity is maintained after a rotation, which is why an orthogonal transform is
known as a rigid motion transform.



8.8 Diagonal Matrix

A diagonal matrix is a square matrix whose elements are zero, apart from its diagonal:
```
⎡ ⎤
a11 0 . . . 0
⎢ 0 a22 . . .
⎢ 0 ⎥⎥
```


## A=⎢ . . . .. ⎥ .

```
⎣ .. .. . . . ⎦
0 0 . . . ann

```

The determinant of a diagonal matrix must be

```
det A = a11 × a22 × · · · × ann .
```


<a id='p161'></a>
<!-- Página 161 -->

8.8 Diagonal Matrix 143

Here is a diagonal matrix with its determinant
```
⎡ ⎤
200
```


## A = ⎣0 3 0⎦

```
004
det A = 2 × 3 × 4 = 24.

```

The identity matrix I is a diagonal matrix with a determinant of 1.


8.9 Summary

This chapter has covered matrix algebra to some depth and should permit the reader
to use matrices with confidence. The following chapter illustrates how matrices are
used to perform a wide variety of geometric transformations.


8.10 Worked Examples

8.10.1 Matrix Inversion

Invert A and show that AA−1 = I2 .
```

35
```


## A= .

```
24

```

Using  
```
1 d −b
```


## A−1 =

```
det A −c a

```

then det A = 2, and  
```
−1 4 −5
```


## A = 21 .

```
−2 3

```

Calculating AA−1 :
```
      
−1 35 4 −5 1 2 0 10
```


## AA = 21 =2 = .

```
24 −2 3 02 01
```


<a id='p162'></a>
<!-- Página 162 -->

144 8 Matrix Algebra

8.10.2 Identity Matrix

Invert A and show that AA−1 = I3 .
```
⎡ ⎤
234
```


## A = ⎣1 2 1⎦.

```
567

```

Using Sarrus’s rule for det A:

```
det A = 28 + 15 + 24 − 40 − 12 − 21 = −6.

```

Therefore,
```
⎡ ⎤
215
```


## AT = ⎣ 3 2 6 ⎦

```
417
⎡ ⎤
14 − 6) −(21 − 24) 3 − 8
```


## A−1 = − 16 ⎣ −(7 − 5) 14 − 20 −(2 − 4) ⎦

```
6 − 10) −(12 − 15) 4 − 3
⎡ ⎤
8 3 −5
= − 16 ⎣ −2 −6 2 ⎦
−4 3 1

```

and
```
⎡ ⎤⎡ ⎤
234 8 3 −5
```


## AA−1 = − 16 ⎣ 1 2 1 .⎦ ⎣ −2 −6 2 ⎦

```
567 −4 3 1
⎡ ⎤ ⎡ ⎤
−6 0 0 100
= − 16 ⎣ 0 −6 0 ⎦ = ⎣ 0 1 0 ⎦ .
0 0 −6 001



```

8.10.3 Solving Two Equations Using Matrices

Solve the following equations using matrices.

```
20 = 2x + 3y
36 = 7x + 2y.
```


<a id='p163'></a>
<!-- Página 163 -->

8.10 Worked Examples 145

Let  
```
23
```


## A=

```
72

```

therefore, det A = −17, and
```
 
−1 2 −3
```


## A = − 17

```
1
−7 2

```

therefore,
```
    
x 2 −3 20
= − 17
1
y −7 2 36
 
40 − 108
= − 17
1
−140 + 72
 
−68
= − 17
1
−68
 
4
=
4

```

therefore, x = y = 4.


8.10.4 Solving Three Equations Using Matrices

Solve the following equations using matrices.

```
10 = 2x + y − z
13 = −x − y + z
28 = −x + 2y + z.

```

Let ⎡ ⎤
```
2 1 −1
```


## A = ⎣ −1 −1 1 ⎦ .

```
−1 2 1

```

Using Sarrus’s rule for det A:

```
det A = −2 − 1 + 2 + 1 − 4 + 1 = −3.

```

Therefore,
```
⎡ ⎤
2 −1 −1
```


## AT = ⎣ 1 −1 2 ⎦

```
−1 1 1
```


<a id='p164'></a>
<!-- Página 164 -->

146 8 Matrix Algebra
```
⎡ ⎤
(−1 − 2) −(1 + 2) (1 − 1)
```


## A−1 = − 13 ⎣ −(−1 + 1) (2 − 1) −(2 − 1) ⎦

```
(−2 − 1) −(4 + 1) (−2 + 1)
⎡ ⎤
−3 −3 0
= − 13 ⎣ 0 1 −1 ⎦
−3 −5 −1

```

therefore,
```
⎡ ⎤ ⎡ ⎤⎡ ⎤
x −3 −3 0 10
⎣ y ⎦ = − 1 ⎣ 0 1 −1 ⎦ ⎣ 13 ⎦
3
z −3 −5 −1 28
⎡ ⎤
−30 − 39
1⎣ ⎦
=− 13 − 28
3 −30 − 65 − 28
⎡ ⎤
−69
1⎣
=− −15 ⎦
3 −123
⎡ ⎤
23
=⎣ 5 ⎦
41

```

therefore, x = 23, y = 5, z = 41.



8.10.5 Solving Two Complex Equations

Solve the following complex equations using matrices.

```
7 + i8 = 2x + y
−4 − i = x − 2y.

```

Let  
```
2 1
```


## A=

```
1 −2

```

therefore, det A = −5, and
```


2 1
```


## A = T

```
1 −2
 
−1 1 −2 −1
```


## A = −5

```
−1 2
```


<a id='p165'></a>
<!-- Página 165 -->

8.10 Worked Examples 147

therefore,
```
    
x −2 −1 7 + i8
= − 15
y −1 2 −4 − i
 
−14 − i16 + 4 + i
= − 15
−7 − i8 − 8 − i2
 
−10 − i15
= − 15
−15 − i10
 
2 + i3
=
3 + i2

```

therefore, x = 2 + i3, y = 3 + i2.



8.10.6 Solving Three Complex Equations

Solve the following complex equations using matrices.

```
0=x+y−z
3 + i3 = 2x − y + z
−5 − i5 = −x + y − 2z.

```

Let ⎡ ⎤
```
1 1 −1
```


## A = ⎣ 2 −1 1 ⎦

```
−1 1 −2

```

therefore, det A = 2 − 1 − 2 + 1 − 1 + 4 = 3, and
```
⎡ ⎤
1 2 −1
```


## AT = ⎣ 1 −1 1 ⎦

```
−1 1 −2
⎡ ⎤
(2 − 1) −(−2 + 1) 0
```


## A−1 = 13 ⎣ −(−4 + 1) (−2 − 1) −(1 + 2) ⎦

```
(2 − 1) −(1 + 1) (−1 − 2)

```

therefore,
```
⎡ ⎤ ⎡ ⎤⎡ ⎤
x 1 1 0 0
⎣ y ⎦ = 1 ⎣ 3 −3 −3 ⎦ ⎣ 3 + i3 ⎦
3
z 1 −2 −3 −5 − i5
```


<a id='p166'></a>
<!-- Página 166 -->

148 8 Matrix Algebra
```
⎡ ⎤
3 + i3
= 13 ⎣ −9 − i9 + 15 + i15 ⎦
−6 − i6 + 15 + i15
⎡ ⎤
1+i
= ⎣ 2 + i2 ⎦
3 + i3

```

therefore, x = 1 + i, y = 2 + i2, z = 3 + i3.



8.10.7 Solving Two Complex Equations

Solve the following complex equations using matrices.

```
3 + i5 = i x + 2y
5 + i = 3x − i y.

```

Let  
```
i 2
```


## A=

```
3 −i

```

therefore, set A = 1 − 6 = −5, and
```
 
i 3
```


## A =


## T

```
2 −i
 
−1 1 −i −2
```


## A = −5

```
−3 i

```

therefore,
```
    
x 1 −i −2 3 + i5
= −5
y −3 i 5+i
 
1 −i3 + 5 − 10 − i2
= −5
−9 − i15 + i5 − 1
 
−5 − i5
= −51
−10 − i10
 
1+i
=
2 + i2

```

therefore, x = 1 + i, y = 2 + i2.

<a id='p167'></a>
<!-- Página 167 -->

8.10 Worked Examples 149

8.10.8 Solving Three Complex Equations

Solve the following complex equations using matrices.

```
6 + i2 = i x + 2y − i z
−2 + i6 = 2x − i y + i2z
2 + i10 = i2x + i y + 2z.

```

Let ⎡ ⎤
```
i 2 −i
A = ⎣ 2 −i i2 ⎦
i2 i 2

```

therefore, det A = 2 − 8 + 2 + i2 + i2 − 8 = −12 + i4, and
```
⎡ ⎤
i 2 i2
AT = ⎣ 2 −i i ⎦
−i i2 2
⎡ ⎤
−i2 + 2 −(4 − 1) i4 + 1
1 ⎣ −(4 + 4) i2 − 2 −(−2 + i2) ⎦
```


## A−1 =

```
−12 + i4 i2 − 2 −(−1 − i4) 1−4
⎡ ⎤
2 − i2 −3 1 + i4
1 ⎣ −8 −2 + i2 2 − i2 ⎦
=
−12 + i4 −2 + i2 1 + i4 −3

```

therefore,
⎡ ⎤ ⎡ ⎤⎡ ⎤
```
x 2 − i2 −3 1 + i4 6 + i2
```

⎣y⎦ = 1 ⎣ −8 −2 + i2 2 − i2 ⎦ ⎣ −2 + i6 ⎦
```
z −12 + i4 −2 + i2 1 + i4 −3 2 + i10
⎡ ⎤
(2 − i2)(6 + i2) − 3(−2 + i6) + (1 + i4)(2 + i10)
1 ⎣ −8(6 + i2) + (−2 + i2)(−2 + i6) + (2 − i2)(2 + i10) ⎦
=
−12 + i4 (−2 + i2)(6 + i2) + (1 + i4)(−2 + i6) − 3(2 + i10)
⎡ ⎤
12 + i4 − i12 + 4 + 6 − i18 + 2 + i10 + i8 − 40
1 ⎣ −48 − i16 + 4 − i12 − i4 − 12 + 4 + i20 − i4 + 20 ⎦
=
−12 + i4 −12 − i4 + i12 − 4 − 2 + i6 − i8 − 24 − 6 − i30
⎡ ⎤
−16 − i8
1 ⎣ −32 − i16 ⎦
=
−12 + i4 −48 − i24

```

multiply by the conjugate of −12 + i4:

<a id='p168'></a>
<!-- Página 168 -->

150 8 Matrix Algebra
```
⎡ ⎤ ⎡ ⎤
x −16 − i8
⎣y⎦ = −12 − i4 ⎣ −32 − i16 ⎦
z 160 −48 − i24

```

therefore,

```
x = 160
1
(−12 − i4)(−16 − i8)
= 160
1
(192 + i64 + i96 − 32)
= 160
1
(160 + i160) = 1 + i
y = 160
1
(−12 − i4)(−32 − i16)
= 160
1
(384 + i128 + i192 − 64)
= 160
1
(320 + i320) = 2 + i2
z = 160
1
(−12 − i4)(−48 − i24)
= 160
1
(576 + i192 + i288 − 96)
= 160
1
(480 + i480) = 3 + i3

```

therefore, x = 1 + i, y = 2 + i2, z = 3 + i3.

<a id='p169'></a>
<!-- Página 169 -->


## Chapter 9

Complex Numbers




9.1 Introduction

In this chapter we investigate complex numbers and show how they can be thought of
as an ordered pair. We also show how they are represented by a matrix. Many of the
qualities associated with quaternions are found in complex numbers, which is why
they are worthy of close examination. Readers interested in this subject may want to
examine the author’s book Imaginary Mathematics for Computer Science [1].



9.2 Definition of a Complex Number

By definition, a complex number is the combination of a real number and an imaginary
number, and is expressed as

```
z = a + bi, a, b ∈ , i 2 = −1.

```

The set of complex numbers is , which permits us to write z ∈ . For example,
3 + 4i is a complex number where 3 is the real part and 4i is the imaginary part. The
following are all complex numbers:

```
3, 3 + 4i, −4 − 6i, 7i, 5.5 + 6.7i.

```

A real number is also a complex number—it just has no imaginary part. This leads
to the idea that the set of real numbers is a subset of complex numbers, which is
expressed as:

```
⊂

```

where ⊂ means is a subset of.

© Springer-Verlag London Ltd., part of Springer Nature 2022 151
J. Vince, Mathematics for Computer Graphics, Undergraduate Topics
in Computer Science, https://doi.org/10.1007/978-1-4471-7520-9_9

<a id='p170'></a>
<!-- Página 170 -->

152 9 Complex Numbers

```
Although some mathematicians place i before its multiplier: i4, others place it
```

after the multiplier: 4i, which is the convention used in this book. However, when i
is associated with trigonometric functions, it is good practice to place it before the
```
function to avoid any confusion with the function’s angle. For example, sin αi could
```

imply that the angle is imaginary, whereas i sin α implies that the value of sin α is
imaginary.
```
Therefore, a complex number can be constructed in all sorts of ways:

sin α + i cos β, 2 − i tan α, 23 + x 2 i.

```

In general, we write a complex number as a + bi and subject it to the normal rules
of real algebra. All that we have to remember is that whenever we encounter i 2 it is
replaced by −1. For example:

```
(2 + 3i)(3 + 4i) = 2 × 3 + 2 × 4i + 3i × 3 + 3i × 4i
= 6 + 8i + 9i + 12i 2
= 6 + 17i − 12
= −6 + 17i.



```

9.2.1 Addition and Subtraction of Complex Numbers

Given two complex numbers:

```
z 1 = a1 + b1 i
z 2 = a2 + b2 i

```

then,
```
z 1 ± z 2 = (a1 ± a2 ) + (b1 ± b2 )i

```

where the real and imaginary parts are added or subtracted, respectively. The operations are closed, so long as a1 , b1 , a2 , b2 ∈ .
For example:

```
z 1 = 2 + 3i
z 2 = 4 + 2i
z 1 + z 2 = 6 + 5i
z 1 − z 2 = −2 + i.
```


<a id='p171'></a>
<!-- Página 171 -->

9.2 Definition of a Complex Number 153

9.2.2 Multiplying a Complex Number by a Scalar

A complex number is multiplied by a scalar using normal algebraic rules. For example, the complex number a + bi is multiplied by the scalar λ as follows:

```
λ(a + bi) = λa + λbi

```

for example:
```
3(2 + 5i) = 6 + 15i.



```

9.2.3 Product of Complex Numbers

Given two complex numbers:

```
z 1 = a1 + b1 i
z 2 = a2 + b2 i

```

their product is

```
z 1 z 2 = (a1 + b1 i) (a2 + b2 i)
= a1 a2 + a1 b2 i + b1 a2 i + b1 b2 i 2
= (a1 a2 − b1 b2 ) + (a1 b2 + b1 a2 )i

```

which is another complex number and confirms that the operation is closed. For
example:

```
z 1 = 3 + 4i
z 2 = 3 − 2i
z 1 z 2 = (3 + 4i)(3 − 2i)
= 9 − 6i + 12i − 8i 2
= 9 + 6i + 8
= 17 + 6i.

```

Note that the addition, subtraction and multiplication of complex numbers obey the
normal axioms of algebra.

<a id='p172'></a>
<!-- Página 172 -->

154 9 Complex Numbers

9.2.4 Square of a Complex Number

Given a complex number z, its square z 2 is given by:

```
z = a + bi
z 2 = (a + bi)(a + bi)
 
= a 2 − b2 + 2abi.

```

For example:

```
z = 4 + 3i
z 2 = (4 + 3i)(4 + 3i)
 
= 42 − 32 + 2 × 4 × 3i
= 7 + 24i.



```

9.2.5 Norm of a Complex Number

The norm, modulus or absolute value of a complex number z is written |z| and by
definition is

```
z = a + bi

|z| = a 2 + b2 .

```

For example, the norm of 3 + 4i is 5. We’ll see why this is so when we cover the
polar representation of a complex number.



9.2.6 Complex Conjugate of a Complex Number

The product of two complex numbers, where the only difference between them is
the sign of the imaginary part, gives rise to a special result:

```
(a + bi)(a − bi) = a 2 − abi + abi − b2 i 2
= a 2 + b2 .

```

This type of product always results in a real quantity and is used to resolve the quotient
of two complex numbers. Because this real value is such an interesting result, a − bi
is called the complex conjugate of z = a + bi, and is written either with a bar z̄, or
an asterisk z ∗ , and implies that

<a id='p173'></a>
<!-- Página 173 -->

9.2 Definition of a Complex Number 155

```
zz ∗ = a 2 + b2 = |z|2 .

```

For example:

```
z = 3 + 4i
z ∗ = 3 − 4i
zz ∗ = 9 + 16 = 25.



```

9.2.7 Quotient of Complex Numbers

The complex conjugate provides us with a mechanism to divide one complex number
by another. For instance, the quotient

```
a1 + b1 i
a2 + b2 i

```

is resolved by multiplying the numerator and denominator by the denominator’s
complex conjugate a2 − b2 i to create a real denominator:

```
a1 + b1 i (a1 + b1 i)(a2 − b2 i)
=
a2 + b2 i (a2 + b2 i)(a2 − b2 i)
a1 a2 − a1 b2 i + b1 a2 i − b1 b2 i 2
=
a22 + b22
   
a1 a2 + b1 b2 b1 a2 − a1 b2
= + i.
a22 + b22 a22 + b22

```

For example, to evaluate
```
4 + 3i
.
3 + 4i

```

we multiply top and bottom by the complex conjugate 3 − 4i:

```
4 + 3i (4 + 3i)(3 − 4i)
=
3 + 4i (3 + 4i)(3 − 4i)
12 − 16i + 9i − 12i 2
=
25
= 24
25
− 7
25
i.
```


<a id='p174'></a>
<!-- Página 174 -->

156 9 Complex Numbers

9.2.8 Inverse of a Complex Number

To compute the inverse of z = a + bi we start with

```
1
z −1 = .
z

```

Multiplying top and bottom by z ∗ we have
```
z∗
z −1 = .
zz ∗

```

But we have previously shown that zz ∗ = |z|2 , therefore,

```
z∗
z −1 =
|z|2
   
a b
= − i.
a 2 + b2 a 2 + b2

```

As an example, the inverse of 3 + 4i is

```
(3 + 4i)−1 = 25
3
− 25
4
i.

```

Let’s test this result by multiplying 3 + 4i by its inverse:
```
  3 
3 + 4i 25 − 25
4
i = 25
9
− 12
25
i + 12
25
i + 16
25
=1

```

which confirms the correctness of the result.



9.2.9 Square-Root of ±i
```
√
```

To find i we assume that the roots are complex. Therefore, we start with
```
√
i = a + bi
i = (a + bi)(a + bi)
= a 2 + 2abi − b2
= a 2 − b2 + 2abi

```

and equating real and imaginary parts we have

```
a 2 − b2 = 0
2ab = 1.
```


<a id='p175'></a>
<!-- Página 175 -->

9.2 Definition of a Complex Number 157

From this we deduce that √
```
a = b = ± 22 .

```

Therefore, the roots are √ √
```
i = ± 22 (1 + i).

```

Let’s test this result by squaring each root to ensure the answer is i:
```
 √ 2
± 22 (1 + i)(1 + i) = 21 2i = i.

√
```

To find −i we assume that the roots are complex. Therefore, we start with
```
√
−i = a + bi
−i = (a + bi)(a + bi)
= a 2 + 2abi − b2
= a 2 − b2 + 2abi

```

and equating real and imaginary parts we have

```
a 2 − b2 = 0
2ab = −1.

```

From this we deduce that √
```
a = b = ± 22 i.

```

Therefore, the roots are
```
√ √
−i = ± 22 i(1 + i)
√
= ± 22 (−1 + i)
√
= ± 22 (1 − i).

```

Let’s test this result by squaring each root to ensure the answer is −i:
```
 √ 2
± 22 (1 − i)(1 − i) = − 21 2i = −i.

```

We use these roots in the next chapter to investigate the rotational properties of
complex numbers.

<a id='p176'></a>
<!-- Página 176 -->

158 9 Complex Numbers

9.3 Ordered Pairs

So far, we have chosen to express a complex number as a + bi where we can distinguish between the real and imaginary parts. However, one thing we cannot assume
is that the real part is always first, and the imaginary part second, because bi + a
is also a complex number. Consequently, two functions are employed to extract the
real and imaginary coefficients as follows:

```
Re(a + bi) = a
Im(a + bi) = b

```

and leads us to the idea of representing a complex number by an ordered pair where
order is guaranteed:
```
a + bi = (a, b)

```

where b follows a to define the order. Thus the set  of complex numbers is equivalent
to the set 2 of ordered pairs (a, b).
```
Writing a complex number as an ordered pair was a great contribution, and first
```

made by Hamilton in 1833. Such notation is very succinct and free from any imaginary term, which can be added whenever required.



9.3.1 Addition and Subtraction of Ordered Pairs

Given two complex numbers:

```
z 1 = a1 + b1 i
z 2 = a2 + b2 i

```

they are written as ordered pairs:

```
z 1 = (a1 , b1 )
z 2 = (a2 , b2 )

```

and
```
z 1 ± z 2 = (a1 ± a2 , b1 ± b2 )

```

where the two parts are added or subtracted, respectively.
For example:

```
z 1 = 2 + 3i = (2, 3)
z 2 = 4 + 2i = (4, 2)
```


<a id='p177'></a>
<!-- Página 177 -->

9.3 Ordered Pairs 159

```
z 1 + z 2 = (6, 5)
z 1 − z 2 = (−2, 1).



```

9.3.2 Multiplying an Ordered Pair by a Scalar

We have already seen how a complex number is multiplied by a scalar, which must
be the same as ordered pairs:

```
λ(a, b) = (λa, λb).

```

An example is
```
3(2, 5) = (6, 15).



```

9.3.3 Product of Ordered Pairs

Given two complex numbers:

```
z 1 = a1 + b1 i
z 2 = a2 + b2 i

```

their product is
```
z 1 z 2 = (a1 a2 − b1 b2 ) + (a1 b2 + b1 a2 )i

```

which must also work with ordered pairs:

```
z 1 = (a1 , b1 )
z 2 = (a2 , b2 )
z 1 z 2 = (a1 , b1 )(a2 , b2 )
= (a1 a2 − b1 b2 , a1 b2 + b1 a2 ).

```

For example:

```
z 1 = (6, 2)
z 2 = (4, 3)
z 1 z 2 = (6, 2)(4, 3)
= (24 − 6, 18 + 8)
= (18, 26).
```


<a id='p178'></a>
<!-- Página 178 -->

160 9 Complex Numbers

9.3.4 Square of an Ordered Pair

The square of a complex number is given by:

```
z = a + bi
z 2 = (a + bi)(a + bi)
 
= a 2 − b2 + 2abi.

```

Therefore, the square of an ordered pair is:

```
z = (a, b)
z 2 = (a, b)(a, b)
 
= a 2 − b2 , 2ab .

```

For example:

```
z = (4, 3)
z 2 = (4, 3)(4, 3)
 
= 42 − 32 , 2 × 4 × 3
= (7, 24).

```

Let’s continue to develop an algebra based upon ordered pairs that is identical to the
algebra of complex numbers. We start by writing

```
z = (a, b)
= (a, 0) + (0, b)
= a(1, 0) + b(0, 1)

```

which creates the unit ordered pairs (1, 0) and (0, 1).
Now let’s compute the product (1, 0)(1, 0):

```
(1, 0)(1, 0) = (1 − 0, 0)
= (1, 0)

```

which shows that (1, 0) behaves like the real number 1. i.e. (1, 0) = 1.
Next, let’s compute the product (0, 1)(0, 1):

```
(0, 1)(0, 1) = (0 − 1, 0)
= (−1, 0)

```

which is the real number −1:

<a id='p179'></a>
<!-- Página 179 -->

9.3 Ordered Pairs 161

```
(0, 1)2 = −1

```

or √
```
(0, 1) = −1 and is imaginary.

```

This means that the ordered pair (a, b), together with its associated rules, represents
a complex number. i.e. (a, b) ≡ a + bi.



9.3.5 Norm of an Ordered Pair

The norm, modulus or absolute value of an ordered pair z is written |z| and by
definition is

```
z = (a, b)

|z| = a 2 + b2 .

```

For example, the norm of (3, 4) is 5.



9.3.6 Complex Conjugate of an Ordered Pair

The complex conjugate of z = a + bi is defined as z ∗ = a − bi, which in terms of
an ordered pair is z ∗ = (a, −b):

```
z = (a, b)
z ∗ = (a, −b)
zz ∗ = (a, b)(a, −b)
= (a 2 + b2 , ba − ab)
= (a 2 + b2 , 0)
= a 2 + b2 = |z|2 .



```

9.3.7 Quotient of an Ordered Pair

The technique for resolving z 1 /z 2 is to multiply the expression by z 2∗ /z 2∗ , which using
ordered pairs is

```
z1 (a1 , b1 )
=
z2 (a2 , b2 )
```


<a id='p180'></a>
<!-- Página 180 -->

162 9 Complex Numbers

```
(a1 , b1 ) (a2 , −b2 )
=
(a2 , b2 ) (a2 , −b2 )
(a1 a2 + b1 b2 , b1 a2 − a1 b2 )
=  2 
a2 + b22 , 0
 
a1 a2 + b1 b2 b1 a2 − a1 b2
= , .
a22 + b22 a22 + b22

```

For example, to evaluate
```
(4, 3)
.
(3, 4)

```

we multiply top and bottom by the complex conjugate (3, −4):

```
(4, 3) (4, 3)(3, −4)
=
(3, 4) (3, 4)(3, −4)
 
12 + 12 9 − 16
= ,
25 25
 24 
= 25 , − 25 .
7




```

9.3.8 Inverse of an Ordered Pair

We have previously shown that z −1 is

```
z∗ z∗
z −1 = =
zz ∗ |z|2

```

which using ordered pairs is

```
z = (a, b)
(a, −b)
z −1 =
(a, b)(a, −b)
(a, −b)
= 2 
a + b2 , 0
 
a −b
= , .
a 2 + b2 a 2 + b2

```

As an illustration, the inverse of (3, 4) is
```
3 
(3, 4)−1 = 25
, − 25
4
.
```


<a id='p181'></a>
<!-- Página 181 -->

9.3 Ordered Pairs 163

Let’s test this result by multiplying (3, 4) by its inverse:
```
3  9 
(3, 4) 25 , − 25
4
= 25 + 1625
, − 12
25
+ 12
25
= (1, 0).



```

9.3.9 Square-Root of ±i
```
√
```

To find i we assume that the roots are complex. Therefore, we start with
```
√
i = (a, b)
i = (a, b)(a, b)
 
(0, 1) = a 2 − b2 , 2ab

```

and equating left and right ordered elements we have

```
a 2 − b2 = 0
2ab = 1.

```

From this we deduce that √
```
a = b = ± 22 .

```

Therefore, the roots are √ √
```
i = ± 22 (1, 1).

```

Let’s test this result by squaring each root to ensure the answer is i:
```
 √ 2
± 22 (1, 1)(1, 1) = 21 (0, 2) = (0, 1).

√
```

To find −i we assume that the roots are complex. Therefore, we start with
```
√
−i = (a, b)
−i = (a, b)(a, b)
 
(0, −1) = a 2 − b2 , 2ab

```

and equating left and right ordered elements we have

```
a 2 − b2 = 0
2ab = −1.

```

From this we deduce that

<a id='p182'></a>
<!-- Página 182 -->

164 9 Complex Numbers
```
√
a = b = ± 22 i
√
= ± 22 (0, 1)(1, 1)
√
= ± 22 (−1, 1).

```

Therefore, the roots are √ √
```
−i = ± 22 (1, −1).

```

Let’s test this result by squaring each root to ensure the answer is −i:
```
 √ 2
± 22 (1, −1)(1, −1) = 21 (0, −2) = (0, −1).

```

It is obvious from the above definitions that ordered pairs provide an alternative
notation for expressing complex numbers, where the imaginary feature is embedded
within the product axiom. We will also use ordered pairs to define a quaternion with
three imaginary terms, which when incorporated within the product axiom remain
hidden.



9.4 Matrix Representation of a Complex Number

As quaternions have a matrix representation, perhaps we should investigate the matrix
representation for a complex number.
Although I have only hinted that i can be regarded as some sort of rotational
operator, this is the perfect way of visualising it. In Chap. 2 we discovered that
multiplying a complex number by i effectively rotates the number 90◦ anticlockwise.
So for the moment, it can be represented by a rotation matrix of 90◦ :

```
cos 90◦ − sin 90◦ 0 −1
i≡ =
sin 90◦ cos 90◦ 1 0

```

and the 2 × 2 identity matrix is
```
10
.
01

```

This permits us to write a complex number as:

```
10 0 −1
a + bi = a +b
01 1 0
a0 0 −b
= +
0a b 0
a −b
= .
b a
```


<a id='p183'></a>
<!-- Página 183 -->

9.4 Matrix Representation of a Complex Number 165

Note that the matrix representing i squares to −1:

```
0 −1 0 −1 −1 0
=
1 0 1 0 0 −1
10
= −1 .
01

```

However, we must also remember that i 2 = (−i)2 = −1, which is interpreted as
anticlockwise and clockwise rotations in the complex plane. This is confirmed by:

```
01 01 −1 0
=
−1 0 −1 0 0 −1
10
= −1 .
01

```

Now let’s employ matrix notation for all the arithmetic operations used for complex numbers.



9.4.1 Adding and Subtracting Complex Numbers

Two complex numbers are added or subtracted as follows:

```
z 1 = a1 + b1 i
z 2 = a2 + b2 i
a1 −b1
z1 =
b1 a1
a2 −b2
z2 =
b2 a2
a1 −b1 a −b2
z1 ± z2 = ± 2
b1 a1 b2 a2
a1 ± a2 −(b1 ± b2 )
= .
b1 ± b2 a1 ± a2

```

For example:

```
z 1 = 2 + 3i
z 2 = 4 + 2i
2 −3
z1 =
3 2
```


<a id='p184'></a>
<!-- Página 184 -->

166 9 Complex Numbers

```
4 −2
z2 =
2 4
2 −3 4 −2
z1 ± z2 = ±
3 2 2 4
6 −5
z1 + z2 = = 6 + 5i
5 6
−2 −1
z1 − z2 = = −2 + i.
1 −2



```

9.4.2 Product of Two Complex Numbers

The product of two complex numbers is computed as follows:

```
z 1 = a1 + b1 i
z 2 = a2 + b2 i
a1 −b1 a2 −b2
z1 z2 =
b1 a1 b2 a2
a1 a2 − b1 b2 −(a1 b2 + b1 a2 )
= .
a1 b2 + b1 a2 a1 a2 − b1 b2

```

For example:

```
z 1 = 6 + 2i
z 2 = 4 + 3i
6 −2 4 −3
z1 z2 =
2 6 3 4
24 − 6 −(18 + 8)
=
18 + 8 24 − 6
18 −26
= .
26 18



```

9.4.3 Norm Squared of a Complex Number

The square of the norm is as the determinant of the matrix:

```
z = a + bi
```


<a id='p185'></a>
<!-- Página 185 -->

9.4 Matrix Representation of a Complex Number 167

```
a −b
=
b a
a −b
|z|2 = a 2 + b2 = .
b a



```

9.4.4 Complex Conjugate of a Complex Number

The complex conjugate of a complex number is

```
a −b
z = a + bi =
b a
ab
z ∗ = a − bi = .
−b a

```

The product zz ∗ = a 2 + b2 :

```
a −b ab
zz ∗ =
b a −b a
a 2 + b2 0
=
0 a 2 + b2
  10
= a 2 + b2 .
01

```

For example:

```
3 −4
z = 3 + 4i =
4 3
34
z ∗ = 3 − 4i =
−4 3
3 −4 34 25 0
zz ∗ = =
4 3 −4 3 0 25
10
= 25 .
01



```

9.4.5 Inverse of a Complex Number

The inverse of 2 × 2 matrix A is given by

<a id='p186'></a>
<!-- Página 186 -->

168 9 Complex Numbers

```
a11 a12
```


## A=

```
a21 a22
1 a22 −a12
```


## A−1 =

```
a11 a22 − a12 a21 −a21 a12

```

therefore, the inverse of z is given by

```
z = a + bi
a −b
z=
b a
1 ab
z −1 = .
a 2 + b2 −b a

```

For example:

```
z = 3 + 4i
3 −4
z=
4 3
34
z −1 = 25
1
.
−4 3



```

9.4.6 Quotient of a Complex Number

The quotient of two complex numbers is computed as follows:

```
z 1 = a1 + b1 i
z 2 = a2 + b2 i
z1
= z 1 z 2−1
z2
a −b1 1 a2 b2
= 1
b1 a1 a22 + b22 −b2 a2
1 a1 a2 + b1 b2 −(b1 a2 − a1 b2 )
= .
a22 + b22 b1 a2 − a1 b2 a1 a2 + b1 b2

```

For example:

```
z 1 = 4 + 3i
z 2 = 3 + 4i
z1
= z 1 z 2−1
z2
```


<a id='p187'></a>
<!-- Página 187 -->

9.4 Matrix Representation of a Complex Number 169

```
4 −3 1 34
=
3 4 9 + 16 −4 3
24 7
= 25
1
.
−7 24



```

9.4.7 Square-Root of ±i
```
√
```

To find i we assume that the roots are complex. Therefore, we start with

```
√ a −b
i=
b a
a −b a −b
i=
b a b a
0 −1 a 2 − b2 −2ab
=
1 0 2ab a 2 − b2

```

and equating left and right matrices we have

```
a 2 − b2 = 0
2ab = 1.

```

From this we deduce that √
```
a = b = ± 22 .

```

Therefore, the roots are
```
√ √
1 −1
i = ± 22 .
1 1

```

Let’s test this result by squaring each root to ensure the answer is i:
```
 √ 2
1 −1 1 −1 0 −2
± 22 = 21 =i
1 1 1 1 2 0
√
```

To find −i we assume that the roots are complex. Therefore, we start with

```
√ a −b
−i =
b a
a −b a −b
−i =
b a b a
01 a 2 − b2 −2ab
=
−1 0 2ab a 2 − b2
```


<a id='p188'></a>
<!-- Página 188 -->

170 9 Complex Numbers

and equating left and right matrices we have

```
a 2 − b2 = 0
2ab = −1.

```

From this we deduce that √
```
a = b = ± 22 i.

```

Therefore, the roots are

```
√ √
0 −1 1 −1 √
11
−i = ± 22 = ± 22 .
1 0 1 1 −1 1

```

Let’s test this result by squaring each root to ensure the answer is i:
```
 √ 2 11 11 02
± 22 = 21 = −i
−1 1 −1 1 −2 0



```

9.5 Summary

We have shown in this chapter that there is a one-to-one correspondence between a
complex number and an ordered pair, and that a complex number can be represented
as a matrix, which permits us to compute all complex number operations as matrix
operations or ordered pairs.
If this the first time you have come across complex numbers you probably will
have found them strange on the one hand, and amazing on the other. Simply by
declaring the existence of i that squares to −1, opens up a new number system that
unifies large areas of mathematics.



9.6 Worked Examples

Here are some worked examples that employ the ideas described above. In some
cases a test is included to confirm the result.



9.6.1 Adding and Subtracting Complex Numbers

Add and subtract z 1 and z 2 .

<a id='p189'></a>
<!-- Página 189 -->

9.6 Worked Examples 171

Complex Number:

```
z 1 = 12 + 6i
z 2 = 10 − 4i
z 1 + z 2 = 22 + 2i
z 1 − z 2 = 2 + 10i.

```

Ordered Pair:

```
z 1 = (12, 6)
z 2 = (10, −4)
z 1 + z 2 = (12, 6) + (10, −4) = (22, 2)
z 1 − z 2 = (12, 6) − (10, −4) = (2, 10).

```

Matrix:

```
12 −6
z1 =
6 12
10 4
z2 =
−4 10
12 −6 10 4 22 −2
z1 + z2 = + =
6 12 −4 10 2 22
12 −6 10 4 2 −10
z1 − z2 = − = .
6 12 −4 10 10 2




```

9.6.2 Product of Complex Numbers

Compute the product z 1 z 2 .


Complex Number:

```
z 1 = 12 + 6i
z 2 = 10 − 4i
z 1 z 2 = (12 + 6i)(10 − 4i)
= 144 + 12i.
```


<a id='p190'></a>
<!-- Página 190 -->

172 9 Complex Numbers

Ordered Pair:

```
z 1 = (12, 6)
z 2 = (10, −4)
z 1 z 2 = (12, 6)(10, −4)
= (120 + 24, −48 + 60)
= (144, 12).

```

Matrix:

```
12 −6
z1 =
6 12
10 4
z2 =
−4 10
12 −6 10 4 144 −12
z1 z2 = = .
6 12 −4 10 12 144



```

9.6.3 Multiplying a Complex Number by i

Multiply z 1 by i.


Complex Number:

```
z 1 = 12 + 6i
z 1 i = (12 + 6i)i
= −6 + 12i.

```

Ordered Pair:

```
z 1 = (12, 6)
i = (0, 1)
z 1 i = (12, 6)(0, 1)
= (−6, 12).

```

Matrix:

<a id='p191'></a>
<!-- Página 191 -->

9.6 Worked Examples 173

```
12 −6
z1 =
6 12
0 −1
i=
1 0
12 −6 0 −1 −6 −12
z1 z2 = = .
6 12 1 0 12 −6



```

9.6.4 The Norm of a Complex Number

Compute the norm of z 1 .


Complex Number:

```
z 1 = 12 + 6i

|z 1 | = 122 + 62 ≈ 13.416.

```

Ordered Pair:

```
z 1 = (12, 6)

|z 1 | = 122 + 62 ≈ 13.416.

```

Matrix:

```
12 −6
z1 =
6 12
12 −6 
|z 1 | = = 122 + 62 ≈ 13.416.
6 12



```

9.6.5 The Complex Conjugate of a Complex Number

Compute the complex conjugate of the following.


Complex Number:

```
(2 + 3i)∗ = 2 − 3i
```


<a id='p192'></a>
<!-- Página 192 -->

174 9 Complex Numbers

```
1∗ = 1
i ∗ = −i.

```

Ordered Pair:

```
(2, 3)∗ = (2, −3)
(1, 0)∗ = (1, 0)
(0, 1)∗ = (0, −1).

```

Matrix:

```
2 −3
z=
3 2
23
z∗ =
−3 2
10
1=
01
10
1∗ =
01
0 −1
i=
1 0
01
i∗ = .
−1 0




```

9.6.6 The Quotient of Two Complex Numbers

Compute the quotient (2 + 3i)/(3 + 4i).


Complex Number:

```
2 + 3i (2 + 3i) (3 − 4i)
=
3 + 4i (3 + 4i) (3 − 4i)
6 − 8i + 9i + 12
=
25
= 25 + 25 i.
18 1
```


<a id='p193'></a>
<!-- Página 193 -->

9.6 Worked Examples 175

Test:
```
 
(3 + 4i) 18
25
+ 25
1
i = 54
25
+ 25
3
i + 72
25
i − 25
4

= 2 + 3i.

```

Ordered Pair:

```
(2, 3) (2, 3) (3, −4)
=
(3, 4) (3, 4) (3, −4)
(6 + 12, 1)
=
(9 + 16, 0)
 18 1 
= 25 , 25 .

```

Matrix:

```
2 −3
z1 =
3 2
3 −4
z2 =
4 3
z1
= z 1 z 2−1
z2
2 −3 34
= 25
1
3 2 −4 3
18 −1
= 25
1
.
1 18



```

9.6.7 Divide a Complex Number by i

Divide 2 + 3i by i.


Complex Number:

```
2 + 3i (2 + 3i) (0 − i)
=
0+i (0 + i) (0 − i)
−2i + 3
=
1
= 3 − 2i.
```


<a id='p194'></a>
<!-- Página 194 -->

176 9 Complex Numbers

Test:

```
i(3 − 2i) = 2 + 3i.

```

Ordered Pair:

```
(2, 3) (2, 3) (0, −1)
=
(0, 1) (0, 1) (0, −1)
(3, −2)
=
(1, 0)
= (3, −2).

```

Matrix:

```
2 −3
z=
3 2
0 −1
i=
1 0
01
i −1 =
−1 0
2 −3 01 32
zi −1 = = .
3 2 −1 0 −2 3



```

9.6.8 Divide a Complex Number by −i

Divide 2 + 3i by −i.


Complex Number:

```
2 + 3i (2 + 3i) (0 + i)
=
0−i (0 − i) (0 + i)
2i − 3
=
1
= −3 + 2i.

```

Test:

```
−i(−3 + 2i) = 2 + 3i.
```


<a id='p195'></a>
<!-- Página 195 -->

9.6 Worked Examples 177

Ordered Pair:

```
(2, 3) (2, 3) (0, 1)
=
(0, −1) (0, −1) (0, 1)
(−3, 2)
=
1
= (−3, 2).

```

Matrix:

```
2 −3
z=
3 2
01
−i =
−1 0
0 −1
−i −1 =
1 0
  2 −3 0 −1 −3 −2
z −i −1 = = .
3 2 1 0 2 −3



```

9.6.9 The Inverse of a Complex Number

Compute the inverse of 2 + 3i.


Complex Number:

```
1 1 (2 − 3i)
=
2 + 3i (2 + 3i) (2 − 3i)
2 − 3i
=
13
= 13
2
− 13
3
i.

```

Ordered Pair:

```
1 1 (2, −3)
=
(2, 3) (2, 3) (2, −3)
(2, −3)
=
 2 13 3 
= 13 , − 13 .
```


<a id='p196'></a>
<!-- Página 196 -->

178 9 Complex Numbers

Matrix:

```
2 −3
z=
3 2
23
z −1 = 13
1
.
−3 2



```

9.6.10 The Inverse of i

Compute the inverse of i.


Complex Number:

```
1 1 (0 − i)
=
0+i (0 + i) (0 − i)
−i
= = −i.
1

```

Ordered Pair:

```
1 1 (0, −1)
=
(0, 1) (0, 1) (0, −1)
(0, −1)
= = (0, −1) = −i.
(1, 0)

```

Matrix:

```
0 −1
i=
1 0
01
i −1 = = −i.
−1 0



```

9.6.11 The Inverse of −i

Compute the inverse of −i.


Complex Number:

<a id='p197'></a>
<!-- Página 197 -->

9.6 Worked Examples 179

```
1 1 (0 + i)
=
0−i (0 − i) (0 + i)
i
= = i.
1

```

Ordered Pair:

```
1 1 (0, 1)
=
(0, −1) (0, −1) (0, 1)
(0, 1)
= = (0, 1) = i.
(1, 0)

```

Matrix:

```
01
−i =
−1 0
0 −1
−i −1 = = i.
1 0




```

Reference

1. Vince J (2018) Imaginary mathematics for computer science. Springer

<a id='p198'></a>
<!-- Página 198 -->


## Chapter 10

Geometric Transforms




10.1 Introduction

This chapter shows how matrices are used to scale, translate, reflect, shear and rotate
2D shapes and 3D objects. The reader should try to understand the construction of the
various matrices and recognise the role of each matrix element. After a little practice
it will be possible to define a wide variety of matrices without thinking about the
underlying algebra.



10.2 Background

A point P(x, y) is transformed into P  (x  , y  ) by manipulating the original coordinates x and y using

```
x  = ax + by + e
y  = cx + dy + f,

```

where a, b, c, d, e and f have assigned values. Similarly, a 3D point P(x, y, z)
is transformed into P  (x  , y  , z  ) using

```
x  = ax + by + cz + k
y  = d x + ey + f z + l
z  = gx + hy + j z + m.

```

The values for a, b, c, . . . etc. determine whether the transform translates, shears,
scales, reflects or rotates a point.



© Springer-Verlag London Ltd., part of Springer Nature 2022 181
J. Vince, Mathematics for Computer Graphics, Undergraduate Topics
in Computer Science, https://doi.org/10.1007/978-1-4471-7520-9_10

<a id='p199'></a>
<!-- Página 199 -->

182 10 Geometric Transforms

Although transforms have an algebraic origin, it is convenient to express them as
matrices, which provide certain advantages for viewing the transform and for interfacing to various types of computer graphics hardware. We begin with an algebraic
approach and then introduce matrix notation.



10.3 2D Transforms

10.3.1 Translation

Cartesian coordinates provide a one-to-one relationship between number and shape,
such that when we change a shape’s coordinates, we change its geometry. For example, if P(x, y) is a shape’s vertex, when we apply the operation x  = x + 3 we create
a new point P  (x  , y) three units to the right. Similarly, the operation y  = y + 1
creates a new point P  (x, y  ) displaced one unit vertically. By applying both of these
transforms to every vertex on the original shape, the shape is displaced as shown in
Fig. 10.1.



10.3.2 Scaling

Shape scaling is effected by multiplying coordinates as follows:

```
x  = 2.5x
y  = 1.5y.

p
```

Fig. 10.1 The translated y
shape results by adding 3 to 3
every x-coordinate, and 1 to
every y-coordinate to the translated
original shape
```
2
original
1



1 2 3 4 5 x
```


<a id='p200'></a>
<!-- Página 200 -->

10.3 2D Transforms 183
```
p
```

Fig. 10.2 The scaled shape y
results by multiplying the 3
x-coordinates by 2.5 and the
y-coordinates by 1.5 scaled
```
2
original

1



1 2 3 4 5 x



```

This transform results in a horizontal scaling of 2.5 and a vertical scaling of 1.5 as
illustrated in Fig. 10.2. Note that a point located at the origin does not change its
place, so scaling is relative to the origin.



10.3.3 Reflection

To make a reflection of a shape relative to the y-axis, we simply reverse the sign of
the x-coordinates, leaving the y-coordinates unchanged:

```
x  = −x
y = y

```

and to reflect a shape relative to the x-axis we reverse the y-coordinates:

```
x = x
y  = −y.

```

Figure 10.3 shows three reflections derived from the original shape by reversing the
signs for the x- and y-coordinates. Note that a shape’s vertex order is reversed for
each reflection.
Before proceeding, we pause to introduce matrix notation so that we can develop
further transforms using algebra and matrix algebra side by side.

<a id='p201'></a>
<!-- Página 201 -->

184 10 Geometric Transforms

```
p
```

Fig. 10.3 The original shape y
gives rise to three reflections
simply by reversing the signs 1
of its coordinates
```
reflected about
the y-axis original


-2 -1 1 2 x
reflected about reflected about
the x- & y-axes the x-axis
-1




```

10.4 Transforms as Matrices

10.4.1 Systems of Notation

Over time two systems of matrix notation have evolved: one where the matrix multiplies a column vector, as described above, and another where a row vector multiplies
the matrix:  
```
     a c  
x y = x y = ax + by cx + dy .
bd

```

Note how the elements of the matrix are transposed to accommodate the algebraic
correctness of the transform. There is no preferred system of notation, and you will
find technical books and papers supporting both. Personally, I prefer a matrix premultiplying a column vector, as it is very similar to the original algebraic equations.
However, the important thing to remember is that the rows and columns of the matrix
are transposed when moving between the two systems.



10.5 Homogeneous Coordinates


## Chapter 8 showed how a pair of equations such as


```
x  = ax + by
y  = cx + dy

```

can be written in matrix notation as:
```
    
x ab x
= .
y cd y
```


<a id='p202'></a>
<!-- Página 202 -->

10.5 Homogeneous Coordinates 185

One immediate problem with this notation is that there is no apparent mechanism to
add or subtract a constant such as e or f :

```
x  = ax + by + e
y  = cx + dy + f.

```

Mathematicians resolved this by using homogeneous coordinates, which appeared
in the early 19th century where they were independently proposed by the German
mathematician August Möbius (1790–1868) (who also is associated with a one-sided
curled band, the Möbius strip), and the German mathematician and physicist Julius
Plücker (1801–1868). Möbius called them barycentric coordinates, and they have
also been called areal coordinates because of their area-calculating properties.
```
Basically, homogeneous coordinates define a point in a plane using three coordi-
```

nates instead of two. Initially, Plücker located a homogeneous point relative to the
sides of a triangle, but later revised his notation to the one employed in contemporary
mathematics and computer graphics. This states that for a point (x, y) there exists a
homogeneous point (xt, yt, t) where t is an arbitrary number. For example, the point
(3, 4) has homogeneous coordinates (6, 8, 2), because 3 = 6/2 and 4 = 8/2. But
the homogeneous point (6, 8, 2) is not unique to (3, 4); (12, 16, 4), (15, 20, 5)
and (300, 400, 100) are all possible homogeneous coordinates for (3, 4).
```
The reason why this coordinate system is called ‘homogeneous’ is because it is
```

possible to transform functions such as f (x, y) into the form f (x/t, y/t) without
disturbing the degree of the curve. To the non-mathematician this may not seem
anything to get excited about, but in the field of projective geometry it is a very
powerful concept.
```
Figure 10.4 shows a 3D homogeneous space with axes x, y and h, where a point
```

(x, y, 1) is associated with a projected point (xt, yt, t). The figure shows a triangle
on the h = 1 plane, and a similar triangle on the plane h = t. Thus instead of working
in two dimensions, we can work on an arbitrary xy-plane in three dimensions. The hcoordinate of the plane is immaterial because the x- and y-coordinates are eventually
divided by t. However, to keep things simple it seems a good idea to choose t = 1.


Fig. 10.4 2D homogeneous y
coordinates can be visualised (xt, yt, t)
as a plane in 3D space
generally where h = 1, for
convenience

```
(x, y, 1)
h
t
x
1
```


<a id='p203'></a>
<!-- Página 203 -->

186 10 Geometric Transforms

This means that the point (x, y) has homogeneous coordinates (x, y, 1) making
scaling superfluous.
```
If we substitute 3D homogeneous coordinates for traditional 2D Cartesian coordi-
```

nates we must attach 1 to every (x, y) pair. When a point (x, y, 1) is transformed,
it emerges as (x  , y  , 1), and we discard the 1. This may seem a futile exercise, but
it resolves the problem of creating a translation transform.
```
Consider the following transform on the homogeneous point (x, y, 1):
⎡ ⎤ ⎡ ⎤⎡ ⎤
x ab e x
⎣ y ⎦ = ⎣ c d f ⎦ ⎣ y ⎦ .
1 00 1 1

```

This expands to

```
x  = ax + by + e
y  = cx + dy + f
1=1

```

and solves the above problem of adding a constant. Now let’s move on to see how
homogeneous coordinates are used in practice.



10.5.1 2D Translation

The algebraic and matrix notation for 2D translation is

```
x  = x + tx
y = y + ty

```

or using matrices: ⎡ ⎤ ⎡ ⎤⎡ ⎤
```
x 1 0 tx x
⎣ y ⎦ = ⎣ 0 1 ty ⎦ ⎣ y ⎦ .
1 00 1 1



```

10.5.2 2D Scaling

The algebraic and matrix notation for 2D scaling is

```
x  = sx x
y = sy y
```


<a id='p204'></a>
<!-- Página 204 -->

10.5 Homogeneous Coordinates 187

or using matrices: ⎡ ⎤ ⎡ ⎤⎡ ⎤
```
x sx 0 0 x
⎣ y ⎦ = ⎣ 0 sy 0 ⎦ ⎣ y ⎦ .
1 0 0 1 1

```

The scaling action is relative to the origin, i.e. the point (0, 0) remains unchanged.
All other points move away from the origin when sx > 1, or move towards the origin
when sx < 1. To scale relative to another point ( px , p y ) we first subtract ( px , p y )
```
from (x, y) respectively. This effectively makes the reference point ( px , p y ) the
```

new origin. Second, we perform the scaling operation relative to the new origin,
and third, add ( px , p y ) back to the new (x, y) respectively to compensate for the
original subtraction. Algebraically this is

```
x  = sx (x − px ) + px
y  = s y (y − p y ) + p y

```

which simplifies to

```
x  = sx x + px (1 − sx )
y  = s y y + p y (1 − s y )

```

or as a homogeneous matrix:
```
⎡ ⎤ ⎡ ⎤⎡ ⎤
x sx 0 px (1 − sx ) x
⎣ y  ⎦ = ⎣ 0 s y p y (1 − s y ) ⎦ ⎣ y ⎦ . (10.1)
1 0 0 1 1

```

For example, to scale a shape by 2 relative to the point (1, 1) the matrix is
```
⎡ ⎤ ⎡ ⎤⎡ ⎤
x 2 0 −1 x
⎣ y  ⎦ = ⎣ 0 2 −1 ⎦ ⎣ y ⎦ .
1 00 1 1



```

10.5.3 2D Reflections

The matrix notation for reflecting about the y-axis is
```
⎡ ⎤ ⎡ ⎤⎡ ⎤
x −1 0 0 x
⎣ y ⎦ = ⎣ 0 1 0 ⎦ ⎣ y ⎦
1 001 1

```

or about the x-axis:

<a id='p205'></a>
<!-- Página 205 -->

188 10 Geometric Transforms
```
⎡ ⎤ ⎡ ⎤⎡ ⎤
x 1 00 x
⎣ y  ⎦ = ⎣ 0 −1 0 ⎦ ⎣ y ⎦ .
1 0 01 1

```

However, to make a reflection about an arbitrary vertical or horizontal axis we need
to introduce some more algebraic deception.
```
To make a reflection about the vertical axis x = 1, we first subtract 1 from the
```

x-coordinate. This effectively makes the x = 1 axis coincident with the major y-axis.
Next, we perform the reflection by reversing the sign of the modified x-coordinate.
And finally, we add 1 to the reflected coordinate to compensate for the original
subtraction. Algebraically, the three steps are

```
x1 = x − 1
x2 = −(x − 1)
x  = −(x − 1) + 1

```

which simplifies to

```
x  = −x + 2
y = y

```

or in matrix form: ⎡ ⎤ ⎡ ⎤⎡ ⎤
```
x −1 0 2 x
⎣ y ⎦ = ⎣ 0 1 0 ⎦ ⎣ y ⎦ .
1 001 1

```

Figure 10.5 illustrates this process.
To reflect a point about an arbitrary y-axis, x = ax , the following transform is
required:

```
x  = −(x − ax ) + ax = −x + 2ax
y = y

p
```

Fig. 10.5 The shape on the y
right is reflected about the 3
x = 1 axis

```
2
reflected original

1



-1 1 2 3 4 x
```


<a id='p206'></a>
<!-- Página 206 -->

10.5 Homogeneous Coordinates 189

or in matrix form: ⎡ ⎤ ⎡ ⎤⎡ ⎤
```
x −1 0 2ax x
⎣ y ⎦ = ⎣ 0 1 0 ⎦ ⎣ y ⎦ . (10.2)
1 00 1 1

```

Similarly, to reflect a point about an arbitrary x-axis y = a y , the following transform is required:

```
x = x
y  = −(y − a y ) + a y = −y + 2a y

```

or in matrix form: ⎡ ⎤ ⎡ ⎤⎡ ⎤
```
x 1 0 0 x
⎣ y  ⎦ = ⎣ 0 −1 2a y ⎦ ⎣ y ⎦ .
1 0 0 1 1




```

10.5.4 2D Shearing

A shape is sheared by leaning it over at an angle β. Figure 10.6 illustrates the
geometry, and we see that the y-coordinates remain unchanged but the x-coordinates
are a function of y and tan β.

```
x  = x + y tan β
y = y

```

or in matrix form:


Fig. 10.6 The original
green, square shape is
sheared to the right by an
angle β, and the horizontal
shear is proportional to
y tan β

<a id='p207'></a>
<!-- Página 207 -->

190 10 Geometric Transforms
```
⎡ ⎤ ⎡ ⎤⎡ ⎤
x 1 tan β 0 x
⎣ y ⎦ = ⎣ 0 1 0 ⎦ ⎣ y ⎦ .
1 0 0 1 1




```

10.5.5 2D Rotation

Figure 10.7 shows a point P(x, y), distance R from the origin, which is to be rotated
by an angle β about the origin to P  (x  , y  ). It can be seen that

```
x  = R cos(θ + β)
y  = R sin(θ + β)

```

and substituting the identities for cos(θ + β) and sin(θ + β) we have

```
x  = R(cos θ cos β − sin θ sin β)
y  = R(sin θ cos β + cos θ sin β)
x y
x = R cos β − sin β
```


## R R

```
y x
y = R cos β + sin β
```


## R R

```
x  = x cos β − y sin β
y  = x sin β + y cos β

```

or in matrix form: ⎡ ⎤ ⎡ ⎤⎡ ⎤
```
x cos β − sin β 0 x
⎣ y  ⎦ = ⎣ sin β cos β 0 ⎦ ⎣ y ⎦ .
1 0 0 1 1


```

Fig. 10.7 The point
P(x, y) is rotated through
an angle β to P  (x  , y  )

<a id='p208'></a>
<!-- Página 208 -->

10.5 Homogeneous Coordinates 191

For example, to rotate a point through 90◦ the matrix is
```
⎡ ⎤ ⎡ ⎤⎡ ⎤
x 0 −1 0 x
⎣ y ⎦ = ⎣ 1 0 0 ⎦ ⎣ y ⎦ .
1 0 01 1

```

Thus the point (1, 0) becomes (0, 1). If we rotate through 360◦ the matrix becomes
```
⎡ ⎤ ⎡ ⎤⎡ ⎤
x 100 x
⎣ y ⎦ = ⎣ 0 1 0 ⎦ ⎣ y ⎦ .
1 001 1

```

Such a matrix has a null effect and is called an identity matrix.
```
To rotate a point (x, y) about an arbitrary point ( px , p y ) we first, subtract
```

( px , p y ) from the coordinates (x, y) respectively. This enables us to perform the
rotation about the origin. Second, we perform the rotation, and third, we add ( px , p y )
to compensate for the original subtraction. Here are the steps:
1. Subtract ( px , p y ):

```
x1 = (x − px )
y1 = (y − p y ).

```

2. Rotate β about the origin:

```
x2 = (x − px ) cos β − (y − p y ) sin β
y2 = (x − px ) sin β + (y − p y ) cos β.

```

3. Add ( px , p y ):

```
x  = (x − px ) cos β − (y − p y ) sin β + px
y  = (x − px ) sin β + (y − p y ) cos β + p y .

```

Simplifying,

```
x  = x cos β − y sin β + px (1 − cos β) + p y sin β
y  = x sin β + y cos β + p y (1 − cos β) − px sin β

```

and in matrix form:
```
⎡ ⎤ ⎡ ⎤⎡ ⎤
x cos β − sin β px (1 − cos β) + p y sin β x
⎣ y  ⎦ = ⎣ sin β cos β p y (1 − cos β) − px sin β ⎦ ⎣ y ⎦ . (10.3)
1 0 0 1 1

```

For example, to rotate a point 90◦ about the point (1, 1) the matrix operation becomes

<a id='p209'></a>
<!-- Página 209 -->

192 10 Geometric Transforms
```
⎡ ⎤ ⎡ ⎤⎡ ⎤
x 0 −1 2 x
⎣ y ⎦ = ⎣ 1 0 0 ⎦ ⎣ y ⎦ .
1 0 01 1

```

A simple test is to substitute the point (2, 1) for (x, y); which is transformed correctly to (1, 2).
```
The algebraic approach in deriving the above transforms is relatively easy. How-
```

ever, it is also possible to use matrices to derive compound transforms, such as a
reflection relative to an arbitrary line and scaling and rotation relative to an arbitrary
point. These transforms are called affine, as parallel lines remain parallel after being
transformed. Furthermore, the word ‘affine’ is used to imply that there is a strong
geometric affinity between the original and transformed shape. One can not always
guarantee that angles and lengths are preserved, as the scaling transform can alter
these when different x and y scaling factors are used. For completeness, we will
repeat these transforms from a matrix perspective.



10.5.6 2D Scaling

The strategy used to scale a point (x, y) relative to some arbitrary point ( px , p y )
is to first, translate (− px , − p y ); second, perform the scaling; and third translate
( px , p y ). These three transforms are represented in matrix form as follows:
⎡ ⎤ ⎡ ⎤
```
x       x
```

⎣ y  ⎦ = translate( px , p y ) scale(sx , s y ) translate(− px , − p y ) ⎣ y ⎦
```
1 1

```

which expands to
```
⎡ ⎤ ⎡ ⎤⎡ ⎤⎡ ⎤⎡ ⎤
x 1 0 px sx 0 0 1 0 − px x
⎣ y ⎦ = ⎣ 0 1 py ⎦ ⎣ 0 sy 0 ⎦ ⎣ 0 1 − py ⎦ ⎣ y ⎦ .
1 00 1 0 0 1 00 1 1

```

Note the sequence of the transforms, as this often causes confusion. The first transform acting on the point (x, y, 1) is translate (− px , − p y ), followed by scale
(sx , s y ), followed by translate ( px , p y ). If they are placed in any other sequence,
you will discover, like Gauss, that transforms are not commutative!
```
We can now combine these matrices into a single matrix by multiplying them
```

together. This can be done in any sequence, so long as we preserve the original order.
Let’s start with scale (sx , s y ) and translate (− px , − p y ) matrices. This produces
```
⎡ ⎤ ⎡ ⎤⎡ ⎤⎡ ⎤
x 1 0 px sx 0 −sx px x
⎣ y  ⎦ = ⎣ 0 1 p y ⎦ ⎣ 0 s y −s y p y ⎦ ⎣ y ⎦
1 00 1 0 0 1 1
```


<a id='p210'></a>
<!-- Página 210 -->

10.5 Homogeneous Coordinates 193

and finally: ⎡ ⎤ ⎡ ⎤⎡ ⎤
```
x sx 0 px (1 − sx ) x
⎣ y  ⎦ = ⎣ 0 s y p y (1 − s y ) ⎦ ⎣ y ⎦
1 0 0 1 1

```

which is the same as the previous transform (10.1).



10.5.7 2D Reflection

A reflection about the y-axis is given by
```
⎡ ⎤ ⎡ ⎤⎡ ⎤
x −1 0 0 x
⎣ y ⎦ = ⎣ 0 1 0 ⎦ ⎣ y ⎦ .
1 001 1

```

Therefore, using matrices, we can reason that a reflection transform about an arbitrary
axis x = ax , parallel with the y-axis, is given by
```
⎡ ⎤ ⎡ ⎤
x       x
⎣ y  ⎦ = translate(ax , 0) reflection translate(−ax , 0) ⎣ y ⎦
1 1

```

which expands to
```
⎡ ⎤ ⎡ ⎤⎡ ⎤⎡ ⎤⎡ ⎤
x 1 0 ax −1 0 0 1 0 −ax x
⎣ y ⎦ = ⎣ 0 1 0 ⎦ ⎣ 0 1 0 ⎦ ⎣ 0 1 0 ⎦ ⎣ y ⎦ .
1 00 1 001 00 1 1

```

We can now combine these matrices into a single matrix by multiplying them together.
Let’s begin by multiplying the reflection and the translate (−ax , 0) matrices together.
This produces ⎡ ⎤ ⎡ ⎤⎡ ⎤⎡ ⎤
```
x 1 0 ax −1 0 ax x
⎣ y ⎦ = ⎣ 0 1 0 ⎦ ⎣ 0 1 0 ⎦ ⎣ y ⎦
1 00 1 00 1 1

```

and finally: ⎡ ⎤ ⎡ ⎤⎡ ⎤
```
x −1 0 2ax x
⎣ y ⎦ = ⎣ 0 1 0 ⎦ ⎣ y ⎦
1 00 1 1

```

which is the same as the previous transform (10.2).

<a id='p211'></a>
<!-- Página 211 -->

194 10 Geometric Transforms

10.5.8 2D Rotation About an Arbitrary Point

A rotation about the origin is given by
```
⎡ ⎤ ⎡ ⎤⎡ ⎤
x cos β − sin β 0 x
⎣ y  ⎦ = ⎣ sin β cos β 0 ⎦ ⎣ y ⎦
1 0 0 1 1

```

Therefore, using matrices, we can develop a rotation about an arbitrary point ( px , p y )
as follows:
```
⎡ ⎤ ⎡ ⎤
x       x
⎣ y  ⎦ = translate( px , p y ) rotateβ translate(− px , − p y ) ⎣ y ⎦
1 1

```

which expands to
```
⎡ ⎤ ⎡ ⎤⎡ ⎤⎡ ⎤⎡ ⎤
x 1 0 px cos β − sin β 0 1 0 − px x
⎣ y  ⎦ = ⎣ 0 1 p y ⎦ ⎣ sin β cos β 0 ⎦ ⎣ 0 1 − p y ⎦ ⎣ y ⎦ .
1 00 1 0 0 1 00 1 1

```

We can now combine these matrices into a single matrix by multiplying them together.
Let’s begin by multiplying the rotate β and the translate (− px , − p y ) matrices
together. This produces
```
⎡ ⎤ ⎡ ⎤⎡ ⎤⎡ ⎤
x 1 0 px cos β − sin β − px cos β + p y sin β x
⎣ y  ⎦ = ⎣ 0 1 p y ⎦ ⎣ sin β cos β − px sin β − p y cos β ⎦ ⎣ y ⎦
1 00 1 0 0 1 1
⎡ ⎤ ⎡ ⎤⎡ ⎤
x cos β − sin β px (1 − cos β) + p y sin β x
⎣ y  ⎦ = ⎣ sin β cos β p y (1 − cos β) − px sin β ⎦ ⎣ y ⎦
1 0 0 1 1

```

which is the same as the previous transform (10.3).
I hope it is now clear to the reader that one can derive all sorts of transforms either
algebraically, or by using matrices—it is just a question of convenience.



10.6 3D Transforms

Now we come to transforms in three dimensions, where we apply the same reasoning
as in two dimensions. Scaling and translation are basically the same, but where in
2D we rotated a shape about a point, in 3D we rotate an object about an axis.

<a id='p212'></a>
<!-- Página 212 -->

10.6 3D Transforms 195

10.6.1 3D Translation

The algebra is so simple for 3D translation that we can simply write the homogeneous
matrix directly: ⎡ ⎤ ⎡ ⎤⎡ ⎤
```
x 1 0 0 tx x
⎢ y ⎥ ⎢ 0 1 0 ty ⎥ ⎢ y ⎥
⎢ ⎥=⎢ ⎥⎢ ⎥
⎣ z ⎦ ⎣ 0 0 1 tz ⎦ ⎣ z ⎦ .
1 000 1 1



```

10.6.2 3D Scaling

The algebra for 3D scaling is

```
x  = sx x
y = sy y
z  = sz z

```

which in matrix form is
```
⎡ ⎤ ⎡ ⎤⎡ ⎤
x sx 0 0 0 x
⎢ y ⎥ ⎢ 0 sy 0 0 ⎥ ⎢ y ⎥
⎢ ⎥=⎢ ⎥⎢ ⎥
⎣ z ⎦ ⎣ 0 0 sz 0 ⎦ ⎣ z ⎦ .
1 0 0 0 1 1

```

The scaling is relative to the origin, but we can arrange for it to be relative to an
arbitrary point ( px , p y , pz ) using the following algebra:

```
x  = sx (x − px ) + px
y  = s y (y − p y ) + p y
z  = sz (z − pz ) + pz

```

which in matrix form is
```
⎡ ⎤ ⎡ ⎤⎡ ⎤
x sx 0 0 px (1 − sx ) x
⎢ y  ⎥ ⎢ 0 s y 0 p y (1 − s y ) ⎥ ⎢ y ⎥
⎢ ⎥=⎢ ⎥⎢ ⎥
⎣ z ⎦ ⎣ 0 0 sz pz (1 − sz ) ⎦ ⎣ z ⎦ .
1 0 0 0 1 1
```


<a id='p213'></a>
<!-- Página 213 -->

196 10 Geometric Transforms

10.6.3 3D Rotation

In two dimensions a shape is rotated about a point, whether it be the origin or some
other position. In three dimensions an object is rotated about an axis, whether it be the
x-, y- or z-axis, or some arbitrary axis. To begin with, let’s look at rotating a vertex
about one of the three orthogonal axes; such rotations are called Euler rotations after
Leonhard Euler.
Recall that a general 2D rotation transform is given by
```
⎡ ⎤ ⎡ ⎤⎡ ⎤
x cos β − sin β 0 x
⎣ y  ⎦ = ⎣ sin β cos β 0 ⎦ ⎣ y ⎦
1 0 0 1 1

```

which in 3D can be visualised as rotating a point P(x, y, z) on a plane parallel with
the x y-plane as shown in Fig. 10.8. In algebraic terms this is written as

```
x  = x cos β − y sin β
y  = x sin β + y cos β
z  = z.

```

Therefore, the 3D rotation transform is
```
⎡ ⎤ ⎡ ⎤⎡ ⎤
x cos β − sin β 0 0 x
⎢ y  ⎥ ⎢ sin β cos β 0 0 ⎥ ⎢ y ⎥
⎢ ⎥=⎢ ⎥⎢ ⎥
⎣z ⎦ ⎣ 0 0 1 0⎦⎣ z ⎦
1 0 0 01 1

```

which basically rotates a point about the z-axis.
When rotating about the x-axis, the x-coordinates remain constant whilst the yand z-coordinates are changed. Algebraically, this is


Fig. 10.8 Rotating the point
P, through an angle β, about
the z-axis

<a id='p214'></a>
<!-- Página 214 -->

10.6 3D Transforms 197

```
x = x
y  = y cos β − z sin β
z  = y sin β + z cos β

```

or in matrix form: ⎡ ⎤ ⎡ ⎤⎡ ⎤
```
x 1 0 0 0 x
⎢ y  ⎥ ⎢ 0 cos β − sin β 0 ⎥ ⎢ y ⎥
⎢ ⎥=⎢ ⎥⎢ ⎥
⎣ z ⎦ ⎣ 0 sin β cos β 0 ⎦ ⎣ z ⎦ .
1 0 0 0 1 1

```

When rotating about the y-axis, the y-coordinate remains constant whilst the x- and
z-coordinates are changed. Algebraically, this is

```
x  = z sin β + x cos β
y = y
z  = z cos β − x sin β

```

or in matrix form: ⎡ ⎤ ⎡ ⎤⎡ ⎤
```
x cos β 0 sin β 0 x
⎢ y ⎥ ⎢ 0 1 0 0 ⎥⎢y⎥
⎢ ⎥=⎢ ⎥⎢ ⎥
⎣ z ⎦ ⎣ − sin β 0 cos β 0 ⎦ ⎣ z ⎦ .
1 0 0 0 1 1

```

Note that the matrix terms do not appear to share the symmetry seen in the previous
two matrices. Nothing really has gone wrong, it is just the way the axes are paired
together to rotate the coordinates.
The above rotations are also known as yaw, pitch and roll, and great care should
be taken with these angles when referring to other books and technical papers. Sometimes a left-handed system of axes is used rather than a right-handed set, and the
vertical axis may be the y-axis or the z-axis. Consequently, the matrices representing
the rotations can vary greatly. In this chapter all Cartesian coordinate systems are
right-handed, and the vertical axis is always the y-axis.
I will define the roll, pitch and yaw angles as follows:
• r oll is the angle of rotation about the z-axis,
• pitch is the angle of rotation about the x-axis,
• yaw is the angle of rotation about the y-axis.
Figure 10.9 illustrates these rotations and the sign convention. The homogeneous
matrices representing these rotations are as follows:
• rotate r oll about the z-axis:

<a id='p215'></a>
<!-- Página 215 -->

198 10 Geometric Transforms

Fig. 10.9 The convention Y
for r oll, pitch and yaw
angles



```
pitch roll




Z yaw X

⎡ ⎤
cos r oll − sin r oll 0 0
⎢ sin r oll cos r oll 0 0 ⎥
⎢ ⎥.
⎣ 0 0 1 0⎦
0 0 01

```

• rotate pitch about the x-axis:
```
⎡ ⎤
1 0 0 0
⎢ 0 cos pitch − sin pitch 0 ⎥
⎢ ⎥
⎣ 0 sin pitch cos pitch 0 ⎦ .
0 0 0 1

```

• rotate yaw about the y-axis:
```
⎡ ⎤
cos yaw 0 sin yaw 0
⎢ 0 1 0 0⎥
⎢ ⎥
⎣ − sin yaw 0 cos yaw 0 ⎦ .
0 0 0 1

```

A common sequence for applying these rotations is r oll, pitch, yaw, as seen in
the following transform:
```
⎡ ⎤ ⎡ ⎤
x x
⎢ y ⎥    ⎢y⎥
⎢  ⎥ = yaw pitch r oll ⎢ ⎥
⎣z ⎦ ⎣z⎦
1 1

```

and if a translation is involved,

<a id='p216'></a>
<!-- Página 216 -->

10.6 3D Transforms 199

Fig. 10.10 The X  Y  Z  axial
system after a pitch of 90◦




Fig. 10.11 The X  Y  Z  axial
system after a yaw of 90◦




```
⎡ ⎤ ⎡ ⎤
x x
⎢ y ⎥     ⎢y⎥
⎢  ⎥ = translate yaw pitch r oll ⎢ ⎥ .
⎣z ⎦ ⎣z⎦
1 1

```

When these rotation transforms are applied, the vertex is first rotated about the z-axis
(r oll), followed by a rotation about the x-axis ( pitch), followed by a rotation about
the y-axis (yaw). Euler rotations are relative to the fixed frame of reference. This is
not always easy to visualise as one’s attention is normally with the rotating frame of
reference. Let’s consider a simple example where an axial system is subjected to a
pitch rotation followed by a yaw rotation relative to fixed frame of reference.
```
We begin with two frames of reference X Y Z and X  Y  Z  mutually aligned. Figure
```

10.10 shows the orientation of X  Y  Z  after it is subjected to a pitch of 90◦ about
the X -axis. And Fig. 10.11 shows the final orientation after X  Y  Z  is subjected to a
yaw of 90◦ about the Y -axis.



10.6.4 Gimbal Lock

Let’s take another example starting from the point where the two axial systems are
mutually aligned. Figure 10.12 shows the orientation of X  Y  Z  after it is subjected

<a id='p217'></a>
<!-- Página 217 -->

200 10 Geometric Transforms

Fig. 10.12 The X  Y  Z  axial
system after a r oll of 45◦




Fig. 10.13 The X  Y  Z  axial
system after a pitch of 90◦




to a roll of 45◦ about the Z -axis, and Fig. 10.13 shows the orientation of X  Y  Z  after
it is subjected to a pitch of 90◦ about the X -axis. Now the interesting thing about
this orientation is that if we now performed a yaw of 45◦ about the Y -axis, it would
rotate the X  -axis towards the X -axis, counteracting the effect of the original roll.
Yaw has become a negative roll rotation, caused by the 90◦ pitch. This situation is
known as gimbal lock, because one degree of rotational freedom has been lost. Quite
innocently, we have stumbled across one of the major weaknesses of Euler angles:
under certain conditions it is only possible to rotate an object about two axes. One
way of preventing this is to create a secondary set of axes constructed from three
orthogonal vectors that are also rotated alongside an object or virtual camera. But
instead of making the rotations relative to the fixed frame of reference, the roll, pitch
and yaw rotations are relative to the rotating frame of reference.



10.6.5 Rotating About an Axis

The above rotations were relative to the x-, y-, z-axis. Now let’s consider rotations
about an axis parallel to one of these axes. To begin with, we will rotate about an axis
parallel with the z-axis, as shown in Fig. 10.14. The scenario is very reminiscent of
the 2D case for rotating a point about an arbitrary point, and the general transform
is given by

<a id='p218'></a>
<!-- Página 218 -->

10.6 3D Transforms 201

Fig. 10.14 Rotating a point
about an axis parallel with
the x-axis




⎡ ⎤ ⎡ ⎤
```
x x
```

⎢ y ⎥    ⎢ ⎥
⎢  ⎥ = translate( px , p y , 0) rotateβ translate(− px , − p y , 0) ⎢ y ⎥
⎣z ⎦ ⎣z⎦
```
1 1

```

and the matrix is
```
⎡ ⎤ ⎡ ⎤⎡ ⎤
x cos β − sin β 0 px (1 − cos β) + p y sin β x
⎢ y  ⎥ ⎢ sin β cos β 0 p y (1 − cos β) − px sin β ⎥ ⎢ y ⎥
⎢ ⎥=⎢ ⎥⎢ ⎥.
⎣z ⎦ ⎣ 0 0 1 0 ⎦⎣ z ⎦
1 0 0 0 1 1

```

I hope you can see the similarity between rotating in 3D and 2D: the x- and ycoordinates are updated while the z-coordinate is held constant. We can now state
the other two matrices for rotating about an axis parallel with the x-axis and parallel
with the y-axis:
• rotating about an axis parallel with the x-axis:

```
⎡ ⎤ ⎡ ⎤⎡ ⎤
x 1 0 0 0 x
⎢ y  ⎥ ⎢ 0 cos β − sin β p y (1 − cos β) + pz sin β ⎥ ⎢ y ⎥
⎢ ⎥=⎢ ⎥⎢ ⎥
⎣ z ⎦ ⎣ 0 sin β cos β pz (1 − cos β) − p y sin β ⎦ ⎣ z ⎦ .
1 0 0 0 1 1

```

• rotating about an axis parallel with the y-axis:

```
⎡ ⎤ ⎡ ⎤⎡ ⎤
x cos β 0 sin β px (1 − cos β) − pz sin β x
⎢ y ⎥ ⎢ 0 1 0 0 ⎥⎢y⎥
⎢ ⎥=⎢ ⎥⎢ ⎥
⎣ z ⎦ ⎣ − sin β 0 cos β pz (1 − cos β) + px sin β ⎦ ⎣ z ⎦ .
1 0 0 0 1 1
```


<a id='p219'></a>
<!-- Página 219 -->

202 10 Geometric Transforms

10.6.6 3D Reflections

Reflections in 3D occur with respect to a plane, rather than an axis. The matrix giving
the reflection relative to the yz-plane is
```
⎡ ⎤ ⎡ ⎤⎡ ⎤
x −1 0 0 0 x
⎢ y ⎥ ⎢ 0 1 0 0 ⎥ ⎢ y ⎥
⎢ ⎥=⎢ ⎥⎢ ⎥
⎣ z ⎦ ⎣ 0 0 1 0⎦⎣ z ⎦
1 0001 1

```

and the reflection relative to a plane parallel to, and ax units from the yz-plane is
```
⎡ ⎤ ⎡ ⎤⎡ ⎤
x −1 0 0 2ax x
⎢ y ⎥ ⎢ 0 1 0 0 ⎥ ⎢ y ⎥
⎢ ⎥=⎢ ⎥⎢ ⎥
⎣ z ⎦ ⎣ 0 0 1 0 ⎦⎣ z ⎦.
1 000 1 1

```

It is left to the reader to develop similar matrices for the other major axial planes.



10.7 Change of Axes

Points in one coordinate system often have to be referenced in another one. For
example, to view a 3D scene from an arbitrary position, a virtual camera is positioned
in the world space using a series of transforms. An object’s coordinates, which are
relative to the world frame of reference, are computed relative to the camera’s axial
system, and then used to develop a perspective projection. Before explaining how
this is achieved in 3D, let’s examine the simple case of changing axial systems in
two dimensions.



10.7.1 2D Change of Axes

Figure 10.15 shows a point P(x, y) relative to the X Y -axes, but we require to know
the coordinates relative to the X  Y  -axes. To do this, we need to know the relationship
between the two coordinate systems, and ideally we want to apply a technique that
works in 2D and 3D. If the second coordinate system is a simple translation (tx , t y )
relative to the reference system, as shown in Fig. 10.15, the point P(x, y) has
coordinates relative to the translated system (x − tx , y − t y ) :

<a id='p220'></a>
<!-- Página 220 -->

10.7 Change of Axes 203

Fig. 10.15 The X  Y  axial
system is translated (tx , t y )




Fig. 10.16 The X  Y  axial
system is rotated β




```
⎡ ⎤ ⎡ ⎤⎡ ⎤
x 1 0 −tx x
⎣ y  ⎦ = ⎣ 0 1 −t y ⎦ ⎣ y ⎦ .
1 00 1 1

```

If the X  Y  -axes are rotated β relative to the X Y -axes, as shown in Fig. 10.16,
a point P(x, y) relative to the X Y -axes becomes P  (x  , y  ) relative to the rotated
axes is given by ⎡ ⎤ ⎡ ⎤⎡ ⎤
```
x cos(−β) − sin(−β) 0 x
⎣ y  ⎦ = ⎣ sin(−β) cos(−β) 0 ⎦ ⎣ y ⎦
1 0 0 1 1

```

which simplifies to ⎡ ⎤ ⎡ ⎤⎡ ⎤
```
x cos β sin β 0 x
⎣ y  ⎦ = ⎣ − sin β cos β 0 ⎦ ⎣ y ⎦ .
1 0 0 1 1

```

When a coordinate system is rotated and translated relative to the reference system,
a point P(x, y) becomes P  (x  , y  ) relative to the new axes given by

<a id='p221'></a>
<!-- Página 221 -->

204 10 Geometric Transforms

Fig. 10.17 If the X  - and
Y  -axes are assumed to be
unit vectors, their direction
cosines form the elements of
the rotation matrix




```
⎡ ⎤ ⎡ ⎤⎡ ⎤⎡ ⎤
x cos β sin β 0 1 0 −tx x
⎣ y  ⎦ = ⎣ − sin β cos β 0 ⎦ ⎣ 0 1 −t y ⎦ ⎣ y ⎦
1 0 0 1 00 1 1

```

which simplifies to
```
⎡ ⎤ ⎡ ⎤⎡ ⎤
x cos β sin β −tx cos β − t y sin β x
⎣ y  ⎦ = ⎣ − sin β cos β tx sin β − t y cos β ⎦ ⎣ y ⎦ .
1 0 0 1 1



```

10.7.2 Direction Cosines

Direction cosines are the cosines of the angles between a vector and the Cartesian
axes, and for unit vectors they are the vector’s components. Figure 10.17 shows two
unit vectors X  and Y  , and by inspection the direction cosines for X  are cos β and
cos(90◦ − β), which can be rewritten as cos β and sin β, and the direction cosines
for Y  are cos(90◦ + β) and cos β, which can be rewritten as − sin β and cos β. But
these direction cosines cos β, sin β, − sin β and cos β are the four elements of the
rotation matrix used above  
```
cos β sin β
.
− sin β cos β

```

The top row contains the direction cosines for the X  -axis and the bottom row contains
the direction cosines for the Y  -axis. This relationship also holds in 3D.
As an example, let’s evaluate a simple 2D case where a set of axes is rotated 45◦
as shown in Fig. 10.18. The appropriate transform is

<a id='p222'></a>
<!-- Página 222 -->

10.7 Change of Axes 205

Fig. 10.18 The vertices of a
unit square relative to the
two axial systems




```
⎡ ⎤ ⎡ ⎤⎡ ⎤
x cos 45◦ sin 45◦ 0 x
⎣ y  ⎦ = ⎣ − sin 45◦ cos 45◦ 0 ⎦ ⎣ y ⎦
1 0 0 1 1
⎡ ⎤⎡ ⎤
0.707 0.707 0 x
≈ ⎣ −0.707 0.707 0 ⎦ ⎣ y ⎦ .
0 0 1 1

```

The four vertices on a unit square become

```
(0, 0) → (0, 0)
(1, 0) → (0.707, −0.707)
(1, 1) → (1.1414, 0)
(0, 1) → (0.707, 0.707)

```

which by inspection of Fig. 10.18 are correct.



10.7.3 3D Change of Axes

The ability to reference a collection of coordinates is fundamental in computer graphics, especially in 3D. And rather than investigate them within this section, let’s delay
their analysis for the next section, where we see how the technique is used for relating
an object’s coordinates relative to an arbitrary virtual camera.



10.8 Positioning the Virtual Camera

Four coordinate systems are used in the computer graphics pipeline: object space,
world space, camera space and image space.

<a id='p223'></a>
<!-- Página 223 -->

206 10 Geometric Transforms

• The object space is a domain where objects are modelled and assembled.
• The world space is where objects are positioned and animated through appropriate
transforms. The world space also hosts a virtual camera or observer.
• The camera space is a transform of the world space relative to the camera.
• Finally, the image space is a projection—normally perspective—of the camera
space onto an image plane.
The transforms considered so far are used to manipulate and position objects
within the world space. What we will consider next is how a virtual camera or observer
is positioned in world space, and the process of converting world coordinates to
camera coordinates. The procedure used generally depends on the method employed
to define the camera’s frame of reference within the world space, which may involve
the use of direction cosines, Euler angles or quaternions.



10.8.1 Direction Cosines

A 3D unit vector has three components [x y z]T , which are equal to the cosines
of the angles formed between the vector and the three orthogonal axes. These angles
are known as direction cosines and can be computed taking the dot product of the
vector and the Cartesian unit vectors. Figure 10.19 shows the direction cosines and
the angles. These direction cosines enable any point P(x, y, z) in one frame of
reference to be transformed into P  (x  , y  , z  ) in another frame of reference as
follows: ⎡ ⎤ ⎡ ⎤⎡ ⎤
```
x r11 r12 r13 0 x
⎢ y  ⎥ ⎢ r21 r22 r23 0 ⎥ ⎢ y ⎥
⎢ ⎥=⎢ ⎥⎢ ⎥
⎣ z ⎦ ⎣ r31 r32 r33 0 ⎦ ⎣ z ⎦
1 0 0 0 1 1

```

where:
• r11 , r12 , r13 are the direction cosines of the secondary x-axis,
• r21 , r22 , r23 are the direction cosines of the secondary y-axis,


Fig. 10.19 The components
of a unit vector are equal to
the cosines of the angles
between the vector and the
axes

<a id='p224'></a>
<!-- Página 224 -->

10.8 Positioning the Virtual Camera 207

Fig. 10.20 Two axial Y
systems mutually aligned





## Z X


Fig. 10.21 The X  Y  Z  axial Y
system after a roll of 90◦





## Z X




• r31 , r32 , r33 are the direction cosines of the secondary z-axis.
To illustrate this operation, consider the scenario shown in Fig. 10.20 with two
axial systems mutually aligned. Evaluating the direction cosines results in the following matrix transformation:
```
⎡ ⎤ ⎡ ⎤⎡ ⎤
x 1000 x
⎢ y ⎥ ⎢ 0 1 0 0 ⎥ ⎢ y ⎥
⎢ ⎥=⎢ ⎥⎢ ⎥
⎣ z ⎦ ⎣0 0 1 0⎦⎣ z ⎦
1 0001 1

```

which is the identity matrix and implies that (x  , y  , z  ) = (x, y, z) .
Figure 10.21 shows another scenario where the axes are rolled 90◦ , and the associated transform is ⎡ ⎤ ⎡ ⎤⎡ ⎤
```
x 0100 x
⎢ y  ⎥ ⎢ −1 0 0 0 ⎥ ⎢ y ⎥
⎢ ⎥=⎢ ⎥⎢ ⎥
⎣ z ⎦ ⎣ 0 0 1 0⎦⎣ z ⎦.
1 0001 1

```

Substituting (1, 1, 0) for (x, y, z) produces (1, −1, 0) for (x  , y  , z  ) in the new
frame of reference, which by inspection, is correct.
```
If the virtual camera is offset by (tx , t y , tz ) the transform relating points in world
```

space to camera space is expressed as a compound operation consisting of a translation back to the origin, followed by a change of axial systems. This is expressed
as

<a id='p225'></a>
<!-- Página 225 -->

208 10 Geometric Transforms

Fig. 10.22 The secondary
axial system is subject to a Y
yaw of 180◦ and an offset of
(10, 1, 1)

```
, 0)
1) (10, 0
(0, 1,


(0, 0,
0) (10, 1, 1)
(10, -
1, 1)

```


## Z X



```
⎡ ⎤ ⎡ ⎤⎡ ⎤⎡ ⎤
x r11 r12 r13 0 1 0 0 −tx x
⎢ y  ⎥ ⎢ r21 r22 r23 0 ⎥ ⎢ 0 1 0 −t y ⎥ ⎢ y ⎥
⎢ ⎥=⎢ ⎥⎢ ⎥⎢ ⎥
⎣ z ⎦ ⎣ r31 r32 r33 0 ⎦ ⎣ 0 0 1 −tz ⎦ ⎣ z ⎦ .
1 0 0 0 1 000 1 1

```

To illustrate this, consider the scenario shown in Fig. 10.22. The values of (tx , t y , tz )
are (10, 1, 1), and the direction cosines are as shown in the following matrix operation: ⎡ ⎤ ⎡ ⎤⎡ ⎤⎡ ⎤
```
x −1 0 0 0 1 0 0 −10 x
⎢ y  ⎥ ⎢ 0 1 0 0 ⎥ ⎢ 0 1 0 −1 ⎥ ⎢ y ⎥
⎢ ⎥=⎢ ⎥⎢ ⎥⎢ ⎥
⎣ z ⎦ ⎣ 0 0 −1 0 ⎦ ⎣ 0 0 1 −1 ⎦ ⎣ z ⎦
1 00 01 000 1 1

```

which simplifies to ⎡ ⎤ ⎡ ⎤⎡ ⎤
```
x −1 0 0 10 x
⎢ y  ⎥ ⎢ 0 1 0 −1 ⎥ ⎢ y ⎥
⎢ ⎥=⎢ ⎥⎢ ⎥
⎣ z ⎦ ⎣ 0 0 −1 1 ⎦ ⎣ z ⎦ .
1 00 0 1 1

```

Substituting (0, 0, 0) for (x, y, z) in the above transform produces (10, −1, 1)
for (x  , y  , z  ), which can be confirmed from Fig. 10.22. Similarly, substituting
(0, 1, 1) for (x, y, z) produces (10, 0, 0) for (x  , y  , z  ), which is also correct.



10.8.2 Euler Angles

Another approach for locating the virtual camera involves Euler angles, but we must
remember that they suffer from gimbal lock. However, if the virtual camera is located
in world space using Euler angles, the transform relating world coordinates to camera coordinates can be derived from the inverse operations. The yaw, pitch, r oll
matrices described above are called orthogonal matrices, as the inverse matrix is the

<a id='p226'></a>
<!-- Página 226 -->

10.8 Positioning the Virtual Camera 209

transpose of the original rows and columns. Consequently, to rotate through angles
−r oll, − pitch and −yaw, we use
• rotate −r oll about the z-axis:
```
⎡ ⎤
cos r oll sin r oll 0 0
⎢ − sin r oll cos r oll 0 0 ⎥
⎢ ⎥.
⎣ 0 0 1 0⎦
0 0 01

```

• rotate − pitch about the x-axis:
```
⎡ ⎤
1 0 0 0
⎢ 0 cos pitch sin pitch 0 ⎥
⎢ ⎥
⎣ 0 − sin pitch cos pitch 0 ⎦ .
0 0 0 1

```

• rotate −yaw about the y-axis:
```
⎡ ⎤
cos yaw 0 − sin yaw 0
⎢
⎢ 0 1 0 0⎥⎥
⎣ sin yaw 0 cos yaw 0 ⎦ .
0 0 0 1

```

The same result is obtained by substituting −r oll, − pitch, −yaw in the original
matrices. As described above, the virtual camera will normally be translated from
the origin by (tx , t y , tz ), which implies that the transform from the world space to
the camera space must be evaluated as follows:
```
⎡ ⎤ ⎡ ⎤
x x
⎢ y ⎥     ⎢y⎥
⎢  ⎥ = −r oll − pitch −yaw translate(−tx , −t y , −tz ) ⎢ ⎥
⎣z ⎦ ⎣z⎦
1 1

```

which is represented by a single homogeneous matrix:
```
⎡ ⎤ ⎡ ⎤⎡ ⎤
x T11 T12 T13 T14 x
⎢ y  ⎥ ⎢ T21 T22 T23 T24 ⎥ ⎢ y ⎥
⎢ ⎥=⎢ ⎥⎢ ⎥
⎣ z ⎦ ⎣ T31 T32 T33 T34 ⎦ ⎣ z ⎦
```


## 1 T41 T42 T43 T44 1


<a id='p227'></a>
<!-- Página 227 -->

210 10 Geometric Transforms

where

```
T11 = cos(yaw) cos(r oll) + sin(yaw) sin( pitch) sin(r oll)
T12 = cos( pitch) sin(r oll)
T13 = − sin(yaw) cos(r oll) + cos(yaw) sin( pitch) sin(r oll)
 
T14 = − tx T11 + t y T12 + tz T13
T21 = − cos(yaw) sin(r oll) + sin(yaw) sin( pitch) cos(r oll)
T22 = cos( pitch) cos(r oll)
T23 = − sin(yaw) sin(r oll) + cos(yaw) sin( pitch) cos(r oll)
 
T24 = − tx T21 + t y T22 + tz T23
T31 = sin(yaw) cos( pitch)
T32 = − sin( pitch)
T33 = cos(yaw) cos( pitch)
 
T34 = − tx T31 + t y T32 + tz T33
```


## T41 = T42 = T43 = 0


## T44 = 1.


For example, consider the scenario shown in Fig. 10.22 where the following
conditions prevail:

```
r oll = 0◦
pitch = 0◦
yaw = 180◦
tx = 10
ty = 1
tz = 1.

```

The transform is ⎡ ⎤ ⎡ ⎤⎡ ⎤
```
x −1 0 0 10 x
⎢ y  ⎥ ⎢ 0 1 0 −1 ⎥ ⎢ y ⎥
⎢ ⎥=⎢ ⎥⎢ ⎥
⎣ z ⎦ ⎣ 0 0 −1 1 ⎦ ⎣ z ⎦
1 00 0 1 1

```

which is identical to the equation used for direction cosines.
Another scenario is shown in Fig. 10.23 where the following conditions prevail:

<a id='p228'></a>
<!-- Página 228 -->

10.8 Positioning the Virtual Camera 211

Fig. 10.23 The secondary

## Y

axial system is subject to a
roll of 90◦ , a pitch of 180◦
and a translation of
(0.5, 0.5, 11)
```
(1, 1, 1)

(0.5, 0.5, 11)


```


## X


## Z




```
r oll = 90◦
pitch = 180◦
yaw = 0◦
tx = 0.5
t y = 0.5
tz = 11.

```

The transform is ⎡ ⎤ ⎡ ⎤⎡ ⎤
```
x 0 −1 0 0.5 x
⎢ y  ⎥ ⎢ −1 0 0 0.5 ⎥ ⎢ y ⎥
⎢ ⎥=⎢ ⎥⎢ ⎥
⎣ z ⎦ ⎣ 0 0 −1 11 ⎦ ⎣ z ⎦ .
1 0 0 0 1 1

```

Substituting (1, 1, 1) for (x, y, z) produces (−0.5, −0.5, 10) for (x  , y  , z  ).
Similarly, substituting (0, 0, 1) for (x, y, z) produces (0.5, 0.5, 10) for
(x  , y  , z  ), which can be visually verified from Fig. 10.23.



10.9 Rotating a Point About an Arbitrary Axis

10.9.1 Matrices

Let’s consider two ways of developing a matrix for rotating a point about an arbitrary
axis. The first approach employs vector analysis and is quite succinct. The second
technique is less analytical and relies on matrices and trigonometric evaluation and
is rather laborious. Fortunately, they both arrive at the same result!
```
Figure 10.24 shows a view of the geometry associated with the task at hand. For
```

clarification, Fig. 10.25 shows a cross-section and a plan view of the geometry.

<a id='p229'></a>
<!-- Página 229 -->

212 10 Geometric Transforms

Fig. 10.24 A view of the
geometry associated with P
rotating a point about an
arbitrary axis n̂ r
```
α P p
N Q p
n
θ
```


## O


Fig. 10.25 A cross-section n̂
and plan view of the
geometry associated with P
rotating a point about an r P
arbitrary axis N |r|
```
n p
α r
```


## P


## N Q



```
θ


```


## O



The axis of rotation is given by the unit vector:

```
n̂ = ai + bj + ck.

P(x p , y p , z p ) is the point to be rotated by angle α to P  (x p , y p , z p ).

```

O is the origin, whilst p and p are position vectors for P and P  respectively.
From Figs. 10.24 and 10.25:

```
−−→ −−→ −−→
p = O N + N Q + Q P  .
−−→
```

To find O N :

```
n = p cos θ = n̂ · p

```

therefore,
```
−−→
O N = n = n̂(n̂ · p).
−−→
```

To find N Q:

## −−→ NQ NQ

```
NQ = r= r = cos α r
```


## NP N P


<a id='p230'></a>
<!-- Página 230 -->

10.9 Rotating a Point About an Arbitrary Axis 213

but
```
p = n + r = n̂(n̂ · p) + r

```

therefore,
```
r = p − n̂(n̂ · p)

```

and
```
−−→
N Q = [p − n̂(n̂ · p)] cos α.
−−→
```

To find Q P  :
Let
```
n̂ × p = w

```

where
```
w = n̂p sin θ = p sin θ

```

but
```
r = p sin θ

```

therefore,
```
w = r.

```

Now

## Q P Q P Q P

```

= = = sin α
NP r w

```

therefore,
```
−−→
Q P = w sin α = (n̂ × p) sin α

```

then
```
p = n̂(n̂ · p) + [p − n̂(n̂ · p] cos α + (n̂ × p) sin α

```

and
```
p = p cos α + n̂(n̂ · p)(1 − cos α) + (n̂ × p) sin α.

```

Let
```
K = 1 − cos α

```

then
```
p = p cos α + n̂(n̂ · p)K + (n̂ × p) sin α

```

and

<a id='p231'></a>
<!-- Página 231 -->

214 10 Geometric Transforms

```
p = (x p i + y p j + z p k) cos α + (ai + bj + ck)(ax p + by p + cz p )K
+ [(bz p − cy p )i + (cx p − az p )j + (ay p − bx p )k] sin α
= [x p cos α + a(ax p + by p + cz p )K + (bz p − cy p ) sin α]i
+ [y p cos α + b(ax p + by p + cz p )K + (cx p − az p ) sin α]j
+ [z p cos α + c(ax p + by p + cz p )K + (ay p − bx p ) sin α]k
   
= x p a 2 K + cos α + y p (abK − c sin α) + z p (acK + b sin α) i
   
+ x p (abK + c sin α) + y p b2 K + cos α + z p (bcK − a sin α) j
  
+ x p (acK − b sin α) + y p (bcK + a sin α) + z p c2 K + cos α k

```

and the transform is:
```
⎡  ⎤ ⎡ 2 ⎤⎡ ⎤
xp a K + cos α abK − c sin α acK + b sin α 0 xp
⎢ y p ⎥ ⎢ abK + c sin α b2 K + cos α bcK − a sin α 0 ⎥ ⎢ y p ⎥
⎢ ⎥=⎢ ⎥⎢ ⎥
⎣ z p ⎦ ⎣ acK − b sin α bcK + a sin α c2 K + cos α 0 ⎦ ⎣ z p ⎦
1 0 0 0 1 1

```

where
```
K = 1 − cos α.

Now let’s approach the problem using transforms and trigonometric identities.
```

The following is extremely tedious, but it is a good exercise for improving one’s
algebraic skills!
```
Figure 10.26 shows a point P(x, y, z) to be rotated through an angle α to
```

P  (x  , y  , z  ) about an axis defined by

```
v = ai + bj + ck

```

where v = 1.
The transforms to achieve this operation is expressed as follows:


Fig. 10.26 The geometry

## Y

associated with rotating a
point about an arbitrary axis b
```
α
v
```


## P

```
θ
c φ a

```


## Z X


<a id='p232'></a>
<!-- Página 232 -->

10.9 Rotating a Point About an Arbitrary Axis 215
```
⎡ ⎤ ⎡ ⎤
x x
⎣ y  ⎦ = [T5 ] [T4 ] [T3 ] [T2 ] [T1 ] ⎣ y ⎦
z z

```

which aligns the axis of rotation with the x-axis, performs the rotation of P through
an angle α about the x-axis, and returns the axis of rotation back to its original
position. Therefore,

```
T1 rotates + φ about the y-axis
T2 rotates − θ about the z-axis
T3 rotates + α about the x-axis
T4 rotates + θ about the z-axis
T5 rotates − φ about the y-axis

```

where
```
⎡ ⎤ ⎡ ⎤
cos φ 0 sin φ cos θ sin θ 0
T1 = ⎣ 0 1 0 ⎦ , T2 = ⎣ − sin θ cos θ 0 ⎦
− sin φ 0 cos φ 0 0 1
⎡ ⎤ ⎡ ⎤
1 0 0 cos θ − sin θ 0
T3 = ⎣ 0 cos α − sin α ⎦ , T4 = ⎣ sin θ cos θ 0 ⎦
0 sin α cos α 0 0 1
⎡ ⎤
cos φ 0 − sin φ
```


## T5 = ⎣ 0 1 0 ⎦.

```
sin φ 0 cos φ

```

Let ⎡ ⎤

## E 11 E 12 E 13 0


## ⎢ E 21 E 22 E 23 0 ⎥


## [T5 ] [T4 ] [T3 ] [T2 ] [T1 ] = ⎢ ⎥


## ⎣ E 31 E 32 E 33 0 ⎦

```
0 0 0 1

```

where by multiplying the matrices together we find that:

<a id='p233'></a>
<!-- Página 233 -->

216 10 Geometric Transforms

```
E 11 = cos2 φ cos2 θ + cos2 φ sin2 θ cos α + sin2 φ cos α
E 12 = cos φ cos θ sin θ − cos φ sin θ cos θ cos α − sin φ cos θ sin α
E 13 = cos φ sin φ cos2 θ + cos φ sin φ sin2 θ cos α + sin2 φ sin θ sin α
+ cos2 φ sin θ sin α − cos φ sin φ cos α
E 21 = sin θ cos θ cos φ − cos θ sin θ cos φ cos α + cos θ sin φ sin α
E 22 = sin2 θ + cos2 θ cos α
E 23 = sin θ cos θ sin φ − cos θ sin θ sin φ cos α − cos θ cos φ sin α
E 31 = cos φ sin φ cos2 θ + cos φ sin φ sin2 θ cos α − cos2 φ sin θ sin α
= − cos φ sin φ cos α
E 32 = sin φ cos θ sin θ − sin φ sin θ cos θ cos α + cos φ cos θ sin α
E 33 = sin2 φ cos2 θ + sin2 φ sin2 θ cos α − cos φ sin φ sin θ sin α
+ cos φ sin φ sin θ sin α + cos2 φ cos α.

```

From Fig. 10.26 we compute the sin and cos of θ and φ in terms of a, b and c, and
then compute their equivalent sin2 and cos2 values:
```

cos θ = 1 − b2 ⇒ cos2 θ = 1 − b2
sin θ = b ⇒ sin2 θ = b2
a a2
cos φ = √ ⇒ cos2 φ =
1 − b2 1 − b2
c c2
sin φ = √ ⇒ sin2 φ = .
1 − b2 1 − b2

```

To find E 11 :

```
E 11 = cos2 φ cos2 θ + cos2 φ sin2 θ cos α + sin2 φ cos α
a2 a2 c2
= (1 − b2 ) + b2 cos α + cos α
1−b 2 1−b 2 1 − b2
a 2 b2 c2
= a2 + cos α + cos α
1 − b2 1 − b2
 2 
c + a 2 b2
= a2 + cos α
1 − b2

```

but
```
a 2 + b2 + c2 = 1 ⇒ c2 = 1 − a 2 − b2

```

substituting c2 in E 11

<a id='p234'></a>
<!-- Página 234 -->

10.9 Rotating a Point About an Arbitrary Axis 217
```
 
1 − a 2 − b2 + a 2 b2
E 11 = a +
2
cos α
1 − b2
 
(1 − a 2 )(1 − b2 )
= a2 + cos α
1 − b2
= a 2 + (1 − a 2 ) cos α
= a 2 (1 − cos α) + cos α.

```

Let
```
K = 1 − cos α

```

then
```
E 11 = a 2 K + cos α.

```

To find E 12 :

E 12 = cos φ cos θ sin θ − cos φ sin θ cos θ cos α − sin φ cos θ sin α
```
a  a  c 
=√ 1 − b2 b − √ b 1 − b2 cos α − √ 1 − b2 sin α
1 − b2 1 − b2 1 − b2
= ab − ab cos α − c sin α
= ab(1 − cos α) − c sin α
```

E 12 = abK − c sin α.

To find E 13 :

E 13 = cos φ sin φ cos2 θ + cos φ sin φ sin2 θ cos α + sin2 φ sin θ sin α
```
+ cos2 φ sin θ sin α − cos φ sin φ cos α
= cos φ sin φ cos2 θ + cos φ sin φ sin2 θ cos α + sin θ sin α − cos φ sin φ cos α
a c a c
=√ √ (1 − b2 ) + √ √ b2 cos α + b sin α
1−b 2 1−b 2 1−b 2 1 − b2
a c
−√ √ cos α
1−b 2 1 − b2
b2 ac
= ac + ac cos α + b sin α − cos α
(1 − b )
2 (1 − b2 )
(b2 − 1)
= ac + ac cos α + b sin α
(1 − b2 )
= ac(1 − cos α) + b sin α
```

E 13 = acK + b sin α.

Using similar algebraic methods, we discover that:

<a id='p235'></a>
<!-- Página 235 -->

218 10 Geometric Transforms

```
E 21 = abK + c sin α
E 22 = b2 K + cos α
E 23 = bcK − a sin α
E 31 = acK − b sin α
E 32 = bcK + a sin α
E 33 = c2 K + cos α

```

and our original matrix transform becomes:
```
⎡ ⎤ ⎡ 2 ⎤⎡ ⎤
x p a K + cos α abK − c sin α acK + b sin α 0 xp
⎢ y p ⎥ ⎢ abK + c sin α b2 K + cos α bcK − a sin α 0 ⎥ ⎢ y p ⎥
⎢ ⎥=⎢ ⎥ ⎢ ⎥
⎣ z p ⎦ ⎣ acK − b sin α bcK + a sin α c2 K + cos α 0 ⎦ ⎣ z p ⎦
1 0 0 0 1 1

```

where
```
K = 1 − cos α.

```

which is identical to the transformation derived from the first approach. Now let’s
test the matrix with a simple example that can be easily verified. We do this by
rotating a point P(10, 5, 0), about an arbitrary axis v = i + j + k, through 360◦ ,
which should return it to itself producing P(10, 5, 0).
Therefore,
```
α = 360◦ , cos α = 1, sin α = 0, K = 0

a = 1, b = 1, c = 1

```

and ⎡ ⎤ ⎡ ⎤⎡ ⎤
```
10 1000 10
⎢ 5 ⎥ ⎢0 1 0 0⎥⎢ 5 ⎥
⎢ ⎥=⎢ ⎥⎢ ⎥
⎣ 0 ⎦ ⎣0 0 1 0⎦⎣ 0 ⎦.
1 0001 1

```

As the matrix is an identity matrix P  = P.



10.10 Transforming Vectors

The transforms described in this chapter have been used to transform single points.
However, a geometric database will not only contain pure vertices, but vectors, which
must also be subject to any prevailing transform. A generic transform Q of a 3D point
is represented by

<a id='p236'></a>
<!-- Página 236 -->

10.10 Transforming Vectors 219
```
⎡ ⎤ ⎡ ⎤
x x
⎢ y ⎥   ⎢ y ⎥
```


## ⎢ ⎥= Q ⎢ ⎥

```
⎣z ⎦ ⎣z⎦
1 1

```

and as a vector is defined by two points we can write
```
⎡ ⎤ ⎡ ⎤
x x2 − x1
⎢ y  ⎥   ⎢ y2 − y1 ⎥
```


## ⎢ ⎥= Q ⎢ ⎥

```
⎣z ⎦ ⎣ z2 − z1 ⎦
1 1−1

```

where we see the homogeneous scaling term collapse to zero; which implies that any
vector [x y z]T can be transformed using
```
⎡ ⎤ ⎡ ⎤
x x
⎢ y ⎥   ⎢ y ⎥
```


## ⎢ ⎥= Q ⎢ ⎥

```
⎣z ⎦ ⎣z⎦
0 0

```

Let’s put this to the test by using a transform from an earlier example. The problem concerned a change of axial system where a virtual camera was subject to the
following:

```
r oll = 90◦
pitch = 180◦
yaw = 90◦
tx = 2
ty = 2
tz = 0

```

and the transform is
```
⎡ ⎤ ⎡ ⎤⎡ ⎤
x 0 −1 0 2 x
⎢ y ⎥ ⎢ 0 0 1 0 ⎥ ⎢ y ⎥
⎢ ⎥=⎢ ⎥⎢ ⎥
⎣ z ⎦ ⎣ −1 0 0 2 ⎦ ⎣ z ⎦ .
1 0 001 1

```

The point (1, 1, 0) is transformed to (1, 0, 1), as shown in Fig. 10.27. And the
vector [1 1 0]T is transformed to [−1 0 − 1]T , using the following transform

<a id='p237'></a>
<!-- Página 237 -->

220 10 Geometric Transforms

Fig. 10.27 Vector

## Y

[1 1 0]T is transformed to

## [−1 0 − 1]T

```
(2,2,0)

(1,1,0)
[1 1 0]
[-1 0 -1]



```


## Z X



```
⎡ ⎤ ⎡ ⎤⎡ ⎤
−1 0 −1 0 2 1
⎢ 0⎥ ⎢ 0 0 1 0⎥⎢1⎥
⎢ ⎥ ⎢ ⎥⎢ ⎥
⎣ −1 ⎦ = ⎣ −1 0 0 2 ⎦ ⎣ 0 ⎦
0 0 001 0

```

which is correct with reference to Fig. 10.27.



10.11 Determinants

Before concluding this chapter, I would like to expand upon the role of the determinant in transforms.
```
In Chap. 6 we saw that determinants arise in the solution of linear equations. Now
```

let’s investigate their graphical significance. Consider the transform:
```
    
x ab x
= .
y cd y

```

The determinant of the transform is ad − cb. If we subject the vertices of a unitsquare to this transform, we create the situation shown in Fig. 10.28. The vertices of
the unit-square are transformed as follows:

```
(0, 0) ⇒ (0, 0)
(1, 0) ⇒ (a, c)
(1, 1) ⇒ (a + b, c + d)
(0, 1) ⇒ (b, d).

```

From Fig. 10.28 it can be seen that the area of the transformed unit-square A is given
by

<a id='p238'></a>
<!-- Página 238 -->

10.11 Determinants 221

Fig. 10.28 The inner

## Y

parallelogram is the b a (a+b,c+d)
transformed unit square
```
c C D

(b,d)
d
```


## B A B

```
d (a,c)

D C c

(0,0) a b X




area = (a + b)(c + d) − 2B − 2C − 2D
= (ac + ad + cb + bd) − bd − 2cb − ac
= ad − cb

```

which is the determinant of the transform. But as the area of the original unit-square
is 1, the determinant of the transform controls the scaling factor applied to the transformed shape.
```
Let’s examine the determinants of two transforms: The first 2D transform encodes
```

a scaling of 2, and results in an overall area scaling of 4:
```
 
20
02

```

and the determinant is  
```
2 0
 
 0 2  = 4.

```

The second 2D transform encodes a scaling of 3 and a translation of (3, 3), and
results in an overall area scaling of 9:
```
⎡ ⎤
303
⎣0 3 3⎦
001

```

and the determinant is
```
     
3 3 0 3 0 3

3  
−0  
+0  = 9.
0 1 0 1 3 3

```

These two examples demonstrate the extra role played by the elements of a matrix.

<a id='p239'></a>
<!-- Página 239 -->

222 10 Geometric Transforms

10.12 Perspective Projection

Of all the projections employed in computer graphics, the perspective projection is
one most widely used. There are two stages to its computation: the first involves
converting world coordinates to the camera’s frame of reference, and the second
transforms camera coordinates to the projection plane coordinates. We have already
looked at the transforms for locating a camera in world space, and the inverse transform for converting world coordinates to the camera’s frame of reference. Let’s now
investigate how these camera coordinates are transformed into a perspective projection.
We begin by assuming that the camera is directed along the z-axis as shown in
Fig. 10.29. Positioned d units along the z-axis is a projection screen, which is used
to capture a perspective projection of an object. Figure 10.29 shows that any point
(xc , yc , z c ) is transformed to (x p , y p , d). It also shows that the screen’s x-axis is
pointing in the opposite direction to the camera’s x-axis, which can be compensated
for by reversing the sign of x p when it is computed.
Figure 10.30 shows a plan view of the scenario depicted in Figs. 10.29 and 10.31
a side view. Next, we reverse the sign of x p and state:


Fig. 10.29 The axial system
```
Yc
```

used to produce a perspective (xc,yc,zc)
view

```
xp Yp
yp
Zc


Xc Xp
d



```

Fig. 10.30 The plan view of
```
Xc (xc,yc,zc)
```

the camera’s axial system
```
screen


(xp,yp,d)
xc

xp


d Zc
zc
```


<a id='p240'></a>
<!-- Página 240 -->

10.12 Perspective Projection 223

Fig. 10.31 The side view of
```
Yc (xc,yc,zc)
```

the camera’s axial system
```
screen


(xp,yp,d)
yc

yp


d Zc
zc



xc −x p
=
zc d
−xc
xp =
z c /d

```

and
```
yc yp
=
zc d
yc
yp = .
z c /d

```

This is expressed in matrix form as
```
⎡ ⎤ ⎡ ⎤⎡ ⎤
xp −1 0 0 0 xc
⎢ y p ⎥ ⎢ 0 1 0 0 ⎥ ⎢ yc ⎥
⎢ ⎥=⎢ ⎥⎢ ⎥
⎣ z p ⎦ ⎣ 0 0 1 0 ⎦ ⎣ zc ⎦ .
w 0 0 1/d 0 1

```

At first the transform seems strange, but if we multiply this out we get

```
[x p y p z p w]T = [−xc yc z c z c /d]T

```

and if we remember the idea behind homogeneous coordinates, we must divide the
terms x p , y p , z p by w to get the scaled terms, which produces

```
−xc
xp =
z c /d
yc
yp =
z c /d
zc
zp = =d
z c /d
```


<a id='p241'></a>
<!-- Página 241 -->

224 10 Geometric Transforms

which, after all, is rather elegant. Notice that this transform takes into account the sign
change that occurs with the x-coordinate. Some algorithms delay this sign reversal
until the mapping is made to screen coordinates.


10.13 Summary

The purpose of this chapter was to introduce the reader to transforms and matrices—I
hope this has been achieved. This is not the end of the subject, as one can do so much
with matrices. For example, it would be interesting to see how a matrix behaves when
some of its elements are changed dynamically.


10.14 Worked Examples

10.14.1 2D Scaling Transform

State the 2D homogeneous matrix to scale by a factor of 2 in the x-direction and 3
in the y-direction. ⎡ ⎤ ⎡ ⎤⎡ ⎤
```
x 200 x
⎣ y ⎦ = ⎣ 0 3 0 ⎦ ⎣ y ⎦ .
1 001 1



```

10.14.2 2D Scale and Translate

Given matrix T1 which scales a 2D point by a factor of 2, and T2 which translates
a 2D point by x = 2 and y = 2, combine them in two possible ways and show that
the point (1, 1) is transformed to two different places.

```
⎡ ⎤ ⎡ ⎤⎡ ⎤
x 200 x

T1 = ⎣ y ⎦ = ⎣ 0 2 0 ⎦ ⎣ y ⎦
1 001 1
⎡ ⎤ ⎡ ⎤⎡ ⎤
x 102 x
T2 = ⎣ y  ⎦ = ⎣ 0 1 2 ⎦ ⎣ y ⎦
1 001 1
⎡ ⎤ ⎡ ⎤⎡ ⎤⎡ ⎤
x 200 102 x

T1 T2 = ⎣ y ⎦ = ⎣ 0 2 0 ⎦ ⎣ 0 1 2 ⎦ ⎣ y ⎦
1 001 001 1
⎡ ⎤⎡ ⎤
204 x
= ⎣0 2 4⎦⎣ y ⎦
001 1
```


<a id='p242'></a>
<!-- Página 242 -->

10.14 Worked Examples 225

and the point (1, 1) is transformed to (6, 6).
```
⎡ ⎤ ⎡ ⎤⎡ ⎤⎡ ⎤
x 102 200 x
T2 T1 = ⎣ y  ⎦ = ⎣ 0 1 2 ⎦ ⎣ 0 2 0 ⎦ ⎣ y ⎦
1 001 001 1
⎡ ⎤⎡ ⎤
202 x
= ⎣0 2 2⎦⎣ y ⎦
001 1

```

and the point (1, 1) is transformed to (4, 4).



10.14.3 3D Scaling Transform

Derive the 3D homogeneous matrix to scale by a factor of 2 in the x-direction, 3 in
the y-direction and 4 in the z-direction, relative to the point (1, 1, 1), and compute
the transformed position of (2, 2, 2).
```
⎡ ⎤ ⎡ ⎤⎡ ⎤
x sx 0 0 px (1 − sx ) x
⎢ y  ⎥ ⎢ 0 s y 0 p y (1 − s y ) ⎥ ⎢ y ⎥
⎢ ⎥=⎢ ⎥⎢ ⎥
⎣ z ⎦ ⎣ 0 0 sz pz (1 − sz ) ⎦ ⎣ z ⎦ .
1 0 0 0 1 1

```

Substituting the given values:
```
⎡ ⎤ ⎡ ⎤⎡ ⎤
x 2 0 0 −1 x
⎢ y  ⎥ ⎢ 0 3 0 −2 ⎥ ⎢ y ⎥
⎢ ⎥=⎢ ⎥⎢ ⎥
⎣ z ⎦ ⎣ 0 0 4 −3 ⎦ ⎣ z ⎦ .
1 000 1 1

```

The point (2, 2, 2) is transformed to (3, 4, 5):
```
⎡ ⎤ ⎡ ⎤⎡ ⎤
3 2 0 0 −1 2
⎢ 4 ⎥ ⎢ 0 3 0 −2 ⎥ ⎢ 2 ⎥
⎢ ⎥=⎢ ⎥⎢ ⎥
⎣ 5 ⎦ ⎣ 0 0 4 −3 ⎦ ⎣ 2 ⎦ .
1 000 1 1



```

10.14.4 2D Rotation

Compute the coordinates of the unit square in Table 10.1 after a rotation of 90◦ . The
points are rotated as follows:

<a id='p243'></a>
<!-- Página 243 -->

226 10 Geometric Transforms

Table 10.1 Original and rotated coordinates of the unit square
x y x y
0 0 0 0
1 0 0 1
1 1 −1 1
0 1 −1 0


```
⎡ ⎤ ⎡ ⎤⎡ ⎤
x cos β − sin β 0 x
⎣ y  ⎦ = ⎣ sin β cos β 0 ⎦ ⎣ y ⎦
1 0 0 1 1
⎡ ⎤⎡ ⎤
0 −1 0 x
= ⎣1 0 0⎦⎣ y ⎦
0 01 1
⎡ ⎤ ⎡ ⎤⎡ ⎤
0 0 −1 0 0
⎣0⎦ = ⎣1 0 0⎦⎣0⎦
1 0 01 1
⎡ ⎤ ⎡ ⎤⎡ ⎤
0 0 −1 0 1
⎣1⎦ = ⎣1 0 0⎦⎣0⎦
1 0 01 1
⎡ ⎤ ⎡ ⎤⎡ ⎤
−1 0 −1 0 1
⎣ 1⎦ = ⎣1 0 0⎦⎣1⎦
1 0 01 1
⎡ ⎤ ⎡ ⎤⎡ ⎤
−1 0 −1 0 0
⎣ 0⎦ = ⎣1 0 0⎦⎣1⎦.
1 0 01 1




```

10.14.5 2D Rotation About a Point

Derive the 2D homogeneous matrix to rotate 180◦ about (−1, 0), and compute the
transformed position of (0, 0).
```
⎡ ⎤ ⎡ ⎤⎡ ⎤
x cos β − sin β px (1 − cos β) + p y sin β x
⎣ y ⎦ = ⎣ sin β cos β p y (1 − cos β) − px sin β ⎦ ⎣ y ⎦


1 0 0 1 1
⎡ ⎤⎡ ⎤
cos 180◦ − sin 180◦ −1(1 − cos 180◦ ) + 0 sin 180◦ x
= ⎣ sin 180 cos 180
◦ ◦ 0(1 − cos 180 ) + 1 sin 180 ⎦ ⎣ y ⎦
◦ ◦

0 0 1 1
⎡ ⎤ ⎡ ⎤⎡ ⎤
−2 −1 0 −2 0
⎣ 0 ⎦ = ⎣ 0 −1 0 ⎦ ⎣ 0 ⎦ .
1 0 0 1 1

```

The point (0, 0) is rotated to (−2, 0).

<a id='p244'></a>
<!-- Página 244 -->

10.14 Worked Examples 227

10.14.6 Determinant of the Rotate Transform

Using determinants, show that the rotate transform preserves area.
The determinant of a 2D matrix transform reflects the area change produced by
the transform. Therefore, if area is preserved, the determinant must equal 1. Using
Sarrus’s rule: ⎡ ⎤
```
 cos β − sin β 0 
 
⎣ sin β cos β 0 ⎦ = cos2 β + sin2 β = 1
 
 0 0 1 

```

which confirms the role of the determinant.


10.14.7 Determinant of the Shear Transform

Using determinants, show that the shear transform preserves area.
The determinant of a 2D matrix transform reflects the area change produced by
the transform. Therefore, if area is preserved, the determinant must equal 1. Using
Sarrus’s rule: ⎡ ⎤
```
 1 tan β 0 
 
⎣ 0 1 0 ⎦ = 1
 
 0 0 1 

```

which confirms the role of the determinant.


10.14.8 Yaw, Pitch and Roll Transforms

Using the yaw and pitch transforms in the sequence yaw × pitch, compute how the
point (1, 1, 1) is transformed with yaw = pitch = 90◦ .
```
⎡ ⎤⎡ ⎤⎡ ⎤
⎡ 
⎤ cos yaw 0 sin yaw 0 1 0 0 0 x
x ⎢ ⎥ ⎢ ⎥ ⎢ ⎥
⎣ y ⎦ = ⎢ 0 1 0 0 ⎥⎢ 0 cos pitch − sin pitch 0 ⎥⎢y⎥
⎣ − sin yaw 0 cos yaw 0 ⎦ ⎣ 0 sin pitch cos pitch 0 ⎦ ⎣ z ⎦
1
0 0 0 1 0 0 0 1 1
⎡ ⎤⎡ ⎤⎡ ⎤
0010 10 00 x
⎢ 0 1 0 0 ⎥ ⎢ 0 0 −1 0 ⎥ ⎢ y ⎥
=⎢ ⎥⎢ ⎥⎢ ⎥
⎣ −1 0 0 0 ⎦ ⎣ 0 1 0 0 ⎦ ⎣ z ⎦
0001 00 01 1
```

⎡ ⎤ ⎡ ⎤⎡ ⎤
```
1 01 00 1
```

⎢ −1 ⎥ ⎢ 0 0 −1 0 ⎥ ⎢ 1 ⎥
⎢ ⎥ ⎢ ⎥⎢ ⎥
⎣ −1 ⎦ = ⎣ −1 0 0 0 ⎦ ⎣ 1 ⎦
```
1 00 01 1
```


<a id='p245'></a>
<!-- Página 245 -->

228 10 Geometric Transforms

therefore, (1, 1, 1) is transformed to (1, −1, −1).



10.14.9 3D Rotation About an Axis

Derive a homogeneous matrix to rotate (−1, 1, 0), 270◦ about an axis parallel to
the y-axis, and intersecting (1, 0, 0).
```
⎡ ⎤ ⎡ ⎤⎡ ⎤
x cos β 0 sin β px (1 − cos β) − pz sin β x
⎢ y ⎥ ⎢ 0 1 0 0 ⎥⎢y⎥
⎢ ⎥=⎢ ⎥⎢ ⎥
⎣ z ⎦ ⎣ − sin β 0 cos β pz (1 − cos β) + px sin β ⎦ ⎣ z ⎦
1 0 0 0 1 1
⎡ ⎤⎡ ⎤
cos 270 0 sin 270 1(1 − cos 270 ) − 0 sin 270◦
◦ ◦ ◦
x
⎢ 0 1 0 0 ⎥⎢y⎥
=⎢ ⎥⎢ ⎥
⎣ − sin 270◦ 0 cos 270◦ 0(1 − cos 270◦ ) + 1 sin 270◦ ⎦ ⎣ z ⎦
0 0 0 1 1
⎡ ⎤⎡ ⎤
0 0 −1 1(1 − 0) x
⎢0 1 0 0 ⎥⎢y⎥
=⎢ ⎥⎢ ⎥
⎣ 1 0 0 0(1 − 0) − 1 ⎦ ⎣ z ⎦
00 0 1 1
⎡ ⎤⎡ ⎤
0 0 −1 1 x
⎢0 1 0 0⎥⎢ y ⎥
=⎢ ⎥⎢ ⎥
⎣ 1 0 0 −1 ⎦ ⎣ z ⎦
00 0 1 1
⎡ ⎤ ⎡ ⎤⎡ ⎤
1 0 0 −1 1 −1
⎢ 1⎥ ⎢0 1 0 0⎥⎢ 1⎥
⎢ ⎥ ⎢ ⎥⎢ ⎥
⎣ −2 ⎦ = ⎣ 1 0 0 −1 ⎦ ⎣ 0 ⎦ .
1 00 0 1 1

```

The point (−1, 1, 0) is rotated to (1, 1, −2).



10.14.10 3D Rotation Transform Matrix

Show that the matrix for rotating a point about an arbitrary axis corresponds to the
three matrices for rotating about the x-, y- and z-axis.
```
⎡ ⎤
a 2 K + cos α abK − c sin α acK + b sin α 0
⎢ abK + c sin α b2 K + cos α bcK − a sin α 0 ⎥
⎢ ⎥
⎣ acK − b sin α bcK + a sin α c2 K + cos α 0 ⎦
0 0 0 1
```


<a id='p246'></a>
<!-- Página 246 -->

10.14 Worked Examples 229

Pitch about the x-axis: n̂ = i, where a = 1 and b = c = 0; K = 1 − cos α.
```
⎡ ⎤
1 0 0 0
⎢ 0 cos α − sin α 0 ⎥
pitch = ⎢
⎣ 0 sin α cos α 0 ⎦
⎥

0 0 0 1

```

Yaw about the y-axis: n̂ = j, where b = 1 and a = c = 0; K = 1 − cos α.
```
⎡ ⎤
cos α 0 sin α 0
⎢ 0 1 0 0⎥
yaw = ⎢ ⎥
⎣ − sin α 0 cos α 0 ⎦
0 0 0 1

```

Roll about the z-axis: n̂ = k, where c = 1 and a = b = 0; K = 1 − cos α.
```
⎡ ⎤
cos α − sin α 0 0
⎢ sin α cos α 0 0 ⎥
roll = ⎢
⎣ 0
⎥.
0 1 0⎦
0 0 01



```

10.14.11 2D Change of Axes

Derive a 2D homogeneous
```
√ matrix to compute
√ (1, 1) in an axial system with direction
```

cosines cos β = 2/2 and sin β = − 2/2.
```
⎡ ⎤ ⎡ ⎤
x   x
⎣ y ⎦ = cos β sin β ⎣y⎦
− sin β cos β
1 1
⎡ ⎤
√ √  1
2/2 −√ 2/2 ⎣ ⎦
= √ 1
2/2 2/2
1
⎡ ⎤ ⎡ ⎤
 √ √ 
√0 1
⎣ 2 ⎦ = √2/2 −√ 2/2 ⎣ 1 ⎦ .
2/2 2/2
1 1
√
```

The point (1, 1) has coordinates (0, 2) in the rotated axial system.

<a id='p247'></a>
<!-- Página 247 -->

230 10 Geometric Transforms

10.14.12 3D Change of Axes

Derive a 3D homogeneous matrix to compute the positions of (0, 0, 0) and (0, 1, 0)
in an axial system with 180◦ yaw, 0◦ pitch, 180◦ roll, and translated by (10, 0, 0).
```
⎡ ⎤ ⎡ ⎤⎡ ⎤
x T11 T12 T13 T14 x
⎢ y  ⎥ ⎢ T21 T22 T23 T24 ⎥ ⎢ y ⎥
⎢ ⎥=⎢ ⎥⎢ ⎥
⎣ z ⎦ ⎣ T31 T32 T33 T34 ⎦ ⎣ z ⎦
```


## 1 T41 T42 T43 T44 1


where

```
T11 = cos(yaw) cos(r oll) + sin(yaw) sin( pitch) sin(r oll)
T12 = cos( pitch) sin(r oll)
T13 = − sin(yaw) cos(r oll) + cos(yaw) sin( pitch) sin(r oll)
T14 = −(tx T11 + t y T12 + tz T13 )
T21 = − cos(yaw) sin(r oll) + sin(yaw) sin( pitch) cos(r oll)
T22 = cos( pitch) cos(r oll)
T23 = − sin(yaw) sin(r oll) + cos(yaw) sin( pitch) cos(r oll)
T24 = −(tx T21 + t y T22 + tz T23 )
T31 = sin(yaw) cos( pitch)
T32 = − sin( pitch)
T33 = cos(yaw) cos( pitch)
T34 = −(tx T31 + t y T32 + tz T33 )
```


## T41 = T42 = T43 = 0


## T44 = 1.


Substituting the above values:

```
T11 = cos 180◦ cos 180◦ + sin 180◦ sin 0◦ sin 180◦ = 1
T12 = cos 0◦ sin 180◦ = 0
T13 = − sin 180◦ cos 180◦ + cos 180◦ sin 0◦ sin 180◦ = 0
```


## T14 = −(−10T11 + 0T12 + 0T13 ) = 10

```
T21 = − cos 180◦ sin 180◦ + sin 180◦ sin 0◦ cos 180◦ = 0
T22 = cos 0◦ cos 180◦ = −1
T23 = − sin 180◦ sin 180◦ + cos 180◦ sin 0◦ cos 180◦ = 0
```


## T24 = −(−10T21 + 0T22 + 0T23 ) = 0

```
T31 = sin 180◦ cos 0◦ = 0
T32 = − sin 0◦ = 0
```


<a id='p248'></a>
<!-- Página 248 -->

10.14 Worked Examples 231

```
T33 = cos 180◦ cos 0◦ = −1
```


## T34 = −(−10T31 + 0T32 + 0T33 ) = 0


## T41 = T42 = T43 = 0


## T44 = 1.


Therefore: ⎡ ⎤ ⎡ ⎤⎡ ⎤
```
10 1 0 0 10 0
⎢ 0 ⎥ ⎢ 0 −1 0 0 ⎥ ⎢ 0 ⎥
⎢ ⎥=⎢ ⎥⎢ ⎥
⎣ 0 ⎦ ⎣ 0 0 −1 0 ⎦ ⎣ 0 ⎦
1 0 0 0 0 1

```

and ⎡ ⎤ ⎡ ⎤⎡ ⎤
```
10 1 0 0 10 0
⎢ −1 ⎥ ⎢ 0 −1 0 0 ⎥ ⎢ 1 ⎥
⎢ ⎥ ⎢ ⎥⎢ ⎥
⎣ 0 ⎦ = ⎣ 0 0 −1 0 ⎦ ⎣ 0 ⎦ .
1 0 0 0 0 1

```

The positions of (0, 0, 0) and (0, 1, 0) in the transformed axial system are
(10, 0, 0) and (10, −1, 0) respectively.



10.14.13 Rotate a Point About an Axis

```
◦
```

Derive a 3D homogeneous √ matrix√to rotate (1, 0, 0), 180 about an axis whose
parallel vector is n̂ = 1/ 2j + 1/ 2k.
Given
```
⎡  ⎤ ⎡ 2 ⎤⎡ ⎤
xp a K + cos α abK − c sin α acK + b sin α 0 xp
⎢ y p ⎥ ⎢ abK + c sin α b2 K + cos α bcK − a sin α 0 ⎥ ⎢ y p ⎥
⎢ ⎥=⎢ ⎥⎢ ⎥
⎣ z p ⎦ ⎣ acK − b sin α bcK + a sin α c2 K + cos α 0 ⎦ ⎣ z p ⎦
1 0 0 0 1 1

```

where
```
K = 1 − cos α.

```

Therefore,
```
⎡ ⎤ ⎡ ⎤⎡ ⎤
−1 −1 0 0 0 1
⎢ 0⎥ ⎢ 0 0 1 0⎥⎢0⎥
⎢ ⎥ ⎢ ⎥⎢ ⎥
⎣ 0⎦ = ⎣ 0 1 0 0⎦⎣0⎦.
1 0001 1

```

The rotated point is (−1, 0, 0).

<a id='p249'></a>
<!-- Página 249 -->

232 10 Geometric Transforms

Table 10.2 Coordinates of a 3D cube
Vertex xc yc zc xp yp
1 0 0 10 0 0
2 10 0 10 20 0
3 10 10 10 20 20
4 0 10 10 0 20
5 0 0 20 0 0
6 10 0 20 10 0
7 10 10 20 10 10
8 0 10 20 0 10



Fig. 10.32 A perspective Yp
sketch of a 3D cube
```
20 4 3




8 7
10




1, 5 6 2
Xp
10 20




```

10.14.14 Perspective Projection

Compute the perspective coordinates of a 3D cube stored in Table 10.2 with the
projection screen distance d = 20. Sketch the result.
Using the perspective transform:
```
⎡ ⎤ ⎡ ⎤⎡ ⎤
xp −1 0 0 0 xc
⎢ y p ⎥ ⎢ 0 1 0 0 ⎥ ⎢ yc ⎥
⎢ ⎥=⎢ ⎥⎢ ⎥
⎣ z p ⎦ ⎣ 0 0 1 0 ⎦ ⎣ zc ⎦ .
w 0 0 1/d 0 1

```

the perspective coordinates are stored in Table 10.2, and Fig. 10.32 shows a sketch
of the result.

<a id='p250'></a>
<!-- Página 250 -->


## Chapter 11

Quaternion Algebra




11.1 Introduction

This chapter contains some historical background to the invention of quaternions,
and covers the evolution of quaternion algebra. I show how quaternion algebra is
greatly simplified by treating a quaternion as an ordered pair, and provide examples
of addition, subtraction, real, pure and unit quaternions. After defining the complex
conjugate, norm, quaternion product, square and inverse, I show how a quaternion
is represented by a matrix. The chapter concludes with a summary of the important
definitions and several worked examples.



11.2 Some History

A complex number is defined as

```
z = a + ib, a, b ∈ , i 2 = −1.

```

Complex numbers can be regarded as a 2D point, which begs the question: is there
a complex object for a 3D point? After many years of thinking, Sir Willian Rowan
Hamilton found the answer in the form of a quaternion.
Hamilton defined a quaternion q, and its associated rules as

```
q = s + ia + jb + kc, s, a, b, c ∈ 

```

where,
```
i 2 = j 2 = k 2 = i jk = −1

i j = k, jk = i, ki = j
ji = −k, k j = −i, ik = − j

```

© Springer-Verlag London Ltd., part of Springer Nature 2022 233
J. Vince, Mathematics for Computer Graphics, Undergraduate Topics
in Computer Science, https://doi.org/10.1007/978-1-4471-7520-9_11

<a id='p251'></a>
<!-- Página 251 -->

234 11 Quaternion Algebra

[1–3], but we tend to write quaternions as

```
q = s + ai + bj + ck.

```

Observe from Hamilton’s rules how the occurrence of i j is replaced by k. The
extra imaginary k term is key to the cyclic patterns i j = k, jk = i, and ki = j, which
are very similar to the cross product of two unit Cartesian vectors:

```
i × j = k, j × k = i, k × i = j.

```

In fact, this similarity is no coincidence, as Hamilton also invented the scalar and
vector products. However, although quaternions provided an algebraic framework to
describe vectors, one must acknowledge that vectorial quantities had been studied
for many years prior to Hamilton.
Hamilton also saw that the i, j, k terms could represent three Cartesian unit
vectors i, j and k, which had to possess imaginary qualities. i.e. i2 = −1, etc., which
didn’t go down well with some mathematicians and scientists who were suspicious
of the need to involve so many imaginary terms.
Hamilton’s motivation to search for a 3D equivalent of complex numbers was part
algebraic, and part geometric. For if a complex number is represented by a couple
and is capable of rotating points on the plane by 90◦ , then perhaps a triple rotates
points in space by 90◦ . In the end, a triple had to be replaced by a a quadruple—a
quaternion.
One can regard Hamilton’s rules from two perspectives. The first, is that they
are an algebraic consequence of combining three imaginary terms. The second, is
that they reflect an underlying geometric structure of space. The latter interpretation
was adopted by the Scottish mathematical physicist Peter Guthrie Tait (1831–1901),
and outlined in his book An Elementary Treatise on Quaternions. Tait’s approach
assumes three unit vectors i, j, k aligned with the x-, y-, z-axes respectively:
The result of the multiplication of i into j or ij is defined to be the turning of j through a right
angle in the plane perpendicular to i in the positive direction, in other words, the operation
of i on j turns it round so as to make it coincide with k; and therefore briefly ij = k.
To be consistent it is requisite to admit that if i instead of operating on j had operated on
any other unit vector perpendicular to i in the plane yz, it would have turned it through a
right-angle in the same direction, so that ik can be nothing else than −j.
Extending to other unit vectors the definition which we have illustrated by referring to i, it
is evident that j operating on k must bring it round to i, or jk = i. [4]

Tait’s explanation is illustrated in Fig. 11.1a–d. Figure 11.1a shows the original alignment of i, j, k. Figure 11.1b shows the effect of turning j into k. Figure 11.1c shows
the turning of k into i, and Fig. 11.1d shows the turning of i in to j.
So far, there is no mention of imaginary quantities—we just have:

```
ij = k, jk = i, ki = j
ji = −k, kj = −i, ik = −j.
```


<a id='p252'></a>
<!-- Página 252 -->

11.2 Some History 235


```
(a) (b)
z z

k k

jk


i j i j
x y x y
(c) (d)
z z
k k

ki


i j i j
x y x y
ij

```

Fig. 11.1 Interpreting the products jk, ki, ij



If we assume that these vectors obey the distributive and associative axioms of
algebra, their imaginary qualities are exposed. For example:

```
ij = k

```

and multiplying throughout by i:

```
iij = ik = −j

```

therefore,
```
ii = i2 = −1.

```

Similarly, we can show that j2 = k2 = −1.
Next:
```
ijk = i(jk) = ii = i2 = −1.

```

Thus, simply by declaring the action of the cross-product, Hamilton’s rules emerge,
with all of their imaginary features. Tait also made the following observation:
A very curious speculation, due to Servois, and published in 1813 in Gergonne’s Annales
is the only one, so far has been discovered, in which the slightest trace of an√anticipation
of Quaternions is contained. Endeavouring to extend to space the form a + b −1 for the
plane, he is guided by analogy to write a directed unit-line in space the form

```
p cos α + q cos β + r cos γ ,
```


<a id='p253'></a>
<!-- Página 253 -->

236 11 Quaternion Algebra

where α, β, γ are its inclinations to the three axes. He perceives easily that p, q, r must
be non-reals : but, he asks, “seraient-elles imaginaires réductibles à la forme générale
```
√
```

A + B −1?” This could not be the answer. In fact they are the i, j, k of the Quaternion
Calculus. [4]

So the French mathematician François-Joseph Servois (1768–1847), was another
person who came very close to discovering quaternions. Furthermore, both Tait and
Hamilton were apparently unaware of a paper on transformation groups published
by the French banker and mathematician Olinde Rodrigues (1795–1851) in 1840.
And it doesn’t stop there: the brilliant mathematician Carl Friedrich Gauss was
extremely cautious, and nervous of publishing anything too revolutionary, just in case
he was ridiculed by fellow mathematicians. His diaries reveal that he had anticipated
non-euclidean geometry ahead of the Russian mathematician Nikolai Lobachevsky
(1792–1856). And in a short note from his diary in 1819 [5] he reveals that he
had identified a method of finding the product of two quadruples (a, b, c, d) and
(α, β, γ , δ) as:

```
(A, B, C, D) = (a, b, c, d)(α, β, γ , δ)
= (aα − bβ − cγ − dδ, aβ + bα − cδ + dγ ,
aγ + bδ + cα − dβ, aδ − bγ + cβ + dα).

```

At first glance, this result does not look like a quaternion product, but if we transpose
the second and third coordinates of the quadruples, and treat them as quaternions,
we have:

(A, B, C, D) = (a + ci + bj + dk)(α + γ i + β j + δk)
```
= aα − cγ − bβ − dδ + a(γ i + β j + δk)
+ α(ci + bj + dk), (bδ − dβ)i + (dγ − cδ) j + (cβ − bγ )k

```

which is identical to Hamilton’s quaternion product! Furthermore, Gauss also realised
that the product was non-commutative. However, he did not publish his findings, and
it was left to Hamilton to invent quaternions for himself, publish his results and take
the credit.
```
In 1881 and 1884, Josiah Willard Gibbs, at Yale University, printed his lecture
```

notes on vector analysis for his students. Gibbs had cut the ‘umbilical cord’ between
the real and vector parts of a quaternion and raised the 3D vector as an independent
object without any imaginary connotations. Gibbs also took on board the ideas of
Grassmann, who had been developing his own ideas for a vectorial system since
1832. Gibbs also defined the scalar and vector products using the relevant parts of
the quaternion product. Finally, in 1901, a student of Gibbs, Edwin Bidwell Wilson,
published Gibbs’ notes in book form: Vector Analysis [6], which contains the notation
in use today.
```
Quaternion algebra is definitely imaginary, yet simply by isolating the vector
```

part and ignoring the imaginary rules, Gibbs was able to reveal a new branch of
mathematics that exploded into vector analysis.

<a id='p254'></a>
<!-- Página 254 -->

11.2 Some History 237

```
Hamilton and his supporters were unable to persuade their peers that quaternions
```

could represent vectorial quantities, and eventually, Gibbs’ notation won the day, and
quaternions faded from the scene.
```
In recent years, quaternions have been rediscovered by the flight simulation indus-
```

try, and more recently by the computer graphics community, where they are used to
rotate vectors about an arbitrary axis. In the intervening years, various people have
had the opportunity to investigate the algebra, and propose new ways of harnessing
its qualities.
```
So let’s look at three ways of annotating a quaternion q:

q = s + xi + y j + zk (11.1)
q =s+v (11.2)
q = [s, v] (11.3)
where s, x, y, z ∈ , v ∈  3

and i 2 = j 2 = k 2 = −1.

The difference is rather subtle. In (11.1) we have Hamilton’s original definition
```

with its imaginary terms and associated rules. In (11.2) a ‘+’ sign is used to add a
scalar to a vector, which seems strange, yet works. In (11.3) we have an ordered pair
comprising a scalar and a vector.
```
Now you may be thinking: How is it possible to have three different definitions
```

for the same object? Well, I would argue that you can call an object whatever you
like, so long as they are algebraically identical. For example, matrix notation is used
to represent a set of linear equations, and leads to the same results as every-day
equations. Therefore, both systems of notation are equally valid.
```
Although I have employed the notation in (11.1) and (11.2) in other publications,
```

in this book I have used ordered pairs. So what we need to show is that Hamilton’s
original definition of a quaternion (11.1), with its scalar and three imaginary terms,
can be replaced by an ordered pair (11.3) comprising a scalar and a ‘modern’ vector.



11.3 Defining a Quaternion

Let’s start with two quaternions qa and qb à la Hamilton:

```
qa = sa + xa i + ya j + z a k
qb = sb + xb i + yb j + z b k

```

and the obligatory rules:
```
i 2 = j 2 = k 2 = i jk = −1

i j = k, jk = i, ki = j
ji = −k, k j = −i, ik = − j.
```


<a id='p255'></a>
<!-- Página 255 -->

238 11 Quaternion Algebra

Our objective is to show that qa and qb can also be represented by the ordered pairs

```
qa = [sa , a]
qb = [sb , b], sa , sb ∈ , a, b ∈ 3 .


```

The quaternion product qa qb expands to

```
qa qb = [sa , a][sb , b] = [sa + xa i + ya j + z a k][sb + xb i + yb j + z b k]
= [(sa sb − xa xb − ya yb − z a z b )
+ (sa xb + sb xa + ya z b − yb z a )i
+ (sa yb + sb ya + z a xb − z b xa ) j
+ (sa z b + sb z a + xa yb − xb ya )k]. (11.4)

```

Equation (11.4) takes the form of another quaternion, and confirms that the quaternion
product is closed.
At this stage, Hamilton turned the imaginary terms i, j, k into unit Cartesian
vectors i, j, k and transformed (11.4) into a vector form. The problem with this
approach is that the vectors retain their imaginary roots. The author Simon Altmann
suggests replacing the imaginaries by the ordered pairs:

```
i = [0, i], j = [0, j], k = [0, k]

```

which are themselves quaternions, and called quaternion units.
The idea of defining a quaternion in terms of quaternion units is exactly the same
as defining a vector in terms of its unit Cartesian vectors. Furthermore, it permits
vectors to exist without any imaginary associations.
Let’s substitute these quaternion units in (11.4) together with [1, 0] = 1:

```
[sa , a][sb , b] = [(sa sb − xa xb − ya yb − z a z b )[1, 0]
+ (sa xb + sb xa + ya z b − yb z a )[0, i]
+ (sa yb + sb ya + z a xb − z b xa )[0, j]
+ (sa z b + sb z a + xa yb − xb ya )[0, k]]. (11.5)

```

Next, we expand (11.5) using previously defined rules:

```
[sa , a][sb , b] = [[sa sb − xa xb − ya yb − z a z b , 0]
+ [0, (sa xb + sb xa + ya z b − yb z a )i]
+ [0, (sa yb + sb ya + z a xb − z b xa )j]
+ [0, (sa z b + sb z a + xa yb − xb ya )k]]. (11.6)
```


<a id='p256'></a>
<!-- Página 256 -->

11.3 Defining a Quaternion 239

A vertical scan of (11.6) reveals some hidden vectors:

[sa , a][sb , b] = [[sa sb − xa xb − ya yb − z a z b , 0]
```
+ [0, sa (xb i + yb j + z b k) + sb (xa i + ya j + z a k)
+ (ya z b − yb z a )i + (z a xb − z b xa )j + (xa yb − xb ya )k]]. (11.7)

```

Equation (11.7) contains two ordered pairs which can now be combined:

[sa , a][sb , b] = [sa sb − xa xb − ya yb − z a z b ,
```
+ sa (xb i + yb j + z b k) + sb (xa i + ya j + z a k)
+ (ya z b − yb z a )i + (z a xb − z b xa )j + (xa yb − xb ya )k]. (11.8)

```

If we make

```
a = xa i + ya j + z a k
b = xb i + yb j + z b k

```

and substitute them in (11.8) we get:

```
[sa , a][sb , b] = [sa sb − a · b, sa b + sb a + a × b] (11.9)

```

which defines the quaternion product.
From now on, we don’t have to worry about Hamilton’s rules as they are embedded
within (11.9). Furthermore, our vectors have no imaginary associations.
Although Rodrigues did not have access to Gibbs’ vector notation used in (11.9),
he managed to calculate the equivalent algebraic expression, which was some
achievement.



11.3.1 The Quaternion Units

Using (11.9) we can check to see if the quaternion units are imaginary by squaring
them:

```
i = [0, i]
i = [0, i][0, i]
2

= [i · i, i × i]
= [−1, 0]

```

which is a real quaternion and equivalent to −1, confirming that [0, i] is imaginary.
Using a similar expansion we can shown that [0, j] and [0, k] have the same property.

<a id='p257'></a>
<!-- Página 257 -->

240 11 Quaternion Algebra

Now let’s compute the products i j, jk and ki:

```
i j = [0, i][0, j]
= [−i · j, i × j]
= [0, k]

```

which is the quaternion unit k.

```
jk = [0, j][0, k]
= [−j · k, j × k]
= [0, i]

```

which is the quaternion unit i.

```
ki = [0, k][0, i]
= [−k · i, k × i]
= [0, j]

```

which is the quaternion unit j.
Next, let’s confirm that i jk = −1:

```
i jk = [0, i][0, j][0, k]
= [0, k][0, k]
= [−k · k, k × k]
= [−1, 0]

```

which is a real quaternion equivalent to −1, confirming that i jk = −1.
Thus the notation of ordered pairs upholds all of Hamilton’s rules. However, the
last double product assumes that quaternions are associative. So let’s double check
to show that (i j)k = i( jk):

```
i( jk) = [0, i][0, j][0, k]
= [0, i][0, i]
= [−i · i, i × i]
= [−1, 0]

```

which is correct.

<a id='p258'></a>
<!-- Página 258 -->

11.3 Defining a Quaternion 241

11.3.2 Example of Quaternion Products

Although we have yet to discover how quaternions are used to rotate vectors, let’s
concentrate on their algebraic traits by evaluating an example.

```
qa = [1, 2i + 3j + 4k]
qb = [2, 3i + 4j + 5k]

```

the product qa qb is

```
qa qb = [1, 2i + 3j + 4k][2, 3i + 4j + 5k]
= [1 × 2 − (2 × 3 + 3 × 4 + 4 × 5),
1(3i + 4j + 5k) + 2(2i + 3j + 4k)
+ (3 × 5 − 4 × 4)i − (2 × 5 − 4 × 3)j + (2 × 4 − 3 × 3)k]
= [−36, 7i + 10j + 13k − i + 2j − k]
= [−36, 6i + 12j + 12k]

```

which is another ordered pair representing a quaternion.
Having shown that Hamilton’s imaginary notation has a vector equivalent, and
can be represented as an ordered pair, we continue with this notation and describe
other features of quaternions. Note that we can abandon Hamilton’s rules as they
are embedded within the definition of the quaternion product, and will surface in the
following definitions.



11.4 Algebraic Definition

A quaternion is the ordered pair:

```
q = [s, v], s ∈ , v ∈ 3 .

```

If we express v in terms of its components, we have

```
q = [s, xi + yj + zk], s, x, y, z ∈ .



```

11.5 Adding and Subtracting Quaternions

Addition and subtraction employ the following rule:

```
qa = [sa , a]
```


<a id='p259'></a>
<!-- Página 259 -->

242 11 Quaternion Algebra

```
qb = [sb , b]
qa ± qb = [sa ± sb , a ± b].

```

For example:

```
qa = [0.5, 2i + 3j − 4k]
qb = [0.1, 4i + 5j + 6k]
qa + qb = [0.6, 6i + 8j + 2k]
qa − qb = [0.4, −2i − 2j − 10k].



```

11.6 Real Quaternion

A real quaternion has a zero vector term:

```
q = [s, 0].

```

The product of two real quaternions is

```
qa = [sa , 0]
qb = [sb , 0]
qa qb = [sa , 0][sb , 0]
= [sa sb , 0]

```

which is another real quaternion, and shows that they behave just like real numbers:

```
[s, 0] ≡ s.

```

We have already come across this with complex numbers containing a zero imaginary
term:
```
a + bi = a, when b = 0.



```

11.7 Multiplying a Quaternion by a Scalar

Intuition suggests that multiplying a quaternion by a scalar should obey the rule:

```
q = [s, v]
λq = λ[s, v], λ ∈ 
= [λs, λv].
```


<a id='p260'></a>
<!-- Página 260 -->

11.7 Multiplying a Quaternion by a Scalar 243

For example:

```
q = 3[2, 3i + 4j + 5k]
= [6, 9i + 12j + 15k].

```

We can confirm our intuition by multiplying a quaternion by a scalar in the form of
a real quaternion:

```
q = [s, v]
λ = [λ, 0]
λq = [λ, 0][s, v]
= [λs, λv]

```

which is excellent confirmation.



11.8 Pure Quaternion

Hamilton defined a pure quaternion as one having a zero scalar term:

```
q = xi + y j + zk

```

and is just a vector, but with imaginary qualities. Simon Altmann, and others, believe
that this was a serious mistake on Hamilton’s part to call a quaternion with a zero
real term, a vector.
```
The main issue is that there are two types of vectors: polar and axial, also called
```

a pseudovector. Richard Feynman describes polar vectors as ‘honest’ vectors [7]
and represent the every-day vectors of directed lines. Whereas, axial vectors are
computed from polar vectors, such as in a vector product. However, these two types
of vector do not behave in the same way when transformed. For example, given two
‘honest’, polar vectors a and b, we can compute the axial vector: c = a × b. Next, if
we subject a and b to an inversion transform through the origin, such that a becomes
−a, and b becomes −b, and compute their cross product (−a) × (−b), we still get c!
Which implies that the axial vector c must not be transformed along with a and b.
```
It could be argued that the inversion transform is not a ‘proper’ transform as it
```

turns a right-handed set of axes into a left-handed set. But in physics, laws of nature
are expected to work in either system. Unfortunately, Hamilton was not aware of this
distinction, as he had only just invented vectors. However, in the intervening years,
it has become evident that Hamilton’s quaternion vector is an axial vector, and not a
polar vector.
```
As we will see, in 3D rotations quaternions take the form
     
q = cos θ2 , sin θ2 v
```


<a id='p261'></a>
<!-- Página 261 -->

244 11 Quaternion Algebra

where θ is the angle of rotation and v is the axis of rotation, and when we set θ = 180◦ ,
we get
```
q = [0, v]

```

which remains a quaternion, even though it only contains a vector part.
Consequently, we define a pure quaternion as

```
q = [0, v].

```

The product of two pure quaternions is

```
qa = [0, a]
qb = [0, b]
qa qb = [0, a][0, b]
= [−a · b, a × b]

```

which is no longer ‘pure’, as some of the original vector information has ‘tunnelled’
across into the real part via the dot product.



11.9 Unit Quaternion

Let’s pursue this analysis further by introducing some familiar vector notation.
Give vector v, then

```
v = λv̂, where λ = v and v̂ = 1.

```

Combining this with the definition of a pure quaternion we get:

```
q = [0, v]
= [0, λv̂]
= λ[0, v̂]

```

and reveals the object [0, v̂] which is called the unit quaternion and comprises a
zero scalar and a unit vector. It is convenient to identify this unit quaternion as q̂:

```
q̂ = [0, v̂].

```

So now we have a notation similar to that of vectors where a vector v is described in
terms of its unit form:
```
v = λv̂
```


<a id='p262'></a>
<!-- Página 262 -->

11.9 Unit Quaternion 245

and a quaternion q is also described in terms of its unit form:

```
q = λq̂.

```

Note that q̂ is an imaginary object as it squares to −1:

```
q̂ 2 = [0, v̂][0, v̂]
= [−v̂ · v̂, v̂ × v̂]
= [−1, 0]
= −1

```

which is not too surprising, bearing in mind Hamilton’s original invention!


11.10 Additive Form of a Quaternion

We now come to the idea of splitting a quaternion into its constituent parts: a real
quaternion and a pure quaternion. Again, intuition suggests that we can write a
quaternion as

```
q = [s, v]
= [s, 0] + [0, v]

```

and we can test this by forming the algebraic product of two quaternions represented
in this way:

```
qa = [sa , 0] + [0, a]
qb = [sb , 0] + [0, b]
  
qa qb = [sa , 0] + [0, a] [sb , 0] + [0, b]
= [sa , 0][sb , 0] + [sa , 0][0, b] + [0, a][sb , 0] + [0, a][0, b]
= [sa sb , 0] + [0, sa b] + [0, sb a] + [−a · b, a × b]
= [sa sb − a · b, sa b + sb a + a × b]

```

which is correct, and confirms that the additive form works.


11.11 Binary Form of a Quaternion

Having shown that the additive form of a quaternion works, and discovered the unit
quaternion, we can join the two objects together as follows:

```
q = [s, v]
```


<a id='p263'></a>
<!-- Página 263 -->

246 11 Quaternion Algebra

```
= [s, 0] + [0, v]
= [s, 0] + λ[0, v̂]
= s + λq̂.

```

Just to recap, s is a scalar, λ is the length of the vector term, and q̂ is the unit quaternion
[0, v̂].
Look how similar this notation is to a complex number:

```
z = a + bi
q = s + λq̂

```

where a, b, s, λ are scalars, i is the unit imaginary and q̂ is the unit quaternion.



11.12 The Complex Conjugate of a Quaternion

We have already discovered that the conjugate of a complex number z = a + bi is
given by
```
z ∗ = a − bi

```

and is very useful in computing the inverse of z. The quaternion conjugate plays a
similar role in computing the inverse of a quaternion. Therefore, given

```
q = [s, v]

```

the quaternion conjugate is defined as

```
q ∗ = [s, −v].

```

For example:

```
q = [2, 3i − 4j + 5k]
q ∗ = [2, −3i + 4j − 5k]

```

If we compute the product qq ∗ we obtain

```
qq ∗ = [s, v][s, −v]
 
= s 2 − v · (−v), −sv + sv + v × (−v)
 
= s 2 + v · v, 0
 
= s 2 + v2 , 0 .
```


<a id='p264'></a>
<!-- Página 264 -->

11.12 The Complex Conjugate of a Quaternion 247

Let’s show that qq ∗ = q ∗ q:

```
q ∗ q = [s, −v][s, v]
 
= s 2 − (−v) · v, sv − sv + (−v) × v
 
= s 2 + v · v, 0
 
= s 2 + v2 , 0
= qq ∗ .

```

Now let’s show that (qa qb )∗ = qb∗ qa∗ .

```
qa = [sa , a]
qb = [sb , b]
qa qb = [sa , a][sb , b]
= [sa sb − a · b, sa b + sb a + a × b]
(qa qb )∗ = [sa sb − a · b, −sa b − sb a − a × b]. (11.10)

```

Next, we compute qb∗ qa∗

```
qa∗ = [sa , −a]
qb∗ = [sb , −b]
∗ ∗
qb qa = [sb , −b][sa , −a]
= [sa sb − a · b, −sa b − sb a − a × b]. (11.11)

```

And as (11.10) equals (11.11), (qa qb )∗ = qb∗ qa∗ .



11.13 Norm of a Quaternion

The norm of a complex number z = a + bi is defined as:
```

|z| = a 2 + b2

```

which allows us to write
```
zz ∗ = |z|2 .

```

Similarly, the norm of a quaternion q is defined as:

```
q = [s, v]
= [s, λv̂]

|q| = s 2 + λ2
```


<a id='p265'></a>
<!-- Página 265 -->

248 11 Quaternion Algebra

where λ = v which allows us to write

```
qq ∗ = |q|2 .

```

For example:

```
q = [1, 4i + 4j − 4k]

|q| = 12 + 42 + 42 + (−4)2
√
= 49
= 7.



```

11.14 Normalised Quaternion

A quaternion with a unit norm is called a normalised quaternion. For example, the
quaternion q = [s, v] is normalised by dividing it by |q|:
```
q
q = √ .
s 2 + λ2
```

We must be careful not to confuse the unit quaternion with a unit-norm quaternion.
The unit quaternion is [0, v̂] with a unit-vector part, whereas a unit-norm quaternion
is normalised such that s 2 + λ2 = 1.
```
I will be careful to distinguish between these two terms as many authors—
```

including myself—use the term unit quaternion to describe a quaternion with a unit
norm. For example:

```
q = [1, 4i + 4j − 4k]

```

has a norm of 7, and q is normalised by dividing by 7:

```
q  = 17 [1, 4i + 4j − 4k] .

```

The type of unit-norm quaternion we will be using takes the form:
```
     
q = cos θ2 , sin θ2 v̂

```

because cos2 θ + sin2 θ = 1.



11.15 Quaternion Products

Having shown that ordered pairs can represent a quaternion and its various manifestations, let’s summarise the products we will eventually encounter. To start, we have
the product of two normal quaternions:

<a id='p266'></a>
<!-- Página 266 -->

11.15 Quaternion Products 249

```
qa qb = [sa , a][sb , b]
= [sa sb − a · b, sa b + sb a + a × b].



```

11.15.1 Product of Pure Quaternions

Given two pure quaternions:

```
qa = [0, a]
qb = [0, b]

```

their product is

```
qa qb = [0, a][0, b]
= [−a · b, a × b].



```

11.15.2 Product of Unit-Norm Quaternions

Given two unit-norm quaternions:

```
qa = [sa , a]
qb = [sb , b]

```

where |qa | = |qb | = 1. Their product is another unit-norm quaternion, which is
proved as follows.
We assume qc = [sc , c] and show that |qc | = sc2 + c2 = 1 where

```
[sc , c] = [sa , a][sb , b]
= [sa sb − a · b, sa b + sb a + a × b].

```

Let’s assume the angle between a and b is θ , which permits us to write:

```
sc = sa sb − ab cos θ
 
c = sa bb̂ + sb a â + ab sin θ â × b̂ .

```

Therefore,

```
sc2 = (sa sb − ab cos θ )(sa sb − ab cos θ )
= sa2 sb2 − 2sa sb ab cos θ + a 2 b2 cos2 θ.
```


<a id='p267'></a>
<!-- Página 267 -->

250 11 Quaternion Algebra

Fig. 11.2 Geometry for |â × b̂| = ab sin θ
sa bb̂ + sb a â + ab sin θ(â ×
b̂)
```
c



sa bb̂ d
sa bb̂
π−θ θ
sb aâ


```

Figure 11.2 shows the geometry representing c.

```
d 2 = sb2 a 2 + sa2 b2 − 2sa sb ab cos(π − θ)
= sb2 a 2 + sa2 b2 + 2sa sb ab cos θ
c2 = d 2 + a 2 b2 sin2 θ
= sb2 a 2 + sa2 b2 + 2sa sb ab cos θ + a 2 b2 sin2 θ
```

sc2 + c2 = sa2 sb2 − 2sa sb ab cos θ + a 2 b2 cos2 θ + sb2 a 2 + sa2 b2 + 2sa sb ab cos θ + a 2 b2 sin2 θ
```
= sa2 sb2 + a 2 b2 + sb2 a 2 + sa2 b2
   
= sa2 sb2 + b2 + a 2 sb2 + b2

= sa2 + a 2
= 1.


```

Therefore, the product of two unit-norm quaternions is another unit-norm quaternion.
Consequently, multiplying a quaternion by a unit-norm quaternion, does not change
its norm:

```
qa = [sa , a]
|qa | = 1
qb = [sb , b]
|qa qb | = |qb |.



```

11.15.3 Square of a Quaternion

The square of a quaternion is given by:

```
v = xi + yj + zk
q = [s, v]
q 2 = [s, v][s, v]
```


<a id='p268'></a>
<!-- Página 268 -->

11.15 Quaternion Products 251
```
 
= s 2 − v · v, 2sv + v × v
 
= s 2 − v · v, 2sv
 
= s 2 − x 2 − y 2 − z 2 , 2s(xi + yj + zk) .

```

For example:

```
q = [7, 2i + 3j + 4k]
 
q 2 = 72 − 22 − 32 − 42 , 14(2i + 3j + 4k)
= [20, 28i + 42j + 56k].

```

The square of a pure quaternion is

```
v = xi + yj + zk
q = [0, v]
q 2 = [0, v][0, v]
= [0 − v · v, v × v]
= [0 − v · v, 0]
   
= − x 2 + y2 + z2 , 0

```

which makes the square of a pure, unit-norm quaternion equal to −1, and was one
of the results, to which some 19th-century mathematicians objected.



11.15.4 Norm of the Quaternion Product

In proving that the product of two unit-norm quaternions is another unit-norm quaternion we saw that

```
qa = [sa , a]
qb = [sb , b]
q c = qa q b
   
|qc |2 = sa2 sb2 + b2 + a 2 sb2 + b2
  
= sa2 + a 2 sb2 + b2

```

which, if we ignore the constraint of unit-norm quaternions, shows that the norm of
a quaternion product equals the product of the individual norms:

```
|qa qb |2 = |qa |2 |qb |2
|qa qb | = |qa ||qb |.
```


<a id='p269'></a>
<!-- Página 269 -->

252 11 Quaternion Algebra

11.16 Inverse Quaternion

An important feature of quaternion algebra is the ability to divide two quaternions
qb /qa , as long as qa does not vanish.
```
By definition, the inverse q −1 of q satisfies

qq −1 = [1, 0] = 1. (11.12)

```

To isolate q −1 , we multiply (11.12) by q ∗

```
q ∗ qq −1 = q ∗
|q|2 q −1 = q ∗ (11.13)

```

and from (11.13) we can write
```
q∗
q −1 = .
|q|2

```

If q is a unit-norm quaternion, then

```
q −1 = q ∗

```

which is useful in the context of rotations.

Furthermore, as
```
(qa qb )∗ = qb∗ qa∗

```

then
```
(qa qb )−1 = qb−1 qa−1 .

```

Note that qq −1 = q −1 q:

```
qq ∗
qq −1 = =1
|q|2
q ∗q
q −1 q = = 1.
|q|2

```

Thus, we represent the quotient qb /qa as
```
qb
qc =
qa
= qb qa−1
qb qa∗
= .
|qa |2
```


<a id='p270'></a>
<!-- Página 270 -->

11.16 Inverse Quaternion 253

For completeness let’s evaluate the inverse of q where

```
q = 1, √13 i + √13 j + √13 k

q ∗ = 1, − √13 i − √13 j − √13 k
|q|2 = 1 + 13 + 13 + 13 = 2
q∗
q −1 = = 21 1, − √13 i − √13 j − √13 k .
|q|2

```

It should be clear that q −1 q = 1:

```
q −1 q = 21 1, − √13 i − √13 j − √13 k 1, √13 i + √13 j + √13 k
 
= 21 1 + 13 + 13 + 13 , 0
= 1.



```

11.17 Matrices

Matrices provide another way to express a quaternion product. For convenience, let’s
repeat (11.8) again and show it in matrix form:

```
[sa , a] [sb , b] = [sa sb − xa xb − ya yb − z a z b ,
+ sa (xb i + yb j + z b k) + sb (xa i + ya j + z a k)
+ (ya z b − yb z a )i + (z a xb − z b xa )j + (xa yb − xb ya )k]
⎡ ⎤⎡ ⎤
sa −xa −ya −z a sb
⎢ xa sa −z a ya ⎥ ⎢ xb ⎥
=⎣⎢ ⎥ ⎢ ⎥. (11.14)
ya z a sa −xa ⎦ ⎣ yb ⎦
z a −ya xa sa zb

```

Let’s recompute the product qa qb using the above matrix:

```
qa = [1, 2i + 3j + 4k]
qb = [2, 3i + 4j + 5k]
⎡ ⎤⎡ ⎤
1 −2 −3 −4 2
⎢ 2 1 −4 3 ⎥ ⎢ 3 ⎥
qa q b = ⎢ ⎥⎢ ⎥
⎣ 3 4 1 −2 ⎦ ⎣ 4 ⎦
4 −3 2 1 5
```


<a id='p271'></a>
<!-- Página 271 -->

254 11 Quaternion Algebra
```
⎡ ⎤
−36
⎢ 6⎥
=⎢
⎣ 12 ⎦
⎥

12
= [−36, 6i + 12j + 12k] .



```

11.17.1 Orthogonal Matrix

We can demonstrate that the unit-norm quaternion matrix is orthogonal by showing
that the product with its transpose equals the identity matrix. As we are dealing with
matrices, Q will represent the matrix for q:

```
q = [s, xi + yj + zk]
where 1 = s 2 + x 2 + y 2 + z 2
⎡ ⎤
s −x −y −z
⎢ x s −z y ⎥
Q=⎢ ⎣ y z s −x ⎦
⎥

z −y x s
⎡ ⎤
s x y z
⎢ −x s z −y ⎥
```


## QT = ⎢

```
⎣ −y −z s x ⎦
⎥

−z y −x s
⎡ ⎤⎡ ⎤
s −x −y −z s x y z
⎢ x s −z y ⎥ ⎢ −x s z −y ⎥
```


## QQT = ⎢ ⎥⎢

```
⎣ y z s −x ⎦ ⎣ −y −z s x ⎦
⎥

z −y x s −z y −x s
⎡ ⎤
1000
⎢0 1 0 0⎥
=⎣⎢ ⎥
0 0 1 0⎦
0001

```

For this to occur, QT = Q−1 .



11.18 Quaternion Algebra

Ordered pairs provide a simple notation for representing quaternions, and allow us
to represent the real unit 1 as [1, 0], and the imaginaries i, j, k as [0, i], [0, j],
[0, k] respectively. A quaternion then becomes a linear combination of these elements with associated real coefficients. Under such conditions, the elements form
the basis for an algebra over the field of reals.

<a id='p272'></a>
<!-- Página 272 -->

11.18 Quaternion Algebra 255

Furthermore, because quaternion algebra supports division, and obeys the normal
axioms of algebra, except that multiplication is non-commutative, it is called a division algebra. The German mathematician Ferdinand Georg Frobenius (1849–1917)
proved that only three such real associative division algebras exist: real numbers,
complex numbers and quaternions [8].
The Cayley numbers , constitute a real division algebra, but the Cayley numbers
are 8-dimensional and are not associative, i.e. a(bc) = (ab)c for all a, b, c ∈ .



11.19 Summary

Quaternions are very similar to complex numbers, apart from the fact that they
have three imaginary terms, rather than one. Consequently, they inherit some of
the properties associated with complex numbers, such as norm, complex conjugate,
unit norm and inverse. They can also be added, subtracted, multiplied and divided.
However, unlike complex numbers, they anticommute when multiplied.



11.19.1 Summary of Definitions

Quaternion

```
qa = [sa , a] = [sa , xa i + ya j + z a k]
qb = [sb , b] = [sb , xb i + yb j + z b k] .

```

Adding and subtracting

```
qa ± qb = [sa ± sb , a ± b].

```

Product

```
qa qb = [sa , a][sb , b]
= [sa sb − a · b, sa b + sb a + a × b]
⎡ ⎤⎡ ⎤
sa −xa −ya −z a sb
⎢ xa sa −z a ya ⎥ ⎢ xb ⎥
=⎢ ⎥⎢ ⎥
⎣ ya z a sa −xa ⎦ ⎣ yb ⎦ .
z a −ya xa sa zb

```

Square

```
v = xi + yj + zk
q 2 = [s, v][s, v]
```


<a id='p273'></a>
<!-- Página 273 -->

256 11 Quaternion Algebra
```
 
= s 2 − x 2 − y 2 − z 2 , 2s(xi + yj + zk) .

```

Pure

```
v = xi + yj + zk
q 2 = [0, v][0, v]
 
= −(x 2 + y 2 + z 2 ), 0 .

```

Norm

```
v = λv̂
q = [s, λv̂]

|q| = s 2 + λ2 .

```

Unit norm 
```
|q| = s 2 + λ2 = 1.

```

Conjugate

```
q ∗ = [s, −v]
(qa qb )∗ = qb∗ qa∗ .

```

Inverse
```
q∗
q −1 =
|q|2
(qa qb ) = qb−1 qa−1 .
−1




```

11.20 Worked Examples

Here are some further worked examples that employ the ideas described above. In
some cases, a test is included to confirm the result.



11.20.1 Adding and Subtracting Quaternions

Add and subtract the following quaternions:

```
qa = [2, −2i + 3j − 4k]
qb = [1, −2i + 5j − 6k]
```


<a id='p274'></a>
<!-- Página 274 -->

11.20 Worked Examples 257

```
qa + qb = [3, −4i + 8j − 10k]
qa − qb = [1, 0i − 2j + 2k].



```

11.20.2 Norm of a Quaternion

Find the norm of the following quaternions:

```
qa = [2, −2i + 3j − 4k]
qb = [1, −2i + 5j − 6k]
 √
|qa | = 22 + (−2)2 + 32 + (−4)2 = 33
 √
|qb | = 12 + (−2)2 + 52 + (−6)2 = 66.



```

11.20.3 Unit-norm Quaternions

Convert these quaternions to their unit-norm form:

```
qa = [2, −2i + 3j − 4k]
qb = [1, −2i + 5j − 6k]
√
|qa | = 33
√
|qb | = 66
qa = √133 [2, −2i + 3j − 4k]
qb = √166 [1, −2i + 5j − 6k].



```

11.20.4 Quaternion Product

Compute the product and reverse product of the following quaternions.

```
qa = [2, −2i + 3j − 4k]
qb = [1, −2i + 5j − 6k]
```

qa qb = [2, −2i + 3j − 4k][1, −2i + 5j − 6k]
```
= [2 × 1 − ((−2) × (−2) + 3 × 5 + (−4) × (−6)),
+ 2(−2i + 5j − 6k) + 1(−2i + 3j − 4k)
+ (3 × (−6) − (−4) × 5)i − ((−2) × (−6) − (−4) × (−2))j + ((−2) × 5 − 3 × (−2))k]
= [−41, −6i + 13j − 16k + 2i − 4j − 4k]
= [−41, −4i + 9j − 20k].
```


<a id='p275'></a>
<!-- Página 275 -->

258 11 Quaternion Algebra


qb qa = [1, −2i + 5j − 6k][2 − 2i + 3j − 4k]
```
= [1 × 2 − ((−2) × (−2) + 5 × 3 + (−6) × (−4)),
+ 1(−2i + 3j − 4k) + 2(−2i + 5j − 6k)
+ (5 × (−4) − (−6) × 3)i − ((−2) × (−4) − (−6) × (−2))j + ((−2) × 3 − 5 × (−2))k]
= [−41, −6i + 13j − 16k − 2i + 4j + 4k]
= [−41, −8i + 17j − 12k].


```

Note: The only thing that has changed in this computation is the sign of the
cross-product axial vector.



11.20.5 Square of a Quaternion

Compute the square of this quaternion:

```
q = [2, −2i + 3j − 4k]
q 2 = [2, −2i + 3j − 4k][2, −2i + 3j − 4k]
= [2 × 2 − ((−2) × (−2) + 3 × 3 + (−4) × (−4)),
+ 2 × 2(−2i + 3j − 4k)]
= [−25, −8i + 12j − 16k].



```

11.20.6 Inverse of a Quaternion

Compute the inverse of this quaternion:

```
q = [2, −2i + 3j − 4k]
q ∗ = [2, 2i − 3j + 4k]
|q|2 = 22 + (−2)2 + 32 + (−4)2 = 33
q −1 = 33
1
[2, 2i − 3j + 4k].




```

References

1. Hamilton WR (1844) On quaternions: or a new system of imaginaries in algebra. Phil Mag 3rd
ser. 25
2. Hamilton WR (1853) Lectures on quaternions. Hodges & Smith, Dublin
3. Hamilton WR (1899–1901) Elements of quaternions, 2nd edn. Longmans, Green & Co., London
(Jolly, C.J. (ed.) 2 vols.)

<a id='p276'></a>
<!-- Página 276 -->

References 259

4. Tait PG (1867) An elementary treatise on quaternions. Cambridge University Press, Cambridge
5. Gauss CF (1819) Mutation des Raumes In: Carl Friedrich Gauss Werke, Achter Band, pp 357–
361, König. Gesell. Wissen. Göttingen, 1900
6. Wilson EB (1901) Vector analysis. Yale University Press, New Haven
7. Feynman RP. Symmetry and physical laws. In: Feynman lectures in physics, vol 1
8. Altmann SL (2005) Rotations. Quaternions and Double Groups, Dover, New York

<a id='p277'></a>
<!-- Página 277 -->


## Chapter 12

Quaternions in Space




12.1 Introduction

In this chapter we show how quaternions are used to rotate vectors about an arbitrary
axis. We begin by reviewing some of the history associated with quaternions, and
the development of octonions.
```
We then examine various quaternion products to discover their rotational prop-
```

erties. This begins with two orthogonal quaternions, and moves towards the general
case of using qpq −1 where q is a unit-norm quaternion, and p is a pure quaternion.
```
A technique shows how to express a quaternion product as a matrix.
We continue to represent a quaternion as an ordered pair, with italic, lower-case
```

letters to represent quaternions, and bold lower-case letters to represent vectors.


12.2 Some History

Hamilton invented quaternions in October 1843, and by December of the same year,
his friend, Irish mathematician John Thomas Graves (1806–1870), had invented
octaves, which would eventually be called octonions. Arthur Cayley had also been
intrigued by Hamilton’s quaternions, and independently invented octonions in 1845.
Octonions eventually became known as Cayley numbers rather than octaves, simply
because Graves did not publish his results until 1848—three years after Cayley!
Just as quaternions can be defined in terms of ordered pairs of complex numbers,
the octaves, or octonions, can be defined as ordered pairs of quaternions.


12.3 Quaternion Products

A quaternion q is the union of a scalar s and a vector v:

```
q = [s, v], s ∈ , v ∈ 3 .
```

© Springer-Verlag London Ltd., part of Springer Nature 2022 261
J. Vince, Mathematics for Computer Graphics, Undergraduate Topics
in Computer Science, https://doi.org/10.1007/978-1-4471-7520-9_12

<a id='p278'></a>
<!-- Página 278 -->

262 12 Quaternions in Space

If we express v in terms of its components, we have

```
q = [s, xi + yj + zk], s, x, y, z ∈ .

```

When two such quaternions are multiplied together, we obtain a third quaternion:

```
qa = [sa , va ]
qb = [sb , vb ]
qa qb = [sa , va ][sb , vb ]
= [sa sb − va · vb , sa vb + sb va + va × vb ].

```

Naturally, if sa or sb are zero, as in the case of a pure quaternion, the product is
simplified. Therefore, in future I will omit any zero terms, to simplify the algebra.
Hamilton had hoped that a quaternion could be used like a complex rotor, where

```
Rθ = cos θ + i sin θ

```

rotates a complex number by θ . Could a unit-norm quaternion q be used to rotate
a vector stored as a pure quaternion p? Well yes, but only as a special case. To
understand this, let’s construct the product of a unit-norm quaternion q and a pure
quaternion p. The unit-norm quaternion q is defined as

```
q = [s, λv̂], s, λ ∈ , v̂ ∈ 3 , (12.1)
v̂ = 1
s + λ2 = 1
2



```

and the pure quaternion p stores the vector p to be rotated:

```
p = [0, p], p ∈ 3 .

```

Let’s compute the product p  = qp and examine the vector part of p  to see if p is
rotated:

```
q = [s, λv̂]
p = [0, p]
p  = qp
= [s, λv̂][0, p]
= [−λv̂ · p, sp + λv̂ × p]. (12.2)

```

We can see from (12.2) that the result is a general quaternion with a scalar and a
vector component.

<a id='p279'></a>
<!-- Página 279 -->

12.3 Quaternion Products 263

12.3.1 Special Case

The ‘special case’ referred to above is that v̂ must be perpendicular to p, which
makes the dot product term −λv̂ · p in (12.2) vanish, and we are left with the pure
quaternion:
```
p  = [0, sp + λv̂ × p]. (12.3)

Figure 12.1 illustrates this scenario, where p is perpendicular to v̂, and v̂ × p is
```

perpendicular to the plane containing p and v̂.
```
Now as v̂ is a unit vector, p = v̂ × p, which means that we have two orthog-
```

onal vectors, i.e. p and v̂ × p, with the same length. Therefore, to rotate p about v̂,
all that we have to do is make s = cos θ and λ = sin θ in (12.3):

```
p  = [0, p ]
= [0, cos θ p + sin θ v̂ × p].

```

For example, to rotate a vector about the z-axis, q’s vector v̂ must be aligned with
the z-axis as shown in Fig. 12.2. If we make the angle of rotation θ = 45◦ then

```
q = [s, λv̂]
= [cos θ, sin θ k]


```

Fig. 12.1 Three orthogonal z
vectors p, v̂ and v̂ × p

```
p
v̂


θ

x y
p
v̂ × p

```

Fig. 12.2 The vector 2i is z
rotated ◦ by the quaternion
```
 √45 √  v̂ = k
```

q = 22 , 22 k



```
p = 2i 45◦ v̂ × p = 2j
x y
√ √
p = 2i + 2j
```


<a id='p280'></a>
<!-- Página 280 -->

264 12 Quaternions in Space
```
√ √ 
= 2
2
, 2
2
k
√
= 22 [1, k]

```

and if the vector to be rotated is p = 2i, then

```
p = [0, p]
= [0, 2i]
= 2[0, i].

```

There are now four product combinations worth exploring: qp, pq, q −1 p and pq −1 .
It’s not worth considering qp −1 and p −1 q as p −1 simply reverses the direction of p.
Let’s start with qp:
```
√
q = 22 [1, k]
p = 2[0, i]
p  = qp
√
= 2[1, k][0, i]
√
= 2[0, i + j]
√ √
```

and p has been rotated 45◦ to p = 2i + 2j.

Next, pq:

```
p = 2[0, i]
√
q = 22 [1, k]
p  = pq
√
= 2[0, i][1, k]
√
= 2[0, i + i × k]
√
= 2[0, i − j]
√ √
```

and p has been rotated −45◦ to p = 2i − 2j.

Next, q −1 p, and as q is a unit-norm quaternion, q −1 = q ∗ :
```
√
q = 22 [1, k]
√
q −1 = 22 [1, −k]
p = 2[0, i]
p  = q −1 p
```


<a id='p281'></a>
<!-- Página 281 -->

12.3 Quaternion Products 265
```
√
= 2[1, −k][0, i]
√
= 2[0, i − k × i]
√
= 2[0, i − j]
√ √
```

and p has been rotated −45◦ to p = 2i − 2j.
Finally, pq −1 :

```
p = 2[0, i]
√
q = 22 [1, k]
√
q −1 = 22 [1, −k]
p  = pq −1
√
= 2[0, i][1, −k]
√
= 2[0, i − i × k]
√
= 2[0, i + j]
√ √
```

and p has been rotated 45◦ to p = 2i + 2j. Thus, for orthogonal quaternions, θ
is the angle of rotation, then

```
qp = pq −1
pq = q −1 p.

```

Before moving on, let’s see what happens to the product qp when θ = 180◦ :

```
q = [cos θ, sin θ k]
= [−1, 0]
p = 2[0, i]
p  = qp
= 2[−1, 0][0, i]
= 2[0, −i + 0 × i]
= [0, −2i]

```

and p has been rotated 180◦ to p = −2i.
Note that in all the above products, the vector has not been scaled during the
rotation. This is because q is a unit-norm quaternion.
Now let’s see what happens if we change the angle between v̂ and p. Let’s reduce
the angle to 45◦ and retain q’s unit vector, as shown in Fig. 12.3, such that v̂ is
directed along the z-axis, and p = i + k. Therefore,

```
v̂ = k
```


<a id='p282'></a>
<!-- Página 282 -->

266 12 Quaternions in Space

Fig. 12.3 Rotating the z
vector p = i + k by the v̂ = k
```
p=i+k
```

quaternion
```
 
```

q = cos θ, sin θ v̂




```
x y


 
q = cos θ, sin θ v̂
p = [0, p].

```

This time we must include the dot product term − sin θ v̂ · p, as it is no longer
zero:

```
q = [cos θ, sin θ v̂]
p = [0, p]
p  = qp
= [cos θ, sin θ v̂][0, p]
= [− sin θ v̂ · p, cos θ p + sin θ v̂ × p]. (12.4)

```

Substituting v̂, p and θ = 45◦ in (12.4), we have

```
v̂ = k
p=i+k
 √ √ √ 
p  = − 22 k · (i + k) , 22 (i + k) + 22 k × (i + k)
 √ √ √ √ 
= − 22 , 22 i + 22 k + 22 j
√
= 22 [−1, i + j + k] (12.5)

```

which, unfortunately, is no longer a pure quaternion. Multiplying the vector by a
non-orthogonal quaternion has converted some of the vector information into the
quaternion’s scalar component.



12.3.2 General Case

Not to worry. Could it be that an inverse quaternion reverses the operation? Let’s see
what happens if we post-multiply qp by q −1 .

<a id='p283'></a>
<!-- Página 283 -->

12.3 Quaternion Products 267

Given
```
q = [cos θ, sin θ k]

```

then

```
q −1 = [cos θ, − sin θ k]
√ √ 
= 22 , − 22 k
√
= 22 [1, −k].

```

Therefore, post-multiplying (12.5) by q −1 we have:
```
√
qp = 22 [−1, i + j + k]
√
q −1 = 22 [1, −k]
√ √
qpq −1 = 22 [−1, i + j + k] 22 [1, −k]
= 21 [−1, i + j + k][1, −k]
= 21 [−1 + 1, k + i + j + k + (i + j + k) × −k)]
= 21 [0, i + j + 2k − i + j]
= [0, j + k]. (12.6)
√
```

Equation (12.6) is a pure quaternion, with a norm of 2, which is the same as p.
However, the vector has been rotated 90◦ rather than 45◦ , twice the desired angle, as
shown in Fig. 12.4.
If this ‘sandwiching’ of the vector in the form of a pure quaternion by q and q −1
is correct, it suggests that increasing θ to 90◦ should rotate p = i + k by 180◦ to
−i + k. Let’s try this.
Let θ = 90◦ , therefore,

```
q = [cos 90◦ , sin 90◦ k]
= [0, k]
p = [0, i + k]
qp = [0, k][0, i + k]


```

Fig. 12.4 The vector i + k z
is rotated 90◦ to j + k
```
p=i+k v̂ = k p = j + k

90◦



x y
```


<a id='p284'></a>
<!-- Página 284 -->

268 12 Quaternions in Space

```
= [−1, k × (i + k)]
= [−1, j].

```

Next, we post-multiply qp by q −1 :

```
q −1 = [0, −k]
qpq −1 = [−1, j][0, −k]
= [0, k + (j × −k)]
= [0, −i + k]

```

which confirms our prediction and suggests that qpq −1 works.



12.3.3 Double Angle

Now let’s show how this double angle arises. We begin by defining a unit-norm
quaternion q:
```
q = [s, λv̂]

```

where s 2 + λ2 = 1. The vector p to be rotated is encoded as a pure quaternion:

```
p = [0, p]

```

and the inverse quaternion q −1 is

```
q −1 = [s, −λv̂].

```

Therefore, the product qpq −1 is
```
 
qpq −1 = s, λv̂ [0, p][s, −λv̂]
 
= −λv̂ · p, sp + λv̂ × p [s, −λv̂]

= −λs v̂ · p + λsp · v̂ + λ2 (v̂ × p) · v̂,
+ λ2 (v̂ · p)v̂ + s 2 p + λs v̂ × p

− λsp × v̂ − λ2 (v̂ × p) × v̂
 
= λ2 (v̂ × p) · v̂, λ2 (v̂ · p)v̂ + s 2 p + 2λs v̂ × p − λ2 (v̂ × p) × v̂ .

```

Note that
```
(v̂ × p) · v̂ = 0

```

and
```
(v̂ × p) × v̂ = (v̂ · v̂)p − (p · v̂)v̂ = p − (p · v̂)v̂.
```


<a id='p285'></a>
<!-- Página 285 -->

12.3 Quaternion Products 269

Therefore,
```
     
qpq −1 = 0, λ2 v̂ · p v̂ + s 2 p + 2λs v̂ × p − λ2 p + λ2 p · v̂ v̂
     
= 0, 2λ2 v̂ · p v̂ + s 2 − λ2 p + 2λs v̂ × p . (12.7)

```

Clearly, (12.7) is a pure quaternion as the scalar component is zero. However, it is
not obvious where the angle doubling comes from. But look what happens when we
make s = cos θ and λ = sin θ :
```
     
qpq −1 = 0, 2 sin2 θ v̂ · p v̂ + cos2 θ − sin2 θ p + 2 sin θ cos θ v̂ × p
   
= 0, (1 − cos(2θ )) v̂ · p v̂ + cos(2θ )p + sin(2θ )v̂ × p .

```

The double-angle trigonometric terms emerge! Now, if we want this product to
actually rotate the vector by θ , then we must build this in from the outset by halving
θ in q:      
```
q = cos θ2 , sin θ2 v̂ (12.8)

```

which makes
```
   
qpq −1 = 0, (1 − cos θ ) v̂ · p v̂ + cos θ p + sin θ v̂ × p . (12.9)

```

The product qpq −1 was discovered by Hamilton who failed to publish the result.
Cayley, also discovered the product and published the result in 1845 [1]. However,
Altmann notes that ‘in Cayley’s collected papers he concedes priority to Hamilton.’ [2], which was a nice gesture. However, the person who had recognised the
importance of the half-angle parameters in (12.8) before Hamilton and Cayley was
Rodrigues—who published a solution that was not seen by Hamilton, but apparently,
was seen by Cayley.
Let’s test (12.9) using the previous example where we rotated a vector p = i + k,
θ = 90◦ about the quaternion’s vector v̂ = k.
```
 
qpq −1 = 0, (1 − cos θ )(v̂ · p)v̂ + cos θ p + sin θ v̂ × p
 
= 0, (v̂ · p)v̂ + v̂ × p
= [0, (k · (i + k))k + j]
= [0, j + k]

```

which agrees with (12.6). Thus, when a unit-norm quaternion takes the form
```
     
q = cos θ2 , sin θ2 v̂

```

and a pure quaternion storing a vector to be rotated takes the form

```
p = [0, p]
```


<a id='p286'></a>
<!-- Página 286 -->

270 12 Quaternions in Space

the pure quaternion
```
p  = qpq −1

```

stores the rotated vector p . Let’s show why this product preserves the magnitude of
the rotated vector.

```
| p  | = |qp||q −1 |
= |q|| p||q −1 |
= |q|2 | p|

```

and if q is a unit-norm quaternion, |q| = 1, then | p  | = | p|.
You may be wondering what happens if the product is reversed to q −1 pq? A guess
would suggest that the rotation sequence is reversed, but let’s see what an algebraic
analysis confirms.

q −1 pq = [s, −λv̂][0, p][s, λv̂]
```
= [λv̂ · p, sp − λv̂ × p][s, λv̂]

= λs v̂ · p − λsp · v̂,

λ2 v̂ × p · v̂ + λ2 v̂ · pv̂ + s 2 p − λs v̂ × p + λsp × v̂ − λ2 v̂ × p × v̂
 
= λ2 (v̂ × p) · v̂, λ2 (v̂ · p)v̂ + s 2 p − 2λs v̂ × p − λ2 (v̂ × p) × v̂ .

```

Once again
```
(v̂ × p) · v̂ = 0

```

and
```
(v̂ × p) × v̂ = p − (p · v̂)v̂.

```

Therefore,
```
 
q −1 pq = 0, λ2 (v̂ · p)v̂ + s 2 p − 2λs v̂ × p − λ2 p + λ2 (p · v̂)v̂
   
= 0, 2λ2 (v̂ · p)v̂ + s 2 − λ2 p − 2λs v̂ × p .

```

Again, let’s make s = cos θ and λ = sin θ :
```
 
q −1 pq = 0, (1 − cos(2θ ))(v̂ · p)v̂ + cos(2θ )p − sin(2θ )v̂ × p

```

and the only thing that has changed from qpq −1 is the sign of the cross-product term,
which reverses the direction of its vector. However, we must remember to compensate
for the angle-doubling by halving θ :
```
 
q −1 pq = 0, (1 − cos θ )(v̂ · p)v̂ + cos θ p − sin θ v̂ × p . (12.10)

```

Let’s see what happens when we employ (12.10) to rotate p = i + k, 90◦ about
the quaternion’s vector v̂ = k:

<a id='p287'></a>
<!-- Página 287 -->

12.3 Quaternion Products 271

Fig. 12.5 The point z
P(0, 1, 1) is rotated 90◦ to
P  (1, 1, 0) about the y-axis
```
p=j+k


90◦
v̂ = j

x y
p =i+j

q −1 pq = [0, (k · (i + k)k) − j]
= [0, −j + k]

```

which has rotated p clockwise 90◦ about the quaternion’s vector. Therefore, the rotor
qpq −1 rotates a vector counter-clockwise, and q −1 pq rotates a vector clockwise:
```
 
qpq −1 = 0, (1 − cos θ )(v̂ · p)v̂ + cos θ p + sin θ v̂ × p
 
q −1 pq = 0, (1 − cos θ )(v̂ · p)v̂ + cos θ p − sin θ v̂ × p .

Let’s compute another example. Consider the point P(0, 1, 1) in Fig. 12.5 which
```

is to be rotated 90◦ about the y-axis. We can see that the rotated point P  has the
coordinates (1, 1, 0) which we will confirm algebraically. The point P is represented
by its position vector p in the pure quaternion

```
p = [0, p].

```

The axis of rotation is v̂ = j, and the vector to be rotated is p = j + k. Therefore,
```
 
qpq −1 = 0, (1 − cos θ )(v̂ · p)v̂ + cos θ p + sin θ v̂ × p
= [0, j · (j + k) j + j × (j + k)]
= [0, i + j]

```

and confirms that P is indeed rotated to (1, 1, 0).
Now let’s explore how this product is represented in matrix form.



12.4 Quaternions in Matrix Form

Having discovered a vector equation to represent qpq −1 , let’s continue and convert
it into a matrix. We will explore two methods: the first is a simple vectorial method
which translates the vector equation representing qpq −1 directly into matrix form.
The second method uses matrix algebra to develop a rather cunning solution.

<a id='p288'></a>
<!-- Página 288 -->

272 12 Quaternions in Space

12.4.1 Vector Method

For the vector method it is convenient to describe the unit-norm quaternion as

```
q = [s, v]
= [s, xi + yj + zk]

```

where
```
s 2 + v2 = 1

```

and the pure quaternion as

```
p = [0, p]
= [0, x p i + y p j + z p k].

```

A simple way to compute qpq −1 is to use (12.9) and substitute v for λ:
```
     
qpq −1 = 0, 2λ2 v̂ · p v̂ + s 2 − λ2 p + 2λs v̂ × p
     
= 0, 2v2 v̂ · p v̂ + s 2 − v2 p + 2vs v̂ × p .

```

Next, we substitute v for vv̂:
```
   
qpq −1 = 0, 2 (v · p) v + s 2 − v2 p + 2sv × p .

```

Finally, as we are working with unit-norm quaternions to prevent scaling

```
s 2 + v2 = 1

```

and
```
s 2 − v2 = 2s 2 − 1

```

therefore,    
```
qpq −1 = 0, 2(v · p)v + 2s 2 − 1 p + 2sv × p .

```

If we let p  = qpq −1 , which is a pure quaternion, we have

```
p  = qpq −1
= [0, p ]
   
= 0, 2(v · p)v + 2s 2 − 1 p + 2sv × p
 
p = 2(v · p)v + 2s 2 − 1 p + 2sv × p.
```


<a id='p289'></a>
<!-- Página 289 -->

12.4 Quaternions in Matrix Form 273

```

```

We  interested in the rotated vector p comprising the three terms 2(v · p)v,
 2are only
2s − 1 p and 2sv × p, which can be represented by three individual matrices and
summed together.
```
  
2(v · p)v = 2 x x p + yy p + zz p xi + yj + zk
⎡ 2 ⎤⎡ ⎤
2x 2x y 2x z xp
= ⎣ 2x y 2y 2 2yz ⎦ ⎣ y p ⎦
2x z 2yz 2z 2 zp
 2   2   2   
2s − 1 p = 2s − 1 x p i + 2s − 1 y p j + 2s 2 − 1 z p k
⎡ 2 ⎤⎡ ⎤
2s − 1 0 0 xp
=⎣ 0 2s 2 − 1 0 ⎦ ⎣ yp ⎦
0 0 2s 2 − 1 zp
     
2sv × p = 2s yz p − zy p i + zx p − x z p j + x y p − yx p k
⎡ ⎤⎡ ⎤
0 −2sz 2sy xp
= ⎣ 2sz 0 −2sx ⎦ ⎣ y p ⎦ .
−2sy 2sx 0 zp

```

Adding these matrices together:
```
⎡  2      ⎤⎡ ⎤
2 s + x 2 −  1 2 x y − sz
 2 x z + sy  xp
p = ⎣ 2x y + sz  2 s2 + y 2 − 1 2 yz − sx ⎦ ⎣ yp ⎦ (12.11)
  
2 x z − sy 2 yz + sx 2 s2 + z2 − 1 zp

```

or
```
⎡       ⎤⎡ ⎤
1 −2 y 2 + z 2 2 x y − sz  2 x z + sy  xp
p = ⎣ 2x y + sz  1 −2 x 2 + z 2 2 yz − sx  ⎦ ⎣ y p ⎦ (12.12)
2 x z − sy 2 yz + sx 1 − 2 x 2 + y2 zp

```

where
```
[0, p ] = qpq −1 .

```

Now let’s reverse the product. To compute the vector part of q −1 pq all that we have
to do is reverse the sign of 2sv × p:
```
⎡  2      ⎤⎡ ⎤
2 s + x 2 −  1 2 x y + sz
 2 x z − sy  xp
p = ⎣ 2x y − sz  2 s2 + y 2 −  1 2 yz + sx

⎦ ⎣ yp ⎦ (12.13)
2 x z + sy 2 yz − sx 2 s2 + z2 − 1 zp

```

or
```
⎡       ⎤⎡ ⎤
1 −2 y 2 + z 2 2 x y + sz  2 x z − sy  xp
p = ⎣ 2x y − sz  1 −2 x 2 + z 2 2 yz + sx  ⎦ ⎣ y p ⎦ (12.14)
2 x z + sy 2 yz − sx 1 − 2 x 2 + y2 zp
```


<a id='p290'></a>
<!-- Página 290 -->

274 12 Quaternions in Space

where
```
[0, p ] = q −1 pq.


```

Observe that (12.13) is the transpose of (12.11), and (12.14) is the transpose of
(12.12).



12.4.2 Geometric Verification

Let’s illustrate the action of (12.11) by rotating the point (0, 1, 1), 90◦ about the
y-axis, as shown in Fig. 12.6. The quaternion takes the form
```
     
q = cos θ2 , sin θ2 v̂

```

which means that θ = 90◦ and v̂ = j, therefore,
```
 
q = cos 45◦ , sin 45◦ ĵ .

```

Consequently, √ √
```
s = 22 , x = 0, y = 22 , z = 0.

```

Substituting these values in (12.11) gives
```
⎡  2      ⎤⎡ ⎤
2 s + x 2 −  1 2 x y − sz
 2 x z + sy  xp
p = ⎣ 2x y + sz  2 s2 + y 2 −  1 2 yz − sx

⎦ ⎣ yp ⎦
2 x z − sy 2 yz + sx 2 s2 + z2 − 1 zp
⎡ ⎤ ⎡ ⎤⎡ ⎤
1 001 0
⎣1⎦ = ⎣ 0 1 0⎦⎣1⎦
0 −1 0 0 1

```

where (0, 1, 1) is rotated to (1, 1, 0), which is correct.

Fig. 12.6 The point z
P(0, 1, 1) is rotated 90◦ to
P  (1, 1, 0) about the y-axis p = j + k (0, 1, 1)




```
90◦ v̂ = j
x y
p =i+j
(1, 1, 0)
```


<a id='p291'></a>
<!-- Página 291 -->

12.4 Quaternions in Matrix Form 275

So now we have a transform that rotates a point about an arbitrary axis intersecting
the origin without the problems of gimbal lock associated with Euler transforms.
Before moving on, let’s evaluate one more example. Let’s perform a 180◦ rotation
about a vector v = i + k. To begin with, we will deliberately forget to convert the v
into a unit vector, just to see what happens to the final matrix. The quaternion takes
the form      
```
q = cos θ2 , sin θ2 v̂

```

but we will use v as specified. Therefore, with θ = 180◦

```
s = 0, x = 1, y = 0, z = 1.

```

Substituting these values in (12.11) gives
```
⎡  2      ⎤⎡ ⎤
2 s + x 2 −  1 2 x y − sz
 2 x z + sy  xp
p = ⎣ 2x y + sz  2 s2 + y 2 − 1 2 yz − sx ⎦ ⎣ yp ⎦
  
2 x z − sy 2 yz + sx 2 s2 + z2 − 1 zp
⎡ ⎤⎡ ⎤
1 02 1
= ⎣ 0 −1 0 ⎦ ⎣ 0 ⎦
2 01 0

```

which looks nothing like a rotation matrix, and reminds us how important it is to
have a unit vector√to represent
```
√
the axis. Let’s repeat these calculations normalising
```

the vector to v̂ = 22 i + 22 k:
```
√ √
s = 0, x = 22 , y = 0, z = 22 .

```

Substituting these values in (12.11) gives
```
⎡  2  ⎤⎡ ⎤
2 s + x 2 − 1 2 (x y − sz) 2 (x z + sy) xp
p = ⎣ 2 (x y + sz) 2 s 2 + y 2 − 1 2 (yz − sx) ⎦ ⎣ y p ⎦
2 (x z − sy) 2 (yz + sx) 2 s 2 + z 2 − 1 zp
⎡ ⎤ ⎡ ⎤⎡ ⎤
0 0 01 1
⎣ 0 ⎦ = ⎣ 0 −1 0 ⎦ ⎣ 0 ⎦
1 1 00 0

```

which not only looks like a rotation matrix, but has a determinant of 1 and rotates
the point (1, 0, 0) to (0, 0, 1) as shown in Fig. 12.7.

<a id='p292'></a>
<!-- Página 292 -->

276 12 Quaternions in Space

Fig. 12.7 The point z
P(1, 0, 0) is rotated 180◦ to
P  (0, 0, 1) about v̂ (0, 0, 1)
```
p =k
v̂


(1, 0, 0) p=i
x y


```

12.5 Multiple Rotations

Say a vector or frame of reference is subjected to two rotations specified by q1
followed by q2 . There is a temptation to convert both quaternions to their respective
matrix and multiply the matrices together. However, this not the most efficient way
of combining the rotations. It is best to accumulate the rotations as quaternions and
then convert to matrix notation, if required.
To illustrate this, consider the pure quaternion p subjected to the first quaternion q1 :
```
q1 pq1−1

```

followed by a second quaternion q2
```
 
q2 q1 pq1−1 q2−1

```

which can be expressed as
```
(q2 q1 ) p (q2 q1 )−1 .

```

Extra quaternions can be added accordingly. Let’s illustrate this with two examples.
To keep things simple, the first quaternion q1 rotates 30◦ about the y-axis:
```
 
q1 = cos 15◦ , sin 15◦ j .

```

The second quaternion q2 rotates 60◦ also about the y-axis:
```
 
q2 = cos 30◦ , sin 30◦ j .

```

Together, the two quaternions rotate 90◦ about the y-axis. To accumulate these rotations, we multiply them together:
```
  
```

q1 q2 = cos 15◦ , sin 15◦ j cos 30◦ , sin 30◦ j
```
 
= cos 15◦ cos 30◦ − sin 15◦ sin 30◦ , cos 15◦ sin 30◦ j + cos 30◦ sin 15◦ j
√
= 22 [1, j]
```


<a id='p293'></a>
<!-- Página 293 -->

12.5 Multiple Rotations 277

which is a quaternion that rotates 90◦ about the y-axis. Using the matrix (12.11) we
have
```
⎡  2  ⎤⎡ ⎤
2 s + x 2 − 1 2 (x y − sz) 2 (x z + sy) xp
p = ⎣ 2 (x y + sz) 2 s 2 + y 2 − 1 2 (yz − sx) ⎦ ⎣ y p ⎦
2 (x z − sy) 2 (yz + sx) 2 s 2 + z 2 − 1 zp
⎡ ⎤⎡ ⎤
001 xp
= ⎣ 0 1 0 ⎦ ⎣ yp ⎦
−1 0 0 zp

```

which rotates points about the y-axis by 90◦ .
For a second example, let’s just evaluate the quaternions. The first quaternion q1
rotates 90◦ about the x-axis, and q2 rotates 90◦ about the y-axis:
```
√
q1 = 22 [1, i]
√
q2 = 22 [1, j]
p = [0, i + j].

```

Therefore,
```
√ √
q2 q1 = 22 [1, i] 22 [1, j]
= 21 [1, i + j − k]
(q2 q1 )−1 = 21 [1, −i − j + k]
(q2 q1 ) p = 21 [1, i + j − k] [0, i + j]
= 21 [−2, (i + j) + i − j]
= [−1, i]
(q2 q1 ) p(q2 q1 )−1 = 21 [−1, i] [1, −i − j + k]
= 21 [−1 + 1, i + j − k + i − j − k]
= [0, i − k] .

```

Thus the point (1, 1, 0) is rotated to (1, 0, −1), which is correct.



12.6 Rotating About an Off-Set Axis

Now that we have a matrix to represent a quaternion rotor, we can employ it to resolve
problems such as rotating a point about an off-set axis using the same techniques
associated with normal rotation transforms. We use the following notation to rotate
a point about a fixed axis parallel with the y-axis:

<a id='p294'></a>
<!-- Página 294 -->

278 12 Quaternions in Space
```
⎡ ⎤ ⎡ ⎤
x x
⎢ y ⎥ ⎢y⎥
⎢  ⎥ = T(t , 0, t ) Rβ, y T(−t , 0, −t ) ⎢ ⎥
⎣z ⎦ x z x z ⎣
z⎦
1 1
```

Therefore, by substituting the matrix qpq −1 for Rβ, y we have:
```
⎡ ⎤ ⎡ ⎤
x x
⎢ y ⎥   ⎢y⎥
⎢  ⎥ = T(t , 0, t ) qpq
⎣z ⎦ x z
−1
T(−tx , 0, −tz ) ⎢ ⎥
⎣ z ⎦.
1 1
```

Let’s test this by rotating our unit cube 90◦ about the axis intersecting vertices 4 and
6 as shown in Fig. 12.8. The unit-norm quaternion to achieve this is
```
 
q = cos 45◦ , sin 45◦ j

```

with the pure quaternion
```
p = [0, p].

```

Consequently, √ √
```
s = 22 , x = 0, y = 22 , z = 0

```

and using (12.11) in a homogeneous form we have
```
⎡  2      ⎤⎡ ⎤
2 s + x 2 − 1 2 2x y −2sz
 2 x z + sy  0 xp
⎢ 2 x y + sz 2 s + y − 1 2 yz − sx 0 ⎥ ⎢ yp ⎥
p =⎢
       ⎥⎢ ⎥
⎣ 2 x z − sy 2 yz + sx 2 s2 + z2 − 1 0 ⎦ ⎣ z p ⎦
0 0 0 1 1
⎡ ⎤⎡ ⎤
0010 xp
⎢ 0 1 0 0 ⎥ ⎢ yp ⎥
=⎢ ⎥⎢ ⎥
⎣ −1 0 0 0 ⎦ ⎣ z p ⎦ .
0001 1


(a) z (b) z
1
5 3 0
1 2
7 3
0
4 y
4 2 5
x x 6
6
y
θ = 90◦ 7


```

Fig. 12.8 The cube is rotated 90◦ about the axis intersecting vertices 4 and 6

<a id='p295'></a>
<!-- Página 295 -->

12.6 Rotating About an Off-Set Axis 279

The other two matrices are
```
⎡ ⎤
1 0 0 −1
⎢0 1 0 0⎥
T(−tx , 0, 0) = ⎢
⎣0 0 1 0⎦
⎥

000 1
⎡ ⎤
1001
⎢0 1 0 0⎥
T(tx , 0, 0) = ⎢ ⎥
⎣0 0 1 0⎦.
0001

```

Multiplying these three matrices together creates:

```
⎡ ⎤⎡ ⎤ ⎡ ⎤
0010 1 0 0 −1 0010
⎢ 0 1 0 0⎥⎢0 1 0 0⎥ ⎢ 0 1 0 0⎥
p T(−tx , 0, 0) = ⎢ ⎥⎢ ⎥ ⎢
⎣ −1 0 0 0 ⎦ ⎣ 0 0 1 0 ⎦ = ⎣ −1 0 0 1 ⎦
⎥

0001 000 1 0001
⎡ ⎤⎡ ⎤ ⎡ ⎤
1001 0010 0011
⎢0 1 0 0⎥⎢ 0 1 0 0⎥ ⎢ 0 1 0 0⎥
T(tx , 0, 0) p T(−tx , 0, 0) = ⎢ ⎥⎢ ⎥ ⎢ ⎥
⎣ 0 0 1 0 ⎦ ⎣ −1 0 0 1 ⎦ = ⎣ −1 0 0 1 ⎦
0001 0001 0001
⎡ ⎤
0011
⎢ 0 1 0 0⎥
T(tx , 0, 0) p T(−tx , 0, 0) = ⎢ ⎥
⎣ −1 0 0 1 ⎦ . (12.15)
0001

```

Although not mathematically correct, the following statement shows the matrix
(12.15) and the array of coordinates representing a unit cube, followed by the rotated
cube’s coordinates.
```
⎡ ⎤⎡ ⎤ ⎡ ⎤
0011 00001111 12121212
⎢ 0 1 0 0⎥⎢0 0 1 1 0 0 1 1⎥ ⎢0 0 1 1 0 0 1 1⎥
⎢ ⎥⎢ ⎥ ⎢ ⎥
⎣ −1 0 0 1 ⎦ ⎣ 0 1 0 1 0 1 0 1 ⎦ = ⎣ 1 1 1 1 0 0 0 0 ⎦ .
0001 11111111 11111111

```

These coordinates are confirmed by Fig. 12.8.



12.7 Converting a Rotation Matrix to a Quaternion

Very often one has a 3D rotation matrix which would be nice to see as a quaternion.
So let’s see how this can be realised. The matrix transform equivalent to qpq −1 is

<a id='p296'></a>
<!-- Página 296 -->

280 12 Quaternions in Space
```
⎡  2  ⎤⎡ ⎤
2 s + x 2 − 1 2(x y − sz)  2(x z + sy) xp
```

qpq −1 = ⎣ 2(x y + sz) 2 s 2 + y 2 − 1 2(yz − sx) 
```
⎦ ⎣ yp ⎦ (12.16)
2(x z − sy) 2(yz + sx) 2 s 2 + z 2 − 1 zp
⎡ ⎤⎡ ⎤
a11 a12 a13 xp
= ⎣ a21 a22 a23 ⎦ ⎣ y p ⎦ . (12.17)
a31 a32 a33 zp

```

Inspection of (12.16) and (12.17) shows that by combining various elements we
can isolate the terms of a quaternion s, x, y, z. For example, by adding the diagonal
terms of (12.17): a11 + a22 + a33 , we obtain
```
           
```

a11 + a22 + a33 = 2 s 2 + x 2 − 1 + 2 s 2 + y 2 − 1 + 2 s 2 + z 2 − 1
```
 
= 6s 2 + 2 x 2 + y 2 + z 2 − 3
= 4s 2 − 1

```

therefore, 
```
s = 21 1 + a11 + a22 + a33 .

```

To isolate x, y, z we employ:

```
1 
x= a32 − a23
4s
1 
y= a13 − a31
4s
1 
z= a21 − a12 .
4s


```

12.8 Summary

This chapter has shown how a quaternion is used to rotate a vector about a quaternion’s vector. It would have been useful if this could have been achieved by the
simple product qp, like complex numbers. But as we saw, this only works when the
quaternion is orthogonal to the vector. The product qpq −1 —discovered by Hamilton
and Cayley—works for all orientations between a quaternion and a vector. It is also
relatively easy to compute. We also saw that the product can be represented as a
matrix, which can be integrated with other matrices.
Perhaps one of the most interesting features of quaternions that has emerged in
this chapter, is that their imaginary qualities are not required in any calculations,
because they are embedded within the algebra.
The reverse product q −1 pq reverses the angle of rotation, and is equivalent to
changing the sign of the rotation angle in qpq −1 . Consequently, it can be used to
rotate a frame of reference in the same direction as qpq −1 .

<a id='p297'></a>
<!-- Página 297 -->

12.8 Summary 281

12.8.1 Summary of Definitions

Rotating a vector by a quaternion

```
q = [s, v]
s + v2 = 1
2

p = [0, p]
−1
   
qpq = 0, 2(v · p)v + 2s 2 − 1 p + 2sv × p .

     
q = cos θ2 , sin θ2 v̂
p = [0, p]
−1
 
qpq = 0, (1 − cos θ )(v̂ · p)v̂ + cos θ p + sin θ v̂ × p .

```

Matrix for rotating a vector by a quaternion
```
⎡   ⎤⎡ ⎤
1 − 2 y2 + z2 2(x y − sz)  2(x z + sy) xp
p = ⎣ 2(x y + sz) 1 − 2 x 2 + z 2 2(yz − sx)  ⎦ ⎣ y p ⎦ .
2(x z − sy) 2(yz + sx) 1 − 2 x 2 + y 2 zp



```

12.9 Worked Examples

Here are some further worked examples that employ the ideas described above.



12.9.1 Special Case Quaternion

Use qp to rotate p = [0, j] 90◦ about the x-axis.
For this to work q must be orthogonal to p:

```
q = [cos θ, sin θ i]
= [0, i]

```

and

```
p  = qp
= [0, i][0, j]
= [0, k].
```


<a id='p298'></a>
<!-- Página 298 -->

282 12 Quaternions in Space

12.9.2 Rotating a Vector Using a Quaternion

Use qpq −1 to rotate p = [0, j] 90◦ about the x-axis.
For this to work:
```
     
q = cos θ2 , sin θ2 i
√ √ 
= 22 , 22 i
√
= 22 [1, i]

```

and

```
p  = qpq −1
√ √
= 22 22 [1, i] [0, j] [1, −i]
= 21 [0, j + k] [1, −i]
= 21 [0, (j + k) − j + k]
= [0, k] .



```

12.9.3 Evaluate q pq −1
```
     
```

Evaluate qpq −1 for p = [0, p] and q = cos θ2 , sin θ2 v , where θ = 360◦ .


```
q = [−1, 0]
−1
qpq = [−1, 0] [0, p] [−1, 0]
 
= 0, −p [−1, 0]
 
= 0, p

```

which confirms that the vector remains unmoved, as expected.




12.9.4 Evaluate q pq −1 Using a Matrix
```
 √ 
```

Compute the matrix for q = 21 , 23 k .
From q: √
```
s = 21 , x = 0, y = 0, z = 23
```


<a id='p299'></a>
<!-- Página 299 -->

12.9 Worked Examples 283
```
⎡  2      ⎤⎡ ⎤
2 s + x 2 −  1 2 x y − sz
 2 x z + sy  xp
p = ⎣ 2x y + sz  2 s2 + y 2 −  1 2 yz − sx

⎦ ⎣ yp ⎦
2 x z − sy 2 yz + sx 2 s2 + z2 − 1 zp
⎡ √ ⎤⎡ ⎤
− 1 − 23 0 xp
⎢ √32 ⎥⎣ ⎦
=⎣ − 1
0 ⎦ yp .
2 2
0 0 1 zp

```

If we plug in the point (1, 0, 0), it is rotated about the z-axis by 120◦ :
```
⎡ ⎤ ⎡√ ⎤⎡ ⎤
−
√2
1
− 1
− 3
0 1
⎣ 3 ⎦=⎢
√2 2 ⎥⎣ ⎦
2
⎣ 3
− 1
0 ⎦ 0 .
2 2
1 0 0 1 0




```

References

1. Cayley A (1848) The collected mathematical papers, vol I, p 586, note 20
2. Altmann SL (1986) Rotations, quaternions and double groups, p 16. Dover Publications
3. Vince JA (2017) Mathematics for computer graphics, 5th edn. Springer

<a id='p300'></a>
<!-- Página 300 -->


## Chapter 13

Interpolation




13.1 Introduction

This chapter covers linear and non-linear interpolation of scalars, and includes
trigonometric and cubic polynomials. It also includes the interpolation of vectors
and quaternions.



13.2 Background

Interpolation is not a branch of mathematics but rather a collection of techniques
the reader will find useful when solving computer graphic problems. Basically, an
interpolant is a strategy for selecting a number between two limits. For example, if
the limits are 2 and 4, a parameter t can be used to select the sequence 2.0, 2.2, 2.4,
2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, and 4. These numbers could then be used to translate,
scale, rotate an object, move a virtual camera, or change the position, colour or
brightness of a virtual light source.
```
To implement the above interpolant for different limits we require a general algo-
```

rithm, which is one of the first exercises of this chapter. We also need to explore
ways of controlling the spacing between the interpolated values. In animation, for
example, we often need to move an object very slowly and gradually increase its
speed. Conversely, we may want to bring an object to a halt, making its speed less
and less. The interpolant function includes a parameter within its algorithm, which
permits any interpolated value to be created at will. The parameter can depend upon
time, or operate over a distance in space.




© Springer-Verlag London Ltd., part of Springer Nature 2022 285
J. Vince, Mathematics for Computer Graphics, Undergraduate Topics
in Computer Science, https://doi.org/10.1007/978-1-4471-7520-9_13

<a id='p301'></a>
<!-- Página 301 -->

286 13 Interpolation

13.3 Linear Interpolation

A linear interpolant generates equal spacing between the interpolated values for
equal changes in the interpolating parameter. In the above example the increment 0.2
is calculated by subtracting the first number from the second and dividing the result
by 10, i.e. (4 − 2)/10 = 0.2. Although this works, it is not in a very flexible form,
so let’s express the problem differently.
```
Given two numbers n 1 and n 2 , which represent the start and final values of the
```

interpolant, we require an interpolated value controlled by a parameter t that varies
between 0 and 1. When t = 0, the result is n 1 , and when t = 1, the result is n 2 . A
solution to this problem is given by

```
n = n 1 + t (n 2 − n 1 )

```

for when n 1 = 2, n 2 = 4 and t = 0.5:

```
n = 2 + 21 (4 − 2) = 3

```

which is a halfway point. Furthermore, when t = 0, n = n 1 , and when t = 1, n = n 2 ,
which confirms that we have a sound interpolant. However, it can be expressed
differently:
```
n = n 1 (1 − t) + n 2 t (13.1)

```

which shows what is really going on, and forms the basis for further development.
Figure 13.1 shows the graphs of n = 1 − t and n = t over the range 0 ≤ t ≤ 1.
With reference to (13.1), we see that as t changes from 0 to 1, the (1 − t) term
varies from 1 to 0. This attenuates the value of n 1 to zero over the range of t, while
the t term scales n 2 from zero to its actual value. Figure 13.2 illustrates these two
actions with n 1 = 1 and n 2 = 5.
Observe that the terms (1 − t) and t sum to unity—this is not a coincidence. This
type of interpolant ensures that if it takes a quarter of n 1 , it balances it with threequarters of n 2 , and vice versa. Obviously we could design an interpolant that takes
arbitrary portions of n 1 and n 2 , but would lead to arbitrary results.

Fig. 13.1 The graphs of 1
n = 1 − t and n = t over the
range 0 ≤ t ≤ 1
```
0.75

n n =1-t n=t
0.5



0.25



0 0.25 0.5 0.75 1
t
```


<a id='p302'></a>
<!-- Página 302 -->

13.3 Linear Interpolation 287

Fig. 13.2 The green line 5
shows the result of linearly
interpolating between 1 and 4
5 n = 5t
```
3
n =1(1-t)+5t
n
2


1
n =1(1-t)
0
0 0.25 0.5 0.75 1
t

```

Fig. 13.3 Interpolating 5
```
t=1
```

between the points (1, 1)
and (4, 5) 4
```
t=0.75
3
t=0.5
y
2
t=0.25
1
t=0
0
0 1 2 x 3 4 5



```

Although this interpolant is extremely simple, it is widely used in computer graphics software. Just to put it into context, consider the task of moving an object between
two locations (x1 , y1 , z 1 ) and (x2 , y2 , z 2 ). The interpolated position is given by
```
⎫
x = x1 (1 − t) + x2 t ⎬
y = y1 (1 − t) + y2 t 0 ≤ t ≤ 1.
⎭
z = x1 (1 − t) + z 2 t

```

The parameter t could be generated from two frame values within an animation.
What is assured by this interpolant, is that equal steps in t result in equal steps in
x, y, and z. Figure 13.3 illustrates this linear spacing with a 2D example where we
interpolate between the points (1, 1) and (4, 5). Note the equal spacing between
the intermediate interpolated points.
We can write (13.1) in matrix form as follows:
```
 
n1
n = [(1 − t) t]
n2

```

or as   
```
−1 1 n1
n = [t 1] .
10 n2

```

The reader can confirm that this generates identical results to the algebraic form.

<a id='p303'></a>
<!-- Página 303 -->

288 13 Interpolation

13.4 Non-Linear Interpolation

A linear interpolant ensures that equal steps in the parameter t give rise to equal
steps in the interpolated values; but it is often required that equal steps in t give
rise to unequal steps in the interpolated values. We can achieve this using a variety
of mathematical techniques. For example, we could use trigonometric functions or
polynomials. To begin with, let’s look at a trigonometric solution.



13.4.1 Trigonometric Interpolation

In Chap. 4 we noted that sin2 t + cos2 t = 1, which satisfies one of the requirements
of an interpolant: the terms must sum to 1. If t varies between 0 and π/2, cos2 t varies
between 1 and 0, and sin2 t varies between 0 and 1, which can be used to modify the
two interpolated values n 1 and n 2 as follows:

```
n = n 1 cos2 t + n 2 sin2 t, 0 ≤ t ≤ π2 . (13.2)

```

The interpolation curves are shown in Fig. 13.4.
If n 1 = 1 and n 2 = 3 in (13.2), we obtain the curves shown in Fig. 13.5. If we
apply this interpolant to two 2D points in space: (1, 1) and (4, 5), we obtain a


Fig. 13.4 The curves for 1
n = cos2 t and n = sin2 t
```
0.75

n n = sin2t
0.5
n = cos2t


0.25



0
0 0.25 t 0.5



```

Fig. 13.5 Interpolating 3
between 1 and 3 using a
trigonometric interpolant
```
2
n = cos2t+3sin2t

n n = 3sin2t
1

n = cos2t

0
0 0.25 t 0.5
```


<a id='p304'></a>
<!-- Página 304 -->

13.4 Non-Linear Interpolation 289

Fig. 13.6 Interpolating 5 t=1
between two points (1, 1)
```
t=0.75
```

and (4, 5) 4


```
3 t=0.5
y
2
t=0.25
1 t=0

0
0 1 2 x 3 4 5




```

straight-line interpolation, but the distribution of points is non-linear, as shown in
Fig. 13.6. In other words, equal steps in t give rise to unequal distances in space.
```
The main problem with this approach is that it is impossible to change the nature
```

of the curve—it is a sinusoid, and its slope is determined by the interpolated values.
One way of gaining control over the interpolated curve is to use a polynomial, which
is the subject of the next section.



13.4.2 Cubic Interpolation

To begin with, let’s develop a cubic blending function that will be similar to the
previous sinusoidal one. This can then be extended to provide extra flexibility. A
cubic polynomial will form the basis of the interpolant:

```
v1 = at 3 + bt 2 + ct + d

```

and the final interpolant will be of the form
```
 
n1
n = [v1 v2 ] .
n2

```

The task is to find the values of the constants associated with the polynomials v1 and
v2 . The requirements are:
1. The cubic function v2 must grow from 0 to 1 for 0 ≤ t ≤ 1.
2. The slope at a point t must equal the slope at the point (1 − t). This ensures
```
slope continuity over the range of the function.
```

3. The value v2 at any point t must also produce (1 − v2 ) at (1 − t). This ensures
```
curve continuity.
• To satisfy the first requirement:

v2 = at 3 + bt 2 + ct + d
```


<a id='p305'></a>
<!-- Página 305 -->

290 13 Interpolation

```
and when t = 0, v2 = 0 and d = 0. Similarly, when t = 1, v2 = a + b + c.
• We now need some calculus, which is described in a later chapter. To satisfy
the second requirement, differentiate v2 to obtain the slope:

dv2
= 3at 2 + 2bt + c = 3a(1 − t)2 + 2b(1 − t) + c
dt
and equating constants we discover c = 0 and 0 = 3a + 2b.
• To satisfy the third requirement:

at 3 + bt 2 = 1 − [a(1 − t)3 + b(1 − t)2 ]

where we discover 1 = a + b. But 0 = 3a + 2b, therefore a = 2 and b = 3.
Therefore,
v2 = −2t 3 + 3t 2 . (13.3)

To find the curve’s mirror curve, which starts at 1 and collapses to 0 as t moves
from 0 to 1, we subtract (13.3) from 1:

v1 = 2t 3 − 3t 2 + 1.

Therefore, the two polynomials are

v1 = 2t 3 − 3t 2 + 1 (13.4)
v2 = −2t + 3t 3 2
(13.5)

and are shown in Fig. 13.7. They are used as interpolants as follows:

n = v1 n 1 + v2 n 2

or in matrix form:
 
n
n = [2t − 3t + 1
3 2
− 2t + 3t ] 1
3 2
n2


```

Fig. 13.7 Two cubic 1
polynomials
```
0.75

n n = 2t3-3t2+1 n = -2t3+3t2
0.5



0.25



0
0 0.25 0.5 t 0.75 1
```


<a id='p306'></a>
<!-- Página 306 -->

13.4 Non-Linear Interpolation 291

Fig. 13.8 Interpolating 3
between 1 and 3 using a
cubic interpolant
```
2
n = -4t3+6t2+1
n
n = -6t3+9t2
1

n = 2t3-3t2+1

0
0 0.25 0.5 t 0.75 1




```

Fig. 13.9 A cubic 4
interpolant between points
(1, 1) and (8, 3)
```
3 t=1
t=0.8
y2
t=0.5
t=0.3
1
t=0

0
0 1 2 3 4 x 5 6 7 8 9



⎡
⎤
2 −2  
⎢ −3 3 ⎥ n 1
n = [t 3 t 2 t 1] ⎢ ⎥
⎣ 0 0 ⎦ n2 . (13.6)
1 0

If we let n 1 = 1 and n 2 = 3 we obtain the curves shown in Fig. 13.8. And if we
```

apply the interpolant to the points (1, 1) and (8, 3) we obtain the line shown in
Fig. 13.9. This interpolant can be used to blend any pair of numbers together.
```
Now let’s examine the scenario where we interpolate between two points P1 and
```

P2 , and have to arrange that the interpolated curve is tangential with a vector at
each point. Such tangent vectors forces the curve into a desired shape, as shown
in Fig. 13.11. Unfortunately, calculus is required to compute the slope of the cubic
polynomial, which is covered in a later chapter.
```
As this interpolant can be applied to 2D and 3D points, P1 and P2 are repre-
```

sented by their position vectors P1 and P2 , which are unpacked for each Cartesian
component.
```
We now have two position vectors P1 and P2 and their respective tangent vectors
```

s1 and s2 . The requirement is to modulate the interpolating curve in Fig. 13.8 with
two further cubic curves. One that blends out the tangent vector s1 associated with
P1 , and the other that blends in the tangent vector s2 associated with P2 . Let’s begin
with a cubic polynomial to blend s1 to zero:

<a id='p307'></a>
<!-- Página 307 -->

292 13 Interpolation

```
vout = at 3 + bt 2 + ct + d.

```

vout must equal zero when t = 0 and t = 1, otherwise it will disturb the start and end
values. Therefore d = 0, and
```
a + b + c = 0.

```

The rate of change of vout relative to t (i.e. dvout /dt) must equal 1 when t = 0, so it
can be used to multiply s1 . When t = 1, dvout /dt must equal 0 to attenuate any trace
of s1 :
```
dvout
= 3at 2 + 2bt + c
dt
```

but dvout /dt = 1 when t = 0, and dvout /dt = 0 when t = 1. Therefore, c = 1, and

```
3a + 2b + 1 = 0.

```

Using (13.6) implies that b = −2 and a = 1. Therefore, the polynomial vout has the
form
```
vout = t 3 − 2t 2 + t. (13.7)

```

Using a similar argument, one can prove that the function to blend in s2 equals

```
vin = t 3 − t 2 . (13.8)

```

Graphs of (13.4), (13.5), (13.7) and (13.8) are shown in Fig. 13.10.
The complete interpolating function looks like
```
⎤
⎡
```


## P1


## ⎢ P2 ⎥

```
n = [2t 3 − 3t 2 + 1 − 2t 3 + 3t 2 t 3 − 2t 2 + t t 3 − t 2 ] ⎢ ⎥
⎣ s1 ⎦
s2

```

and unpacking the constants and polynomial terms we obtain


Fig. 13.10 The four 1
Hermite interpolating curves
```
0.75

n n = 2t3-3t2+1 n = -2t3+3t2
0.5


0.25
vout = t3-2t2+t

0
0 0.25 0.5 t 0.75 1
vin = t3-t2
```


<a id='p308'></a>
<!-- Página 308 -->

13.4 Non-Linear Interpolation 293
```
⎡ ⎤⎡ ⎤
```


## 2 −2 1 1 P1


## ⎢ −3 3 −2 −1 ⎥ ⎢ P2 ⎥

```
1] ⎢ ⎥⎢ ⎥
n = [t 3 t 2 t 1 ⎣ 0 0 1 0 ⎦ ⎣ s1 ⎦ .
1 0 0 0 s2

This type of interpolation is called Hermite interpolation, after the French math-
```

ematician Charles Hermite (1822–1901). Hermite also proved in 1873 that e is transcendental.
```
Now let’s illustrate Hermite interpolation with a 2D example. It is also very easy
```

to implement the same technique in 3D. Figure 13.11 shows how two points (0, 0)
and (1, 1) are to be connected by a cubic curve that responds to the initial and final
tangent vectors. At the start point (0, 0) the tangent vector is [−5 0]T , and at the
final point (1, 1) the tangent vector is [0 − 5]T . The x and y interpolants are
```
⎡ ⎤⎡ ⎤
2 −2 1 1 0
⎢ −3 3 −2 −1 ⎥ ⎢ 1 ⎥
x = [t 3 t 2 t 1 1] ⎢ ⎥⎢
⎣ 0 0 1 0 ⎦ ⎣ −5 ⎦
⎥

1 0 0 0 0
⎡ ⎤⎡ ⎤
2 −2 1 1 0
⎢ −3 3 −2 −1 ⎥ ⎢ 1 ⎥
y = [t 3 t 2 t 1 1] ⎢ ⎥⎢ ⎥
⎣ 0 0 1 0⎦⎣ 0⎦
1 0 0 0 −5

```

which become
```
⎡ ⎤
−7
⎢ 13 ⎥
x = [t 3 t 2 t 1 1] ⎢ ⎥
⎣ −5 ⎦ = −7t + 13t − 5t
3 2


0
⎡ ⎤
−7
⎢ 8⎥
y = [t 3 t 2 t 1 1] ⎢ ⎥
⎣ 0 ⎦ = −7t + 8t .
3 2


0

```

Fig. 13.11 A Hermite curve y
between the points (0, 0)
```
1.5
```

and (1, 1) with tangent
vectors [−5 0]T and
[0 − 5]T not drawn to scale
```
1

[0 -5]
0.5



0
[-5 0]
-0.5 0 0.5 1 x
```


<a id='p309'></a>
<!-- Página 309 -->

294 13 Interpolation

When these polynomials are plotted over the range 0 ≤ t ≤ 1 we obtain the curve
shown in Fig. 13.11
We have now reached a point where we are starting to discover how parametric polynomials can be used to generate space curves, which is the subject of the
next chapter. So, to conclude this chapter on interpolants, we will take a look at
interpolating vectors.



13.5 Interpolating Vectors

So far we have been interpolating between a pair of numbers. Now the question
arises: can we use the same interpolants for vectors? We can if we interpolate both
the magnitude and direction of a vector. However, if we linearly interpolate only the
x- and y-components of two vectors, the in-between vectors would neither respect
their orientation nor their magnitude. But if we defined two 2D vectors as l1 , θ1 and
l2 , θ2 , where l is the magnitude and θ the rotated angle, then a linearly interpolated
vector is given by

```
l = l1 (1 − t) + l2 t
θ = θ1 (1 − t) + θ2 t

```

and the x- and y-components of the interpolated vector are:

```
l x = l cos θ
l y = l sin θ.

```

Figure 13.12 shows the trace of interpolating between vector 2, 45◦ and vector
3, 135◦ . The half-way point, when t = 0.5, generates the vector 2.5, 90◦ . The same
technique can be used with 3D vectors using the equivalent polar notation.
We can interpolate between x- y- and z-coordinates if we respect the magnitude
and orientation of the encoded vectors using the following technique. Figure 13.13


Fig. 13.12 The trace of 3 y
interpolating between
vectors 2, 45◦ and 3, 135◦ t = 0.5
```
2.5, 90

2

3, 135


1
2, 45




-2.5 -2 -1.5 -1 -0.5 0 0.5 1 1.5 2 2.5
x
```


<a id='p310'></a>
<!-- Página 310 -->

13.5 Interpolating Vectors 295

Fig. 13.13 Vector v is v2
derived from part a of of v1
and part b of v2



```
v
n
)θ
−t
(1
m b

θ tθ θ
a v1



```

shows two unit vectors v1 and v2 separated by an angle θ . The interpolated vector v
is defined as a proportion of v1 and a proportion of v2 :

```
v = av1 + bv2 .

```

Let’s define the values of a and b such that they are a function of the separating angle
θ . Vector v is tθ from v1 and (1 − t)θ from v2 , and it is evident from Fig. 13.13 that
using the sine rule
```
a b
= (13.9)
sin[(1 − t)θ ] sin(tθ )

```

and furthermore:

```
m = a cos(tθ )
n = b cos[(1 − t)θ ]

```

where
```
m + n = 1. (13.10)

```

From (13.9)
```
a sin(tθ )
b=
sin[(1 − t)θ ]

```

and from (13.10) we get

```
a sin(tθ ) cos[(1 − t)θ ]
a cos(tθ ) + = 1.
sin[(1 − t)θ ]

```

Solving for a we find

```
sin[(1 − t)θ ]
a=
sin θ
```


<a id='p311'></a>
<!-- Página 311 -->

296 13 Interpolation

```
sin(tθ )
b= .
sin θ
```

Therefore, the final interpolant is

```
sin[(1 − t)θ ] sin(tθ )
v= v1 + v2 . (13.11)
sin θ sin θ
```

To see how (13.11) operates, let’s consider √ a simple
```
√ exercise of interpolating
```

between two unit vectors [1 0]T and [−1/ 2 1/ 2]T . The angle between the
vectors θ is 135◦ . Equation (13.11) is used to interpolate the x- and the y-components
individually:

```
sin[(1 − t)135◦ ] sin(t135◦ ) 
vx = × (1) + × − √1
sin 135◦ sin 135◦ 2
sin[(1 − t)135◦ ] sin(t135◦ )
vy = × (0) + × √12 .
sin 135◦ sin 135◦
```

Figure 13.14 shows the interpolating curves and Fig. 13.15 shows a trace of the
interpolated vectors.
Two observations to note with (13.11):
• The angle θ is the angle between the two vectors, which, if not known, can be
computed using the dot product.
• Secondly, the range of θ is given by 0 ≤ θ ≤ 180◦ , but when θ = 180◦ the denominator collapses to zero.
```
So far, we have only considered unit vectors. Now let’s see how the interpolant
```

reacts to vectors of different magnitudes. As a test, we can input the following vectors
to (13.11):
```
v1 = [2 0]T , and v2 = [0 1]T .




1
vx
v vy
0.5




0 0.5 t 1


-0.5



```

Fig. 13.14 Curves of vx and v y using (13.11)

<a id='p312'></a>
<!-- Página 312 -->

13.5 Interpolating Vectors 297

```
y
1 t = 0.5

0.75


3, 135 0.5

0.25
2, 45
0
-0.75 -0.5 -0.25 0.25 0.5 0.75 1 x
√ √
```

Fig. 13.15 A trace of the interpolated vectors [1 0]T and [−1/ 2 1/ 2]T


```
y
1

[0 1]T t = 0.5

0.5



```


## [2 0]T

```
0
0.5 1 1.5 2 x

```

Fig. 13.16 Interpolating between the vectors [2 0]T and [0 1]T


The separating angle θ = 90◦ , and the result is shown in Fig. 13.16. Note how the
initial length of v1 reduces from 2 to 1 over 90◦ . It is left to the reader to examine
other combinations of vectors. There is one more application for this interpolant, and
that is with quaternions.



13.6 Interpolating Quaternions

It just so happens that the interpolant used for vectors also works with quaternions.
Which means that, given two quaternions q1 and q2 , the interpolated quaternion q is
given by
```
sin[(1 − t)θ ] sin(tθ )
q= q1 + q2 . (13.12)
sin θ sin θ
```

The interpolant is applied individually to the four terms of the quaternion.
When interpolating vectors, θ is the angle between the two vectors. If this is not
known, it can be derived using the dot product formula:

<a id='p313'></a>
<!-- Página 313 -->

298 13 Interpolation

```
v1 · v2
cos θ =
v1 v2 
x1 x2 + y1 y2 + z 1 z 2
= .
v1 v2 

```

Similarly, when interpolating quaternions, θ is computed by taking the 4-D dot
product of the two quaternions:
```
q1 · q2
cos θ =
|q1 ||q2 |
s1 s2 + x1 x2 + y1 y2 + z 1 z 2
= .
|q1 ||q2 |

```

If we are using unit quaternions

```
cos θ = s1 s2 + x1 x2 + y1 y2 + z 1 z 2 . (13.13)

```

We are now in a position to demonstrate how to interpolate between a pair of quaternions. For example, say we have two quaternions q1 and q2 that rotate 0◦ and 90◦
about the z-axis respectively:
```
  ◦  ◦ 
q1 = cos 02 , sin 02 (0i + 0j + 1k)
  ◦  ◦ 
q1 = cos 902 , sin 902 (0i + 0j + 1k)

```

which become

```
q1 = [1, 0i + 0j + 0k]
q2 ≈ [0.7071, 0i + 0j + 0.7071k].

```

Any interpolated quaternion is found by the application of (13.12). But first, we
need to find the value of θ using (13.13):

```
cos θ ≈ 0.7071
θ = 45◦ .

```

Now when t = 0.5, the interpolated quaternion is given by

```
sin(45◦ /2) sin(45◦ /2)
```

q≈ [1, 0i + 0j + 0k] + [0.7071, 0i + 0j + 0.7071k]
```
sin 45◦ sin 45◦
≈ 0.541196[1, 0i + 0j + 0k] + 0.541196[0.7071, 0i + 0j + 0.7071k]
≈ [0.541196, 0i + 0j + 0k] + [0.382683, 0i + 0j + 0.382683k]
≈ [0.923879, 0i + 0j + 0.382683k].
```


<a id='p314'></a>
<!-- Página 314 -->

13.6 Interpolating Quaternions 299

Although it is not obvious, this interpolated quaternion is also a unit quaternion,
as the square root of the sum of the squares is 1. It should rotate a point about the
z-axis, halfway between 0◦ and 90◦ , i.e. 45◦ . We can test that this works with a simple
example.
Take the point (1, 0, 0) and subject it to the standard quaternion operation:

```
P = qPq−1 .

```

To keep the arithmetic work to a minimum, we substitute a = 0.923879 and b =
0.382683. Therefore,

```
q = [a, 0i + 0j + bk]
−1
q = [a, −0i − 0j − bk]

P = [a, 0i + 0j + bk][0, 1i + 0j + 0k][a, −0i − 0j − bk]
= [0, ai + bj + 0k][a, −0i − 0j − bk]
= [0, (a 2 − b2 )i + 2abj + 0k]

P ≈ [0, 0.7071i + 0.7071j + 0k].

```

Therefore, (1, 0, 0) is rotated to (0.7071, 0.7071, 0), which is correct!



13.7 Summary

This chapter has covered some very interesting, yet simple ideas about changing one
number into another. In the following chapter we will develop these ideas and see
how we design algebraic solutions to curves and surfaces.

<a id='p315'></a>
<!-- Página 315 -->


## Chapter 14

Curves and Patches




14.1 Introduction

In this chapter we investigate the foundations of curves and surface patches. This is a
very large and complex subject and it will be impossible to delve too deeply. However,
we can explore many of the ideas that are essential to understanding the mathematics
behind 2D and 3D curves and how they are developed to produce surface patches.
Once you have understood these ideas you will be able to read more advanced texts
and develop a wider knowledge of the subject.



14.2 Background

Two people, working for competing French car manufacturers, are associated with
what are now called Bézier curves: the French physicist and mathematician Paul de
Casteljau (1930–), who worked for Citröen, and the French engineer Pierre Bézier
(1910–1999), who worked for Rénault. De Casteljau’s work was slightly ahead of
Bézier’s, but because of Citröen’s policy of secrecy it was never published, so Bézier’s
name has since been associated with the theory of polynomial curves and surfaces.
Casteljau started his research work in 1959, but his reports were only discovered in
1975, by which time Bézier had become known for his special curves and surfaces.
In the previous chapter we saw how polynomials are used as interpolants and
blending functions. We will now see how these form the basis of parametric curves
and patches. To begin with, let’s start with the humble circle.




© Springer-Verlag London Ltd., part of Springer Nature 2022 301
J. Vince, Mathematics for Computer Graphics, Undergraduate Topics
in Computer Science, https://doi.org/10.1007/978-1-4471-7520-9_14

<a id='p316'></a>
<!-- Página 316 -->

302 14 Curves and Patches

Fig. 14.1 The circle is y
drawn by tracing out a series
of points on the
circumference
```
r
y
t
x x




```

14.3 The Circle

The circle has a very simple equation:

```
x 2 + y2 = r 2

```

where r is the radius and (x, y) is a point on the circumference. Although this
equation has its uses, it is not very convenient for drawing the curve. What we really
want are two functions that generate the coordinates of any point on the circumference
in terms of some parameter t. Figure 14.1 shows a scenario where the x- and ycoordinates are given by
```

x = r cos t
0 ≤ t ≤ 2π.
y = r sin t

```

By varying the parameter t over the range 0 to 2π , we trace out the curve of the
circumference. In fact, by selecting a suitable range of t we can isolate any portion
of the circle’s circumference.



14.4 The Ellipse

The equation for an ellipse is
```
x2 y2
2
+ 2
=1
rma j rmin

```

and its parametric form is
```

x = rma j cos t
0 ≤ t ≤ 2π
y = rmin sin t
```


<a id='p317'></a>
<!-- Página 317 -->

14.4 The Ellipse 303

Fig. 14.2 An ellipse y
showing the major and minor
radii
```
rmin


rmax x




```

where rma j and rmin are the major and minor radii respectively, and (x, y) is a
point on the circumference, as shown in Fig. 14.2. We now examine a very useful
parametric curve called a Bézier curve.



14.5 Bézier Curves

14.5.1 Bernstein Polynomials

Bézier curves employ Bernstein polynomials which were described by the Russian
mathematician Sergei Bernstein (1880–1968) in 1912. They are expressed as follows:
```
 
n i
Bin (t) = t (1 − t)n−i (14.1)
i
 
n
```

where is shorthand for the number of selections of i different items from n
```
i
```

distinguishable items when the order of selection is ignored, and equals
```
 
n n!
= (14.2)
i (n − i)!i!

```

where, for example, 3! (factorial 3) is shorthand for 3 × 2 × 1. When (14.2) is evaluated for different values of i and n, we discover the pattern of numbers shown in Table
14.1. This pattern of numbers is known as Pascal’s triangle. In western countries
they are named after a 17th century French mathematician, even though they had
been described in China as early as 1303 in Precious Mirror of the Four Elements by
the Chinese mathematician Chu Shih-chieh. The pattern represents the coefficients
found in binomial expansions. For example, the expansion of (x + a)n for different
values of n is

<a id='p318'></a>
<!-- Página 318 -->

304 14 Curves and Patches

Table 14.1 Pascal’s triangle
n i
```
0 1 2 3 4 5 6
```

0 1
1 1 1
2 1 2 1
3 1 3 3 1
4 1 4 6 4 1
5 1 5 10 10 5 1
6 1 6 15 20 15 6 1



Table 14.2 Expansion of the terms t and (1 − t)
n i
```
0 1 2 3 4
```

1 t (1 − t)
2 t2 t (1 − t) (1 − t)2
3 t3 t 2 (1 − t) t (1 − t)2 (1 − t)3
4 t4 t 3 (1 − t) t 2 (1 − t)2 t (1 − t)3 (1 − t)4




```
(x + a)0 = 1
(x + a)1 = 1x + 1a
(x + a)2 = 1x 2 + 2ax + 1a 2
(x + a)3 = 1x 3 + 3ax 2 + 3a 2 x + 1a 3
(x + a)4 = 1x 4 + 4ax 3 + 6a 2 x 2 + 4a 3 x + 1a 4
 
n
```

which reveal Pascal’s triangle as coefficients of the polynomial terms. Thus the
```
i
```

term in (14.1) is nothing more than a generator for Pascal’s triangle. The powers of
t and (1 − t) in (14.1) appear as shown in Table 14.2 for different values of n and i.
When the two sets of results are combined we get the complete Bernstein polynomial
terms shown in Table 14.3. One very important property of these terms is that they
sum to unity, which is an important feature of any interpolant.
The sum of (1 − t) and t is 1, therefore,

```
[(1 − t) + t]n = 1 (14.3)

```

which is why we can use the binomial expansion of (1 − t) and t as interpolants. For
example, when n = 2 we obtain the quadratic form:

<a id='p319'></a>
<!-- Página 319 -->

14.5 Bézier Curves 305

Table 14.3 The Bernstein polynomial terms
n i
```
0 1 2 3 4
```

1 1t 1(1 − t)
2 1t 2 2t (1 − t) 1(1 − t)2
3 1t 3 3t 2 (1 − t) 3t (1 − t)2 1(1 − t)3
4 1t 4 4t 3 (1 − t) 6t 2 (1 − t)2 4t (1 − t)3 1(1 − t)4



Fig. 14.3 Graphs of the v
quadratic Bernstein 1
polynomials
```
0.75 v = (1-t)2 v = t2

v = 2t(1-t)
0.5



0.25



0
0 0.25 0.5 0.75 1 t



(1 − t)2 + 2t (1 − t) + t 2 = 1. (14.4)

```

Figure 14.3 shows the graphs of the three polynomial terms of (14.4). The (1 − t)2
graph starts at 1 and decays to zero, whereas the t 2 graph starts at zero and rises to
1. The 2t (1 − t) graph starts at zero reaches a maximum of 0.5 and returns to zero.
Thus the central polynomial term has no influence at the end conditions, where t = 0
and t = 1. We can use these three terms to interpolate between a pair of values as
follows:
```
v = v1 (1 − t)2 + 2t (1 − t) + v2 t 2 .

```

If v1 = 1 and v2 = 3 we obtain the curve shown in Fig. 14.4. However, there is
nothing preventing us from multiplying the middle term 2t (1 − t) by any arbitrary
number vc :
```
v = v1 (1 − t)2 + vc 2t (1 − t) + v2 t 2 . (14.5)

```

For example, if vc = 3, we obtain the graph shown in Fig. 14.5, which is totally
different to the curve in Fig. 14.4. As Bézier observed, the value of vc provides an
excellent mechanism for determining the rate of change between two values. Figure
14.6 shows a variety of graphs for different values of vc . A very interesting effect
occurs when the value of vc is set midway between v1 and v2 . For example, when
v1 = 1, v2 = 3 and vc = 2, we obtain linear interpolation between v1 and v2 , as
shown in Fig. 14.5.

<a id='p320'></a>
<!-- Página 320 -->

306 14 Curves and Patches

Fig. 14.4 Bernstein v
interpolation between the
```
3
```

values 1 and 3


```
2
v = (1-t)2+2t(1-t)+3t2


1



0
0 0.25 0.5 0.75 1 t

```

Fig. 14.5 Bernstein v
interpolation between the
```
3
```

values 1 and 3 with vc = 3

```
2
v = (1-t)2+6t(1-t)+3t2

1



0
0 0.25 0.5 0.75 1 t

```

Fig. 14.6 Bernstein v
interpolation between the
```
3 4
```

values 1 for different values vc=
```
= 3
```

of vc vc
```
2
2 vc=
1
vc=
0
vc=
1



0
0 0.25 0.5 0.75 1 t



```

14.5.2 Quadratic Bézier Curves

Quadratic Bézier curves are formed by using Bernstein polynomials to interpolate
between the x-, y- and z-coordinates associated with the start- and end-points forming
the curve. For example, we can draw a 2D quadratic Bézier curve between (1, 1)
and (4, 3) using the following equations:

<a id='p321'></a>
<!-- Página 321 -->

14.5 Bézier Curves 307

Fig. 14.7 Quadratic Bézier y
curve between (1, 1) and 4
(4, 3), with (3, 4) as the
control vertex 3


```
2


1


0
0 1 2 3 4 x



x = 1(1 − t)2 + xc 2t (1 − t) + 4t 2 (14.6)
y = 1(1 − t) + yc 2t (1 − t) + 3t .
2 2
(14.7)

```

But what should be the values of (xc , yc )? Well, this is entirely up to us; the position
of this control vertex determines how the curve moves between (1, 1) and (4, 3).
```
A Bézier curve possesses interpolating and approximating qualities: the interpo-
```

lating feature ensures that the curve passes through the end points, while the approximating feature shows how the curve passes close to the control point. To illustrate
this, if we make xc = 3 and yc = 4 we obtain the curve shown in Fig. 14.7, which
shows how the curve intersects the end-points, but misses the control point. It also
highlights two important features of Bézier curves: the convex hull property, and the
end slopes of the curve.
```
The convex hull property implies that the curve is always contained within the
```

polygon connecting the start, end and control points. In this case the curve is inside
the triangle formed by the vertices (1, 1), (3, 4) and (4, 3). The slope of the curve
at (1, 1) is equal to the slope of the line connecting the start point to the control point
(3, 4), and the slope of the curve at (4, 3) is equal to the slope of the line connecting
the control point (3, 4) to the end point (4, 3). Naturally, these two qualities of
Bézier curves can be proved mathematically.



14.5.3 Cubic Bernstein Polynomials

Before moving on, there are two further points to note:
• No restrictions are placed upon the position of (xc , yc )—it can be anywhere.
• Simply including z-coordinates for the start, end and control vertices creates 3D
curves.
One of the drawbacks with quadratic curves is that they are perhaps, too simple.
If we want to construct a complex curve with several peaks and valleys, we would
have to join together a large number of such curves. A cubic curve, on the other

<a id='p322'></a>
<!-- Página 322 -->

308 14 Curves and Patches

hand, naturally supports one peak and one valley, which simplifies the construction
of more complex curves.
When n = 3 in (14.3) we obtain the following terms:

```
[(1 − t) + t]3 = (1 − t)3 + 3t (1 − t)2 + 3t 2 (1 − t) + t 3

```

which can be used as a cubic interpolant, as

```
v = v1 (1 − t)3 + vc1 3t (1 − t)2 + vc2 3t 2 (1 − t) + v2 t 3 .

```

Once more, the terms sum to unity, and the convex hull and slope properties also
hold. Figure 14.8 shows the graphs of the four polynomial terms.
This time we have two control values vc1 and vc2 . These are set to any value,
independent of the values chosen for v1 and v2 . To illustrate this, let’s consider an
example of blending between values 1 and 3, with vc1 and vc2 set to 2.5 and −2.5
respectively. The blending curve is shown in Fig. 14.9.
The next step is to associate the blending polynomials with x- and y-coordinates:

```
x = x1 (1 − t)3 + xc1 3t (1 − t)2 + xc2 3t 2 (1 − t) + x2 t 3 (14.8)
y = y1 (1 − t) + yc1 3t (1 − t) + yc2 3t (1 − t) + y2 t .
3 2 2 3
(14.9)


```

Fig. 14.8 The cubic v
Bernstein polynomial curves 1


```
0.75 v = (1-t)3 v = t3

0.5 v = 3t(1-t)2 v = 3t2(1-t)

0.25


0
0 0.25 0.5 0.75 1 t

```

Fig. 14.9 The cubic v
Bernstein polynomial 3
through the values 1, 2.5,
–2.5, 3
```
2



1



0
0 0.25 0.5 0.75 1 t
```


<a id='p323'></a>
<!-- Página 323 -->

14.5 Bézier Curves 309

Fig. 14.10 A cubic Bézier y
curve
```
3

2

1


0 1 2 3 4 x
-1

-2




```

Evaluating (14.8) and (14.9) with the following points:

```
(x1 , y1 ) = (1, 1), (x2 , y2 ) = (4, 3)
(xc1 , yc1 ) = (2, 3), (xc2 , yc2 ) = (3, −2)

```

we obtain the cubic Bézier curve shown in Fig. 14.10, which also shows the guidelines
between the end and control points.
Just to show how consistent Bernstein polynomials are, let’s set the values to

```
(x1 , y1 ) = (1, 1), (x2 , y2 ) = (4, 3)
(xc1 , yc1 ) = (2, 1.666), (xc2 , yc2 ) = (3, 2.333)

```

where (xc1 , yc1 ) and (xc2 , yc2 ) are points one-third and two-thirds respectively,
between the start and final values. As we found in the quadratic case, where the
single control point was halfway between the start and end values, we obtain linear
interpolation as shown in Fig. 14.11.
As mathematicians are interested in expressing a formula succinctly, there is
an elegant way of abbreviating Bernstein polynomials. Equations (14.6) and (14.7)
describe the three polynomial terms for generating a quadratic Bézier curve and
(14.8) and (14.9) describe the four polynomial terms for generating a cubic Bézier


Fig. 14.11 A cubic Bézier y
line
```
3



2



1



0
0 1 2 3 4 x
```


<a id='p324'></a>
<!-- Página 324 -->

310 14 Curves and Patches

curve. To begin with, quadratic equations are called second-degree equations, and
cubics are called third-degree equations. In the original Bernstein formulation:
```
 
n i
Bin (t) = t (1 − t)n−i
i

```

n represents the degree of the polynomial, and i, which has values between 0 and n,
creates the individual polynomial terms. These terms are then used to multiply the
coordinates of the end and control points. If these points are stored as a vector P, the
position vector p(t) for a point on the curve is written:
```
n  
 n
p(t) = t i (1 − t)n−i Pi , 0≤i ≤n (14.10)
i=0
i

```

or
```

n
p(t) = Bin (t)Pi , 0 ≤ i ≤ n. (14.11)
i=0


```

For example, a point p(t) on a quadratic curve is represented by

```
p(t) = 1t 0 (1 − t)2 P0 + 2t 1 (1 − t)1 P1 + 1t 2 (1 − t)0 P2 .

```

You will discover (14.10) and (14.11) used in more advanced texts to describe Bézier
curves. Although they initially appear intimidating, you should now find them relatively easy to understand.



14.6 A Recursive Bézier Formula

Note that (14.10) explicitly describes the polynomial terms needed to construct the
blending terms. With the use of recursive functions (a recursive function is a function
that calls itself), it is possible to arrive at another formulation
```
 that
 leads towards an
n
```

understanding of B-splines. To begin, we need to express in terms of lower
```
i
```

terms, and because the coefficients of any row in Pascal’s triangle are the sum of the
two coefficients immediately above, we can write
```
     
n n−1 n−1
= + .
i i i −1
```


<a id='p325'></a>
<!-- Página 325 -->

14.6 A Recursive Bézier Formula 311

Therefore, we can write:
```
   
n−1 i n−1 i
Bin (t) = t (1 − t)n−i + t (1 − t)n−i
i i −1
Bin (t) = (1 − t)Bin−1 (t) + t Bi−1
n−1
(t).

```

As with all recursive functions, some condition must terminate the process; in this
case, it is when the degree is zero. Consequently, B00 (t) = 1 and B nj (t) = 0 for j < 0.



14.7 Bézier Curves Using Matrices

As we have already seen, matrices provide a very compact notation for algebraic
formulae. So let’s see how Bernstein polynomials lend themselves to this form of
notation. Recall (14.4) which defines the three terms associated with a quadratic
Bernstein polynomial. These are expanded to

```
1 − 2t + t 2 , 2t − 2t 2 , t 2

```

and written as the product:
```
⎡ ⎤
2  1 −2 1
t t 1 ⎣ −2 2 0 ⎦ .
1 00

```

This means that (14.5) can be written:
```
⎡ ⎤⎡ ⎤
2  1 −2 1 v1
v = t t 1 ⎣ −2 2 0 ⎦ ⎣ vc ⎦
1 00 v2

```

or ⎡ ⎤⎡ ⎤

## 2  1 −2 1 P1

```
p(t) = t t 1 ⎣ −2 2 0 ⎦ ⎣ Pc ⎦
```


## 1 00 P2


where p(t) points to any point on the curve, and P1 , Pc and P2 point to the start,
control and end points respectively.
A similar development is used for a cubic Bézier curve, which has the following
matrix formulation:

<a id='p326'></a>
<!-- Página 326 -->

312 14 Curves and Patches

Fig. 14.12 Linearly
interpolating between several
values
```
v0 v1 v2



t0 t1 t2 t3 t4


⎡ ⎤⎡ ⎤
```


## −1 3 −3 1 P1

```
  ⎢ 3 −6 3 0 ⎥ ⎢ Pc1 ⎥
t 1 ⎢ ⎥⎢ ⎥
p(t) = t 3 t 2 ⎣ −3 3 0 0 ⎦ ⎣ Pc2 ⎦ .
```


## 1 0 00 P2


```
There is no doubt that Bézier curves are very useful, and they find their way into
```

all sorts of applications. But, perhaps their one weakness is that whenever an end or
control vertex is repositioned, the entire curve is modified. So let’s examine another
type of curve that prevents this from happening—B-splines. But before we consider
this form, let’s revisit linear interpolation between multiple values.



14.7.1 Linear Interpolation

To interpolate linearly between two numbers v0 and v1 , we use the following interpolant:
```
v(t) = v0 (1 − t) + v1 t, 0 ≤ t ≤ 1.

```

But say we have to interpolate continuously between three values on a linear basis, i.e.
v0 , v1 , v2 , with the possibility of extending the technique to any number of values.
One solution is to use a sequence of parameter values t1 , t2 , t3 that are associated
with the given values of v, as shown in Fig. 14.12. For the sake of symmetry:
```
v0 is associated with the parameter range t0 to t2 ,
v1 is associated with the parameter range t1 to t3 ,
v2 is associated with the parameter range t2 to t4 .
```

This sequence of parameters is called a knot vector. The only assumption we make
about the knot vector is that t0 ≤ t1 ≤ t2 ≤, etc.
Now let’s invent a linear blending function Bi1 (t) whose subscript i is used to
reference values in the knot vector. We want to use the blending function to compute
the influence of the three values on any interpolated value v(t) as follows:

```
v(t) = B01 (t)v0 + B11 (t)v1 + B21 (t)v2 . (14.12)
```


<a id='p327'></a>
<!-- Página 327 -->

14.7 Bézier Curves Using Matrices 313

It’s obvious from this arrangement that v0 will influence v(t) only when t is between
t0 and t2 . Similarly, v1 and v2 will influence v(t) only when t is between t1 and t3 ,
and t2 and t4 respectively.
```
To understand the action of the blending function let’s concentrate upon one
```

particular value B11 (t). When t is less than t1 or greater than t3 , the function B11 (t) must
be zero. When t1 ≤ t ≤ t3 , the function must return a value reflecting the proportion
of v1 that influences v(t). During the span t1 ≤ t ≤ t2 , v1 has to be blended in, and
during the span t1 ≤ t ≤ t3 , v1 has to be blended out. The blending in is effected by
the ratio  
```
t − t1
t2 − t1

```

and the blending out is effected by the ratio
```
 
t3 − t
.
t3 − t2

```

Thus B11 (t) has to incorporate both ratios, but it must ensure that they only become
active during the appropriate range of t. Let’s remind ourselves of this requirement
by subscripting the ratios accordingly:
```
   
t − t1 t3 − t
B11 (t) = + .
t2 − t1 1,2 t3 − t2 2,3


```

We can now write the other two blending terms B01 (t) and B21 (t) as
```
   
t − t0 t2 − t
B01 (t) = +
t1 − t0 0,1 t2 − t1 1,2
   
t − t2 t4 − t
B21 (t) = + .
t3 − t2 2,3 t4 − t3 3,4

```

You should be able to see a pattern linking the variables with their subscripts, and
the possibility of writing a general linear blending term Bi1 (t) as
```
   
t − ti ti+2 − t
Bi1 (t) = + .
ti+1 − ti i,i+1 ti+2 − ti+1 i+1,i+2

```

This enables us to write (14.12) in a general form as

```

2
v(t) = Bi1 (t)vi .
i=0
```


<a id='p328'></a>
<!-- Página 328 -->

314 14 Curves and Patches

But there is still a problem concerning the values associated with the knot vector.
Fortunately, there is an easy solution. One simple approach is to keep the differences
between t1 , t2 and t3 whole numbers, e.g. 0, 1 and 2. But what about the end conditions
t0 and t4 ? To understand the resolution of this problem let’s examine the action of
the three terms over the range of the parameter t. The three terms are
```
    
t − t0 t2 − t
+ v0 (14.13)
t1 − t0 0,1 t2 − t1 1,2
    
t − t1 t3 − t
+ v1 (14.14)
t2 − t1 1,2 t3 − t2 2,3

    
t − t2 t4 − t
+ v2 (14.15)
t3 − t2 2,3 t4 − t3 3,4


```

and I propose to initialise the knot vector as follows:
```
t0 t1 t2 t3 t4
0 0 1 2 2


```

• Remember that the subscripts of the ratios are the subscripts of t, not the values of t.
• Over the range t0 ≤ t ≤ t1 , i.e. 0 to 0. Only the first ratio in (14.13) is active and
returns 00 . The algorithm must detect this condition and take no action.
• Over the range t1 ≤ t ≤ t2 . i.e. 0 to 1. The first ratio of (14.13) is active again, and
over the range of t blends out v0 . The first ratio of (14.14) is also active, and over
the range of t blends in v1 .
• Over the range t2 ≤ t ≤ t3 . i.e. 1 to 2. The second ratio of (14.14) is active, and
over the range of t blends out v1 . The first ratio of (14.15) is also active, and over
the range of t blends in v2 .
• Finally, over the range t3 ≤ t ≤ t4 . i.e. 2 to 2. The second ratio of (14.15) is active
and returns 00 . The algorithm must detect this condition and take no action.

This process results in a linear interpolation between v0 , v1 and v2 . If (14.13)–(14.15)
are applied to coordinate values, the result is two straight lines. This seems like a lot
of work just to draw two lines, but the beauty of the technique is that it will work
with any number of points, and can be developed for quadratic and higher order
interpolants.
The New Zealand mathematician Alexander Aitken (1895–1967), developed the
following recursive interpolant:
```
    
ti+r − t t − ti r = 1, . . . , n
pri (t) = pri −1 (t) + −1
pri+1 (t)
ti+r − ti ti+r − ti i = 0, . . . , n − r

```

which interpolates between a series of points using repeated linear interpolation.

<a id='p329'></a>
<!-- Página 329 -->

14.8 B-Splines 315

14.8 B-Splines

B-splines, like Bézier curves, use polynomials to generate a curve segment. But,
unlike Bézier curves, B-splines employ a series of control points that determine the
curve’s local geometry. This feature ensures that only a small portion of the curve is
changed when a control point is moved.
There are two types of B-splines: rational and non-rational splines, which divide
into two further categories: uniform and non-uniform. Rational B-splines are formed
```
from the ratio of two polynomials such as

X (t) Y (t) Z (t)
x(t) = , y(t) = , z(t) = .
W (t) W (t) W (t)

```

Although this appears to introduce an unnecessary complication, the division by a
second polynomial brings certain advantages:
• They describe perfect circles, ellipses, parabolas and hyperbolas, whereas nonrational curves can only approximate these curves.
• They are invariant of their control points when subjected to rotation, scaling,
translation and perspective transformations, whereas non-rational curves lose this
geometric integrity.
• They allow weights to be used at the control points to push and pull the curve.
An explanation of uniform and non-uniform types is best left until you understand
the idea of splines. So, without knowing the meaning of uniform, let’s begin with
uniform B-splines.



14.8.1 Uniform B-Splines

A B-spline is constructed from a string of curve segments whose geometry is determined by a group of local control points. These curves are known as piecewise polynomials. A curve segment does not have to pass through a control point, although
this may be desirable at the two end points.
```
Cubic B-splines are very common, as they provide a geometry that is one step away
from simple quadratics, and possess continuity characteristics that make the joins
```

between the segments invisible. In order to understand their construction consider
the scenario in Fig. 14.13. Here we see a group of (m + 1) control points P0 , P1 ,
P2 , . . . , Pm which determine the shape of a cubic curve constructed from a series of
curve segments S0 , S1 , S2 , . . . , Sm−3 .
```
As the curve is cubic, curve segment Si is influenced by Pi , Pi+1 , Pi+2 , Pi+3 , and
```

curve segment Si+1 is influenced by Pi+1 , Pi+2 , Pi+3 , Pi+4 . And as there are (m + 1)
control points, there are (m − 2) curve segments.
```
A single segment Si (t) of a B-spline curve is defined by
```


<a id='p330'></a>
<!-- Página 330 -->

316 14 Curves and Patches

```
Pi+3
Pi+5


Pi+1 Si+2 Si+3


Si Si+1


Pi+2 Pi+4
Pi

```

Fig. 14.13 The construction of a uniform non-rational B-spline curve



```

3
Si (t) = Pi+r Br (t), 0≤t ≤1
r =0

```

where
```
 
B0 (t) = 16 −t 3 + 3t 2 − 3t + 1 = 16 (1 − t)3 (14.16)
 
B1 (t) = 16 3t 3 − 6t 2 + 4 (14.17)
 
B2 (t) = 16 −3t 3 + 3t 2 + 3t + 1 (14.18)
B3 (t) = 16 t 3 . (14.19)

```

These are the B-spline basis functions and are shown in Fig. 14.14.
```
Although it is not apparent, these four curve segments are part of one curve. The
```

basis function B3 (t) starts at zero and rises to 0.1666 at t = 1. It is taken over by
B2 (t) at t = 0, which rises to 0.666 at t = 1. The next segment is B1 (t) and takes
over at t = 0 and falls to 0.1666 at t = 1. Finally, B0 (t) takes over at 0.1666 and
falls to zero at t = 1. Equations (14.16)–(14.19) are represented in matrix form by


Fig. 14.14 The B-spline v
basis functions 1


```
0.75
v = (3t3-6t2+4)/6 v = (-3t3+3t2+3t+1)/6
0.5


0.25

v = (1-t)3/6 v = t3/6
0
0 0.25 0.5 0.75 1 t
```


<a id='p331'></a>
<!-- Página 331 -->

14.8 B-Splines 317

Fig. 14.15 Four curve y
segments forming a B-spline
```
3
```

curve

```
2



1



0
0 1 2 3 4 x


⎡ ⎤⎡ ⎤
−1 3 −3 1 Pi
  ⎢ 3 −6 3 0 ⎥ ⎢ Pi+1 ⎥
t 1 ⎢ ⎥⎢ ⎥
Q1 (t) = 16 t 3 t 2 ⎣ −3 0 3 0 ⎦ ⎣ Pi+2 ⎦ . (14.20)
1 4 10 Pi+3

Let’s now illustrate how (14.20) works. We first identify the control points Pi ,
```

Pi+1 , Pi+2 , etc. Let these be (0, 1), (1, 3), (2, 0), (4, 1), (4, 3), (2, 2) and (2, 3).
They can be seen in Fig. 14.15 connected together by straight lines. If we take the
first four control points: (0, 1), (1, 3), (2, 0), (4, 1), and subject the x- and ycoordinates to the matrix in (14.20) over the range 0 ≤ t ≤ 1 we obtain the first
B-spline curve segment shown in Fig. 14.15. If we move along one control point and
take the next group of control points (1, 3), (2, 0), (4, 1), (4, 3), we obtain the
second B-spline curve segment. This is repeated a further two times.
```
Figure 14.15 shows the four curve segments, and it is obvious that even though
```

there are four discrete segments, they join together perfectly. This is no accident.
The slopes at the end points of the basis curves are designed to match the slopes of
their neighbours and ultimately keep the geometric curve continuous.



14.8.2 Continuity

In order to explain continuity, it is necessary to employ differentiation. Therefore,
you may wish to read the chapter on calculus before continuing.
```
Constructing curves from several segments can only succeed if the slope of the
```

abutting curves match. As we are dealing with curves whose slopes are changing
everywhere, it will be necessary to ensure that even the rate of change of slopes is
matched at the join. This aspect of curve design is called geometric continuity and
is determined by the continuity properties of the basis function. Let’s explore such
features.
```
The first level of curve continuity C 0 , ensures that the physical end of one basis
```

curve corresponds with the following, e.g. Si (1) = Si+1 (0). We know that this occurs
```
from the basis graphs shown in Fig. 14.14. The second level of curve continuity C 1 ,
```


<a id='p332'></a>
<!-- Página 332 -->

318 14 Curves and Patches

Table 14.4 Continuity properties of cubic B-splines
t t t
C0 0 1 C1 0 1 C2 0 1
B3 (t) 0 1/6 B3 (t) 0 0.5 B3 (t) 0 1
B2 (t) 1/6 2/3 B2 (t) 0.5 0 B2 (t) 1 −2
B1 (t) 2/3 1/6 B1 (t) 0 −0.5 B1 (t) −2 1
B0 (t) 1/6 0 B0 (t) −0.5 0 B0 (t) 1 0




ensures that the slope at the end of one basis curve matches that of the following
curve. This is confirmed by differentiating the basis functions (14.16)–(14.19):
```
 
B0 (t) = 16 −3t 2 + 6t − 3 (14.21)
 
B1 (t) = 16 9t 2 − 12t (14.22)
 
B2 (t) = 16 −9t 2 + 6t + 3 (14.23)
B3 (t) = 16 3t 2 . (14.24)

```

Evaluating (14.21)–(14.24) for t = 0 and t = 1, we discover the slopes
0.5, 0, −0.5, 0 for the joins between B3 , B2 , B1 , B0 . The third level of curve continuity C 2 , ensures that the rate of change of slope at the end of one basis curve matches
that of the following curve. This is confirmed by differentiating (14.21)–(14.24):

```
B0 (t) = −t + 1 (14.25)
B1 (t) = 3t − 2 (14.26)
B2 (t) = −3t + 1 (14.27)
B3 (t) = t. (14.28)

```

Evaluating (14.25)–(14.28) for t = 0 and t = 1, we discover the values 1, 2, 1, 0
for the joins between B3 , B2 , B1 , B0 . These combined continuity results are tabulated
in Table 14.4.



14.8.3 Non-uniform B-Splines

Uniform B-splines are constructed from curve segments where the parameter spacing
is at equal intervals. Non-uniform B-splines, with the support of a knot vector, provide
extra shape control and the possibility of drawing periodic shapes. Unfortunately an
explanation of the underlying mathematics would take us beyond the introductory
nature of this text, and readers are advised to seek out other books dealing in such
matters.

<a id='p333'></a>
<!-- Página 333 -->

14.8 B-Splines 319

14.8.4 Non-uniform Rational B-Splines

Non-uniform rational B-splines (NURBS) combine the advantages of non-uniform
B-splines and rational polynomials: they support periodic shapes such as circles,
and they accurately describe curves associated with the conic sections. They also
play a very important role in describing geometry used in the modeling of computer
animation characters.
NURBS surfaces also have a patch formulation and play a very important role in
surface modelling in computer animation and CAD. However, tempting though it is
to give a description of NURBS surfaces here, they have been omitted because their
inclusion would unbalance the introductory nature of this text.



14.9 Surface Patches

14.9.1 Planar Surface Patch

The simplest form of surface geometry consists of a patchwork of polygons or triangles, where three or more vertices provide the basis for describing the associated
planar surface. For example, given four vertices P00 , P10 , P01 , P11 as shown in Fig.
14.16, a point Puv can be defined as follows. To begin with, a point along the edge
P00 – P10 is defined as
```
Pu1 = (1 − u)P00 + u P10

```

and a point along the edge P01 – P11 is defined as

```
Pu2 = (1 − u)P01 + u P11 .

```

Therefore, any point Puv is defined as

```
Puv = (1 − v)Pu1 + v Pu2
= (1 − v)[(1 − u)P00 + u P10 ] + v[(1 − u)P01 + u P11 ]
= (1 − u)(1 − v)P00 + u(1 − v)P10 + v(1 − u)P01 + uv P11

```

and is written in matrix form as
```
  
P P 1−v
Puv = [1 − u u] 00 01
P10 P11 v

```

which expands to
```
    
−1 1 P00 P01 −1 1 v
Puv = [u 1] .
```


## 10 P10 P11 10 1


<a id='p334'></a>
<!-- Página 334 -->

320 14 Curves and Patches

Fig. 14.16 A flat patch P01 P11
defined by u and v
parameters


```
v Puv




P00 u P10



```

Let’s illustrate this with an example. Given the following four points: P00 =
(0, 0, 0), P10 = (0, 0, 4), P01 = (2, 2, 1), P11 = (2, 2, 3), we can write the
coordinates of any point on the patch as
```
    
−1 1 02 −1 1 v
xuv = [u 1]
10 02 10 1
    
−1 1 02 −1 1 v
yuv = [u 1]
10 02 10 1
    
−1 1 01 −1 1 v
z uv = [u 1]
10 43 10 1


xuv = 2v (14.29)
yuv = 2v (14.30)
z uv = u(4 − 2v) + v. (14.31)

```

By substituting values of u and v in (14.29)–(14.31) between the range 0 ≤ (u, v) ≤
1, we obtain the coordinates of any point on the surface of the patch.
If we now introduce the ideas of Bézier control points into a surface patch definition, we provide a very powerful way of creating smooth 3D surface patches.



14.9.2 Quadratic Bézier Surface Patch

Bézier proposed a matrix of nine control points to determine the geometry of a
quadratic patch, as shown in Fig. 14.17. Any point on the patch is defined by

<a id='p335'></a>
<!-- Página 335 -->

14.9 Surface Patches 321

Fig. 14.17 A quadratic P11
Bézier surface patch


## P01


## P12 P21



## P02


## P10




## P22



## P00


## P20


```
⎡ ⎤⎡ ⎤⎡ ⎤⎡ 2⎤
 2  1 −2 1 P00 P01 P02 1 −2 1 v
Puv = u u 1 ⎣ −2 2 0 ⎦ ⎣ P10 P11 P12 ⎦ ⎣ −2 2 0 ⎦ ⎣ v ⎦ .
```


## 1 00 P20 P21 P22 1 00 1


The individual x-, y- and z-coordinates are obtained by substituting the x-, y- and
z-values for the central P matrix.
Let’s illustrate the process with an example. Given the following points:


## P00 = (0, 0, 0), P01 = (1, 1, 0), P02 = (2, 0, 0)


## P10 = (0, 1, 1), P11 = (1, 2, 1), P12 = (2, 1, 1)


## P20 = (0, 0, 2), P21 = (1, 1, 2), P22 = (2, 0, 2)


we can write
```
⎡ ⎤⎡ ⎤⎡ ⎤⎡ 2⎤
 2  1 −2 1 012 1 −2 1 v
xuv = u u 1 ⎣ −2 2 0 ⎦ ⎣ 0 1 2 ⎦ ⎣ −2 2 0 ⎦ ⎣ v ⎦
1 00 012 1 00 1
⎡ ⎤⎡ 2⎤
  000 v
xuv = u 2 u 1 ⎣ 0 0 0 ⎦ ⎣ v ⎦
020 1
xuv = 2v
⎡ ⎤⎡ ⎤⎡ ⎤⎡ 2⎤
 2  1 −2 1 010 1 −2 1 v
yuv = u u 1 ⎣ −2 2 0 ⎦ ⎣ 1 2 1 ⎦ ⎣ −2 2 0 ⎦ ⎣ v ⎦
1 00 010 1 00 1
⎡ ⎤⎡ 2⎤
  0 0 −2 v
yuv = u 2 u 1 ⎣ 0 0 2 ⎦ ⎣ v ⎦
−2 2 0 1
 
yuv = 2 u + v − u − v
2 2
```


<a id='p336'></a>
<!-- Página 336 -->

322 14 Curves and Patches

Table 14.5 The x-, y-, z-coordinates for different values of u and v
u v
```
0 0.5 1
```

0 (0, 0, 0) (1, 0.5, 0) (2, 0, 0)
0.5 (0, 0.5, 1) (1, 0.5, 1) (2, 0.5, 1)
1 (0, 0, 2) (1, 0.5, 2) (2, 0, 2)



```
⎡ ⎤⎡ ⎤⎡ ⎤⎡ 2⎤
 2  1 −2 1 000 1 −2 1 v
z uv = u u 1 ⎣ −2 2 0 ⎦ ⎣ 1 1 1 ⎦ ⎣ −2 2 0 ⎦ ⎣ v ⎦
1 00 222 1 00 1
⎡ ⎤⎡ 2⎤
  000 v
z uv = u 2 u 1 ⎣ 0 0 2 ⎦ ⎣ v ⎦
000 1
z uv = 2u.

```

Therefore, any point on the surface patch has coordinates
```
 
xuv = 2v, yuv = 2 u + v − u 2 − v 2 , z uv = 2u.

```

Table 14.5 shows the coordinate values for different values of u and v. In this example, the y-coordinates provide the surface curvature, which could be enhanced by
modifying the y-coordinates of the control points.



14.9.3 Cubic Bézier Surface Patch

As we saw earlier in this chapter, cubic Bézier curves require two end-points, and
two central control points. In the surface patch formulation a 4 × 4 matrix is required
as follows:
```
⎡ ⎤⎡ ⎤
```


## −1 3 −3 1 P00 P01 P02 P03


##   ⎢ 3 −6 3 0 ⎥ ⎢ P10 P11 P12 P13 ⎥

```
Puv = u 3 u 2 u 1 ⎢ ⎥⎢ ⎥
```


## ⎣ −3 3 0 0 ⎦ ⎣ P20 P21 P22 P23 ⎦


## 1 0 00 P30 P31 P32 P33

```
⎡ ⎤⎡ 3⎤
−1 3 −3 1 v
⎢ 3 −6 3 0 ⎥ ⎢ v 2 ⎥
⎢ ⎥⎢ ⎥
⎣ −3 3 0 0 ⎦ ⎣ v ⎦
1 0 00 1

```

which is illustrated with an example.
Given the points:

<a id='p337'></a>
<!-- Página 337 -->

14.9 Surface Patches 323


## P00 = (0, 0, 0), P01 = (1, 1, 0), P02 = (2, 1, 0), P03 = (3, 0, 0)


## P10 = (0, 1, 1), P11 = (1, 2, 1), P12 = (2, 2, 1), P13 = (3, 1, 1)


## P20 = (0, 1, 2), P21 = (1, 2, 2), P22 = (2, 2, 2), P23 = (3, 1, 2)


## P30 = (0, 0, 3), P31 = (1, 1, 3), P32 = (2, 1, 3), P33 = (3, 0, 3)


we can write the following matrix equations:
```
⎡ ⎤⎡ ⎤
−1 3 −3 1 0123
  ⎢ 3 −6 3 0 ⎥ ⎢ 0 1 2 3 ⎥
xuv = u 3 u 2 u 1 ⎢ ⎥⎢
⎣ −3 3 0 0 ⎦ ⎣ 0 1 2 3 ⎦
⎥

1 0 00 0123
⎡ ⎤⎡ 3⎤
−1 3 −3 1 v
⎢ 3 −6 3 0 ⎥ ⎢ v 2 ⎥
⎢ ⎥⎢ ⎥
⎣ −3 3 0 0 ⎦ ⎣ v ⎦
1 0 00 1
⎡ ⎤⎡ 3⎤
0000 v
  ⎢ 0 0 0 0 ⎥ ⎢ v2 ⎥
xuv = u 3 u 2 u 1 ⎢ ⎥⎢ ⎥
⎣0 0 0 0⎦⎣ v ⎦
0030 1
xuv = 3v
⎡ ⎤⎡ ⎤
−1 3 −3 1 0110
  ⎢ 3 −6 3 0 ⎥ ⎢ 1 2 2 1 ⎥
yuv = u 3 u 2 u 1 ⎢ ⎥⎢ ⎥
⎣ −3 3 0 0 ⎦ ⎣ 1 2 2 1 ⎦
1 0 00 0110
⎡ ⎤⎡ 3⎤
−1 3 −3 1 v
⎢ 3 −6 3 0 ⎥ ⎢ v 2 ⎥
⎢ ⎥⎢ ⎥
⎣ −3 3 0 0 ⎦ ⎣ v ⎦
1 0 00 1
⎡ ⎤⎡ 3⎤
0 00 0 v
  ⎢ 0 0 0 −3 ⎥ ⎢ v 2 ⎥
yuv = u 3 u 2 u 1 ⎢ ⎥⎢ ⎥
⎣0 0 0 3⎦⎣ v ⎦
0 −3 3 0 1


 
yuv = 3 u + v − u 2 − v 2


⎡ ⎤⎡ ⎤
−1 3 −3 1 0000
  ⎢ 3 −6 3 0 ⎥ ⎢ 1 1 1 1 ⎥
z uv = u 3 u 2 u 1 ⎢ ⎥⎢ ⎥
⎣ −3 3 0 0 ⎦ ⎣ 2 2 2 2 ⎦
1 0 00 3333
```


<a id='p338'></a>
<!-- Página 338 -->

324 14 Curves and Patches

Table 14.6 The x-, y-, z-coordinates for different values of u and v
u v
```
0 0.5 1
```

0 (0, 0, 0) (1.5, 0.75, 0) (3, 0, 0)
0.5 (0, 0.75, 1.5 (1.5, 1.5, 1.5) (3, 0.75, 1.5)
1 (0, 0, 3) (1.5, 0.75, 3) (3, 0, 3)



```
⎡ ⎤⎡ 3⎤
−1 3 −3 1 v
⎢ 3 −6 3 0 ⎥ ⎢ v 2 ⎥
⎢ ⎥⎢ ⎥
⎣ −3 3 0 0 ⎦ ⎣ v ⎦
1 0 00 1
⎡ ⎤⎡ 3⎤
0000 v
  ⎢ 0 0 0 0 ⎥ ⎢ v2 ⎥
z uv = u 3 u 2 u 1 ⎢ ⎥⎢ ⎥
⎣0 0 0 3⎦⎣ v ⎦
0000 1

z uv = 3u.

```

Therefore, any point on the surface patch has coordinates
```
 
xuv = 3v, yuv = 3 u + v − u 2 − v 2 , z uv = 3u.

```

Table 14.6 shows the coordinate values for different values of u and v. In this example, the y-coordinates provide the surface curvature, which could be enhanced by
modifying the y-coordinates of the control points.
Complex 3D surfaces are readily modeled using Bézier patches. One simply
creates a mesh of patches such that their control points are shared at the joins. Surface
continuity is controlled using the same mechanism for curves. But where the slopes
of trailing and starting control edges apply for curves, the corresponding slopes of
control tiles apply for patches.



14.10 Summary

This subject has been the most challenging one to describe. On the one hand, the
subject is vital to every aspect of computer graphics, and on the other, the reader
is required to wrestle with cubic polynomials and a little calculus. However, I do
hope that I have managed to communicate some essential concepts behind curves
and surfaces, and that you will be tempted to implement some of the mathematics.

<a id='p339'></a>
<!-- Página 339 -->


## Chapter 15

Analytic Geometry




15.1 Introduction

This chapter explores some basic elements of geometry and analytic geometry that
are frequently encountered in computer graphics. For completeness, I have included a
short review of important elements of Euclidean geometry with which you should be
familiar. Perhaps the most important topics that you should try to understand concern
the definitions of straight lines in space, 3D planes, and how points of intersection
are computed. Another useful topic is the role of parameters in describing lines and
line segments, and their intersection.


15.2 Background

In the third century BCE, Euclid laid the foundations of geometry that have been taught
in schools for centuries. In the 19th century, mathematicians such as Bernhard Riemann (1809–1900) and Nicolai Lobachevsky transformed this Euclidean geometry
with ideas such as curved space, and spaces with higher dimensions. Although none
of these developments affect computer graphics, they do place Euclid’s theorems in
a specific context: a set of axioms that apply to flat surfaces. We have probably all
been taught that parallel lines never meet, and that the internal angles of a triangle
sum to 180◦ , but these are only true in specific situations. As soon as the surface
or space becomes curved, such rules break down. So let’s review some rules and
observations that apply to shapes drawn on a flat surface.



15.2.1 Angles

By definition, 360◦ or 2π [radians] measure one revolution. You should be familiar
with both units of measurement, and how to convert from one to the other. Figure 15.1

© Springer-Verlag London Ltd., part of Springer Nature 2022 325
J. Vince, Mathematics for Computer Graphics, Undergraduate Topics
in Computer Science, https://doi.org/10.1007/978-1-4471-7520-9_15

<a id='p340'></a>
<!-- Página 340 -->

326 15 Analytic Geometry

Fig. 15.1 Examples of
adjacent, supplementary,
opposite and complementary φ
angles
```
β α
α β
δ

α + β = 180◦ δ + φ = 90◦

```

Fig. 15.2 The first intercept
theorem
```
a
c

a c
d
d b

b




```

Fig. 15.3 The second
intercept theorem
```
c

a

b
a b
c
d
d



```

shows examples of adjacent / supplementary angles (sum to 180◦ ), opposite angles
(equal), and complementary angles (sum to 90◦ ).



15.2.2 Intercept Theorems

The Intercept Theorems are attributed to the Greek philosopher and mathematician Thales of Miletus (c.624–c.546 BC) and involve intersecting and parallel lines.
Figures 15.2 and 15.3 show two scenarios that give rise to the following observations:

<a id='p341'></a>
<!-- Página 341 -->

15.2 Background 327

• First intercept theorem:

```
a+b c+d b d
= , = .
a c a c
```

• Second intercept theorem:
```
a c
= .
b d


```

15.2.3 Golden Section

The golden section is widely used in art and architecture to represent an ‘ideal’ ratio
for the height and width of an object. Its origins stem from the interaction between
a circle and triangle and give rise to the following relationship:
```
a √ 
b= 5 − 1 ≈ 0.618a.
2
```

The rectangle in Fig. 15.4 has proportions:

```
height = 0.618 × width.



```

15.2.4 Triangles

The rules associated with interior and exterior angles of a triangle are very useful in
solving all sorts of geometric problems. Figure 15.5 shows two diagrams identifying
interior and exterior angles. We can see that the sum of the interior angles is 180◦ ,
and that the exterior angles of a triangle are equal to the sum of the opposite angles:

```
α + β + θ = 180◦
α = θ + β
β = α + θ
θ  = α + β.


```

Fig. 15.4 A rectangle with a
height to width ratio equal to
the golden section
```
6.18




10.0
```


<a id='p342'></a>
<!-- Página 342 -->

328 15 Analytic Geometry

Fig. 15.5 Relationship
between interior and exterior α
angles θ
```
α β β
θ θ



α β α α β β


```

15.2.5 Centre of Gravity of a Triangle

A median is a straight line joining a vertex of a triangle to the mid-point of the
opposite side. When all three medians are drawn, they intersect at a common point,
which is also the triangle’s centre of gravity. The centre of gravity divides all the
medians in the ratio 2 : 1. Figure 15.6 illustrates this arrangement.



15.2.6 Isosceles Triangle

Figure 15.7 shows an isosceles triangle, which has two equal sides of length l and
equal base angles α. The triangle’s altitude and area are
```
  c 2
h= l2 − , A = 21 ch.
2

```

Fig. 15.6 The three medians
of a triangle intersect at its
centre of gravity
```
b a

b a

c c
```

Fig. 15.7 An isosceles
triangle
```
l l
h

α α
c/2 c/2
```


<a id='p343'></a>
<!-- Página 343 -->

15.2 Background 329

15.2.7 Equilateral Triangle

An equilateral triangle has three equal sides of length l and equal angles of 60◦ . The
triangle’s altitude and area are
```
√ √
h = 23 l, A = 43 l 2 .



```

15.2.8 Right Triangle

Figure 15.8 shows a right triangle with its obligatory right angle. The triangle’s altitude and area are
```
ab
h= , A = 21 ab.
c


```

15.2.9 Theorem of Thales

Figure 15.9 illustrates the theorem of Thales, which states that the right angle of a
right triangle lies on the circumcircle over the hypotenuse.


15.2.10 Theorem of Pythagoras

Although this theorem is named after Pythagoras there is substantial evidence to show
that it was known by the Babylonians a millennium earlier. However, Pythagoras is

Fig. 15.8 A right triangle


```
b a
h


c
```

Fig. 15.9 The theorem of
Thales

<a id='p344'></a>
<!-- Página 344 -->

330 15 Analytic Geometry

Fig. 15.10 The theorem of
Pythagoras states that
a 2 = b2 + c2
```
a



c
a
c
b

b

```

credited with its proof. Figure 15.10 illustrates the well-known relationship:

```
a 2 = b2 + c2

from which one can show that

sin2 θ + cos2 θ = 1.



```

15.2.11 Quadrilateral

Quadrilaterals have four sides and include the square, rectangle, trapezoid, parallelogram and rhombus, whose interior angles sum to 360◦ . As the square and rectangle
are familiar shapes, we will only consider the other three.



15.2.12 Trapezoid

Figure 15.11 shows a trapezoid which has one pair of parallel sides h apart. The
mid-line m and area are given by

Fig. 15.11 A trapezoid with b
one pair of parallel sides

```
h
m


a
```


<a id='p345'></a>
<!-- Página 345 -->

15.2 Background 331

Fig. 15.12 A parallelogram a
formed by two pairs of
parallel lines
```
d2 d1
b b h



α
a


m = 21 (a + b)
A = mh.



```

15.2.13 Parallelogram

Figure 15.12 shows a parallelogram, which is formed from two pairs of intersecting
parallel lines, so it has equal opposite sides and equal opposite angles. The altitude,
diagonal lengths and area are given by

```
h = b sin α
 
d1,2 = a 2 + b2 ± 2a b2 − h 2
A = ah.



```

15.2.14 Rhombus

Figure 15.13 shows a rhombus, which is a parallelogram with four sides of equal
length a. The area is given by


Fig. 15.13 A rhombus is a
parallelogram with four
equal sides a a
```
d1
α
d2
a a
```


<a id='p346'></a>
<!-- Página 346 -->

332 15 Analytic Geometry

Fig. 15.14 Part of a regular
gon showing the inner and
outer radii and the edge
length

```
Ri Ro




an


A = a 2 sin α = 21 d1 d2 .



```

15.2.15 Regular Polygon

Figure 15.14 shows part of a regular n-gon with outer radius Ro , inner radius Ri and
edge length an . Table 15.1 shows the relationship between the area, an , Ri and Ro
for different polygons.



15.2.16 Circle

The circumference C and area A of a circle are given by

```
C = π d = 2πr


```

Table 15.1 The area An , edge length an , inner radius Ri , and outer radius Ro for different polygons
n an = 2Ri tan(180◦ /n) Ri = Ro cos(180◦ /n) Ro2 = Ri2 + 41 an2
n n 2 ◦
```
An = 4 an cot(180 /n) An = 2 Ro sin(360 /n)
n 2 ◦ An = n Ri2 tan(180◦ /n)
 √ √ √
Ro
```

5 a5 = 2Ri 5 − 2 5 Ri = 4 ( 5 + 1) Ro = Ri ( 5 − 1)
```
a 2  √  √  √
```

5 A5 = 45 25 + 10 5 A5 = 58 Ro2 10 + 2 5 A5 = 5Ri2 5 − 2 5
```
√ √ √
```

6 a6 = 23 Ri 3 Ri = R2o 3 Ro = 23 Ri 3
```
√ √ √
```

6 A6 = 23 a62 3 A6 = 23 Ro2 3 A6 = 2Ri2 3
```
√  √  √
```

8 a8 = 2Ri ( 2 − 1) Ri = R2o 2 + 2 R o = Ri 4 − 2 2
```
√  √ √ 
```

8 A8 = 2a82 2+1 A8 = 2Ro2 2 A8 = 8Ri2 2−1
```
 √  √  √
```

10 a10 = 25 Ri 25 − 10 5 Ri = R4o 10 + 2 5 Ro = R5i 50 − 10 5
```
 √  √  √
```

10 A10 = 25 a102 5+2 5 A10 = 54 Ro2 10 − 2 5 A10 = 2Ri2 25 − 10 5

<a id='p347'></a>
<!-- Página 347 -->

15.2 Background 333

Fig. 15.15 An annulus
formed from two concentric
circles

## R



## D

```
d r




```

Fig. 15.16 A sector of a
circle defined by the angle α
```
r

α




A = πr 2 = 41 π d 2

```

where the diameter d = 2r .
```
An annulus is the area between two concentric circles as shown in Fig. 15.15, and
```

its area A is given by
```
   
A = π R 2 − r 2 = 41 π D 2 − d 2

```

where D = 2R and d = 2r .
Figure 15.16 shows a sector of a circle, whose area is given by

```
α◦
A= πr 2 .
360◦

```

Figure 15.17 shows a segment of a circle, whose area is given by

```
A = 21 r 2 (α − sin α), where α is in radians.


```

The area of an ellipse with major and minor radii a and b is

```
A = πab.
```


<a id='p348'></a>
<!-- Página 348 -->

334 15 Analytic Geometry

Fig. 15.17 A segment of a
circle defined by the angle α
```
r

α




```

15.3 2D Analytic Geometry

In this section we briefly examine familiar descriptions of geometric elements and
ways of computing intersections.



15.3.1 Equation of a Straight Line

The well-known equation of a line is

```
y = mx + c

```

where m is the slope and c the intersection with the y-axis, as shown in Fig. 15.18.
This is called the normal form.

Given two points (x1 , y1 ) and (x2 , y2 ) we can state that for any other point (x, y)

```
y − y1 y2 − y1
=
x − x1 x2 − x1


```

Fig. 15.18 The normal form Y
of the straight line is
y = mx + c
```
y
y2

y1
m
c


x1 x2 x X
```


<a id='p349'></a>
<!-- Página 349 -->

15.3 2D Analytic Geometry 335

which yields
```
y2 − y1
y = (x − x1 ) + y1 .
x2 − x1

```

Although these equations have their uses, the more general form is much more
convenient:
```
ax + by + c = 0.

```

As we shall see, this equation possesses some interesting qualities.



15.3.2 The Hessian Normal Form

Figure 15.19 shows a line whose orientation is controlled by a normal unit vector
n = [a b]T . If P(x, y) is any point on the line, then p is a position vector where
p = [x y]T and d is the perpendicular distance from the origin to the line. Therefore,

```
d
= cos α
p

```

and
```
d = p cos α.

```

But the dot product n · p is given by

```
n · p = np cos α = ax + by

```

which implies that
```
ax + by = dn


```

Fig. 15.19 The orientation Y
of a line can be controlled by
a normal vector n and a
distance d n




```
d
P (x, y)
p
α
```


## X


<a id='p350'></a>
<!-- Página 350 -->

336 15 Analytic Geometry

and because n = 1 we can write

```
ax + by − d = 0

```

where (x, y) is a point on the line, a and b are the components of a unit vector
normal to the line, and d is the perpendicular distance from the origin to the line. The
distance d is positive when the normal vector points away from the origin, otherwise
it is negative. For example, let’s find the equation of a line whose normal vector is
[3 4]T and the perpendicular distance from the origin to the line is 1.
```
We begin by normalising
√ the normal vector to its unit form. Therefore, if n =
```

[3 4]T , n = 32 + 42 = 5 The equation of the line is
```
3
5
x + 45 y − 1 = 0.

```

Similarly, let’s find the Hessian normal form of y = 2x + 1.
Rearranging the equation we get

```
2x − y = −1

```

which gives a negative distance. If we want the normal vector to point away from
the origin we multiply by −1:

```
−2x + y − 1 = 0.

```

Normalise the normal vector to a unit form
```
 √
i.e. (−2)2 + 12 = 5

− √25 x + √15 y − √15 = 0.

```

Therefore, the perpendicular distance from the origin to the line, and the unit normal
vector are respectively

## T

```
−2
√1
5
and √
5
√1
5
.

```

As the Hessian normal form involves a unit normal vector, we can incorporate the
vector’s direction cosines within the equation:

```
x cos α + y sin α − d = 0

```

where α is the angle between the normal vector and the x-axis.

<a id='p351'></a>
<!-- Página 351 -->

15.3 2D Analytic Geometry 337

Fig. 15.20 The Hessian Y
normal form of the line
equation partitions space into
two zones n
```
ax + by − d > 0

ax
+
by
d −
d=
0
ax + by − d < 0

```


## X




15.3.3 Space Partitioning

The Hessian normal form provides a very useful way of partitioning space into two
zones: the partition that includes the normal vector, and the opposite partition. This
is illustrated in Fig. 15.20.
```
Given the equation
ax + by − d = 0

```

a point (x, y) on the line satisfies the equation. But if the point (x, y) is in the
partition in the direction of the normal vector, it creates the inequality

```
ax + by − d > 0.

```

Conversely, if (x, y) is in the partition opposite to the direction of the normal vector
creates the inequality
```
ax + by − d < 0.

```

This space-partitioning feature of the Hessian normal form is useful in clipping lines
against polygonal windows.



15.3.4 The Hessian Normal Form from Two Points

Given two points (x1 , y1 ) and (x2 , y2 ) we compute the values of a, b and d for the
Hessian normal form as follows.
The vector joining the two points is v = [x  y ]T where

```
x = x 2 − x 1
 y = y2 − y1
```


<a id='p352'></a>
<!-- Página 352 -->

338 15 Analytic Geometry
```

v = 2x + 2y

```

The unit vector normal to v is n = [−y x ]T , where

```
x
x =
v
y
y =
v

```

Therefore, let p = [x y]T be any point on the line, and using the Hessian Normal
Form, we can write:

```
n · p = −y x + x y = −y x1 + x y1

```

and
```
− y x + x y + (y x1 − x y1 ) = 0 (15.1)

```

For example, given√ the following points:
```
√ (x1 , y1 ) = (0, 1) and (x2 , y2 ) =
```

(1, 0); then x = 1/ 2 and y = −1/ 2. Therefore, using (15.1)

```
x y  
−1
√ + √ + 0× √ 2
− 1 × √1
2
=0
2 2
x y 1
√ + √ − √ = 0.
2 2 2



```

15.4 Intersection Points

15.4.1 Intersecting Straight Lines

Given two line equations of the form

```
a1 x + b1 y + d1 = 0
a2 x + b2 y + d2 = 0

```

the intersection point (xi , yi ) is given by

```
b1 d2 − b2 d1
xi =
a1 b2 − a2 b1
d1 a2 − d2 a1
yi =
a1 b2 − a2 b1
```


<a id='p353'></a>
<!-- Página 353 -->

15.4 Intersection Points 339

or using determinants:

```
b1 d1
b2 d2
xi =
a1 b1
a2 b2
d1 a1
d2 a2
yi = .
a1 b1
a2 b2


```

If the denominator is zero, the equations are linearly dependent, indicating that there
is no intersection.



15.4.2 Intersecting Line Segments

We are often concerned with line segments in computer graphics as they represent
the edges of shapes and objects. So let’s investigate how to compute the intersection
of two 2D-line segments. Figure 15.21 shows two line segments defined by their end
points P1 , P2 , P3 , P4 and respective position vectors p1 , p2 , p3 and p4 . We can write
the following vector equations to identify the point of intersection:

```
pi = p1 + t (p2 − p1 ) (15.2)
pi = p3 + s(p4 − p3 ) (15.3)

```

where parameters s and t vary between 0 and 1. For the point of intersection, we can
write


Fig. 15.21 Two line Y
segments with their P1 P3
associated position vectors Pi
```
p3 P2
p1 pi
```


## P4

```
p2
p4



```


## X


<a id='p354'></a>
<!-- Página 354 -->

340 15 Analytic Geometry

```
p1 + t (p2 − p1 ) = p3 + s(p4 − p3 ).

```

Therefore, the parameters s and t are given by

```
(p1 − p3 ) + t (p2 − p1 )
s= (15.4)
p4 − p3
(p3 − p1 ) + s(p4 − p3 )
t= . (15.5)
p2 − p1

```

From (15.5) we can write

```
(x3 − x1 ) + s(x4 − x3 )
t=
x2 − x1
(y3 − y1 ) + s(y4 − y3 )
t=
y2 − y1

```

which yields
```
x1 (y3 − y2 ) + x2 (y3 − y1 ) + x3 (y2 − y1 )
s= (15.6)
(x2 − x1 )(y4 − y3 ) − (x4 − x3 )(y2 − y1 )

```

similarly,
```
x1 (y4 − y3 ) + x3 (y1 − y4 ) + x4 (y3 − y1 )
t= . (15.7)
(x4 − x3 )(y2 − y1 ) − (x2 − x1 )(y4 − y3 )

```

Let’s test (15.6) and (15.7) with two examples to illustrate how the equations are
used in practice. The first example demonstrates an intersection condition, and the
second demonstrates a touching condition.
Figure 15.22a shows two line segments intersecting, with an obvious intersection
point of (1.5, 0). The coordinates of the line segments are

```
(x1 , y1 ) = (1, 0), (x2 , y2 ) = (2, 0)
(x3 , y3 ) = (1.5, −1), (x4 , y4 ) = (1.5, 1)

```

therefore,
```
1(1 − (−1)) + 1.5(0 − 1) + 1.5(−1 − 0)
t= = 0.5
(0 − 0)(1.5 − 1.5) − (2 − 1)(1 − (−1))

```

and
```
1(−1 − 0) + 2(0 − (−1)) + 1.5(0 − 0)
s= = 0.5.
(1 − (−1))(2 − 1) − (1.5 − 1.5)(0 − 0)

```

Substituting s and t in (15.2) and (15.3) we get (xi , yi ) = (1.5, 0) as predicted.
Figure 15.22b shows two line segments touching at (1.5, 0). The coordinates of
the line segments are

<a id='p355'></a>
<!-- Página 355 -->

15.4 Intersection Points 341

Fig. 15.22 a Shows two line Y Y
segments intersecting b
Shows two line segments (1.5, 1) (1.5, 1)
touching

```
(1, 0) (2, 0) (1, 0) (2, 0)
```


## X (1.5, 0) X



```
(1.5, −1)

(a) (b)



(x1 , y1 ) = (1, 0), (x2 , y2 ) = (2, 0)
(x3 , y3 ) = (1.5, 0), (x4 , y4 ) = (1.5, 1)

```

therefore,
```
1(1 − 0) + 1.5(0 − 1) + 1.5(0 − 0)
t= = 0.5
(0 − 0)(1.5 − 1.5) − (2 − 1)(1 − 0)

```

and
```
1(0 − 0) + 2(0 − 0) + 1.5(0 − 0)
s= = 0.
(1 − 0)(2 − 1) − (1.5 − 1.5)(0 − 0)

```

The zero value of s confirms that the lines touch, rather than intersect, and t = 0.5
confirms that the touching takes place halfway along the line segment.



15.5 Point Inside a Triangle

We often require to test whether a point is inside, outside or touching a triangle. Let’s
examine two ways of performing this operation. The first is related to finding the
area of a triangle.



15.5.1 Area of a Triangle

Let’s declare a triangle formed by the anticlockwise points P1 (x1 , y1 ), P2 (x2 , y2 )
and P3 (x3 , y3 ) as shown in Fig. 15.23. The area of the triangle is given by:

A = (x2 − x1 )(y3 − y1 ) − 21 (x2 − x1 )(y2 − y1 ) − 21 (x2 − x3 )(y3 − y2 ) − 21 (x3 − x1 )(y3 − y1 )


which simplifies to

<a id='p356'></a>
<!-- Página 356 -->

342 15 Analytic Geometry

Fig. 15.23 The area of the Y
triangle is computed by P3
subtracting the smaller
triangles from the
rectangular area

## P2





## P1



## X





```
A = 21 [x1 (y2 − y3 ) + x2 (y3 − y1 ) + x3 (y1 − y2 )]

```

and this can be further simplified to

```
x1 y1 1
A = 21 x2 y2 1 .
x3 y3 1

```

Figure 15.24 shows two triangles with opposing vertex sequences. If we calculate
the area of the top triangle with anticlockwise vertices, we obtain


## A = 21 [1(2 − 4) + 3(4 − 2) + 2(2 − 2)] = 2


whereas the area of the bottom triangle with clockwise vertices is


## A = 21 [1(2 − 0) + 3(0 − 2) + 2(2 − 2)] = −2


which shows that the technique is sensitive to vertex direction. We can exploit this
sensitivity to test if a point is inside or outside a triangle.


Fig. 15.24 The top triangle Y

## P3

has anticlockwise vertices,
and the bottom triangle
clockwise vertices



## P1 P2






## P3 X


<a id='p357'></a>
<!-- Página 357 -->

15.5 Point Inside a Triangle 343

Fig. 15.25 If the point Pt is Y
inside the triangle, it is P3
always to the left as the
boundary is traversed in an
anticlockwise direction Pt

## P2





## P1



## X





Consider the scenario shown in Fig. 15.25, where the point Pt is inside the triangle

## (P1 , P2 , P3 ).

• If the area of triangle (P1 , P2 , Pt ) is positive, Pt must be to the left of the
line (P1 , P2 ).
• If the area of triangle (P2 , P3 , Pt ) is positive, Pt must be to the left of the
line (P2 , P3 ).
• If the area of triangle (P3 , P1 , Pt ) is positive, Pt must be to the left of the
line (P3 , P1 ).
If all the above tests are positive, Pt is inside the triangle. Furthermore, if one area
is zero and the other areas are positive, the point is on the boundary, and if two areas
are zero and the other positive, the point is on a vertex.
```
Let’s now investigate how the Hessian normal form provides a similar function.



```

15.5.2 Hessian Normal Form

We can determine whether a point is inside, touching or outside a triangle by representing the triangle’s edges in the Hessian normal form, and testing in which partition
the point is located. If we arrange that the normal vectors are pointing towards the
inside of the triangle, any point inside the triangle will create a positive result when
tested against the edge equation. In the following calculations there is no need to
ensure that the normal vector is a unit vector, therefore (15.1) can be written:

```
− y x + x y + ( y x1 − x y1 ) = 0


```

To illustrate this, consider the scenario shown in Fig. 15.26 where a triangle is formed
by the points (1, 1), (3, 1) and (2, 3). With reference to (15.1) we compute the three
line equations:

<a id='p358'></a>
<!-- Página 358 -->

344 15 Analytic Geometry

Fig. 15.26 The triangle is Y (2, 3)
represented by three line
equations expressed in the
Hessian normal form. Any
point inside the triangle is
found by evaluating their
equations


```
(1, 1) (3, 1)



```


## X




The line between (1, 1) and (3, 1):

```
x = 2
y = 0
−0 × x + 2 × y − 2 × 1 = 0
2y − 2 = 0.

```

The line between (3, 1) and (2, 3):

```
x = −1
y = 2
−2 × x − 1 × y + (2 × 3 + 1 × 1) = 0
−2x − y + 7 = 0.

```

The line between (2, 3) and (1, 1):

```
x = −1
 y = −2
2 × x − 1 × y + (−2 × 2 − 1 × 3) = 0
2x − y − 1 = 0.

```

Thus the three line equations for the triangle are

```
2y − 2 = 0
−2x − y + 7 = 0
2x − y − 1 = 0.
```


<a id='p359'></a>
<!-- Página 359 -->

15.5 Point Inside a Triangle 345

We are only interested in the signs of the equations:

```
2y − 2 (15.8)
− 2x − y + 7 (15.9)
2x − y − 1 (15.10)

```

which can be tested for any arbitrary point (x, y). If they are all positive, the point is
inside the triangle. If one expression is negative, the point is outside. If one expression
is zero, the point is on an edge, and if two expressions are zero, the point is on a
vertex.
Just as a quick test, consider the point (2, 2). The three expressions (15.8) to
(15.10) are positive, which confirms that the point is inside the triangle. The point
(3, 3) is obviously outside the triangle, which is confirmed by two positive results
and one negative. Finally, the point (2, 3), which is a vertex, creates one positive
result and two zero results.



15.6 Intersection of a Circle with a Straight Line

The equation of a circle has already been given in the previous chapter, so we will
now consider how to compute its intersection with a straight line. We begin by testing
the equation of a circle with the normal form of the line equation:

```
x 2 + y 2 = r 2 and y = mx + c.

```

By substituting the line equation in the circle’s equation we discover the two intersection points:
```

−mc ± r 2 (1 + m 2 ) − c2
x1,2 = (15.11)
1 + m2

c ± m r 2 (1 + m 2 ) − c2
y1,2 = . (15.12)
1 + m2

```

Let’s test this result with the scenario shown in Fig. 15.27. Using the normal form of
the line equation we have

```
y = x + 1, m = 1, and c = 1.

```

Substituting these values in (15.11) and (15.12) yields

```
x1,2 = −1, 0, y1,2 = 0, 1.

```

The actual points of intersection are (−1, 0) and (0, 1).

<a id='p360'></a>
<!-- Página 360 -->

346 15 Analytic Geometry

Fig. 15.27 The intersection Y
of a circle with a line (0, 1) y =x+1




```
(−1, 0)
```


## X




```
x2 + y 2 = 1




```

Testing the equation of the circle with the general equation of the line ax + by +
c = 0 yields intersections given by
```

−ac ± b r 2 (a 2 + b2 ) − c2
x1,2 = (15.13)
a 2 + b2

−bc ± a r 2 (a 2 + b2 ) − c2
y1,2 = . (15.14)
a 2 + b2

```

The general form of the line equation y = x + 1 is

```
x − y + 1 = 0 where a = 1, b = −1 and c = 1.

```

Substituting these values in (15.13) and (15.14) yields

```
x1,2 = −1, 0, and y1,2 = 0, 1

```

which gives the same intersection points found above.
Finally, using the Hessian normal form of the line ax + by − d = 0 yields intersections given by
```

x1,2 = ad ± b r 2 − d 2 (15.15)

y1,2 = bd ± a r 2 − d 2 . (15.16)

```

The Hessian normal form of the line equation x − y + 1 = 0 is

```
−0.707x + 0.707y − 0.707 ≈ 0

```

where a ≈ −0.707, b ≈ 0.707 and d ≈ 0.707. Substituting these values in (15.15)
and (15.16) yields

<a id='p361'></a>
<!-- Página 361 -->

15.6 Intersection of a Circle with a Straight Line 347

```
x1,2 = −1, 0 and y1,2 = 0, 1

```

which gives the same intersection points found above. One can readily see the computational benefits of using the Hessian normal form over the other forms of equations.



15.7 3D Geometry

3D straight lines are best described using vector notation, and readers are urged
to develop strong skills in these techniques if they wish to solve problems in 3D
geometry. Let’s begin this short survey of 3D analytic geometry by describing the
equation of a straight line.



15.7.1 Equation of a Straight Line

We start by using a vector b to define the orientation of the line, and a point a in space
through which the line passes. This scenario is shown in Fig. 15.28. Given another
point P on the line we can define a vector tb between a and P, where t is a scalar.
The position vector p for P is given by

```
p = a + tb

from which we can obtain the coordinates of the point P:

x p = xa + t xb
y p = ya + t yb
z p = za + t zb .


```

Fig. 15.28 The line Y
equation is based upon the
point a and the vector b b

## P

```
tb
a
p
a X




```


## Z


<a id='p362'></a>
<!-- Página 362 -->

348 15 Analytic Geometry

For example, if b = [1 2 3]T and a = (2, 3, 4), then by setting t = 1 we can
identify a second point on the line:

```
xp = 2 + 1 = 3
yp = 3 + 2 = 5
z p = 4 + 3 = 7.

```

In fact, by using different values of t we can slide up and down the line with ease.
If we have two points P1 and P2 , such as the vertices of an edge, we can represent
the line equation using the above vector technique:

```
p = p1 + t (p2 − p1 )

```

where p1 and p2 are position vectors to their respective points. Once more, we can
write the coordinates of any point P as follows:

```
x p = x1 + t (x2 − x1 )
y p = y1 + t (y2 − y1 )
z p = z 1 + t (z 2 − z 1 ).



```

15.7.2 Intersecting Two Straight Lines

Given two straight lines we can test for a point of intersection, but must be prepared
for three results:
• a real intersection point
• no intersection point
• an infinite number of intersections (identical lines).
If the line equations are of the form

```
p = a1 + r b1
p = a2 + r b2

```

for an intersection we can write

```
a1 + r b1 = a2 + sb2

```

which yields

```
xa1 + r xb1 = xa2 + sxb2 (15.17)
ya1 + r yb1 = ya2 + syb2 (15.18)
```


<a id='p363'></a>
<!-- Página 363 -->

15.7 3D Geometry 349

```
z a1 + r z b1 = z a2 + sz b2 . (15.19)

```

We now have three equations in two unknowns, and any value of r and s must hold for
all three equations. We begin by selecting two equations that are linearly independent
(i.e. one equation is not a scalar multiple of the other) and solve for r and s, which
must then satisfy the third equation. If this final substitution fails, then there is no
intersection. If all three equations are linearly dependent, they describe two parallel
lines, which can never intersect.
```
To check for linear dependency we rearrange (15.17)–(15.19) as follows:

r xb1 − sxb2 = xa2 − xa1 (15.20)
r yb1 − syb2 = ya2 − ya1 (15.21)
r z b1 − sz b2 = z a2 − z a1 . (15.22)

```

If the determinant  of any pair of these equations is zero, then they are dependent.
For example, (15.20) and (15.21) form the determinant

```
xb1 −xb2
=
yb1 −yb2

```

which, if zero, implies that the two equations can not yield a solution. As it is impossible to predict which pair of equations from (15.20) to (15.22) will be independent,
let’s express two independent equations as follows:

```
ra11 − sa12 = b1
ra21 − sa22 = b2

```

which yields

```
a22 b1 − a12 b2
r=

a21 b1 − a11 b2
s=

```

where
```
a11 a12
= .
a21 a22

```

Solving for r and s we obtain

```
yb2 (xa2 − xa1 ) − xb2 (ya2 − ya1 )
r= (15.23)
xb1 yb2 − yb1 xb2
yb1 (xa2 − xa1 ) − xb1 (ya2 − ya1 )
s= . (15.24)
xb1 yb2 − yb1 xb2
```


<a id='p364'></a>
<!-- Página 364 -->

350 15 Analytic Geometry

As a quick test, consider the intersection of the lines encoded by the following
vectors: ⎡ ⎤ ⎡ ⎤ ⎡ ⎤ ⎡ ⎤
```
0 3 0 2
a1 = ⎣ 1 ⎦ , b1 = ⎣ 3 ⎦ , a2 = ⎣ 0.5 ⎦ , b2 = ⎣ 3 ⎦ .
0 3 0 2

```

Substituting the x- and y-components in (15.23) and (15.24) we discover

```
r = 13 and s = 21

```

but for these to be consistent, they must satisfy the z-component of the original
equation:
```
r z b1 − sz b2 = z a2 − z a1
1
3
× 3 − 21 × 2 = 0

```

which is correct. Therefore, the point of intersection is given by either

```
pi = a1 + r b1 , or
pi = a2 + sb2 .

```

Let’s try both, just to prove the point:

```
xi = 0 + 13 3 = 1, xi = 0 + 21 2 = 1
yi = 1 + 13 3 = 2, yi = 21 + 21 3 = 2
z i = 0 + 13 3 = 1, z i = 0 + 21 2 = 1.

```

Therefore, the point of intersection point is (1, 2, 1).
Now let’s take two lines that don’t intersect, and also exhibit some linear dependency: ⎡ ⎤ ⎡ ⎤ ⎡ ⎤ ⎡ ⎤
```
0 2 0 2
a1 = ⎣ 1 ⎦ , b1 = ⎣ 2 ⎦ , a2 = ⎣ 2 ⎦ , b2 = ⎣ 2 ⎦ .
0 0 0 1

Taking the x- and y-components we discover that the determinant  is zero, which
```

has identified the linear dependency. Taking the y- and z-components the determinant
is non-zero, which permits us to compute r and s using

```
z b2 (ya2 − ya1 ) − yb2 (z a2 − z a1 )
r=
yb1 z b2 − z b1 yb2
z b1 (ya2 − ya1 ) − yb1 (z a2 − z a1 )
s=
yb1 z b2 − z b1 yb2
1(2 − 1) − 2(0 − 0) 1
r= =
2×1−0×2 2
```


<a id='p365'></a>
<!-- Página 365 -->

15.7 3D Geometry 351

```
0(2 − 1) − 2(0 − 0)
s= = 0.
2×1−0×2

```

But these values of r and s must also apply to the x-components:

```
r xb1 − sxb2 = xa2 − xa1
1
2
× 2 − 0 × 2 = 0

```

which they clearly do not, therefore the lines do not intersect.
Now let’s proceed with the equation of a plane, and then look at how to compute
the intersection of a line with a plane using a similar technique.



15.8 Equation of a Plane

We now consider four ways of representing a plane equation: the Cartesian form,
general form, parametric form and a plane from three points.



15.8.1 Cartesian Form of the Plane Equation

One popular method of representing a plane equation is the Cartesian form, which
employs a vector normal to the plane’s surface and a point on the plane. The equation
is derived as follows.
```
Let n be a nonzero vector normal to the plane and P0 (x0 , y0 , z 0 ) a point on
```

the plane. P(x, y, z) is any other point on the plane. Figure 15.29 illustrates the
scenario.
The normal vector is defined as


Fig. 15.29 The vector n is Y
normal to the plane, which n
contains a point P0 . P is any
other point on the plane


## P0

```
h q P
α p0
p


```


## Z X


<a id='p366'></a>
<!-- Página 366 -->

352 15 Analytic Geometry

```
n = ai + bj + ck

```

and the position vectors for P0 and P are

```
p0 = x0 i + y0 j + z 0 k
p = xi + yj + zk

```

respectively. From Fig. 15.29 we observe that

```
q = p − p0

```

and as n is orthogonal to q
```
n·q=0

```

therefore,
```
n · (p − p0 ) = 0

```

which expands into
```
n · p = n · p0 . (15.25)

```

Writing (15.25) in its Cartesian form we obtain

```
ax + by + cz = ax0 + by0 + cz 0

```

but ax0 + by0 + cz 0 is a scalar quantity associated with the plane and can be replaced
by d . Therefore,
```
ax + by + cz = d (15.26)

```

which is the Cartesian form of the plane equation.
The value of d has the following geometric interpretation.
In Fig. 15.29 the perpendicular distance from the origin to the plane is

```
h = p0  cos α

```

therefore,
```
n · p0 = np0  cos α = hn

```

therefore, the plane equation is also expressed as

```
ax + by + cz = hn. (15.27)

```

Dividing (15.27) by n we obtain

```
a b c
x+ y+ z=h
n n n
```


<a id='p367'></a>
<!-- Página 367 -->

15.8 Equation of a Plane 353

Fig. 15.30 A plane Y
represented by the normal
vector n and a point
P0 (0, 1, 0) P0 (0, 1, 0)


```
n




(0, 0, 1)
```


## Z X



where 
```
n = a 2 + b2 + c2 .

```

This means that when a unit normal vector is used, h is the perpendicular distance
```
from the origin to the plane. Let’s investigate this equation with an example.
```

Figure 15.30 shows a plane represented by the normal vector n = j + k and a
point on the plane P0 (0, 1, 0). Using (15.26) we have

```
0x + 1y + 1z = 0 × 0 + 1 × 1 + 1 × 0 = 1

```

therefore, the plane equation is
```
y + z = 1.

```

If we normalise the equation to create a unit normal vector, we have

```
y z 1
√ +√ =√
2 2 2
√
```

where the perpendicular distance from the origin to the plane is 1/ 2.



15.8.2 General Form of the Plane Equation

The general form of the equation of a plane is expressed as

```
Ax + By + C z + D = 0

```

which means that the Cartesian form is translated into the general form by making

<a id='p368'></a>
<!-- Página 368 -->

354 15 Analytic Geometry

Fig. 15.31 A plane is Y
defined by the vectors a and
b and the point T (xt , yt , z t )

## P

```
a

c
p λa b

b
Z t
```


## T


## X



```
A = a, B = b, C = c, D = −d.



```

15.8.3 Parametric Form of the Plane Equation

Another method of representing a plane is to employ two vectors and a point that
lie on the plane. Figure 15.31 illustrates a scenario where vectors a and b, and the
point T (xt , yt , z t ) lie on a plane. We now identify any other point on the plane
P(x p , y p , z p ) with its associated position vector p. The point T also has its associated position vector t.
```
Using vector addition we can write

c = λa + b

```

where λ and  are two scalars such that c locates the point P . We can now write

```
p=t+c (15.28)

```

therefore,

```
x p = xt + λxa + xb
y p = yt + λya + yb
z p = z t + λz a + z b

```

which means that the coordinates of any point on the plane are formed from the
coordinates of the known point on the plane, and a linear mixture of the components
of the two vectors. Let’s illustrate this vector approach with an example.

<a id='p369'></a>
<!-- Página 369 -->

15.8 Equation of a Plane 355

Fig. 15.32 The plane is
defined by the vectors a and Y
b and the point T (1, 1, 1)

## T

```
b λa

```


## P

```
t p

```


## Z


## X



Figure 15.32 shows a plane containing the vectors a = i and b = k, and the point
T (1, 1, 1) with its position vector t = i + j + k . By inspection, the plane is parallel
with the x z-plane and intersects the y-axis at y = 1.
From (15.28) we can write

```
p = t + λa + b

```

where λ and  are arbitrary scalars.
For example, if λ = 2 and  = 1:

```
xp = 1 + 2 × 1 + 1 × 0 = 3
yp = 1 + 2 × 0 + 1 × 0 = 1
z p = 1 + 2 × 0 + 1 × 1 = 2.

```

Therefore, the point (3, 1, 2) is on the plane.



15.8.4 Converting from the Parametric to the General Form

It is possible to convert from the parametric form to the general form of the plane
equation using the following formulae:

```
(a · b)(b · t) − (a · t)b2
λ=
a2 b2 − (a · b)2
(a · b)(a · t) − (b · t)a2
= .
a2 b2 − (a · b)2

```

The resulting point P(x p , y p , z p ) is perpendicular to the origin.

<a id='p370'></a>
<!-- Página 370 -->

356 15 Analytic Geometry

If vectors a and b are unit vectors, λ and  become

```
(a · b)(b · t) − a · t
λ= (15.29)
1 − (a · b)2
(a · b)(a · t) − b · t
= . (15.30)
1 − (a · b)2

```

P’s position vector p is also the plane’s normal vector. Therefore,

```
x p = xt + λxa + xb
y p = yt + λya + yb
z p = z t + λz a + z b .

```

The normal vector is
```
p = x pi + ypj + z pk

```

and because p is the perpendicular distance from the plane to the origin we can
state xp yp zp
```
x+ y+ z = p
p p p

```

or in the general form of the plane equation:

```
Ax + By + C z + D = 0

```

where xp yp zp
```
A= , B= , C= , D = −p.
p p p

```

As an example, Fig. 15.33 shows a plane inclined 45◦ to the y- and z-axis and
parallel with the x-axis. The vectors for the parametric equation are


Fig. 15.33 The vectors a Y
and b are parallel to the (0, 1, 0)
plane and the point (0, 0, 1)
is on the plane
```
λa


```


## P

```
p
t
```


## T (0, 0, 1)

```
b X
```


## Z


<a id='p371'></a>
<!-- Página 371 -->

15.8 Equation of a Plane 357

```
a =j−k
b=i
t = k.

```

Substituting these components in (15.29) and (15.30) we have

```
(0)(0) − (−1) × 1
λ= = 0.5
2 × 1 − (0)
(0)(−1) − (0) × 2
= = 0.
2 × 1 − (0)

```

Therefore,

```
x p = 0 + 0.5 × 0 + 0 × 1 = 0
y p = 0 + 0.5 × 1 + 0 × 0 = 0.5
z p = 1 + 0.5 × (−1) + 0 × 0 = 0.5.

```

The point (0, 0.5, 0.5) has position vector p, where
```
 √
p = 02 + 0.52 + 0.52 = 22

```

the plane equation is

```
0.5 0.5 √
0x + √ y+√ z − 2/2 = 0
2/2 2/2

```

which simplifies to
```
y + z − 1 = 0.



```

15.8.5 Plane Equation from Three Points

Very often in computer graphics problems we need to find the plane equation from
three known points. To begin with, the three points must be distinct and not lie on a
line. Figure 15.34 shows three points R, S and T , from which we create two vectors
```
−
→ −→
```

u = RS and v = RT . The vector product u × v then provides a vector normal to
the plane containing the original points. We now take another point P(x, y, z) and
```
−→
```

form a vector w = R P. The scalar product w · (u × v) = 0 if P is in the plane

<a id='p372'></a>
<!-- Página 372 -->

358 15 Analytic Geometry

Fig. 15.34 The vectors used
to determine a plane
equation from three points
R, S and T u×v

## R


```
w v
```


## P T

```
u

```


## S




containing the original points. This condition can be expressed as a determinant and
converted into the general equation of a plane. The three points are assumed to be in
an anticlockwise sequence viewed from the direction of the surface normal.
We begin with
```
i j k
u × v = xu yu z u .
xv yv z v

```

As w is perpendicular to u × v

```
xw yw z w
w · (u × v) = xu yu z u = 0.
xv yv z v

```

Expanding the determinant we obtain

```
yu z u z x x y
xw + yw u u + z w u u = 0
yv z v z v xv xv yv

```

which becomes

```
yS − y R z S − z R z − z R xS − x R
(x − x R ) + (y − y R ) S
yT − y R z T − z R zT − z R xT − x R
x S − x R yS − y R
+ (z − z R ) = 0.
x T − x R yT − y R

```

This can be arranged in the form ax + by + cz + d = 0 where

```
yS − y R z S − z R z − z R xS − x R
a= , b= S
yT − y R z T − z R xT − z R xT − x R
```


<a id='p373'></a>
<!-- Página 373 -->

15.8 Equation of a Plane 359

```
x S − x R yS − y R
c= , d = −(ax R + by R + cz R )
x T − x R yT − y R

```

or

```
1 yR z R xR 1 zR x R yR 1
a = 1 yS z S , b = x S 1 z S , c = x S yS 1
1 yT z T xT 1 zT x T yT 1
d = −(ax R + by R + cz R ).

```

As an example, consider the three points R(0, 0, 1), S(1, 0, 0), T (0, 1, 0).
Therefore,

```
101 011 001
a = 1 0 0 = 1, b = 1 1 0 = 1, c = 1 0 1 = 1
110 010 011
d = −(1 × 0 + 1 × 0 + 1 × 1) = −1

```

and the plane equation is
```
x + y + z − 1 = 0.



```

15.9 Intersecting Planes

When two non-parallel planes intersect, they form a straight line at the intersection,
which is parallel to both planes. This line can be represented as a vector, whose
direction is revealed by the vector product of the planes’ surface normals. However,
we require a point on this line to establish a unique vector equation; a useful point is
chosen as P0 , whose position vector p0 is perpendicular to the line.


Fig. 15.35 Two intersecting Y
planes create a line of n2
intersection


```
P0 P n3

p0 p n1



```


## X


## Z


<a id='p374'></a>
<!-- Página 374 -->

360 15 Analytic Geometry

Figure 15.35 shows two planes with normal vectors n1 and n2 intersecting to
create a line represented by n3 , whilst P0 (x0 , y0 , z 0 ) is a particular point on n3 and
P(x, y, z) is any point on the line.
We start the analysis by defining the surface normals:

```
n1 = a1 i + b1 j + c1 k
n2 = a2 i + b2 j + c2 k

```

next we define p and p0 :

```
p = xi + yj + zk
p0 = x0 i + y0 j + z 0 k.

```

Now we state the plane equations in vector form:

```
n1 · p + d1 = 0
n2 · p + d2 = 0.

```

The geometric significance of the scalars d1 and d2 has already been described above.
Let’s now define the line of intersection as

```
p = p0 + λn3

```

where λ is a scalar.
As the line of intersection must be orthogonal to n1 and n2 :

```
n3 = a3 i + b3 j + c3 k = n1 × n2 .

```

Now we introduce P0 as this must satisfy both plane equations, therefore,

```
n1 · p0 = −d1 (15.31)
n2 · p0 = −d2 (15.32)

```

and as P0 is such that p0 is orthogonal to n3

```
n3 · p0 = 0. (15.33)

```

Equations (15.31)–(15.33) form three simultaneous equations, which reveal the point
P0 . These are represented in matrix form as
```
⎡ ⎤ ⎡ ⎤⎡ ⎤
−d1 a1 b1 c1 x0
⎣ −d2 ⎦ = ⎣ a2 b2 c2 ⎦ ⎣ y0 ⎦
0 a3 b3 c3 z0
```


<a id='p375'></a>
<!-- Página 375 -->

15.9 Intersecting Planes 361

or ⎡ ⎤ ⎡ ⎤⎡ ⎤
```
d1 a1 b1 c1 x0
⎣ d2 ⎦ = − ⎣ a2 b2 c2 ⎦ ⎣ y0 ⎦
0 a3 b3 c3 z0

```

therefore,
```
x0 y0 z0 −1
= = =
d1 b1 c1 a1 d1 c1 a1 b1 d1 DET
d2 b2 c2 a2 d2 c2 a2 b2 d2
0 b3 c3 a3 0 c3 a3 b3 0

```

which enables us to state

```
b1 c1 b c
d2 − d1 2 2
b3 c3 b3 c3
x0 =
```


## DET

```
a3 c3 a c
d2 − d1 3 3
a1 c1 a2 c2
y0 =
```


## DET



```
a1 b1 a b
d2 − d1 2 2
a3 b3 a3 b3
z0 =
```


## DET

where
```
a1 b1 c1
D E T = a2 b2 c2 .
a3 b3 c3

```

The line of intersection is then given by

```
p = p0 + λn3 .

```

If D E T = 0 the line and plane are parallel.
To illustrate this, let the two intersecting planes be the xy-plane and the yz-plane,
which means that the line of intersection will be the y-axis, as shown in Fig. 15.36.
The plane equations are z = 0 and x = 0, therefore,

```
n1 = k
n2 = i

```

and d1 = d2 = 0.
We now compute n3 , D E T , x0 , y0 , z 0 :

<a id='p376'></a>
<!-- Página 376 -->

362 15 Analytic Geometry

Fig. 15.36 Two intersecting Y
planes creating a line of
intersection coincident with
the y-axis P
```
n3



```


## P0

```
Z n2 n1 X


i jk
n3 = 0 0 1 = j
100
001
```


## DET = 1 0 0 = 1

```
010
01 00
0 −0
10 10
x0 = =0
1
00 00
0 −0
01 10
y0 = =0
1
00 10
0 −0
01 01
z0 = = 0.
1
```

Therefore, the line equation is p = λn3 , where n3 = j, which is the y-axis.



15.9.1 Intersection of Three Planes

Three mutually intersecting planes will intersect at a point as shown in Fig. 15.37, and
we can find this point by using a similar strategy to the one used in two intersecting
planes by creating three simultaneous plane equations using determinants.
Figure 15.37 shows the common point P(x, y, z) . The three planes can be
defined by the following equations:

```
a1 x + b1 y + c1 z + d1 = 0
a2 x + b1 y + c2 z + d2 = 0
```


<a id='p377'></a>
<!-- Página 377 -->

15.9 Intersecting Planes 363

Fig. 15.37 Three mutually Y
intersecting planes





## P


## Z X




```
a3 x + b1 y + c3 z + d3 = 0

```

which means that they can be rewritten as
```
⎡ ⎤ ⎡ ⎤⎡ ⎤
−d1 a1 b1 c1 x
⎣ −d2 ⎦ = ⎣ a2 b2 c2 ⎦ ⎣ y ⎦
−d3 a3 b3 c3 z

```

or ⎡ ⎤ ⎡ ⎤⎡ ⎤
```
d1 a1 b1 c1 x
⎣ d2 ⎦ = − ⎣ a2 b2 c2 ⎦ ⎣ y ⎦
d3 a3 b3 c3 z

```

or in determinant form
```
x y z −1
= = =
d1 b1 c1 a1 d1 c1 a1 b1 d1 DET
d2 b2 c2 a2 d2 c2 a2 b2 d2
d3 b3 c3 a3 d3 c3 a3 b3 d3

```

where
```
a1 b1 c1
D E T = a2 b2 c2 .
a3 b3 c3

```

Therefore, we can state that

```
d1 b1 c1
d2 b2 c2
d3 b3 c3
x =−
```


## DET


<a id='p378'></a>
<!-- Página 378 -->

364 15 Analytic Geometry

Fig. 15.38 Three planes Y
intersecting at a point P
```
2
k
j
```


## P


```
i+j+k


2 2
```


## Z X



```
a1 d1 c1
a2 d2 c2
a3 d3 c3
y=−
```


## DET

```
a1 b1 d1
a2 b2 d2
a3 b3 d3
z=− .
```


## DET

If D E T = 0, two of the planes at least, are parallel. Let’s test these equations
with a simple example.
The planes shown in Fig. 15.38 have the following equations:

```
x +y+z−2=0
z=0
y−1=0

```

therefore,

```
111
```


## D E T = 0 0 1 = −1

```
010
−2 1 1
001
−1 1 0
x =− =1
−1
```


<a id='p379'></a>
<!-- Página 379 -->

15.9 Intersecting Planes 365

```
1 −2 1
0 01
0 −1 0
y=− =1
−1
1 1 −2
00 0
0 1 −1
z=− =0
−1

```

which means that the intersection point is (1, 1, 0), which is correct.



15.9.2 Angle Between Two Planes

Calculating the angle between two planes is relatively easy and can be found by
taking the dot product of the planes’ normals. Figure 15.39 shows two planes with α
representing the angle between the two surface normals n1 and n2 .
Let the plane equations be

```
ax1 + by1 + cz 1 + d1 = 0
ax2 + by2 + cz 2 + d2 = 0

```

therefore, their surface normals are

```
n1 = a1 i + b1 j + c1 k
n2 = a2 i + b2 j + c2 k.

```

Taking the dot product of n1 and n2 :

```
n1 · n2 = n1  n2  cos α


```

Fig. 15.39 The angle Y
between two planes is the
angle between their surface n1
normals
```
α
n2




```


## Z X


<a id='p380'></a>
<!-- Página 380 -->

366 15 Analytic Geometry

Fig. 15.40 α is the angle Y
between two planes
```
1

n1
α
n2

1 1

```


## Z X




and  
```
n1 · n2
α = cos−1 .
n1  n2 

```

For example, Fig. 15.40 shows two planes with normal vectors n1 and n2 .
The plane equations are

```
x +y+z−1=0
z=0

```

therefore,

```
n1 = i + j + k
n2 = k

```

therefore,
```
√
n1  = 3
n2  = 1

```

and  
```
α = cos−1 √1
3
≈ 54.74◦ .



```

15.9.3 Angle Between a Line and a Plane

The angle between a line and a plane is calculated using a similar technique used for
calculating the angle between two planes. If the line equation employs a direction

<a id='p381'></a>
<!-- Página 381 -->

15.9 Intersecting Planes 367

Fig. 15.41 α is the angle
between the plane’s surface
normal and the line’s Y
direction vector

```
T P n
α v
t
p


```


## Z X




vector, the angle is determined by taking the dot product of this vector and between
the plane’s normal. Figure 15.41 shows such a scenario where n is the plane’s surface
normal and v is the line’s direction vector.
Let the plane equation be

```
ax + by + cz + d = 0

```

then its surface normal is
```
n = ai + bj + ck.

```

Let the line’s direction vector be v and T (xt yt , z t ) is a point on the line, then any
point on the line is given by the position vector p :

```
p = t + λv

```

therefore, we can write

```
n · v = n v cos α
 
n·v
α = cos−1 .
n v

```

When the line is parallel to the plane n · v = 0.
Consider the scenario illustrated in Fig. 15.42 where the plane equation is

```
x +y+z−1=0

```

therefore, the surface normal is given by n:

```
n =i+j+k
```


<a id='p382'></a>
<!-- Página 382 -->

368 15 Analytic Geometry

Fig. 15.42 The required Y
angle is between a and b
```
1
a
n




1 1

```


## Z X




and the line’s direction vector is a:

```
a =i+j

```

therefore,
```
√
n = 3
√
a = 2

```

and  
```
α = cos−1 √2
6
≈ 35.26◦ .



```

15.9.4 Intersection of a Line with a Plane

Given a line and a plane, they will either intersect, or not, if they are parallel. Either
way, both conditions can be found using some simple vector analysis, as shown in
Fig. 15.43. The objective is to identify a point P that is on the line and the plane.
Let the plane equation be

```
ax + by + cz + d = 0

```

where
```
n = ai + bj + ck.

```

P is a point on the plane with position vector

```
p = xi + yj + zk
```


<a id='p383'></a>
<!-- Página 383 -->

15.9 Intersecting Planes 369

Fig. 15.43 The vectors Y
required to determine n
whether a line and plane
intersect

## T


## P

```
v
t p



```


## Z X




therefore,
```
n · p + d = 0.

```

Let the line equation be
```
p = t + λv

```

where
```
t = xt i + yt j + z t k

```

and
```
v = xv i + yv j + z v k

```

therefore, the line and plane will intersect for some λ such that

```
n · (t + λv) + d = n · t + λn · v + d = 0.

```

Therefore,
```
−(n · t + d)
λ=
n·v
```

for the intersection point. The position vector for P is p = t + λv.
If n · v = 0 the line and plane are parallel.
Let’s test this result with the scenario shown in Fig. 15.44.
Given the plane

```
x +y+z−1=0
n =i+j+k

```

and the line
```
p = t + λv
```


<a id='p384'></a>
<!-- Página 384 -->

370 15 Analytic Geometry

Fig. 15.44 P identifies the Y
intersection point of the line
and the plane 1
```
v
n
P (x, y, z)




```


## 1 T 1



## Z X




where

```
t=0
v =i+j

```

then
```
−(1 × 0 + 1 × 0 + 1 × 0 − 1)
λ= = 0.5
1×1+1×1+1×0

```

and the point of intersection is P(0.5, 0.5, 0).



15.10 Summary

Mixing vectors with geometry is a powerful analytical tool, and helps us solve many
problems associated with computer graphics, encountered in rendering, modelling,
collision detection and physically-based animation. Unfortunately, there has not been
space to investigate every topic, but hopefully, what has been covered, will enable
the reader solve other problems with greater confidence.

<a id='p385'></a>
<!-- Página 385 -->


## Chapter 16

Barycentric Coordinates




16.1 Introduction

Cartesian coordinates are a fundamental concept in mathematics and are central to
computer graphics. Such rectangular coordinates are just offsets relative to some
origin. Other coordinate systems also exist such as polar, spherical and cylindrical
coordinates, and they too, require an origin. Barycentric coordinates, on the other
hand, locate points relative to existing points, rather than to an origin and are known
as local coordinates.



16.2 Background

The German mathematician August Möbius is credited with their discovery. ‘barus’
is the Greek entomological root for ‘heavy’, and barycentric coordinates were originally used for identifying the centre of mass of shapes and objects. It is interesting
to note that the prefixes ‘bari’, ‘bary’ and ‘baro’ have also influenced other words
such as baritone, baryon (heavy atomic particle) and barometer.
```
Although barycentric coordinates are used in geometry, computer graphics, rel-
```

ativity and global time systems, they do not appear to be a major topic in a typical
math syllabus. Nevertheless, they are important and I would like to describe what
they are and how they can be used in computer graphics.
```
The idea behind barycentric coordinates can be approached from different direc-
```

tions, and I have chosen mass points and linear interpolation. But before we begin
this analysis, it will be useful to investigate a rather elegant theorem known as Ceva’s
Theorem, which we will invoke later in this chapter.




© Springer-Verlag London Ltd., part of Springer Nature 2022 371
J. Vince, Mathematics for Computer Graphics, Undergraduate Topics
in Computer Science, https://doi.org/10.1007/978-1-4471-7520-9_16

<a id='p386'></a>
<!-- Página 386 -->

372 16 Barycentric Coordinates

16.3 Ceva’s Theorem

The Italian mathematician Giovanni Ceva (1647–1734) is credited with a theorem
associated with the concurrency of lines in a triangle. It states that: In a triangle
ΔABC, the lines A A , B B  and CC  , where A , B  and C  are points on the opposite
sides facing vertices A, B and C respectively, are concurrent (intersect at a common
point) if, and only if

## AC  B A C B 

```
· · = 1.
```


## C  B A C B  A

Figure 16.1 shows such a scenario.
There are various ways of proving this theorem, and Alfred Posamentier provides
one [1]; but perhaps the simplest proof is as follows.
Figure 16.2 shows triangle ΔABC with line A A extended to R and B B  extended
to S, where line S R is parallel to line AB. The resulting geometry creates a number
of similar triangles:


## A C CR


## ΔAB A : ΔRC A ⇒ = (16.1)


## B A AB



Fig. 16.1 The geometry C
associated with Ceva’s
Theorem



## A


## B


## P






## A C B



Fig. 16.2 The geometry for S C R
proving Ceva’s Theorem




## B A



## P






## A C B


<a id='p387'></a>
<!-- Página 387 -->

16.3 Ceva’s Theorem 373


## B A AB


## ΔAB B  : ΔC S B  ⇒ = (16.2)


## C B SC


## C B C P


## ΔB PC  : ΔC S P ⇒ = (16.3)


## SC PC

```

```


## AC C P


## ΔAC  P : ΔRC P ⇒ = . (16.4)


## CR PC

From (16.3) and (16.4) we get

## C B AC 

```
=
```


## SC CR

which can be rewritten as

## C B SC

```
= . (16.5)
```


## AC  CR

The product of (16.1), (16.2) and (16.5) is


## A C B  A C  B C R AB SC

```

· 
· 
= · · = 1. (16.6)
```


## B A C B AC AB SC C R

Rearranging the terms of (16.6) we get


## AC  B A C B 

```
· · =1
```


## C  B A C B  A

which is rather an elegant relationship.



16.4 Ratios and Proportion

Central to barycentric coordinates are ratios and proportion, so let’s begin by revising
some fundamental formulae used in calculating ratios.
Imagine the problem of dividing £100 between two people in the ratio 2 : 3. The
solution lies in the fact that the money is divided into 5 parts (2 + 3), where 2 parts
go to one person and 3 parts to the other person. In this case, one person receives
£40 and the other £60. At a formal level, we can describe this as follows.
A scalar A can be divided into the ratio r : s using the following expressions:
```
r s
A and A.
r +s r +s

```

Note that r s
```
+ =1
r +s r +s
```


<a id='p388'></a>
<!-- Página 388 -->

374 16 Barycentric Coordinates

and r s
```
1− = .
r +s r +s

```

Furthermore, the above formulae can be extended to incorporate any number of ratio
divisions. For example, A can be divided into the ratio r : s : t by the following:

```
r s t
A, A and A
r +s+t r +s+t r +s+t

```

similarly,
```
r s t
+ + = 1.
r +s+t r +s+t r +s+t

```

These expressions are very important as they show the emergence of barycentric coordinates. For the moment though, just remember their structure and we will investigate
some ideas associated with balancing weights.



16.5 Mass Points

We begin by calculating the centre of mass—the centroid—of two masses. Consider
the scenario shown in Fig. 16.3 where two masses m A and m B are placed at the ends
of a massless rod.
If m A = m B a state of equilibrium is achieved by placing the fulcrum mid-way
between the masses. If the fulcrum is moved towards m A , mass m B will have a turning
advantage and the rod rotates clockwise.
To calculate a state of equilibrium for a general system of masses, consider the
geometry illustrated in Fig. 16.4, where two masses m A and m B are positioned x A


Fig. 16.3 Two masses fixed
at the ends of a massless rod mA mB




Fig. 16.4 The geometry A B
used for equating turning mA + m B
moments mA mB


```
xA x̄ xB
x̄ − xA xB − x̄
```


<a id='p389'></a>
<!-- Página 389 -->

16.5 Mass Points 375

and x B at A and B respectively. When the system is in balance we can replace the
two masses by a single mass m A + m B at the centroid denoted by x̄ (pronounced ‘x
bar’).
A balance condition arises when the LHS turning moment equals the RHS turning
moment. The turning moment being the product of a mass by its offset from the
fulcrum. Equating turning moments, equilibrium is reached when

```
m B (x B − x̄) = m A (x̄ − x A )
m B x B − m B x̄ = m A x̄ − m A x A
(m A + m B )x̄ = m A x A + m B x B

m AxA + m B xB mA mB
x̄ = = xA + xB. (16.7)
mA + mB mA + mB mA + mB

```

For example, if m A = 6 and m B = 12, and positioned at x A = 0 and x B = 12 respectively, the centroid is located at

```
x̄ = 18
6
× 0 + 12
18
× 12 = 8.

```

Thus we can replace the two masses by a single mass of 18 located at x̄ = 8.
Note that the terms in (16.7) m A /(m A + m B ) and m B /(m A + m B ) sum to 1 and
are identical to those used above for calculating ratios. They are also called the
barycentric coordinates of x̄ relative to the points A and B.
Using the general form of (16.7) any number of masses can be analysed using

```

n
m i xi
i=1
x̄ = n

mi
i=1

```

where m i is a mass located at xi . Furthermore, we can compute the y-component of
the centroid ȳ using
```

n
m i yi
i=1
ȳ = n

mi
i=1

```

and in 3D the z-component of the centroid z̄ is

```

n
m i zi
i=1
z̄ = n .

mi
i=1
```


<a id='p390'></a>
<!-- Página 390 -->

376 16 Barycentric Coordinates

Fig. 16.5 The geometry
used for equating turning C mC
moments


```
A a
b
```


## B P̄





## C

```
A mA c mB B


```

To recap, (16.7) states that
```
mA mB
x̄ = xA + xB
mA + mB mA + mB

```

therefore, we can write
```
mA mB
ȳ = yA + yB
mA + mB mA + mB

```

which allows us to state
```
mA mB
```


## P̄ = A+ B

```
mA + mB mA + mB

```

where A and B are the position vectors for the mass locations A and B respectively,
and P̄ is the position vector for the centroid P̄.
If we extend the number of masses to three: m A , m B and m C , which are organised
as a triangle, then we can write
```
mA mB mC
P̄ = A+ B+ C. (16.8)
m A + m B + mC m A + m B + mC m A + m B + mC

The three multipliers of A, B and C are the barycentric coordinates of P̄ relative
```

to the points A, B and C. Note that the number of coordinates is not associated with
the number of spatial dimensions, but the number of reference points.
```
Now consider the scenario shown in Fig. 16.5. If m A = m B = m C then we can
```

determine the location of A , B  and C  as follows:

1. We begin by placing a fulcrum under A mid-way along BC as shown in
Fig. 16.6.
The triangle will balance because m B = m C and A is 21 a from C and 21 a
```
from B.
```


<a id='p391'></a>
<!-- Página 391 -->

16.5 Mass Points 377

2. Now we place the fulcrum under B mid-way along C A as shown in Fig. 16.7.
Once more the triangle will balance, because m C = m A and B  is 21 b from C and
1
2
```
b from A.
```

3. Finally, we do the same for C and AB. Figure 16.8 shows the final scenario.

Ceva’s Theorem confirms that the medians A A , B B  and CC  are concurrent at
P̄ because


Fig. 16.6 Balancing the
triangle along A A mA A



```
c b



```


## A

```
B mB 1
a
1
a
mC C
2 2




```

Fig. 16.7 Balancing the
triangle along B B  mB B
```
1
a
2

```


## A

```
c
1
a
2




C mC
B mA A
1 1
b b
2 2




```

Fig. 16.8 P̄ is the centroid
of the triangle mC C

```
1 1
b a
2 2

```


## B A

```
1
```


## P̄

```
b 1
2 a
2



```


## C

```
A mA 1 1
mB B
2
c mA + mB 2
c
```


<a id='p392'></a>
<!-- Página 392 -->

378 16 Barycentric Coordinates


## AC  B A C B  1

```
c 21 a 21 b
· · = 2
· · = 1.
```


## C  B A C B  A 1

```
2
c 21 a 21 b

```

Arbitrarily, we select the median C  C. At C  we have an effective mass of m A + m B
and m C at C. For a balance condition

```
(m A + m B ) × C  P̄ = m C × P̄C

```

and as the masses are equal, C  P̄ must be 13 along the median C  C.
If we use (16.8) we obtain


## P̄ = 13 A + 13 B + 13 C


which locates the coordinates of the centroid correctly.
```
Now let’s consider another example where m A = 1, m B = 2 and m C = 3, as
```

shown in Fig. 16.9. For a balance condition A must be 35 a from B and 25 a from C.
Equally, B  must be 41 b from C and 43 b from A. Similarly, C  must be 23 c from A and
1
3
c from B.
```
Ceva’s Theorem confirms that the lines A A , B B  and CC  are concurrent at P̄
```

because

## AC  B A C B  2

```
c 35 a 41 b
· · = 3
· · = 1.
```


## C  B A C B  A 1

```
3
c 25 a 43 b

```

Arbitrarily select C  C. At C  we have an effective mass of 3 (1 + 2) and 3 at C,
which means that for a balance condition P̄ is mid-way along C  C. Similarly, P̄ is
1
6
along A A and 13 along B  B.
Once more, using (16.8) in this scenario we obtain


## P̄ = 16 A + 13 B + 21 C.


Note that the multipliers of A, B and C are identical to the proportions of P̄ along
A A, B  B and C  C. Let’s prove why this is so.


Fig. 16.9 How the masses
determine the positions of
```
1
```


## 3 C

A , B  and C  4
```
b

```


## B 2

```
5
a

```


## A


## P̄

```
3
b
4
3
a
5




```


## A 1 2 1 2 B

```
3
c C 3
c
```


<a id='p393'></a>
<!-- Página 393 -->

16.5 Mass Points 379

Fig. 16.10 How the masses
determine the positions of mC C
A , B  and C  mA
```
mA + mC mB
mB + mC

```


## B A

```
mC P̄ mC
mA + mC mB + mC




A mA mB mA
mB B
mA + mB C mA + mB




```

Figure 16.10 shows three masses with the triangle’s sides divided into their various
proportions to derive P̄.
On the line A A we have m A at A and effectively m B + m C at A , which means that
P̄ divides A A in the ratio m A /(m A + m B + m C ) : (m B + m C )/(m A + m B + m C ).
On the line B  B we have m B at B and effectively m A + m C at B  , which means that
P̄ divides B  B in the ratio m B /(m A + m B + m C ) : (m A + m C )/(m A + m B + m C ).
Similarly, on the line C  C we have m C at C and effectively m A + m B at C  , which
means that P̄ divides C  C in the ratio m C /(m A + m B + m C ) : (m A + m B )/(m A +
m B + m C ).
To summarise, given three masses m A , m B and m C located at A, B and C respectively, the centroid P̄ is given by
```
mA mB mC
P̄ = A+ B+ C. (16.9)
m A + m B + mC m A + m B + mC m A + m B + mC

```

If we accept that m A , m B and m C can have any value, including zero, then the barycentric coordinates of P̄ will be affected by these values. For example, if m B = m C = 0
and m A = 1, then P̄ will be located at A with barycentric coordinates (1, 0, 0).
Similarly, if m A = m C = 0 and m B = 1, then P̄ will be located at B with barycentric coordinates (0, 1, 0). And if m A = m B = 0 and m C = 1, then P̄ will be located
at C with barycentric coordinates (0, 0, 1).
```
Now let’s examine a 3D example as illustrated in Fig. 16.11. The figure shows
```

three masses 4, 8 and 12 and their equivalent mass 24 located at (x̄, ȳ, z̄).
```
The magnitude and coordinates of three masses are shown in Table 16.1, together
```

with the barycentric coordinate ti . The column headed ti expresses the masses as
fractions of the total mass: i.e.
```
mi
ti =
m1 + m2 + m3

```

and we see that the centroid is located at (5, 5, 3).
Having discovered barycentric coordinates in weight balancing, let’s see how they
emerge in linear interpolation.

<a id='p394'></a>
<!-- Página 394 -->

380 16 Barycentric Coordinates

Fig. 16.11 Three masses Y
can be represented by a
single mass located at the
centroid
```
24
4
8
ȳ
12
Z x̄ X
z̄

```

Table 16.1 The magnitude and coordinates of three masses
mi ti xi yi zi ti xi ti yi ti z i
```
1
```

12 2 8 6 2 4 3 1
```
1 2
```

8 3 2 3 3 3 1 1
```
1 1
```

4 6 2 6 6 3 1 1
```
x̄ = 5 ȳ = 5 z̄ = 3




```

16.6 Linear Interpolation

Suppose that we wish to find a value mid-way between two scalars A and B. We
could proceed as follows:


## V = A + 21 (B − A)


## = 21 A + 21 B


which seems rather obvious. Similarly, to find a value one-third between A and B,
we can write:


## V = A + 13 (B − A)


## = 23 A + 13 B.


Generalising, to find some fraction t between A and B we can write

```
V = (1 − t)A + t B. (16.10)

```

For example, to find a value 43 between 10 and 18 we have
```
 
```


## V = 1 − 43 × 10 + 43 × 18 = 16.


<a id='p395'></a>
<!-- Página 395 -->

16.6 Linear Interpolation 381

Although this is a trivial formula, it is very useful when interpolating between two
numerical values. Let us explore (16.10) in greater detail.
To begin with, it is worth noting that the multipliers of A and B sum to 1:

```
(1 − t) + t = 1.

```

Rather than using (1 − t) as a multiplier, it is convenient to make a substitution such
as s = 1 − t , and we have
```
V = sA + tB

```

where
```
s =1−t

```

and
```
s + t = 1.

```

Equation (16.10) is called a linear interpolant as it linearly interpolates between
A and B using the parameter t. It is also known as a lerp. The terms s and t are the
barycentric coordinates of V as they determine the value of V relative to A and B .
Now let’s see what happens when we substitute coordinates for scalars. We start
with 2D coordinates A(x A , y A ) and B(x B , y B ), and position vectors A, B and C
and the following linear interpolant

```
V = sA + tB

```

where
```
s =1−t

```

and
```
s+t =1

```

then

```
x V = sx A + t x B
yV = sy A + t y B .


```

Figure 16.12 illustrates what happens when t varies between 0 and 1.
The point V slides along the line connecting A and B. When t = 0, V is coincident
with A, and when t = 1, V is coincident with B. You should not be surprised that
the same technique works in 3D.
Now let’s extend the number of vertices to three in the form of a triangle as shown
in Fig. 16.13. This time we will use r , s and t to control the interpolation. We would
start as follows:

<a id='p396'></a>
<!-- Página 396 -->

382 16 Barycentric Coordinates


## Y

```
yB
```


## B

```
t=1


yV V


yA A
t=0


xA xV xB X
```

Fig. 16.12 The position of V slides between A and B as t varies between 0 and 1




## Y

```
yC
t=1
```


## C


```
yV V

yA A
r=1 B
yB
s=1
xA xV xB xC X
```

Fig. 16.13 The position of V moves between A, B and C depending on the value r, s and t



```
V = r A + sB + tC

```

where A, B and C are the position vectors for A, B and C respectively, and V is the
position vector for the point V .
Let
```
r =1−s−t

```

and
```
r + s + t = 1.

```

Once more, we begin with 2D coordinates A(x A , y A ), B(x B , y B ) and C(xC , yC )
where

<a id='p397'></a>
<!-- Página 397 -->

16.6 Linear Interpolation 383

```
x V = r x A + sx B + t xC
yV = r y A + sy B + t yC .

```

When

```
r = 1, V is coincident with A
s = 1, V is coincident with B
t = 1, V is coincident with C.

```

Similarly, when

```
r = 0, V is located on the edge BC
s = 0, V is located on the edge C A
t = 0, V is located on the edge AB.

```

For all other values of r , s and t, where r + s + t = 1 and 0 ≤ r, s, t ≤ 1, V is inside
triangle ΔABC , otherwise it is outside the triangle.
```
The triple (r, s, t) are barycentric coordinates and locate points relative to A, B
```

and C, rather than an origin. For example, the barycentric coordinates of A, B and
C are (1, 0, 0), (0, 1, 0) and (0, 0, 1) respectively.
```
All of the above formulae work equally well in three dimensions, so let’s inves-
```

tigate how barycentric coordinates can locate points inside a 3D triangle. However,
before we start, let’s clarify what we mean by inside a triangle. Fortunately, barycentric coordinates can distinguish points within the triangle’s three sides; points coincident with the sides; and points outside the triangle’s boundary. The range and
value of the barycentric coordinates provide the mechanism for detecting these three
conditions.
```
As an example, Fig. 16.14 illustrates a scenario with the points P1 (x1 , y1 , z 1 ),
```

P2 (x2 , y2 , z 2 ) and P3 (x3 , y3 , z 3 ). Using barycentric coordinates we can state that
any point P0 (x0 , y0 , z 0 ) inside or on the edge of triangle ΔP1 P2 P3 is defined by


Fig. 16.14 A 3D triangle Y P3




## P0


## P1






## Z X


## P2


<a id='p398'></a>
<!-- Página 398 -->

384 16 Barycentric Coordinates

```
x0 = r x1 + sx2 + t x3
y0 = r y1 + sy2 + t y3
z 0 = r z 1 + sx2 + t z 3

```

where r + s + t = 1 and 0 ≤ r, s, t, ≤ 1.
If the triangle’s vertices are P1 (0, 2, 0), P2 (0, 0, 4) and P3 (3, 1, 2) then we
can choose different values of r , s and t to locate P0 inside the triangle. However, I
would also like to confirm that P0 lies on the plane containing the three points. To
do this we require the plane equation for the three points, which can be derived as
follows.
Given P1 (x1 , y1 , z 1 ), P2 (x2 , y2 , z 2 ) and P3 (x3 , y3 , z 3 ), and the target plane
equation ax + by + cz + d = 0, then
```
 
 1 y1 z 1 
 
a =  1 y2 z 2 
 1 y3 z 3 
 
 x1 1 z 1 
 
b =  x2 1 z 2 
 x3 1 z 3 
 
 x1 y1 1 
 
c =  x2 y2 1 
 x3 z 2 1 
d = −(ax1 + by1 + cz 1 )

```

thus
```
 
1 2 0
 
a =  1 0 4  = 0
1 1 2
 
0 1 0
 
b =  0 1 4  = 12
3 1 2
 
0 2 1
 
c =  0 0 1  = 6
3 1 1
d = −24

```

therefore, the plane equation is

```
12y + 6z = 24. (16.11)
```


<a id='p399'></a>
<!-- Página 399 -->

16.6 Linear Interpolation 385

Table 16.2 The barycentric coordinates of P0
r s t x0 y0 z0 12y0 + 6z 0
1 0 0 0 2 0 24
0 1 0 0 0 4 24
0 0 1 3 1 2 24
1 1 1
4 4 2 1 21 1 2 24
```
1 1
```

0 2 2 1 21 1
```
2 3 24
```

1 1
2 2 0 0 1 2 24
1 1 1
3 3 3 1 1 2 24




If we substitute a point (x0 , y0 , z 0 ) in the LHS of (16.11) and obtain a value of 24,
then the point is on the plane.
```
Table 16.2 shows various values of r , s and t, and the corresponding position of
```

P0 . The table also confirms that P0 is always on the plane containing the three points.
```
Now we are in a position to test whether a point is inside, on the boundary or
```

outside a 3D triangle.
```
We begin by writing the three simultaneous equations defining P0 in matrix form
⎡ ⎤ ⎡ ⎤⎡ ⎤
x0 x1 x2 x3 r
⎣ y0 ⎦ = ⎣ y1 y2 y3 ⎦ ⎣ s ⎦
z0 z1 z2 z3 t

```

therefore,
```
r s t 1
 = = = 
 x0 x2 x3   x1 x0 x3   x1 x2 x0   x1 x2 x3 
       
 y0 y2 y3   y1 y0 y3   y1 y2 y0   y1 y2 y3 
       
 z0 z2 z3   z1 z0 z3   z1 z2 z0   z1 z2 z3 

```

and
```
 
 x0 x2 x3 
 
 y0 y2 y3 
 
 z0 z2 z3 
r=
```


##  DET 

```
 x1 x0 x3 
 
 y1 y0 y3 
 
 z1 z0 z3 
s=
```


##  DET 

```
 x1 x2 x0 
 
 y1 y2 y0 
 
 z1 z2 z0 
t=
```


## DET


<a id='p400'></a>
<!-- Página 400 -->

386 16 Barycentric Coordinates
```
 
 x1 x2 x3 
 
D E T =  y1 y2 y3  .
 z1 z2 z3 

```

Using the three points P1 (0, 2, 0), P2 (0, 0, 4), P3 (3, 1, 2) and arbitrary positions of P0 , the values of r , s and t identify whether P0 is inside or outside triangle
ΔABC. For example, the point P0 (0, 2, 0) is a vertex and is classified as being on
the boundary. To confirm this we calculate r , s and t, and show that r + s + t = 1:
```
 
0 0 3
 
```


## D E T =  2 0 1  = 24

```
0 4 2
 
0 0 3
 
2 0 1
 
0 4 2
r= =1
 24 
0 0 3
 
2 2 1
 
0 0 2
s= =0
 24 
0 0 0
 
2 0 2
 
0 4 0
t= =0
24
```

therefore r + s + t = 1, but both s and t are zero which confirms that the point
(0, 2, 0) is on the boundary. In fact, as both coordinates are zero it confirms that
the point is located on a vertex.
Now let’s deliberately choose a point outside the triangle. For example,
P0 (4, 0, 3) is outside the triangle, which is confirmed by the corresponding values of r , s and t:
```
 
4 0 3
 
0 0 1
 
3 4 2
r= = − 23
 24 
0 4 3
 
2 0 1
 
0 3 2
s= = 43
 24 
0 0 4
 
2 0 0
 
0 4 3
t= = 43
24
```


<a id='p401'></a>
<!-- Página 401 -->

16.6 Linear Interpolation 387

therefore,
```
r + s + t = − 23 + 34 + 43 = 1 12
5



```

which confirms that the point (4, 0, 3) is outside the triangle. Note that r < 0 and
t > 1 , which individually confirm that the point is outside the triangle’s boundary.



16.7 Convex Hull Property

We have already shown that it is possible to determine whether a point is inside or
outside a triangle. But remember that triangles are always convex. So can we test
whether a point is inside or outside any polygon? Well the answer is no, unless the
polygon is convex. The reason for this can be understood by considering the concave
polygon shown in Fig. 16.15.
Let the barycentric coordinates for a point P0 be

```
P0 = r A + sB + tC + uD

```

where r + s + t + u = 1. When t = 0, P0 can exist anywhere inside triangle ΔAB D.
Thus, if any vertex creates a concavity, it will be ignored by barycentric coordinates.



16.8 Areas

Barycentric coordinates are also known as areal coordinates due to their area dividing
properties. For example, in Fig. 16.16 the areas of the three internal triangles are in
proportion to the barycentric coordinates of the point P.
To prove this, let P have barycentric coordinates

```
P = r A + sB + tC


```

Fig. 16.15 A concave B
polygon





## C



## A



## D


<a id='p402'></a>
<!-- Página 402 -->

388 16 Barycentric Coordinates

Fig. 16.16 The areas of the C
internal triangles are directly
proportional to the
barycentric coordinates of P




```
sΔABC rΔABC
```


## P


```
tΔABC
```


## A B



where
```
r + s + t = 1, and 0 ≤ (r, s, t) ≤ 1.


If we use the notation area(ΔABC) to represent the area of the triangle formed
from the vertices A, B and C then area(ΔABC) is the sum of the areas of the smaller
```

triangles:

```
area(ΔABC) = area(ΔAB P) + area(ΔBC P) + area(ΔC A P).

```

But the area of any 2D triangle ΔP1 P2 P3 is
```
 
 x1 y1 1 
 
area(ΔP1 P2 P3 ) = 21  x2 y2 1 
 x3 y3 1 

```

therefore,  
```
 x A yA 1 
 
area(ΔAB P) = 21  x B y B 1 
 x P yP 1 

```

but
```
x P = r x A + sx B + t xC

```

and
```
y P = r y A + sy B + t yC

```

therefore,

<a id='p403'></a>
<!-- Página 403 -->

16.8 Areas 389
```
 
 xA yA 1 

area(ΔAB P) = 21  xB yB 1 
 r x A + sx B + t xC r y A + sy B + t yC 1 

```

which expands to

```
x A y B + r x B y A + sx B y B + t x B yC + r x A y A + sx B y A + t xC y A
area(ΔAB P) = 21
−r x A y A − sx A y B − t x A yC − x B y A − r x A y B − sx B y B − t xC y B
x A y B − x B y A + r (x B y A − x A y B ) + s(x B y A − x A y B )
= 21
+t (x B yC − xC y B ) + t (xC y A − x A yC )
x A y B − x B y A + (1 − t)(x B y A − x A y B ) + t (x B yC − xC y B )
= 21
+t (xC y A − x A yC )
= 21 [−t x B y A + t x A y B + t x B yC − t xC y B + t xC y A − t x A yC ]


```

and simplifies to
```
 
 x A yA 1 
 
area(ΔAB P) = 21 t  x B y B 1  = t × area(ΔABC)
 xC yC 1 

```

therefore,
```
area(ΔAB P)
t=
area(ΔABC)

```

similarly,  
```
 x A yA 1 
 
area(ΔBC P) = 21 r  x B y B 1  = r × area(ΔABC)
 xC yC 1 

area(ΔBC P)
r=
area(ΔABC)

```

and  
```
 x A yA 1 
 
area(ΔC A P) = 21 s  x B y B 1  = s × area(ΔABC)
 xC yC 1 

area(ΔC A P)
s= .
area(ΔABC)

```

Thus, we see that the areas of the internal triangles are directly proportional to the
barycentric coordinates of P.
This is quite a useful relationship and can be used to resolve various geometric
problems. For example, let’s use it to find the radius and centre of the inscribed circle
for a triangle. We could approach this problem using classical Euclidean geome-

<a id='p404'></a>
<!-- Página 404 -->

390 16 Barycentric Coordinates

Fig. 16.17 The inscribed C
circle in triangle ΔABC




```
b
a
```


## P


## R




```
A c B


```

try, but barycentric coordinates provide a powerful analytical tool for resolving the
problem very quickly. Consider triangle ΔABC with sides a, b and c as shown in
Fig. 16.17. The point P is the centre of the inscribed circle with radius R. From our
knowledge of barycentric coordinates we know that

```
P = r A + sB + tC

```

where
```
r + s + t = 1. (16.12)

```

We also know that the area properties of barycentric coordinates permit us to state

```
area(ΔBC P) = r × area(ΔABC) = 21 a R
area(ΔC A P) = s × area(ΔABC) = 21 b R
area(ΔAB P) = t × area(ΔABC) = 21 c R

```

therefore,

```
aR bR cR
r= , s= , t=
2 × area(ΔABC) 2 × area(ΔABC) 2 × area(ΔABC)

```

substituting r , s and t in (16.12) we get


## R

```
(a + b + c) = 1
2 × area(ΔABC)

```

and
```
2 × area(ΔABC)
```


## R= .

```
a+b+c

```

Substituting R in the definitions of r , s and t we obtain

<a id='p405'></a>
<!-- Página 405 -->

16.8 Areas 391

Fig. 16.18 The inscribed Y
circle for a triangle
```
10



√
200

P (xP , yP )
```


## R





## 10 X



```
a b c
r= s= t=
a+b+c a+b+c a+b+c

```

and

```
x P = r x A + sx B + t xC
y P = r y A + sy B + t yC .


```

√ To test this solution, consider the right-angled triangle in Fig. 16.18, where a =
200, b = 10, c = 10 and area(ΔABC) = 50. Therefore

```
2 × 50
```


## R= √ ≈ 2.929

```
10 + 10 + 200

```

and
```
√
200 10 10
```

r= ≈ 0.4142, s = ≈ 0.2929, t = ≈ 0.2929
```
34.1421 34.1421 34.1421
```

therefore,

```
x P = 0.4142 × 0 + 0.2929 × 10 + 0.2929 × 0 ≈ 2.929
y P = 0.4142 × 0 + 0.2929 × 0 + 0.2929 × 0 ≈ 2.929.

```

Therefore, the inscribed circle has a radius of 2.929 and a centre with coordinates
(2.929, 2.929).
Let’s explore another example where we determine the barycentric coordinates
of a point using virtual mass points.

<a id='p406'></a>
<!-- Página 406 -->

392 16 Barycentric Coordinates

Fig. 16.19 Triangle ΔABC C
with sides divided in the 1

## AC

ratio 1 : 2. 3


## B 2


## BC

```
3


2
```


## AC

```
3
```


## A

```
1
```


## BC

```
3




```


## A 1

```
3
```


## AB C 2


## AB B

```
3




```

Fig. 16.20 The masses
assigned to A, B and C to 1 C
determine D

```
2
```


## BC

```
3




```


## A

```
1
```


## D 3


## BC






## A 4 2 B

```
1
3
```


## AB C 2

```
3
```


## AB





Figure 16.19 shows triangle ΔABC where A , B  and C  divide BC, C A and AB
respectively, in the ratio 1 : 2. The objective is to find the barycentric coordinates of
D, E and F, and the area of triangle ΔD E F as a proportion of triangle ΔABC.
We can approach the problem using mass points. For example, if we assume D is
the centroid, all we have to do is determine the mass points that create this situation.
Then the barycentric coordinates of D are given by (16.8). We proceed as follows.
The point D is on the intersection of lines CC  and A A . Therefore, we begin by
placing a mass of 1 at C. Then, for line BC to balance at A a mass of 2 must be
placed at B. Similarly, for line AB to balance at C  a mass of 4 must be placed at A.
This configuration is shown in Fig. 16.20.
The total mass is 7 = (1 + 2 + 4), therefore,


## D = 47 A + 27 B + 17 C.


The point E is on the intersection of lines B B  and A A . Therefore, we begin by
placing a mass of 1 at A. Then, for line C A to balance at B  a mass of 2 must be
placed at C. Similarly, for line BC to balance at A a mass of 4 must be placed at B.

<a id='p407'></a>
<!-- Página 407 -->

16.8 Areas 393

Fig. 16.21 The masses
assigned to A, B and C to 1

## 2 C


## AC

determine E 3


## B 2


## BC

```
3


2
```


## AC

```
3
```


## E A

```
1
```


## BC

```
3



```


## A 1 4 B



This configuration is shown in Fig. 16.21. The total mass is still 7, therefore,


## E = 17 A + 47 B + 27 C.


From the symmetry of the triangle we can state that


## F = 27 A + 17 B + 47 C.


Thus we can locate the points and using the vector equations


## D = 47 A + 27 B + 17 C


## E = 17 A + 47 B + 27 C


## F = 27 A + 17 B + 47 C.


The important feature of these equations is that the barycentric coordinates of D, E
and F are independent of A, B and C they arise from the ratio used to divide the
triangle’s sides.
```
Although it was not the original intention, we can quickly explore what the
```

barycentric coordinates of D, E and F would be if the triangle’s sides had been
1 : 3 instead of 1 : 2. Without repeating all of the above steps, we would proceed as
follows.
```
The point D is on the intersection of lines CC  and A A . Therefore, we begin by
```

placing a mass of 1 at C. Then, for line BC to balance at A a mass of 3 must be
placed at B. Similarly, for line AB to balance at C  a mass of 9 must be placed at
A. This configuration is shown in Fig. 16.22. The total mass is 13 = (1 + 3 + 9),
therefore,


## D = 13

```
9
```


## A + 13

```
3
```


## B + 13

```
1
```


## C


## E = 13

```
1
```


## A + 13

```
9
```


## B + 13

```
3
```


## C


## F = 13

```
3
```


## A + 13

```
1
```


## B + 13

```
9
```


## C.


<a id='p408'></a>
<!-- Página 408 -->

394 16 Barycentric Coordinates

Fig. 16.22 The masses
assigned to A, B and C to 1 C
determine D

```
3
```


## BC

```
4




```


## A

```
1
```


## D 4


## BC






## A 9 3 B

```
1
4
```


## AB C 3

```
4
```


## AB





We could even develop the general equations for a ratio 1 : n. It is left to the reader
to show that

```
n2 n 1
```


## D= A+ 2 B+ 2 C

```
n +n+1
2 n +n+1 n +n+1
1 n2 n
```


## E= 2 A+ 2 B+ 2 C

```
n +n+1 n +n+1 n +n+1
n 1 n2
```


## F= 2 A+ 2 B+ 2 C.

```
n +n+1 n +n+1 n +n+1

```

As a quick test for the above equations, let n = 1, which make D, E and F
concurrent at the triangle’s centroid:


## D = 13 A + 13 B + 13 C


## E = 13 A + 13 B + 13 C


## F = 13 A + 13 B + 13 C


which is rather reassuring!
Now let’s return to the final part of the problem and determine the area of triangle
ΔD E F in terms of ΔABC. The strategy is to split triangle ΔABC into four triangles:
ΔBC F, ΔC AD, ΔAB E and ΔD E F as shown in Fig. 16.23.
Therefore,

area(ΔABC) = area(ΔBC F) + area(ΔC AD) + area(ΔAB E) + area(ΔD E F)

and
```
area(ΔBC F) area(ΔC AD) area(ΔAB E) area(ΔD E F)
```

1= + + + (16.13)
```
area(ΔABC) area(ΔABC) area(ΔABC) area(ΔABC)
```


<a id='p409'></a>
<!-- Página 409 -->

16.8 Areas 395

Fig. 16.23 Triangle ΔABC C
divides into four triangles 1

## ΔAB E, ΔBC F, ΔC AD 3


## AC


and ΔD E F

## B 2


## BC

```
3
```


## F

```
2
```


## AC

```
3
```


## E A

```
1
```


## BC

```
3
```


## D


## A B

```
1
3
```


## AB C 2

```
3
```


## AB





But we have just discovered that the barycentric coordinates are intimately connected with the ratios of triangles. For example, if F has barycentric coordinates
(r F , s F , t F ) relative to the points A, B and C respectively, then

```
area(ΔBC F)
rF = .
area(ΔABC)

```

And if D has barycentric coordinates (r D , s D , t D ) relative to the points A, B and C
respectively, then
```
area(ΔC AD)
sD = .
area(ΔABC)

```

Similarly, if E has barycentric coordinates (r E , s E , t E ) relative to the points A, B
and C respectively, then
```
area(ΔAB E)
tE = .
area(ΔABC)

```

Substituting r F , s E and t D in (16.13) we obtain

```
area(ΔD E F)
1 = r F + sD + tE + .
area(ΔABC)
```

From (16.12) we see that

```
r F = 27 , s D = 27 , t E = 27

```

therefore,
```
area(ΔD E F)
1 = 67 +
area(ΔABC)
```

and

<a id='p410'></a>
<!-- Página 410 -->

396 16 Barycentric Coordinates

```
area(ΔD E F) = 17 area(ΔABC)

```

which is rather neat!
Before we leave this example, let’s state a general expression for the area(ΔD E F)
for a triangle whose sides are divided in the ratio 1 : n. Once again, I’ll leave it to
the reader to prove that

```
n 2 − 2n + 1
area(ΔD E F) = × area(ΔABC).
n2 + n + 1

```

Note that when n = 1, area(ΔD E F) = 0, which is correct.
[Hint: The corresponding values of r F , s D and t E are n/(n 2 + n + 1).]



16.9 Volumes

We have now seen that barycentric coordinates can be used to locate a scalar within
a 1D domain, a point within a 2D area, so it seems logical that the description should
extend to 3D volumes, which is the case.
To demonstrate this, consider the tetrahedron shown in Fig. 16.24. The volume
of a tetrahedron is give by  
```
 x1 y1 z 1 
 
V = 16  x2 y2 z 2 
 x3 y3 z 3 

```

where [x1 y1 z 1 ]T , [x2 y2 z 2 ]T and [x3 y3 z 3 ]T are the three vectors extending
```
from the fourth vertex to the other three vertices. However, if we locate the fourth ver-
```

tex at the origin, (x1 , y1 , z 1 ), (x2 , y2 , z 2 ) and (x3 , y3 , z 3 ) become the coordinates
of the three vertices.


Fig. 16.24 A tetrahedron

## Y


## P3




```
v3
```


## P

```
p v2
v1
```


## P1 P2



## Z X


<a id='p411'></a>
<!-- Página 411 -->

16.9 Volumes 397

Let’s locate a point P(x P , y P , z P ) inside the tetrahedron with the following
barycentric definition
```
P = r P1 + sP2 + tP3 + uP0 (16.14)

```

where P, P1 , P2 , P3 and P0 are the position vectors for P, P1 , P2 , P3 and P0
respectively. The fourth barycentric term uP0 can be omitted as P0 has coordinates
(0, 0, 0).
Therefore, we can state that the volume of the tetrahedron formed by the three
vectors P, P2 and P3 is given by
```
 
 x P yP z P 
 
V = 16  x2 y2 z 2  . (16.15)
 x3 y3 z 3 

```

Substituting (16.14) in (16.15) we obtain
```
 
 r x1 + sx2 + t x3 r y1 + sy2 + t y3 r z 1 + sz 2 + t z 3 
 
V = 16  x2 y2 z2 
 (16.16)
 x3 y3 z3 

```

which expands to

```
y2 z 3 (r x1 + sx2 + t x3 ) + x2 y3 (r z 1 + sz 2 + t z 3 ) + x3 z 2 (r y1 + sy2 + t y3 )
```


## V = 16

```
−y3 z 2 (r x1 + sx2 + t x3 ) − x3 y2 (r z 1 + sz 2 + t z 3 ) − x2 z 3 (r y1 + sy2 + t y3 )
⎡ ⎤
r (x1 y2 z 3 + x2 y3 z 1 + x3 y1 z 2 − x1 y3 z 2 − x3 y2 z 1 − x2 y1 z 3 )
= 6 ⎣ +s(x2 y2 z 3 + x2 y3 z 2 + x3 y1 z 2 − x2 y3 z 2 − x3 y1 z 2 − x2 y2 z 3 ) ⎦
1
+t (x3 y2 z 3 + x2 y3 z 3 + x3 y3 z 2 − x3 y3 z 2 − x3 y2 z 3 − x2 y3 z 3 )


```

and simplifies to  
```
 x1 y1 z 1 
 
V = 16 r  x2 y2 z 2  .
 x3 y3 z 3 

```

This states that the volume of the smaller tetrahedron is r times the volume of the
larger tetrahedron VT , where r is the barycentric coordinate modifying the vertex not
included in the volume. By a similar process we can develop volumes for the other
tetrahedra:

```
V (P, P2 , P4 , P3 ) = r VT
V (P, P1 , P3 , P4 ) = sVT
V (P, P1 , P2 , P4 ) = t VT
V (P, P1 , P2 , P3 ) = uVT
```


<a id='p412'></a>
<!-- Página 412 -->

398 16 Barycentric Coordinates

where r + s + t + u = 1. Similarly, the barycentric coordinates of a point inside the
volume sum to unity.
Let’s test the above  with an example. Given P1 (0, 0, 1), P2 (1, 0, 0),
```
 statements
```

P3 (0, 1, 0) and P 13 , 13 , 13 which is located inside the tetrahedron, the volume of
the tetrahedron VT is  
```
0 0 1
 
```


## VT = 16  1 0 0  = 16

```
0 1 0


 2 1 1
 
```


## V (P, P2 , P4 , P3 )  3 −3 −3 

```
r= = 66  − 13 − 13 − 13  = 13
```


## VT −1 2 −1 

```
 13 13 23 
− − 
```


## V (P, P1 , P3 , P4 )  3 3 3

```
s= = 66  − 13 23 − 13  = 13
```


## VT −1 −1 −1 

```
 31 31 23 
− − 
```


## V (P, P1 , P2 , P4 )  3 31 31  1

```
t= = 6  3 − 3 − 3  = 3
6  2
```


## VT −1 −1 −1 

```
 13 13 23 
− − 
```


## V (P, P1 , P2 , P3 )  3 31 31 

```
u= = 6  3 − 3 − 3  = 0.
6  2
```


## VT −1 2 −1 

```
3 3 3

```

The barycentric coordinates (r, s, t, u) confirm that the point is located at the centre
of triangle ΔP1 P2 P3 . Note that the above determinants will create a negative volume
if the vector sequences are reversed.



16.10 Bézier Curves and Patches

In Chap. 14 we examined Bézier curves and surface patches which are based on
Bernstein polynomials:
```
n i
Bin (t) = t (1 − t)n−i .
i

```

We discovered that these polynomials create the quadratic terms

```
(1 − t)2 , 2t (1 − t), t 2

```

and the cubic terms

```
(1 − t)3 , 3t (1 − t)2 , 3t 2 (1 − t), t 3
```


<a id='p413'></a>
<!-- Página 413 -->

16.10 Bézier Curves and Patches 399

which are used as scalars to multiply sequences of control points to create a parametric curve. Furthermore, these terms sum to unity, therefore they are also another
form of barycentric coordinates. The only difference between these terms and the
others described above is that they are controlled by a common parameter t. Another
property of Bézier curves and patches is that they are constrained within the convex
hull formed by the control points, which is also a property of barycentric coordinates.



16.11 Summary

Barycentric coordinates provide another way to locate points in space, which permit
them to be used for ratios and proportion, areas, volumes, and centres of gravity.



Reference

1. Posamentier A (2008) Advanced euclidean geometry. Blackwell

<a id='p414'></a>
<!-- Página 414 -->


## Chapter 17

Geometric Algebra




17.1 Introduction

This can only be a brief introduction to geometric algebra as the subject really
demands an entire book. Those readers who wish to pursue the subject further should
consult the author’s books [1, 2].



17.2 Background

Although geometric algebra introduces some new ideas, the subject should not be
regarded as difficult. If you have read and understood the previous chapters, you
should be familiar with vectors, vector products, transforms, and the idea that the
product of two transforms is sensitive to the transform sequence. For example, in
general, scaling an object after it has been translated, is not the same as translating
an object after it has been scaled. Similarly, given two vectors r and s their vector
product r × s creates a third vector t, using the right-hand rule, perpendicular to the
plane containing r and s. However, just by reversing the vectors to s × r, creates a
similar vector but in the opposite direction −t.
```
We regard vectors as directed lines or oriented lines, but if they exist, why
```

shouldn’t oriented planes and oriented volumes exist? Well, the answer to this question is that they do, which is what geometric algebra is about. Unfortunately, when
vectors were invented, geometric algebra was overlooked, and it has taken a further
century for it to emerge through the work of William Kingdon Clifford and the theoretical physicist David Hestenes (1933–). So let’s continue and discover an exciting
new algebra that will, in time, be embraced by the computer graphics community.




© Springer-Verlag London Ltd., part of Springer Nature 2022 401
J. Vince, Mathematics for Computer Graphics, Undergraduate Topics
in Computer Science, https://doi.org/10.1007/978-1-4471-7520-9_17

<a id='p415'></a>
<!-- Página 415 -->

402 17 Geometric Algebra

17.3 Symmetric and Antisymmetric Functions

It is possible to classify functions into two categories: symmetric (even) and antisymmetric (odd) functions. For example, given two symmetric functions f (x) and
f (x, y):
```
f (−x) = f (x)

```

and
```
f (y, x) = f (x, y)

```

an example being cos x where cos(−x) = cos x. Figure 17.1 illustrates how the
cosine function is reflected about the origin. However, if the functions are antisymmetric:
```
f (−x) = − f (x)

```

and
```
f (y, x) = − f (x, y)

```

an example being sin x where sin(−x) = − sin x. Figure 17.2 illustrates how the sine
```
function is reflected about the origin.


```

Fig. 17.1 The graph of the cos x
symmetric cosine function 1



```
0.5



- -0.5 0 0.5 x

-0.5



-1


```

Fig. 17.2 The graph of the sin x
antisymmetric sine function 1



```
0.5



- -0.5 0 0.5 x

-0.5



-1
```


<a id='p416'></a>
<!-- Página 416 -->

17.3 Symmetric and Antisymmetric Functions 403

The reason why we have covered symmetric and antisymmetric functions is that
they play an important role in geometric algebra. Now let’s continue with this introduction and explore some important trigonometric foundations.



17.4 Trigonometric Foundations

Figure 17.3 shows two line segments a and b with coordinates (a1 , a2 ), (b1 , b2 )
respectively. The lines are separated by an angle θ , and we will compute the expressions ab cos θ and ab sin θ , as these play an important role in geometric algebra.

Using the trigonometric identities

```
sin(θ + φ) = sin θ cos φ + cos θ sin φ (17.1)
cos(θ + φ) = cos θ cos φ − sin θ sin φ (17.2)

```

and the following observations

```
a1 a2 b1 b2
cos φ = , sin φ = , cos(θ + φ) = , sin(θ + φ) =
a a b b
```

we can rewrite (17.1) and (17.2) as

```
b2 a1 a2
= sin θ + cos θ (17.3)
b a a
b1 a1 a2
= cos θ − sin θ. (17.4)
b a a
```

To isolate cos θ we multiply (17.3) by a2 and (17.4) by a1 :


Fig. 17.3 Two line segments Y
a and b separated by +θ
```
b2
a2


b a


θ
φ
b1 a1 X
```


<a id='p417'></a>
<!-- Página 417 -->

404 17 Geometric Algebra

```
a2 b2 a1 a2 a2
= sin θ + 2 cos θ (17.5)
b a a
a1 b1 a12 a1 a2
= cos θ − sin θ. (17.6)
b a a
```

Adding (17.5) and (17.6) we obtain

```
a1 b1 + a2 b2 a 2 + a22
= 1 cos θ = a cos θ
b a
```

therefore,
```
ab cos θ = a1 b1 + a2 b2 .

```

To isolate sin θ we multiply (17.3) by a1 and (17.4) by a2

```
a1 b2 a2 a1 a2
= 1 sin θ + cos θ (17.7)
b a a
a2 b1 a1 a2 a2
= cos θ − 2 sin θ (17.8)
b a a
```

Subtracting (17.8) from (17.7) we obtain

```
a1 b2 − a2 b1 a 2 + a22
= 1 sin θ = a sin θ
b a
```

therefore,
```
ab sin θ = a1 b2 − a2 b1 .

If we form the product of b’s projection on a with a, we get ab cos θ which we have
```

shown equals a1 b1 + a2 b2 . Similarly, if we form the product ab sin θ we compute the
area of the parallelogram formed by sweeping a along b, which equals a1 b2 − a2 b1 .
What is noteworthy, is that the product ab cos θ is independent of the sign of the
angle θ , whereas the product ab sin θ is sensitive to the sign of θ . Consequently, if we
construct the lines a and b such that b is rotated −θ relative to a as shown in Fig. 17.4,
ab cos θ = a1 b1 + a2 b2 , but ab sin θ = −(a1 b2 − a2 b1 ). The antisymmetric nature
of the sine function reverses the sign of the area.
```
Having shown that area is a signed quantity just by using trigonometric identities,
```

let’s explore how vector algebra responds to this idea.

<a id='p418'></a>
<!-- Página 418 -->

17.5 Vectorial Foundations 405

Fig. 17.4 Two line segments Y
a and b separated by −θ

```
a2


a


b2
−θ b
φ
b1 a1 X


```

17.5 Vectorial Foundations

When we form the algebraic product of two 2D vectors a and b:

```
a = a1 i + a2 j
b = b1 i + b2 j

```

we obtain
```
ab = a1 b1 i2 + a2 b2 j2 + a1 b2 ij + a2 b1 ji (17.9)

```

and it is clear that a1 b1 i2 + a2 b2 j2 has something to do with ab cos θ , and a1 b2 ij +
a2 b1 ji has something to do with ab sin θ . The product ab creates the terms i2 , j2 , ij
and ji, which are resolved as follows.



17.6 Inner and Outer Products

I like to believe that mathematics is a game—a game where we make the rules. Some
rules might take us nowhere; others might take us so far in a particular direction and
then restrict any further development; whilst other rules might open up a fantastic
landscape that would have remained hidden had we not stumbled upon them. There
are no ‘wrong’ or ‘right’ rules—there are just rules where some work better than
others. Fortunately, the rules behind geometric algebra have been tested for over a
hundred years, so we know they work. But these rules were not hiding somewhere
waiting to be discovered, they arose due to the collective intellectual endeavour of
many mathematicians over several decades.
```
Let’s begin with the products ij and ji in (17.9) and assume that they anticommute:
```

ji = −ij. Therefore,

```
ab = a1 b1 i2 + a2 b2 j2 + (a1 b2 − a2 b1 )ij (17.10)
```


<a id='p419'></a>
<!-- Página 419 -->

406 17 Geometric Algebra

and if we reverse the product to ba we obtain

```
ba = a1 b1 i2 + a2 b2 j2 − (a1 b2 − a2 b1 )ij. (17.11)

```

From (17.10) and (17.11) we see that the product of two vectors contains a symmetric
component
```
a1 b1 i2 + a2 b2 j2

```

and an antisymmetric component

```
(a1 b2 − a2 b1 )ij.

```

It is interesting to observe that the symmetric component has 0◦ between its vector
pairs (i2 or j2 ), whereas the antisymmetric component has 90◦ between its vector pairs
(i and j). Therefore, the sine and cosine functions play a natural role in our rules.
What we are looking for are two functions that, when given our vectors a and b, one
```
function returns the symmetric component and the other returns the antisymmetric
```

component. We call these the inner and outer functions respectively.
```
It should be clear that if the inner function includes the cosine of the angle between
```

the two vectors it will reject the antisymmetric component and return the symmetric
element. Similarly, if the outer function includes the sine of the angle between the
vectors, the symmetric component is rejected, and returns the antisymmetric element.
```
If we declare the inner function as the inner product:

a · b = ab cos θ (17.12)

```

then

```
a · b = (a1 i + a2 j) · (b1 i + b2 j)
= a1 b1 i · i + a1 b2 i · j + a2 b1 j · i + a2 b2 j · j
= a1 b1 + a2 b2

```

which is perfect!
Next, we declare the outer function as the outer product using the wedge ‘∧’
symbol; which is why it is also called the wedge product:

```
a ∧ b = ab sin θ i ∧ j. (17.13)

```

Note that product includes a strange i ∧ j term. This is included as we just can’t
ignore the ij term in the antisymmetric component:

<a id='p420'></a>
<!-- Página 420 -->

17.6 Inner and Outer Products 407

```
a ∧ b = (a1 i + a2 j) ∧ (b1 i + b2 j)
= a1 b1 i ∧ i + a1 b2 i ∧ j + a2 b1 j ∧ i + a2 b2 j ∧ j
= (a1 b2 − a2 b1 )i ∧ j

```

which enables us to write

```
ab = a · b + a ∧ b (17.14)
ab = ab cos θ + ab| sin θ i ∧ j. (17.15)



```

17.7 The Geometric Product in 2D

Clifford named the sum of the two products the geometric product, which means
that (17.14) reads: The geometric product ab is the sum of the inner product ‘a dot
b’ and the outer product ‘a wedge b’. Remember that all this assumes that ji = −ij
which seems a reasonable assumption.
Given the definition of the geometric product, let’s evaluate i2

```
ii = i · i + i ∧ i.

```

Using the definition for the inner product (17.12) we have

```
i · i = 1 × 1 × cos 0◦ = 1

```

whereas, using the definition of the outer product (17.13) we have

```
i ∧ i = 1 × 1 × sin 0◦ i ∧ i = 0.

```

Thus i2 = 1 and j2 = 1, and aa = a2 :

```
aa = a · a + a ∧ a
= aa cos 0◦ + aa sin 0◦ i ∧ j
aa = a2 .

```

Now let’s evaluate ij:
```
ij = i · j + i ∧ j.

```

Using the definition for the inner product (17.12) we have

```
i · j = 1 × 1 × cos 90◦ = 0

```

whereas using the definition of the outer product (17.13) we have

<a id='p421'></a>
<!-- Página 421 -->

408 17 Geometric Algebra

Fig. 17.5 An anticlockwise
```
j j
```

and clockwise bivector


```
i∧j j∧i



i i



i ∧ j = 1 × 1 × sin 90◦ i ∧ j = i ∧ j.

```

Thus ij = i ∧ j. But what is i ∧ j? Well, it is a new object and is called a ‘bivector’
and defines the orientation of the plane containing i and j.
As the order of the vectors is from i to j, the angle is +90◦ and sin(+90)◦ = 1.
Whereas, if the order is from j to i the angle is −90◦ and sin(−90◦ ) = −1. Consequently,

```
ji = j · i + j ∧ i
= 0 + 1 × 1 × sin(−90◦ )i ∧ j
ji = −i ∧ j.

```

Thus the bivector i ∧ j defines the orientation of a surface as anticlockwise, whilst
the bivector j ∧ i defines the orientation as clockwise. These ideas are shown in
Fig. 17.5.
So far, so good. Our rules seem to be leading somewhere. The inner product
(17.12) is our old friend the dot product, and does not need explaining. However, the
outer product (17.13) does require some further explanation.
The equation
```
ab = 9 + 12i ∧ j

```

simply means that the geometric product of two vectors a and b creates a scalar,
inner product of 9, and an outer product of 12 on the ij-plane.
For example, given

```
a = 3i
b = 3i + 4j

```

then

```
ab = 3i · (3i + 4j) + 3i ∧ (3i + 4j)
= 9 + 9i ∧ i + 12i ∧ j
ab = 9 + 12i ∧ j.
```


<a id='p422'></a>
<!-- Página 422 -->

17.7 The Geometric Product in 2D 409

The 9 represents ab cos θ , whereas the 12 represents an area ab sin θ on
the ij-plane. The angle between the two vectors θ is given by
```
3
θ = cos−1 5
.

```

However, reversing the product, we obtain

```
ba = (3i + 4j) · 3i + (3i + 4j) ∧ 3i
= 9 + 9i ∧ i + 12j ∧ i
ab = 9 − 12i ∧ j.

```

The sign of the outer (wedge) product has flipped to reflect the new orientation of
the vectors relative to the accepted orientation of the basis bivectors.
```
So the geometric product combines the scalar and wedge products into a single
```

product, where the scalar product is the symmetric component and the wedge product
is the antisymmetric component. Now let’s see how these products behave in 3D.



17.8 The Geometric Product in 3D

Before we consider the geometric product in 3D we need to introduce some new
notation, which will simplify future algebraic expressions. Rather than use i, j and k
to represent the unit basis vectors let’s employ e1 , e2 and e3 respectively. This means
that (17.15) can be written

```
ab = ab cos θ + ab sin θ e1 ∧ e2 .

```

We begin with two 3D vectors:

```
a = a1 e 1 + a2 e 2 + a3 e 3
b = b1 e1 + b2 e2 + b3 e3

```

therefore, their inner product is

```
a · b = (a1 e1 + a2 e2 + a3 e3 ) · (b1 e1 + b2 e2 + b3 e3 )
= a1 b1 + a2 b2 + a3 b3

```

and their outer product is

```
a ∧ b = (a1 e1 + a2 e2 + a3 e3 ) ∧ (b1 e1 + b2 e2 + b3 e3 )
= a1 b2 e1 ∧ e2 + a1 b3 e1 ∧ e3 + a2 b1 e2 ∧ e1 + a2 b3 e2 ∧ e3
+ a3 b1 e3 ∧ e1 + a3 b2 e3 ∧ e2
```


<a id='p423'></a>
<!-- Página 423 -->

410 17 Geometric Algebra

Fig. 17.6 The 3D bivectors e2



```
e 2 ∧ e3 e1 ∧ e 2




e 3 ∧ e1
e3 e1




```

a ∧ b = (a1 b2 − a2 b1 )e1 ∧ e2 + (a2 b3 − a3 b2 )e2 ∧ e3 + (a3 b1 − a1 b3 )e3 ∧ e1 .
```
(17.16)
```

This time we have three unit-basis bivectors: e1 ∧ e2 , e2 ∧ e3 , e3 ∧ e1 , and three associated scalar multipliers: (a1 b2 − a2 b1 ), (a2 b3 − a3 b2 ), (a3 b1 − a1 b3 ) respectively.
Continuing with the idea described in the previous section, the three bivectors
represent the three planes containing the respective vectors as shown in Fig. 17.6,
and the scalar multipliers are projections of the area of the vector parallelogram onto
the three bivectors as shown in Fig. 17.7. The orientation of the vectors a and b
determine whether the projected areas are positive or negative.
You may think that (17.16) looks familiar. In fact, it looks very similar to the cross
product a × b:

```
a × b = (a1 b2 − a2 b1 )e3 + (a2 b3 − a3 b2 )e1 + (a3 b1 − a1 b3 )e2 . (17.17)

```

This similarity is no accident. For when Hamilton invented quaternions, he did not
recognise the possibility of bivectors, and invented some rules, which eventually


Fig. 17.7 The projections e2
on the three bivectors

```
e2 ∧ e3 e1 ∧ e2




b
a


e3 e1
e3 ∧ e1
```


<a id='p424'></a>
<!-- Página 424 -->

17.8 The Geometric Product in 3D 411

became the cross product! Later in this chapter we discover that quaternions are
really bivectors in disguise.
We can see that a simple relationship exists between (17.16) and (17.17):

```
e1 ∧e2 and e3
e2 ∧e3 and e1
e3 ∧e1 and e2

```

the wedge product bivectors are perpendicular to the vector components of the cross
product. So the wedge product is just another way of representing the cross product.
However, the wedge product introduces a very important bonus: it works in space of
any dimension, whereas, the cross product is only comfortable in 3D. Not only that,
the wedge (outer product) is a product that creates volumes, hypervolumes, and can
also be applied to vectors, bivectors, trivectors, etc.



17.9 The Outer Product of Three 3D Vectors

Having seen that the outer product of two 3D vectors is represented by areal projections onto the three basis bivectors, let’s explore the outer product of three 3D
vectors.
Given

```
a = a1 e 1 + a2 e 2 + a3 e 3
b = b1 e1 + b2 e2 + b3 e3
c = c1 e1 + c2 e2 + c3 e3

```

then

a ∧ b ∧ c = (a1 e1 + a2 e2 + a3 e3 ) ∧ (b1 e1 + b2 e2 + b3 e3 ) ∧ (c1 e1 + c2 e2 + c3 e3 )
```
= [(a1 b2 − a2 b1 )e1 ∧ e2 + (a2 b3 − a3 b2 )e2 ∧ e3 + (a3 b1 − a1 b3 )e3 ∧ e1 ]
∧ (c1 e1 + c2 e2 + c3 e3 ).


```

At this stage we introduce another axiom: the outer product is associative. This means
that a ∧ (b ∧ c) = (a ∧ b) ∧ c. Therefore, knowing that a ∧ a = 0:

```
a ∧ b ∧ c = c3 (a1 b2 − a2 b1 )e1 ∧ e2 ∧ e3 + c1 (a2 b3 − a3 b2 )e2 ∧ e3 ∧ e1
+ c2 (a3 b1 − a1 b3 )e3 ∧ e1 ∧ e2 .
```


<a id='p425'></a>
<!-- Página 425 -->

412 17 Geometric Algebra

But we are left with the products e1 ∧ e2 ∧ e3 , e2 ∧ e3 ∧ e1 and e3 ∧ e1 ∧ e2 . Not to
worry, because we know that a ∧ b = −b ∧ a. Therefore,

```
e2 ∧ e3 ∧ e1 = −e2 ∧ e1 ∧ e3 = e1 ∧ e2 ∧ e3

```

and
```
e3 ∧ e1 ∧ e2 = −e1 ∧ e3 ∧ e2 = e1 ∧ e2 ∧ e3 .

```

Therefore, we can write a ∧ b ∧ c as

```
a ∧ b ∧ c = c3 (a1 b2 − a2 b1 )e1 ∧ e2 ∧ e3 + c1 (a2 b3 − a3 b2 )e1 ∧ e2 ∧ e3
+ c2 (a3 b1 − a1 b3 )e1 ∧ e2 ∧ e3

```

or

a ∧ b ∧ c = [c3 (a1 b2 − a2 b1 ) + c1 (a2 b3 − a3 b2 ) + c2 (a3 b1 − a1 b3 )] e1 ∧ e2 ∧ e3

or using a determinant:
```
 
 a1 b1 c1 
 
a ∧ b ∧ c =  a2 b2 c2  e1 ∧ e2 ∧ e3
 a3 b3 c3 

```

which is the well-known expression for the volume of a parallelpiped formed by
three vectors.
```
The term e1 ∧ e2 ∧ e3 is a trivector and reminds us that the volume is oriented.
```

If the sign of the determinant is positive, the original three vectors possess the same
orientation of the three basis vectors. If the sign of the determinant is negative, the
three vectors possess an orientation opposing that of the three basis vectors.



17.10 Axioms

One of the features of geometric algebra is that it behaves very similar to the everyday algebra of scalars:
Axiom 1: The associative rule:

```
a(bc) = (ab)c.

```

Axiom 2: The left and right distributive rules:

```
a(b + c) = ab + ac
(b + c)a = ba + ca.
```


<a id='p426'></a>
<!-- Página 426 -->

17.10 Axioms 413

The next four axioms describe how vectors interact with a scalar λ:
Axiom 3:
```
(λa)b = λ(ab) = λab.

```

Axiom 4:
```
λ(φa) = (λφ)a.

```

Axiom 5:
```
λ(a + b) = λa + λb.

```

Axiom 6:
```
(λ + φ)a = λa + φa.

```

The next axiom that is adopted is
Axiom 7:
```
a2 = a2

```

which has already emerged as a consequence of the algebra. However, for nonEuclidean geometries, this can be set to a2 = −a2 , which does not concern us
here.



17.11 Notation

Having abandoned i, j, k for e1 , e2 , e3 , it is convenient to convert geometric products
e1 e2 . . . en to e12...n . For example, e1 e2 e3 ≡ e123 . Furthermore, we must get used to
the following substitutions:

```
ei ei e j = e j
e21 = −e12
e312 = e123
e112 = e2
e121 = −e2 .



```

17.12 Grades, Pseudoscalars and Multivectors

As geometric algebra embraces such a wide range of objects, it is convenient to grade
them as follows: scalars are grade 0, vectors are grade 1, bivectors are grade 2, and
trivectors are grade 3, and so on for higher dimensions. In such a graded algebra
it is traditional to call the highest grade element a pseudoscalar. Thus in 2D the
pseudoscalar is e12 and in 3D the pseudoscalar is e123 .

<a id='p427'></a>
<!-- Página 427 -->

414 17 Geometric Algebra

One very powerful feature of geometric algebra is the idea of a multivector, which
is a linear combination of a scalar, vector, bivector, trivector or any other higher
dimensional object. For example the following are multivectors:

```
A = 3 + (2e1 + 3e2 + 4e3 ) + (5e12 + 6e23 + 7e31 ) + 8e123
B = 2 + (2e1 + 2e2 + 3e3 ) + (4e12 + 5e23 + 6e31 ) + 7e123

```

and we can form their sum:

```
A + B = 5 + (4e1 + 5e2 + 7e3 ) + (9e12 + 11e23 + 13e31 ) + 15e123

```

or their difference:

```
A − B = 1 + (e2 + e3 ) + (e12 + e23 + e31 ) + e123 .

```

We can even form their product AB, but at the moment we have not explored the
products between all these elements.
We can isolate any grade of a multivector using the following notation:

```
multivector g

```

where g identifies a particular grade. For example, say we have the following multivector:
```
2 + 3e1 + 2e2 − 5e12 + 6e123

```

we extract the scalar term using:

```
2 + 3e1 + 2e2 − 5e12 + 6e123 0 = 2

```

the vector term using

```
2 + 3e1 + 2e2 − 5e12 + 6e123 1 = 3e1 + 2e2

```

the bivector term using:

```
2 + 3e1 + 2e2 − 5e12 + 6e123 2 = −5e12

```

and the trivector term using:

```
2 + 3e1 + 2e2 − 5e12 + 6e123 3 = 6e123 .

```

It is also worth pointing out that the inner vector product converts two grade 1
elements, i.e. vectors, into a grade 0 element, i.e. a scalar, whereas the outer vector
product converts two grade 1 elements into a grade 2 element, i.e. a bivector. Thus

<a id='p428'></a>
<!-- Página 428 -->

17.12 Grades, Pseudoscalars and Multivectors 415

the inner product is a grade lowering operation, while the outer product is a grade
raising operation. These qualities of the inner and outer products are associated with
higher grade elements in the algebra. This is why the scalar product is renamed as the
inner product, because the scalar product is synonymous with transforming vectors
into scalars. Whereas, the inner product transforms two elements of grade n into a
grade n − 1 element.



17.13 Redefining the Inner and Outer Products

As the geometric product is defined in terms of the inner and outer products, it
seems only natural to expect that similar functions exist relating the inner and outer
products in terms of the geometric product. Such functions do exist and emerge when
we combine the following two equations:

```
ab = a · b + a ∧ b (17.18)
ba = a · b − a ∧ b. (17.19)

```

Adding and subtracting (17.18) and (17.19) we have

```
a · b = 21 (ab + ba) (17.20)
a ∧ b = 21 (ab − ba). (17.21)

```

Equations (17.20) and (17.21) and used frequently to define the products between
different grade elements.



17.14 The Inverse of a Vector

In traditional vector analysis we accept that it is impossible to divide by a vector, but
that is not so in geometric algebra. In fact, we don’t actually divide a multivector by
another vector but find a way of representing the inverse of a vector. For example,
we know that a unit vector â is defined as
```
a
â =
a

```

and using the geometric product

```
a2
â2 = =1
a2
```


<a id='p429'></a>
<!-- Página 429 -->

416 17 Geometric Algebra

therefore,
```
a2 b
b=
a2

```

and exploiting the associative nature of the geometric product we have

```
a(ab)
b= . (17.22)
a2

```

Equation (17.22) is effectively stating that, given the geometric product ab we can
recover the vector b by pre-multiplying by a−1 :
```
a
.
a2

```

Similarly, we can recover the vector a by post-multiplying by b−1 :

```
(ab)b
a= .
b2

```

For example, given two vectors

```
a = e1 + 2e2
b = 3e1 + 2e2

```

their geometric product is
```
ab = 7 − 4e12 .

```

Therefore, given ab and a, we can recover b as follows:

```
e1 + 2e2
b= (7 − 4e12 )
5
= 5 (7e1 − 4e112 + 14e2 − 8e212 )
1

= 15 (7e1 − 4e2 + 14e2 + 8e1 )
b = 3e1 + 2e2 .

```

Similarly, give ab and b, a is recovered as follows:

```
3e1 + 2e2
a = (7 − 4e12 )
13
= 13
1
(21e1 + 14e2 − 12e121 − 8e122 )
= 13
1
(21e1 + 14e2 + 12e2 − 8e1 )
a = e1 + 2e2 .
```


<a id='p430'></a>
<!-- Página 430 -->

17.14 The Inverse of a Vector 417

Note that the inverse of a unit vector is the original vector:

```
â
â−1 = = â.
â2



```

17.15 The Imaginary Properties of the Outer Product

So far we know that the outer product of two vectors is represented by one or more
unit basis vectors, such as

```
a ∧ b = λ1 e12 + λ2 e23 + λ3 e31

```

where, in this case, the λi terms represent areas projected onto their respective unit
basis bivectors. But what has not emerged is that the outer product is an imaginary
quantity, which is revealed by expanding e212 :

```
e212 = e1212

```

but as
```
e21 = −e12

```

then

```
e1(21)2 = −e1(12)2
= −e21 e22
e212 = −1.

```

Consequently, the geometric product effectively creates a complex number! Thus in
a 2D scenario, given two vectors

```
a = a1 e 1 + a2 e 2
b = b1 e1 + b2 e2

```

their geometric product is

```
ab = (a1 b1 + a2 b2 ) + (a1 b2 − a2 b1 )e12

```

and knowing that e12 = i, then we can write ab as

```
ab = (a1 b1 + a2 b2 ) + (a1 b2 − a2 b1 )i. (17.23)
```


<a id='p431'></a>
<!-- Página 431 -->

418 17 Geometric Algebra

However, this notation is not generally adopted by the geometric community. The
reason being that i is normally only associated with a scalar, with which it commutes.
Whereas in 2D, e12 is associated with scalars and vectors, and although scalars present
no problem, under some conditions, it anticommutes with vectors. Consequently, an
upper-case I is used so that there is no confusion between the two elements. Thus
(17.23) is written as

```
ab = (a1 b1 + a2 b2 ) + (a1 b2 − a2 b1 )I

```

where

## I 2 = −1.


It goes without saying that the 3D unit basis bivectors are also imaginary quantities,
so is e123 .
```
Multiplying a complex number by i rotates it 90◦ on the complex plane. Therefore,
```

it should be no surprise that multiplying a 2D vector by e12 rotates it by 90◦ . However,
because vectors are sensitive to their product partners, we must remember that premultiplying a vector by e12 rotates a vector clockwise and post-multiplying rotates
a vector anticlockwise.
```
Whilst on the subject of rotations, let’s consider what happens in 3D. We begin
```

with a 3D vector
```
a = a1 e 1 + a2 e 2 + a3 e 3

```

and the unit basis bivector e12 as shown in Fig. 17.8. Next we construct their geometric
product by pre-multiplying a by e12 :

```
e12 a = a1 e12 e1 + a2 e12 e2 + a3 e12 e3



```

Fig. 17.8 The effect of e2
pre-multiplying a vector by a a2
bivector
```
e12
a


a1
a3
e3 e1
```


<a id='p432'></a>
<!-- Página 432 -->

17.15 The Imaginary Properties of the Outer Product 419

which becomes

```
e12 a = a1 e121 + a2 e122 + a3 e123
= −a1 e2 + a2 e1 + a3 e123
= a2 e1 − a1 e2 + a3 e123

```

and contains two parts: a vector (a2 e1 − a1 e2 ) and a volume a3 e123 .
Figure 17.8 shows how the projection of vector a is rotated clockwise on the
bivector e12 . A volume is also created perpendicular to the bivector. This enables us
to predict that if the vector is coplanar with the bivector, the entire vector is rotated
−90◦ and the volume component will be zero.
By post-multiplying a by e12 creates

```
ae12 = −a2 e1 + a1 e2 + a3 e123

```

which shows that while the volumetric element has remained the same, the projected
vector is rotated anticlockwise.
You may wish to show that the same happens with the other two bivectors.



17.16 Duality

The ability to exchange pairs of geometric elements such as lines and planes involves
a dual operation, which in geometric algebra is relatively easy to define. For example,
given a multivector A its dual A∗ is defined as


## A∗ = I A


where I is the local pseudoscalar. For 2D this is e12 and for 3D it is e123 . Therefore,
given a 2D vector
```
a = a1 e 1 + a2 e 2

```

its dual is

```
a∗ = e12 (a1 e1 + a2 e2 )
= a1 e121 + a2 e122
= a2 e 1 − a1 e 2

```

which is another vector rotated 90◦ clockwise.
It is easy to show that (a∗ )∗ = −a, and two further dual operations return the
vector back to a.

<a id='p433'></a>
<!-- Página 433 -->

420 17 Geometric Algebra

```
In 3D the dual of a vector e1 is

e123 e1 = e1231 = e23

```

which is the perpendicular bivector. Similarly, the dual of e2 is e31 and the dual of e3
is e12 .
```
For a general vector a1 e1 + a2 e2 + a3 e3 its dual is

e123 (a1 e1 + a2 e2 + a3 e3 ) = a1 e1231 + a2 e1232 + a3 e1233
= a3 e12 + a1 e23 + a2 e31 .

The duals of the 3D basis bivectors are:

e123 e12 = e12312 = −e3
e123 e23 = e12323 = −e1
e123 e31 = e12331 = −e2 .



```

17.17 The Relationship Between the Vector Product
```
and the Outer Product

```

We have already discovered that there is a very close relationship between the vector
product and the outer product, and just to recap: Given two vectors

```
a = a1 e 1 + a2 e 2 + a3 e 3
b = b1 e1 + b2 e2 + b3 e3

```

then

```
a × b = (a2 b3 − a3 b2 )e1 + (a3 b1 − a1 b3 )e2 + (a1 b2 − a2 b1 )e3 (17.24)

```

and

```
a ∧ b = (a2 b3 − a3 b2 )e2 ∧ e3 + (a3 b1 − a1 b3 )e3 ∧ e1 + (a1 b2 − a2 b1 )e1 ∧ e2

```

or

```
a ∧ b = (a2 b3 − a3 b2 )e23 + (a3 b1 − a1 b3 )e31 + (a1 b2 − a2 b1 )e12 . (17.25)

```

If we multiply (17.25) by I123 we obtain

<a id='p434'></a>
<!-- Página 434 -->

17.17 The Relationship Between the Vector Product and the Outer Product 421

I123 (a ∧ b) = (a2 b3 − a3 b2 )e123 e23 + (a3 b1 − a1 b3 )e123 e31 + (a1 b2 − a2 b1 )e123 e12
```
= −(a2 b3 − a3 b2 )e1 − (a3 b1 − a1 b3 )e2 − (a1 b2 − a2 b1 )e3

```

which is identical to the cross product (17.24) apart from its sign. Therefore, we can
state:
```
a × b = −I123 (a ∧ b).



```

17.18 The Relationship Between Quaternions and Bivectors

Hamilton’s rules for the imaginaries i, j and k are shown in Table 17.1, whilst
Table 17.2 shows the rules for 3D bivector products.
Although there is some agreement between the table entries, there is a sign reversal
in some of them. However, if we switch to a left-handed axial system the bivectors
become e32 , e13 , e21 and their products are as shown in Table 17.3.
If we now create a one-to-one correspondence (isomorphism) between the two
systems:
```
i ↔ e32 j ↔ e13 k ↔ e21

```

there is a true correspondence between quaternions and a left-handed set of bivectors.


Table 17.1 Hamilton’s quaternion product rules
```
i j k
```

i −1 k −j
j −k −1 i
k j −i −1



Table 17.2 3D bivector product rules
```
e23 e31 e12
```

e23 −1 −e12 e31
e31 e12 −1 −e23
e12 −e31 e23 −1



Table 17.3 Left-handed 3D bivector product rules
```
e32 e13 e21
```

e32 −1 e21 −e13
e13 −e21 −1 e32
e21 e13 −e32 −1

<a id='p435'></a>
<!-- Página 435 -->

422 17 Geometric Algebra

17.19 Reflections and Rotations

One of geometric algebra’s strengths is the elegance it brings to calculating reflections
and rotations. Unfortunately, there is insufficient space to examine the derivations of
the formulae, but if you are interested, these can be found in the author’s books [1,
2]. Let’s start with 2D reflections.



17.19.1 2D Reflections

Given a line, whose perpendicular unit vector is m̂ and a vector a its reflection a is
given by
```
a = m̂am̂

```

which is rather elegant! For example, Fig. 17.9 shows a scenario where


```
m̂ = √12 (e1 + e2 )
a = e1

```

therefore,

```
a = √12 (e1 + e2 )(e1 ) √12 (e1 + e2 )
= 21 (1 − e12 )(e1 + e2 )
= 21 (e1 + e2 + e2 − e1 )
a = e2 .


```

Fig. 17.9 The reflection of a e2
2D vector a
```
m̂




a e1
```


<a id='p436'></a>
<!-- Página 436 -->

17.19 Reflections and Rotations 423

Note that in this scenario a reflection means a mirror image about the perpendicular
vector.



17.19.2 3D Reflections

Let’s explore the 3D scenario shown in Fig. 17.10 where

```
a = e1 + e2 − e3
m̂ = e2

```

therefore,

```
a = e2 (e1 + e2 − e3 )e2
= e212 + e222 − e232
= −e1 + e2 + e3 .

```

As one might expect, it is also possible to reflect bivectors, trivectors and higherdimensional objects, and for reasons of brevity, they are summarised as follows:

Reflecting about a line:

```
scalars: invariant
vectors: v = m̂vm̂
bivectors: B = m̂Bm̂
trivectors: T = m̂Tm̂.



```

Fig. 17.10 The reflection of e2
a 3D vector

```
a m̂ a




e3 e1
```


<a id='p437'></a>
<!-- Página 437 -->

424 17 Geometric Algebra

Reflecting about a mirror:

```
scalars: invariant
vectors: v = −m̂vm̂
bivectors: B = m̂Bm̂
trivectors: T = −m̂Tm̂.



```

17.19.3 2D Rotations

Figure 17.11 shows a plan view of two mirrors M and N separated by an angle θ .
The point P is in front of mirror M and subtends an angle α, and its reflection PR
exists in the virtual space behind M and also subtends an angle α with the mirror.
The angle between PR and N must be θ − α, and its reflection P must also lie θ − α
behind N . By inspection, the angle between P and the double reflection P is 2θ .
If we apply this double reflection transform to a collection of points, they are
effectively all rotated 2θ about the origin where the mirrors intersect. The only slight
drawback with this technique is that the angle of rotation is twice the angle between
the mirrors.
Instead of using points, let’s employ position vectors and substitute normal unit
vectors for the mirrors’ orientation. For example, Fig. 17.12 shows the same mirrors
with unit normal vectors m̂ and n̂. After two successive reflections, P becomes P ,


Fig. 17.11 Rotating a point N θ
by a double reflection

## PR



## M


```
P θ−α
θ−α α
α
```


## O P


Fig. 17.12 Rotating a point N n̂
by a double reflection

## PR



## M

```
pR
P m̂
p

p P
```


## O


<a id='p438'></a>
<!-- Página 438 -->

17.19 Reflections and Rotations 425

Fig. 17.13 Rotating a point e2
by 180◦ n̂

## P

```
p N
m̂
```


## M

```
e1
p


```


## P



and using the relationship:
```
v = −m̂vm̂

```

we compute the reflections as follows:

```
p R = −m̂pm̂
p = −n̂p R n̂
p = n̂m̂pm̂n̂

```

which is also rather elegant and compact. However, we must remember that P is
rotated twice the angle separating the mirrors, and the rotation is relative to the
origin. Let’s demonstrate this technique with an example.
Figure 17.13 shows two mirrors M and N with unit normal vectors m̂, n̂ and
position vector p:

```
m̂ = e2
n̂ = −e1
```


## P = (1, −1)

```
p = e1 − e2 .

```

As the mirrors are separated by 90◦ the point P is rotated 180◦ :

```
p = n̂m̂pm̂n̂
= −e1 e2 (e1 − e2 )e2 (−e1 )
= e12121 − e12221
= −e1 + e2
```


## P = (−1, 1).


<a id='p439'></a>
<!-- Página 439 -->

426 17 Geometric Algebra

17.20 Rotors

Quaternions are the natural choice for rotating vectors about an arbitrary axis, and
although it may not be immediately obvious, we have already started to discover
geometric algebra’s equivalent.
We begin with
```
p = n̂m̂pm̂n̂

```

and substitute R for n̂m̂ and R̃ for m̂n̂, therefore,

```
p = RpR̃

```

where R and R̃ are called rotors which perform the same function as a quaternion.
```
Because geometric algebra is non-commutative, the sequence of elements, be they
```

vectors, bivectors, trivectors, etc., is very important. Consequently, it is very useful
to include a command that reverses a sequence of elements. The notation generally
employed is the tilde (˜) symbol:

```
R = n̂m̂
R̃ = m̂n̂.

```

Let’s unpack a rotor in terms of its angle and bivector as follows:
The bivector defining the plane is m̂ ∧ n̂ and θ is the angle between the vectors.
Let

```
R = n̂m̂
R̃ = m̂n̂

```

where

```
n̂m̂ = n̂ · m̂ − m̂ ∧ n̂
m̂n̂ = n̂ · m̂ + m̂ ∧ n̂
n̂ · m̂ = cos θ
m̂ ∧ n̂ = B̂ sin θ.

```

Therefore,

```
R = cos θ − B̂ sin θ
R̃ = cos θ + B̂ sin θ.

```

We now have an equation that rotates a vector p through an angle 2θ about an axis
defined by B̂:

<a id='p440'></a>
<!-- Página 440 -->

17.20 Rotors 427

Fig. 17.14 Rotating a vector e2
by 90◦
```
90◦
p
a
p




```


## B̂

```
e3 e1


p = RpR̂

```

or
```
p = (cos θ − B̂ sin θ )p(cos θ + B̂ sin θ )

```

We can also express this such that it identifies the real angle of rotation α:
```
 
p = (cos(α/2) − B̂ sin(α/2))p cos(α/2) + B̂ sin(α/2) . (17.26)

```

Equation (17.26) references a bivector, which may make you feel uncomfortable! But
remember, it simply identifies the axis perpendicular to its plane. Let’s demonstrate
how (17.26) works with two examples.
Figure 17.14 shows a scenario where vector p is rotated 90◦ about e2 which is
perpendicular to B̂, where

```
α = 90◦
a = e2
p = e1 + e2
B̂ = e31 .

```

Therefore,

```
p = (cos 45◦ − e31 sin 45◦ )(e1 + e2 )(cos 45◦ + e31 sin 45◦ )
√ √  √ √ 
= 22 − 22 e31 (e1 + e2 ) 22 + 22 e31
√ √ √ √  √ √ 
= 22 e1 + 22 e2 − 22 e3 − 22 e312 2
2
+ 2
2
e 31

= 21 (e1 − e3 + e2 + e231 − e3 − e1 − e312 − e31231 )
p = e2 − e3 .
```


<a id='p441'></a>
<!-- Página 441 -->

428 17 Geometric Algebra

Fig. 17.15 Rotating a vector e2
by 120◦ 1
```
p n



m∧n
120◦
1 1
m
e3 e1
p


```

Observe what happens when the bivector’s sign is reversed to −e31 :

```
p = (cos 45◦ + e31 sin 45◦ )(e1 + e2 )(cos 45◦ − e31 sin 45◦ )
√ √  √ √ 
= 22 + 22 e31 (e1 + e2 ) 22 − 22 e31
√ √ √ √  √ √ 
= 22 e1 + 22 e2 + 22 e3 + 22 e312 2
2
− 2
2
e 31

= 21 (e1 + e3 + e2 + e231 + e3 − e1 + e312 − e31231 )
p = e2 + e3 .

```

the rotation is clockwise about e2 .
Figure 17.15 shows another scenario where vector p is rotated 120◦ about the
bivector B, where

```
m = e1 − e3
n = e2 − e3
α = 120◦
p = e2 + e3
B=m∧n
= (e1 − e3 ) ∧ (e2 − e3 )
B = e12 + e31 + e23 .

```

Next, we normalise B to B̂:

```
1
B̂ = √ (e12 + e23 + e31 )
3
```


<a id='p442'></a>
<!-- Página 442 -->

17.20 Rotors 429

therefore,

p = (cos 60◦ − B̂ sin 60◦ )p(cos 60◦ + B̂ sin 60◦ )
```
 √   √ 
= 21 − √13 (e12 + e23 + e31 ) 23 (e2 + e3 ) 21 + √13 (e12 + e23 + e31 ) 23
 e12 e23 e31   e12 e23 e31 
= 21 − − − (e2 + e3 ) 21 + + +
2 2 2 2 2 2
= 41 (e2 + e3 − e1 − e123 + e3 − e2 − e312 + e1 ) (1 + e12 + e23 + e31 )
= 21 (e3 − e123 )(1 + e12 + e23 + e31 )
= 21 (e3 + e312 − e2 + e1 − e123 − e12312 − e12323 − e12331 )
= 21 (e3 − e2 + e1 + e3 + e1 + e2 )
```

p = e1 + e3 .

These examples show that rotors behave just like quaternions. Rotors not only rotate
vectors, but they can be used to rotate bivectors, and even trivectors, although, as one
might expect, a rotated trivector remains unaltered in 3D.



17.21 Applied Geometric Algebra

This has been a very brief introduction to geometric algebra, and it has been impossible to cover all the algebra’s features. However, if you have understood the above
topics, you will have understood some of the fundamental ideas behind the algebra.
Let’s now consider some practical applications for geometric algebra.
The sine rule states that for any triangle ABC with angles α, β and θ , and
respective opposite sides a, b and c, then

```
a b c
= = .
sin α sin β sin θ

```

This rule can be proved using the outer product of two vectors, which we know
incorporates the sine of the angle between two vectors:

```
a ∧ b = ab sin α.

```

With reference to Fig. 17.16, we can state the triangle’s area as

```
area of ABC = 21  − c ∧ a = 21 ca sin β
area of BCA = 21  − a ∧ b = 21 ab sin θ
area of CAB = 21  − b ∧ c = 21 bc sin α
```


<a id='p443'></a>
<!-- Página 443 -->

430 17 Geometric Algebra

Fig. 17.16 The sine rule C

```
θ

b a



α β
A c B

```

Fig. 17.17 The cosine rule C




```
b a



α
A c B


```

which means that

```
ca sin β = ab sin θ = bc sin α

a b c
= = .
sin α sin β sin θ

```

The cosine rule states that for any triangle ABC with sides a, b and c, then

```
a 2 = b2 + c2 − 2bc cos α

```

where α is the angle between b and c.
Although this is an easy rule to prove using simple trigonometry, the geometric
algebra solution is even easier.
Figure 17.17 shows a triangle ABC constructed from vectors a, b and c. From
Fig. 17.17
```
a = b − c. (17.27)

```

Squaring (17.27) we obtain

```
a2 = b2 + c2 − (bc + cb).
```


<a id='p444'></a>
<!-- Página 444 -->

17.21 Applied Geometric Algebra 431

Fig. 17.18 A point P e2 P
perpendicular to a point T on
a line
```
δ
v̂
p
```


## T


```
t


e1


```

But
```
bc + cb = 2b · c = 2bc cos α

```

therefore,
```
a2 = b2 + c2 − 2bc cos α.

```

Figure 17.18 shows a scenario where a line with direction vector v̂ passes through a
point T . The objective is to locate another point P perpendicular to v̂ and a distance
δ from T . The solution is found by post-multiplying v̂ by the psuedoscalar e12 , which
rotates v̂ through an angle of 90◦ .
```
As v̂ is a unit vector
−→
T P = δ v̂e12

```

therefore,
```
−→
p=t+TP

```

and

```
p = t + δ v̂e12 . (17.28)

```

For example, Fig. 17.19 shows a 2D scenario where

```
v̂ = √12 (e1 + e2 )
```


## T = (4, 1)

```
t = 4e1 + e2
√
δ = 32.

```

Using (17.28)

<a id='p445'></a>
<!-- Página 445 -->

432 17 Geometric Algebra

Fig. 17.19 A point P e2
perpendicular to a point T on
a line P


```
p
δ

```


## T

```
t
v̂
e1

```

Fig. 17.20 Reflecting a e2
vector about a vector

```
m̂ a
v̂

a




e1


p = t + δ v̂e12
√
= 4e1 + e2 + 32 √12 (e1 + e2 )e12
= 4e1 + e2 + 4e2 − 4e1
p = 5e2

```

and

## P = (0, 5).


If p is required on the other side of the line, we pre-multiply v̂ by e12 :

```
p = t + δe12 v̂

```

which is the same as reversing the sign of δ.
Reflecting a vector about another vector happens to be a rather easy problem for
geometric algebra. Figure 17.20 shows the scenario where we see a vector a reflected
about the normal to a line with direction vector v̂.
We begin by calculating m̂:
```
m̂ = v̂e12 (17.29)
```


<a id='p446'></a>
<!-- Página 446 -->

17.21 Applied Geometric Algebra 433

Fig. 17.21 Reflecting a e2
vector about a vector


```
m̂
a
v̂

a




e1


```

then reflecting a about m̂:
```
a = m̂am̂

```

substituting m̂ we have
```
a = v̂e12 av̂e12 . (17.30)


```

As an illustration, consider the scenario shown in Fig. 17.21 where

```
v̂ = √12 (e1 + e2 )
a = −e1 .

```

Therefore, using (17.29)

```
m̂ = √12 (e1 + e2 )e12
m̂ = √12 (e2 − e1 )

```

and using (17.30)

```
a = √12 (e2 − e1 )(−e1 ) √12 (e2 − e1 )
= 21 (e12 + 1)(e2 − e1 )
= 21 (e1 + e2 + e2 − e1 )
a = e2 .

```

In computer graphics we often need to test whether a point is above, below or
on a planar surface. If we already have the plane equation for the surface it is just
a question of substituting the test point in the equation and investigating its signed
value. But here is another way using geometric algebra. For example, if a bivector
is used to represent the orientation of a plane, the outer product of the test point’s

<a id='p447'></a>
<!-- Página 447 -->

434 17 Geometric Algebra

Fig. 17.22 Point relative to P
a bivector
```
p
b
a∧b



a

```

Fig. 17.23 Three points e2
relative to a bivector P
```
p




b
r R
a a∧b
e3 e1
q
```


## Q




position vector with the bivector computes an oriented volume. Figure 17.22 shows
a bivector a ∧ b and a test point P with position vector p relative to the bivector.
Let
```
a ∧ b ∧ p is +ve, then P is ‘above’ the bivector
a ∧ b ∧ p is -ve, then P is ‘below’ the bivector
a ∧ b ∧ p is zero, then P is coplanar with the bivector.
```

The terms ‘above’ and ‘below’ mean in the bivector’s positive and negative halfspace respectively.
As an example, consider the scenario shown in Fig. 17.23 where the plane’s orientation is represented by the bivector a ∧ b, and three test points P, Q and R.
If P = (0, 1, 0), Q = (0, −1, 0), R = (1, 0, 0)

```
a = e1 + e3
b = e1

```

then

```
p = e2
q = −e2
r = e1
```


<a id='p448'></a>
<!-- Página 448 -->

17.21 Applied Geometric Algebra 435

and

```
a ∧ b ∧ p = (e1 + e3 ) ∧ e1 ∧ e2
= e123
a ∧ b ∧ q = (e1 + e3 ) ∧ e1 ∧ (−e2 )
= −e123
a ∧ b ∧ r = (e1 + e3 ) ∧ e1 ∧ e1
= 0.

```

We can see that the signs of the first two volumes show that P is in the positive
half-space, Q is in the negative half-space, and R is on the plane.



17.22 Summary

Geometric algebra is a new and exciting subject and is destined to impact upon the
way we solve problems in computer games and animation. Hopefully, you have found
this chapter interesting, and if you are tempted to take the subject further, then look
at the author’s books.



References

1. Vince JA (2008) Geometric algebra for computer graphics. Springer
2. Vince JA (2009) Geometric algebra: an algebraic system for computer games and animation.
Springer

<a id='p449'></a>
<!-- Página 449 -->


## Chapter 18

Calculus: Derivatives




18.1 Introduction

Calculus is a very large subject, and calculus books have a reputation for being heavy.
Therefore, to minimise this book’s weight, and provide a gentle introduction to the
subject, I have selected specific topics from my book [1], and condensed them into
two chapters.
One branch of calculus is concerned with a function’s derivative, which describes
how fast a function changes relative to its independent variable. In this chapter, I
show how limits are used in this process. We begin with some historical background,
and then look at small numerical quantities, and how they can be ignored if they
occur in certain products, but remain important in quotients.



18.2 Background

Over a period of 350 years or more, calculus has evolved conceptually and in notation.
Up until recently, calculus was described using infinitesimals, which are numbers so
small, they can be ignored in certain products. However, it was Cauchy and the
German mathematician Karl Weierstrass (1815–1897), who showed how limits can
replace infinitesimals.



18.3 Small Numerical Quantities

The adjective small is a relative term, and requires clarification in the context of
numbers. For example, if numbers are in the hundreds, and also contain some decimal
component, then it seems reasonable to ignore digits after the 3rd decimal place for
any quick calculation. For instance,

© Springer-Verlag London Ltd., part of Springer Nature 2022 437
J. Vince, Mathematics for Computer Graphics, Undergraduate Topics
in Computer Science, https://doi.org/10.1007/978-1-4471-7520-9_18

<a id='p450'></a>
<!-- Página 450 -->

438 18 Calculus: Derivatives

```
100.000003 × 200.000006 ≈ 20, 000

```

and ignoring the decimal part has no significant impact on the general accuracy of
the answer, which is measured in tens of thousands.
To develop an algebraic basis for this argument let’s divide a number into two
parts: a primary part x, and some very small secondary part δx (pronounced delta x).
In one of the above numbers, x = 100 and δx = 0.000003. Given two such numbers,
x1 and y1 , their product is given by

```
x1 = x + δx
y1 = y + δy
x1 y1 = (x + δx)(y + δy)
= x y + x · δy + y · δx + δx · δy.

```

Using x1 = 100.000003 and y1 = 200.000006 we have

x1 y1 = 100 × 200 + 100 × 0.000006 + 200 × 0.000003 + 0.000003 × 0.000006
```
= 20, 000 + 0.0006 + 0.0006 + 0.00000000018
= 20, 000 + 0.0012 + 0.00000000018
= 20, 000.00120000018

```

where it is clear that the products x · δy, y · δx and δx · δy contribute very little to
the result. Furthermore, the smaller we make δx and δy, their contribution becomes
even more insignificant. Just imagine if we reduce δx and δy to the level of quantum
phenomenon, e.g. 10−34 , then their products play no part in every-day numbers. But
there is no need to stop there, we can make δx and δy as small as we like, e.g.
10−100,000,000,000 . Later on we employ the device of reducing a number towards zero,
such that any products involving them can be dropped from any calculation.
Even though the product of two numbers less than one is an even smaller number,
care must be taken with their quotients. For example, in the above scenario, where
δy = 0.000006 and δx = 0.000003,

```
δy 0.000006
= =2
δx 0.000003
```

so we must watch out for such quotients.
From now on I will employ the term derivative to describe a function’s rate of
change relative to its independent variable. I will now describe two ways of computing
a derivative, and provide a graphical interpretation of the process. The first way uses
simple algebraic equations, and the second way uses a functional representation.
Needless to say, they both give the same result.

<a id='p451'></a>
<!-- Página 451 -->

18.4 Equations and Limits 439

18.4 Equations and Limits

18.4.1 Quadratic Function

Here is a simple algebraic approach using limits to compute the derivative of a
quadratic function. Starting with the function y = x 2 , let x change by δx, and let δy
be the corresponding change in y. We then have

```
y = x2
y + δy = (x + δx)2
= x 2 + 2x · δx + (δx)2
δy = 2x · δx + (δx)2 .

```

Dividing throughout by δx we have

```
δy
= 2x + δx.
δx
```

The ratio δy/δx provides a measure of how fast y changes relative to x, in increments
of δx. For example, when x = 10

```
δy
= 20 + δx,
δx
```

and if δx = 1, then δy/δx = 21. Equally, if δx = 0.001, then δy/δx = 20.001. By
making δx smaller and smaller, δy becomes equally smaller, and their ratio converges
towards a limiting value of 20.
In this case, as δx approaches zero, δy/δx approaches 2x, which is written

```
δy
lim = 2x.
δx→0 δx

```

Thus in the limit, when δx = 0, we create a condition where δy is divided by zero—
which is a meaningless operation. However, if we hold onto the idea of a limit,
as δx → 0, it is obvious that the quotient δy/δx is converging towards 2x. The
subterfuge employed to avoid dividing by zero is to substitute another quotient dy/d x
to stand for the limiting condition:

```
dy δy
= lim = 2x.
dx δx→0 δx


```

dy/d x (pronounced dee y dee x) is the derivative of y = x 2 , i.e. 2x. For instance,
when x = 0, dy/d x = 0, and when x = 3, dy/d x = 6. The derivative dy/d x, is the
instantaneous rate at which y changes relative to x.

<a id='p452'></a>
<!-- Página 452 -->

440 18 Calculus: Derivatives

If we had represented this equation as a function:

```
f (x) = x 2
f  (x) = 2x

```

where f  (x) is another way of expressing dy/d x.
Now let’s introduce two constants into the original quadratic equation to see what
effect, if any, they have on the derivative. We begin with

```
y = ax 2 + b

```

and increment x and y:

```
y + δy = a(x + δx)2 + b
 
= a x 2 + 2x · δx + (δx)2 + b
 
δy = a 2x · δx + (δx)2 .

```

Dividing throughout by δx:
```
δy
= a(2x + δx)
δx
```

and the derivative is
```
dy δy
= lim = 2ax.
dx δx→0 δx

```

Thus we see the added constant b disappears (i.e. because it does not change), whilst
the multiplied constant a is transmitted through to the derivative.



18.4.2 Cubic Equation

Now let’s repeat the above analysis for y = x 3 :

```
y = x3
y + δy = (x + δx)3
= x 3 + 3x 2 · δx + 3x(δx)2 + (δx)3
δy = 3x 2 · δx + 3x(δx)2 + (δx)3 .

```

Dividing throughout by δx:

```
δy
= 3x 2 + 3x · δx + (δx)2 .
δx
```


<a id='p453'></a>
<!-- Página 453 -->

18.4 Equations and Limits 441

Employing the idea of infinitesimals, one would argue that any term involving δx
can be ignored, because its numerical value is too small to make any contribution
to the result. Similarly, using the idea of limits, one would argue that as δx is made
increasingly smaller, towards zero, any term involving δx rapidly disappears.
```
Using limits, we have
δy
lim = 3x 2
δx→0 δx

```

or
```
dy δy
= lim = 3x 2 .
dx δx→0 δx


```

We could also show that if y = ax 3 + b then

```
dy
= 3ax 2 .
dx
```

This incremental technique can be used to compute the derivative of all sorts of
functions.
If we continue computing the derivatives of higher-order polynomials, we discover
the following pattern:

```
dy
y = x 2, = 2x
dx
dy
y = x 3, = 3x 2
dx
dy
y = x 4, = 4x 3
dx
dy
y = x 5, = 5x 4 .
dx
```

Clearly, the rule is
```
dy
y = xn, = nx n−1
dx
```

but we need to prove why this is so. The solution is found in the binomial expansion
for (x + δx)n , which can be divided into three components:
1. Decreasing terms of x.
2. Increasing terms of δx.
3. The terms of Pascal’s triangle.
For example, the individual terms of (x + δx)4 are:
Decreasing terms of x: x4 x3 x2 x1 x0
Increasing terms of δx: (δx)0 (δx)1 (δx)2 (δx)3 (δx)4
The terms of Pascal’s triangle: 1 4 6 4 1
which when combined produce

<a id='p454'></a>
<!-- Página 454 -->

442 18 Calculus: Derivatives

```
x 4 + 4x 3 (δx) + 6x 2 (δx)2 + 4x(δx)3 + (δx)4 .

```

Thus when we begin an incremental analysis:

```
y = x4
y + δy = (x + δx)4
= x 4 + 4x 3 (δx) + 6x 2 (δx)2 + 4x(δx)3 + (δx)4
δy = 4x 3 (δx) + 6x 2 (δx)2 + 4x(δx)3 + (δx)4 .

```

Dividing throughout by δx:

```
δy
= 4x 3 + 6x 2 (δx)1 + 4x(δx)2 + (δx)3 .
δx
```

In the limit, as δx slides to zero, only the second term of the original binomial
expansion remains:
```
4x 3 .

```

The second term of the binomial expansion (x + δx)n is always of the form

```
nx n−1

```

which is the proof we require.



18.4.3 Functions and Limits

In order to generalise the above findings, let’s approach the above analysis using
a function of the form y = f (x). We begin by noting some arbitrary value of its
independent variable and note the function’s value. In general terms, this is x and
f (x) respectively. We then increase x by a small amount δx, to give x + δx, and
measure the function’s value again: f (x + δx). The function’s change in value is
f (x + δx) − f (x), whilst the change in the independent variable is δx. The quotient
of these two quantities approximates to the function’s rate of change at x:

```
f (x + δx) − f (x)
. (18.1)
δx
```

By making δx smaller and smaller towards zero, (18.1) converges towards a limiting
value expressed as
```
dy f (x + δx) − f (x)
= lim (18.2)
dx δx→0 δx
```


<a id='p455'></a>
<!-- Página 455 -->

18.4 Equations and Limits 443

which can be used to compute all sorts of functions. For example, to compute the
derivative of sin x we proceed as follows:

```
y = sin x
y + δy = sin(x + δx).

```

Using the identity sin(A + B) = sin A cos B + cos A sin B, we have

```
y + δy = sin x cos(δx) + cos x sin(δx)
δy = sin x cos(δx) + cos x sin(δx) − sin x
= sin x(cos(δx) − 1) + cos x sin(δx).

```

Dividing throughout by δx we have

```
δy sin x sin(δx)
= (cos(δx) − 1) + cos x.
δx δx δx

```

In the limit as δx → 0, (cos(δx) − 1) → 0 and sin(δx)/δx = 1, and

```
dy d(sin x)
= = cos x.
dx dx
```

Before moving on, let’s compute the derivative of cos x.

```
y = cos x
y + δy = cos(x + δx).

```

Using the identity cos(A + B) = cos A cos B − sin A sin B, we have

```
y + δy = cos x cos(δx) − sin x sin(δx)
δy = cos x cos(δx) − sin x sin(δx) − cos x
= cos x(cos(δx) − 1) − sin x sin(δx).

```

Dividing throughout by δx we have

```
δy cos x sin(δx)
= (cos(δx) − 1) − sin x.
δx δx δx

```

In the limit as δx → 0, (cos(δx) − 1) → 0 and sin(δx)/δx = 1 (see Appendix A)
and
```
dy d(cos x)
= − sin x.
dx dx
```

We will continue to employ this strategy to compute the derivatives of other functions
later on.

<a id='p456'></a>
<!-- Página 456 -->

444 18 Calculus: Derivatives

18.4.4 Graphical Interpretation of the Derivative

To illustrate this limiting process graphically, consider the scenario in Fig. 18.1 where
```
 point is P. In this case the function is f (x) = x and P’s coordinates are
2
```

the
 sample
x, x . We2 identify another point R, displaced δx to the right of P, with coordinates
```
2

```

x + δx, x . The point Q on the curve, vertically above R, has coordinates x +
δx, (x + δx)2 . When δx is relatively small, the slope of the line P Q approximates
to the function’s rate of change at P, which is the graph’s slope. This is given by

```
QR (x + δx)2 − x 2
slope = =
PR δx
x + 2x(δx) + (δx)2 − x 2
2
=
δx
2x(δx) + (δx)2
=
δx
= 2x + δx.

```

We can now reason that as δx is made smaller and smaller, Q approaches P, and
slope becomes the graph’s slope at P. This is the limiting condition:

```
dy
= lim (2x + δx) = 2x.
dx δx→0

 
```

Thus, for any point with coordinates x, x 2 , the slope is given by 2x. For example,
when x = 0, the slope is 0, and when x = 4, the slope is 8, etc.


Fig. 18.1 Sketch of
f (x) = x 2 4

## Q


```
3


2

```


## P R

```
1



-1 0 1 2

-1
```


<a id='p457'></a>
<!-- Página 457 -->

18.4 Equations and Limits 445

18.4.5 Derivatives and Differentials

Given a function f (x), the ratio d f /d x represents the instantaneous change of f
for some x, and is called the first derivative of f (x). For linear functions, this is
constant, for other functions, the derivative’s value changes with x and is represented
by a function.
The elements d f , dy and d x are called differentials, and historically, the derivative
used to be called the differential coefficient, but has now been dropped in favour of
derivative. One can see how the idea of a differential coefficient arose if we write,
for example:
```
dy
= 3x
dx
```

as
```
dy = 3x d x.

```

In this case, 3x acts like a coefficient of d x, nevertheless, we will use the word
derivative. It is worth noting that if y = x, then dy/d x = 1, or dy = d x. The two
differentials are individual algebraic quantities, which permits us to write statements
such as
```
dy dy
= 3x, dy = 3x d x, dx = .
dx 3x

```

Now let’s find dy/d x, for

```
y = 6x 3 − 4x 2 + 8x + 6.

Differentiating y:
dy
= 18x 2 − 8x + 8
dx
```

which is the instantaneous change of y relative to x. When x = 1, dy/d x = 18 −
8 + 8 = 18, which means that y is changing 18 times faster than x. Consequently,
d x/dy = 1/18.



18.4.6 Integration and Antiderivatives

If it is possible to differentiate a function, it seems reasonable to assume the existence of an inverse process to convert a derivative back to its associated function.
Fortunately, this is the case, but there are some limitations. This inverse process is
called integration and reveals the antiderivative of a function. Many functions can
be paired together in the form of a derivative and an antiderivative, such as 2x with
x 2 , and cos x with sin x. However, there are many functions where it is impossible

<a id='p458'></a>
<!-- Página 458 -->

446 18 Calculus: Derivatives

to derive its antiderivative in a precise form. For example, there is no simple, finite
functional antiderivative for sin x 2 or (sin x)/x. To understand integration, let’s begin
with a simple derivative.
If we are given
```
dy
= 18x 2 − 8x + 8
dx
```

it is not too difficult to reason that the original function could have been

```
y = 6x 3 − 4x 2 + 8x.

```

However, it could have also been

```
y = 6x 3 − 4x 2 + 8x + 2

```

or
```
y = 6x 3 − 4x 2 + 8x + 20

```

or with any other constant. Consequently, when integrating the original function, the
integration process has to include a constant:

```
y = 6x 3 − 4x 2 + 8x + C.

```

The value of C is not always required, but it can be determined if we are given some
extra information, such as y = 10 when x = 0, then C = 10. 
The notation for integration employs a curly ‘S’ symbol , which may seem
strange, but is short for sum and will be explained later. So, starting with

```
dy
= 18x 2 − 8x + 8
dx
```

we rewrite this as
```
dy = (18x 2 − 8x + 8)d x

```

and integrate both sides, where dy becomes y and the right-hand-side becomes
```

 
18x 2 − 8x + 8 d x

```

although brackets are not always used:
```

y= 18x 2 − 8x + 8 d x.

```

This equation reads: “y is the integral of 18x 2 − 8x + 8 dee x.” The d x reminds us
that x is the independent variable. In this case we can write the answer:

<a id='p459'></a>
<!-- Página 459 -->

18.4 Equations and Limits 447

```
dy = 18x 2 − 8x + 8 d x

y = 18x 2 − 8x + 8 d x

= 6x 3 − 4x 2 + 8x + C

```

where C is some constant.
For example, let’s find y, given

```
dy = 6x 2 + 10x d x.

```

Integrating:
```

y= 6x 2 + 10x d x

= 2x 3 + 5x 2 + C.


```

Now let’s find y, given
```
dy = d x.

```

Integrating:
```

y= 1 dx

= x + C.

```

The antiderivatives for the sine and cosine functions are written:
```

sin x d x = − cos x + C

cos x d x = sin x + C

```

which you may think obvious, as we have just computed their derivatives. However, the reason for introducing integration alongside differentiation, is to make you
familiar with the notation, and memorise the two distinct processes, as well as lay
the foundations for the next chapter.


18.5 Function Types

Mathematical functions come in all sorts of shapes and sizes. Sometimes they are
described explicitly where y equals some function of its independent variable(s),
such as

<a id='p460'></a>
<!-- Página 460 -->

448 18 Calculus: Derivatives

```
y = x sin x

```

or implicitly where y, and its independent variable(s) are part of an equation, such
as
```
x 2 + y 2 = 10.

```

A function may reference other functions, such as
```
 
y = sin cos2 x

```

or
```
y = x sin x .

```

There is no limit to the way functions can be combined, which makes it impossible
to cover every eventuality. Nevertheless, we will explore some useful combinations
that prepare us for any future surprises.
```
First, we examine how to differentiate different types of functions, that include
```

sums, products and quotients, which are employed later on to differentiate specific functions such as trigonometric, logarithmic and hyperbolic. Where relevant, I
include the appropriate antiderivative to complement its derivative.



18.6 Differentiating Groups of Functions

So far we have only considered simple individual functions, which, unfortunately, do
not represent the equations found in mathematics, science, physics or even computer
graphics. In general, the functions we have to differentiate include sums of functions,
functions of functions, function products and function quotients. Let’s explore these
four scenarios.



18.6.1 Sums of Functions

A function normally computes a numerical value from its independent variable(s),
and if it can be differentiated, its derivative generates another function with the same
independent variable. Consequently, if a function contains two functions of x, such
as u and v, where
```
y = u(x) + v(x)

```

which can be abbreviated to
```
y =u+v

```

then

<a id='p461'></a>
<!-- Página 461 -->

18.6 Differentiating Groups of Functions 449

Fig. 18.2 Graph of
y = 2x 6 + sin x + cos x and 3
its derivative,
dy 2
d x = 12x + cos x − sin x
```
5

```

(dashed) 1


```
-1 0 1

-1

-2

-3




dy du dv
= +
dx dx dx
```

where we just sum their individual derivatives.
As an example, find dy/d x, given

```
u = 2x 6
v = 3x 5
y =u+v
y = 2x 6 + 3x 5 .

```

Differentiating y:
```
dy
= 12x 5 + 15x 4 .
dx
```

Similarly, find dy/d x, given

```
u = 2x 6
v = sin x
w = cos x
y =u+v+w
y = 2x 6 + sin x + cos x.

```

Differentiating y:
```
dy
= 12x 5 + cos x − sin x.
dx

```

Figure 18.2 shows a graph of y = 2x 6 + sin x + cos x and its derivative y =
12x 5 + cos x − sin x. Differentiating such functions is relatively easy, so too, is integrating. Given

<a id='p462'></a>
<!-- Página 462 -->

450 18 Calculus: Derivatives

```
dy du dv
= +
dx dx dx
```

then
```
 
du dv
y= dx + dx
dx dx
  
du dv
= + d x.
dx dx

```

For example, let’s find y, given

```
dy
= 12x 5 + cos x − sin x.
dx
```

Integrating:
```
 
dy = 12x 5 + cos x − sin x d x
  
y = 12x d x + cos x d x − sin x d x
5


= 2x 6 + sin x + cos x + C.



```

18.6.2 Function of a Function

One of the advantages of modern mathematical notation is that it lends itself to
unlimited elaboration without introducing any new symbols. For example, the polynomial 3x 2 + 2x is easily raised to some power by adding brackets and an appropriate
```
 2
```

index: 3x 2 + 2x . Such an object is a function of a function, because the function
3x 2 + 2x is subjected to a further squaring function. The question now is: how are
such functions differentiated? Well, the answer is relatively easy, but does introduce
some new ideas.
Imagine that Heidi swims twice as fast as John, who in turn, swims three times as
fast as his dog, Monty. It should be obvious that Heidi swims six (2 × 3) times faster
than Monty. This product rule, also applies to derivatives, because if y changes twice
as fast as u, i.e. dy/du = 2, and u changes three times as fast as x, i.e. du/d x = 3,
then y changes six times as fast as x:

```
dy dy du
= · .
dx du d x
```

To differentiate  2
```
y = 3x 2 + 2x
```


<a id='p463'></a>
<!-- Página 463 -->

18.6 Differentiating Groups of Functions 451

we substitute
```
u = 3x 2 + 2x

```

then
```
y = u2

```

and
```
dy
= 2u
du  
= 2 3x 2 + 2x
= 6x 2 + 4x.

```

Next, we require du/d x:

```
u = 3x 2 + 2x
du
= 6x + 2
dx
```

therefore, we can write

```
dy dy du
= ·
dx du 2 d x 
= 6x + 4x (6x + 2)
= 36x 3 + 36x 2 + 8x.

```

This result is easily verified by expanding the original polynomial and differentiating:
```
 2
y = 3x 2 + 2x
  
= 3x 2 + 2x 3x 2 + 2x
= 9x 4 + 12x 3 + 4x 2
dy
= 36x 3 + 36x 2 + 8x.
dx
 2
```

Figure 18.3 shows a graph of y = 3x 2 + 2x and its derivative y = 36x 3 + 36x 2 +
8x.
Now let’s differentiate y = sin(ax), which is a function of a function.
Substitute u for ax:

<a id='p464'></a>
<!-- Página 464 -->

452 18 Calculus: Derivatives

Fig. 18.3 Graph of
```
 2
```

y = 3x 2 + 2x and its
derivative, 2
dy
d x = 36x + 36x + 8x
```
3 2

```

(dashed)

```
-1 0 1




-2




y = sin u
dy
= cos u
du
= cos(ax).

```

Next, we require du/d x:

```
u = ax
du
=a
dx
```

therefore, we can write

```
dy dy du
= ·
dx du d x
= cos(ax) · a
= a cos(ax).

```

Consequently, given
```
dy
= cos(ax)
dx
```

then

```
dy = cos(ax) d x

y = cos(ax) d x

= a1 sin(ax) + C.

```

Similarly, given

<a id='p465'></a>
<!-- Página 465 -->

18.6 Differentiating Groups of Functions 453

```
dy
= sin(ax)
dx
```

then

```
dy = sin(ax) d x

y = sin(ax) d x

= − a1 cos(ax) + C.


 
```

To differentiate y = sin x 2 , which is also a function of a function, we substitute
u for x 2 :

```
y = sin u
dy
= cos u
du  
= cos x 2 .

```

Next, we require du/d x:

```
u = x2
du
= 2x
dx
```

therefore, we can write

```
dy dy du
= ·
dx du  d x
= cos x 2 · 2x
 
= 2x cos x 2 .
   
```

Figure 18.4 shows a graph of y = sin x 2 and its derivative y = 2x cos x 2 . In
general, there can be any depth of functions within a function, which permits us to
write the chain rule for derivatives:
```
dy dy du dv dw
= · · · .
dx du dv dw d x
```


<a id='p466'></a>
<!-- Página 466 -->

454 18 Calculus: Derivatives

Fig. 18.4 Graph
```
 of
```

y = sin x 2 and its 8
```
 
```

derivative, ddyx = 2x cos x 2
(dashed) 4



```
-4 -3 -2 -1 0 1 2 3 4


-4



-8




```

18.6.3 Function Products

Function products occur frequently in every-day mathematics, and involve the product of two, or more functions. Here are three simple examples:
```
  
y = 3x 2 + 2x 2x 2 + 3x
y = sin x cos x
y = x 2 sin x.

```

When it comes to differentiating function products of the form

```
y = uv

```

it seems natural to assume that
```
dy du dv
= · (18.3)
dx dx dx
```

which unfortunately, is incorrect. For example, in the case of
```
  
y = 3x 2 + 2x 2x 2 + 3x

```

differentiating using the above rule (18.3) produces

```
dy
= (6x + 2)(4x + 3)
dx
= 24x 2 + 26x + 6.

```

However, if we expand the original product and then differentiate, we obtain

<a id='p467'></a>
<!-- Página 467 -->

18.6 Differentiating Groups of Functions 455
```
  
y = 3x 2 + 2x 2x 2 + 3x
= 6x 4 + 13x 3 + 6x 2
dy
= 24x 3 + 39x 2 + 12x
dx
```

which is correct, but differs from the first result. Obviously, (18.3) must be wrong.
So let’s return to first principles and discover the correct rule.
So far we have incremented the independent variable—normally x—by δx to
discover the change in y—normally δy. Next, we see how the same notation can be
used to increment functions.
Given the following functions of x, u and v, where

```
y = uv

```

if x increases by δx, then there will be corresponding changes of δu, δv and δy, in
u, v and y respectively. Therefore,

```
y + δy = (u + δu)(v + δv)
= uv + uδv + vδu + δuδv
δy = uδv + vδu + δuδv.

```

Dividing throughout by δx we have

```
δy δv δu δv
=u +v + δu .
δx δx δx δx
```

In the limiting condition:
```
     
dy δv δu δv
= lim u + lim v + lim δu .
dx δx→0 δx δx→0 δx δx→0 δx
 δv 
```

As δx → 0, then δu → 0 and δu δx → 0. Therefore,

```
dy dv du
=u +v . (18.4)
dx dx dx
```

Applying (18.4) to the original function product:

```
u = 3x 2 + 2x
v = 2x 2 + 3x
y = uv
du
= 6x + 2
dx
```


<a id='p468'></a>
<!-- Página 468 -->

456 18 Calculus: Derivatives

Fig. 18.5
```
 Graph
 of 
```

y = 3x 2 + 2x 2x 2 + 3x 3
and its derivative,
dy
d x = 24x + 39x + 12x
```
3 2
2
```

(dashed)

```
1



-2 -1 0 1


-1




dv
= 4x + 3
dx
dy dv du
=u +v
dx  dx dx  
= 3x 2 + 2x (4x + 3) + 2x 2 + 3x (6x + 2)
   
= 12x 3 + 17x 2 + 6x + 12x 3 + 22x 2 + 6x
= 24x 3 + 39x 2 + 12x

```

which agrees
```
  with our  previous prediction. Figure 18.5 shows a graph of y =
```

3x 2 + 2x 2x 2 + 3x and its derivative y = 24x 3 + 39x 2 + 12x.
```
Now let’s differentiate y = sin x cos x using (18.4).

y = sin x cos x
u = sin x
du
= cos x
dx
v = cos x
dv
= − sin x
dx
dy dv du
=u +v
dx dx dx
= sin x(− sin x) + cos x cos x
= cos2 x − sin2 x
= cos(2x).

```

Using the identity sin(2x) = 2 sin x cos x, we can rewrite the original function as

```
y = sin x cos x
= 21 sin(2x)
```


<a id='p469'></a>
<!-- Página 469 -->

18.6 Differentiating Groups of Functions 457

Fig. 18.6 Graph of
y = sin x cos x and its
derivative, ddyx = cos(2x) 1

(dashed)


```
-2 - 0 2




-1




dy
= cos(2x)
dx
```

which confirms the above derivative. Now let’s consider the antiderivative of cos 2x.
Given
```
dy
= cos(2x)
dx
```

then

```
dy = cos(2x) d x

y = cos(2x) d x

= 21 sin(2x) + C
= sin x cos x + C.

```

Figure 18.6 shows a graph of y = sin x cos and its derivative y = cos(2x).

Let’s differentiate y = x 2 sin x, using (18.4):

```
y = x 2 sin x
u = x2
du
= 2x
dx
v = sin x
dv
= cos x
dx
dy dv du
=u +v
dx dx dx
= x 2 cos x + 2x sin x.
```


<a id='p470'></a>
<!-- Página 470 -->

458 18 Calculus: Derivatives

Fig. 18.7 Graph of
y = x 2 sin x and its 4
derivative
y = x 2 cos x + 2x sin x
```
2
```

(dashed)

```
- 0



-2



-4




```

Figure 18.7 shows a graph of y = x 2 sin x and its derivative x 2 cos x + 2x sin x.



18.6.4 Function Quotients

Next, we investigate how to differentiate the quotient of two functions. We begin
with two functions of x, u and v, where
```
u
y=
v
```

which makes y also a function of x.
We now increment x by δx and measure the change in u as δu, and the change in
v as δv. Consequently, the change in y is δy:

```
u + δu
y + δy =
v + δv
u + δu u
δy = −
v + δv v
v(u + δu) − u(v + δv)
=
v(v + δv)
vδu − uδv
= .
v(v + δv)

```

Dividing throughout by δx we have

```
δu δv
δy v −u
= δx δx .
δx v(v + δv)

```

As δx → 0, δu, δv and δy also tend towards zero, and the limiting conditions are

<a id='p471'></a>
<!-- Página 471 -->

18.6 Differentiating Groups of Functions 459

```
dy δy
= lim
dx δx→0 δx
du δu
v = lim v
dx δx→0 δx
dv δv
u = lim u
dx δx→0 δx
v 2 = lim v(v + δv)
δx→0

```

therefore,
```
du dv
dy v −u
= d x d x.
dx v2

```

To illustrate this, let’s differentiate y, given

```
x 3 + 2x 2 + 3x + 6
y= .
x2 + 3

```

Substitute u = x 3 + 2x 2 + 3x + 6 and v = x 2 + 3, then

```
du
= 3x 2 + 4x + 3
dx
dv
= 2x
dx  2    
dy x + 3 3x 2 + 4x + 3 − x 3 + 2x 2 + 3x + 6 2x
=  2
dx x2 + 3
 4   
3x + 4x 3 + 3x 2 + 9x 2 + 12x + 9 − 2x 4 + 4x 3 + 6x 2 + 12x
=
x 4 + 6x 2 + 9
x + 6x + 9
4 2
= 4
x + 6x 2 + 9
=1

```

which is not a surprising result when one sees that the original function has the factors
```
 2 
x + 3 (x + 2)
y= = x +2
x2 + 3
   
```

whose derivative is 1. Figure 18.8 shows a graph of y = x 2 + 3 (x + 2)/ x 2 + 3
and its derivative y = 1.

<a id='p472'></a>
<!-- Página 472 -->

460 18 Calculus: Derivatives


 2 18.8 Graph of 2y = 
Fig.
x + 3 (x + 2)/ x + 3
```
2
```

and its derivative, ddyx = 1
(dashed)
```
1



-4 -3 -2 -1 0 1 2 3 4


-1


-2




```

18.7 Differentiating Implicit Functions

Functions conveniently fall into two types: explicit and implicit. An explicit function,
describes a function in terms of its independent variable(s), such as

```
y = a sin x + b cos x

```

where the value of y is determined by the values of a, b and x. On the other hand,
an implicit function, such as
```
x 2 + y 2 = 25

```

combines the function’s name with its definition. In this case, it is easy to untangle
the explicit form: 
```
y = 25 − x 2 .

```

So far, we have only considered differentiating explicit functions, so now let’s examine how to differentiate implicit functions. Let’s begin with a simple explicit function
and differentiate it as it is converted into its implicit form.
Let
```
y = 2x 2 + 3x + 4

```

then
```
dy
= 4x + 3.
dx
```

Now let’s start the conversion into the implicit form by bringing the constant 4 over
to the left-hand side:
```
y − 4 = 2x 2 + 3x

```

differentiating both sides:
```
dy
= 4x + 3.
dx
```


<a id='p473'></a>
<!-- Página 473 -->

18.7 Differentiating Implicit Functions 461

Bringing 4 and 3x across to the left-hand side:

```
y − 3x − 4 = 2x 2

```

differentiating both sides:

```
dy
− 3 = 4x
dx
dy
= 4x + 3.
dx
```

Finally, we have
```
y − 2x 2 − 3x − 4 = 0

```

differentiating both sides:

```
dy
− 4x − 3 = 0
dx
dy
= 4x + 3
dx
```

which seems straight forward. The reason for working through this example is to
remind us that when y is differentiated we get dy/d x.

Let’s find dy/d x, given
```
y + sin x + 4x = 0.

```

Differentiating the individual terms:

```
y + sin x + 4x = 0
dy
+ cos x + 4 = 0
dx
dy
= − cos x − 4.
dx
y + x 2 − cos x = 0
dy
+ 2x + sin x = 0
dx
dy
= −2x − sin x.
dx

```

But how do we differentiate y 2 + x 2 = r 2 ? Well, the important difference between
this implicit function and previous functions, is that it involves a function of a function. y is not only a function of x, but is squared, which means that we must employ
the chain rule described earlier:

<a id='p474'></a>
<!-- Página 474 -->

462 18 Calculus: Derivatives

```
dy dy du
= · .
dx du d x
```

Therefore, given

```
y2 + x 2 = r 2
dy
2y + 2x = 0
dx
dy −2x
=
dx 2y
−x
=√ .
r2 − x2

```

This is readily confirmed by expressing the original function in its explicit form and
differentiating:
```
 1
y = r2 − x2 2

```

which is a function of a function.
Let u = r 2 − x 2 , then
```
du
= −2x.
dx
1
```

As y = u 2 , then

```
dy
= 21 u − 2
1

du
1
= 1
2u 2
1
= √ .
2 r2 − x2

```

However,

```
dy dy du
= ·
dx du d x
−2x
= √
2 r2 − x2
−x
=√
r2 − x2

```

which agrees with the implicit differentiated form.
As another example, let’s find dy/d x, given

```
x 2 − y 2 + 4x = 6y.
```


<a id='p475'></a>
<!-- Página 475 -->

18.7 Differentiating Implicit Functions 463

Differentiating the individual terms:

```
dy dy
2x − 2y +4=6 .
dx dx
```

Rearranging the terms, we have

```
dy dy
2x + 4 = 6 + 2y
dx dx
dy
= (6 + 2y)
dx
dy 2x + 4
= .
dx 6 + 2y

```

If, for example, we have to find the slope of x 2 − y 2 + 4x = 6y at the point (4, 3),
then we simply substitute x = 4 and y = 3 in dy/d x to obtain the answer 1.
```
Finally, let’s find dy/d x, given

x n + yn = an
dy
nx n−1 + ny n−1 =0
dx
dy nx n−1
= − n−1
dx ny
dy x n−1
= − n−1 .
dx y



```

18.8 Differentiating Exponential and Logarithmic
```
Functions

```

18.8.1 Exponential Functions

Exponential functions have the form y = a x , where the independent variable is the
exponent. Such functions are used to describe various forms of growth or decay, from
the compound interest law, to the rate at which a cup of tea cools down. One special
value of a is 2.718282.., called e, where
```
 
1 n
e = lim 1+ .
n→∞ n

```

Raising e to the power x:  
```
1 nx
e x = lim 1+
n→∞ n
```


<a id='p476'></a>
<!-- Página 476 -->

464 18 Calculus: Derivatives

Fig. 18.9 Graphs of y = e x
and y = e−x
```
4


3
y = e-x y = ex
2


1

0
-4 -3 -2 -1 1 2 3 4




```

which, using the Binomial Theorem, is

```
x2 x3 x4
ex = 1 + x + + + + ··· .
2! 3! 4!
```

If we let

```
y = ex
dy x2 x3 x4
=1+x + + + + ···
dx 2! 3! 4!
= ex .

```

which is itself. Figure 18.9 shows graphs of y = e x and y = e−x .
Now let’s differentiate y = a x . We know from the rules of logarithms that

```
log x n = n log x

```

therefore, given
```
y = ax

```

then
```
ln y = ln a x = x ln a

```

therefore
```
y = e x ln a

```

which means that
```
a x = e x ln a .

```

Consequently,

<a id='p477'></a>
<!-- Página 477 -->

18.8 Differentiating Exponential and Logarithmic Functions 465

```
d x d x ln a
a = e
dx dx
= ln a e x ln a
= a x ln a.

```

Similarly, it can be shown that

```
dy
y = e−x , = −e−x
dx
dy
y = eax , = aeax
dx
dy
y = e−ax , = −ae−ax
dx
dy
y = ax , = ln a a x
dx
dy
y = a −x , = − ln a a −x .
dx
```

The exponential antiderivatives are written:
```

ex d x = ex + C

e−x d x = −e−x + C

1 ax
eax d x =e +C
a

1
e−ax d x = − e−ax + C
a

1 x
ax d x = a +C
ln a

1 −x
a −x d x = − a + C.
ln a




```

18.8.2 Logarithmic Functions

Given a function of the form
```
y = ln x

```

then
```
x = ey .
```


<a id='p478'></a>
<!-- Página 478 -->

466 18 Calculus: Derivatives

Fig. 18.10 Graph of
y = ln x and its derivative, 2
dy
d x = x (dashed)
```
1
1



-1 0 1 2 3 4 5 6


-1


-2




```

Therefore,

```
dx
= ey
dy
=x
dy 1
= .
dx x
```

Thus
```
d 1
ln x = .
dx x
```

Figure 18.10 shows the graph of y = ln x and its derivative y = 1/x. Conversely,
```

1
d x = ln |x| + C.
x

```

When differentiating logarithms to a base a, we employ the conversion formula:

```
y = loga x
= (ln x)(loga e)

```

whose derivative is
```
dy 1
= loga e.
dx x
```

When a = 10, then log10 e = 0.4343... and

```
d 0.4343
log10 x ≈
dx x
```

Figure 18.11 shows the graph of y = log10 x and its derivative y ≈ 0.4343/x.

<a id='p479'></a>
<!-- Página 479 -->

18.9 Differentiating Trigonometric Functions 467

Fig. 18.11 Graph of
```
2
```

y = log10 x and its
derivative, ddyx ≈ 0.4343
```
x 1
```

(dashed)

```
-1 0 1 2 3 4 5 6


-1


-2




```

18.9 Differentiating Trigonometric Functions

We have only differentiated two trigonometric functions: sin x and cos x, so let’s add
tan x, csc x, sec x and cot x to the list, as well as their inverse forms.



18.9.1 Differentiating tan

Rather than return to first principles and start incrementing x by δx, we can employ
the rules for differentiating different function combinations and various trigonometric
identities. In the case of tan(ax), this can be written as

```
sin(ax)
tan(ax) =
cos(ax)

```

and employ the quotient rule:

```
du dv
dy v −u
= d x d x.
dx v2

```

Therefore, let u = sin(ax) and v = cos(ax), and

```
dy a cos(ax) cos(ax) + a sin(ax) sin(ax)
=
dx cos2 (ax)
 2 
a cos (ax) + sin2 (ax)
=
cos2 (ax)
a
=
cos2 (ax)
= a sec2 (ax)
 
= a 1 + tan2 (ax) .
```


<a id='p480'></a>
<!-- Página 480 -->

468 18 Calculus: Derivatives

Fig. 18.12 Graph of
y = tan x and its derivative,
dy 4
d x = 1 + tan x (dashed)
```
2

2


-2 0 2


-2


-4




```

Figure 18.12 shows the graph of y = tan x and its derivative y = 1 + tan2 x.

It follows that 
```
1
sec2 (ax) d x = tan(ax) + C.
a




```

18.9.2 Differentiating csc

Using the quotient rule:

```
y = csc(ax)
1
=
sin(ax)
dy 0 − a cos(ax)
=
dx sin2 (ax)
−a cos(ax)
=
sin2 (ax)
a cos(ax)
=− ·
sin(ax) sin(ax)
= −a csc(ax) · cot(ax).

```

Figure 18.13 shows the graph of y = csc x and its derivative y = − csc x cot x.

It follows that 
```
1
csc(ax) · cot(ax) d x = − csc(ax) + C.
a
```


<a id='p481'></a>
<!-- Página 481 -->

18.9 Differentiating Trigonometric Functions 469

Fig. 18.13 Graph of
y = csc x and its derivative,
dy 4
d x = − csc x cot x (dashed)

```
2


-2 0 2


-2


-4


```

Fig. 18.14 Graph of
y = sec x and its derivative,
dy 4
d x = sec x tan x (dashed)

```
2


-2 0 2


-2


-4




```

18.9.3 Differentiating sec

Using the quotient rule:

```
y = sec(ax)
1
=
cos(ax)
dy −(−a sin(ax))
=
dx cos2 (ax)
a sin(ax)
=
cos2 (ax)
a sin(ax)
= ·
cos(ax) cos(ax)
= a sec(ax) · tan(ax).

```

Figure 18.14 shows the graph of y = sec x and its derivative y = sec x tan x.

It follows that 
```
1
sec(ax) · tan(ax) d x = sec(ax) + C.
a
```


<a id='p482'></a>
<!-- Página 482 -->

470 18 Calculus: Derivatives

18.9.4 Differentiating cot

Using the quotient rule:

```
y = cot(ax)
1
=
tan(ax)
dy −a sec2 (ax)
=
dx tan2 (ax)
a cos2 (ax)
=− 2 ·
cos (ax) sin2 (ax)
a
=− 2
sin (ax)
= −a csc2 (ax)
 
= −a 1 + cot 2 (ax) .

```

Figure 18.15 shows the graph of y = cot x and its derivative y = −(1 + cot 2 x).

It follows that 
```
1
csc2 (ax) d x = − cot(ax) + C.
a




```

18.9.5 Differentiating arcsin, arccos and arctan

These inverse functions are solved using a clever strategy.
Let
```
x = sin y


```

Fig. 18.15 Graph of
y = cot x and its derivative,
dy
d x = −(1 + cot x)
```
2 4

```

(dashed)
```
2




-2 - 0 2


-2




-4
```


<a id='p483'></a>
<!-- Página 483 -->

18.9 Differentiating Trigonometric Functions 471

then
```
y = arcsin x.

```

Differentiating the first expression, we have

```
dx
= cos y
dy
dy 1
=
dx cos y

```

and as sin2 y + cos2 y = 1, then
```

cos y = 1 − sin2 y = 1 − x2

```

and
```
d 1
arcsin x = √ .
dx 1 − x2

```

Using a similar technique, it can be shown that

```
d 1
arccos x = − √
dx 1 − x2
d 1
arctan x = .
dx 1 + x2

```

It follows that
```

dx
√ = arcsin x + C
1 − x2

dx
= arctan x + C.
1 + x2



```

18.9.6 Differentiating arccsc, arcsec and arccot

Let
```
y = arccsc x

```

then

```
x = csc y
1
=
sin y
```


<a id='p484'></a>
<!-- Página 484 -->

472 18 Calculus: Derivatives

```
dx − cos y
=
dy sin2 y
dy − sin2 y
=
dx cos y
1 x
=− 2√
x x −1
2

d 1
arccsc x = − √ .
dx x x2 − 1

```

Similarly,

```
d 1
arcsec x = √
dx x x2 − 1
d 1
arccot x = − 2 .
dx x +1

```

It follows:
```

dx
√ = arcsec |x| + C
x x2 − 1

dx
= − arccot x + C.
x2 + 1




```

18.10 Differentiating Hyperbolic Functions

Trigonometric functions are useful for parametric, circular motion, whereas hyperbolic functions arise in equations for the absorption of light, mechanics and in integral
calculus. Figure 18.16 shows graphs of the unit circle and a hyperbola whose respective equations are


Fig. 18.16 Graphs of the
unit circle x 2 + y 2 = 1 and
the hyperbola x 2 − y 2 = 1 2 Q


## 1 P


```
-4 -3 -2 -1 0 1 2 3 4


-1


-2
```


<a id='p485'></a>
<!-- Página 485 -->

18.10 Differentiating Hyperbolic Functions 473

```
x 2 + y2 = 1
x 2 − y2 = 1

```

where the only difference between them is a sign. The parametric form for the
trigonometric, or circular functions and the hyperbolic functions are respectively:

```
sin2 θ + cos2 θ = 1
cosh2 x − sinh2 x = 1.

```

The three hyperbolic functions have the following definitions:

```
e x − e−x
sinh x =
2
e x + e−x
cosh x =
2
sinh x e2x − 1
tanh x = = 2x
cosh x e +1

```

and their reciprocals are:

```
1 2
cosech x = = x
sinh x e − e−x
1 2
sech x = = x
cosh x e + e−x
1 e2x + 1
coth x = = 2x .
tanh x e −1

```

Other useful identities include:

```
sech 2 x = 1 − tanh2 x
cosech 2 x = coth2 x − 1.

```

The coordinates of P and Q in Fig. 18.16 are given by P(cos θ, sin θ ) and
Q(cosh x, sinh x). Table 18.1 shows the names of the three hyperbolic functions,
their reciprocals and inverse forms. As these functions are based upon e x and e−x ,
they are relatively easy to differentiate.


Table 18.1 Hyperbolic function names
Function Reciprocal Inverse Function Inverse Reciprocal
sinh cosech arsinh arcsch
cosh sech arcosh arsech
tanh coth artanh arcoth

<a id='p486'></a>
<!-- Página 486 -->

474 18 Calculus: Derivatives

18.10.1 Differentiating sinh, cosh and tanh

Here are the rules for differentiating hyperbolic functions:

```
y dy/d x
sinh x cosh x
cosh x sinh x
tanh x sech2 x
cosech x − cosech x coth x
sech x − sech x tanh x
coth x − cosech2 x

```

and the inverse, hyperbolic functions:

```
y dy/d x
1
arsinh x √
1 + x2
1
arcosh x √
x −1
2
1
artanh x
1 − x2
1
arcsch x − √
x 1 + x2
1
arsech x − √
x 1 − x2
1
arcoth x − 2
x −1

```

Here are the rules for integrating hyperbolic functions:
```

f (x) f (x) d x
sinh x cosh x + C
cosh x sinh x + C
sech2 x tanh x + C

```

and the inverse, hyperbolic functions:
```

f (x) f (x) d x
1
√ arsinh x + C
1 + x2
1
√ arcosh x + C
x2 − 1
1
artanh x + C.
1 − x2
```


<a id='p487'></a>
<!-- Página 487 -->

18.11 Higher Derivatives 475

18.11 Higher Derivatives

There are three parts to this section: The first part shows what happens when a function
is repeatedly differentiated; the second shows how these higher derivatives resolve
local minimum and maximum conditions; and the third section provides a physical
interpretation for these derivatives. Let’s begin by finding the higher derivatives of
simple polynomials.



18.12 Higher Derivatives of a Polynomial

We have previously seen that polynomials of the form

```
y = ax r + bx s + cx t . . .

```

are differentiated as follows:
```
dy
= rax r −1 + sbx s−1 + tcx t−1 . . . .
dx
```

For example, given
```
y = 3x 3 + 2x 2 − 5x

```

then
```
dy
= 9x 2 + 4x − 5
dx
```

which describes how the slope of the original function changes with x.
Figure 18.17 shows the graph of y = 3x 3 + 2x 2 − 5x and its derivative y = 9x 2 +
4x − 5, and we can see that when x = −1 there is a local maximum, where the
```
function reaches a value of 4, then begins a downward journey to 0, where the slope
```

is −5. Similarly, when x ≃ 0.55, there is a point where the function reaches a local


Fig. 18.17 Graph of
y = 3x 3 + 2x 2 − 5x 4
and its derivative
dy
d x = 9x + 4x − 5 (dashed)
```
2
2



-2 -1 0 1 2

-2


-4
```


<a id='p488'></a>
<!-- Página 488 -->

476 18 Calculus: Derivatives

minimum with a value of approximately −1.65. The slope is zero at both points,
which is reflected in the graph of the derivative.
```
Having differentiated the function once, there is nothing to prevent us differen-
```

tiating a second time, but first we require a way to annotate the process, which is
performed as follows. At a general level, let y be some function of x, then the first
derivative is
```
d
(y).
dx
```

The second derivative is found by differentiating the first derivative:
```
 
d dy
dx dx

```

and is written:
```
d2 y
.
dx2
```

Similarly, the third derivative is
```
d3 y
dx3
```

and the nth derivative:
```
dn y
.
dxn

```

When a function is expressed as f (x), its derivative is written f  (x). The second
derivative is written f  (x), and so on for higher derivatives.
Returning to the original function, the first and second derivatives are

```
dy
= 9x 2 + 4x − 5
dx
d2 y
= 18x + 4
dx2
```

and the third and fourth derivatives are

```
d3 y
= 18
dx3
d4 y
= 0.
dx4
```

Figure 18.18 shows the original function and the first two derivatives. The graph of
the first derivative shows the slope of the original function, whereas the graph of
the second derivative shows the slope of the first derivative. These graphs help us
identify a local maximum and minimum. By inspection of Fig. 18.18, when the first
derivative equals zero, there is a local maximum or a local minimum. Algebraically,

<a id='p489'></a>
<!-- Página 489 -->

18.12 Higher Derivatives of a Polynomial 477

Fig. 18.18 Graph of
y = 3x 3 + 2x 2 − 5x, its first 4
derivative
dy
d x = 9x + 4x − 5 (short
```
2
2
```

dashes) and its second
```
2
```

derivative dd x y2 = 18x + 4
(long dashes) -2 -1 0 1 2

```
-2


-4




```

this is when
```
dy
=0
dx
9x 2 + 4x − 5 = 0.

```

Solving this quadratic in x we have
```
√
−b ± b2 − 4ac
x=
2a
```

where a = 9, b = 4, c = −5:
```
√
−4 ± 16 + 180
x=
18
x1 = −1, x2 ≈ 0.555

```

which confirms our earlier analysis. However, what we don’t know, without referring
to the graphs, whether it is a minimum, or a maximum.



18.13 Identifying a Local Maximum or Minimum

Figure 18.19 shows a function containing a local maximum of 5 when x = −1. Note
that as the independent variable x, increases from −2 towards 0, the slope of the
graph changes from positive to negative, passing through zero at x = −1. This is
shown in the function’s first derivative, which is the straight line passing through the
points (−2, 6), (−1, 0) and (0, −6). A natural consequence of these conditions
implies that the slope of the first derivative must be negative:

<a id='p490'></a>
<!-- Página 490 -->

478 18 Calculus: Derivatives

Fig. 18.19 A function
containing a local maximum, 6

and its first derivative
```
4
```

(dashed)
```
2


-2 -1 0 1

-2


-4


-6


```

Fig. 18.20 A function
```
6
```

containing a local minimum,
and its first derivative 4
(dashed)
```
2


-3 -2 -1 0 1

-2


-4


-6




d2 y
= −ve.
dx2
```

Figure 18.20 shows another function containing a local minimum of −5 when
x = −1. Note that as the independent variable x, increases from −2 towards 0,
the slope of the graph changes from negative to positive, passing through zero at
x = −1. This is shown in the function’s first derivative, which is the straight line
passing through the points (−2, −6), (−1, 0) and (0, 6). A natural consequence
of these conditions implies that the slope of the first derivative must be positive:

```
d2 y
= +ve.
dx2
```

We can now apply this observation to the original function for the two values of x,
x1 = −1, x2 ≈ 0.555:

```
dy
= 9x 2 + 4x − 5
dx
d2 y
= 18x + 4.
dx2
```


<a id='p491'></a>
<!-- Página 491 -->

18.13 Identifying a Local Maximum or Minimum 479

Fig. 18.21 Graph of
y = −3x 3 + 9x, its first 24


derivative y = −9x 2 + 9 18
(short dashes) and its second
derivative y = −18x (long 12

dashes) 6


```
-2 -1 0 1 2


-6


-12


-18




d2 y
x = −1, = 18 × (−1) + 4 = −14
dx2
d2 y
x = 0.555, = 18 × (0.555) + 4 = 14.
dx2
```

Which confirms that when x = −1 there is a local maximum, and when x ≈ 0.555,
there is a local minimum, as shown in Fig. 18.17.

Now let’s find the local minimum and maximum for y, given

```
y = −3x 3 + 9x.

```

The first derivative is
```
dy
= −9x 2 + 9
dx
```

and second derivative
```
d2 y
= −18x
dx2
```

as shown in Fig. 18.21. For a local maximum or minimum, the first derivative equals
zero:
```
−9x 2 + 9 = 0

```

which implies that x = ±1.
The sign of the second derivative determines whether there is a local minimum
or maximum.

```
d2 y
= −18x
dx2
= −18 × (−1) = +ve
= −18 × (+1) = −ve
```


<a id='p492'></a>
<!-- Página 492 -->

480 18 Calculus: Derivatives

therefore, when x = −1 there is a local minimum, and when x = +1 there is a local
maximum, as confirmed by Fig. 18.21.



18.14 Partial Derivatives

Up to this point we have used functions with one independent variable, such as
y = f (x). However, we must be able to compute derivatives of functions with more
than one independent variable, such as y = f (u, v, w). The technique employed is
to assume that only one variable changes, whilst the other variables are held constant.
This means that a function can possess several derivatives—one for each independent
variable. Such derivatives are called partial derivatives and employ a new symbol ∂,
which can be read as ‘partial dee’.
```
Given a function f (u, v, w), the three partial derivatives are defined as

∂f f (u + h, v, w) − f (u, v, w)
= lim
∂u h→0 h
∂f f (u, v + h, w) − f (u, v, w)
= lim
∂v h→0 h
∂f f (u, v, w + h) − f (u, v, w)
= lim .
∂w h→0 h

```

For example, a function for the volume of a cylinder is

```
V (r, h) = πr 2 h

```

where r is the radius, and h is the height. Say we wish to compute the function’s
partial derivative with respect to r . First, the partial derivative is written


## ∂V

```
.
∂r
```

Second, we hold h constant, whilst allowing r to change. This means that the function
becomes
```
V (r, h) = kr 2 (18.5)

```

where k = π h. Thus the partial derivative of (18.5) with respect to r is


## ∂V

```
= 2kr
∂r
= 2π hr.

```

Next, by holding r constant, and allowing h to change, we have

<a id='p493'></a>
<!-- Página 493 -->

18.14 Partial Derivatives 481


## ∂V

```
= πr 2 .
∂h
```

Sometimes, for purposes of clarification, the partial derivatives identify the constant
variable(s):
```
 
```


## ∂V

```
= 2π hr
∂r h
 
```


## ∂V

```
= πr 2 .
∂h r

```

Partial differentiation is subject to the same rules for ordinary differentiation—we just
to have to remember which independent variable changes, and those held constant.
As with ordinary derivatives, we can compute higher-order partial derivatives.
As an example, let’s find the second-order partial derivatives of f , given

```
f (u, v) = u 4 + 2u 3 v 2 − 4v 3 .

```

The first partial derivatives are

```
∂f
= 4u 3 + 6u 2 v 2
∂u
∂f
= 4u 3 v − 12v 2
∂v
```

and the second-order partial derivatives are

```
∂2 f
= 12u 2 + 12uv 2
∂u 2
∂2 f
= 4u 3 − 24v.
∂v 2
```

Now let’s find the second-order partial derivatives of f , given

```
f (u, v) = sin(4u) cos(5v)

```

the first partial derivatives are

```
∂f
= 4 cos(4u) cos(5v)
∂u
∂f
= −5 sin(4u) sin(5v)
∂v
```

and the second-order partial derivatives are

<a id='p494'></a>
<!-- Página 494 -->

482 18 Calculus: Derivatives

```
∂2 f
= −16 sin(4u) cos(5v)
∂u 2
∂ f
2
= −25 sin(4u) cos(5v).
∂v 2
```

In general, given f (u, v) = uv, then

```
∂f
=v
∂u
∂f
=u
∂v
```

and the second-order partial derivatives are

```
∂2 f
=0
∂u 2
∂ f
2
= 0.
∂v 2
```

Similarly, given f (u, v) = u/v, then

```
∂f 1
=
∂u v
∂f u
=− 2
∂v v
```

and the second-order partial derivatives are

```
∂2 f
=0
∂u 2
∂2 f 2u
= 3.
∂v 2 v
```

Finally, given f (u, v) = u v , then

```
∂f
= vu v−1
∂u
```

whereas, ∂ f /∂v requires some explaining. First, given

```
f (u, v) = u v

```

taking natural logs of both sides, we have

```
ln f (u, v) = v ln u
```


<a id='p495'></a>
<!-- Página 495 -->

18.14 Partial Derivatives 483

and
```
f (u, v) = ev ln u .

```

Therefore,

```
∂f
= ev ln u ln u
∂v
= u v ln u.

```

The second-order partial derivatives are

```
∂2 f
= v(v − 1)u v−2
∂u 2
∂2 f
= u v ln2 u.
∂v 2




```

18.14.1 Visualising Partial Derivatives

Functions of the form y = f (x) are represented by a 2D graph, and the function’s
derivative f  (x) represents the graph’s slope at any point x. Functions of the form
z = f (x, y) can be represented by a 3D surface, like the one shown in Fig. 18.22,
which is z(x, y) = 2.5x 2 − 2.5y 2 . The two partial derivatives are

```
∂z
= 8x
∂x
∂z
= −4y
∂y


```

Fig. 18.22 Surface of
z = 2.5x 2 − 2.5y 2 using a
right-handed axial system
with a vertical z-axis

<a id='p496'></a>
<!-- Página 496 -->

484 18 Calculus: Derivatives

Fig. 18.23 ∂∂zx describes the
slopes of these contour lines




Fig. 18.24 ∂∂zy describes the
slopes of these contour lines




where ∂z/∂ x is the slope of the surface in the x-direction, as shown in Fig. 18.23,
and ∂z/∂ y is the slope of the surface in the y-direction, as shown in Fig. 18.24.
The second-order partial derivatives are

```
∂2z
= 8 = +ve
∂x2
∂2z
= −4 = −ve.
∂ y2

```

As ∂ 2 z/∂ x 2 is positive, there is a local minimum in the x-direction, and as ∂ 2 z/∂ y 2
is negative, there is a local maximum in the y-direction, as confirmed by Fig. 18.23.

<a id='p497'></a>
<!-- Página 497 -->

18.14 Partial Derivatives 485

18.14.2 Mixed Partial Derivatives

We have seen that, given a function of the form f (u, v), the partial derivatives
∂ f /∂u and ∂ f /∂v provide the relative instantaneous changes in f and u, and f
and v, respectively, whilst the second independent variable remains fixed. However,
nothing prevents us from differentiating ∂ f /∂u with respect to v, whilst keeping u
constant:  
```
∂ ∂f
∂v ∂u

```

which is also written as
```
∂2 f
∂v∂u
```

and is a mixed partial derivative.
As an example, let’s find the mixed partial derivative of f , given

```
f (u, v) = u 3 v 4 .

```

Therefore,
```
∂f
= 3u 2 v 4
∂u
```

and
```
∂2 f
= 12u 2 v 3 .
∂v∂u
```

It should be no surprise that reversing the differentiation gives the same result. Let

```
f (u, v) = u 3 v 4

```

then
```
∂f
= 4u 3 v 3
∂v
```

and
```
∂2 f
= 12u 2 v 3 .
∂u∂v
```

Generally, for continuous functions, we can write

```
∂2 f ∂2 f
= .
∂u∂v ∂v∂u
```

Let’s look at two examples. The formula for the volume of a cylinder is given
by V (r, h) = πr 2 h, where r and h are the cylinder’s radius and height, respectively.
The mixed partial derivative is computed as follows.

<a id='p498'></a>
<!-- Página 498 -->

486 18 Calculus: Derivatives

```
V (r, h) = πr 2 h
```


## ∂V

```
= 2π hr
∂r
```


## ∂2V

```
= 2πr
∂h∂r
```

or

```
V (r, h) = πr 2 h
```


## ∂V

```
= πr 2
∂h
```


## ∂2V

```
= 2πr.
∂r ∂h
Given
f (u, v) = sin(4u) cos(3v)

```

then
```
∂f
= 4 cos(4u) cos(3v)
∂u
∂2 f
= −12 cos(4u) sin(3v)
∂v∂u
```

or
```
∂f
= −3 sin(4u) sin(3v)
∂v
∂ f
2
= −12 cos(4u) sin(3v).
∂u∂v


```

18.15 Chain Rule

Earlier, we came across the chain rule for computing the derivatives
```
  of functions
```

of functions. For example, to compute the derivative of y = sin x 2 we substitute
u = x 2 , then

```
y = sin u
dy
= cos u
du  
= cos x 2 .

```

Next, we compute du/d x:

<a id='p499'></a>
<!-- Página 499 -->

18.15 Chain Rule 487

```
u = x2
du
= 2x
dx
```

and dy/d x is the product of the two derivatives using the chain rule:

```
dy dy du
= ·
dx du  d x
= cos x 2 2x
 
= 2x cos x 2 .

```

But say we have a function where w is a function of two variables x and y, which in
turn, are a function of u and v. Then we have

```
w = f (x, y)
x = r (u, v)
y = s(u, v).

```

With such a scenario, we have the following partial derivatives:

```
∂w ∂w
,
∂x ∂y
∂w ∂w
,
∂u ∂v
∂x ∂x
,
∂u ∂v
∂y ∂y
, .
∂u ∂v
```

These are chained together as follows

```
∂w ∂w ∂ x ∂w ∂ y
= · + · (18.6)
∂u ∂ x ∂u ∂ y ∂u
∂w ∂w ∂ x ∂w ∂ y
= · + · . (18.7)
∂v ∂ x ∂v ∂ y ∂v

```

Here is an example of the chain rule. Find ∂w/∂u and ∂w/∂v, given

```
w = f (2x + 3y)
 
x = r u 2 + v2
 
y = s u 2 − v2 .

```

Therefore

<a id='p500'></a>
<!-- Página 500 -->

488 18 Calculus: Derivatives

```
∂w ∂w
= 2, =3
∂x ∂y
∂x ∂x
= 2u, = 2v
∂u ∂v
∂y ∂y
= 2u, = −2v
∂u ∂v
```

and plugging these into (18.6) and (18.7) we have

```
∂w ∂w ∂ x ∂w ∂ y
= +
∂u ∂ x ∂u ∂ y ∂u
= 2 × 2u + 3 × 2u
= 10u
∂w ∂w ∂ x ∂w ∂ y
= +
∂v ∂ x ∂v ∂ y ∂v
= 2 × 2v + 3 × (−2v)
= −2v.

```

Thus, when u = 2 and v = 1

```
∂w ∂w
= 20, and = −2.
∂u ∂v


```

18.16 Total Derivative

Given a function with three independent variables, such as w = f (x, y, t), where
x = g(t) and y = h(t), there are three primary partial derivatives:

```
∂w ∂w ∂w
, ,
∂x ∂y ∂t

```

which show the differential change of w with x, y and t respectively. There are also
three derivatives:
```
dx dy dt
, ,
dt dt dt
```

where dt/dt = 1. The partial and ordinary derivatives can be combined to create the
total derivative which is written
```
dw ∂w d x ∂w dy ∂w
= + + .
dt ∂ x dt ∂ y dt ∂t
```


<a id='p501'></a>
<!-- Página 501 -->

18.16 Total Derivative 489

dw/dt measures the instantaneous change of w relative to t, when all three independent variables change.
Let’s find dw/dt, given

```
w = x 2 + x y + y3 + t 2
x = 2t
y = t − 1.

```

Therefore,

```
dx
=2
dt
dy
=1
dt
∂w
= 2x + y = 4t + t − 1 = 5t − 1
∂x
∂w
= x + 3y 2 = 2t + 3(t − 1)2 = 3t 2 − 4t + 3
∂y
∂w
= 2t
∂t
dw ∂w d x ∂w dy ∂w
= + +
dt ∂ x dt ∂ y dt ∂t
 2 
= (5t − 1)2 + 3t − 4t + 3 + 2t = 3t 2 + 8t + 1

```

and the total derivative equals

```
dw
= 3t 2 + 8t + 1
dt
```

and when t = 1, dw/dt = 12.



18.17 Summary

This chapter has shown how limits provide a useful tool for computing a function’s
derivative. Basically, the function’s independent variable is disturbed by a very small
quantity, typically δx, which alters the function’s value. The quotient

```
f (x + δx) − f (x)
δx
```

is a measure of the function’s rate of change relative to its independent variable. By
making δx smaller and smaller towards zero, we converge towards a limiting value

<a id='p502'></a>
<!-- Página 502 -->

490 18 Calculus: Derivatives

called the function’s derivative. Unfortunately, not all functions possess a derivative,
therefore we can only work with functions that can be differentiated.
We have seen how to differentiate generic functions such as sums, products, quotients and a function of a function, and we have also seen how to address explicit
and implicit forms. These techniques were then used to differentiate exponential,
logarithmic, trigonometric and hyperbolic functions, which will be employed in
later chapters to solve various problems. Where relevant, integrals of certain functions have been included to show the intimate relationship between derivatives and
antiderivatives.
Hopefully, it is now clear that differentiation is like an operator—in that it describes
how fast a function changes relative to its independent variable in the form of another
function.



Reference

1. Vince JA (2013) Calculus for computer graphics, 2nd edn. Springer

<a id='p503'></a>
<!-- Página 503 -->


## Chapter 19

Calculus: Integration




19.1 Introduction

In this chapter I develop the idea that integration is the inverse of differentiation, and
examine standard algebraic strategies for integrating functions, where the derivative
is unknown; these include simple algebraic manipulation, trigonometric identities,
integration by parts, integration by substitution and integration using partial fractions.



19.2 Indefinite Integral

In the previous chapter we have seen that given a simple function, such as

```
y = sin x + 23
dy
= cos x
dx
```

and the constant term 23 disappears. Inverting the process, we begin with

```
dy = cos x d x

```

and integrating:
```

y= cos x d x

= sin x + C.

```

An integral of the form 
```
f (x) d x

```

© Springer-Verlag London Ltd., part of Springer Nature 2022 491
J. Vince, Mathematics for Computer Graphics, Undergraduate Topics
in Computer Science, https://doi.org/10.1007/978-1-4471-7520-9_19

<a id='p504'></a>
<!-- Página 504 -->

492 19 Calculus: Integration

is known as an indefinite integral; and as we don’t know whether the original function
contains a constant term, a constant C has to be included. Its value remains undetermined unless we are told something about the original function. In this example, if
we are told that when x = π/2, y = 24, then
```
 
24 = sin π/2 + C
```


## =1+C


## C = 23.




19.3 Integration Techniques

19.3.1 Continuous Functions

Functions come in all sorts of shapes and sizes, which is why we have to be very
careful before they are differentiated or integrated. If a function contains any form of
discontinuity, then it cannot be differentiated or integrated. For example, the squarewave function shown in Fig. 19.1 cannot be differentiated as it contains discontinuities. Consequently, to be very precise, we identify an interval [a, b], over which a
```
function is analysed, and stipulate that it must be continuous over this interval. For
```

example, a and b define the upper and lower bounds of the interval such that

```
a≤x ≤b

```

then we can say that for f (x) to be continuous

```
lim f (x + h) = f (x).
h→0

```

Even this needs further clarification as h must not take x outside of the permitted
interval. So, from now on, we assume that all functions are continuous and can be
integrated without fear of singularities.

Fig. 19.1 A discontinuous
```
2
```

square-wave function

```
1




-1 0 1 2 3 4 5


-1



-2
```


<a id='p505'></a>
<!-- Página 505 -->

19.3 Integration Techniques 493

19.3.2 Difficult Functions

There are many functions that cannot be differentiated and represented by a finite
collection of elementary functions. For example, the derivative f  (x) = (sin x)/x
does not exist, which precludes the possibility of its integration. Figure 19.2 shows
this function, and even though it is continuous, its √derivative and integral can only
be approximated. Similarly, the derivative f  (x) = x sin x does not exist, and also
precludes the possibility of its integration. Figure 19.3 shows this continuous function. So now let’s examine how most functions have to be rearranged to secure their
integration.



19.3.3 Trigonometric Identities

Sometimes it is possible to simplify the integrand
```
 by substituting a trigonometric
2
```

identity.
 To illustrate this, let’s evaluate sin x d x, cos2 x d x, tan2 x d x and
sin(3x) cos x d x.



Fig. 19.2 Graph of
```
1
```

y = (sin x)/x




```
-2 0 2




-1




```

Fig. 19.3
```
√ Graph of
3
```

y = x sin x
```
2


1


0 2

-1


-2


-3
```


<a id='p506'></a>
<!-- Página 506 -->

494 19 Calculus: Integration

The identity sin2 x = 21 (1 − cos(2x)) converts sin2 x into a double-angle form:
```
 
sin 2
x d x = 21 1 − cos(2x) d x
 
= 21 d x − 21 cos(2x) d x

= 21 x − 41 sin(2x) + C.

```

Figure 19.4 shows the graphs of y = sin2 x and y = 21 x − 41 sin(2x).
The identity cos2 x = 21 (cos(2x) + 1) converts cos2 x into a double-angle form:
```
 
cos 2
x d x = 21 cos(2x) + 1 d x
 
= 21 cos(2x) d x + 21 dx

= 41 sin(2x) + 21 x + C.

```

Figure 19.5 shows the graphs of y = cos2 x and y = 41 sin(2x) + 21 x.


Fig. 19.4 The graphs of
y = sin2 x (dashed) and 3
y = 21 x − 41 sin(2x)
```
2


1


-4 -3 -2 -1 0 1 2 3 4 5


-1


-2




```

Fig. 19.5 The graphs of
y = cos2 x (dashed) and 3
y = 41 sin(2x) + 21 x
```
2


1


-4 -3 -2 -1 0 1 2 3 4 5


-1


-2
```


<a id='p507'></a>
<!-- Página 507 -->

19.3 Integration Techniques 495

Fig. 19.6 The graphs of
y = tan2 x (dashed) and
y = tan x − x
```
4




-8 -4 0 4 8




-4




```

The identity sec2 x = 1 + tan2 x, permits us to write
```
 
tan x d x =
2
sec2 x − 1 d x
 
= sec2 x d x − d x

= tan x − x + C.

```

Figure 19.6 shows the graphs of y = tan2 x and y = tan x − x.
```

```

Finally, to evaluate sin(3x) cos x d x we use the identity

```
2 sin a cos b = sin(a + b) + sin(a − b)

```

which converts the integrand’s product into the sum and difference of two angles:

```
sin(3x) cos x = 21 (sin(4x) + sin(2x))
 
sin(3x) cos x d x = 2 sin(4x) + sin(2x) d x
1

 
= 21 sin(4x) d x + 21 sin(2x) d x

= − 18 cos(4x) − 41 cos(2x) + C.

```

Figure 19.7 shows the graphs of y = sin(3x) cos x and y = − 18 cos(4x) − 41 cos(2x).



19.3.4 Exponent Notation

Radicals are best replaced by their equivalent exponent notation. For example, to
evaluate

<a id='p508'></a>
<!-- Página 508 -->

496 19 Calculus: Integration

Fig. 19.7 The graphs of
```
2
```

y = sin(3x) cos x (dashed)
and y =
− 18 cos(4x) − 41 cos(2x) 1




```
-3 -2 -1 0 1 2 3


-1



-2





2
√
4
dx
x

```

we proceed as follows:
The constant 2 is moved outside the integral, and the integrand is converted into an
exponent form:
```
 
1
x− 4
1
2 √
4
dx = 2
x
 3
x4
=2 3
```


## +C

```
4

4 34
=2 3
x +C
3
= 83 x + C.
4



√ 3
```

Figure 19.8 shows the graphs of y = 2/ 4 x and y = 8x 4 /3.


Fig. 19.8
```
√ The graphs of
```

y = 2/ 4 x (dashed) and
```
3
```

y = 8x 4 /3 4


```
3


2


1


-1 0 1 2 3 4 5 6 7 8

-1
```


<a id='p509'></a>
<!-- Página 509 -->

19.3 Integration Techniques 497

19.3.5 Completing the Square

Where possible, see if an integrand can be simplified by completing the square. For
example, to evaluate 
```
1
dx
x 2 − 4x + 8

```

we proceed as follows:
We have already seen that
```

1
d x = arctan x + C
1 + x2

```

and it’s not too difficult to prove that
```
 x
1 1
d x = arctan + C.
a2 + x 2 a a

```

Therefore, if we can manipulate an integrand into this form, then the integral will
reduce to an arctan result. The following needs no manipulation:
```
 x
1
d x = 1
arctan + C.
4 + x2 2
2

```

However, the original integrand has x 2 − 4x + 8 as the denominator, which is
resolved by completing the square:

```
x 2 − 4x + 8 = 4 + (x − 2)2 .

```

Therefore,
```
 
1 1
dx = dx
x 2 − 4x + 8 22 + (x − 2)2
x −2
= 21 arctan +C.
2
 x−2 
```

Figure 19.9 shows the graphs of y = 1/(x 2 − 4x + 8) and y = 21 arctan 2
```
.

```

To evaluate 
```
1
d x.
x 2 + 6x + 10

```

we factorize the denominator:

<a id='p510'></a>
<!-- Página 510 -->

498 19 Calculus: Integration

Fig. 19.9 The graphs of
y = 1/(x 2 − 4x + 8) 0.4
(dashed) and  
y = 21 arctan x−2
```
2 0.2




-3 -2 -1 0 1 2 3 4 5 6

-0.2


-0.4




```

Fig. 19.10 The graphs of
y = 1/(x 2 + 6x + 10)
```
1
```

(dashed) and
y = arctan(x + 3)


```
-7 -6 -5 -4 -3 -2 -1 0 1 2




-1




 
1 1
d x = dx
x + 6x + 10
2 1 + (x + 3)2
2

= arctan(x + 3) + C.

```

Figure 19.10 shows the graphs of y = 1/(x 2 + 6x + 10) and y = arctan(x + 3).




19.3.6 The Integrand Contains a Derivative

An integral of the form 
```
f (x) f  (x) d x

```

is relatively easy to integrate. For example, let’s evaluate
```

arctan x
d x.
1 + x2
```


<a id='p511'></a>
<!-- Página 511 -->

19.3 Integration Techniques 499

Knowing that
```
d 1
arctan x =
dx 1 + x2

let u = arctan x, then
du 1
=
dx 1 + x2

```

and
```
 
arctan x
d x = u du
1 + x2
= 21 u 2 + C
= 21 (arctan x)2 + C.

```

Figure 19.11 shows the graphs of y = arctan
```
1+x 2
x
and y = 21 (arctan x)2 .
```

An integral of the form  
```
f (x)
dx
f (x)

```

is also relatively easy to integrate. For example, let’s evaluate
```

cos x
d x.
sin x

```

Knowing that
```
d
sin x = cos x
dx
let u = sin x, then
du
= cos x
dx



```

Fig. 19.11 The graphs of
y = arctan
```
1+x 2
x
(dashed) and
1
```

y = 21 (arctan x)2



```
- 0




-1
```


<a id='p512'></a>
<!-- Página 512 -->

500 19 Calculus: Integration

Fig. 19.12 The graphs of
y = cos x/ sin x (dashed)
and y = ln | sin x| 2


```
1


- 0


-1


-2




```

and
```
 
cos x 1
dx = du
sin x u
= ln |u| + C
= ln | sin x| + C.

```

Figure 19.12 shows the graphs of y = cos x/ sin x and y = ln | sin x|.



19.3.7 Converting the Integrand into a Series of Fractions

Integration is often made easier by converting an integrand into a series of fractions.
For example, to integrate
```

4x 3 + x 2 − 8 + 12x cos x
dx
4x

```

we divide the numerator by 4x:
    
```
4x 3 + x 2 − 8 + 12x cos x x 2
dx = x2 dx + dx − d x + 3 cos x d x
4x 4 x
= 13 x 3 + 18 x 2 − 2 ln |x| + 3 sin x + C.
 
```

Figure 19.13 shows the graphs of y = 4x 3 + x 2 − 8 + 12x cos x /4x and y =
3
x + 18 x 2 − 2 ln |x| + 3 sin x.
1 3

<a id='p513'></a>
<!-- Página 513 -->

19.3 Integration Techniques 501

Fig. 19.13 The graphs of
y = (4x 3 + x 2 − 8 + 6
12x cos x)/4x (dashed) and
y = 13 x 3 + 18 x 2 − 2 ln |x| + 4
3 sin x
```
2


-3 -2 -1 0 1 2 3


-2


-4




```

19.3.8 Integration by Parts

Integration by parts is based upon the rule for differentiating function products where

```
d dv du
uv = u +v
dx dx dx
```

therefore,  
```
uv = uv  d x + vu  d x

```

which rearranged, gives
```
 
uv  d x = uv − vu  d x.

```

Thus, if an integrand contains a product of two functions, we can attempt to integrate
it by parts. For example, let’s evaluate
```

x sin x d x.

```

In this case, we try the following:

```
u = x and v  = sin x

```

therefore
```
u  = 1 and v = C1 − cos x.

```

Integrating by parts:

<a id='p514'></a>
<!-- Página 514 -->

502 19 Calculus: Integration

Fig. 19.14 The graphs of
y = x sin x (dashed) and
y = −x cos x + sin x
```
2




- 0




-2




 
uv  d x = uv − vu  d x
 
x sin x d x = x(C1 − cos x) − (C1 − cos x)(1) d x

= C1 x − x cos x − C1 x + sin x + C
= −x cos x + sin x + C.

```

Figure 19.14 shows the graphs of y = x sin x and y = −x cos x + sin x.
Note the problems that arise if we make the wrong substitution:

```
u = sin x and v  = x

```

therefore
```
u  = cos x and v = 21 x 2 + C1

```

Integrating by parts:
```
 

uv d x = uv − vu  d x
 
1 2  1 2 
x sin x d x = sin x 2
x + C1 − 2
x + C1 cos x d x

```

which requires to be integrated by parts, and is even more difficult, which suggests
the substitution was not useful.
Now let’s evaluate 
```
x 2 cos x d x.

```

In this case, we try the following:

```
u = x 2 and v  = cos x
```


<a id='p515'></a>
<!-- Página 515 -->

19.3 Integration Techniques 503

therefore
```
u  = 2x and v = sin x + C1 .

```

Integrating by parts:
```
 
uv  d x = uv − vu  d x
 
x cos x d x = x (sin x + C1 ) − 2
2 2
(sin x + C1 )(x) d x
 
= x 2 sin x + C1 x 2 − 2C1 x d x − 2 x sin x d x

 
= x 2 sin x + C1 x 2 − 2C1 21 x 2 + C2 − 2 x sin x d x

= x 2 sin x − C3 − 2 x sin x d x.


```

At this point we come across x sin x d x, which we have already solved:
```

x 2 cos x d x = x 2 sin x − C3 − 2(−x cos x + sin x + C4 )

= x 2 sin x − C3 + 2x cos x − 2 sin x − C5
= x 2 sin x + 2x cos x − 2 sin x + C

```

Figure 19.15 shows the graphs of y = x 2 cos x and y = x 2 sin x + 2x cos x − 2 sin x.
Now let’s evaluate 
```
x ln x d x.

```

In this case, we try the following:

```
u = ln x and v  = x


```

Fig. 19.15 The graphs of
y = x 2 cos x (dashed) and
y=
x 2 sin x + 2x cos x − 2 sin x 2




```
- 0




-2
```


<a id='p516'></a>
<!-- Página 516 -->

504 19 Calculus: Integration

therefore
```
1
u = and v = 21 x 2 .
x
```

Integrating by parts:
```
 

uv d x = uv − vu  d x
 
1
x ln x d x = 21 x 2 ln x − 1 2
2
x dx
x

= 21 x 2 ln x − 21 x d x

= 21 x 2 ln x − 14 x 2 + C.

```

Figure 19.16 shows the graphs of y = x ln x and y = 21 x 2 ln x − 41 x 2 .
Finally, let’s evaluate 
```
1 + x 2 d x.

```

Although this integrand does not look as though it can be integrated by parts, if we
rewrite it as 
```
1 + x 2 (1) d x.

```

then we can use the formula.
Let
```
u= 1 + x 2 and v  = 1

```

therefore x
```
u = √ and v = x.
1 + x2


```

Fig. 19.16 The graphs of
y = x ln x (dashed) and
```
6
```

y = 21 x 2 ln x − 41 x 2

```
4



2



-1 0 1 2 3 4



-2
```


<a id='p517'></a>
<!-- Página 517 -->

19.3 Integration Techniques 505

Fig. 19.17
```
√ The graphs of
```

y = 1 + x 2 (dashed) and 3

y =√
```
2
```

2 x 1 + x + 2 arsinh x
1 2 1

```
1


-4 -3 -2 -1 0 1 2 3 4

-1


-2


-3




```

Integrating by parts:
```
 

uv d x = uv − vu  d x
 
x2
1 + x dx = x 1 + x − √
2 2 d x.
1 + x2

```

Now we simplify the right-hand integrand:
```
 
(1 + x 2 ) − 1
1 + x2 dx = x 1 + x2 − √ dx
1 + x2
 
1 + x2 1
= x 1+x − √
2 dx + √ dx
1+x 2 1 + x2

= x 1 + x2 − 1 + x 2 d x + arsinh x + C1 .

```

Now we have the original integrand on the right-hand side, therefore
```

2 1 + x 2 d x = x 1 + x 2 + arsinh x + C1

1 + x 2 d x = 21 x 1 + x 2 + 21 arsinh x + C.

√ √
```

Figure 19.17 shows the graphs of y = 1 + x 2 and y = 21 x 1 + x 2 + 21 arsinh x.


19.3.9 Integration by Substitution

Integration by substitution is based upon the chain rule for differentiating a function
of a function, which states that if y is a function of u, which in turn is a function of
x, then

<a id='p518'></a>
<!-- Página 518 -->

506 19 Calculus: Integration

```
dy dy du
= .
dx du d x
```

For example, let’s evaluate  √
```
x 2 x 3 d x.

```

This is easily solved by rewriting the integrand:
```
 √ 
7
x2 x3 dx = x 2 dx
9
= 29 x 2 + C.

```

However, introducing a constant term within the square-root requires integration by
substitution. For example,
```

evaluate x 2 x 3 + 1 d x.

```

First, we let u = x 3 + 1, then

```
du du
= 3x 2 or d x = 2 .
dx 3x
```

Substituting u and d x in the integrand gives
```
 
√ du
x2 x3 + 1 dx = x2 u
3x 2

√
= 13 u du

1
= 13 u 2 du
3
= 13 · 23 u 2 + C
 3
= 29 x 3 + 1 2 + C.

√  3
```

Figure 19.18 shows the graphs of y = x 2 x 3 + 1 and y = 29 x 3 + 1 2 .
Now let’s evaluate 
```
2 sin x · cos x d x.

```

Integrating by substitution we let u = sin x, then

```
du du
= cos x or d x = .
dx cos x
```


<a id='p519'></a>
<!-- Página 519 -->

19.3 Integration Techniques 507

Fig. 19.18
```
√ The graphs of
```

y = x 2 x 3 + 1 (dashed)
```
 3 2
```

and y = 29 x 3 + 1 2

```
1




-1 0 1 2



-1




```

Fig. 19.19 The graphs of
y = 2 sin x · cos x (dashed)
and y = sin2 x 2


```
1


- 0


-1


-2




```

Substituting u and d x in the integrand gives
```
 
du
2 sin x · cos x d x = 2 u cos x
cos x

=2 u du

= u 2 + C1
= sin2 x + C.

```

Figure 19.19 shows the graphs of y = 2 sin x · cos x and y = sin2 x.
To evaluate 
```
2ecos 2x sin x · cos x d x.

```

we integrate by substitution, and let u = cos(2x), then

```
du du
= −2 sin(2x) or d x = − .
dx 2 sin(2x)
```


<a id='p520'></a>
<!-- Página 520 -->

508 19 Calculus: Integration

Fig. 19.20 The graphs of
y = 2ecos(2x) sin x · cos x
(dashed) and y = − 21 ecos(2x) 2


```
1



- 0


-1


-2




```

Substituting a double-angle identity, u and du:
```
 
du
2e cos 2x
sin x · cos x d x = − eu sin(2x)
2 sin(2x)

= − 21 eu du

= − 21 eu + C
= − 21 ecos(2x) + C.

```

Figure 19.20 shows the graphs of y = 2ecos(2x) sin x · cos x and y = − 21 ecos(2x) .
To evaluate 
```
cos x
d x.
(1 + sin x)3

```

we integrate by substitution, and let u = 1 + sin x, then

```
du du
= cos x or d x = .
dx cos x

 
cos x cos x du
dx =
(1 + sin x)3 u 3 cos x

= u −3 du

= − 21 u −2 + C
= − 21 (1 + sin x)−2 + C
1
```


## =− + C.

```
2(1 + sin x)2

```

Figure 19.21 shows the graphs of y = cos x/(1 + sin x)3 and y = − 21 (1 + sin x)−2 .

<a id='p521'></a>
<!-- Página 521 -->

19.3 Integration Techniques 509

```
4

3

2

1

-2 - 0 2
-1

-2

-3

-4


```

Fig. 19.21 The graphs of y = cos x/(1 + sin x)3 (dashed) and y = − 21 (1 + sin x)−2



To evaluate 
```
sin(2x) d x.

```

we integrate by substitution, and let u = 2x, then

```
du du
= 2 or d x = .
dx 2

 
sin(2x) d x = 21 sin u du

= − 21 cos u + C
= − 21 cos(2x) + C

```

Figure 19.22 shows the graphs of y = sin(2x) and y = − 21 cos(2x).




```
1




- 0




-1




```

Fig. 19.22 The graphs of y = sin(2x) (dashed) and y = − 21 cos(2x)

<a id='p522'></a>
<!-- Página 522 -->

510 19 Calculus: Integration

19.3.10 Partial Fractions

Integration by partial fractions is used when an integrand’s denominator contains
a product that can be split into two fractions. For example, it should be possible to
convert 
```
3x + 4
dx
(x + 1)(x + 2)

```

into  

## A B

```
dx + dx
x +1 x +2

```

which individually, are easy to integrate. Let’s compute A and B:

```
3x + 4 A B
= +
(x + 1)(x + 2) x +1 x +2
3x + 4 = A(x + 2) + B(x + 1)
= Ax + 2 A + Bx + B.

```

Equating constants and terms in x:


## 4 = 2A + B (19.1)


## 3= A+B (19.2)


Subtracting (19.2) from (19.1), gives A = 1 and B = 2. Therefore,
```
  
3x + 4 1 2
dx = dx + dx
(x + 1)(x + 2) x +1 x +2
= ln(x + 1) + 2 ln(x + 2) + C.

```

Figure 19.23 shows the graphs of y = (x+1)(x+2)
```
3x+4
and y = ln(x + 1) + 2 ln(x + 2).


```

Fig. 19.23 The graphs of
y = (x+1)(x+2)
```
3x+4
(dashed) and 4
```

y = ln(x + 1) + 2 ln(x + 2)
```
2



-4 -2 0 2 4



-2



-4
```


<a id='p523'></a>
<!-- Página 523 -->

19.3 Integration Techniques 511

Fig. 19.24 The graphs of
y = (x−1)(x−2)
```
5x−7
(dashed) and 4

```

y=
2 ln(x − 1) + 3 ln(x − 2) 2



```
-3 -2 -1 0 1 2 3 4 5 6


-2



-4



```

Now let’s evaluate 
```
5x − 7
d x.
(x − 1)(x − 2)

```

Integrating by partial fractions:

```
5x − 7 A B
= +
(x − 1)(x − 2) x −1 x −2
5x − 7 = A(x − 2) + B(x − 1)
= Ax + Bx − 2 A − B.

```

Equating constants and terms in x:


## −7 = −2 A − B (19.3)


## 5= A+B (19.4)


Subtracting (19.3) from (19.4), gives A = 2 and B = 3. Therefore,
```
  
5x − 7 2 3
dx = dx + dx
(x − 1)(x − 2) x −1 x −2
= 2 ln(x − 1) + 3 ln(x − 2) + C.

```

Figure 19.24 shows the graphs of y = (x−1)(x−2)
```
5x−7
and y = 2 ln(x − 1) + 3 ln(x − 2).
```

Finally, let’s evaluate 
```
6x 2 + 5x − 2
dx
x 3 + x 2 − 2x

```

using partial fractions:

<a id='p524'></a>
<!-- Página 524 -->

512 19 Calculus: Integration

Fig. 19.25 The graphs of
```
2 +5x−2 3
```

y = 6x
```
x 3 +x 2 −2x
(dashed) and
```

y = ln x + 2 ln(x + 2) + 2
3 ln(x − 1)
```
1


-4 -3 -2 -1 0 1 2 3 4

-1


-2


-3



6x 2 + 5x − 2 A B C
= + +
x + x − 2x
3 2 x x +2 x −1
6x 2 + 5x − 2 = A(x + 2)(x − 1) + Bx(x − 1) + C x(x + 2)
= Ax 2 + Ax − 2 A + Bx 2 − Bx + C x 2 + 2C x.

```

Equating constants, terms in x and x 2 :


## −2 = −2 A (19.5)


## 5 = A − B + 2C (19.6)


## 6= A+ B +C (19.7)


Manipulating (19.5), (19.6) and (19.7): A = 1, B = 2 and C = 3, therefore,
```
   
6x 2 + 5x − 2 1 2 3
d x = d x + d x + dx
x 3 + x 2 − 2x x x +2 x −1
= ln x + 2 ln(x + 2) + 3 ln(x − 1) + C.

+5x−2 2
```

Figure 19.25 shows the graphs of y = 6x
```
x 3 +x 2 −2x
and y = ln x + 2 ln(x + 2) +
```

3 ln(x − 1).


19.4 Area Under a Graph

The ability to calculate the area under a graph is one of the most important discoveries
of integral calculus. Prior to calculus, area was computed by dividing a zone into
very small strips and summing the individual areas. The accuracy of the result is
improved simply by making the strips smaller and smaller, taking the result towards
some limiting value. In this section, I show how integral calculus provides a way to
compute the area between a function’s graph and the x- and y-axis.

<a id='p525'></a>
<!-- Página 525 -->

19.5 Calculating Areas 513

19.5 Calculating Areas

Before considering the relationship between area and integration, let’s see how area
is calculated using functions and simple geometry.
```
Figure 19.26 shows the graph of y = 1, where the area A of the shaded zone is

A = x, x > 0.

```

For example, when x = 4, A = 4, and when x = 10, A = 10. An interesting observation is that the original function is the derivative of A:

```
dA
= 1 = y.
dx
```

Figure 19.27 shows the graph of y = 2x. The area A of the shaded triangle is

```
A = 21 base × height
= 21 x × 2x
= x 2.




```

Fig. 19.26 Area of the y
shaded zone is A = x
```
1 y=1




A=x




x x


```

Fig. 19.27 Area of the y
shaded zone is A = x 2 y = 2x




```
A = x2



x x
```


<a id='p526'></a>
<!-- Página 526 -->

514 19 Calculus: Integration

Fig. 19.28
```
√ Graph of y
```

y = r2 − x2
```
f(x)
y = r 2 x2


```


## A1


```
r
rcos
```


## A2



```
rsin x x




```

Thus, when x = 4, A = 16. Once again, the original function is the derivative of A:

```
dA
= 2x = y
dx
```

which is no coincidence.
Finally, Fig. 19.28 shows a circle where x 2 + y 2 = r 2 , and the curve of the first
quadrant is described by the function

```
y= r 2 − x 2 , 1 ≤ x ≤ r.

```

The total area of the shaded zones is the sum of the two parts A1 and A2 . To simplify
the calculations the function is defined in terms of the angle θ , such that

```
x = r sin θ

```

and
```
y = r cos θ.

```

Therefore,

```
A1 = 21 r 2 θ
A2 = 21 (r cos θ )(r sin θ ) = 41 r 2 sin(2θ )
```


## A = A1 + A2

```
 
= 21 r 2 θ + 21 sin(2θ ) .

```

To show that the total area is related to the function’s derivative, let’s differentiate A
with respect to θ :
```
dA
= 21 r 2 (1 + cos(2θ )) = r 2 cos2 θ.
dθ
```


<a id='p527'></a>
<!-- Página 527 -->

19.5 Calculating Areas 515

But we want the derivative dd Ax , which requires the chain rule

```
dA d A dθ
=
dx dθ d x
```

where
```
dx
= r cos θ
dθ
```

or
```
dθ 1
=
dx r cos θ
```

therefore,
```
dA r 2 cos2 θ
= = r cos θ = y
dx r cos θ
```

which is the equation for the quadrant.
Hopefully, these three examples provide strong evidence that the derivative of the
```
function for the area under a graph, equals the graph’s function:

dA
= f (x)
dx
```

which implies that 
```
A= f (x) d x.

```

Now let’s prove this observation using Fig. 19.29, which shows a continuous
```
function y = f (x). Next, we define a function A(x) to represent the area under the
```

graph over the interval [a, x]. δ A is the area increment between x and x + δx, and

```
δ A ≈ f (x) · δx.


```

Fig. 19.29 Relationship y
between y = f (x) and A(x)

```
y = f(x)




A(x) A




a x x+ x x
```


<a id='p528'></a>
<!-- Página 528 -->

516 19 Calculus: Integration

We can also reason that

```
δ A = A(x + δx) − A(x) ≈ f (x) · δx

```

and the derivative dd Ax is the limiting condition:

```
dA A(x + δx) − A(x) f (x) · δx
= lim = lim = f (x)
dx δx→0 δx δx→0 δx

```

thus,
```
dA
= f (x),
dx
```

whose antiderivative is 
```
A(x) = f (x) d x.

```

The function A(x) computes the area over the interval [a, b] and is represented by
```
 b
A(x) = f (x) d x
a

```

which is called the integral or definite integral.
Let’s assume that A(b) is the area under the graph of f (x) over the interval [0, b],
as shown in Fig. 19.30, and is written
```
 b
A(b) = f (x) d x.
0

```

Similarly, let A(a) be the area under the graph of f (x) over the interval [0, a], as
shown in Fig. 19.31, and is written


Fig. 19.30 A(b) is the area y
under the graph y = f (x),
0≤x ≤b
```
y = f(x)




A(b)




b x
```


<a id='p529'></a>
<!-- Página 529 -->

19.5 Calculating Areas 517

Fig. 19.31 A(a) is the area y
under the graph y = f (x),
0≤x ≤a
```
y = f(x)




A(a)



a x


```

Fig. 19.32 A(b) − A(a) is y
the area under the graph
y = f (x), a ≤ x ≤ b
```
y = f(x)




A(b)-A(a)



a b x


 a
A(a) = f (x) d x.
0

```

Figure 19.32 shows that the area of the shaded zone over the interval [a, b] is
calculated by
```
A = A(b) − A(a)

```

which is written  b  a
```
A= f (x) d x − f (x) d x
0 0

```

and is contracted to  b
```
A= f (x) d x. (19.8)
a

```

The fundamental theorem of calculus states that the definite integral
```
 b
f (x) d x = F(b) − F(a)
a
```


<a id='p530'></a>
<!-- Página 530 -->

518 19 Calculus: Integration

where
```

F(a) = f (x) d x, x = a

F(b) = f (x) d x, x = b.

```

In order to compute the area beneath a graph of f (x) over the interval [a, b], we
first integrate the graph’s function
```

F(x) = f (x) d x

```

and then calculate the area, which is the difference

```
A = F(b) − F(a).

```

To illustrate how (19.8) is used in the context of the earlier three examples, let’s
calculate the area over the interval [1, 4] for y = 1, as shown in Fig. 19.33. We
begin with
```
 4
A= 1 d x.
1

```

Next, we integrate the function, and transfer the interval bounds employing the sub-
```
4  4 4
```

stitution symbol , or square brackets . Using , we have
```
1 1 1



```

Fig. 19.33 Area under the
```
4 y
```

graph is 1 1 d x
```
1 y=1



4
A= 1 dx
1




1 4 x
```


<a id='p531'></a>
<!-- Página 531 -->

19.5 Calculating Areas 519

Fig. 19.34 Area under the
```
4 y
```

graph is 1 2x d x y = 2x




```
4
A= 2x dx
1




1 4 x



4
A= x
1
=4−1
=3
 4
```

or using , we have
```
1

 4
A= x
1
=4−1
= 3.

```

I will continue with square brackets.
Now let’s calculate the area over the interval [1, 4] for y = 2x, as shown in Fig.
19.34. We begin with
```
 4
A= 2x d x.
1

```

Next, we integrate the function and evaluate the area
```
 4
A = x2
1
= 16 − 1
= 15.
√
Finally, let’s calculate the area over the interval [0, r ] for y = r 2 − x 2 , which
```

is the equation for a circle, as shown in Fig. 19.35. We begin with

<a id='p532'></a>
<!-- Página 532 -->

520 19 Calculus: Integration

Fig. 19.35 Area under the
```
r √ y
```

graph is 0 r 2 − x 2 d x
```
y = r 2 x2

(rsin , rcos )




r x


 r
A= r 2 − x 2 d x. (19.9)
0

```

Unfortunately, (19.9) contains a function of a function, which is resolved by substituting another independent variable. In this case, the geometry of the circle suggests

```
x = r sin θ

```

therefore,
```
r 2 − x 2 = r cos θ

```

and
```
dx
= r cos θ. (19.10)
dθ
```

However, changing the independent variable requires changing the interval for the
integral. In this case, changing 0 ≤ x ≤ r into θ1 ≤ θ ≤ θ2 :
When x = 0, r sin θ1 = 0, therefore θ1 = 0.
When x = r , r sin θ2 = r , therefore θ2 = π/2.
Thus, the new interval is [0, π/2].
Finally, the d x in (19.9) has to be changed into dθ , which using (19.10) makes

```
d x = r cos θ dθ.

```

Now we are in a position to rewrite the original integral using θ as the independent
variable:

<a id='p533'></a>
<!-- Página 533 -->

19.5 Calculating Areas 521
```
 π
2
A= (r cos θ )(r cos θ ) dθ
0
 π
2
= r2 cos2 θ dθ
0
 π
r2 2
= 1 + cos(2θ ) dθ
2 0
  π2
r2
= θ + 21 sin(2θ )
2 0
r2 π
=
2 2
πr 2
=
4

```

which makes the area of a full circle πr 2 .



19.6 Positive and Negative Areas

Area in the real world is always regarded as a positive quantity—no matter how it is
measured. In mathematics, however, area is often a signed quantity, and is determined
by the clockwise or anticlockwise direction of vertices. As we generally use a lefthanded Cartesian axial system in calculus, areas above the x-axis are positive, whilst
areas below the x-axis are negative. This can be illustrated by computing the area of
the positive and negative parts of a sine wave.
Figure 19.36 shows a sketch of a sine wave over one cycle, where the area above
the x-axis is labelled A1 , and the area below the x-axis is labelled A2 . These areas
are computed as follows.


Fig. 19.36 The two areas y
associated with a sine wave

```
y = sin x

π
A1 = sin xdx
0 2
x
2π
A2 = sin xdx
π
```


<a id='p534'></a>
<!-- Página 534 -->

522 19 Calculus: Integration

Fig. 19.37 The accumulated
```
2
```

area of a sine wave




```
1




0



 π
A1 = sin x d x
0
 π
= − cos x
0
=1+1
= 2.

```

However, A2 gives a negative result:
```
 2π
A2 = sin x d x
π
 2π
= − cos x
π
= −1 − 1
= −2.

```

This means that the area is zero over the bounds 0 to 2π , .
```
 2π
A2 = sin x d x
0
 2π
= − cos x
0
= −1 + 1
= 0.

```

Consequently, one must be very careful using this technique for functions that are
negative in the interval under investigation. Figure 19.37 shows a sine wave over the
interval [0, π ] and its accumulated area.

<a id='p535'></a>
<!-- Página 535 -->

19.7 Area Between Two Functions 523

19.7 Area Between Two Functions

Figure 19.38 shows the graphs of y = x 2 and y = x 3 , with two areas labelled A1 and
A2 . A1 is the area trapped between the two graphs over the interval [−1, 0] and A2
is the area trapped between the two graphs over the interval [0, 1]. These areas are
calculated very easily: in the case of A1 we sum the individual areas under the two
graphs, remembering to reverse the sign for the area associated with y = x 3 . For A2
we subtract the individual areas under the two graphs.
```
 0  0
A1 = x dx −
2
x3 dx
−1 −1
 3 0  4 0
x x
= −
3 −1 4 −1
= 13 + 14
= 12
7
.
 1  1
A2 = x2 dx − x3 dx
0 0
 3 1  4 1
x x
= −
3 0 4 0
= 13 − 14
= 12
1
.

```

Note, that in both cases the calculation is the same, which implies that when we
employ
```
 b
A= [ f (x) − g(x)] d x
a

```

A is always the area trapped between f (x) and g(x) over the interval [a, b].


Fig. 19.38 Two areas
between y = x 2 and y = x 3 1

```
y = x2 y = x2

A2 y = x3
```


## A1

```
-1 0 1

y = x3


-1
```


<a id='p536'></a>
<!-- Página 536 -->

524 19 Calculus: Integration

Fig. 19.39 The area
between y = sin x and y = sin x
```
1
```

y = 0.5


## A


```
(0.5236, 0.5) y = 0.5 (2.618, 0.5)



0 1 2 3




```

Let’s take another example, by computing the area A between y = sin x and the
line y = 0.5, as shown in Fig. 19.39. The horizontal line intersects the sine curve at
x = 30◦ and x = 150◦ , marked in radians as 0.5236 and 2.618 respectively.
```
 150◦  5π/6
A= sin x d x − 0.5 d x
30◦ π/6
 150◦  5π/6
= − cos x − 21 x
30◦ π/6
√ √ 
3 3 5π π
= + − 21 −
2 2 6 6
√ π
= 3−
3
≈ 0.685.




```

19.8 Areas with the y-Axis

So far we have only calculated areas between a function and the x-axis. So let’s
compute the area between a function and the y-axis. Figure 19.40 shows the function
y = x 2 over the interval [0, 4], where A1 is the area between the curve and the xaxis, and A2 is the area between the curve and y-axis. The sum A1 + A2 must equal
4 × 16 = 64, which is a useful control. Let’s compute A1 .

<a id='p537'></a>
<!-- Página 537 -->

19.8 Areas with the y-Axis 525

Fig. 19.40 The areas 16
between the x-axis and the
y-axis

```
A2 y = x2



```


## A1


```
4




 4
A1 = x2 dx
0
 3 4
x
=
3 0
= 64
3
≈ 21.333

```

which means that A2 ≈ 42.666. To compute A2 we construct an integral relative to
```
1
```

dy with a corresponding interval. If y = x 2 then x = y 2 , and the interval is [0, 16]:
```
 16
1
A2 = y 2 dy
0
 16
2 23
= 3y
0
= 23 64
≈ 42.666.




```

19.9 Area with Parametric Functions

When working with functions of the form y = f (x), the area under its curve and the
x-axis over the interval [a, b] is
```
 b
A= f (x) d x.
a
```


<a id='p538'></a>
<!-- Página 538 -->

526 19 Calculus: Integration

However, if the curve has a parametric form where

```
x = f x (t) and y = f y (t)

```

then we can derive an equivalent integral as follows.
First: We need to establish equivalent limits [α, β] for t, such that

```
a = f x (α) and b = f x (β).

```

Second: Any point on the curve has corresponding Cartesian and parametric coordinates:
```
x and f x (t)

y = f (x) and f y (t).

```

Third:

```
x = f x (t)
d x = f x (t)dt
 b
A= f (x) d x
a
 β
= f y (t) f x (t) dt
α

```

therefore  β
```
A= f y (t) f x (t) dt. (19.11)
α

```

Let’s apply (19.11) using the parametric equations for a circle

```
x = −r cos t
y = r sin t.

```

as shown in Fig. 19.41. Remember that the Cartesian interval is [a, b] left to right,
and the polar interval [α, β], must also be left to right, which is why x = −r cos t.
Therefore,

```
f x t = r sin t
f y (t) = r sin t
```


<a id='p539'></a>
<!-- Página 539 -->

19.9 Area with Parametric Functions 527

Fig. 19.41 The parametric y
functions for a circle




```
-rcost


rsint
t
0 x


 β
A= f y (t) f x (t) dt
α
 π
= r sin t · r sin t dt
 π
0

= r2 sin2 t dt
0

r2 π
= 1 − cos(2t) dt
2 0
 π
r2
= t + 21 sin(2t)
2 0
πr 2
=
2

```

which makes the area of a full circle πr 2 .



19.10 The Riemann Sum

The German mathematician Bernhard Riemann (1826–1866) (pronounced ‘Reeman’) made major contributions to various areas of mathematics, including integral
calculus, where his name is associated with a formal method for summing areas and
volumes. Through the Riemann Sum, Riemann provides an elegant and consistent
notation for describing single, double and triple integrals when calculating area and
volume. Let’s see how the Riemann sum explains why the area under a curve is the
function’s integral.
Figure 19.42 shows a function f (x) divided into eight equal sub-intervals where

```
b−a
Δx =
8
```


<a id='p540'></a>
<!-- Página 540 -->

528 19 Calculus: Integration

Fig. 19.42 The graph of y
```
function f (x) over the y = f(x)
```

interval [a, b]


```
h0 h 1 h 2 h3 h4 h5 h6 h7 h8




a x x x x x x x x b
x0 x1 x2 x3 x4 x5 x6 x7 x8 x




```

and
```
a = x0 < x1 < x2 < · · · < x7 < x8 = b.

```

In order to compute the area under the curve over the interval [a, b], the interval
is divided into some large number of sub-intervals. In this case, eight, which is not
very large, but convenient to illustrate. Each sub-interval becomes a rectangle with
a common width Δx and a different height. The area of the first rectangular subinterval shown shaded, can be calculated in various ways. We can take the left-most
height f (x0 ) and form the product f (x0 )Δx, or we can take the right-most height
f (x1 ) and form the product f (x1 )Δx. On the other hand, we could take the mean
of the two heights ( f (x0 ) + f (x1 ))/2 and form the product ( f (x0 ) + f (x1 ))Δx/2.
A solution that shows no bias towards either left, right or centre, is to let f (xi∗ ) be
anywhere in a specific sub-interval Δxi , then the area of the rectangle associated
with the sub-interval is f (xi∗ )Δxi , and the sum of the rectangular areas is given by

```

8
A= f (xi∗ )Δxi .
i=1

```

Dividing the interval into eight equal sub-intervals will not generate a very accurate
result for the area under the graph. But increasing it to eight-thousand or eightmillion, will take us towards some limiting value. Rather than specify some specific
large number, it is common practice to employ n, and let n tend towards infinity,
which is written
```
 n
A= f (xi∗ )Δxi . (19.12)
i=1

```

The right-hand side of (19.12) is called a Riemann sum, of which there are many.
For the above description, I have assumed that the sub-intervals are equal, which is
not a necessary requirement.
If the number of sub-intervals is n, then

```
b−a
Δx =
n
```


<a id='p541'></a>
<!-- Página 541 -->

19.10 The Riemann Sum 529

and the definite integral is defined as
```
 b 
n
f (x) d x = lim f (xi∗ )Δxi .
a n→∞
i=1




```

19.11 Summary

In this chapter we have discovered the double role of integration. Integrating a function reveals another function, whose derivative is the function under investigation.
Simultaneously, integrating a function computes the area between the function’s
graph and the x- or y-axis. Although the concept of area in every-day life is an
unsigned quantity, within mathematics, and in particular calculus, area is a signed
quality, and one must be careful when making such calculations.

<a id='p542'></a>
<!-- Página 542 -->


## Chapter 20

Worked Examples




20.1 Introduction

This chapter examines a variety of problems encountered in computer graphics and
develops mathematical strategies for their solution. Such strategies may not be the
most efficient, however, they will provide the reader with a starting point, which may
be improved upon.



20.2 Area of Regular Polygon

Given a regular polygon with n sides, side length s, and radius r of the circumscribed
circle, its area can be computed by dividing it into n isosceles triangles and summing
their total area.
Figure 20.1 shows one of the isosceles triangles O AB formed by an edge s and
the centre O of the polygon. From Fig. 20.1 we observe that
```
s π 
= tan
2h n
```

therefore,
```
s π 
h= cot
2 n
sh s2 π 
area(ΔO AB) = = cot
2 4 n
```

but there are n such triangles, therefore,




© Springer-Verlag London Ltd., part of Springer Nature 2022 531
J. Vince, Mathematics for Computer Graphics, Undergraduate Topics
in Computer Science, https://doi.org/10.1007/978-1-4471-7520-9_20

<a id='p543'></a>
<!-- Página 543 -->

532 20 Worked Examples

Fig. 20.1 One of the O
isosceles triangles forming a
regular polygon
```
π
n



h r


s s
2 2
A s B
```

Table 20.1 Area of first 6 n Area
regular polygons
```
3 0.433
4 1
5 1.72
6 2.598
7 3.634
8 4.828




ns 2 π 
area = cot .
4 n
```

Table 20.1 shows the area for the first six regular polygons with s = 1.



20.3 Area of Any Polygon

Figure 20.2 shows a polygon with the following vertices in anticlockwise sequence,
and by inspection, the area is 9.5.

```
x 0 2 5 4 2
y 2 0 1 3 3

```

The area of a polygon is given by

```

n−1
ar ea = 21 (xi yi+1(mod n) − yi xi+1(mod n) )
i=0
= 2 (0 × 0 + 2 × 1 + 5 × 3 + 4 × 3 + 2 × 2 − 2 × 2
1

− 0 × 5 − 1 × 4 − 3 × 2 − 3 × 0)
ar ea = 21 (33 − 14) = 9.5.
```


<a id='p544'></a>
<!-- Página 544 -->

20.4 Dihedral Angle of a Dodecahedron 533

Fig. 20.2 A five-sided Y
irregular polygon 4


```
3


2
area = 9.5
1



```


## 1 2 3 4 5 X



20.4 Dihedral Angle of a Dodecahedron

The dodecahedron is a member of the five Platonic solids, which are constructed from
regular polygons. The dihedral angle is the internal angle between two touching faces.
Figure 20.3 shows a dodecahedron with one of its pentagonal sides.
Figure 20.4 illustrates the geometry required to fold two pentagonal sides through
the dihedral angle γ .
The point P has coordinates

```
P(x, y, z) = (sin 72◦ , 0, − cos 72◦ )


```

Fig. 20.3 A dodecahedron
with one of its pentagonal
sides


```
72◦
108◦ 108◦




```

Fig. 20.4 The dihedral Y
angle γ between two
pentagonal sides



## P

```
v2
γ P
v1
```


## Z X


<a id='p545'></a>
<!-- Página 545 -->

534 20 Worked Examples

and for simplicity, we will use a unit vector to represent an edge, therefore

```
v1  = v2  = 1.

```

The coordinates of the rotated point P  are given by the following transform:
```
⎡ ⎤ ⎡ ⎤⎡ ⎤
x cos γ − sin γ 0 sin 72◦
⎣ y  ⎦ = ⎣ sin γ cos γ 0 ⎦ ⎣ 0 ⎦
z 0 0 1 − cos 72◦

```

where

```
x  = cos γ sin 72◦
y  = sin γ sin 72◦
z  = − cos 72◦ .

```

But
```
v1 · v2 = v1 v2  cos θ = x x  + yy  + zz 

```

therefore,
```
cos θ = cos γ sin2 72◦ + cos2 72◦

```

but θ = 108◦ (internal angle of a regular pentagon), therefore,

```
cos 108◦ − cos2 72◦ cos 72◦
cos γ = = .
sin2 72◦ cos 72◦ − 1

```

The dihedral angle γ ≈ 116.56505◦ .
A similar technique can be used to calculate the dihedral angles of the other
Platonic objects.



20.5 Vector Normal to a Triangle

Very often in computer graphics we have to calculate a vector normal to a plane
containing three points. The most effective tool to achieve this is the vector product.
For example, given three points P1 (5, 0, 0), P2 (0, 0, 5) and P3 (10, 0, 5), we can
create two vectors a and b as follows:
```
⎡ ⎤ ⎡ ⎤
x2 − x1 x3 − x1
a = ⎣ y2 − y1 ⎦ , b = ⎣ y3 − y1 ⎦ ,
z2 − z1 z3 − z1
```


<a id='p546'></a>
<!-- Página 546 -->

20.5 Vector Normal to a Triangle 535

therefore,
```
a = −5i + 5k, b = 5i + 5k.

```

The normal vector n is given by

```
ijk
n = a × b = −5 0 5 = 50j.
505



```

20.6 Area of a Triangle Using Vectors

The vector product is also useful in calculating the area of a triangle using two of
its sides as vectors. For example, using the same points and vectors in the previous
example:
```
ijk
ar ea = 21 a × b = 21 −5 0 5 = 21 50j = 25.
505



```

20.7 General Form of the Line Equation from Two Points

The general form of the line equation is given by

```
ax + by + c = 0

```

and it may be required to compute this equation from two known points. For example,
Fig. 20.5 shows two points P1 (x1 , y1 ) and P2 (x2 , y2 ), from which it is possible to
determine P(x, y).


Fig. 20.5 A line formed Y
```
from two points P1 and P2
```


## P2

```
y2
```


## P

```
y
y1 P1




x1 x x2 X
```


<a id='p547'></a>
<!-- Página 547 -->

536 20 Worked Examples

From Fig. 20.5

```
y2 − y1 y − y1
=
x2 − x1 x − x1
(y2 − y1 )(x − x1 ) = (x2 − x1 )(y − y1 )
(y2 − y1 )x − (y2 − y1 )x1 = (x2 − x1 )y − (x2 − x1 )y1
(y2 − y1 )x + (x1 − x2 )y = x1 y2 − x2 y1

```

therefore,
```
a = y2 − y1 b = x1 − x2 c = −(x1 y2 − x2 y1 ).

```

If the two points are P1 (1, 0) and P2 (3, 4), then

```
(4 − 0)x + (1 − 3)y − (1 × 4 − 3 × 0) = 0

```

and
```
4x − 2y − 4 = 0.



```

20.8 Angle Between Two Straight Lines

Given two line equations it is possible to compute the angle between the lines using
the scalar product. For example, if the line equations are

```
a1 x + b1 y + c1 = 0
a2 x + b2 y + c2 = 0

```

their normal vectors are n = a1 i + b1 j and m = a2 i + b2 j respectively, therefore,

```
n · m = nm cos α

```

and the angle between the lines α is given by

```
n·m
α = cos−1 .
nm

```

Figure 20.6 shows two lines with equations

```
2x + 2y − 4 = 0
2x + 4y − 4 = 0
```


<a id='p548'></a>
<!-- Página 548 -->

20.8 Angle Between Two Straight Lines 537

Fig. 20.6 Two lines Y
intersecting at an angle α 2


```
1



```


## 0 1 2 3 4 5 X

```
−1 α

−2




```

therefore,
```
2×2+2×4
α = cos−1 √ √ ≈ 18.435◦ .
2 2 + 2 2 2 2 + 42



```

20.9 Test if Three Points Lie on a Straight Line

Figure 20.7 shows three points P1 , P2 and P3 which lie on a straight line. There are
all sorts of ways to detect such a condition. For example, we could assume that the
points are the vertices of a triangle, and if the triangle’s area is zero, then the points
lie on a line. Here is another approach.
```
−−→ −−→
Given P1 (x1 , y1 ), P2 (x2 , y2 ), P3 (x3 , y3 ) and r = P1 P2 and s = P1 P3 , the three
```

points lie on a straight line when s = λr where λ is a scalar.
```
Let the points be

```


## P1 (0, −2), P2 (1, −1), P3 (4, 2)





Fig. 20.7 Three points on a Y
common line 2

## P3

```
1



```


## 0 1 2 3 4 5 X

```
−1
```


## P2

```
−2
```


## P1


<a id='p549'></a>
<!-- Página 549 -->

538 20 Worked Examples

then
```
r = i + j, and s = 4i + 4j

```

and
```
s = 4r

```

therefore, the points lie on a straight line as confirmed by the diagram.
Another way is to compute

```
x1 y1 1 0 −2 1
x2 y2 1 = 1 −1 1 = 0
x3 y3 1 4 21

```

which is twice the area of ΔP1 P2 P3 , and as this equals zero, the points must be
co-linear.



20.10 Position and Distance of the Nearest Point on a Line
```
to a Point

```

Suppose we have a line and some arbitrary point P, and we require to find the
nearest point on the line to P. Vector analysis provides a very elegant way to solve
such problems. Figure 20.8 shows a line and a point P and the nearest point Q
on the line. The nature of the geometry is such that the line connecting P to Q is
perpendicular to the reference line, which is exploited in the analysis. The objective
is to determine the position vector q.
```
We start with the line equation

ax + by + c = 0

```

and declare Q(x, y) as the nearest point on the line to P.


Fig. 20.8 Q is the nearest Y
point on the line to P
```
n

```


## Q



```
r
q
```


## P

```
p
```


## X


<a id='p550'></a>
<!-- Página 550 -->

20.10 Position and Distance of the Nearest Point on a Line to a Point 539

The normal to the line must be

```
n = ai + bj

```

and the position vector for Q is

```
q = xi + yj.

```

Therefore,
```
n · q = −c. (20.1)

```

r is parallel to n, therefore,
```
r = λn (20.2)

```

where λ is some scalar.
Taking the scalar product of (20.2)

```
n · r = λn · n (20.3)

```

but as

```
r =q−p (20.4)
n · r = n · q − n · p. (20.5)

```

Substituting (20.1) and (20.3) in (20.5) we obtain

```
λn · n = −c − n · p

```

therefore,
```
−(n · p + c)
λ= .
n·n
```

From (20.4) we get
```
q = p + r. (20.6)

```

Substituting (20.2) in (20.6) we obtain the position vector for Q:

```
q = p + λn.

```

The distance P Q must be the magnitude of r:

```
P Q = r = λn.

```

Let’s test this result with an example where the answer can be predicted.

<a id='p551'></a>
<!-- Página 551 -->

540 20 Worked Examples

Fig. 20.9 Q is the nearest Y
point on the line to P P
```
1 n




```


## Q






## 1 X



Figure 20.9 shows a line whose equation is x + y − 1 = 0, and the associated
point is P(1, 1). By inspection, the nearest point is Q 21 , 21 and the distance P Q ≈
0.7071.
From the line equation

```
a = 1, b = 1, c = −1

```

therefore,
```
2−1
λ=− = − 21
2
```

and

```
x Q = x P + λxn = 1 − 21 × 1 = 21
y Q = y P + λyn = 1 − 21 × 1 = 21 .

```

The nearest point is Q ,
```
1 1
2 2
and the distance is

P Q = λn = 21 i + j ≈ 0.7071.



```

20.11 Position of a Point Reflected in a Line

Suppose that instead of finding the nearest point on a line we require the reflection
Q of P in the line. Once more, we set out to discover the position vector for Q.
Figure 20.10 shows the vectors used in the analysis. We start with the line equation

```
ax + by + c = 0
```


<a id='p552'></a>
<!-- Página 552 -->

20.11 Position of a Point Reflected in a Line 541

Fig. 20.10 The vectors n
required to find the reflection Y
of P in the line r P

## T



```
r+r
t
p r


```


## Q

```
q
```


## X



and declare T (x, y) as the nearest point on the line to O with t = xi + yj as its
position vector.
From the line equation
```
n = ai + bj

```

therefore,
```
n · t = −c. (20.7)

```

We note that r + r is orthogonal to n, therefore,

```
n · (r + r ) = 0

```

and
```
n · r + n · r = 0. (20.8)

```

We also note that p − q is parallel to n, therefore,

```
p − q = r − r = λn

```

where λ is some scalar, therefore,

```
r − r
λ= . (20.9)
n
```

From the figure we note that
```
r = p − t. (20.10)

```

Substituting (20.7) in (20.10)

```
n · r = n · p − n · t = n · p + c. (20.11)
```


<a id='p553'></a>
<!-- Página 553 -->

542 20 Worked Examples

Fig. 20.11 Q is the Y
reflection of P in the line P
```
1




```


## Q


## 1 X



Substituting (20.8) and (20.11) in (20.9)

```
n · r − n · r 2n · r
λ= =
n·n n·n
2(n · p + c)
λ=
n·n
```

and the position vector is
```
q = p − λn.

```

Let’s again test this formula with a scenario that can be predicted in advance.
Given the line equation
```
x +y−1=0

```

and the point P(1, 1), the reflection must be the origin, as shown in Fig. 20.11.
Now let’s confirm this prediction. From the line equation

```
a = 1, b = 1, c = −1

```

and

```
xP = 1
yP = 1
2 × (2 − 1)
λ= =1
2
```

therefore,

```
x Q = x P − λxn = 1 − 1 × 1 = 0
y Q = y P − λyn = 1 − 1 × 1 = 0

```

and the reflection point is Q(0, 0).

<a id='p554'></a>
<!-- Página 554 -->

20.12 Intersection of a Line and a Sphere 543

20.12 Intersection of a Line and a Sphere

In ray tracing and ray casting it is necessary to detect whether a ray (line) intersects
objects within a scene. Such objects may be polygonal, constructed from patches,
or defined by equations. In this example, we explore the intersection between a line
and a sphere.
```
There are three possible scenarios: the line intersects, touches or misses the sphere.
```

It just so happens, that the cosine rule proves very useful in setting up a geometric
condition that identifies the above scenarios, which are readily solved using vector
analysis.
```
Figure 20.12 shows a sphere with radius r located at C. The line is represented
```

parametrically, which lends itself to this analysis. The objective is to discover whether
there are points in space that satisfy both the line equation and the sphere equation.
If there is a point, a position vector will locate it.
```
The position vector for C is

c = xc i + yc j + z c k

```

and the equation of the line is
```
p = t + λv

```

where λ is a scalar, and
```
v = 1. (20.12)

```

For an intersection at P

```
q = r
q2 = r 2
q2 − r 2 = 0.




```

Fig. 20.12 The vectors
required to locate a possible v
intersection r
```
P q C
c Y

λv s p

T t
```


## Z X


<a id='p555'></a>
<!-- Página 555 -->

544 20 Worked Examples

Using the cosine rule

```
q2 = λv2 + s2 − 2λvs cos θ (20.13)
q = λ v + s − 2vsλ cos θ.
2 2 2 2
(20.14)

```

Substituting (20.12) in (20.14)

```
q2 = λ2 + s2 − 2sλ cos θ. (20.15)

```

Now let’s identify cos θ :
```
s · v = sv cos θ

```

therefore,
```
s·v
cos θ = . (20.16)
s

```

Substituting (20.16) in (20.15)

```
q2 = λ2 − 2s · vλ + s2

```

therefore,
```
q2 − r 2 = λ2 − 2s · vλ + s2 − r 2 = 0. (20.17)

```

Equation (20.17) is a quadratic in λ where
```

λ=s·v± (s · v)2 − s2 + r 2 (20.18)

```

and
```
s = c − t.

```

The discriminant of (20.18) determines whether the line intersects, touches or misses
the sphere.
The position vector for P is given by

```
p = t + λv

```

where 
```
λ=s·v± (s · v)2 − s2 + r 2

```

and
```
s = c − t.

```

For a miss condition
```
(s · v)2 − s2 + r 2 < 0.
```


<a id='p556'></a>
<!-- Página 556 -->

20.12 Intersection of a Line and a Sphere 545

Fig. 20.13 Three lines that Y
miss, touch and intersect the λv2
sphere λv3 P3

```
r
```


## C

```
P2 λv1

c
```


## P3


## T

```
t X
```


## Z L1 L2 L3




For a touch condition
```
(s · v)2 − s2 + r 2 = 0.

```

For an intersect condition

```
(s · v)2 − s2 + r 2 > 0.

```

To test these formulae we will create all three scenarios and show that the equations
are well behaved.
Figure 20.13 shows a sphere with three lines represented by their direction vectors
λv1 , λv2 and λv3 . The sphere has radius r = 1 and is located at C with position vector

```
c =i+j

```

whilst the three lines L 1 , L 2 and L 3 miss, touch and intersect the sphere respectively.
The lines are of the form
```
p = t + λv

```

therefore,

```
p1 = t1 + λv1
p2 = t2 + λv2
p3 = t3 + λv3

```

where,

```
t1 = 2i, v1 = √12 i + √12 j
t2 = 2i, v2 = j
t3 = 2i, v3 = − √12 i + √12 j
```


<a id='p557'></a>
<!-- Página 557 -->

546 20 Worked Examples

and
```
c = i + j.

```

Let’s substitute the lines in the original equations:

## L 1:


```
s = −i + j
(s · v) − s + r = 0 − 2 + 1 = −1
2 2 2



```

the negative discriminant confirms a miss condition.

## L 2:


```
s = −i + j
(s · v) − s + r = 1 − 2 + 1 = 0
2 2 2



```

the zero discriminant confirms a touch condition, therefore λ = 1 and the touch point
is P2 (2, 1, 0) which is correct.

## L 3:


```
s = −i + j
(s · v) − s + r = 2 − 2 + 1 = 1
2 2 2



```

the positive discriminant confirms an intersect condition, therefore,
```
√ √
λ = √22 ± 1 = 1 + 2 or 2 − 1.

```

The intersection√points are given by the two values of λ:
When λ = 1 + 2
```
 √  
x P = 2 + 1 + 2 − √12 = 1 − √12
 √ 
y P = 0 + 1 + 2 √12 = 1 + √12
z P = 0.
√
```

When λ = 2−1
```
√  
xP = 1 + 2 − 1 − √12 = 1 + √12
√ 
yP = 0 + 2 − 1 √12 = 1 − √12
z P = 0.
```


<a id='p558'></a>
<!-- Página 558 -->

20.12 Intersection of a Line and a Sphere 547

The intersection points are
```
 
```


## P3 1 − √12 , 1 + √12 , 0

```
 
```


## P3 1 + √12 , 1 − √12 , 0


which are correct.



20.13 Sphere Touching a Plane

A sphere will touch a plane if the perpendicular distance from its centre to the plane
equals its radius. The geometry describing this condition is identical to finding the
position and distance of the nearest point on a plane to a point.
Figure 20.14 shows a sphere located at P with position vector p. A potential touch
condition occurs at Q, and the objective of the analysis is to discover its position
vector q. Given the following plane equation

```
ax + by + cz + d = 0

```

its surface normal is
```
n = ai + bj + ck.

```

The nearest point Q on the plane to a point P is given by the position vector

```
q = p + λn (20.19)

```

where
```
n·p+d
λ=−
n·n




```

Fig. 20.14 The vectors used Y
to detect when a sphere
touches a plane n

## P


```
p
```


## Q

```
q


```


## Z X


<a id='p559'></a>
<!-- Página 559 -->

548 20 Worked Examples

Fig. 20.15 A sphere Y
touching a plane n

## Q


```
P r



```


## Z X



the distance
```
P Q = λn.

```

If P is the centre of the sphere with radius r , and position vector p, the touch point
is also given by (20.19) when

```
P Q = λn = r.

```

Let’s test the above equations with a simple example, as shown in Fig. 20.15,
which shows a sphere with radius r = 1 and centred at P(1, 1, 1).
The plane equation is
```
y−2=0

```

therefore,
```
n=j

```

and
```
p=i+j+k

```

therefore,
```
λ = −(1 − 2) = 1

```

which equals the sphere’s radius and therefore the sphere and plane touch. The touch
point is

```
xQ = 1 + 1 × 0 = 1
yQ = 1 + 1 × 1 = 2
zQ = 1 + 1 × 0 = 1
```


## Q = (1, 2, 1).


<a id='p560'></a>
<!-- Página 560 -->

20.14 Summary 549

20.14 Summary

Unfortunately, problem solving is not always obvious, and it is possible to waste
hours of analysis simply because the objective of the solution has not been well
formulated. Hopefully, though, the reader has discovered some of the strategies used
in solving the above geometric problems, and will be able to implement them in
other scenarios. At the end of the day, practice makes perfect!

<a id='p561'></a>
<!-- Página 561 -->

Appendix A
Limit of (sin θ)/θ




This appendix proves that

```
sin θ
lim = 1, where θ is in radians.
θ→0 θ

```

From high-school mathematics we know that sin θ ≈ θ , for small values of θ . For
example:

```
sin 0.1 = 0.099833
sin 0.05 = 0.04998
sin 0.01 = 0.0099998

```

and
```
sin 0.1
= 0.99833
0.1
sin 0.05
= 0.99958
0.05
sin 0.01
= 0.99998.
0.01
```

Therefore, we can reason that in the limit, as θ → 0:

```
sin θ
lim = 1.
θ→0 θ


```

Figure A.1 shows a graph of (sin θ )/θ , which confirms this result. However, this is
an observation, rather than a proof. So, let’s pursue a geometric line of reasoning.
From Fig. A.2 we see as the circle’s radius is unity, O A = O B = 1, and
AC = tan θ . As part of the strategy, we need to calculate the area of the triangle
O AB, the sector O AB and the O AC:
© Springer-Verlag London Ltd., part of Springer Nature 2022 551
J. Vince, Mathematics for Computer Graphics, Undergraduate Topics
in Computer Science, https://doi.org/10.1007/978-1-4471-7520-9

<a id='p562'></a>
<!-- Página 562 -->

552 Appendix A

Fig. A.1 Graph of (sin θ)/θ
```
1




-3 -2 - 0 2 3




-1




```

Fig. A.2 Unit radius circle y C
with trigonometric ratios

## B

```
tan
1
sin

O cos D A x




area(O AB) = area(O D B) + area(D AB)
= 21 cos θ sin θ + 21 (1 − cos θ ) sin θ
= 21 cos θ sin θ + 21 sin θ − 21 cos θ sin θ
= 21 sin θ.
θ
area of sector O AB = π(1)2 = 21 θ.
2π
area(O AC) = 21 (1) tan θ = 21 tan θ.

```

From the geometry of a circle, we know that
```
1
2
sin θ < 21 θ < 21 tan θ
sin θ
sin θ < θ <
cos θ
θ 1
1< <
sin θ cos θ
sin θ
1> > cos θ
θ
```


<a id='p563'></a>
<!-- Página 563 -->

Appendix A 553

```
sin θ
```

and as θ → 0, cos θ → 1 and → 1. This holds, even for negative values of θ ,
```
θ
```

because
```
sin(−θ ) − sin θ sin θ
= = .
−θ −θ θ

```

Therefore,
```
sin θ
lim = 1.
θ→0 θ
```


<a id='p564'></a>
<!-- Página 564 -->

Appendix B
Integrating cosn θ




We start with  
```
cos x d x =
n
cos x cosn−1 x d x.

```

Let u = cosn−1 x and v  = cos x, then

```
u  = −(n − 1) cosn−2 x sin x

```

and
```
v = sin x.

```

Integrating by parts:
```
 
uv  d x = uv −
v u d x + C
```

 
```
cosn−1 x cos x d x = cosn−1 x sin x + sin x (n − 1) cosn−2 x sin x d x + C

= sin x cosn−1 x + (n − 1) sin2 x cosn−2 x d x + C

= sin x cosn−1 x + (n − 1) (1 − cos2 x) cosn−2 x d x + C
 
= sin x cosn−1 x + (n − 1) cosn−2 d x − (n − 1) cosn x d x + C
 
n cosn x d x = sin x cosn−1 x + (n − 1) cosn−2 d x + C
 
sin x cosn−1 x n−1
cosn x d x = + cosn−2 d x + C
n n

```

where n is an integer, = 0.
Similarly,
```
 
cos x sinn−1 x n−1
sinn x d x = − + sinn−2 d x + C.
n n
```

© Springer-Verlag London Ltd., part of Springer Nature 2022 555
J. Vince, Mathematics for Computer Graphics, Undergraduate Topics
in Computer Science, https://doi.org/10.1007/978-1-4471-7520-9

<a id='p565'></a>
<!-- Página 565 -->

556 Appendix B

For example, 
```
sin x cos2 x
cos3 x d x = + 23 sin x + C.
3
```


<a id='p566'></a>
<!-- Página 566 -->

Index




A Areal coordinates, 185
Adding Argand, Jean-Robert, 95
complex numbers, 152 Associative law, 10
matrices, 165 Atan2, 57
ordered pairs, 158 Axial vector, 243
quaternions, 241, 256 Axioms, 10, 412
Additive form of a quaternion, 245
Aitken, Alexander, 314
Aleph-zero, 27 B
Algebra, 31 Babylonians, 77
Algebraic number, 20, 26 Back-face detection, 106
Altmann, Simon, 238, 243, 269 Barycentric coordinates, 185, 371
Analytic geometry, 325 Base, 11
Angle Bernstein polynomials, 303
compound, 60 Bézier
Angle between curves, 301, 398
a line and plane, 366 matrix, 311
two planes, 365 Bézier, Pierre, 301
two straight lines, 536 Binary
Annulus, 333 addition, 16
Anticlockwise, 67 negative number, 18
Antiderivative, 445 number, 13
Antisymmetric operation, 10
functions, 402 subtraction, 18
matrix, 128 Binary form of a quaternion, 245
Area, 113 Binomial expansion, 304, 442
between two functions, 523 Bivector, 408
circle, 514 Blending
negative, 521 curve, 308
of any polygon, 532 function, 312
of a regular polygon, 531 Brahmagupta, 7
of a shape, 67 B-splines, 315
of a triangle, 341, 387, 535 Bürgi, Joost, 38
parametric function, 525
positive, 521
under a graph, 512 C
with the y-axis, 524 Calculus, 437
© Springer-Verlag London Ltd., part of Springer Nature 2022 557
J. Vince, Mathematics for Computer Graphics, Undergraduate Topics
in Computer Science, https://doi.org/10.1007/978-1-4471-7520-9

<a id='p567'></a>
<!-- Página 567 -->

558 Index

Camera space, 206 subtraction, 152
Cantor, Georg, 2, 27 Compound angles, 60
Cardano, Girolamo, 77 Continuity, 317, 437
Cardinality, 27 Continuous functions, 492
Cartesian Control
```
coordinates, 65, 66 point, 307, 315
plane, 66 vertex, 307
vector, 103 Convex hull, 307, 387
```

Casteljau, Paul de, 301 Coordinates
Cauchy, Augustin-Louis, 77, 79, 437 barycentric, 371
Cayley, Arthur, 77, 119, 261, 269 Cartesian, 65
Cayley numbers, 255, 261 cylindrical, 72
Centre of gravity, 328 polar, 70
Centroid, 374 spherical polar, 71
Ceva, Giovanni, 372 Cosecant, 54
Ceva’s Theorem, 372 Cosine, 54
Chain rule, 486 rule, 59, 430
Change of axes, 202 Cotangent, 54
```
2D, 202 Counting, 5
3D, 205 Cross product, 107
```

Circle, 332 Cubic
```
equation, 302 Bernstein polynomials, 307
```

Clifford, William Kingdon, 96, 401 Bézier surface patch, 322
Clockwise, 67 equation, 440
Closed interval, 42 function, 66
Cofactor expansion, 140 interpolant, 308
Column vector, 96, 120, 123, 131, 184 interpolation, 289
Commutative law, 10 Curves and patches, 301
Complex Cylindrical coordinates, 72
```
number, 24, 151
plane, 22
```

Complex conjugate, 25 D
```
complex number, 154 Decimal
quaternion, 246 number, 12
```

Complex number system, 7
```
absolute value, 154 Definite integral, 516
adding matrix, 165 Degree, 51
addition, 152 De Moivre’s Formula, 62
complex conjugate, 154 Dependent variable, 41
conjugate matrix, 167 Derivative, 437, 445
definition, 151 graphical interpretation, 444
inverse, 156 partial, 480
inverse matrix, 167 total, 488
matrix, 164 Descartes, René, 21, 32, 65
modulus, 154 Determinant, 77, 125, 220
norm, 154, 166 complex, 92
ordered pair, 158 expansion, 92
product, 153 order, 89
product matrix, 166 property, 91
quotient, 155 second-order, 79
quotient matrix, 168 third-order, 82, 88
square, 154 value, 89
subtracting matrix, 165 Diagonal matrix, 142
```


<a id='p568'></a>
<!-- Página 568 -->

Index 559

Differential, 445 angles, 208
Differentiating, 448 rotations, 196
arccos function, 470 Euler, Leonhard, 40, 62
arccot function, 471 Even function, 44
arccsc function, 471 Explicit equation, 40
arcsec function, 471 Exterior angle, 327
arcsin function, 470
arctan function, 470
cosh function, 474 F
cot function, 470 Fermat, Pierre de, 65
csc function, 468 Feynman, Richard, 243
exponential functions, 463 Frobenius, Ferdinand Georg, 255
```
function of a function, 450 Function, 40, 442
function products, 454 continuous, 492
function quotients, 458 cubic, 66, 440
```

hyperbolic functions, 472 domain, 43
implicit functions, 460 even, 44
logarithmic functions, 465 graph, 66
partial, 481 linear, 66
sec function, 469 notation, 41
sine function, 451 odd, 44
sinh function, 474 power, 46
sums of functions, 448 quadratic, 66, 439
tan function, 467 range, 43
tanh function, 474 second derivative, 479
trigonometric functions, 467 trigonometric, 66
Dihedral angle of a dodecahedron, 533 Function of a function
Dirac, Paul, 3 differentiating, 450
Direction cosines Fundamental theorem of calculus, 517

## 2D, 204


## 3D, 206


## G

Distance
```
Gauss, Johann, 77, 79, 119
```

between two 2D points, 68
```
General form of a line equation, 535
```

between two 3D points, 69
```
Geometric
```

Distributive law, 11
```
algebra, 401
```

Division algebra, 255
```
continuity, 317
```

Dodecahedron, 533
```
product in 2D, 407
```

Domain, 43, 55 product in 3D, 409
Dot product, 104 transform, 181
Double angle, 268, 269 Gibbs, Josiah Willard, 96, 236
Double-angle identities, 61 Gimbal lock, 199
Duality, 419 Gödel, Kurt, 32
```
Golden section, 327
Grades, 413
```

E Grassmann, Hermann Günther, 96, 236
Element, 6 Graves, John Thomas, 261
Ellipse equation, 302
Equation
```
explicit, 40 H
implicit, 40 Half-angle identities, 63
linear, 78, 81 Half-open interval, 42
```

Equilateral triangle, 329 Hamilton’s rules, 233, 421
Euler Hamilton, William Rowan, 95, 108, 269

<a id='p569'></a>
<!-- Página 569 -->

560 Index

Hermite, Charles, 293 vectors, 294
Hermite interpolation, 293 Interpolation, 285
Hessian normal form, 335, 343 cubic, 289
Hestenes, David, 401 linear, 286, 380
Hexadecimal number, 13 non-linear, 288
Higher derivatives, 475 trigonometric, 288
Homogeneous coordinates, 184 Intersecting
```
circle and line, 345
line and sphere, 543
```

I line segments, 339
Identity matrix, 191 planes, 359
Image space, 206 straight lines, 338, 348
Imaginary number, 21 Interval, 42
Implicit equation, 40 closed, 42
Indefinite integral, 491 half-open, 42
Independent variable, 41 open, 42
Indeterminate form, 8 Inverse
Indices, 37 complex number, 156
```
laws of, 38 matrix, 134
```

Infinitesimals, 437 of a vector, 415
Infinity, 27 quaternion, 252, 258
```
trigonometric function, 56
```

Inner product, 405, 415
```
Irrational number, 20
```

Integer, 19
```
Isosceles triangle, 328
number, 6
```

Integral
```
definite, 516
```


## K

```
indefinite, 491
Kronecker, Leopold, 2, 19
```

Integrating, 445
```
arccos function, 470
arccot function, 471 L
arccsc function, 471 Lambert’s law, 105
arcsec function, 471 Laplace expansion, 89
arcsin function, 470 Laplace, Pierre-Simon, 77, 89, 140
arctan function, 470 Laplacian expansion, 140
by parts, 501 Left-handed axes, 69
by substitution, 505 Leibniz, Gottfried von, 40, 77
completing the square, 497 Lerp, 381
cot function, 470 L’Hôpital, Guillaume de, 77
csc function, 468 Lighting calculations, 105
difficult functions, 493 Limits, 437, 442
exponential function, 465 Linear
integrand contains a derivative, 498 equation, 78, 81
logarithmic function, 466 function, 66
partial fractions, 510 interpolation, 286, 305, 312, 380
radicals, 495 Linearly independent, 78
sec function, 469 Lobachevsky, Nikolai, 236, 325
tan function, 467 Local coordinates, 371
techniques, 492 Logarithm, 38
trigonometric identities, 493 base, 39
```

Intercept theorems, 326
Interior angle, 327
Interpolating M
```
quaternions, 297 Mass points, 374, 391
```


<a id='p570'></a>
<!-- Página 570 -->

Index 561

Matrix, 88, 119, 184, 253 Notation, 3
addition, 130 Null matrix, 123
algebra, 119 Number
antisymmetric, 128 algebraic, 20, 26
determinant, 125 arithmetic, 9
diagonal, 142 binary, 13
dimension, 122 complex, 24
inverse, 134 hexadecimal, 13
multiplication, 121 imaginary, 21
notation, 122, 184 integer, 6, 19
null, 123 line, 8
order, 122 natural, 19
orthogonal, 141 negative, 8
products, 130 octal, 12
rectangular, 134 positive, 8
scalar multiplication, 130 rational, 6, 19, 20
singular, 135 real, 6, 20
skew-symmetric, 128 transcendental, 20, 26
square, 122, 133
subtraction, 130
symmetric, 126 O
trace, 124 Object space, 206
transpose, 125 Octal number, 12
unit, 123 Octaves, 261
Maxima, 477 Odd function, 44
Median, 328 One-to-one correspondence, 27
Member, 6 Open interval, 42
Minima, 477 Ordered pair, 158, 238, 241
Mixed partial derivative, 485 absolute value, 161
Möbius, August, 185, 371 addition, 158
Moivre, Abraham de, 62 complex conjugate, 161
Multiple-angle identities, 62 inverse, 162
Multivectors, 413 modulus, 161
```
multiplying by a scalar, 159
norm, 161
```

N product, 158, 159
Napier, John, 38 quotient, 161
Natural number, 19 square, 160
Nearest point to a line, 538 subtraction, 158
Negative number, 8 Oriented axes, 66
Non-linear interpolation, 288 Origin, 66
Non-rational B-splines, 315 Orthogonal
Non-uniform matrix, 141, 208, 254
B-splines, 318 Outer product, 405, 415
rational B-splines, 319 3D, 411
Non-Uniform Rational B-Splines (NURBS), imaginary properties, 417
```
319
```

Norm
complex number, 154, 166 P
ordered pair, 161 Parallelogram, 331
quaternion, 247, 257 Partial derivative, 480
quaternion product, 251 chain rule, 486
Normalised quaternion, 248 first, 481

<a id='p571'></a>
<!-- Página 571 -->

562 Index

```
mixed, 485 interpolating, 297
second, 482 inverse, 252, 258
visualising, 483 matrix, 253, 271
```

Pascal, Blaise, 65 norm, 247, 257
Pascal’s triangle, 303, 442 normalised, 248
Peirce, Benjamin, 119 product, 239, 241, 248, 249, 257, 261
Peirce, Charles, 119 pure, 243
Perimeter relationships, 63 square, 250, 258
Perspective projection, 222 subtraction, 241
Pitch, 197, 208 unit-norm, 248, 257
Placeholder, 7 units, 238, 239, 244
Planar surface patch, 319 Quotient
Plane equation, 351 complex number, 155
```
Cartesian form, 351 quaternion, 252
from three points, 357
general form, 353
parametric form, 354 R
```

Plücker, Julius, 185 Radian, 51, 52, 325
Poincaré, Henri, 2 Radius of the inscribed circle, 390
Point inside a triangle, 341, 385 Range, 43, 55
Point reflected in a line, 540 Rational
Polar B-splines, 315
```
coordinates, 70 coefficients, 20
vector, 243 number, 6, 19
```

Polynomial equation, 20 Ratios, 373
Position vector, 102 Real
Power number, 6, 20
```
functions, 46 quaternion, 242
series, 52 Rectangular matrix, 134
```

Product Recursive Bézier curve, 310
```
complex number, 153 Reflecting a vector, 432
pure quaternion, 249 Reflections, 422
quaternion, 248, 257 Regular polygon, 332
unit-norm quaternion, 249 Rhombus, 331
```

Pseudoscalars, 413 Riemann, Bernhard, 325, 527
Pseudovector, 243 Riemann sum, 527
Pure quaternion, 243 Right-handed axes, 69
```
product, 249 Right-hand rule, 112
Right triangle, 329
Rodrigues, Benjamin Olinde, 269
```

Q Rodrigues, Olinde, 236
Quadratic Roll, 197, 208
Bézier curve, 306 Rotating about an axis, 200, 211
Bézier surface patch, 320 Rotation, 422
equation, 33 matrix, 164
function, 66, 439 Rotors, 426
Quadrilateral, 330 Row vector, 96, 123, 131, 184
Quaternion, 233, 261, 421 Russell, Bertrand, 31
addition, 241, 256
additive form, 245
algebra, 254 S
binary form, 245 Sarrus, Pierre, 88
conjugate, 246 Sarrus’s rule, 88, 92

<a id='p572'></a>
<!-- Página 572 -->

Index 563

Scalar product, 103, 104 vector, 99
Secant, 54 Three intersecting planes, 362
Second derivative, 479 Total derivative, 488
Seki, Takakazu, 77 Trace, 124
Series Transcendental number, 20, 26
```
cosine, 52 Transform
power, 52 2D, 182
sine, 52 2D reflection, 183, 187, 193
```

Servois, François-Joseph, 236 2D rotation about a point, 194
Set, 6 2D scaling, 182, 186
```
member, 6 2D shearing, 189
```

Simultaneous equations, 93 2D translation, 182, 186
Sine, 54 3D reflection, 202
```
differentiating, 451 3D scaling, 195
rule, 58, 429
3D translation, 195
```

Singular matrix, 135
```
affine, 192
```

Skew-symmetric matrix, 128
```
Transforming vectors, 218
```

Space partitioning, 337
```
Transpose matrix, 125
```

Sphere touching a plane, 547
```
Trapezoid, 330
```

Spherical polar coordinates, 71
Square Triangle
```
complex number, 154 centre of gravity, 328
matrix, 122, 133 equilateral, 329
quaternion, 250, 258 isosceles, 328
```

Square-root of i right, 329
```
complex number, 156 Trigonometric
matrix, 169 function, 53, 66
ordered pair, 163 identities, 58
```

Straight line equation, 347 interpolation, 288
Subtracting inverse function, 56
```
complex numbers, 152 ratios, 53
matrices, 165 Trigonometry, 51
ordered pairs, 158 Trivector, 412, 413
quaternions, 241 2D
```

Surface patch, 319 analytic geometry, 334
Symmetric polygon, 67
```
functions, 402 reflections, 422
matrix, 126 rotations, 424
scaling transform, 192
vector, 96
```

T Two’s complement, 18
Tait, Peter Guthrie, 234
Tangent, 54
Thales, 326
Theorem of U
```
Pythagoras, 68, 69, 329 Uniform B-splines, 315
Thales, 329 Unit
```

3D matrix, 123
```
complex numbers, 108 normal vector, 112
coordinates, 69 quaternion, 244
reflections, 423 vector, 102
rotation transform, 196 Unit-norm
transforms, 194 quaternion, 248, 249, 257
```


<a id='p573'></a>
<!-- Página 573 -->

564 Index


## V W

Vector Warren, John, 95
2D, 96 Weierstrass, Karl, 437
3D, 99 Wessel, Caspar, 95
addition, 101 Whitehead, Alfred North, 31
Cartesian, 103 Wilson, Edwin Bidwell, 96, 236
column, 96, 120, 123, 131, 184 Wittgenstein, Ludwig, 2
interpolating, 294 Witt, Jan de, 77
magnitude, 98 World space, 206
normalising, 102
normal to a triangle, 534
position, 102 X
product, 103, 107 Xy-plane, 65
row, 96, 123, 131, 184
scaling, 100
subtraction, 101 Y
transforming, 218 Yaw, 197, 208
unit, 102
Vertices, 67
Virtual camera, 205 Z
Volume of a tetrahedron, 396 Zero, 7