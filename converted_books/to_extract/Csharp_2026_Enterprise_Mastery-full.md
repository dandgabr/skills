# C 2026 Enterprise Mastery Modern .NET Architecture, Performance, Cloud-Native APIs, AI Integration, and Production… (Victor Mihailov) (z-library.sk, 1lib.sk, z-lib.sk)

> Documento convertido de PDF para Markdown para referência de skills.


<a id='p1'></a>
<!-- Página 1 -->


## C# 2026

Enterprise Mastery
Clean Code · Peak Performance · Architecture at Scale




```
Victor Mihailov
2026 Edition
```


<a id='p2'></a>
<!-- Página 2 -->

```
C# 2026: Enterprise Mastery




C# 2026: Enterprise Mastery
Clean Code · Peak Performance · Architecture at Scale

Copyright © 2026 Victor Mihailov
All rights reserved.


```

No part of this publication may be reproduced, distributed, or transmitted in any form or
by any means, including photocopying, recording, or other electronic or mechanical
```
methods,
without the prior written permission of the author.


The code examples in this book are provided for educational purposes.
Code in the companion repository was validated against the .NET 10 SDK.
Companion source code repository:
https://github.com/MrMeHighLove/CSharp2026-Enterprise-Mastery


First Edition: 2026
Printed in the United States of America


The information in this book is distributed on an 'as is' basis, without warranty.
```

While every precaution has been taken in the preparation of this book, the author
assumes no responsibility for errors or omissions, or for damages resulting from the
```
use of the information contained herein.


Microsoft, C#, .NET, Visual Studio, and Azure are registered trademarks
of Microsoft Corporation in the United States and/or other countries.



-2-
```


<a id='p3'></a>
<!-- Página 3 -->

```
C# 2026: Enterprise Mastery




```

To every developer who woke up at 2 a.m. wondering
```
why their perfectly correct code is still wrong.
Keep building. Keep improving.




-3-
```


<a id='p4'></a>
<!-- Página 4 -->

```
C# 2026: Enterprise Mastery




About This Book
```

C# began in the early 2000s as a pragmatic answer to Java. Two decades
on, it has grown well beyond its origins. The language now offers
pattern-matching constructs borrowed from functional programming,
async primitives that other ecosystems have since imitated, and a runtime
whose throughput surprises engineers who last used .NET years ago. Yet
many teams still write code in a modern compiler that would look
unremarkable in 2012 — and closing that gap is what this book is for.

This is not a reference manual; the official documentation already does
that job well. It is an opinionated guide. When a modern feature is worth
adopting, the book explains why. When a new API introduces more
complexity than it removes, the book says so. Good engineering is
judgment applied to knowledge, and the aim here is to build both.

A note on honesty. The patterns and recommendations in this book reflect
widely held practice in the .NET community and the author's own
experience, but no book can substitute for measurement in your own
environment. Where the text makes a performance claim, treat it as a
hypothesis to verify, not a guarantee. Where it recommends an approach,
weigh it against your team's context. The book tries throughout to present
trade-offs rather than verdicts.

Whether you are new to the .NET ecosystem or an experienced architect
refreshing your toolkit, the goal is the same: that you finish a chapter and
change something about how you write code the next morning. Read it,
disagree with it where your experience differs, and use the companion
repository to run the examples for yourself.




```
-4-
```


<a id='p5'></a>
<!-- Página 5 -->

```
C# 2026: Enterprise Mastery




Preface
```

Why write another C# book? Because the C# ecosystem in 2026 barely
resembles what is described in the books that dominate most developers'
shelves. Primary constructors, collection expressions, Span<T>,
HybridCache, native AOT, .NET Aspire, the System.Threading.Lock type,
and a dramatically leaner minimal-API stack are not incremental
upgrades. They represent a different way of writing the language. This
book is the manual for that new reality.

I wrote this for the developer who knows C# but wants to know it deeply.
For the tech lead responsible for a high-traffic system that cannot afford a
bad architectural decision. For the engineer who suspects there is a better
way to solve the problem they are looking at right now. For the team that
wants to move fast without accumulating the kind of technical debt that
eventually brings a product to its knees.

The code in these pages is illustrative and written to communicate ideas
clearly. Some snippets are deliberately abbreviated to focus on the concept
under discussion. Complete, validated implementations — tested against
the .NET 10 SDK — live in the companion repository:
https://github.com/MrMeHighLove/CSharp2026-Enterprise-Mastery

The repository is organised by chapter. Each directory contains
production-quality code—not toy snippets—so you can study, fork, and
adapt it directly into your own projects.

How to use this book:

Parts I through III build the foundation: language mastery, clean-code
discipline, and performance fundamentals that underpin everything else.
Parts IV and V address the realities of enterprise architecture: distributed
systems, caching, testing, observability, and security. Part VI looks at the
horizon: AI integration, cloud-native patterns, and an honest evaluation
of which 2026-era features are worth your attention and which are
engineering theatre. Part VII closes the loop with refactoring strategies
and a catalogue of the anti-patterns that quietly destroy software projects.

```
-5-
```


<a id='p6'></a>
<!-- Página 6 -->

```
C# 2026: Enterprise Mastery


```

You do not need to read every chapter in order. If your team is struggling
with throughput, jump to Part III. If you are about to start a greenfield
microservices project, begin with Part IV. Each chapter is designed to
stand on its own while rewarding readers who make it all the way
through.

Thank you for picking up this book. Now open your IDE and let's write
some great code.

```
— Victor Mihailov
2026




-6-
```


<a id='p7'></a>
<!-- Página 7 -->

```
C# 2026: Enterprise Mastery



Table of Contents


```


## PART I — THE C# 2026 LANDSCAPE

1 C# in 2026: State of the Language.................................
2 C# 14 and .NET 10: What Actually Matters................




## PART II — WRITING CODE THAT ENDURES

3 Clean Code in Modern C#................................................
4 SOLID Principles in Practice...........................................
5 Design Patterns That Still Matter.................................
6 Domain-Driven Design with C#.....................................




## PART III — PERFORMANCE AT EVERY LEVEL

7 Memory Management and GC Deep Dive..................
8 Span<T>, Memory<T>, Zero-Allocation.....................
9 Async/Await Mastery and Concurrency....................
10 LINQ: Master It, Then Know When to Stop..............




## PART IV — ENTERPRISE PATTERNS AND ARCHITECTURE

11 Minimal APIs and High-Performance Web..............
12 gRPC, SignalR, and Real-Time.......................................
13 EF Core Enterprise Patterns...........................................
14 Caching Strategies for High-Traffic Systems............
15 Message Queues and Event-Driven Architecture...
16 Microservices Architecture............................................
17 Dependency Injection at Enterprise Scale.................

```
-7-
```


<a id='p8'></a>
<!-- Página 8 -->

```
C# 2026: Enterprise Mastery




```


## PART V — OBSERVABILITY, TESTING, AND SECURITY

18 Testing Strategies...............................................................
19 Observability: Logging, Tracing, Metrics...................
20 Security Best Practices.....................................................




## PART VI — THE 2026 FRONTIER

21 AI Integration in C# 2026................................................
22 Cloud-Native C# with .NET Aspire..............................
23 C# 2026 Features: What Makes Sense........................




## PART VII — TRANSFORMATION AND WISDOM

24 Refactoring Legacy C# Code..........................................
25 Anti-Patterns: The Hall of Shame................................




## APPENDICES

A C# Version History Quick Reference..................................
B Performance Benchmarks Reference.................................
C Recommended Tools and Libraries 2026..........................




```
-8-
```


<a id='p9'></a>
<!-- Página 9 -->

```
C# 2026: Enterprise Mastery




```

-9-

<a id='p10'></a>
<!-- Página 10 -->

```
C# 2026: Enterprise Mastery


```


## PART I — THE C# 2026 LANDSCAPE


## CHAPTER 1




```
C# in 2026: The State of the
Language

```

"A language that does not affect the way you think about programming is
```
not worth knowing." — Alan Perlis


```

The Quiet Revolution
When Microsoft open-sourced .NET in late 2014 and shipped .NET Core 1.0
in 2016, many industry observers predicted that C# would fade—a legacy
language chained to the Windows ecosystem. The prediction could not
have been more wrong. Over the following decade, C# became one of the
fastest-evolving general-purpose languages on earth, shipping annual
language versions whose features have influenced language evolution
across other ecosystems, while .NET's runtime performance improved to
the point where it is competitive with Go and often compares favourably
with Java in published benchmarks such as TechEmpower.

The transformation is not cosmetic. C# today supports sophisticated
pattern matching, mature async programming primitives, value types
powerful enough to eliminate allocations in hot paths, and a minimal-API
surface as concise as Python's FastAPI while adding the static type
checking that a compiled language provides. The language has grown, yet
it has grown with unusual discipline—almost every feature introduced
since C# 7 solves a real, measurable pain point rather than chasing
academic novelty.




```
- 10 -
```


<a id='p11'></a>
<!-- Página 11 -->

```
C# 2026: Enterprise Mastery



```

Why C# Remains the Right Choice for Enterprise
Work
Enterprise software has requirements that differ fundamentally from
startup prototypes: multi-year maintenance horizons, large teams who
must read each other's code, compliance requirements that demand
auditability, and scaling demands that compound unpredictably. C#
remains one of the strongest mainstream choices for these requirements,
for reasons that go beyond simple feature comparison.

Static typing catches entire categories of bugs at compile time rather than
in production. The type system in C# 2026—with nullable reference types
enforced by default, discriminated unions modelled through sealed
hierarchies, and first-class generics—makes illegal states harder to
represent. Tooling quality is excellent: the Roslyn compiler exposes an
entire syntax and semantic model that powers refactoring engines,
analyzers, and code-generation pipelines that no dynamically-typed
language can match. Rider and Visual Studio in 2026 are so capable that
developers frequently report that the IDE catches architectural problems
their colleagues miss in code review.

The .NET runtime's garbage collector is a generational, concurrent,
region-based collector that has been continuously refined for over two
decades. On well-tuned workloads with modest allocation rates, pause
times can reach the sub-millisecond range, and Background GC keeps
most collections off the critical path. On workloads with extreme
allocation pressure, the Span<T> and Memory<T> APIs let you bypass
allocation entirely. Few ecosystems offer this range: approachable
defaults for common cases and escape hatches for performance-critical
paths, all within the same language.

The .NET Ecosystem in 2026
Understanding the ecosystem around C# is as important as mastering the
language itself. As of publication, the landscape looks like this: .NET 10 is
the current Long-Term Support release, shipping with C# 14. .NET 9 (the
previous Standard Term Support release) remains widely deployed in

```
- 11 -
```


<a id='p12'></a>
<!-- Página 12 -->

```
C# 2026: Enterprise Mastery


```

production. The framework is now truly cross-platform—the same
codebase runs on Windows, Linux, macOS, iOS, Android, WebAssembly
(via Blazor), and even embedded targets via .NET nanoFramework.

NuGet, the package manager, hosts over 400,000 packages and has
matured considerably in dependency-graph resolution and security
scanning. The SDK-style project format, now universal, makes
multi-targeting—shipping a single NuGet package that works on net10.0,
net9.0, and netstandard2.0 simultaneously—a first-class workflow.
Workloads like MAUI (cross-platform native UI), Blazor (WebAssembly
and server-side), and ASP.NET Core (web and gRPC) share a common BCL,
eliminating the platform fragmentation that plagued the .NET Framework
era.

Release Cadence and LTS Strategy
Since .NET 5, Microsoft has shipped a major .NET version every
November. Even-numbered releases receive Long-Term Support (LTS)
status—three years of patches and security fixes. Odd-numbered releases
are Standard Term Support (STS) with eighteen months. For enterprise
teams, the LTS strategy is clear: standardise on .NET 8 -> .NET 10 -> .NET
12. Run STS releases only if you need a specific feature and are confident
you can upgrade within the support window.

C# versions are tied to .NET versions but can be constrained in the project
file. A project targeting net10.0 defaults to C# 14, but you can pin to C# 12
if your team is not ready to adopt newer syntax. This is an underused
safety valve: use it during large-scale team migrations to ensure
consistent code review standards before adopting new language features
across the codebase.
ENTERPRISE TIP: LTS & Language Version Strategy
Always align your LTS .NET version upgrade with a deliberate
syntax-review cycle. Enable new language features intentionally via
<LangVersion> in your .csproj, rather than discovering them accidentally
when a colleague submits a PR using syntax no one else on the team
recognises.


```
- 12 -
```


<a id='p13'></a>
<!-- Página 13 -->

```
C# 2026: Enterprise Mastery



```

When to Choose C# — and When Not To
Intellectual honesty demands acknowledging the domains where C# is
not the optimal choice. For data science and machine learning research,
Python's ecosystem—NumPy, pandas, PyTorch—is simply unmatched.
Although ML.NET and Microsoft.Extensions.AI bring AI capabilities to C#,
and the 2026 tooling for consuming ONNX models from C# is excellent,
most model training still happens in Python. If you are building pipelines
that bridge training and inference, C# shines at the inference and serving
layer; Python shines during research and training.

For systems programming where every byte matters—OS kernels, device
drivers, safety-critical embedded code—Rust has displaced C++ at the
bleeding edge. C# with native AOT and unsafe code can operate in
constrained environments, but it is not the first choice for bare-metal
work. For short-lived scripting tasks where a Bash one-liner or a Python
script would suffice, the ceremony of a compiled .NET project is
unnecessary overhead.

Everywhere else—web APIs, desktop applications, game logic (via Unity),
mobile apps (via MAUI), cloud services, CLI tools, background workers,
data pipelines, IoT gateways—C# is a strong default choice. The
language's combination of expressiveness, static safety, performance, and
tooling quality makes it well suited to production software that must be
maintained by a team over years. Other ecosystems — Java, Go, Rust,
TypeScript — are excellent too; the right choice depends on team skills,
existing investment, and the specific problem.

The Community and Open-Source Ecosystem
The open-source shift has been transformational for C#. The language
specification, the compiler (Roslyn), the runtime (coreclr), the standard
library (corefx), and ASP.NET Core are all developed in the open on
GitHub, with issues, pull requests, and design discussions visible to
everyone. Language design proposals are discussed publicly in the
csharplang repository before implementation begins. This transparency
means that C# developers can read exactly why a feature was designed
the way it was, which helps write idiomatic code.
```
- 13 -
```


<a id='p14'></a>
<!-- Página 14 -->

```
C# 2026: Enterprise Mastery


```

Third-party libraries like Dapper, MassTransit, MediatR,
FluentValidation, Polly, and Serilog remain widely adopted in
enterprise .NET codebases — though the community's preferences
continue to shift, and some teams now favour lighter-weight or
hand-rolled alternatives. Understanding their design, knowing when to
use them, and knowing when to write something simpler yourself is part
of professional C# mastery. This book covers the most important of these
libraries in context, showing both their strengths and the edge cases
where they add more complexity than they remove.


## KEY TAKEAWAYS

```
– C# has evolved dramatically since 2016; code written against 2010
```

idioms is a liability in 2026.
```
– .NET 10 (LTS) is the production standard; align team LTS upgrades
```

with deliberate syntax reviews.
```
– Static typing, strong tooling, and a mature runtime make C# a
```

compelling enterprise choice.
```
– C# is not optimal for ML research, bare-metal systems programming,
```

or trivial scripting tasks.
```
– The open-source shift means language decisions are transparent—
```

read csharplang to understand why.
```
– The community ecosystem (Dapper, MassTransit, Polly, etc.) is part of
```

the C# professional toolkit.




```
- 14 -
```


<a id='p15'></a>
<!-- Página 15 -->

```
C# 2026: Enterprise Mastery


```


## PART I — THE C# 2026 LANDSCAPE


## CHAPTER 2




C# 14 and .NET 10: What Actually
```
Ma'ers

```

"New features earn their place by solving real problems, not by being
```
novel."


```

A note on versions: C# 13 shipped with .NET 9, and C# 14 shipped
with .NET 10. Because many teams upgrade across two LTS releases at
once, this chapter covers both — the C# 13 features you may have
skipped, and the C# 14 features that are new in .NET 10. The emphasis
throughout is on what actually matters for enterprise code, not on
novelty.

How to Evaluate a Language Feature
Every C# release ships new syntax that enthusiasts immediately blog
about. Not every feature deserves immediate adoption in your production
codebase. The right framework for evaluation asks three questions: Does
this feature reduce bugs or make illegal states unrepresentable? Does it
improve runtime performance? Does it reduce boilerplate without
sacrificing readability? Features that score positively on at least two of
these dimensions are worth adopting. Features that only reduce
keystrokes while obscuring intent are worth leaving in opt-in mode until
your team is comfortable with them.

params Collections
Before C# 13, params worked only with arrays. C# 13 extends it to any
collection type that implements IEnumerable<T> or has an appropriate
```
- 15 -
```


<a id='p16'></a>
<!-- Página 16 -->

```
C# 2026: Enterprise Mastery


```

collection interface. This is more than syntax sugar—it enables zero-copy
caller paths when the compiler can prove the argument is already the
right collection type.
Listing: Chapter02/ParamsCollections.cs


// C# 12 and earlier — always allocates an array
void LogMessages(params string[] messages) { ... }

// C# 13 — works with IEnumerable<T>, List<T>,
// ReadOnlySpan<T>, etc.
void LogMessages(params ReadOnlySpan<string> messages)
{
```
foreach (var msg in messages)
Console.WriteLine(msg);
```

}

// Caller: no allocation when passing a span
Span<string> items = stackalloc string[] { "start",
"process", "end" };
// zero heap allocation on this call path
LogMessages(items);




The New System.Threading.Lock Type
The lock keyword in C# has always been a syntactic wrapper around
Monitor.Enter / Monitor.Exit. In .NET 9 and C# 13, a new
System.Threading.Lock type was introduced that the compiler recognises
specially. When you lock on an instance of Lock (rather than a plain
object), the runtime uses a more efficient locking mechanism and the
compiler can emit better-optimised IL. For newly written lock-based
coordination code, the Lock type is a strong default. It does not replace
lock-free techniques, channels, actor-style designs, or async coordination
primitives — those remain the right tool for their respective problems —
but where you would previously have written lock(someObject),
lock(aLockInstance) is the better choice.




```
- 16 -
```


<a id='p17'></a>
<!-- Página 17 -->

```
C# 2026: Enterprise Mastery


```

Listing: Chapter02/ThreadingLock.cs


// Old approach — using an opaque object as a mutex
private readonly object _gate = new object();

void OldWay()
{
```
lock (_gate) { /* critical section */ }
```

}

// C# 13 / .NET 9+ — use System.Threading.Lock
private readonly Lock _lock = new Lock();

void NewWay()
{
```
lock (_lock) { /* critical section — more efficient
```

*/ }
}

// Also supports explicit Enter/Exit for try/finally
// patterns:
using (_lock.EnterScope())
{
```
// critical section
```

}




Partial Properties and Partial Indexers
Partial methods have existed since C# 2, but partial properties were a
notable gap. Source generators—the mechanism behind EF Core's
compiled models, System.Text.Json's source-generated serialisers, and
many other frameworks—frequently need to generate code that
completes a property defined in user code. C# 13 closes this gap with
partial properties and partial indexers, enabling cleaner source-generator
APIs that do not require awkward workarounds.




```
- 17 -
```


<a id='p18'></a>
<!-- Página 18 -->

```
C# 2026: Enterprise Mastery


```

Listing: Chapter02/PartialProperties.cs


// Defining file (user code)
public partial class UserProfile
{
```
// Declaration — just the signature
public partial string DisplayName { get; set; }
```

}

// Generated file (source generator output)
public partial class UserProfile
{
```
private string _displayName = string.Empty;

public partial string DisplayName
{
get => _displayName;
set
{

```

ArgumentException.ThrowIfNullOrWhiteSpace(value);
```
_displayName = value.Trim();
}
}
```

}




ref and unsafe in Iterators and Async Methods
A long-standing restriction prevented the use of ref locals and unsafe code
inside iterator methods (those using yield return) and async methods. C#
13 relaxes this: you may now declare and use ref locals and Span<T>
inside an async method. One rule still holds, and it is the important one —
a ref local or a Span<T> cannot live across an await. The compiler
enforces this. The pattern that works is to confine all ref/Span work to a
synchronous region between await points, typically by extracting it into a
separate non-async method.




```
- 18 -
```


<a id='p19'></a>
<!-- Página 19 -->

```
C# 2026: Enterprise Mastery


```

Listing: Chapter02/RefInAsync.cs


// C# 13: ref locals and Span<T> may be used inside an
// async method.
public async Task<int> ProcessBufferAsync(Memory<byte>
memory, CancellationToken ct)
{
```
// an await boundary
await Task.Yield();

// OK: the ref local and the Span<T> are created, used,
// and discarded
// entirely WITHIN this synchronous region — they never
// cross an await.
int processed = MutateInPlace(memory.Span);

// another await boundary
await SomeAsyncOperation(ct);
return processed;
```

}

// The Span<T> work lives in a synchronous helper. This is
// the pattern that
// always compiles, regardless of C# version, and it
// documents intent clearly.
private static int MutateInPlace(Span<byte> buffer)
{
```
if (buffer.IsEmpty) return 0;
ref byte firstByte = ref buffer[0];
// direct memory mutation
firstByte = 0xFF;
return buffer.Length;
```

}

// WHY NOT keep the ref local in the async method directly?
// Because a ref local (or Span<T>) cannot survive an
// await: after the method
// suspends and resumes, the referenced storage may have
// moved. The compiler
// rejects a ref local that is still in scope across an
// await. Confining the
// ref work to a synchronous helper makes that boundary



```
- 19 -
```


<a id='p20'></a>
<!-- Página 20 -->

```
C# 2026: Enterprise Mastery


```

// explicit.




allows ref struct Constraint
Generic type parameters have historically been unable to accept ref struct
types like Span<T> or ReadOnlySpan<T> because the compiler could not
guarantee that such types would not escape to the heap. The allows ref
struct anti-constraint (note: not a positive constraint—it removes a
restriction) permits generics to accept ref struct arguments, opening up
allocation-free generic algorithms that were previously impossible.
Listing: Chapter02/AllowsRefStruct.cs


// Before C# 13: could not accept Span<T> as a generic
// argument
// After C# 13: the allows ref struct anti-constraint
// permits it

static TResult Transform<T, TResult>(T input)
```
where T : allows ref struct
where TResult : allows ref struct
```

{
```
// process input — T may be Span<byte>,
// ReadOnlySpan<char>, etc.
return default!;
```

}

// Usage: now works with ref structs
ReadOnlySpan<char> slice = "hello world".AsSpan(0, 5);
// Generic algorithms can now process these without boxing




.NET 9 Performance Highlights
.NET 9 shipped in November 2024 with a staggering list of performance
improvements accumulated by the team across the BCL, the JIT compiler,
the garbage collector, and the ASP.NET Core middleware pipeline. A few
highlights that directly affect production code:



```
- 20 -
```


<a id='p21'></a>
<!-- Página 21 -->

```
C# 2026: Enterprise Mastery


```

• The JIT's dynamic profile-guided optimisation (Dynamic PGO) is now
enabled by default for all workloads. It tiered-compiles hot methods
based on actual runtime data, which can measurably improve the
throughput of long-running services compared to .NET 8 without any
code changes. The gain varies by workload — measure your own.
• LINQ gained three new methods: CountBy, AggregateBy, and Index.
CountBy and AggregateBy replace common pattern of GroupBy
followed by ToDictionary with a single pass. Index provides
zero-allocation enumerable index tracking.
• The new HybridCache API (covered deeply in Chapter 14) consolidates
L1/L2 caching behind a single abstraction with built-in stampede
prevention.
• System.Text.Json source generation is increasingly preferred in
high-performance scenarios, avoiding reflection-based serialisation
overhead and supporting trimming and ahead-of-time compilation.
• SearchValues<T> gained char class support, enabling vectorised
character-class searches that are typically much faster than
hand-rolled loops for text parsing.
Listing: Chapter02/NewLinqMethods.cs


// .NET 9: New LINQ methods
```
var orders = GetOrders();

```

// Old: GroupBy + ToDictionary — two passes, allocates
// groups
```
var oldCountByStatus = orders
.GroupBy(o => o.Status)
.ToDictionary(g => g.Key, g => g.Count());

```

// New: CountBy — single pass, no intermediate groups
```
var countByStatus = orders.CountBy(o => o.Status);

```

// New: AggregateBy — single-pass aggregate per key
```
var totalByCustomer = orders.AggregateBy(
keySelector: o => o.CustomerId,
seed: 0m,
func: (acc, o) => acc + o.Amount);



- 21 -
```


<a id='p22'></a>
<!-- Página 22 -->

```
C# 2026: Enterprise Mastery


```

// New: Index — get (index, element) pairs without overhead
foreach (var (i, order) in orders.Index())
{
```
Console.WriteLine($"[{i}] {order.Id}");
```

}




C# 14 Highlights in .NET 10
.NET 10 shipped with C# 14. The following additions are the ones most
likely to affect day-to-day enterprise code. As always, adopt them
deliberately rather than reflexively.

Extension members represent the most ambitious syntax addition in
recent memory. They extend the classic extension-method concept to
allow extension properties, extension events, and even extension
operators. This closes a gap that has frustrated library authors for years,
enabling cleaner fluent APIs and domain-model enrichment patterns
without requiring wrapper classes.
Listing: Chapter02/ExtensionMembers.cs


// C# 14: Extension members
// Extends a type without inheriting from it

extension(string s) StringExtensions
{
```
// Extension property (C# 14)
public bool IsValidEmail => s.Contains('@') &&
```

s.Contains('.');

```
// Extension indexer (C# 14)
public char this[Index index] => s[index];

// Classic extension method — still works
public string Truncate(int maxLength) =>
s.Length <= maxLength ? s : s[..maxLength] + "...";
```

}

// Usage
string email = "victor@example.com";
// true — extension property

```
- 22 -
```


<a id='p23'></a>
<!-- Página 23 -->

```
C# 2026: Enterprise Mastery


```

Console.WriteLine(email.IsValidEmail);
// "victor@ex..." — extension method
Console.WriteLine(email.Truncate(10));




Features to Approach with Caution
Not every new feature deserves immediate adoption. Here are some that
require careful team discussion before enabling across a codebase:

• Extension members (C# 14): Powerful but easy to abuse. Extension
properties that hide significant logic violate the principle of least
surprise. Establish clear guidelines before enabling.
• Interceptors: An advanced source-generator mechanism that allows
generated code to replace calls to specific methods at compile time.
Useful for frameworks, dangerous for application code—the
indirection makes debugging extremely difficult.
• Primary constructors on non-record classes: Useful for simple
dependency injection, but can lead to classes where it is unclear
which fields are initialised by the constructor versus elsewhere. Add a
coding standard document clarifying when they are and are not
appropriate.
• Collection expressions with complex spread syntax: The spread
operator ([..a, ..b, x]) is concise but can obscure O(n) allocations.
Always benchmark when using in hot paths.


## KEY TAKEAWAYS

```
– params Collections now supports ReadOnlySpan<T>, enabling
```

zero-allocation variadic calls.
```
– System.Threading.Lock replaces the opaque-object pattern with a
```

more efficient typed lock.
```
– Partial properties solve a long-standing pain point for
```

source-generator-based frameworks.
```
– allows ref struct opens generic algorithms to Span<T> and
```

Memory<T> without boxing.
```
– .NET 9's Dynamic PGO is on by default—upgrade existing services for
```

free throughput gains.
```
- 23 -
```


<a id='p24'></a>
<!-- Página 24 -->

```
C# 2026: Enterprise Mastery


```

– New LINQ methods CountBy, AggregateBy, and Index replace common
two-pass patterns.
– C# 14 extension members are promising but require disciplined
adoption guidelines.
– Not every feature should be adopted immediately—evaluate against
your team's readiness.




```
- 24 -
```


<a id='p25'></a>
<!-- Página 25 -->

```
C# 2026: Enterprise Mastery


```


## PART II — WRITING CODE THAT ENDURES


## CHAPTER 3




```
Clean Code in Modern C#

"Any fool can write code that a computer can understand. Good
```

programmers write code that humans can understand." — Martin Fowler


What Clean Code Actually Means
Clean code is not about aesthetics. It is about economics. A study by the
National Institute of Standards and Technology estimated that software
defects cost the U.S. economy approximately $59 billion annually, and the
majority of that cost occurs during maintenance—reading code,
understanding code, modifying code. Clean code reduces maintenance
costs by making the code's intent so clear that modifications can be made
confidently, quickly, and correctly.

In the context of C# 2026, clean code means taking full advantage of the
language's expressive power—records, pattern matching, nullable
reference types, LINQ—while resisting the temptation to be clever. Clever
code is the enemy of maintainability. The most senior engineer on a team
is often the one who writes the most straightforward code, not the most
sophisticated. Sophistication should live in the design, not in the
individual lines.

Naming: The Foundation of Readability
The single highest-leverage investment in code readability is choosing
good names. Names are the comments that cannot go stale—they are
always read alongside the code they describe. A name should reveal
intent, avoid disinformation, and make meaningful distinctions.



```
- 25 -
```


<a id='p26'></a>
<!-- Página 26 -->

```
C# 2026: Enterprise Mastery


```

Listing: Chapter03/NamingExamples.cs


// AVOID: Intent-obscuring names
public int Calc(int x, int y) => x * y / 100;

public List<int> GetData(DateTime d)
{
```
var r = new List<int>();
// ... populate r
return r;
```

}

// GOOD: Intent-revealing names
public decimal CalculateDiscountedPrice(decimal unitPrice,
int discountPercent)
```
=> unitPrice * (100 - discountPercent) / 100m;

```

public IReadOnlyList<OrderId>
GetOrdersShippedAfter(DateOnly shippedAfterDate)
{
```
var orderIds = new List<OrderId>();
// ... populate orderIds
return orderIds;
```

}



Notice the return type change in the second example:
IReadOnlyList<OrderId> instead of List<int>. The strong type (OrderId as
a record struct) makes it impossible to accidentally mix up identifiers for
different entity types. The interface return type decouples callers from the
implementation. Both decisions communicate intent and enforce
correctness at compile time.

Method Design: Do One Thing, Do It Well
The single responsibility principle for methods is simple: a method should
do exactly one thing at one level of abstraction. When a method mixes
high-level orchestration with low-level implementation details, it becomes
hard to read, test, and reuse. The telltale sign is a method that needs
multiple sections separated by blank lines and comments explaining what


```
- 26 -
```


<a id='p27'></a>
<!-- Página 27 -->

```
C# 2026: Enterprise Mastery


```

each section does. Those sections should be extracted into their own
methods.
Listing: Chapter03/MethodDesign.cs


// AVOID: Mixed abstraction levels — hard to read and test
public async Task ProcessOrderAsync(OrderRequest request,
CancellationToken ct)
{
```
// Validate input
if (string.IsNullOrEmpty(request.CustomerId))
throw new ArgumentException("Customer ID
```

required");
```
if (request.Items.Count == 0)
throw new ArgumentException("Order must have
```

items");

```
// Calculate total
decimal total = 0;
foreach (var item in request.Items)
total += item.Quantity * item.UnitPrice;

// Apply discount
if (total > 1000)
total *= 0.9m;

// Save to database
var order = new Order { CustomerId =
```

request.CustomerId, Total = total };
```
await _db.Orders.AddAsync(order, ct);
await _db.SaveChangesAsync(ct);

// Send confirmation email
await _emailService.SendAsync(new
```

OrderConfirmationEmail(order), ct);
}

// GOOD: Single level of abstraction per method
public async Task ProcessOrderAsync(OrderRequest request,
CancellationToken ct)
{
```
ValidateOrderRequest(request);
var pricingSummary = CalculatePricing(request.Items);


- 27 -
```


<a id='p28'></a>
<!-- Página 28 -->

```
C# 2026: Enterprise Mastery


var order = await SaveOrderAsync(request.CustomerId,
```

pricingSummary, ct);
```
await SendConfirmationAsync(order, ct);
```

}

private static void ValidateOrderRequest(OrderRequest
request)
{

ArgumentException.ThrowIfNullOrWhiteSpace(request.CustomerI
d, nameof(request.CustomerId));
```
if (request.Items.Count == 0)
throw new ArgumentException("Order must contain at
```

least one item.", nameof(request.Items));
}

private static PricingSummary
CalculatePricing(IReadOnlyList<OrderItem> items)
{
```
var subtotal = items.Sum(i => i.Quantity *
```

i.UnitPrice);
```
var discount = subtotal > 1000m ? subtotal * 0.1m : 0m;
return new PricingSummary(subtotal, discount, subtotal
```

- discount);
}




Meaningful Use of Records and Immutability
Records, introduced in C# 9 and refined through C# 12, are one of the
most impactful additions to the language for writing clean, expressive
code. A record is a reference type (or value type for record struct) whose
identity is defined by its values rather than its reference. This makes
records ideal for domain value objects, DTOs, and event messages—places
where two instances with the same data should be considered equal.
Listing: Chapter03/Records.cs


// Records as value objects — structural equality for free
public record CustomerId(Guid Value)
{
```
public static CustomerId New() => new(Guid.NewGuid());

- 28 -
```


<a id='p29'></a>
<!-- Página 29 -->

```
C# 2026: Enterprise Mastery


public static CustomerId Parse(string raw) =>
```

new(Guid.Parse(raw));
```
public override string ToString() =>
```

Value.ToString("D");
}

public record Money(decimal Amount, string Currency)
{
```
public static Money Zero(string currency) => new(0m,
```

currency);

```
public Money Add(Money other)
{
if (other.Currency != Currency)
throw new InvalidOperationException(
$"Cannot add {Currency} and
```

{other.Currency}");
```
return this with { Amount = Amount +
```

other.Amount };
```
}
```

}

// Usage: two Money instances with same values are equal
```
var a = new Money(100m, "USD");
var b = new Money(100m, "USD");
```

Console.WriteLine(a == b); // true — value equality
// Money { Amount = 200, Currency = USD }
Console.WriteLine(a.Add(b));




The Art of the Comment
Most comments in production code are apologies for unclear code. If you
find yourself writing a comment that explains what the code does, that is
a strong signal to rename the method or variable instead. Good comments
explain why, not what—they document decisions, constraints, and
reasoning that is not obvious and cannot be expressed in code.




```
- 29 -
```


<a id='p30'></a>
<!-- Página 30 -->

```
C# 2026: Enterprise Mastery


```

Listing: Chapter03/Comments.cs


// AVOID: Noise comment — the code already says this
// Increment i
i++;

// AVOID: Redundant comment — same information as the
// method name
// Gets the customer by ID
public Customer? GetCustomerById(Guid customerId) { ... }

// GOOD: Explains WHY a subtle decision was made
// We cap at 100 ms here because the upstream SLA is 200 ms
// and we
// need 100ms headroom for processing (see ADR 0042).
private static readonly TimeSpan UpstreamCallTimeout =
TimeSpan.FromMilliseconds(100);

// GOOD: Documents a known limitation that cannot be fixed
// yet
// KNOWN ISSUE: EF Core does not translate this GroupBy to
// SQL in version 9.
// It materialises the entire table first. Replace with a
// raw SQL query
// before this endpoint is exposed to external traffic. See
// issue #1847.
```
var grouped = await _db.Orders
.AsNoTracking()
.GroupBy(o => o.CustomerId)
.ToDictionaryAsync(g => g.Key, g => g.Count(), ct);




```

Null Safety: Making Bugs Disappear at Compile
Time
Nullable reference types, enabled by default in all new .NET 9+ projects,
are the most impactful safety feature of modern C#. When enabled, the
compiler distinguishes between string (never null) and string? (possibly
null) and warns when you dereference a nullable reference without a null
check. The practical result is that an entire category of
NullReferenceException bugs—the most common exception in

```
- 30 -
```


<a id='p31'></a>
<!-- Página 31 -->

```
C# 2026: Enterprise Mastery


```

enterprise .NET systems—is caught at compile time instead of in
production.
Listing: Chapter03/NullSafety.cs


// With nullable reference types enabled
// (<Nullable>enable</Nullable>)

// The compiler warns: 'Name' may be null, unboxing or
// calling a member may fail
public string GetDisplayName(User? user)
```
// WARNING CS8602: Dereference of a possibly null
// reference
=> user.Name.ToUpper();

```

// GOOD: Explicit null-checking makes intent clear
public string GetDisplayName(User? user)
{
```
if (user is null) return "Anonymous";
return user.Name.ToUpper();
```

}

// GOOD: Or use the null-conditional operator cleanly
public string GetDisplayName(User? user)
```
=> user?.Name?.ToUpper() ?? "Anonymous";

```

// GOOD: Eliminating null from domain models with required
// + init
public class CustomerProfile
{
```
public required string FullName { get; init; }
public required string Email { get; init; }
// Genuinely optional
public string? Phone { get; init; }
```

}

// Compiler enforces FullName and Email at construction
// site:
```
var profile = new CustomerProfile
```

{
```
FullName = "Victor Mihailov",
Email = "victor@example.com"
// Phone is optional — no compiler warning


- 31 -
```


<a id='p32'></a>
<!-- Página 32 -->

```
C# 2026: Enterprise Mastery


```

};




Exception Handling: Fail Loudly, Recover
Deliberately
Exception handling is one of the most frequently abused areas of C# code.
Two anti-patterns dominate: swallowing exceptions silently (catch blocks
that do nothing) and catching Exception at the wrong layer (catching
everything when only specific failures should be handled). Both lead to
systems that appear healthy while silently producing incorrect results.
Listing: Chapter03/ExceptionHandling.cs


// AVOID: Swallowed exception — the worst pattern in
// production code
try
{
```
await _paymentGateway.ChargeAsync(order, ct);
```

}
catch (Exception)
{
```
// Nothing here — caller has no idea if the charge
// succeeded
```

}

// AVOID: Overly broad catch at the wrong layer
try
{
```
var result = await ProcessComplexWorkflowAsync(ct);
return result;
```

}
catch (Exception ex)
{
```
_logger.LogError(ex, "Workflow failed");
return null!; // caller doesn't know what 'null' means
```

}

// GOOD: Catch what you can handle; let everything else
// propagate
public async Task<PaymentResult> ChargeCustomerAsync(Order
order, CancellationToken ct)

```
- 32 -
```


<a id='p33'></a>
<!-- Página 33 -->

```
C# 2026: Enterprise Mastery


```

{
```
try
{
return await _paymentGateway.ChargeAsync(order,
```

ct);
```
}
catch (PaymentDeclinedException ex)
{
// We know how to handle declines — return a typed
// result
_logger.LogInformation("Payment declined for order
```

{OrderId}: {Reason}",
```
order.Id, ex.DeclineReason);
return PaymentResult.Declined(ex.DeclineReason);
}
catch (PaymentGatewayUnavailableException)
{
// Transient failure — let the caller or the retry
// policy handle it
throw;
}
// Any other exception propagates to the global handler
```

}




## KEY TAKEAWAYS

– Names reveal intent — every bad name is technical debt that
compounds with each reader.
– Methods should operate at one level of abstraction; extract sub-steps
into named methods.
– Records provide value equality for free — ideal for domain value
objects, DTOs, and events.
– Comments should explain WHY, never WHAT; if you feel the need to
explain what, rename instead.
– Enable <Nullable>enable</Nullable> in every project — it eliminates
NullReferenceExceptions at compile time.
– Catch only the exceptions you can handle; let everything else
propagate to the appropriate layer.



```
- 33 -
```


<a id='p34'></a>
<!-- Página 34 -->

```
C# 2026: Enterprise Mastery




```

- 34 -

<a id='p35'></a>
<!-- Página 35 -->

```
C# 2026: Enterprise Mastery


```


## PART II — WRITING CODE THAT ENDURES


## CHAPTER 4




```
SOLID Principles in C# Prac,ce

"Good design is not about following rules — it is about internalising
principles and exercising judgment."


```

Why SOLID Still Matters in 2026
SOLID has been discussed so extensively that it risks becoming dogma
rather than principle. The risk cuts both ways: some teams ignore it and
pay the price in tangled, untestable code; others enforce it religiously and
end up with over-engineered systems where a simple feature change
requires modifying seven interfaces and four abstract classes. The goal of
this chapter is to give you a practical, calibrated understanding of each
principle: what problem it solves, what it costs, and when applying it is
the right engineering trade-off.

Single Responsibility Principle (SRP)
A class should have one reason to change. More precisely, it should have
one primary responsibility to one stakeholder. A class that handles both
business logic and database access will change when business rules
change AND when persistence details change, creating unnecessary
coupling and making both concerns harder to test in isolation.
Listing: Chapter04/SRP.cs


// AVOID: Multiple responsibilities: business logic + data
// access + email
public class OrderService
{
```
private readonly SqlConnection _connection;


- 35 -
```


<a id='p36'></a>
<!-- Página 36 -->

```
C# 2026: Enterprise Mastery


private readonly SmtpClient _smtp;

public void PlaceOrder(OrderRequest req)
{
// Business logic
if (req.Total > 10000)
throw new BusinessException("Orders over
```

$10,000 require approval");

```
// Data access
using var cmd = _connection.CreateCommand();
cmd.CommandText = "INSERT INTO Orders ...";
cmd.ExecuteNonQuery();

// Email
_smtp.Send(new MailMessage("no-reply@co.com",
```

req.Email, "Order Confirmed", "..."));
```
}
```

}

// GOOD: Three focused classes, each with one reason to
// change
public class OrderValidationService
{
```
public void Validate(OrderRequest req)
{
if (req.Total > 10000)
throw new BusinessException("Orders over
```

$10,000 require approval");
```
}
```

}

public class OrderRepository
{
```
private readonly AppDbContext _db;
public OrderRepository(AppDbContext db) => _db = db;
public async Task SaveAsync(Order order,
```

CancellationToken ct)
```
=> await _db.Orders.AddAsync(order, ct);
```

}

public class OrderNotificationService
{
```
private readonly IEmailSender _email;

- 36 -
```


<a id='p37'></a>
<!-- Página 37 -->

```
C# 2026: Enterprise Mastery


public OrderNotificationService(IEmailSender email) =>
```

_email = email;
```
public Task SendConfirmationAsync(Order order,
```

CancellationToken ct)
```
=> _email.SendAsync(new
```

OrderConfirmationEmail(order), ct);
}




Open/Closed Principle (OCP)
Software entities should be open for extension but closed for modification.
In practice this means designing systems so that new behaviour can be
added by writing new code rather than by changing existing, tested code.
The classic implementation mechanism in C# is the strategy pattern
combined with dependency injection, but C# 2026 offers richer options
through discriminated union-like sealed hierarchies and pattern
matching.
Listing: Chapter04/OCP.cs


// OCP via strategy pattern + DI — adding new discount
// types without modifying existing code
public interface IDiscountStrategy
{
```
decimal Apply(decimal price, CustomerTier tier);
```

}

public class NoDiscount : IDiscountStrategy
{
```
public decimal Apply(decimal price, CustomerTier tier)
```

=> price;
}

public class VolumeDiscount : IDiscountStrategy
{
```
private readonly decimal _threshold;
private readonly decimal _rate;
public VolumeDiscount(decimal threshold, decimal rate)
=> (_threshold, _rate) = (threshold, rate);

public decimal Apply(decimal price, CustomerTier tier)

- 37 -
```


<a id='p38'></a>
<!-- Página 38 -->

```
C# 2026: Enterprise Mastery


=> price > _threshold ? price * (1 - _rate) :
```

price;
}

// New requirement: loyalty discount — add new class, zero
// modifications to existing code
public class LoyaltyDiscount : IDiscountStrategy
{
```
public decimal Apply(decimal price, CustomerTier tier)
```

=>
```
tier switch
{
CustomerTier.Gold => price * 0.85m,
CustomerTier.Platinum => price * 0.75m,
_ => price,
};
```

}

// Orchestrator never changes regardless of how many
// strategies we add
public class PricingEngine
{
```
private readonly IEnumerable<IDiscountStrategy>
```

_strategies;
```
public PricingEngine(IEnumerable<IDiscountStrategy>
```

strategies)
```
=> _strategies = strategies;

public decimal FinalPrice(decimal basePrice,
```

CustomerTier tier)
```
=> _strategies.Aggregate(basePrice, (p, s) =>
```

s.Apply(p, tier));
}




Liskov Substitution Principle (LSP)
If S is a subtype of T, then objects of type T in a program may be replaced
with objects of type S without altering any of the desirable properties of
that program. Violations of LSP manifest as defensive type-checks in
calling code (the 'if (obj is SubType)' smell), unexpected exceptions from
overridden methods, or pre/postcondition strengthening in subclasses.

```
- 38 -
```


<a id='p39'></a>
<!-- Página 39 -->

```
C# 2026: Enterprise Mastery


```

Listing: Chapter04/LSP.cs


// Classic LSP violation: Rectangle / Square
public class Rectangle
{
```
public virtual int Width { get; set; }
public virtual int Height { get; set; }
public int Area => Width * Height;
```

}

public class Square : Rectangle
{
```
public override int Width { set => base.Width =
```

base.Height = value; }
```
public override int Height { set => base.Width =
```

base.Height = value; }
}

// This method works for Rectangle but breaks for Square:
static void AssertRectangleArea(Rectangle r)
{
```
r.Width = 5;
r.Height = 4;
// FAILS for Square — Area is 16
Debug.Assert(r.Area == 20);
```

}

// GOOD: LSP-safe design: model shapes without inheritance
public abstract record Shape
{
```
public abstract int Area { get; }
```

}

public record RectangleShape(int Width, int Height) : Shape
{
```
public override int Area => Width * Height;
```

}

public record SquareShape(int Side) : Shape
{
```
public override int Area => Side * Side;
```

}



```
- 39 -
```


<a id='p40'></a>
<!-- Página 40 -->

```
C# 2026: Enterprise Mastery



```

Interface Segregation Principle (ISP)
Clients should not be forced to depend on interfaces they do not use. Fat
interfaces—those with many methods—force implementors to provide
stub or throw-not-implemented versions of methods they do not need.
This is especially common in repository patterns where a single
'IRepository' interface demands implementation of Create, Read, Update,
Delete, and a dozen query methods even for read-only use cases.
Listing: Chapter04/ISP.cs


// AVOID: Fat interface — ReadOnlyReportService has to
// implement mutations it doesn't use
public interface IOrderRepository
{
```
Task<Order?> GetByIdAsync(OrderId id, CancellationToken
```

ct);
```
Task<IReadOnlyList<Order>>
```

GetByCustomerAsync(CustomerId id, CancellationToken ct);
```
Task SaveAsync(Order order, CancellationToken ct);
Task DeleteAsync(OrderId id, CancellationToken ct);
Task<IReadOnlyList<Order>> SearchAsync(OrderSearchQuery
```

q, CancellationToken ct);
}

// GOOD: Segregated interfaces — each client depends only
// on what it uses
public interface IOrderReader
{
```
Task<Order?> GetByIdAsync(OrderId id, CancellationToken
```

ct);
```
Task<IReadOnlyList<Order>>
```

GetByCustomerAsync(CustomerId id, CancellationToken ct);
```
Task<IReadOnlyList<Order>> SearchAsync(OrderSearchQuery
```

q, CancellationToken ct);
}

public interface IOrderWriter
{
```
Task SaveAsync(Order order, CancellationToken ct);
Task DeleteAsync(OrderId id, CancellationToken ct);
```

}


```
- 40 -
```


<a id='p41'></a>
<!-- Página 41 -->

```
C# 2026: Enterprise Mastery




```

// Implementation composes both
public class OrderRepository : IOrderReader, IOrderWriter {
... }

// Report service depends only on reading
public class OrderReportService
{
```
private readonly IOrderReader _reader;
public OrderReportService(IOrderReader reader) =>
```

_reader = reader;
```
// No access to Save/Delete — impossible to introduce
// accidental mutations
```

}




Dependency Inversion Principle (DIP)
High-level modules should not depend on low-level modules. Both should
depend on abstractions. This is the foundational principle that makes
dependency injection possible—and testable code achievable. When your
business logic depends on a concrete SqlOrderRepository, you cannot test
it without a database. When it depends on IOrderReader, you can inject a
mock, a fake, or an in-memory implementation.
Listing: Chapter04/DIP.cs


// AVOID: High-level module hard-wires to a low-level
// implementation
public class OrderProcessingService
{
```
private readonly SqlOrderRepository _repo = new
```

SqlOrderRepository(
```
connectionString:
```

"Server=proddb01;Database=Orders;...");
```
private readonly SmtpEmailService _email = new
```

SmtpEmailService(host: "mail.company.com");

```
public async Task ProcessAsync(OrderRequest req,
```

CancellationToken ct)
```
{
// Cannot test without a real SQL Server and an

- 41 -
```


<a id='p42'></a>
<!-- Página 42 -->

```
C# 2026: Enterprise Mastery


// SMTP server
var order = Order.Create(req);
await _repo.SaveAsync(order, ct);
await _email.SendConfirmationAsync(order, ct);
}
```

}

// GOOD: Depending on abstractions — fully testable,
// extensible
public class OrderProcessingService
{
```
private readonly IOrderWriter _orders;
private readonly IOrderNotifier _notifier;

public OrderProcessingService(IOrderWriter orders,
```

IOrderNotifier notifier)
```
=> (_orders, _notifier) = (orders, notifier);

public async Task ProcessAsync(OrderRequest req,
```

CancellationToken ct)
```
{
var order = Order.Create(req);
await _orders.SaveAsync(order, ct);
await _notifier.NotifyAsync(order, ct);
}
```

}

// DI container wires the real implementations in
// production:
builder.Services.AddScoped<IOrderWriter,
SqlOrderRepository>();
builder.Services.AddScoped<IOrderNotifier,
EmailOrderNotifier>();
// Test replaces them with fakes — zero code change in the
// service




When SOLID Becomes Rigid
SOLID is a set of principles, not rules. Over-applying them in contexts
where they are not needed creates accidental complexity that impedes
rather than helps. A CRUD admin panel with ten database tables does not

```
- 42 -
```


<a id='p43'></a>
<!-- Página 43 -->

```
C# 2026: Enterprise Mastery


```

need a complex strategy-pattern pricing engine or fifteen segregated
repository interfaces. A startup building its first MVP should prioritise
shipping over perfect SOLID compliance. Refactoring toward SOLID is
much easier than starting over from scratch.

## PRAGMATIC SOLID

Apply SOLID principles where complexity and change frequency justify
them. In simple, stable areas of your codebase, straightforward code that
does not follow every SOLID letter to the dot is often the right engineering
trade-off. Reserve the investment in abstraction for the parts of your
system that change frequently and must be tested in isolation.


## KEY TAKEAWAYS

```
– SRP: one reason to change, not one method — cohesion of
```

responsibility matters.
```
– OCP: add new behaviour through new code; dependency injection
```

enables this in C#.
```
– LSP: subtypes must be fully substitutable — use sealed hierarchies +
```

pattern matching when inheritance breaks LSP.
```
– ISP: keep interfaces small and client-specific; composing them in
```

implementations is fine.
```
– DIP: depend on abstractions at every inter-module boundary — it is
```

what makes testing possible.
```
– SOLID is calibrated wisdom, not religious law — apply judgment
```

about where complexity is warranted.




```
- 43 -
```


<a id='p44'></a>
<!-- Página 44 -->

```
C# 2026: Enterprise Mastery


```


## PART II — WRITING CODE THAT ENDURES


## CHAPTER 5




Design Pa'erns That S,ll Ma'er in
```
2026

"A pattern is a named solution to a recurring problem in context."


```

Which Patterns Survive the Test of Time
The Gang of Four published Design Patterns in 1994. Some of those
patterns are now language features in C#—Iterator is built into
IEnumerable<T>, Decorator is trivially expressible with records and
extension methods, and Singleton is handled by the DI container. Others
remain as relevant as ever because they solve problems that language
features cannot: the Mediator pattern for decoupling components in a
pipeline, the Outbox pattern for reliable event publishing, and the Saga
pattern for distributed transactions.

This chapter focuses on the patterns that provide the most value in
modern C# enterprise systems. For each, you will see both a naive
implementation and a production-quality version that accounts for
performance, thread safety, and testability.




```
- 44 -
```


<a id='p45'></a>
<!-- Página 45 -->

```
C# 2026: Enterprise Mastery



```

Builder Pattern: Constructing Complex Objects
Safely
Listing: Chapter05/Builder.cs


// for ReadOnlyDictionary<,>
using System.Collections.ObjectModel;

// Production-quality builder for an HTTP request
// configuration
public sealed class HttpRequestOptions
{
```
private HttpRequestOptions() { }

public required Uri BaseUri { get; private
```

init; }
```
public TimeSpan Timeout { get; private
```

init; } = TimeSpan.FromSeconds(30);
```
public int MaxRetries { get; private
```

init; } = 3;
```
public bool FollowRedirects{ get; private
```

init; } = true;
```
// IReadOnlyDictionary is the correct exposed type for
// an immutable map.
private static readonly IReadOnlyDictionary<string,
```

string> EmptyHeaders =
```
new ReadOnlyDictionary<string, string>(new
```

Dictionary<string, string>());
```
public IReadOnlyDictionary<string, string> Headers
```

{ get; private init; }
```
= EmptyHeaders;

public sealed class Builder
{
private Uri? _baseUri;
private TimeSpan _timeout =
```

TimeSpan.FromSeconds(30);
```
private int _maxRetries = 3;
private bool _followRedirects = true;
private readonly Dictionary<string, string>
```

_headers = new();



```
- 45 -
```


<a id='p46'></a>
<!-- Página 46 -->

```
C# 2026: Enterprise Mastery


public Builder WithBaseUri(string uri)
{
_baseUri = new Uri(uri);
return this;
}
public Builder WithTimeout(TimeSpan timeout)
```

{ _timeout = timeout; return this; }
```
public Builder WithMaxRetries(int retries)
```

{ _maxRetries = retries; return this; }
```
public Builder WithHeader(string key, string value)
{
_headers[key] = value;
return this;
}
public HttpRequestOptions Build()
{
ArgumentNullException.ThrowIfNull(_baseUri,
```

nameof(_baseUri));
```
return new HttpRequestOptions
{
BaseUri = _baseUri,
Timeout = _timeout,
MaxRetries = _maxRetries,
FollowRedirects= _followRedirects,
// Dictionary<,> has no AsReadOnly(); wrap
// it explicitly.
Headers = new
```

ReadOnlyDictionary<string, string>(_headers),
```
};
}
}
```

}

// Usage
```
var options = new HttpRequestOptions.Builder()
.WithBaseUri("https://api.example.com")
.WithTimeout(TimeSpan.FromSeconds(10))
.WithHeader("X-Api-Key", apiKey)
.Build();




- 46 -
```


<a id='p47'></a>
<!-- Página 47 -->

```
C# 2026: Enterprise Mastery



```

Strategy Pattern: Injecting Behaviour
The Strategy pattern is one of the most used patterns in enterprise C#,
and the combination of interfaces and .NET's DI container makes it
trivially composable. The key insight in 2026 is using keyed services (new
in .NET 8) to select strategies by name without writing a manual factory.
Listing: Chapter05/Strategy.cs


public interface IPaymentProcessor
{
```
Task<PaymentResult> ChargeAsync(PaymentRequest req,
```

CancellationToken ct);
}

// Two strategies
public class StripeProcessor : IPaymentProcessor { ... }
public class PayPalProcessor : IPaymentProcessor { ... }

// Registration: keyed services (.NET 8+)
builder.Services.AddKeyedScoped<IPaymentProcessor,
StripeProcessor>("stripe");
builder.Services.AddKeyedScoped<IPaymentProcessor,
PayPalProcessor>("paypal");

// Resolution: inject a typed keyed resolver rather than
// the whole container.
// Taking IServiceProvider directly is effectively a
// Service Locator and hides
// the dependency; an explicit factory abstraction keeps
// the dependency visible
// and the class unit-testable.
public interface IPaymentProcessorFactory
{
```
IPaymentProcessor Resolve(string providerKey);
```

}

public sealed class
PaymentProcessorFactory(IServiceProvider sp)
```
: IPaymentProcessorFactory
```

{
```
// The single, intentional resolution boundary lives
// here, not scattered

- 47 -
```


<a id='p48'></a>
<!-- Página 48 -->

```
C# 2026: Enterprise Mastery


// through business code.
public IPaymentProcessor Resolve(string providerKey) =>

```

sp.GetRequiredKeyedService<IPaymentProcessor>(providerKey);
}

public class PaymentOrchestrator(IPaymentProcessorFactory
processors)
{
```
public async Task<PaymentResult> ProcessAsync(
PaymentRequest req, CancellationToken ct)
{
var processor = processors.Resolve(req.Provider);
return await processor.ChargeAsync(req, ct);
}
```

}




Mediator Pattern: Decoupling Commands and
Queries
The Mediator pattern decouples senders from receivers by routing
messages through a central broker. In C# enterprise systems, MediatR by
Jimmy Bogard has popularised this approach for CQRS (Command Query
Responsibility Segregation). The pattern dramatically simplifies
controllers and orchestrators by reducing them to thin layers that
dispatch commands and return results.
Listing: Chapter05/Mediator.cs


// Command + Handler — no direct coupling between API layer
// and business logic
public record CreateOrderCommand(
```
CustomerId CustomerId,
IReadOnlyList<OrderLineItem> Items
```

) : IRequest<OrderId>;

public class CreateOrderHandler :
IRequestHandler<CreateOrderCommand, OrderId>
{
```
private readonly IOrderWriter _orders;


- 48 -
```


<a id='p49'></a>
<!-- Página 49 -->

```
C# 2026: Enterprise Mastery


private readonly IOrderNotifier _notifier;
private readonly ILogger<CreateOrderHandler> _log;

public CreateOrderHandler(
IOrderWriter orders, IOrderNotifier notifier,
ILogger<CreateOrderHandler> log)
=> (_orders, _notifier, _log) = (orders, notifier,
```

log);

```
public async Task<OrderId> Handle(CreateOrderCommand
```

cmd, CancellationToken ct)
```
{
var order = Order.Create(cmd.CustomerId,
```

cmd.Items);
```
await _orders.SaveAsync(order, ct);
await _notifier.NotifyAsync(order, ct);
_log.LogInformation("Order {OrderId} created for
```

customer {CustomerId}",
```
order.Id, cmd.CustomerId);
return order.Id;
}
```

}

// Minimal API endpoint — zero business logic here
app.MapPost("/orders", async (CreateOrderCommand cmd,
ISender mediator, CancellationToken ct) =>
{
```
var orderId = await mediator.Send(cmd, ct);
return Results.Created($"/orders/{orderId}", orderId);
```

});




Decorator Pattern: Adding Cross-Cutting
Concerns
Listing: Chapter05/Decorator.cs


// Decorator: add caching to any IOrderReader without
// modifying the original class
public class CachingOrderReader : IOrderReader
{
```
private readonly IOrderReader _inner;

- 49 -
```


<a id='p50'></a>
<!-- Página 50 -->

```
C# 2026: Enterprise Mastery


private readonly IHybridCache _cache;
private static readonly TimeSpan CacheTtl =
```

TimeSpan.FromMinutes(5);

```
public CachingOrderReader(IOrderReader inner,
```

IHybridCache cache)
```
=> (_inner, _cache) = (inner, cache);

public async Task<Order?> GetByIdAsync(OrderId id,
```

CancellationToken ct)
```
=> await _cache.GetOrCreateAsync(
key: $"order:{id}",
factory: async token => await
```

_inner.GetByIdAsync(id, token),
```
cancellationToken: ct);

public Task<IReadOnlyList<Order>>
```

GetByCustomerAsync(CustomerId id, CancellationToken ct)
```
=> _inner.GetByCustomerAsync(id, ct);

public Task<IReadOnlyList<Order>>
```

SearchAsync(OrderSearchQuery q, CancellationToken ct)
```
=> _inner.SearchAsync(q, ct);
```

}

// DI wiring — transparent to all consumers of IOrderReader
builder.Services.AddScoped<SqlOrderRepository>();
builder.Services.AddScoped<IOrderReader>(sp =>
```
new CachingOrderReader(
sp.GetRequiredService<SqlOrderRepository>(),
sp.GetRequiredService<IHybridCache>()));



```


## KEY TAKEAWAYS

– Many classic GoF patterns are now language features in C# — don't
implement what the runtime gives you for free.
– Builder pattern prevents partially-constructed objects — use it for
complex configuration objects.
– Keyed services (.NET 8+) replace manual strategy factories — cleaner
and DI-friendly.



```
- 50 -
```


<a id='p51'></a>
<!-- Página 51 -->

```
C# 2026: Enterprise Mastery


```

– Mediator/CQRS separates command handling from API dispatch —
controllers become thin routing layers.
– Decorator pattern adds cross-cutting concerns (caching, logging,
metrics) transparently.
– Prefer composition over inheritance — C# records and interfaces
make this natural.




```
- 51 -
```


<a id='p52'></a>
<!-- Página 52 -->

```
C# 2026: Enterprise Mastery


```


## PART II — WRITING CODE THAT ENDURES


## CHAPTER 6




```
Domain-Driven Design with C#

```

"The heart of software is its ability to solve domain-related problems for its
```
users." — Eric Evans


```

Why DDD Matters at Scale
Domain-Driven Design is not a technology choice—it is a collaboration
strategy between developers and domain experts, and an architectural
discipline that aligns the software model closely with the business
problem it solves. At small scale, the investment in DDD may not be worth
it. At enterprise scale—multiple teams, complex business rules, multiple
bounded contexts—DDD's bounded contexts, aggregates, and ubiquitous
language are the difference between a system that can be evolved
confidently and one that becomes a maintenance nightmare within three
years.

Entities and Value Objects in C#
The Entity/Value Object distinction is the cornerstone of the DDD domain
model. Entities have identity that persists through state changes—an
Order is the same Order whether its status is Pending or Shipped. Value
Objects are defined entirely by their values and have no identity of their
own—the Money amount $100 USD is the same regardless of which
variable holds it. Modern C# records are a perfect fit for value objects.




```
- 52 -
```


<a id='p53'></a>
<!-- Página 53 -->

```
C# 2026: Enterprise Mastery


```

Listing: Chapter06/Entities.cs


// Value Object: immutable, structural equality, no
// database identity
public record Money(decimal Amount, string Currency)
{
```
public static readonly Money Zero = new(0m, "USD");

public Money Add(Money other)
{
EnsureSameCurrency(other);
return this with { Amount = Amount +
```

other.Amount };
```
}
public Money Subtract(Money other)
{
EnsureSameCurrency(other);
if (Amount < other.Amount)
throw new DomainException("Cannot result in
```

negative money.");
```
return this with { Amount = Amount -
```

other.Amount };
```
}
private void EnsureSameCurrency(Money other)
{
if (Currency != other.Currency)
throw new DomainException($"Currency mismatch:
```

{Currency} vs {other.Currency}");
```
}
```

}

// Entity: has identity, mutable state, domain behaviour
public class Order
{
```
private readonly List<OrderLine> _lines = [];

private Order() { } // EF Core navigation

public OrderId Id { get; private set; }
public CustomerId CustomerId { get; private set; }
public OrderStatus Status { get; private set; }




- 53 -
```


<a id='p54'></a>
<!-- Página 54 -->

```
C# 2026: Enterprise Mastery


public Money Total =>
```

_lines.Aggregate(Money.Zero, (sum, l) =>
sum.Add(l.Subtotal));
```
public IReadOnlyList<OrderLine> Lines =>
```

_lines.AsReadOnly();

```
private readonly List<IDomainEvent> _domainEvents = [];
public IReadOnlyList<IDomainEvent> DomainEvents =>
```

_domainEvents.AsReadOnly();
```
public void ClearDomainEvents() =>
```

_domainEvents.Clear();

```
public static Order Create(CustomerId customerId,
```

IReadOnlyList<OrderLineRequest> lines)
```
{
ArgumentNullException.ThrowIfNull(customerId,
```

nameof(customerId));
```
if (lines.Count == 0) throw new
```

DomainException("Order must have at least one line.");

```
var order = new Order
{
Id = OrderId.New(),
CustomerId = customerId,
Status = OrderStatus.Draft,
};
foreach (var req in lines)
order._lines.Add(OrderLine.Create(req));

order._domainEvents.Add(new
```

OrderCreatedEvent(order.Id, order.CustomerId));
```
return order;
}

public void Submit()
{
if (Status != OrderStatus.Draft)
throw new DomainException($"Cannot submit an
```

order in status {Status}.");
```
Status = OrderStatus.Submitted;
_domainEvents.Add(new OrderSubmittedEvent(Id));
}
```

}


```
- 54 -
```


<a id='p55'></a>
<!-- Página 55 -->

```
C# 2026: Enterprise Mastery



```

Aggregates: The Consistency Boundary
An Aggregate is a cluster of domain objects treated as a single unit for
data consistency. All modifications to objects within an aggregate must go
through the Aggregate Root—the public entry point. This rule enforces
invariants: the aggregate root is responsible for ensuring that the entire
cluster remains in a valid state after any operation. In the Order example
above, Order is the aggregate root. You never modify an OrderLine directly
—you call methods on Order that modify OrderLine while enforcing all
relevant rules.

## AGGREGATE BOUNDARIES: A RULE OF THUMB

As a rule of thumb, treat one aggregate as one transaction. When you find
yourself wanting to update two aggregates in a single database transaction,
pause and examine the boundary — it is often a sign that the aggregates
are drawn in the wrong place. Domain events achieving eventual
consistency between aggregates are frequently the cleaner design, though
there are legitimate exceptions, and some teams accept a multi-aggregate
transaction when the consistency requirement is strict.


Domain Events: Decoupled Side Effects
Listing: Chapter06/DomainEvents.cs


// Domain event — value object describing something that
// happened
public record OrderSubmittedEvent(OrderId OrderId) :
IDomainEvent
{
```
public DateTime OccurredAt { get; } = DateTime.UtcNow;
```

}

// Dispatcher: publish after the transaction commits
public class DomainEventDispatcher
{
```
private readonly IServiceProvider _sp;
public DomainEventDispatcher(IServiceProvider sp) =>
```

_sp = sp;




```
- 55 -
```


<a id='p56'></a>
<!-- Página 56 -->

```
C# 2026: Enterprise Mastery


public async Task
```

DispatchAsync(IReadOnlyList<IDomainEvent> events,
CancellationToken ct)
```
{
foreach (var evt in events)
{
var handlerType =
```

typeof(IDomainEventHandler<>).MakeGenericType(evt.GetType()
);
```
var handlers = _sp.GetServices(handlerType);
foreach (dynamic handler in handlers)
await handler.HandleAsync((dynamic)evt,
```

ct);
```
}
}
```

}

// Handler: runs outside the transaction — side effects
// isolated
public class SendOrderConfirmationOnSubmit :
IDomainEventHandler<OrderSubmittedEvent>
{
```
private readonly IOrderNotifier _notifier;
public SendOrderConfirmationOnSubmit(IOrderNotifier
```

notifier) => _notifier = notifier;

```
public async Task HandleAsync(OrderSubmittedEvent evt,
```

CancellationToken ct)
```
=> await
```

_notifier.SendSubmissionConfirmationAsync(evt.OrderId, ct);
}




Repository Pattern: Persistence Abstraction
Listing: Chapter06/Repository.cs


// Repository interface — lives in the Domain layer, knows
// nothing about SQL
public interface IOrderRepository
{
```
Task<Order?> FindByIdAsync(OrderId id,
```

CancellationToken ct);

```
- 56 -
```


<a id='p57'></a>
<!-- Página 57 -->

```
C# 2026: Enterprise Mastery


Task SaveAsync(Order order, CancellationToken ct);
```

}

// EF Core implementation — lives in the Infrastructure
// layer
public class EfOrderRepository : IOrderRepository
{
```
private readonly AppDbContext _db;
private readonly DomainEventDispatcher _dispatcher;

public EfOrderRepository(AppDbContext db,
```

DomainEventDispatcher dispatcher)
```
=> (_db, _dispatcher) = (db, dispatcher);

public Task<Order?> FindByIdAsync(OrderId id,
```

CancellationToken ct)
```
=> _db.Orders
.Include(o => o.Lines)
.FirstOrDefaultAsync(o => o.Id == id, ct);

public async Task SaveAsync(Order order,
```

CancellationToken ct)
```
{
// Attach only if the change tracker is not already
// tracking this entity.
// Calling Update() unconditionally marks every
// property modified and can
// clobber a more precise change set EF Core
// already holds for a tracked
// entity. Checking the state first keeps updates
// minimal and correct.
if (_db.Entry(order).State == EntityState.Detached)
_db.Orders.Update(order);

await _db.SaveChangesAsync(ct);

// Dispatch domain events AFTER the transaction
// commits
await _dispatcher.DispatchAsync(order.DomainEvents,
```

ct);
```
order.ClearDomainEvents();
}
```

}


```
- 57 -
```


<a id='p58'></a>
<!-- Página 58 -->

```
C# 2026: Enterprise Mastery


```


## KEY TAKEAWAYS

– Entities have identity; Value Objects are defined by their values —
model the distinction explicitly.
– Use C# records for Value Objects — you get structural equality,
immutability, and with-expressions for free.
– As a rule of thumb, treat one aggregate as one transaction boundary;
use domain events for cross-aggregate consistency.
– The aggregate root is the only public entry point — all mutations go
through it to enforce invariants.
– Repositories abstract the persistence layer from the domain — the
domain knows nothing about SQL or EF.
– Domain events published after transaction commit decouple side
effects cleanly.




```
- 58 -
```


<a id='p59'></a>
<!-- Página 59 -->

```
C# 2026: Enterprise Mastery


```


## PART III — PERFORMANCE AT EVERY LEVEL


## CHAPTER 7




```
Memory Management and the
Garbage Collector Deep Dive

```

"Premature optimisation is the root of all evil — but knowing how your
```
allocator works is not premature."


```

Understanding the .NET Memory Model
The .NET runtime uses a generational garbage collector (GC) that divides
the managed heap into three generations: Gen 0, Gen 1, and Gen 2. Gen 0
holds short-lived objects—allocated and collected most frequently. Gen 1
is a buffer between Gen 0 and Gen 2. Gen 2 holds long-lived objects and is
collected infrequently. The Large Object Heap (LOH) holds objects larger
than 85,000 bytes and is collected only during Gen 2 collections by default.
Understanding this model is essential to writing code that cooperates with
the GC rather than fighting it.

Allocation rate is the single most important performance metric for code
that runs under a garbage collector. If your hot path allocates 50 MB/s,
the GC must collect that 50 MB/s. Each collection stops the world (or at
least suspends the finaliser thread and marks phases) and compacts
memory. Reducing allocations in hot paths directly translates to reduced
GC pressure, fewer pauses, and higher throughput.




```
- 59 -
```


<a id='p60'></a>
<!-- Página 60 -->

```
C# 2026: Enterprise Mastery



```

Stack vs Heap: Where Your Data Lives
Listing: Chapter07/StackVsHeap.cs


// Value types (structs, record structs) avoid heap
// allocation in the common
// case: a local value type that is not captured or boxed
// stays off the heap.
public static void ProcessFrame(ReadOnlySpan<byte> frame)
{
```
// no heap allocation
Vector3 position = new Vector3(1.0f, 2.0f, 3.0f);
// no heap allocation
Quaternion rotation = Quaternion.Identity;
// All operations on position and rotation are
// allocation-free

// Transform: still allocation-free
var transformed =
```

Matrix4x4.CreateTranslation(position);
}

// Reference type instances are generally heap allocated
// Even small objects add GC pressure when allocated at
// high rates
public static void BadHotPath(IEnumerable<int> items)
{
```
foreach (var item in items)
{
// AVOID: Allocates a new Tuple on the heap for
// every item
var tuple = new Tuple<int, string>(item,
```

item.ToString());
```
}
```

}

public static void GoodHotPath(IEnumerable<int> items)
{
```
foreach (var item in items)
{
// GOOD: ValueTuple is a value type — typically
// allocation-free here.
// (A value type lives wherever it is declared: as

- 60 -
```


<a id='p61'></a>
<!-- Página 61 -->

```
C# 2026: Enterprise Mastery


// a local that the
// JIT does not need to box or capture, it stays
// off the heap.
// Capture it in a closure or box it, and it can
// move to the heap.)
var valueTuple = (item, item.ToString());
}
```

}




IDisposable, using, and Deterministic Cleanup
The IDisposable pattern is used to release unmanaged resources (file
handles, database connections, sockets, native memory) deterministically
—at the point the using block exits rather than waiting for the GC
finaliser. Modern C# with 'using' declarations (C# 8+) makes this even
cleaner. Understanding the difference between Dispose() and a finaliser is
critical for writing correct resource management code.
Listing: Chapter07/Disposable.cs


// GOOD: Correct IDisposable implementation with async
// support
public sealed class DatabaseConnectionPool : IDisposable,
IAsyncDisposable
{
```
private readonly SemaphoreSlim _semaphore;
private readonly List<DbConnection> _connections =
```

[];
```
private bool _disposed;

public DatabaseConnectionPool(int maxConnections)
=> _semaphore = new SemaphoreSlim(maxConnections,
```

maxConnections);

```
public async Task<DbConnection>
```

AcquireAsync(CancellationToken ct)
```
{
ObjectDisposedException.ThrowIf(_disposed, this);
await _semaphore.WaitAsync(ct);
return _connections.Count > 0
? _connections[^1] // reuse existing

- 61 -
```


<a id='p62'></a>
<!-- Página 62 -->

```
C# 2026: Enterprise Mastery


: CreateNewConnection();
}

// IDisposable — synchronous cleanup
public void Dispose()
{
if (_disposed) return;
_disposed = true;
foreach (var conn in _connections) conn.Dispose();
_semaphore.Dispose();
}

// IAsyncDisposable — preferred for async resources
public async ValueTask DisposeAsync()
{
if (_disposed) return;
_disposed = true;
foreach (var conn in _connections) await
```

conn.DisposeAsync();
```
_semaphore.Dispose();
}

private DbConnection CreateNewConnection() => throw new
```

NotImplementedException();
}

// Usage with 'using declaration' (C# 8+)
await using var pool = new DatabaseConnectionPool(10);
```
var conn = await pool.AcquireAsync(CancellationToken.None);




```

ArrayPool<T>: Reusing Buffers at Scale
When your code processes data in temporary buffers—network frames,
file chunks, serialisation scratch space—allocating a new array for every
operation creates enormous GC pressure. ArrayPool<T>.Shared provides a
thread-safe pool of reusable arrays that eliminates these allocations
entirely.




```
- 62 -
```


<a id='p63'></a>
<!-- Página 63 -->

```
C# 2026: Enterprise Mastery


```

Listing: Chapter07/ArrayPool.cs


// AVOID: Allocates 4KB on the heap for every call - at
// high request rates this is severe GC pressure
public static async Task<string> ReadResponseAsync(Stream
stream, CancellationToken ct)
{
```
// heap allocation every call
var buffer = new byte[4096];
var read = await stream.ReadAsync(buffer, ct);
return Encoding.UTF8.GetString(buffer, 0, read);
```

}

// GOOD: Rent and return — zero steady-state allocation
public static async Task<string> ReadResponseAsync(Stream
stream, CancellationToken ct)
{
```
var buffer = ArrayPool<byte>.Shared.Rent(4096);
try
{
var read = await stream.ReadAsync(buffer, ct);
return Encoding.UTF8.GetString(buffer, 0, read);
}
finally
{
ArrayPool<byte>.Shared.Return(buffer, clearArray:
```

false);
```
}
```

}

// GOOD: Even better: use RecyclableMemoryStream for
// variable-length payloads
// Microsoft.IO.RecyclableMemoryStream pools both arrays
// and MemoryStream instances
using var ms = _memoryStreamManager.GetStream("requestbody");
await request.Body.CopyToAsync(ms, ct);
// or process the MemoryStream directly
```
var payload = ms.ToArray();




- 63 -
```


<a id='p64'></a>
<!-- Página 64 -->

```
C# 2026: Enterprise Mastery



```

Diagnosing Memory Issues with dotnet-trace and
PerfView
Memory profiling in production is a skill that separates senior engineers
```
from everyone else. The dotnet-trace tool collects EventSource data with
```

minimal overhead and is safe to run against a live production process.
PerfView and the dotnet-dump tools provide heap analysis. For cloud
workloads, Application Insights and OpenTelemetry (covered in Chapter
19) expose GC metrics as time-series data.
Listing: Chapter07/MemoryDiagnostics.cs


# Collect a 30-second allocation trace from a running
process
dotnet-trace collect --process-id <PID> \
```
--providers Microsoft-Windows-DotNETRuntime:0x1:5 \
--duration 00:00:30

```

# Dump a heap snapshot for offline analysis
dotnet-dump collect --process-id <PID>

# Analyse a dump: find the top allocated types
dotnet-dump analyze <dump-file>
> dumpheap -stat
> dumpheap -type System.String -min 10000 # strings >

## 10KB


# In code: monitor GC via EventListener (production-safe)
```
var gcInfo = GC.GetGCMemoryInfo();
var heapSizeMb = gcInfo.HeapSizeBytes / 1_048_576.0;
var gen2CollectCount = GC.CollectionCount(2);



```


## KEY TAKEAWAYS

```
– The generational GC collects Gen0 most frequently — keep short-lived
```

objects truly short-lived.
```
– Allocation rate is the key GC metric — reducing it directly reduces
```

latency and improves throughput.
```
– Prefer structs and record structs for small, short-lived data to avoid
```

heap allocation.
```
- 64 -
```


<a id='p65'></a>
<!-- Página 65 -->

```
C# 2026: Enterprise Mastery


```

– Always implement both IDisposable and IAsyncDisposable for
async-aware resources.
– ArrayPool<T>.Shared eliminates buffer allocations in I/O-intensive
hot paths.
– Use dotnet-trace and dotnet-dump to diagnose memory issues in
production safely.




```
- 65 -
```


<a id='p66'></a>
<!-- Página 66 -->

```
C# 2026: Enterprise Mastery


```


## PART III — PERFORMANCE AT EVERY LEVEL


## CHAPTER 8




```
Span<T>, Memory<T>, and
Zero-Alloca,on Pa'erns

"The fastest code is the code that does not allocate."


```

What Span<T> Is and Why It Exists
Span<T> is a ref struct introduced in .NET Core 2.1 that represents a
contiguous region of arbitrary memory—a segment of an array, a
stack-allocated block, or even unmanaged native memory—without
copying it. Before Span<T>, parsing a substring meant calling Substring()
which allocates a new string on the heap. Span<T> enables the same
operation with zero allocation by working with a view into the original
memory.
Listing: Chapter08/Span.cs


// AVOID: Old approach: Substring allocates on every parse
// operation
public static (string User, string Domain)
ParseEmailOld(string email)
{
```
var atIndex = email.IndexOf('@');
// allocation!
var user = email.Substring(0, atIndex);
// allocation!
var domain = email.Substring(atIndex + 1);
return (user, domain);
```

}

// GOOD: Span<T> approach: zero allocation — works with


```
- 66 -
```


<a id='p67'></a>
<!-- Página 67 -->

```
C# 2026: Enterprise Mastery


```

// slices of existing memory
public static (ReadOnlySpan<char> User, ReadOnlySpan<char>
Domain)
```
ParseEmail(ReadOnlySpan<char> email)
```

{
```
var atIndex = email.IndexOf('@');
if (atIndex < 0) throw new FormatException("Invalid
```

email.");
```
return (email[..atIndex], email[(atIndex + 1)..]);
```

}

// Usage: no allocation at any point
ReadOnlySpan<char> raw = "victor@example.com".AsSpan();
```
var (user, domain) = ParseEmail(raw);
```

Console.WriteLine(user.ToString()); // "victor"
Console.WriteLine(domain.ToString()); // "example.com"

// Real-world parsing: extracting fields from a log line
public static void ParseLogLine(ReadOnlySpan<char> line,
```
out ReadOnlySpan<char> timestamp, out
```

ReadOnlySpan<char> level,
```
out ReadOnlySpan<char> message)
```

{
```
// Format: "2026-01-01T12:00:00Z [INFO] Message content
// here"
var firstSpace = line.IndexOf(' ');
timestamp = line[..firstSpace];
var rest = line[(firstSpace + 1)..];
var closeB = rest.IndexOf(']');
level = rest[1..closeB]; // skip '['
message = rest[(closeB + 2)..];
```

}




stackalloc and High-Performance Buffers
Listing: Chapter08/Stackalloc.cs


// Stack-allocate small buffers — completely avoids heap
// allocation
public static bool TryEncodeBase64(
```
ReadOnlySpan<byte> input,
Span<byte> output,

- 67 -
```


<a id='p68'></a>
<!-- Página 68 -->

```
C# 2026: Enterprise Mastery


out int bytesWritten)
```

{
```
// For small inputs, use a stack-allocated temporary
// buffer
if (input.Length <= 256)
{
Span<byte> temp = stackalloc
```

byte[Base64.GetMaxEncodedToUtf8Length(input.Length)];
```
Base64.EncodeToUtf8(input, temp, out _, out
```

bytesWritten);
```
temp[..bytesWritten].CopyTo(output);
return true;
}
// Fall back to ArrayPool for larger inputs
var rented =
```

ArrayPool<byte>.Shared.Rent(Base64.GetMaxEncodedToUtf8Lengt
h(input.Length));
```
try
{
Base64.EncodeToUtf8(input, rented, out _, out
```

bytesWritten);
```
rented.AsSpan(0, bytesWritten).CopyTo(output);
return true;
}
finally
{
ArrayPool<byte>.Shared.Return(rented);
}
```

}




Memory<T> for Asynchronous Scenarios
Span<T> is a ref struct, which means it cannot be stored on the heap,
cannot be used in async methods that cross await boundaries, and cannot
be a field in a class. Memory<T> solves this by providing a
heap-compatible, non-ref wrapper around the same memory. Use
ReadOnlySpan<T> and Span<T> in synchronous code; use Memory<T>
when you need to pass buffer ownership across async boundaries.




```
- 68 -
```


<a id='p69'></a>
<!-- Página 69 -->

```
C# 2026: Enterprise Mastery


```

Listing: Chapter08/MemoryT.cs


// Memory<T> can be awaited across async boundaries
public async Task<int> ProcessBufferAsync(
```
Memory<byte> buffer, CancellationToken ct)
```

{
```
// Can await here — Memory<T> is not a ref struct
var bytesRead = await _stream.ReadAsync(buffer, ct);

// Get a Span<T> view for synchronous processing within
// this method
var slice = buffer.Span[..bytesRead];
return ProcessSync(slice);
```

}

// IMemoryOwner<T>: manage buffer lifetime with a clear
// ownership model
public async Task<ProcessingResult>
ProcessLargePayloadAsync(
```
Stream source, CancellationToken ct)
```

{
```
// MemoryPool<T> provides pooled, owned memory
using IMemoryOwner<byte> owner =
```

MemoryPool<byte>.Shared.Rent(64 * 1024);
```
var bytesRead = await source.ReadAsync(owner.Memory,
```

ct);
```
return await AnalyseAsync(owner.Memory[..bytesRead],
```

ct);
```
// owner.Dispose() returns memory to the pool at end of
// using block
```

}




ValueTask: Eliminating Task Allocations
Listing: Chapter08/ValueTask.cs


// ValueTask avoids allocation when the result is available
// synchronously
// Use when: the common case completes synchronously (e.g.,
// cache hit)
// Avoid when: the method is always async — overhead


```
- 69 -
```


<a id='p70'></a>
<!-- Página 70 -->

```
C# 2026: Enterprise Mastery


```

// exceeds benefit

public interface ICacheService
{
```
// ValueTask<T> is appropriate here — cache hits are
// synchronous
ValueTask<T?> GetAsync<T>(string key, CancellationToken
```

ct);
}

public class HybridCacheService : ICacheService
{
```
private readonly IMemoryCache _l1;
private readonly IDistributedCache _l2;

public async ValueTask<T?> GetAsync<T>(string key,
```

CancellationToken ct)
```
{
// L1 hit: synchronous — ValueTask does NOT
// allocate
if (_l1.TryGetValue<T>(key, out var cached))
return cached;

// L2 hit: asynchronous — ValueTask wraps a Task
var bytes = await _l2.GetAsync(key, ct);
if (bytes is not null)
return Deserialise<T>(bytes);

return default;
}

private static T? Deserialise<T>(byte[] bytes) =>
JsonSerializer.Deserialize<T>(bytes);
```

}

// CRITICAL: Never await a ValueTask more than once — store
// it in a variable
ValueTask<Order?> task =
_cache.GetAsync<Order>("order:123", ct);
```
var order1 = await task; // GOOD:
```

// var order2 = await task; // AVOID: Undefined behaviour —
// never double-await




```
- 70 -
```


<a id='p71'></a>
<!-- Página 71 -->

```
C# 2026: Enterprise Mastery


```


## KEY TAKEAWAYS

– Span<T> provides zero-allocation views into existing memory —
essential for parsing and I/O hot paths.
– stackalloc allocates on the stack for small buffers; pair with
ArrayPool<T> for larger ones.
– Memory<T> is the async-compatible counterpart to Span<T> — use it
when crossing await boundaries.
– IMemoryOwner<T> from MemoryPool<T> provides clear ownership
semantics for rented buffers.
– ValueTask<T> eliminates Task allocation for methods with
synchronous fast paths (cache hits, etc.).
– Never await a ValueTask twice — it has value semantics and the
result is only valid once.




```
- 71 -
```


<a id='p72'></a>
<!-- Página 72 -->

```
C# 2026: Enterprise Mastery


```


## PART III — PERFORMANCE AT EVERY LEVEL


## CHAPTER 9




```
Async/Await Mastery and
Concurrency at Scale

```

"Concurrency is not parallelism, but at a million requests per second, both
```
matter."


```

The Async State Machine: What the Compiler
Actually Does
Understanding what the compiler generates for async methods is
essential to using them correctly. When you mark a method async, the
compiler transforms it into a state machine—a struct that captures the
method's local variables and continuation logic. Each await becomes a
state transition. If the awaited task is already completed when execution
reaches the await point, the state machine advances synchronously
without allocating a new Task. If it is not completed, the state machine
suspends and the continuation is scheduled to run when the task
completes.

The practical implications: async methods should not be used for trivially
synchronous operations because the state machine overhead—even when
minimal—adds up at high call rates. On the other hand, async is essential
for any I/O-bound operation because it releases the thread back to the
pool during the wait, allowing the same thread to serve hundreds of
concurrent requests.




```
- 72 -
```


<a id='p73'></a>
<!-- Página 73 -->

```
C# 2026: Enterprise Mastery



```

ConfigureAwait(false): When It Matters and
When It Doesn't
Listing: Chapter09/ConfigureAwait.cs


// ConfigureAwait(false) tells the runtime: don't capture
// the current SynchronizationContext
// This matters in library code and in WinForms/WPF apps.
// In ASP.NET Core there is NO SynchronizationContext —
// ConfigureAwait(false) is a no-op
// there, but it's still good practice in library code.

// AVOID: Library code that may deadlock if called from a
// context with SynchronizationContext
public async Task<string> GetDataAsync(string url)
{
```
using var client = new HttpClient();
// captures context
var response = await client.GetAsync(url);
// resumes on original thread
return await response.Content.ReadAsStringAsync();
```

}

// GOOD: Library code — always use ConfigureAwait(false) in
// library projects
public async Task<string> GetDataAsync(string url,
CancellationToken ct)
{
```
using var client = new HttpClient();
var response = await client.GetAsync(url,
```

ct).ConfigureAwait(false);
```
return await
```

response.Content.ReadAsStringAsync(ct).ConfigureAwait(false
);
}

// Rule of thumb:
// - Application code (ASP.NET Core, console apps): omit
// ConfigureAwait(false)
// - Library code (NuGet packages, shared infrastructure):
// always use ConfigureAwait(false)



```
- 73 -
```


<a id='p74'></a>
<!-- Página 74 -->

```
C# 2026: Enterprise Mastery



```

CancellationToken: The Non-Negotiable in 2026
Every async method that performs I/O, waiting, or potentially
long-running work must accept a CancellationToken parameter. This is
not optional in enterprise code. When a client disconnects, when a request
times out, when a server begins graceful shutdown—CancellationToken is
the mechanism that stops in-flight work cooperatively and releases
resources. A system with ten million requests per day that ignores
CancellationToken will accumulate thread-pool exhaustion silently.
Listing: Chapter09/CancellationToken.cs


// GOOD: CancellationToken threaded through every async
// call
public async Task<IReadOnlyList<Product>>
GetRecommendationsAsync(
```
CustomerId customerId,
// <-- always the last parameter, by convention
CancellationToken ct)
```

{
```
ct.ThrowIfCancellationRequested();

var profile = await
```

_profileService.GetAsync(customerId, ct);
```
if (profile is null) return [];

var candidates = await _catalogue.SearchAsync(
new CatalogueQuery(profile.PreferredCategories),
```

ct);

```
var scores = await
```

_scoringService.ScoreAsync(candidates, profile, ct);

```
return scores
.OrderByDescending(s => s.Score)
.Take(10)
.Select(s => s.Product)
.ToList();
```

}

// Composing tokens: request token + operation timeout



```
- 74 -
```


<a id='p75'></a>
<!-- Página 75 -->

```
C# 2026: Enterprise Mastery


```

public async Task<string> CallExternalApiAsync(string url,
CancellationToken requestCt)
{
```
// Combine: cancel if request cancelled OR if call
// exceeds 5 seconds
using var cts =
```

CancellationTokenSource.CreateLinkedTokenSource(requestCt);
```
cts.CancelAfter(TimeSpan.FromSeconds(5));

return await _httpClient.GetStringAsync(url,
```

cts.Token);
}

// Graceful shutdown: ASP.NET Core provides the token via
// IHostApplicationLifetime
app.MapGet("/long-work", async (IHostApplicationLifetime
lifetime, CancellationToken ct) =>
{
```
using var cts =
```

CancellationTokenSource.CreateLinkedTokenSource(
```
ct, lifetime.ApplicationStopping);

await DoLongWorkAsync(cts.Token);
return Results.Ok();
```

});




Channels: High-Throughput Producer-Consumer
Pipelines
System.Threading.Channels, introduced in .NET Core 3.0 and refined
through subsequent releases, provides a high-performance, lock-free
producer-consumer data structure. It is the correct tool for intra-process
pipelines where one set of workers produces items faster than they can be
processed and you need backpressure, buffering, and clean cancellation
support.




```
- 75 -
```


<a id='p76'></a>
<!-- Página 76 -->

```
C# 2026: Enterprise Mastery


```

Listing: Chapter09/Channels.cs


// Bounded channel: built-in backpressure — producer waits
// when consumer falls behind
public class OrderProcessingPipeline
{
```
private readonly Channel<OrderMessage> _channel;
private readonly ILogger _log;

public
```

OrderProcessingPipeline(ILogger<OrderProcessingPipeline>
log)
```
{
_log = log;
_channel = Channel.CreateBounded<OrderMessage>(
new BoundedChannelOptions(capacity: 1000)
{
// backpressure
FullMode =
```

BoundedChannelFullMode.Wait,
```
SingleReader = false,
SingleWriter = false,
});
}

// Producer side
public ValueTask EnqueueAsync(OrderMessage message,
```

CancellationToken ct)
```
=> _channel.Writer.WriteAsync(message, ct);

// Consumer side — run multiple workers concurrently
public async Task RunConsumersAsync(int workerCount,
```

CancellationToken ct)
```
{
var workers = Enumerable.Range(0, workerCount)
.Select(i => RunWorkerAsync(i, ct))
.ToArray();
await Task.WhenAll(workers);
}

private async Task RunWorkerAsync(int workerId,
```

CancellationToken ct)
```
{


- 76 -
```


<a id='p77'></a>
<!-- Página 77 -->

```
C# 2026: Enterprise Mastery


await foreach (var message in
```

_channel.Reader.ReadAllAsync(ct))
```
{
try
{
await ProcessMessageAsync(message, ct);
}
catch (Exception ex) when (ex is not
```

OperationCanceledException)
```
{
_log.LogError(ex, "Worker {WorkerId} failed
```

processing {MessageId}",
```
workerId, message.Id);
}
}
}

public void Complete() => _channel.Writer.Complete();

private static Task ProcessMessageAsync(OrderMessage m,
```

CancellationToken ct)
```
=> Task.CompletedTask; // real implementation
```

}




Parallel.ForEachAsync: Bounded Parallelism
Listing: Chapter09/ParallelAsync.cs


// Process up to 8 items concurrently, respecting
// cancellation
public static async Task ProcessOrdersBatchAsync(
```
IAsyncEnumerable<Order> orders,
CancellationToken ct)
```

{
```
var options = new ParallelOptions
{
MaxDegreeOfParallelism = 8,
CancellationToken = ct
};

await Parallel.ForEachAsync(orders, options, async
```

(order, token) =>

```
- 77 -
```


<a id='p78'></a>
<!-- Página 78 -->

```
C# 2026: Enterprise Mastery


{
await ProcessSingleOrderAsync(order, token);
});
```

}

// SemaphoreSlim: control concurrency without
// Parallel.ForEachAsync
public static async Task ProcessWithThrottleAsync(
```
IReadOnlyList<Guid> ids, int maxConcurrent,
```

CancellationToken ct)
{
```
using var throttle = new SemaphoreSlim(maxConcurrent,
```

maxConcurrent);

```
var tasks = ids.Select(async id =>
{
await throttle.WaitAsync(ct);
try { await ProcessAsync(id, ct); }
finally { throttle.Release(); }
});

await Task.WhenAll(tasks);
```

}

private static Task ProcessSingleOrderAsync(Order o,
CancellationToken ct) => Task.CompletedTask;
private static Task ProcessAsync(Guid id, CancellationToken
ct) => Task.CompletedTask;




## KEY TAKEAWAYS

– Async state machines advance synchronously when the task is already
complete — no overhead for fast paths.
– ConfigureAwait(false) is mandatory in library code; optional (but
harmless) in ASP.NET Core apps.
– CancellationToken is non-negotiable in every async I/O method in
2026 production code.
– Combine tokens with CreateLinkedTokenSource to enforce
per-operation timeouts alongside request cancellation.
– System.Threading.Channels is the correct tool for high-throughput
producer-consumer pipelines.

```
- 78 -
```


<a id='p79'></a>
<!-- Página 79 -->

```
C# 2026: Enterprise Mastery


```

– Parallel.ForEachAsync provides clean, cancellable bounded
parallelism with elegant syntax.




```
- 79 -
```


<a id='p80'></a>
<!-- Página 80 -->

```
C# 2026: Enterprise Mastery


```


## PART III — PERFORMANCE AT EVERY LEVEL


## CHAPTER 10




LINQ: Master It, Then Know When
```
to Stop

```

"LINQ is elegant but not free — every method call is a potential allocation
```
and a potential N+1."


```

LINQ's Deferred Execution Model
LINQ's deferred execution is its most powerful feature and its most
dangerous footgun. When you write a LINQ query over an
IEnumerable<T>, nothing executes. The query is represented as an object
graph of iterator machines that execute lazily when enumerated. This
enables composable, readable pipelines. It also means that enumerating
the same query twice executes it twice, that queries over IQueryable<T>
translate to SQL but only when materialised, and that adding a ToList() or
ToArray() at the wrong place can accidentally materialise a million-row
database table into memory.
Listing: Chapter10/LinqDeferred.cs


```
var query = _db.Orders
.Where(o => o.Status == OrderStatus.Pending)
// Not executed yet — IQueryable
.Select(o => new { o.Id, o.CustomerId });

```

// AVOID: Executes query twice — two round trips to the
// database
```
var count = query.Count();
var first = query.FirstOrDefault();

```

// GOOD: Materialise once — one round trip, then work in

```
- 80 -
```


<a id='p81'></a>
<!-- Página 81 -->

```
C# 2026: Enterprise Mastery


```

// memory
// ONE SQL query
```
var results = await query.ToListAsync(ct);
var count2 = results.Count;
var first2 = results.FirstOrDefault();

```

// AVOID: Accidental full table scan: filtering in C#
// instead of SQL
// materialises entire table!
```
var active = _db.Orders.ToList()
.Where(o => o.Status ==
```

OrderStatus.Pending);

// GOOD: Filter in the database — only Pending rows
// transferred
```
var activeSql = await _db.Orders
.Where(o => o.Status == OrderStatus.Pending)
.ToListAsync(ct);




```

When LINQ Hurts Performance
LINQ is designed for readability and composability, not maximum
throughput. In hot paths—methods called millions of times per second—
the delegate allocations, iterator boxing, and intermediate collection
creations add up to measurable overhead. Benchmarking consistently
shows that hand-written loops outperform equivalent LINQ queries by 2–
10x in tight computation-heavy scenarios.
Listing: Chapter10/LinqPerformance.cs


// BenchmarkDotNet results (representative, varies by
// hardware):
// | Method | Mean | Allocated |
// | LinqSum | 45.2 us | 640 B |
// | ForLoopSum | 8.1 us | 0 B |
// | SpanSum | 3.4 us | 0 B |

// AVOID: LINQ sum: lambda allocation + iterator overhead
int sumLinq = numbers.Where(n => n > 0).Sum();

// GOOD: For loop: no allocation, branch predictor-friendly

```
- 81 -
```


<a id='p82'></a>
<!-- Página 82 -->

```
C# 2026: Enterprise Mastery


```

int sumLoop = 0;
foreach (var n in numbers)
```
if (n > 0) sumLoop += n;

```

// GOOD: Best: Span<T> + vectorisation opportunity
int SumPositive(ReadOnlySpan<int> span)
{
```
int sum = 0;
foreach (var n in span)
if (n > 0) sum += n;
return sum;
```

}

// Rule: use LINQ for clarity in non-hot paths
// use loops/Span in hot paths (> 10,000 calls/sec)




IEnumerable vs IQueryable: The Critical
Difference
Listing: Chapter10/QueryableVsEnumerable.cs


// IQueryable<T>: expression trees — translated to SQL or
// other query languages
// IEnumerable<T>: delegates — executed in memory (C#)

// The mix-up that costs teams dearly:
IQueryable<Order> dbQuery = _db.Orders.Where(o => o.Status
== OrderStatus.Pending);

// GOOD: Stay in IQueryable — condition translated to SQL
// WHERE clause
```
var sqlFiltered = await dbQuery
// SQL: WHERE created_at > ...
.Where(o => o.CreatedAt > DateTime.UtcNow.AddDays(-7))
.ToListAsync(ct);

```

// AVOID: Materialise accidentally — AsEnumerable() pulls
// every row to memory first
```
var cSharpFiltered = dbQuery
// <<< query executes HERE; all rows loaded into memory
.AsEnumerable()

- 82 -
```


<a id='p83'></a>
<!-- Página 83 -->

```
C# 2026: Enterprise Mastery


// in-memory C# filter
.Where(o => o.CreatedAt > DateTime.UtcNow.AddDays(-7))
// synchronous — the data is already in memory
.ToList();

```

// Why this is a trap:
// - After AsEnumerable(), you are in LINQ-to-Objects, not
// LINQ-to-Entities.
// - The WHERE never reaches SQL; the database returns the
// whole table.
// - There is no ToListAsync() here because IEnumerable<T>
// has no async
// enumeration; the await belongs on the database call, not
// the C# filter.
//
// AsEnumerable() has legitimate uses (a condition EF Core
// cannot translate),
// but place it AFTER every filter the database can run,
// never before.




## KEY TAKEAWAYS

– Deferred execution means LINQ queries run on each enumeration —
materialise once with ToList/ToArray.
– Never call ToList() before filtering — you'll load the entire table into
memory.
– Hand-written loops can outperform LINQ in tight hot paths —
measure before rewriting.
– Keep IQueryable filters before AsEnumerable — let the database do
the heavy filtering.
– LINQ is excellent for readability; reserve manual Span<T> loops for
measured hot paths.
– Use CountBy and AggregateBy (.NET 9) to replace GroupBy +
ToDictionary two-pass patterns.




```
- 83 -
```


<a id='p84'></a>
<!-- Página 84 -->

```
C# 2026: Enterprise Mastery


```


## PART IV — ENTERPRISE PATTERNS & ARCHITECTURE


## CHAPTER 11




Minimal APIs and High-Performance
```
Web

```

"An endpoint that does one thing quickly is worth more than a controller
```
that does ten things slowly."


```

Where Minimal APIs Fit
Minimal APIs, introduced in .NET 6 and matured through subsequent
releases, are often preferred for new lightweight endpoints and
microservices. They have fewer pipeline steps, no hidden conventions,
and are straightforward to test in isolation. MVC controllers remain a
perfectly valid — and often better — choice for larger applications: they
offer mature conventions for model binding, filters, and action results
that pay off once an API has many endpoints and cross-cutting concerns.
The two styles also coexist in one project. Choose Minimal APIs when you
want explicitness and a small surface area; choose controllers when you
want structure and convention. This is a trade-off, not a verdict.
Listing: Chapter11/MinimalApiComplete.cs


// Complete, production-quality minimal API endpoint with
// all enterprise concerns
```
var builder = WebApplication.CreateBuilder(args);

```

// Services
builder.Services.AddScoped<IOrderService, OrderService>();
builder.Services.AddHybridCache();
builder.Services.AddRateLimiter(cfg =>
{


```
- 84 -
```


<a id='p85'></a>
<!-- Página 85 -->

```
C# 2026: Enterprise Mastery


cfg.GlobalLimiter =
```

PartitionedRateLimiter.Create<HttpContext, string>(ctx =>
```
RateLimitPartition.GetFixedWindowLimiter(
partitionKey: ctx.User.Identity?.Name ??
```

ctx.Connection.RemoteIpAddress?.ToString() ?? "anon",
```
factory: _ => new FixedWindowRateLimiterOptions
{
PermitLimit = 100, Window =
```

TimeSpan.FromMinutes(1)
```
}));
cfg.RejectionStatusCode = 429;
```

});
builder.Services.AddOutputCache(cfg =>
```
cfg.AddPolicy("orders", p =>
```

p.Expire(TimeSpan.FromSeconds(30))));

```
var app = builder.Build();
```

app.UseRateLimiter();
app.UseOutputCache();

// Endpoint group with shared prefix and filters
```
var orders = app.MapGroup("/api/v1/orders")
.RequireAuthorization()
.AddEndpointFilter<ValidationFilter>()
.WithTags("Orders");

```

orders.MapGet("{id:guid}", async (
```
Guid id, IOrderService svc, CancellationToken ct) =>
```

{
```
var order = await svc.GetByIdAsync(new OrderId(id),
```

ct);
```
return order is null
? Results.NotFound()
: Results.Ok(order);
```

})
.CacheOutput("orders")
.WithName("GetOrderById")
.Produces<OrderResponse>()
.Produces(404)
.WithOpenApi();

orders.MapPost("/", async (
```
CreateOrderRequest req,
IOrderService svc,

- 85 -
```


<a id='p86'></a>
<!-- Página 86 -->

```
C# 2026: Enterprise Mastery


CancellationToken ct) =>
```

{
```
var id = await svc.CreateAsync(req, ct);
return Results.CreatedAtRoute("GetOrderById", new
```

{ id }, id);
})
.Produces<OrderId>(201)
.Produces<ValidationProblemDetails>(400)
.WithOpenApi();




Endpoint Filters: Cross-Cutting Concerns Without
Controllers
Listing: Chapter11/EndpointFilters.cs


// Endpoint filter: validation using FluentValidation or
// DataAnnotations
public class ValidationFilter<TRequest> : IEndpointFilter
{
```
private readonly IValidator<TRequest> _validator;
public ValidationFilter(IValidator<TRequest> validator)
=> _validator = validator;

public async ValueTask<object?> InvokeAsync(
EndpointFilterInvocationContext ctx,
EndpointFilterDelegate next)
{
if
```

(ctx.Arguments.OfType<TRequest>().FirstOrDefault() is not {
} request)
```
return await next(ctx);

var result = await
```

_validator.ValidateAsync(request);
```
if (!result.IsValid)
return
```

Results.ValidationProblem(result.ToDictionary());

```
return await next(ctx);
}
```

}

```
- 86 -
```


<a id='p87'></a>
<!-- Página 87 -->

```
C# 2026: Enterprise Mastery




```

// Timing filter: log endpoint duration
public class TimingFilter : IEndpointFilter
{
```
private readonly ILogger<TimingFilter> _log;
public TimingFilter(ILogger<TimingFilter> log) => _log
```

= log;

```
public async ValueTask<object?> InvokeAsync(
EndpointFilterInvocationContext ctx,
EndpointFilterDelegate next)
{
var sw = Stopwatch.StartNew();
try
{
return await next(ctx);
}
finally
{
_log.LogInformation("Endpoint {Name} completed
```

in {ElapsedMs}ms",
```
ctx.HttpContext.GetEndpoint()?.DisplayName,
sw.ElapsedMilliseconds);
}
}
```

}




Rate Limiting at Scale: 1 Million Users
At scale, rate limiting is not a feature—it is infrastructure. The rate
limiting middleware in .NET 7+ offers four built-in algorithms: Fixed
Window, Sliding Window, Token Bucket, and Concurrency Limiter. For
99% of use cases, a partitioned Fixed Window limiter (per user or per IP)
with a Token Bucket for burst tolerance is the right combination.
Redis-backed rate limiting is required when you run more than one
instance.

## DISTRIBUTED RATE LIMITING WARNING

For distributed rate limiting across multiple instances, use a Redis-backed
IDistributedRateLimiter implementation. The in-memory limiter only


```
- 87 -
```


<a id='p88'></a>
<!-- Página 88 -->

```
C# 2026: Enterprise Mastery


```

protects a single instance — in a Kubernetes deployment with 10 replicas,
10x your intended limit will pass through if you rely on in-memory
limiting alone.


## KEY TAKEAWAYS

– Minimal APIs are faster, more explicit, and easier to test than MVC
controllers for new code.
– MapGroup() shares prefixes, auth, filters, and tags — eliminate
repetition across related endpoints.
– Output caching with CacheOutput() reduces downstream load
dramatically for read-heavy endpoints.
– Endpoint filters implement cross-cutting concerns (validation, timing,
auth) without ActionFilter magic.
– Rate limiting is infrastructure — always use Redis-backed limiting in
multi-instance deployments.
– Always add .WithOpenApi() to every endpoint — documentation is
part of the contract.




```
- 88 -
```


<a id='p89'></a>
<!-- Página 89 -->

```
C# 2026: Enterprise Mastery


```


## PART IV — ENTERPRISE PATTERNS & ARCHITECTURE


## CHAPTER 12




```
gRPC, SignalR, and Real-Time at
Scale

"Not every client-server conversation is a request-response pair."


```

gRPC vs REST vs GraphQL: The 2026 Decision
Guide
Three transport/protocol patterns dominate enterprise API design in
2026: REST (JSON over HTTP), gRPC (Protocol Buffers over HTTP/2), and
GraphQL (query language over HTTP). Each has a legitimate home. REST
is the right choice for public-facing APIs consumed by web browsers and
third-party developers—it is universally understood, debuggable with a
browser, and cacheable at the HTTP layer. gRPC is the right choice for
internal service-to-service communication where performance matters—
Protocol Buffers are 5–10x smaller than equivalent JSON, HTTP/2
multiplexes streams, and strongly typed generated clients eliminate API
drift. GraphQL solves a specific problem: when clients have wildly
different data-fetching requirements that make REST's fixed response
shapes inefficient. Use it deliberately, not by default.
Listing: Chapter12/orders.proto


// gRPC: define the contract in .proto files — source
// generator creates C# classes
syntax = "proto3";
```
package orders.v1;

```

service OrderService {


```
- 89 -
```


<a id='p90'></a>
<!-- Página 90 -->

```
C# 2026: Enterprise Mastery


rpc GetOrder(GetOrderRequest) returns
```

(OrderResponse);
```
// server streaming
rpc ListOrders(ListRequest) returns (stream
```

OrderResponse);
```
rpc CreateOrder(CreateRequest) returns
```

(OrderResponse);
```
// client streaming
rpc BatchCreate(stream CreateRequest) returns
```

(BatchResult);
}

message GetOrderRequest { string order_id = 1; }
message OrderResponse {
```
string order_id = 1;
string customer_id = 2;
double total_amount = 3;
string status = 4;
int64 created_at = 5; // Unix timestamp (UTC)
```

}



Listing: Chapter12/OrderGrpcService.cs


// C# gRPC service implementation
public class OrderGrpcService :
OrderService.OrderServiceBase
{
```
private readonly IOrderReader _reader;
public OrderGrpcService(IOrderReader reader) => _reader
```

= reader;

```
public override async Task<OrderResponse> GetOrder(
GetOrderRequest request,
ServerCallContext context)
{
var order = await _reader.GetByIdAsync(
new OrderId(Guid.Parse(request.OrderId)),
context.CancellationToken);

if (order is null)
{



- 90 -
```


<a id='p91'></a>
<!-- Página 91 -->

```
C# 2026: Enterprise Mastery


var metadata = new Metadata {{ "order-id",
```

request.OrderId }};
```
throw new RpcException(new
```

Status(StatusCode.NotFound,
```
$"Order {request.OrderId} not found"),
```

metadata);
```
}
return MapToResponse(order);
}

// Server streaming: client receives a stream of orders
public override async Task ListOrders(
ListRequest request,
IServerStreamWriter<OrderResponse> responseStream,
ServerCallContext context)
{
var orders = await _reader.GetByCustomerAsync(
new CustomerId(Guid.Parse(request.CustomerId)),
context.CancellationToken);

foreach (var order in orders)
{

```

context.CancellationToken.ThrowIfCancellationRequested();
```
await
```

responseStream.WriteAsync(MapToResponse(order));
```
}
}

private static OrderResponse MapToResponse(Order o) =>
```

new()
```
{
OrderId = o.Id.ToString(),
CustomerId = o.CustomerId.ToString(),
TotalAmount= (double)o.Total.Amount,
Status = o.Status.ToString(),
CreatedAt = new
```

DateTimeOffset(o.CreatedAt).ToUnixTimeSeconds(),
```
};
```

}




```
- 91 -
```


<a id='p92'></a>
<!-- Página 92 -->

```
C# 2026: Enterprise Mastery



```

SignalR for Real-Time Features
SignalR provides real-time bidirectional communication between server
and clients, automatically negotiating the best transport (WebSockets,
Server-Sent Events, Long Polling). In 2026, with WebSockets universally
supported, SignalR consistently uses WebSockets for connected clients.
For a system with many concurrent clients, the backplane (Redis
Pub/Sub) is essential—it allows messages published on one server
instance to reach clients connected to any other instance.
Listing: Chapter12/SignalR.cs


// Hub — the server-side entry point for real-time
// connections
[Authorize]
public class OrderHub : Hub
{
```
private readonly IOrderReader _reader;
public OrderHub(IOrderReader reader) => _reader =
```

reader;

```
// Client calls this to subscribe to updates for a
// specific order
public async Task SubscribeToOrder(string orderId)
{
var groupName = $"order:{orderId}";
await Groups.AddToGroupAsync(Context.ConnectionId,
```

groupName);
```
}

public override async Task OnConnectedAsync()
{
// Add to the customer's personal group for
// directed messages
var customerId =
```

Context.User?.FindFirst("sub")?.Value;
```
if (customerId is not null)
await
```

Groups.AddToGroupAsync(Context.ConnectionId, $"customer:
{customerId}");
```
await base.OnConnectedAsync();
}

- 92 -
```


<a id='p93'></a>
<!-- Página 93 -->

```
C# 2026: Enterprise Mastery


```

}

// Publishing updates from a background service
public class OrderStatusUpdater
{
```
private readonly IHubContext<OrderHub> _hub;
public OrderStatusUpdater(IHubContext<OrderHub> hub) =>
```

_hub = hub;

```
public async Task NotifyStatusChangeAsync(Order order,
```

CancellationToken ct)
```
{
var message = new
```

OrderStatusUpdate(order.Id.ToString(),
order.Status.ToString());

```
// Push to all clients subscribed to this order
await _hub.Clients
.Group($"order:{order.Id}")
.SendAsync("OrderStatusChanged", message, ct);
}
```

}

// Registration with Redis backplane for multi-instance
// deployments
builder.Services.AddSignalR()
```
.AddStackExchangeRedis(redisConnectionString, opts =>
{
opts.Configuration.ChannelPrefix =
```

RedisChannel.Literal("OrderHub");
```
});



```


## KEY TAKEAWAYS

– gRPC suits internal service-to-service calls — its binary payloads are
substantially smaller than JSON.
– REST remains best for public APIs — universal compatibility and
HTTP caching outweigh gRPC's performance.
– Generate typed gRPC clients from .proto files — eliminates API drift at
compile time.



```
- 93 -
```


<a id='p94'></a>
<!-- Página 94 -->

```
C# 2026: Enterprise Mastery


```

– SignalR with WebSockets delivers sub-100ms latency for real-time
client notifications.
– Always configure a Redis backplane for SignalR in multi-instance
deployments.
– Server streaming in gRPC replaces polling patterns — push data as it
becomes available.




```
- 94 -
```


<a id='p95'></a>
<!-- Página 95 -->

```
C# 2026: Enterprise Mastery


```


## PART IV — ENTERPRISE PATTERNS & ARCHITECTURE


## CHAPTER 13




En,ty Framework Core: Enterprise
```
Pa'erns

```

"EF Core is powerful enough to carry your data layer — if you understand
```
what SQL it generates."


```

The Golden Rule: Always Check the SQL
The most important habit when using Entity Framework Core in
enterprise systems is to always verify what SQL a query generates. EF Core
is remarkably good at translating LINQ to efficient SQL, but it has
limitations and edge cases that produce unexpectedly expensive queries—
or worse, queries that succeed but load far more data than intended.
Enable query logging in development, review generated SQL in code
review, and use database-level query analysis tools (EXPLAIN ANALYZE
in PostgreSQL, Query Execution Plans in SQL Server) for any query on a
large table.
Listing: Chapter13/QueryLogging.cs


// Enable EF Core query logging during development
builder.Services.AddDbContext<AppDbContext>(opts =>
{
```
opts.UseSqlServer(connectionString);
if (builder.Environment.IsDevelopment())
{
opts.LogTo(Console.WriteLine,
```

LogLevel.Information);
```
// shows parameter values — only in dev!
opts.EnableSensitiveDataLogging();
opts.EnableDetailedErrors();

- 95 -
```


<a id='p96'></a>
<!-- Página 96 -->

```
C# 2026: Enterprise Mastery


}
```

});

// Using .TagWith() to identify queries in the database
// profiler
```
var orders = await _db.Orders
.TagWith("GetActiveOrders_v2 called from
```

OrderDashboardController")
```
.Where(o => o.Status == OrderStatus.Active &&
```

o.CreatedAt > cutoff)
```
// CRITICAL for read-only queries — no change tracking
// overhead
.AsNoTracking()
.ToListAsync(ct);




```

Compiled Queries: Eliminate the Translation
Overhead
EF Core translates LINQ to SQL every time a query is executed—parsing
the expression tree, generating a SQL string, and parameterising it. For
queries called thousands of times per second, this translation overhead is
measurable. Compiled queries perform the translation once and cache the
result, reducing per-call overhead by 30–70% for simple queries.
Listing: Chapter13/CompiledQueries.cs


// Compiled query: translate ONCE, execute thousands of
// times
public class OrderQueries
{
```
// Static field: compiled at first use, cached for
// application lifetime
private static readonly Func<AppDbContext, OrderId,
```

CancellationToken, Task<Order?>>
```
GetOrderByIdCompiled = EF.CompileAsyncQuery(
(AppDbContext db, OrderId id, CancellationToken
```

_) =>
```
db.Orders
.Include(o => o.Lines)
.FirstOrDefault(o => o.Id == id));


- 96 -
```


<a id='p97'></a>
<!-- Página 97 -->

```
C# 2026: Enterprise Mastery


private readonly AppDbContext _db;
public OrderQueries(AppDbContext db) => _db = db;

// Subsequent calls skip the expression tree
// translation entirely
public Task<Order?> GetByIdAsync(OrderId id,
```

CancellationToken ct)
```
=> GetOrderByIdCompiled(_db, id, ct);
```

}

// BenchmarkDotNet (illustrative):
// | Method | Mean | Notes |
// | RegularQuery | 1.2 ms | Includes LINQ translation |
// | CompiledQuery | 0.7 ms | Translation cached |
// | RawSqlQuery | 0.5 ms | No ORM overhead at all |




The N+1 Query Problem and Split Queries
The N+1 problem is the most common performance issue in EF Core
applications and occurs when code loads a collection and then accesses a
navigation property in a loop, triggering one SQL query for the parent
collection plus N additional queries for each child. Always load related
data with .Include() or .ThenInclude(), and for collections with large
cardinality, consider .AsSplitQuery() to avoid Cartesian explosion.
Listing: Chapter13/NPlusOne.cs


// AVOID: N+1: one query for orders, N queries for each
// order's customer
```
var orders = await _db.Orders.ToListAsync(ct);
```

foreach (var order in orders)
{
```
// EF Core lazy-loads Customer for each order —
// separate DB round trip!
// N additional queries
Console.WriteLine(order.Customer.Name);
```

}

// GOOD: Eager loading: one JOIN query
```
var orders = await _db.Orders
.Include(o => o.Customer) // JOIN — single query

- 97 -
```


<a id='p98'></a>
<!-- Página 98 -->

```
C# 2026: Enterprise Mastery


.Include(o => o.Lines)
.AsNoTracking()
.ToListAsync(ct);

```

// GOOD: Split queries: avoids Cartesian explosion for
// large collections
// Instead of one massive JOIN (rows = orders * lines *
// products)
// EF Core runs 2–3 separate focused queries
```
var orders = await _db.Orders
.Include(o => o.Lines)
.ThenInclude(l => l.Product)
// 3 separate SELECT statements vs one massive JOIN
.AsSplitQuery()
.AsNoTracking()
.ToListAsync(ct);

```

// GOOD: Projection: select only what you need — smallest
// possible payload
```
var summaries = await _db.Orders
.Where(o => o.Status == OrderStatus.Active)
.Select(o => new OrderSummaryDto(
o.Id, o.Customer.Name, o.Lines.Sum(l => l.Total)))
.AsNoTracking()
.ToListAsync(ct);




```

Bulk Operations with ExecuteUpdate and
ExecuteDelete
Listing: Chapter13/BulkOperations.cs


// EF Core 7+: bulk update without loading entities into
// memory
// Old approach: load 10,000 orders, update in memory, save
// — terrible performance
```
var ordersToExpire = await _db.Orders
.Where(o => o.Status == OrderStatus.Pending &&
```

o.CreatedAt < expiryCutoff)
```
.ToListAsync(ct);
```

foreach (var o in ordersToExpire)
```
o.Status = OrderStatus.Expired;

- 98 -
```


<a id='p99'></a>
<!-- Página 99 -->

```
C# 2026: Enterprise Mastery


```

// 10,001 round trips (1 SELECT + N UPDATEs)
await _db.SaveChangesAsync(ct);

// GOOD: New: ExecuteUpdateAsync — single UPDATE ... WHERE
// statement
await _db.Orders
```
.Where(o => o.Status == OrderStatus.Pending &&
```

o.CreatedAt < expiryCutoff)
```
.ExecuteUpdateAsync(
s => s.SetProperty(o => o.Status,
```

OrderStatus.Expired)
```
.SetProperty(o => o.UpdatedAt,
```

DateTime.UtcNow),
```
ct);
```

// Generates: UPDATE Orders SET Status = 'Expired',
// UpdatedAt = @p0
// WHERE Status = 'Pending' AND CreatedAt < @p1

// GOOD: ExecuteDeleteAsync — single DELETE ... WHERE
await _db.Sessions
```
.Where(s => s.ExpiresAt < DateTime.UtcNow)
.ExecuteDeleteAsync(ct);



```


## KEY TAKEAWAYS

– Always enable query logging in development — review the SQL every
EF Core query generates.
– AsNoTracking() is mandatory for read-only queries — eliminates
change-tracker overhead.
– Compiled queries eliminate repeated LINQ-to-SQL translation,
reducing per-call overhead on hot paths.
– Always eager-load navigation properties with Include() — never rely
on lazy loading in hot paths.
– AsSplitQuery() prevents Cartesian explosion when including multiple
collection navigations.
– ExecuteUpdateAsync and ExecuteDeleteAsync (EF Core 7+) replace
bulk load-modify-save patterns.




```
- 99 -
```


<a id='p100'></a>
<!-- Página 100 -->

```
C# 2026: Enterprise Mastery


```


## PART IV — ENTERPRISE PATTERNS & ARCHITECTURE


## CHAPTER 14




Caching Strategies for High-Tra<c
```
Systems

"The fastest operation is the one you never perform."


```

The Caching Hierarchy
Caching is not a single technique—it is a hierarchy of layers, each with
different latency, capacity, and invalidation characteristics. In a
high-traffic system, you typically need at least three layers: an in-process
memory cache (L1) with microsecond access, a distributed cache like
Redis (L2) with sub-millisecond access shared across instances, and a
database query cache (L3) via EF Core's compiled queries and database
connection pooling. The art is knowing which data belongs at which layer
and how long it can safely stay there.

The 2026 answer in .NET is HybridCache—introduced in .NET 9 and the
recommended replacement for the separate IMemoryCache +
IDistributedCache pattern. HybridCache provides L1/L2 in a single API
with built-in stampede protection, background refresh, and tag-based
invalidation.

HybridCache: The 2026 Standard
Listing: Chapter14/HybridCache.cs


// Registration: HybridCache with L1 (in-process) and L2
// (Redis) backing
builder.Services.AddHybridCache(opts =>
{

```
- 100 -
```


<a id='p101'></a>
<!-- Página 101 -->

```
C# 2026: Enterprise Mastery


opts.DefaultEntryOptions = new HybridCacheEntryOptions
{
```


## // L1 TTL

```
LocalCacheExpiration = TimeSpan.FromMinutes(1),
```


## // L2 TTL

```
Expiration = TimeSpan.FromMinutes(15),
};
// 1 MB max per entry
opts.MaximumPayloadBytes = 1024 * 1024;
opts.MaximumKeyLength = 512;
```

});
builder.Services.AddStackExchangeRedisCache(opts =>
```
opts.Configuration = redisConnectionString);

```

// Usage: GetOrCreateAsync handles L1 hit, L2 hit, and DB
// miss automatically
public class ProductCatalogue
{
```
private readonly IHybridCache _cache;
private readonly IProductReader _db;

public ProductCatalogue(IHybridCache cache,
```

IProductReader db)
```
=> (_cache, _db) = (cache, db);

public async ValueTask<Product?> GetByIdAsync(ProductId
```

id, CancellationToken ct)
```
=> await _cache.GetOrCreateAsync(
key: $"product:{id}",
factory: async token => await
```

_db.FindByIdAsync(id, token),
```
cancellationToken: ct);

// Tag-based invalidation: invalidate all products in a
// category
public async Task InvalidateCategoryAsync(string
```

category, CancellationToken ct)
```
=> await _cache.RemoveByTagAsync(category, ct);

// Cache with tags for fine-grained invalidation
public async ValueTask<IReadOnlyList<Product>>
```

GetByCategoryAsync(
```
string category, CancellationToken ct)
=> await _cache.GetOrCreateAsync(

- 101 -
```


<a id='p102'></a>
<!-- Página 102 -->

```
C# 2026: Enterprise Mastery


key: $"products:cat:{category}",
factory: async token => await
```

_db.GetByCategoryAsync(category, token),
```
options: new HybridCacheEntryOptions { Tags =
```

[category] },
```
cancellationToken: ct) ?? [];
```

}




Cache Stampede Prevention
A cache stampede occurs when a popular cache entry expires and
multiple concurrent requests all simultaneously miss the cache and hit
the database. Under heavy load, even a 100ms window of cache miss can
trigger thousands of duplicate database queries. HybridCache prevents
stampedes automatically through a per-key semaphore that allows only
one factory invocation to run while others wait for the result.
Listing: Chapter14/StampedeProtection.cs


// Without stampede protection (IMemoryCache naive pattern)
// 1000 concurrent requests for "product:42" all miss the
// cache simultaneously
// 1000 DB queries fire in parallel — database collapses
// under load

// GOOD: HybridCache: automatic stampede protection
// Only ONE factory invocation runs for "product:42"
// All 999 other callers wait for the single result and
// receive it from memory
```
var product = await _cache.GetOrCreateAsync(
key: "product:42",
factory: async token => await _db.FindByIdAsync(new
```

ProductId(42), token),
```
cancellationToken: ct);

```

// For legacy IMemoryCache: manual protection with
// SemaphoreSlim
private static readonly ConcurrentDictionary<string,
SemaphoreSlim> _locks = new();

public async Task<T?> GetOrSetWithLockAsync<T>(

```
- 102 -
```


<a id='p103'></a>
<!-- Página 103 -->

```
C# 2026: Enterprise Mastery


string key, Func<CancellationToken, Task<T?>> factory,
```

CancellationToken ct)
{
```
if (_memCache.TryGetValue<T>(key, out var cached))
```

return cached;

```
var keyLock = _locks.GetOrAdd(key, _ => new
```

SemaphoreSlim(1, 1));
```
await keyLock.WaitAsync(ct);
try
{
// Double-check after acquiring lock
if (_memCache.TryGetValue<T>(key, out cached))
```

return cached;
```
var value = await factory(ct);
_memCache.Set(key, value, TimeSpan.FromMinutes(5));
return value;
}
finally
{
keyLock.Release();
}
```

}




Cache Invalidation: The Hard Problem
Phil Karlton's famous observation—'There are only two hard things in
Computer Science: cache invalidation and naming things'—remains true
in 2026. The strategies available are: TTL expiry (simple, but data may be
stale until expiry), event-driven invalidation (accurate, but requires an
event pipeline), and write-through caching (always consistent, but
couples write path to cache). For most enterprise scenarios, a combination
of short TTL (30–60 seconds) plus event-driven invalidation on mutations
gives the best balance of freshness and simplicity.


## KEY TAKEAWAYS

```
– Use HybridCache (.NET 9) as the single caching abstraction — it
```

replaces separate L1/L2 management.



```
- 103 -
```


<a id='p104'></a>
<!-- Página 104 -->

```
C# 2026: Enterprise Mastery


```

– Cache stampedes destroy databases at scale — HybridCache prevents
them automatically.
– Short TTL + event-driven invalidation on mutations provides
freshness without over-engineering.
– Tag-based invalidation (HybridCache) lets you invalidate related
entries by logical group.
– Always define cache key conventions ('{entity-type}:{id}') — prevents
key collisions across teams.
– Never cache personal or sensitive data without explicit compliance
review.




```
- 104 -
```


<a id='p105'></a>
<!-- Página 105 -->

```
C# 2026: Enterprise Mastery


```


## PART IV — ENTERPRISE PATTERNS & ARCHITECTURE


## CHAPTER 15




Message Queues and Event-Driven
```
Architecture

```

"Decoupled services that communicate through events scale better than
```
tightly coupled ones that call each other directly."


```

Why Event-Driven Architecture at Scale
As a system grows, synchronous request-response chains become
bottlenecks. When the Order service calls the Inventory service which
calls the Shipping service which calls the Notification service—all
synchronously—the total latency is additive and the failure modes are
multiplicative. If any service is slow or unavailable, the entire chain fails.
Event-driven architecture breaks these chains by publishing domain
events to a message broker and having consumers process them
asynchronously, independently, and at their own pace.

The key technologies in the .NET ecosystem are: RabbitMQ (excellent for
moderate-scale workloads with MassTransit as the abstraction layer),
Azure Service Bus (managed, geo-redundant, with dead-letter queues and
native .NET SDK support), and Apache Kafka (for high-throughput event
streams where retention and replay are important). Choosing between
them is primarily a question of scale and operational model, not a C#
concern.




```
- 105 -
```


<a id='p106'></a>
<!-- Página 106 -->

```
C# 2026: Enterprise Mastery



```

MassTransit: The Enterprise Message
Abstraction
Listing: Chapter15/MassTransit.cs


// MassTransit with RabbitMQ: consistent API regardless of
// broker
builder.Services.AddMassTransit(cfg =>
{
```
cfg.AddConsumer<OrderCreatedConsumer>();
cfg.AddConsumer<OrderShippedConsumer>();

cfg.UsingRabbitMq((ctx, rmq) =>
{
rmq.Host("rabbitmq://localhost", h =>
{
h.Username("guest"); h.Password("guest");
});

rmq.UseMessageRetry(r =>
r.Exponential(5, TimeSpan.FromSeconds(1),
TimeSpan.FromSeconds(30),
TimeSpan.FromSeconds(2)));

rmq.UseCircuitBreaker(cb =>
{
cb.TrackingPeriod = TimeSpan.FromMinutes(1);
// % error rate to trip circuit
cb.TripThreshold = 15;
cb.ActiveThreshold = 10; // min active messages
cb.ResetInterval = TimeSpan.FromMinutes(5);
});

rmq.ConfigureEndpoints(ctx);
});
```

});

// Publishing an event
public class OrderService
{
```
private readonly IPublishEndpoint _bus;



- 106 -
```


<a id='p107'></a>
<!-- Página 107 -->

```
C# 2026: Enterprise Mastery


public OrderService(IPublishEndpoint bus) => _bus =
```

bus;

```
public async Task<OrderId> CreateAsync(OrderRequest
```

req, CancellationToken ct)
```
{
var order = Order.Create(req.CustomerId,
```

req.Items);
```
await _repository.SaveAsync(order, ct);

// Publish event — consumers run asynchronously
await _bus.Publish(new OrderCreatedEvent(
OrderId: order.Id.ToString(),
CustomerId: order.CustomerId.ToString(),
Total: order.Total.Amount,
OccurredAt: DateTime.UtcNow), ct);

return order.Id;
}
```

}

// Consumer: runs independently, can be scaled separately
public class OrderCreatedConsumer :
IConsumer<OrderCreatedEvent>
{
```
private readonly IInventoryService _inventory;
private readonly INotificationService _notify;

public async Task
```

Consume(ConsumeContext<OrderCreatedEvent> ctx)
```
{
var evt = ctx.Message;
await _inventory.ReserveItemsAsync(evt.OrderId,
```

ctx.CancellationToken);
```
await _notify.SendConfirmationAsync(evt.OrderId,
```

evt.CustomerId, ctx.CancellationToken);
```
}
```

}




```
- 107 -
```


<a id='p108'></a>
<!-- Página 108 -->

```
C# 2026: Enterprise Mastery



```

The Outbox Pattern: Guaranteed Event Delivery
The hardest problem in event-driven systems is ensuring that an event is
published if and only if the corresponding database write succeeds. Naive
implementations publish events before saving to the database (events fire
even if the save fails) or after (saves succeed but the process crashes
before publishing). The Transactional Outbox pattern solves this: events
are saved to an outbox table in the same transaction as the business data,
then a background worker reliably publishes them to the broker.
Listing: Chapter15/OutboxPattern.cs


// Outbox pattern with EF Core: atomic business data +
// event storage
public class OutboxOrderRepository : IOrderRepository
{
```
private readonly AppDbContext _db;

public OutboxOrderRepository(AppDbContext db) => _db =
```

db;

```
public async Task SaveAsync(Order order,
```

CancellationToken ct)
```
{
// Both operations in ONE transaction — atomically
// consistent
await using var tx = await
```

_db.Database.BeginTransactionAsync(ct);
```
try
{
// Attach only if not already tracked (see
// Chapter 6 — avoid
// marking every property modified on an
// already-tracked entity).
if (_db.Entry(order).State ==
```

EntityState.Detached)
```
_db.Orders.Update(order);

// Write events to the outbox table — same
// transaction
foreach (var evt in order.DomainEvents)
{

- 108 -
```


<a id='p109'></a>
<!-- Página 109 -->

```
C# 2026: Enterprise Mastery


_db.OutboxMessages.Add(new OutboxMessage
{
Id = Guid.NewGuid(),
Type =
```

evt.GetType().AssemblyQualifiedName!,
```
Payload =
```

JsonSerializer.Serialize(evt, evt.GetType()),
```
CreatedAt = DateTime.UtcNow,
ProcessedAt = null,
});
}

await _db.SaveChangesAsync(ct);
await tx.CommitAsync(ct);
order.ClearDomainEvents();
}
catch
{
await tx.RollbackAsync(ct);
throw;
}
}
```

}

// Background worker: reliably publishes outbox messages
public class OutboxProcessor : BackgroundService
{
```
private readonly IServiceScopeFactory _scopes;
private readonly IPublishEndpoint _bus;
private readonly ILogger<OutboxProcessor> _log;

protected override async Task
```

ExecuteAsync(CancellationToken stoppingToken)
```
{
while (!stoppingToken.IsCancellationRequested)
{
await PublishPendingAsync(stoppingToken);
await Task.Delay(TimeSpan.FromSeconds(5),
```

stoppingToken);
```
}
}

private async Task
```

PublishPendingAsync(CancellationToken ct)

```
- 109 -
```


<a id='p110'></a>
<!-- Página 110 -->

```
C# 2026: Enterprise Mastery


{
using var scope = _scopes.CreateScope();
var db =
```

scope.ServiceProvider.GetRequiredService<AppDbContext>();

```
var pending = await db.OutboxMessages
.Where(m => m.ProcessedAt == null)
.OrderBy(m => m.CreatedAt)
.Take(100)
.ToListAsync(ct);

foreach (var msg in pending)
{
var type = Type.GetType(msg.Type)!;
var payload =
```

JsonSerializer.Deserialize(msg.Payload, type)!;
```
await _bus.Publish(payload, type, ct);
msg.ProcessedAt = DateTime.UtcNow;
}
await db.SaveChangesAsync(ct);
}
```

}




## KEY TAKEAWAYS

– Event-driven architecture breaks synchronous call chains — each
service scales independently.
– MassTransit abstracts the broker — swap RabbitMQ for Azure Service
Bus with minimal code changes.
– The Transactional Outbox pattern guarantees event delivery even if
the process crashes mid-publish.
– Always configure retry and circuit-breaker policies — transient
broker failures are inevitable at scale.
– Consume events idempotently — messages may be delivered more
than once in any reliable messaging system.
– Dead-letter queues are mandatory — unprocessable messages must be
captured for investigation.




```
- 110 -
```


<a id='p111'></a>
<!-- Página 111 -->

```
C# 2026: Enterprise Mastery


```


## PART IV — ENTERPRISE PATTERNS & ARCHITECTURE


## CHAPTER 16




Microservices Architecture with C#

"Microservices are not a silver bullet — they trade deployment complexity
```
for organisational 5exibility."


```

When Microservices Make Sense
The most common mistake with microservices is adopting them before
the organisational and technical maturity is in place to support them. A
monolith with good internal architecture—clear module boundaries,
dependency injection, event-driven communication between modules—
scales well and is dramatically easier to develop, debug, and deploy than a
microservices system. The right time to decompose is when deployment
bottlenecks between teams, or scaling requirements specific to one part of
the system, make the monolith a genuine constraint.

When you do decompose, the bounded context concept from
Domain-Driven Design is your guide: each service should own one
bounded context, with its own data store, its own deployment lifecycle,
and its own team. Services that share a database are not microservices—
they are a distributed monolith with the disadvantages of both
architectures and the advantages of neither.

Resilience with Polly v8
In a microservices environment, every network call can fail. The question
is not whether a service will be unavailable but when. Polly is the most
widely used resilience library for .NET. Polly v8 introduced a fully
redesigned API built on pipelines that compose retry, circuit breaker,
timeout, hedging, and fallback strategies.

```
- 111 -
```


<a id='p112'></a>
<!-- Página 112 -->

```
C# 2026: Enterprise Mastery


```

Listing: Chapter16/Polly.cs


// Polly v8: composable resilience pipeline registered via

## // DI

builder.Services.AddHttpClient<IInventoryClient,
InventoryClient>(client =>
{
```
client.BaseAddress = new Uri("https://inventory-
```

service/");
```
client.Timeout = TimeSpan.FromSeconds(30);
```

})
.AddResilienceHandler("inventory-pipeline", pipeline =>
{
```
// 1. Retry: exponential backoff, up to 3 attempts
pipeline.AddRetry(new HttpRetryStrategyOptions
{
MaxRetryAttempts = 3,
Delay = TimeSpan.FromMilliseconds(200),
BackoffType = DelayBackoffType.Exponential,
UseJitter = true, // prevent thundering herd
ShouldHandle = args => ValueTask.FromResult(
args.Outcome.Exception is not null ||
(args.Outcome.Result?.StatusCode is
```

HttpStatusCode.TooManyRequests
```
or HttpStatusCode.ServiceUnavailable or
```

HttpStatusCode.GatewayTimeout)),
```
});

// 2. Circuit Breaker: open after 5 failures in 30
// seconds
pipeline.AddCircuitBreaker(new
```

HttpCircuitBreakerStrategyOptions
```
{
SamplingDuration = TimeSpan.FromSeconds(30),
MinimumThroughput = 10,
// 50% failure rate trips the circuit
FailureRatio = 0.5,
BreakDuration = TimeSpan.FromSeconds(15),
});

// 3. Timeout per attempt
pipeline.AddTimeout(TimeSpan.FromSeconds(5));
```

});


```
- 112 -
```


<a id='p113'></a>
<!-- Página 113 -->

```
C# 2026: Enterprise Mastery




```

// Typed client — resilience is transparent to the caller
public class InventoryClient
{
```
private readonly HttpClient _http;
public InventoryClient(HttpClient http) => _http =
```

http;

```
public async Task<InventoryStatus?> GetStatusAsync(
string sku, CancellationToken ct)
{
var response = await
```

_http.GetAsync($"/inventory/{sku}", ct);
```
response.EnsureSuccessStatusCode();
return await
```

response.Content.ReadFromJsonAsync<InventoryStatus>(ct);
```
}
```

}




Health Checks and Readiness Probes
Listing: Chapter16/HealthChecks.cs


// Health checks: essential for Kubernetes
// liveness/readiness probes
builder.Services.AddHealthChecks()
```
.AddSqlServer(connectionString, name: "sql-server",
```

tags: ["ready"])
```
.AddRedis(redisConnectionString, name: "redis", tags:
```

["ready"])
```
.AddRabbitMQ(rabbitConnectionString, name: "rabbitmq",
```

tags: ["ready"])
```
.AddCheck<CustomBusinessHealthCheck>("business-rules",
```

tags: ["ready"]);

// Separate liveness (is the process alive?) from readiness
// (can it serve traffic?)
app.MapHealthChecks("/health/live", new HealthCheckOptions
{
```
// liveness: just return 200 — process is alive
Predicate = _ => false,
```

});

```
- 113 -
```


<a id='p114'></a>
<!-- Página 114 -->

```
C# 2026: Enterprise Mastery


```

app.MapHealthChecks("/health/ready", new HealthCheckOptions
{
```
// readiness: check dependencies
Predicate = hc => hc.Tags.Contains("ready"),
ResponseWriter =
```

UIResponseWriter.WriteHealthCheckUIResponse,
});

// Custom health check: business-level diagnostic
public class CustomBusinessHealthCheck : IHealthCheck
{
```
private readonly IOrderReader _orders;
public CustomBusinessHealthCheck(IOrderReader orders)
```

=> _orders = orders;

```
public async Task<HealthCheckResult> CheckHealthAsync(
HealthCheckContext ctx, CancellationToken ct)
{
try
{
var count = await
```

_orders.GetPendingCountAsync(ct);
```
if (count > 10_000)
return HealthCheckResult.Degraded(
$"High pending order backlog:
```

{count}");
```
return HealthCheckResult.Healthy($"Pending
```

orders: {count}");
```
}
catch (Exception ex)
{
return HealthCheckResult.Unhealthy("Cannot
```

reach order store", ex);
```
}
}
```

}




## KEY TAKEAWAYS

– Adopt microservices when organisational or scaling constraints make
the monolith a genuine bottleneck.



```
- 114 -
```


<a id='p115'></a>
<!-- Página 115 -->

```
C# 2026: Enterprise Mastery


```

– Each service owns its data — services sharing a database are a
distributed monolith.
– Polly v8 pipeline API composes retry + circuit breaker + timeout into a
single resilient HTTP client.
– UseJitter on retry prevents thundering herd when multiple services
retry simultaneously.
– Separate liveness from readiness health checks — Kubernetes uses
both differently.
– The Strangler Fig pattern (Chapter 24) is the safest way to extract
services from a monolith.




```
- 115 -
```


<a id='p116'></a>
<!-- Página 116 -->

```
C# 2026: Enterprise Mastery


```


## PART IV — ENTERPRISE PATTERNS & ARCHITECTURE


## CHAPTER 17




Dependency Injec,on at Enterprise
```
Scale

"The DI container is a tool, not an architecture. Use it well, and it
disappears."


```

Service Lifetimes: The Rules That Cannot Be
Broken
The three service lifetimes in .NET's DI container—Singleton, Scoped, and
Transient—have strict compatibility rules that, when violated, create
subtle, hard-to-diagnose bugs. A Singleton that captures a Scoped
dependency will hold a reference to a scoped service well past the end of
the scope, causing data from one HTTP request to leak into another. This
is called 'captive dependency' and it is one of the most insidious bugs in
DI-heavy applications because it does not fail immediately—it fails
intermittently, in production, under load.
Listing: Chapter17/ServiceLifetimes.cs


// AVOID: CAPTIVE DEPENDENCY: Singleton capturing a Scoped
// service
// DbContext is registered as Scoped — but MyCache is
// Singleton
// Result: DbContext from request #1 is used for all
// subsequent requests
public class MyCache // registered as Singleton
{
```
// registered as Scoped — WRONG!
private readonly AppDbContext _db;


- 116 -
```


<a id='p117'></a>
<!-- Página 117 -->

```
C# 2026: Enterprise Mastery


public MyCache(AppDbContext db) => _db = db;
```

}

// GOOD: Correct: Singleton captures IServiceScopeFactory
// and creates scopes explicitly
public class MyCache : IDisposable
{
```
private readonly IServiceScopeFactory _scopeFactory;
public MyCache(IServiceScopeFactory factory) =>
```

_scopeFactory = factory;

```
public async Task<string?> GetValueAsync(string key,
```

CancellationToken ct)
```
{
// Create a short-lived scope to safely resolve
// Scoped services
using var scope = _scopeFactory.CreateScope();
var db =
```

scope.ServiceProvider.GetRequiredService<AppDbContext>();
```
return await db.ConfigValues
.Where(c => c.Key == key)
.Select(c => c.Value)
.FirstOrDefaultAsync(ct);
}
public void Dispose() { }
```

}

// GOOD: Enable scope validation in development to catch
// captive dependencies early
builder.Host.UseDefaultServiceProvider(opts =>
{
```
opts.ValidateScopes = true;
opts.ValidateOnBuild = true;
```

});




```
- 117 -
```


<a id='p118'></a>
<!-- Página 118 -->

```
C# 2026: Enterprise Mastery



```

Keyed Services: Strategy Selection Without
Service Locator
Listing: Chapter17/KeyedServices.cs


// .NET 8+ Keyed Services: resolve different
// implementations by key
public interface IStorageProvider
{
```
Task UploadAsync(string path, Stream content,
```

CancellationToken ct);
}

public class AzureBlobStorage : IStorageProvider { ... }
public class LocalDiskStorage : IStorageProvider { ... }
public class S3Storage : IStorageProvider { ... }

// Register with keys
builder.Services.AddKeyedSingleton<IStorageProvider,
AzureBlobStorage>("azure");
builder.Services.AddKeyedSingleton<IStorageProvider,
LocalDiskStorage>("local");
builder.Services.AddKeyedSingleton<IStorageProvider,
S3Storage>("s3");

// Inject by key via [FromKeyedServices] attribute
public class DocumentService
{
```
private readonly IStorageProvider _storage;

public DocumentService(
[FromKeyedServices("azure")] IStorageProvider
```

storage)
```
=> _storage = storage;
```

}

// Or resolve dynamically at runtime
public class StorageRouter
{
```
private readonly IServiceProvider _sp;
public StorageRouter(IServiceProvider sp) => _sp = sp;



- 118 -
```


<a id='p119'></a>
<!-- Página 119 -->

```
C# 2026: Enterprise Mastery


public IStorageProvider GetFor(string provider)
=>
```

_sp.GetRequiredKeyedService<IStorageProvider>(provider);
}




## KEY TAKEAWAYS

– Captive dependencies (Singleton capturing Scoped) cause data leaks
across requests — enable ValidateScopes.
– ValidateOnBuild catches registration errors at startup rather than at
first use in production.
– Keyed services replace manual factory patterns for strategy selection
— cleaner and DI-native.
– Avoid IServiceProvider as a general-purpose service locator — it hides
dependencies and hurts testability.
– Use IServiceScopeFactory in Singletons that need Scoped services —
create short-lived scopes explicitly.
– Register Open Generics (typeof(IRepository<>)) to handle generic
services without N registrations.




```
- 119 -
```


<a id='p120'></a>
<!-- Página 120 -->

```
C# 2026: Enterprise Mastery


```


## PART V — OBSERVABILITY, TESTING & SECURITY


## CHAPTER 18




Tes,ng Strategies for Enterprise C#

```
"Untested code is not working code — it is untested code."


```

The Test Pyramid Revisited
The test pyramid—many unit tests, fewer integration tests, few
end-to-end tests—remains the right mental model for enterprise C# in
2026. Unit tests provide fast, reliable feedback on individual components
and business logic. Integration tests verify that components work
correctly together, especially at boundaries with databases, message
queues, and external APIs. End-to-end tests provide confidence that the
full system works from a user perspective but are slow, fragile, and
expensive to maintain.

A common mistake is writing integration tests that test business logic
(should be unit tests) or unit tests that test infrastructure (should be
integration tests). The DDD domain model—with its pure,
framework-independent business logic—is perfectly suited for fast,
deterministic unit tests with no I/O.

Unit Testing Domain Logic
Listing: Chapter18/OrderTests.cs


// xUnit + FluentAssertions: clean, readable test
// assertions
public class OrderTests
{
```
[Fact]



- 120 -
```


<a id='p121'></a>
<!-- Página 121 -->

```
C# 2026: Enterprise Mastery


public void
```

Create_WithValidItems_ShouldSetStatusDraft()
```
{
// Arrange
var customerId = CustomerId.New();
var items = new List<OrderLineRequest>
{
new(ProductId.New(), quantity: 2, unitPrice:
```

new Money(50m, "USD")),
```
};

// Act
var order = Order.Create(customerId, items);

// Assert — FluentAssertions for readable failures
order.Status.Should().Be(OrderStatus.Draft);
order.Lines.Should().HaveCount(1);
order.Total.Amount.Should().Be(100m);
order.DomainEvents.Should().ContainSingle()
.Which.Should().BeOfType<OrderCreatedEvent>();
}

[Fact]
public void
```

Submit_WhenDraft_ShouldTransitionToSubmitted()
```
{
var order = OrderFactory.CreateDraftOrder();

order.Submit();

order.Status.Should().Be(OrderStatus.Submitted);
order.DomainEvents.Should().Contain(e => e is
```

OrderSubmittedEvent);
```
}

[Fact]
public void
```

Submit_WhenAlreadySubmitted_ShouldThrowDomainException()
```
{
var order = OrderFactory.CreateSubmittedOrder();

var act = () => order.Submit();

act.Should().Throw<DomainException>()

- 121 -
```


<a id='p122'></a>
<!-- Página 122 -->

```
C# 2026: Enterprise Mastery


.WithMessage("*status*");
}
```

}




Integration Testing with WebApplicationFactory
Listing: Chapter18/IntegrationTests.cs


// Integration tests against a real in-memory ASP.NET Core
// server
public class OrderEndpointTests :
IClassFixture<TestWebAppFactory>
{
```
private readonly HttpClient _client;

public OrderEndpointTests(TestWebAppFactory factory)
=> _client = factory.CreateClient();

[Fact]
public async Task
```

CreateOrder_WithValidRequest_Returns201()
```
{
var request = new CreateOrderRequest(
CustomerId: Guid.NewGuid().ToString(),
Items: [new(ProductId:
```

Guid.NewGuid().ToString(), Quantity: 1, UnitPrice:
99.99m)]);

```
var response = await
```

_client.PostAsJsonAsync("/api/v1/orders", request);



response.StatusCode.Should().Be(HttpStatusCode.Created);
```
response.Headers.Location.Should().NotBeNull();
}
```

}

public class TestWebAppFactory :
WebApplicationFactory<Program>
{
```
protected override void
```

ConfigureWebHost(IWebHostBuilder builder)

```
- 122 -
```


<a id='p123'></a>
<!-- Página 123 -->

```
C# 2026: Enterprise Mastery


{
builder.ConfigureServices(services =>
{
// Replace SQL Server with in-memory EF Core
// for tests
var descriptor = services.SingleOrDefault(d =>
d.ServiceType ==
```

typeof(DbContextOptions<AppDbContext>));
```
if (descriptor is not null)
```

services.Remove(descriptor);

```
services.AddDbContext<AppDbContext>(opts =>
opts.UseInMemoryDatabase("TestDb"));

// Replace real external services with fakes
services.AddSingleton<IEmailSender,
```

NullEmailSender>();
```
services.AddSingleton<IPublishEndpoint,
```

NullPublishEndpoint>();
```
});
}
```

}




TestContainers: Real Database Tests
Listing: Chapter18/TestContainers.cs


// Testcontainers: run a real PostgreSQL in Docker during
// tests
public class OrderRepositoryTests : IAsyncLifetime
{
```
private readonly PostgreSqlContainer _postgres = new
```

PostgreSqlBuilder()
```
.WithImage("postgres:16-alpine")
.WithDatabase("testdb")
.WithUsername("test")
.WithPassword("test")
.Build();

private AppDbContext _db = null!;

public async Task InitializeAsync()

- 123 -
```


<a id='p124'></a>
<!-- Página 124 -->

```
C# 2026: Enterprise Mastery


{
await _postgres.StartAsync();
var opts = new
```

DbContextOptionsBuilder<AppDbContext>()
```
.UseNpgsql(_postgres.GetConnectionString())
.Options;
_db = new AppDbContext(opts);
await _db.Database.MigrateAsync();
}

[Fact]
public async Task SaveAsync_PersistsOrderToDatabase()
{
var order = OrderFactory.CreateDraftOrder();
var repo = new EfOrderRepository(_db, new
```

NullDomainEventDispatcher());

```
await repo.SaveAsync(order,
```

CancellationToken.None);

```
var loaded = await repo.FindByIdAsync(order.Id,
```

CancellationToken.None);
```
loaded.Should().NotBeNull();
loaded!.Status.Should().Be(OrderStatus.Draft);
}

public async Task DisposeAsync()
{
await _db.DisposeAsync();
await _postgres.DisposeAsync();
}
```

}




## KEY TAKEAWAYS

– Unit-test domain logic — no I/O, no frameworks, pure business rule
verification.
– WebApplicationFactory provides a real ASP.NET Core host for
integration tests without a running server.
– Replace external dependencies (email, queues) with null/fake
implementations in test factories.


```
- 124 -
```


<a id='p125'></a>
<!-- Página 125 -->

```
C# 2026: Enterprise Mastery


```

– Testcontainers spins up real Docker containers (PostgreSQL, Redis)
for faithful integration tests.
– BenchmarkDotNet is the correct tool for performance regression
testing in CI pipelines.
– Keep test code as clean as production code — tests are documentation
that must be maintained.




```
- 125 -
```


<a id='p126'></a>
<!-- Página 126 -->

```
C# 2026: Enterprise Mastery


```


## PART V — OBSERVABILITY, TESTING & SECURITY


## CHAPTER 19




Observability: Logging, Tracing, and
```
Metrics

```

"You cannot manage what you cannot measure — and you cannot debug
```
what you cannot observe."


```

The Three Pillars of Observability
Observability is the ability to understand the internal state of a system
```
from its external outputs. The three pillars are: Logs (structured records
```

of discrete events), Traces (end-to-end records of request journeys across
services), and Metrics (numerical measurements aggregated over time).
At a million requests per day, all three are essential and must be emitted
efficiently—logging every request at DEBUG level to disk will consume
more I/O than the service itself produces.

OpenTelemetry (OTel) is the vendor-neutral standard for emitting all
three signal types from .NET applications. The
Microsoft.Extensions.Telemetry and OpenTelemetry NuGet packages
provide a .NET-native OTel SDK that integrates with ASP.NET Core's
built-in Activity API, the ILogger abstraction, and the
System.Diagnostics.Metrics API.




```
- 126 -
```


<a id='p127'></a>
<!-- Página 127 -->

```
C# 2026: Enterprise Mastery



```

Structured Logging with Serilog and OTel
Listing: Chapter19/StructuredLogging.cs


// Program.cs: structured logging with Serilog +
// OpenTelemetry export
builder.Host.UseSerilog((ctx, cfg) =>
{
```
cfg.ReadFrom.Configuration(ctx.Configuration)
.Enrich.FromLogContext()
.Enrich.WithMachineName()
.Enrich.WithEnvironmentName()
// structured JSON to stdout
.WriteTo.Console(new JsonFormatter())
// export to OTel collector
.WriteTo.OpenTelemetry(opts =>
{
opts.Endpoint = "http://otel-collector:4318";
opts.ResourceAttributes = new Dictionary<string,
```

object>
```
{
["service.name"] = "order-service",
["service.version"] = "2.1.0",
};
});
```

});

// Source-generated log messages: faster than string
// interpolation, and allocation-free
public static partial class OrderLog
{
```
[LoggerMessage(Level = LogLevel.Information,
Message = "Order {OrderId} created for customer
```

{CustomerId} total {Total:C}")]
```
public static partial void OrderCreated(
ILogger logger, string orderId, string customerId,
```

decimal total);

```
[LoggerMessage(Level = LogLevel.Warning,
Message = "Order {OrderId} payment declined:
```

{Reason}")]
```
public static partial void PaymentDeclined(
ILogger logger, string orderId, string reason);

- 127 -
```


<a id='p128'></a>
<!-- Página 128 -->

```
C# 2026: Enterprise Mastery




[LoggerMessage(Level = LogLevel.Error,
Message = "Failed to process order {OrderId}")]
public static partial void OrderProcessingFailed(
ILogger logger, Exception ex, string orderId);
```

}

// Usage — no string interpolation, no boxing, no
// allocation until logged
OrderLog.OrderCreated(_logger, order.Id.ToString(),
order.CustomerId.ToString(), order.Total.Amount);




Distributed Tracing with OpenTelemetry
Listing: Chapter19/OpenTelemetry.cs


// OpenTelemetry distributed tracing setup
builder.Services.AddOpenTelemetry()
```
.ConfigureResource(resource => resource
.AddService(serviceName: "order-service",
```

serviceVersion: "2.1.0"))
```
.WithTracing(tracing => tracing
.AddAspNetCoreInstrumentation(opts =>
{
opts.RecordException = true;
opts.Filter = ctx => !
```

ctx.Request.Path.StartsWithSegments("/health");
```
})
.AddHttpClientInstrumentation()
.AddEntityFrameworkCoreInstrumentation(opts =>
// captures SQL — dev only!
opts.SetDbStatementForText = true)
// custom ActivitySource
.AddSource("OrderService")
.AddOtlpExporter(opts =>
opts.Endpoint = new Uri("http://otel-
```

collector:4317")))
```
.WithMetrics(metrics => metrics
.AddAspNetCoreInstrumentation()
.AddRuntimeInstrumentation()
.AddMeter("OrderService")
.AddOtlpExporter());

- 128 -
```


<a id='p129'></a>
<!-- Página 129 -->

```
C# 2026: Enterprise Mastery




```

// Custom spans: instrument business-critical code paths
private static readonly ActivitySource _tracer =
new("OrderService");

public async Task<OrderId> ProcessAsync(OrderRequest req,
CancellationToken ct)
{
```
using var span = _tracer.StartActivity("ProcessOrder");
span?.SetTag("customer.id", req.CustomerId.ToString());
span?.SetTag("order.item_count", req.Items.Count);

var order = Order.Create(req.CustomerId, req.Items);
await _repository.SaveAsync(order, ct);

span?.SetTag("order.id", order.Id.ToString());
span?.SetTag("order.total",
```

order.Total.Amount.ToString("F2"));
```
return order.Id;
```

}

// Custom metrics: business-level counters and histograms
private static readonly Meter _meter = new("OrderService",
"2.1.0");
private static readonly Counter<long> _ordersCreated =
_meter.CreateCounter<long>("orders.created");
private static readonly Histogram<double>_orderTotal =
_meter.CreateHistogram<double>("orders.total_amount",

## "USD");


public void RecordOrderCreated(Order order)
{
```
_ordersCreated.Add(1, new TagList { ["status"] =
```

"success" });
```
_orderTotal.Record((double)order.Total.Amount);
```

}




## KEY TAKEAWAYS

– Logs, traces, and metrics are the three pillars — all three are
necessary at enterprise scale.



```
- 129 -
```


<a id='p130'></a>
<!-- Página 130 -->

```
C# 2026: Enterprise Mastery


```

– OpenTelemetry is the vendor-neutral standard — emit once, route to
any backend.
– Source-generated log messages ([LoggerMessage]) are faster and
allocation-free compared to interpolated logging.
– Never log at DEBUG in production on hot paths — the I/O overhead
exceeds the request processing cost.
– Add TraceId and SpanId to every structured log entry — correlate logs
with traces.
– Custom business metrics (orders created, payment success rate) are as
important as system metrics.




```
- 130 -
```


<a id='p131'></a>
<!-- Página 131 -->

```
C# 2026: Enterprise Mastery


```


## PART V — OBSERVABILITY, TESTING & SECURITY


## CHAPTER 20




Security Best Prac,ces in C# 2026

"Security is not a feature you add at the end — it is a practice you build
```
from the start."


```

Authentication and Authorisation with ASP.NET
Core
ASP.NET Core's authentication and authorisation middleware is one of
the most well-designed parts of the framework. Authentication (who are
you?) is handled through a pluggable authentication scheme system—
JWT Bearer tokens, cookies, API keys, certificate authentication—
configurable in any combination. Authorisation (what can you do?) is
handled through policies that evaluate claims, roles, and resource-specific
requirements. In 2026, JWT Bearer tokens for API authentication and
OpenID Connect for web applications remain the standard. Never roll
your own authentication—use the battle-tested framework abstractions.
Listing: Chapter20/Authentication.cs


// JWT Bearer authentication with proper validation
builder.Services.AddAuthentication(JwtBearerDefaults.Authen
ticationScheme)
```
.AddJwtBearer(opts =>
{
opts.Authority = "https://identity.example.com";
opts.Audience = "order-service";
opts.TokenValidationParameters = new
```

TokenValidationParameters
```
{
ValidateIssuer = true,
ValidateAudience = true,

- 131 -
```


<a id='p132'></a>
<!-- Página 132 -->

```
C# 2026: Enterprise Mastery


ValidateLifetime = true,
ValidateIssuerSigningKey = true,
// tolerance for clock drift
ClockSkew =
```

TimeSpan.FromSeconds(30),
```
};
opts.Events = new JwtBearerEvents
{
OnTokenValidated = ctx =>
{
// Enrich the principal with custom claims
// from a database
var claims = ctx.Principal?.Claims;
return Task.CompletedTask;
},
OnAuthenticationFailed = ctx =>
{
// Log authentication failures for security
// monitoring
var log = ctx.HttpContext.RequestServices
.GetRequiredService<ILogger<Program>>()
```

;
```
log.LogWarning("JWT authentication failed:
```

{Error}", ctx.Exception.Message);
```
return Task.CompletedTask;
}
};
});

```

// Resource-based authorisation: can this user access THIS
// order?
public class OrderAuthorizationHandler
```
: AuthorizationHandler<SameCustomerRequirement, Order>
```

{
```
protected override Task HandleRequirementAsync(
AuthorizationHandlerContext ctx,
SameCustomerRequirement requirement,
Order resource)
{
var userId =
```

ctx.User.FindFirstValue(ClaimTypes.NameIdentifier);
```
if (resource.CustomerId.ToString() == userId ||
```

ctx.User.IsInRole("Admin"))
```
ctx.Succeed(requirement);

- 132 -
```


<a id='p133'></a>
<!-- Página 133 -->

```
C# 2026: Enterprise Mastery


return Task.CompletedTask;
}
```

}




Secrets Management: Never Store Secrets in Code
Listing: Chapter20/SecretsManagement.cs


// AVOID: NEVER: secrets in source code or appsettings.json
```
var connStr =
```

"Server=proddb01;Password=MyS3cr3tP@ssword!;";

// GOOD: Development: .NET User Secrets (never committed to
// source control)
// dotnet user-secrets set "ConnectionStrings:Default"
// "Server=localhost;..."
builder.Configuration.AddUserSecrets<Program>();

// GOOD: Production: Azure Key Vault (or AWS Secrets
// Manager, HashiCorp Vault)
if (!builder.Environment.IsDevelopment())
{
```
var keyVaultUri = new
```

Uri($"https://{keyVaultName}.vault.azure.net/");
```
builder.Configuration.AddAzureKeyVault(keyVaultUri, new
```

DefaultAzureCredential());
}

// GOOD: Container environments: environment variables
// injected by Kubernetes secrets
// The appsettings.json approach is a last resort with
// encrypted values only.

// Data protection: encrypt sensitive data at rest
builder.Services.AddDataProtection()
```
// keys stored externally, not in process
.PersistKeysToAzureBlobStorage(blobUri)
.ProtectKeysWithAzureKeyVault(keyIdentifier, new
```

DefaultAzureCredential())
```
.SetApplicationName("order-service")
.SetDefaultKeyLifetime(TimeSpan.FromDays(90));


- 133 -
```


<a id='p134'></a>
<!-- Página 134 -->

```
C# 2026: Enterprise Mastery



```

Input Validation and Injection Prevention
Listing: Chapter20/InputValidation.cs


// SQL injection prevention: parameterised queries ALWAYS
// (EF Core does this by default)
// Direct string interpolation in EF Core FromSqlRaw is
// dangerous:


## // AVOID: SQL INJECTION VULNERABILITY

```
var search = userInput; // "'; DROP TABLE Orders;--"
var orders = _db.Orders.FromSqlRaw($"SELECT * FROM Orders
```

WHERE CustomerId = '{search}'");

// GOOD: Parameterised — safe against SQL injection
```
var orders = _db.Orders.FromSqlRaw(
"SELECT * FROM Orders WHERE CustomerId = {0}",
```

customerId.ToString());

// Or better: use LINQ which is always parameterised
```
var orders = _db.Orders.Where(o => o.CustomerId ==
```

customerId);

// Input validation at the API boundary
public class CreateOrderRequestValidator :
AbstractValidator<CreateOrderRequest>
{
```
public CreateOrderRequestValidator()
{
RuleFor(r => r.CustomerId)
.NotEmpty()
.Must(BeAValidGuid).WithMessage("CustomerId
```

must be a valid GUID.");

```
RuleFor(r => r.Items)
.NotEmpty().WithMessage("Order must contain at
```

least one item.")
```
.Must(items => items.Count <=
```

100).WithMessage("Maximum 100 items per order.");

```
RuleForEach(r => r.Items).ChildRules(item =>
{



- 134 -
```


<a id='p135'></a>
<!-- Página 135 -->

```
C# 2026: Enterprise Mastery


item.RuleFor(i =>
```

i.Quantity).InclusiveBetween(1, 9999);
```
item.RuleFor(i => i.UnitPrice).GreaterThan(0m);
});
}
private static bool BeAValidGuid(string value) =>
```

Guid.TryParse(value, out _);
}




## KEY TAKEAWAYS

– Never implement authentication yourself — use ASP.NET Core's
built-in JWT Bearer / OIDC support.
– Resource-based authorisation checks whether a user can access a
specific resource, not just a role.
– Secrets never live in source code — use User Secrets locally, Key Vault
(or equivalent) in production.
– EF Core LINQ queries are always parameterised — use FromSqlRaw
with parameters for raw SQL, never interpolation.
– Validate all input at API boundaries with FluentValidation before it
reaches domain logic.
– Security event logging (authentication failures, authorisation denials)
is mandatory for compliance.




```
- 135 -
```


<a id='p136'></a>
<!-- Página 136 -->

```
C# 2026: Enterprise Mastery


```


## PART VI — THE 2026 FRONTIER


## CHAPTER 21




```
AI Integra,on in C# 2026

```

Arti8cial intelligence is no longer a feature — it is an expectation. In 2026,
every serious enterprise application either calls an AI model, orchestrates
```
an AI agent, or embeds AI-powered logic directly in its pipelines. C#
```

and .NET have kept pace, and this chapter shows you how to integrate AI
```
cleanly, safely, and ef8ciently.


```

21.1 The Microsoft.Extensions.AI Abstraction
Microsoft.Extensions.AI (MEAI) is the unified abstraction that arrived
in .NET 9 and matured in .NET 10. The key interfaces are IChatClient,
IEmbeddingGenerator<TInput,TEmbedding>, and ISpeechToTextClient.
These abstractions let you swap providers — OpenAI, Azure OpenAI,
Ollama, Anthropic — without changing business logic.


// Chapter21/MeaiSetup.cs
using Microsoft.Extensions.AI;
using Microsoft.Extensions.DependencyInjection;

```
var builder = WebApplication.CreateBuilder(args);

```

// Register Azure OpenAI chat client
builder.Services.AddChatClient(services =>
```
new AzureOpenAIClient(
new
```

Uri(builder.Configuration["AzureOpenAI:Endpoint"]!),
```
new
```

AzureKeyCredential(builder.Configuration["AzureOpenAI:Key"]
!))
```
.AsChatClient("gpt-4o"));


- 136 -
```


<a id='p137'></a>
<!-- Página 137 -->

```
C# 2026: Enterprise Mastery


```

// Swap to local Ollama with one line change
// builder.Services.AddChatClient(new
// OllamaChatClient("http://localhost:11434", "llama3.2"));

// Pipeline: logging -> caching -> rate-limiting ->
// underlying client
builder.Services.AddChatClient(services =>
```
services.GetRequiredService<IUnderlyingChatClient>()
.AsBuilder()
.UseLogging()
.UseDistributedCache()
.UseRateLimiting()
.Build());




```

21.2 Semantic Kernel for Orchestration
Semantic Kernel is Microsoft's orchestration framework for building AI
agents and pipelines. It gives you plugins, planners, memory, and process
automation in a single coherent model.


// Chapter21/SemanticKernelExample.cs
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;

```
var kernel = Kernel.CreateBuilder()
.AddAzureOpenAIChatCompletion("gpt-4o", endpoint,
```

apiKey)
```
.Build();

```

// Define a plugin from a class
kernel.Plugins.AddFromType<OrderPlugin>("Orders");

// Invoke a function directly
```
var result = await kernel.InvokeAsync("Orders",
```

"GetStatus",
```
new KernelArguments { ["orderId"] = "ORD-1234" });
```

Console.WriteLine(result);

// Use the chat service with auto function invocation


```
- 137 -
```


<a id='p138'></a>
<!-- Página 138 -->

```
C# 2026: Enterprise Mastery


var chatService =
```

kernel.GetRequiredService<IChatCompletionService>();
```
var settings = new OpenAIPromptExecutionSettings
```

{
```
ToolCallBehavior =
```

ToolCallBehavior.AutoInvokeKernelFunctions
};
```
var chat = new ChatHistory("You are an order assistant.");
```

chat.AddUserMessage("What is the status of order ORD1234?");
```
var response = await
```

chatService.GetChatMessageContentAsync(chat, settings,
kernel);
Console.WriteLine(response.Content);

// Chapter21/OrderPlugin.cs
public class OrderPlugin
{
```
private readonly IOrderRepository _repo;
public OrderPlugin(IOrderRepository repo) => _repo =
```

repo;

```
[KernelFunction, Description("Gets the status of a
```

specific order")]
```
public async Task<string> GetStatus([Description("The
```

order ID")] string orderId)
```
{
var order = await _repo.GetByIdAsync(orderId);
return order is null ? "Order not found" :
```

$"Status: {order.Status}";
```
}
```

}




Architect Principle: AI as Application Logic, Not Infrastructure
Keep AI orchestration at the application layer. Never let AI agents call
infrastructure APIs directly. Wrap all side effects in audited plugins that
enforce business rules independently of what the model decides.




```
- 138 -
```


<a id='p139'></a>
<!-- Página 139 -->

```
C# 2026: Enterprise Mastery



```

21.3 Retrieval-Augmented Generation (RAG)
RAG is the standard pattern for grounding AI responses in your own data.
You chunk documents, embed them into a vector store, and at query time
you retrieve the top-k relevant chunks and inject them into the model
prompt.


// Chapter21/RagPipeline.cs
public class RagSearchService
{
```
private readonly IEmbeddingGenerator<string,
```

Embedding<float>> _embeddings;
```
private readonly IVectorStore _store;
private readonly IChatClient _chat;

public RagSearchService(
IEmbeddingGenerator<string, Embedding<float>>
```

embeddings,
```
IVectorStore store,
IChatClient chat)
{
_embeddings = embeddings;
_store = store;
_chat = chat;
}

public async Task<string> AnswerAsync(string question)
{
// 1. Embed the question
var questionEmbedding = await
```

_embeddings.GenerateEmbeddingVectorAsync(question);

```
// 2. Retrieve top 5 relevant chunks
var collection = _store.GetCollection<string,
```

KnowledgeChunk>("docs");
```
var results = await
```

collection.VectorizedSearchAsync(questionEmbedding,
```
new VectorSearchOptions { Top = 5 });

// 3. Build context
var context = new StringBuilder();
await foreach (var result in results.Results)

- 139 -
```


<a id='p140'></a>
<!-- Página 140 -->

```
C# 2026: Enterprise Mastery


context.AppendLine(result.Record.Content);

// 4. Prompt with grounding
var prompt = "Answer the question using ONLY the
```

context below. " +
```
"If the answer is not in the context,
```

say I do not know. " +
```
"Context: " + context + " Question: "
```

+ question;

```
var response = await _chat.CompleteAsync(prompt);
return response.Message.Text ?? string.Empty;
}
```

}




21.4 Streaming Responses
Streaming AI responses dramatically improves perceived latency. MEAI
supports streaming natively through IAsyncEnumerable.


// Chapter21/StreamingExample.cs
// Minimal API endpoint streaming AI response
app.MapGet("/chat/stream", async (string question,
IChatClient chat,
```
CancellationToken ct) =>
```

{
```
return Results.Stream(async stream =>
{
var writer = new StreamWriter(stream);
await foreach (var update in
```

chat.CompleteStreamingAsync(question, null, ct))
```
{
if (update.Text is { Length: > 0 } text)
{
await writer.WriteAsync($"data: {text}

```

");
```
await writer.FlushAsync(ct);
}
}

- 140 -
```


<a id='p141'></a>
<!-- Página 141 -->

```
C# 2026: Enterprise Mastery


}, "text/event-stream");
```

});




21.5 Structured Outputs
Never parse free-text JSON from AI models by hand. Use structured
output mode (guaranteed JSON schema compliance) or at minimum use
JsonSerializerOptions with a strict schema.


// Chapter21/StructuredOutput.cs
public record ProductAnalysis(
```
string Sentiment,
int Score,
List<string> Keywords,
string Summary);

```

public class ReviewAnalyzer
{
```
private readonly IChatClient _chat;

public ReviewAnalyzer(IChatClient chat) => _chat =
```

chat;

```
public async Task<ProductAnalysis> AnalyzeAsync(string
```

reviewText)
```
{
// OpenAI structured output — guaranteed to match
// schema
var options = new ChatOptions
{
ResponseFormat =
```

ChatResponseFormat.ForJsonSchema(

JsonSerializerOptions.Default.GetJsonSchemaAsNode(
```
typeof(ProductAnalysis)))
};

var response = await _chat.CompleteAsync(
$"Analyze this product review: {reviewText}",
```

options);

```
- 141 -
```


<a id='p142'></a>
<!-- Página 142 -->

```
C# 2026: Enterprise Mastery




return JsonSerializer.Deserialize<ProductAnalysis>(
response.Message.Text!)!;
}
```

}




21.6 Token Usage and Cost Tracking
AI API calls have a real cost. Track token usage per request, per user, and
per feature. Set budgets and alert before you exceed them.


// Chapter21/TokenTracking.cs
public class TokenTrackingMiddleware : DelegatingChatClient
{
```
private readonly ITokenUsageStore _store;

public TokenTrackingMiddleware(IChatClient inner,
```

ITokenUsageStore store)
```
: base(inner) => _store = store;

public override async Task<ChatCompletion>
```

CompleteAsync(
```
IList<ChatMessage> messages,
ChatOptions? options = null,
CancellationToken ct = default)
{
var result = await base.CompleteAsync(messages,
```

options, ct);

```
if (result.Usage is { } usage)
{
await _store.RecordAsync(new TokenRecord
{
Timestamp = DateTimeOffset.UtcNow,
InputTokens = usage.InputTokenCount ?? 0,
OutputTokens = usage.OutputTokenCount ?? 0,
ModelId = result.ModelId ?? "unknown"
});
}
return result;

- 142 -
```


<a id='p143'></a>
<!-- Página 143 -->

```
C# 2026: Enterprise Mastery


}
```

}





## KEY TAKEAWAYS

– Microsoft.Extensions.AI provides provider-agnostic interfaces —
design against IChatClient, not against a specific SDK.
– Semantic Kernel is the right tool for multi-step AI orchestration,
agents, and plugin-based function calling.
– RAG is the standard for grounding AI in your own data without
fine-tuning.
– Always use structured output mode; never rely on ad-hoc JSON
parsing.
– Track token usage and cost from day one — AI spend surprises are
real.




```
- 143 -
```


<a id='p144'></a>
<!-- Página 144 -->

```
C# 2026: Enterprise Mastery




```

- 144 -

<a id='p145'></a>
<!-- Página 145 -->

```
C# 2026: Enterprise Mastery


```


## PART VI — THE 2026 FRONTIER


## CHAPTER 22




Cloud-Na,ve C# with .NET Aspire
```
and Kubernetes

```

.NET Aspire arrived as a preview and matured into the standard way to
build, run, and deploy distributed .NET applications. Combined with
Kubernetes and the broader CNCF ecosystem, it gives C# teams a complete
cloud-native platform that doesn't require a dedicated DevOps team to
```
operate.


```

22.1 What .NET Aspire Actually Is
.NET Aspire is a stack of opinionated, cloud-ready components: an
AppHost for orchestrating local development, a ServiceDefaults project for
standardised telemetry and health checks, and a set of integration
packages for Redis, PostgreSQL, RabbitMQ, and more. It is not a hosting
platform — it is a developer experience layer that integrates with
whatever host you use in production.


// Chapter22/AppHost/Program.cs
```
var builder = DistributedApplication.CreateBuilder(args);

```

// Infrastructure resources — Aspire provisions these in
// containers locally
```
var postgres = builder.AddPostgres("postgres")
.WithPgAdmin();

var redis = builder.AddRedis("redis")
.WithRedisInsight();

var rabbit = builder.AddRabbitMQ("messaging");

- 145 -
```


<a id='p146'></a>
<!-- Página 146 -->

```
C# 2026: Enterprise Mastery




```

// Application services with dependencies wired
// automatically
```
var catalog =
```

builder.AddProject<Projects.CatalogService>("catalog")
```
.WithReference(postgres)
.WithReference(redis);

var orders =
```

builder.AddProject<Projects.OrderService>("orders")
```
.WithReference(postgres)
.WithReference(rabbit)
.WithReference(catalog);

```

builder.AddProject<Projects.ApiGateway>("gateway")
```
.WithReference(catalog)
.WithReference(orders)
.WithExternalHttpEndpoints();

```

builder.Build().Run();




22.2 ServiceDefaults — Telemetry Out of the Box

// Chapter22/ServiceDefaults/Extensions.cs
public static class Extensions
{
```
public static IHostApplicationBuilder
```

AddServiceDefaults(
```
this IHostApplicationBuilder builder)
{
builder.ConfigureOpenTelemetry();
builder.AddDefaultHealthChecks();
builder.Services.AddServiceDiscovery();
builder.Services.ConfigureHttpClientDefaults(http
```

=>
```
{
http.AddStandardResilienceHandler();
http.AddServiceDiscovery();
});
return builder;

- 146 -
```


<a id='p147'></a>
<!-- Página 147 -->

```
C# 2026: Enterprise Mastery


}

static void ConfigureOpenTelemetry(this
```

IHostApplicationBuilder builder)
```
{
builder.Logging.AddOpenTelemetry(log =>
{
log.IncludeFormattedMessage = true;
log.IncludeScopes = true;
});

builder.Services.AddOpenTelemetry()
.WithMetrics(m => m
.AddAspNetCoreInstrumentation()
.AddHttpClientInstrumentation()
.AddRuntimeInstrumentation())
.WithTracing(t => t
.AddAspNetCoreInstrumentation()
.AddHttpClientInstrumentation()
.AddEntityFrameworkCoreInstrumentation());

builder.AddOpenTelemetryExporters();
}
```

}




22.3 Kubernetes Deployment Patterns for .NET
Aspire handles local orchestration. In production you target Kubernetes.
The key patterns for .NET services in Kubernetes are: graceful shutdown,
readiness vs liveness probes, and correct resource requests and limits.


# Chapter22/catalog-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
```
name: catalog-service
```

spec:
```
replicas: 3
selector:
matchLabels:

- 147 -
```


<a id='p148'></a>
<!-- Página 148 -->

```
C# 2026: Enterprise Mastery


app: catalog-service
```

template:
```
spec:
terminationGracePeriodSeconds: 30
containers:
- name: catalog
image: myregistry/catalog-service:latest
ports:
- containerPort: 8080
resources:
requests:
cpu: "250m"
memory: "256Mi"
limits:
cpu: "1000m"
memory: "512Mi"
readinessProbe:
httpGet:
path: /health/ready
port: 8080
initialDelaySeconds: 5
periodSeconds: 10
livenessProbe:
httpGet:
path: /health/live
port: 8080
initialDelaySeconds: 30
periodSeconds: 30
lifecycle:
preStop:
exec:
command: ["/bin/sh", "-c", "sleep 5"]




```

// Chapter22/GracefulShutdown.cs
// In Program.cs — essential for zero-downtime Kubernetes
// rolling updates
```
var app = builder.Build();
```

app.Lifetime.ApplicationStopping.Register(() =>
{
```
// Give the load balancer time to stop routing traffic
Thread.Sleep(5000);

- 148 -
```


<a id='p149'></a>
<!-- Página 149 -->

```
C# 2026: Enterprise Mastery


```

});

// Health endpoint — Kubernetes uses this for
// readiness/liveness
app.MapHealthChecks("/health/ready", new HealthCheckOptions
{
```
Predicate = check => check.Tags.Contains("ready"),
ResponseWriter =
```

UIResponseWriter.WriteHealthCheckUIResponse
});
app.MapHealthChecks("/health/live", new HealthCheckOptions
{
```
// Only checks if app is alive, not dependencies
Predicate = _ => false
```

});




22.4 Horizontal Pod Autoscaling with KEDA
Kubernetes HPA scales on CPU and memory. KEDA (Kubernetes
Event-Driven Autoscaling) scales on queue depth, message lag, or any
custom metric — which is far more meaningful for event-driven .NET
services.


# Chapter22/keda-scaledobject.yaml
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
```
name: orders-processor-scaler
```

spec:
```
scaleTargetRef:
name: orders-processor
minReplicaCount: 1
maxReplicaCount: 20
cooldownPeriod: 60
triggers:
- type: rabbitmq
metadata:
host: amqp://rabbitmq.default.svc.cluster.local
queueName: orders


- 149 -
```


<a id='p150'></a>
<!-- Página 150 -->

```
C# 2026: Enterprise Mastery


queueLength: "50" # Scale up when queue depth > 50
```

per replica





## KEY TAKEAWAYS

– .NET Aspire solves the local development complexity of distributed
systems — use it from day one, even for small projects.
– ServiceDefaults gives you production-grade telemetry in a single
method call — never skip it.
– Always define readiness AND liveness probes; they serve different
purposes and both are required for reliable Kubernetes deployments.
– KEDA scales on what matters — queue depth, event lag, custom
metrics — not just CPU which is often a poor proxy for load.




```
- 150 -
```


<a id='p151'></a>
<!-- Página 151 -->

```
C# 2026: Enterprise Mastery




```

- 151 -

<a id='p152'></a>
<!-- Página 152 -->

```
C# 2026: Enterprise Mastery


```


## PART VI — THE 2026 FRONTIER


## CHAPTER 23




```
C# 2026 Features: What Makes
Sense and What Doesn't

```

Every language release brings features that sound exciting in a conference
talk but require careful judgment in production code. This chapter gives
```
you the un8ltered opinion of someone who has shipped high-traf8c
```

systems: which features deserve a place in your daily toolkit, which require
discipline to use well, and which you should avoid outright in enterprise
```
code.


```

23.1 Primary Constructors — Use Them
Selectively
Primary constructors landed in C# 12 and are now mainstream. They
work beautifully for simple services and records, but they erode
encapsulation in complex classes because the parameters are in scope
throughout the entire class body.


// Chapter23/PrimaryConstructors.cs

// GOOD: simple service — primary constructor shines here
public class OrderValidator(ILogger<OrderValidator> logger,
IOptions<OrderRules> options)
{
```
private readonly OrderRules _rules = options.Value;

public ValidationResult Validate(Order order)
{
logger.LogDebug("Validating order {Id}", order.Id);
return order.Amount > _rules.MaxAmount

- 152 -
```


<a id='p153'></a>
<!-- Página 153 -->

```
C# 2026: Enterprise Mastery


? ValidationResult.Fail("Amount exceeds limit")
: ValidationResult.Ok();
}
```

}

// BAD: complex domain class — primary constructor
// parameters leak everywhere
// Avoid: the 'config' parameter is accessible in all 200
// lines of this class
// making it hard to reason about what actually uses it
public class ComplexDomainService(AppConfig config,
IRepository repo, ICache cache,
```
IEventBus bus, ILogger<ComplexDomainService> logger)
```

{
```
// 200 lines of complex logic...
// 'config' is accessible in all of them, which is
// confusing
```

}

// BETTER for complex classes: explicit field assignments
// remain clearer
public class ComplexDomainService
{
```
private readonly AppConfig _config;
private readonly IRepository _repo;
// ... explicit fields make it obvious what this class
// actually uses
```

}




23.2 Collection Expressions — Adopt Widely
Collection expressions are one of the cleanest additions to modern C#.
They work across arrays, List<T>, Span<T>, ImmutableArray<T>, and
ReadOnlySpan<T>, using the same concise syntax.


// Chapter23/CollectionExpressions.cs
// Before C# 12:
int[] oldWay = new int[] { 1, 2, 3 };
List<string> oldList = new List<string> { "a", "b", "c" };


```
- 153 -
```


<a id='p154'></a>
<!-- Página 154 -->

```
C# 2026: Enterprise Mastery


```

ImmutableArray<int> oldImmutable = ImmutableArray.Create(1,
2, 3);

// C# 12+ collection expressions — consistent syntax
// everywhere:
int[] array = [1, 2, 3];
List<string> list = ["a", "b", "c"];
ImmutableArray<int> immutable = [1, 2, 3];
Span<byte> span = [0x01, 0x02, 0x03];

// Spread operator merges collections:
int[] first = [1, 2, 3];
int[] second = [4, 5, 6];
// [1,2,3,4,5,6]
int[] combined = [..first, ..second];
// [0,1,2,3,4,5,6,7]
int[] withExtra = [0, ..first, ..second, 7];

// In methods — clean and expressive:
public static ReadOnlySpan<string> GetDefaultHeaders() =>
```
["Content-Type", "Authorization", "X-Request-Id"];




```

23.3 Field Keyword — Handle With Care
The field keyword (C# 13, stabilised in 2026) allows access to the
compiler-generated backing field inside property accessors, enabling
custom validation without a separate field declaration. It is useful for
records and simple cases; avoid it in complex validation scenarios where
the logic belongs in the domain model.


// Chapter23/FieldKeyword.cs
// GOOD: eliminates boilerplate for simple validated
// properties
public class UserProfile
{
```
public string Email
{
get => field;
set => field = value?.Trim().ToLowerInvariant()


- 154 -
```


<a id='p155'></a>
<!-- Página 155 -->

```
C# 2026: Enterprise Mastery


?? throw new
```

ArgumentNullException(nameof(value));
```
}

public int Age
{
get => field;
set => field = value is >= 0 and <= 150
? value
: throw new
```

ArgumentOutOfRangeException(nameof(value));
```
}
```

}

// CAUTION: don't put complex business logic in property
// setters
// If validation requires calling a service or raising an
// event,
// use a factory method or domain method instead of a
// property setter




23.4 Params Collections — A Clear Win
Params collections in C# 13 allow params to work with any collection
type, not just arrays. The biggest benefit is params ReadOnlySpan<T>,
which avoids the heap allocation that params T[] incurs.


// Chapter23/ParamsCollections.cs
// C# 13: params works with spans — zero allocation on the
// hot path
public static int Sum(params ReadOnlySpan<int> numbers)
{
```
int total = 0;
foreach (var n in numbers) total += n;
return total;
```

}

// Caller syntax is unchanged — the compiler optimises the
// allocation
// No array allocated on the heap

```
- 155 -
```


<a id='p156'></a>
<!-- Página 156 -->

```
C# 2026: Enterprise Mastery


```

int result = Sum(1, 2, 3, 4, 5);

// Works with IEnumerable<T> too for API flexibility
public void LogValues(params IEnumerable<string> values)
{
```
foreach (var v in values) Console.WriteLine(v);
```

}




23.5 What to Avoid: Overuse of Pattern Matching
Pattern matching is powerful but it is not a replacement for
polymorphism and domain design. When you find yourself writing switch
expressions that branch on type or state across multiple places in the
codebase, you have a design problem, not a missing language feature.


// Chapter23/PatternMatchingAbuse.cs
// PROBLEMATIC: pattern matching scattered across the
// codebase
// Every place that uses Shape must know about all concrete
// types
decimal CalculateArea(Shape shape) => shape switch
{
```
Circle c => Math.PI * c.Radius * c.Radius,
Rectangle r => r.Width * r.Height,
Triangle t => 0.5m * t.Base * t.Height,
_ => throw new NotSupportedException()
```

};

string Describe(Shape shape) => shape switch
{
```
Circle c when c.Radius > 10 => "Large circle",
Circle => "Small circle",
Rectangle r when r.Width == r.Height => "Square",
Rectangle => "Rectangle",
_ => "Unknown"
```

};

// BETTER: polymorphism — new shapes require changes in one
// place only
public abstract class Shape

```
- 156 -
```


<a id='p157'></a>
<!-- Página 157 -->

```
C# 2026: Enterprise Mastery


```

{
```
public abstract decimal Area { get; }
public abstract string Describe();
```

}

public class Circle(decimal radius) : Shape
{
```
public override decimal Area => (decimal)Math.PI *
```

radius * radius;
```
public override string Describe() => radius > 10 ?
```

"Large circle" : "Small circle";
}





## KEY TAKEAWAYS

– Adopt collection expressions broadly — they are consistent,
expressive, and allocation-efficient with spans.
– Use primary constructors for simple services; prefer explicit fields for
complex domain classes.
– The field keyword removes setter boilerplate cleanly — do not use it
for complex validation logic.
– Pattern matching is powerful for type dispatch at boundaries; it is not
a substitute for good OOP design inside the domain.
– Evaluate features against your team's context — a language feature
that is a clear win in a library is not necessarily right for enterprise
application code.




```
- 157 -
```


<a id='p158'></a>
<!-- Página 158 -->

```
C# 2026: Enterprise Mastery




```

- 158 -

<a id='p159'></a>
<!-- Página 159 -->

```
C# 2026: Enterprise Mastery


```


## PART VII — TRANSFORMATION AND WISDOM


## CHAPTER 24




```
Refactoring Legacy C# Code

```

Most of the C# code that needs to be written in 2026 already exists. It was
written in .NET Framework 4.x, before async/await was ubiquitous, before
the GC improvements of modern .NET, before anyone had heard of Span<T>
or minimal APIs. Refactoring this code is not glamorous work, but it is
where the most business value lives. This chapter gives you a systematic
```
approach.


```

24.1 The Strangler Fig Pattern at Scale
The Strangler Fig pattern, popularised by Martin Fowler, describes
incrementally replacing a legacy system by routing requests to a new
implementation alongside the old one, gradually strangling the legacy
code out of existence. In C# practice this usually means introducing an
API Gateway or YARP reverse proxy in front of a .NET Framework
monolith.


// Chapter24/YarpStrangler.cs
// YARP (Yet Another Reverse Proxy) — route traffic between
// old and new
```
var builder = WebApplication.CreateBuilder(args);
```

builder.Services.AddReverseProxy()
```
.LoadFromConfig(builder.Configuration.GetSection("Rever
```

seProxy"));

```
var app = builder.Build();

```

// Custom middleware: route /api/orders to new service,
// everything else to legacy
app.Use(async (context, next) =>


```
- 159 -
```


<a id='p160'></a>
<!-- Página 160 -->

```
C# 2026: Enterprise Mastery


```

{
```
if
```

(context.Request.Path.StartsWithSegments("/api/orders") &&
```
FeatureFlags.IsEnabled("NewOrderService"))
{
context.Request.Headers["X-Route"] = "new";
}
await next(context);
```

});

app.MapReverseProxy();
app.Run();




24.2 Migrating Synchronous Code to Async
The most impactful refactoring in legacy .NET code is the async
migration. A synchronous ASP.NET application blocks a thread for every
I/O operation. A modern async application can serve thousands of
concurrent requests with the same thread pool. The migration follows a
clear pattern.


// Chapter24/AsyncMigration.cs
// LEGACY: sync, blocking, thread-hungry
public class OrderService
{
```
public Order GetOrder(int id)
{
using var conn = new
```

SqlConnection(_connectionString);
```
conn.Open(); // Blocks a thread
return conn.QuerySingle<Order>("SELECT * FROM
```

Orders WHERE Id = @id", new { id });
```
}
```

}

// STEP 1: Add async overload, keep sync for now (don't
// break callers)
public class OrderService
{


```
- 160 -
```


<a id='p161'></a>
<!-- Página 161 -->

```
C# 2026: Enterprise Mastery


public Order GetOrder(int id) =>
```

GetOrderAsync(id).GetAwaiter().GetResult();

```
public async Task<Order> GetOrderAsync(int id)
{
using var conn = new
```

SqlConnection(_connectionString);
```
await conn.OpenAsync();
return await conn.QuerySingleAsync<Order>(
"SELECT * FROM Orders WHERE Id = @id", new { id
```

});
```
}
```

}

// STEP 2: Migrate callers to async; remove sync overload
// STEP 3: Fix any ConfigureAwait(false) in library code
// STEP 4: Remove all .Result and .GetAwaiter().GetResult()
// calls

// WARNING: Never call .Result on a Task in ASP.NET — it
// deadlocks
// The async migration must be bottom-up: data layer first,
// then services, then controllers




24.3 Eliminating God Classes
God classes — classes with hundreds of methods and thousands of lines
— are the single biggest source of maintenance pain in legacy C#
codebases. The Extract Class refactoring is the remedy. Apply it one
cohesive group of methods at a time, guided by what data each group uses.


// Chapter24/GodClassRefactoring.cs
// BEFORE: LegacyOrderManager has 80 methods, 2000 lines
public class LegacyOrderManager
{
```
// Pricing logic — 20 methods
public decimal CalculatePrice(Order order) { /* ...
```

*/ }
```
public decimal ApplyDiscount(Order order, Discount d) {
```

/* ... */ }

```
- 161 -
```


<a id='p162'></a>
<!-- Página 162 -->

```
C# 2026: Enterprise Mastery




// Validation logic — 15 methods
public bool ValidateOrder(Order order) { /* ... */ }
public IList<string> GetValidationErrors(Order order) {
```

/* ... */ }

```
// Fulfillment logic — 25 methods
public void Reserve(Order order) { /* ... */ }
public void Ship(Order order) { /* ... */ }
```

}

// AFTER: Extract by cohesion — each class has a single
// responsibility
public class OrderPricingService
{
```
public decimal Calculate(Order order) { /* ... */ }
public decimal ApplyDiscount(Order order, Discount d) {
```

/* ... */ }
}

public class OrderValidator
{
```
public ValidationResult Validate(Order order) { /* ...
```

*/ }
}

public class FulfillmentService
{
```
public async Task ReserveAsync(Order order) { /* ... */
```

}
```
public async Task ShipAsync(Order order) { /* ... */ }
```

}

// Façade to maintain backward compatibility during
// migration
public class LegacyOrderManager
{
```
private readonly OrderPricingService _pricing;
private readonly OrderValidator _validator;
private readonly FulfillmentService _fulfillment;

public decimal CalculatePrice(Order order) =>
```

_pricing.Calculate(order);


```
- 162 -
```


<a id='p163'></a>
<!-- Página 163 -->

```
C# 2026: Enterprise Mastery


public bool ValidateOrder(Order order) =>
```

_validator.Validate(order).IsValid;
```
public void Reserve(Order order) =>
```

_fulfillment.ReserveAsync(order).Wait();
}




24.4 Migrating from .NET Framework to .NET 10
The .NET Upgrade Assistant and the Platform Compatibility Analyzer
automate the mechanical parts of the migration. What they cannot do is
replace the judgment required to decide which dependencies to update,
which to replace, and which to eliminate.


// Chapter24/MigrationChecklist.cs
// Step 1: Run upgrade-assistant to get the migration
// report
// dotnet tool install -g upgrade-assistant
// upgrade-assistant analyze MyApp.sln

// Step 2: Address API compatibility issues
// Common .NET Framework APIs removed in modern .NET:

// REMOVED: HttpContext.Current (thread-static,
// incompatible with async)
// REPLACE: inject IHttpContextAccessor
public class LegacyService
{
```
private readonly IHttpContextAccessor _http;
public LegacyService(IHttpContextAccessor http) =>
```

_http = http;

```
public string GetCurrentUser() =>
_http.HttpContext?.User.Identity?.Name ??
```

"anonymous";
}

// REMOVED: ConfigurationManager.AppSettings
// REPLACE: IConfiguration
public class LegacyConfig
{

```
- 163 -
```


<a id='p164'></a>
<!-- Página 164 -->

```
C# 2026: Enterprise Mastery


private readonly IConfiguration _config;
public LegacyConfig(IConfiguration config) => _config =
```

config;

```
public string GetSetting(string key) => _config[key] ??
```

string.Empty;
}

// REMOVED: Thread.Abort
// REPLACE: CancellationToken throughout the call stack





## KEY TAKEAWAYS

– Use the Strangler Fig pattern — never attempt a big-bang rewrite of a
production system.
– The async migration is the highest-ROI refactoring in legacy .NET
code; do it bottom-up and never mix .Result with async code.
– God class elimination follows the data: methods that use the same
fields belong in the same class.
– The .NET Upgrade Assistant handles 70% of the mechanical migration
work; the remaining 30% requires engineering judgment.
– Always maintain backward compatibility during refactoring through
façades or adapter classes until all callers are updated.




```
- 164 -
```


<a id='p165'></a>
<!-- Página 165 -->

```
C# 2026: Enterprise Mastery




```

- 165 -

<a id='p166'></a>
<!-- Página 166 -->

```
C# 2026: Enterprise Mastery


```


## PART VII — TRANSFORMATION AND WISDOM


## CHAPTER 25




An,-Pa'erns: The Hall of Shame

```
Experience is knowing which mistakes not to make. This chapter
```

catalogues the most damaging anti-patterns found in real C# enterprise
codebases — patterns that compile, pass code review, and then quietly
destroy performance, reliability, or maintainability in production. Each
```
entry shows the problem, the consequence, and the remedy.


```

25.1 async void
async void methods cannot be awaited, exceptions they throw are
unobservable (they crash the process), and they make unit testing nearly
impossible. The only legitimate use is event handlers in UI frameworks. In
all other contexts, return Task.


// Chapter25/AsyncVoid.cs
// ANTI-PATTERN: unhandled exceptions crash the process
// silently
public async void ProcessOrderAsync(int orderId)
{
```
var order = await _repo.GetAsync(orderId);
// If this throws, process crashes
await _processor.ProcessAsync(order);
```

}

// CORRECT: return Task, let the caller handle exceptions
public async Task ProcessOrderAsync(int orderId)
{
```
var order = await _repo.GetAsync(orderId);
await _processor.ProcessAsync(order);
```

}


```
- 166 -
```


<a id='p167'></a>
<!-- Página 167 -->

```
C# 2026: Enterprise Mastery


```

// The ONLY acceptable async void: event handlers
private async void OnSubmitButton_Click(object sender,
EventArgs e)
{
```
try { await ProcessOrderAsync(CurrentOrderId); }
catch (Exception ex) { ShowError(ex.Message); }
```

}
// Note: even here, wrap in try/catch — exceptions still
// uncatchable at call site




25.2 The Repository-Over-Repository
Wrapping Entity Framework's DbContext in a generic IRepository<T>
interface is cargo-cult programming. DbContext is already a unit of work
and repository. Adding another layer of abstraction gives you a leaky
abstraction that fights EF Core's query composability.


// Chapter25/RepositoryAntiPattern.cs
// ANTI-PATTERN: generic repository wrapping EF Core
public interface IRepository<T>
{
```
Task<T?> GetByIdAsync(int id);
Task<IEnumerable<T>> GetAllAsync();
Task AddAsync(T entity);
Task UpdateAsync(T entity);
Task DeleteAsync(T entity);
```

}

// Problems:
// 1. GetAllAsync() loads the entire table — no query
// composition
// 2. No way to express eager loading, projections, or
// filters
// 3. Forces EF-specific concepts through the interface
// anyway
// 4. Tests mock the repository, not the database — catches
// no query bugs

// BETTER: use DbContext directly in application services
public class OrderApplicationService

```
- 167 -
```


<a id='p168'></a>
<!-- Página 168 -->

```
C# 2026: Enterprise Mastery


```

{
```
private readonly OrderDbContext _db;

public async Task<OrderDto[]> GetPendingOrdersAsync(int
```

customerId)
```
{
return await _db.Orders
.Where(o => o.CustomerId == customerId &&
```

o.Status == OrderStatus.Pending)
```
.Select(o => new OrderDto(o.Id, o.Amount,
```

o.CreatedAt))
```
.ToArrayAsync();
}
```

}

// If you need testability, use an in-memory SQLite
// database in tests
// It actually catches query bugs, unlike mocking
// IRepository




25.3 Fire-and-Forget Without Error Handling

// Chapter25/FireAndForget.cs
// ANTI-PATTERN: exceptions disappear silently
// If this throws, nothing handles it
_ = SendEmailAsync(user.Email);

// CORRECT: use a background task infrastructure
public class BackgroundTaskQueue
{
```
private readonly Channel<Func<CancellationToken, Task>>
```

_queue =
```
Channel.CreateBounded<Func<CancellationToken,
```

Task>>(100);

```
public async ValueTask
```

EnqueueAsync(Func<CancellationToken, Task> task)
```
=> await _queue.Writer.WriteAsync(task);




- 168 -
```


<a id='p169'></a>
<!-- Página 169 -->

```
C# 2026: Enterprise Mastery


public IAsyncEnumerable<Func<CancellationToken, Task>>
```

ReadAllAsync(
```
CancellationToken ct) =>
```

_queue.Reader.ReadAllAsync(ct);
}

// Worker processes tasks and logs failures properly
public class BackgroundTaskWorker : BackgroundService
{
```
protected override async Task
```

ExecuteAsync(CancellationToken ct)
```
{
await foreach (var task in _queue.ReadAllAsync(ct))
{
try { await task(ct); }
catch (Exception ex)
{
_logger.LogError(ex, "Background task
```

failed");
```
_metrics.RecordFailure();
}
}
}
```

}




25.4 ServiceLocator Inside Services

// Chapter25/ServiceLocator.cs
// ANTI-PATTERN: Service Locator — hides dependencies,
// impossible to test
public class OrderService
{
```
public async Task ProcessAsync(Order order)
{
// Hidden dep!
var validator =
```

ServiceLocator.Resolve<IOrderValidator>();
```
// Hidden dep!
var repo =
```

ServiceLocator.Resolve<IOrderRepository>();

```
- 169 -
```


<a id='p170'></a>
<!-- Página 170 -->

```
C# 2026: Enterprise Mastery


// ...
}
```

}

// CORRECT: explicit constructor injection — all
// dependencies visible
public class OrderService
{
```
private readonly IOrderValidator _validator;
private readonly IOrderRepository _repo;

public OrderService(IOrderValidator validator,
```

IOrderRepository repo)
```
{
_validator = validator;
_repo = repo;
}

public async Task ProcessAsync(Order order)
{
var result = await _validator.ValidateAsync(order);
if (!result.IsValid) throw new
```

ValidationException(result.Errors);
```
await _repo.SaveAsync(order);
}
```

}




25.5 Catching Exception Everywhere

// Chapter25/ExceptionHandling.cs
// ANTI-PATTERN: swallowing exceptions
public async Task<Order?> GetOrderAsync(int id)
{
```
try { return await _repo.GetAsync(id); }
// The exception is gone. Nobody knows.
catch (Exception) { return null; }
```

}

// ANTI-PATTERN: catching to rethrow without value
try { await DoWorkAsync(); }

```
- 170 -
```


<a id='p171'></a>
<!-- Página 171 -->

```
C# 2026: Enterprise Mastery


```

// Destroys the stack trace
catch (Exception ex) { throw ex; }

// CORRECT: only catch what you can handle; let the rest
// propagate
public async Task<Order?> GetOrderAsync(int id)
{
```
try { return await _repo.GetAsync(id); }
// Expected, handle it
catch (EntityNotFoundException) { return null; }
// SqlException, TimeoutException, etc. propagate to
// the global handler
```

}

// Global exception handler in ASP.NET Core (one place,
// full context)
app.UseExceptionHandler(handler =>
{
```
handler.Run(async context =>
{
var ex =
```

context.Features.Get<IExceptionHandlerFeature>()?.Error;
```
_logger.LogError(ex, "Unhandled exception for
```

request {Path}", context.Request.Path);
```
context.Response.StatusCode = 500;
await context.Response.WriteAsJsonAsync(new { error
```

= "An error occurred" });
```
});
```

});




25.6 The N+1 Query Problem

// Chapter25/NPlusOne.cs
// ANTI-PATTERN: N+1 — 1 query to get orders, then N
// queries for customers
```
var orders = await _db.Orders.ToListAsync();
```

foreach (var order in orders)
{
```
// This executes a new query for EACH order —
// catastrophic at scale

- 171 -
```


<a id='p172'></a>
<!-- Página 172 -->

```
C# 2026: Enterprise Mastery


var customer = await
```

_db.Customers.FindAsync(order.CustomerId);
```
Console.WriteLine($"{customer.Name}: {order.Amount}");
```

}

// CORRECT: use Include() for eager loading
```
var orders = await _db.Orders
.Include(o => o.Customer)
.ToListAsync();
```

// Single query with JOIN — linear cost regardless of row
// count

// EVEN BETTER: project to DTO — load only required columns
```
var summaries = await _db.Orders
.Select(o => new { o.Id, o.Amount, CustomerName =
```

o.Customer.Name })
```
.ToListAsync();




```


## KEY TAKEAWAYS

– async void is almost always wrong. Return Task; handle exceptions at
the call site or in a global handler.
– Generic repositories over EF Core add complexity without value.
DbContext is already a repository and unit of work.
– Fire-and-forget requires infrastructure. Use a background queue with
proper error handling and observability.
– Service Locator is the anti-DI pattern. Explicit constructor injection
always wins for testability.
– Catch the specific exception you can handle; let the rest propagate to a
single, observed global handler.
– The N+1 query problem is one of the most common performance
killers in EF Core applications. Use Include() or projections.




```
- 172 -
```


<a id='p173'></a>
<!-- Página 173 -->

```
C# 2026: Enterprise Mastery




```

Appendix A: C# Version History
Quick Reference
The following table summarises the major C# versions from 6.0 through
13.0, their .NET pairings, and the headline features that matter for
enterprise development.
Version .NET Pairing Key Features

C# 6 .NET 4.6 / Core 1.x String interpolation,
```
null-conditional ?.,
expression-bodied
members

```

C# 7.0 .NET Core 1.1 Tuples, pattern matching
```
(is), local functions, out
variables

```

C# 7.3 .NET Core 2.1 Span<T> in stackalloc,
```
blittable type constraints

```

C# 8.0 .NET Core 3.0 Nullable reference types,
```
async streams, switch
expressions,
indices/ranges

```

C# 9.0 .NET 5 Records, init-only setters,
```
top-level programs,
target-typed new

```

C# 10.0 .NET 6 Global using, file-scoped
```
namespaces, record
structs, const interpolated
strings

```

C# 11.0 .NET 7 Required members, raw
```
string literals, list patterns,
generic attributes

```

C# 12.0 .NET 8 Primary constructors,
```
collection expressions,
inline arrays, default


- 173 -
```


<a id='p174'></a>
<!-- Página 174 -->

```
C# 2026: Enterprise Mastery


lambda params

```

C# 13.0 .NET 9/10 Params collections, field
```
keyword, lock object type,
partial properties




- 174 -
```


<a id='p175'></a>
<!-- Página 175 -->

```
C# 2026: Enterprise Mastery




```

Appendix B: Performance Reference
This appendix deliberately avoids quoting absolute timings. Nanosecond
figures from one machine mislead more than they inform: results depend
on the CPU, the .NET runtime version, JIT warmup, dataset size, and
memory layout. What is stable across hardware is the relative ordering of
approaches and the allocation behaviour. Those are what this reference
captures. To get numbers for your own workload, write a
BenchmarkDotNet harness and run it on hardware representative of
production.

Memory Allocation: Relative Ranking
Ordered from most to least allocation pressure. The ranking holds across
runtimes; the absolute cost does not. The practical takeaway is that each
step down the list removes heap allocations, and removing allocations is
what reduces garbage-collection pressure under load.



// AppendixB/MemoryReference.cs
// Relative allocation behaviour (NOT absolute timings)

// Approach Heap allocation
// ----------------------------------------------------
// new int[100] Allocates an array on the heap
// ArrayPool<int>.Shared.Rent(100) No allocation after pool
// warmup
// stackalloc int[100] No heap allocation (stack only)
// Span<int> over existing array No allocation (a view, not
// a copy)
//
// string concatenation (+) in loop Allocates a new string
// each step
// StringBuilder Fewer allocations; one resize curve
// string.Create Single allocation, sized once
// Span-based string building Zero heap allocation when
// sized right

// Rule of thumb: if a method is on a hot path and

```
- 175 -
```


<a id='p176'></a>
<!-- Página 176 -->

```
C# 2026: Enterprise Mastery


```

// allocates per call,
// measure it. If it allocates per element, measure it
// urgently.




Collection Operations: What to Expect
Big-O complexity is stable and worth memorising; wall-clock time is not.
The table below gives algorithmic complexity, which is what should drive
data-structure choice.



// AppendixB/CollectionReference.cs
// Algorithmic complexity (stable across all hardware)

// Operation Complexity Notes
//
-----------------------------------------------------------
---
// List<T> Add O(1)* amortised; O(n) on resize
// List<T> indexer [i] O(1)
// List<T> Contains O(n) linear scan
// Dictionary<K,V> lookup O(1)* amortised; hash-dependent
// HashSet<T> Contains O(1)* amortised
// Array binary search O(log n) requires sorted array
// SortedList/SortedSet lookup O(log n)

// Pre-size collections when the count is known: it removes
// the
// resize curve entirely. new List<int>(expectedCount) is
// free insurance.

// LINQ vs. hand-written loops: LINQ adds
// delegate-invocation and
// iterator overhead per element. For most code this is
// irrelevant and
// LINQ's clarity wins. On measured hot paths, a plain loop
// or a
// Span<T> iteration removes that overhead. Measure before
// rewriting.


```
- 176 -
```


<a id='p177'></a>
<!-- Página 177 -->

```
C# 2026: Enterprise Mastery




```

- 177 -

<a id='p178'></a>
<!-- Página 178 -->

```
C# 2026: Enterprise Mastery




```

Appendix C: Recommended Tools
and Libraries 2026
The .NET ecosystem has outstanding open-source libraries. The following
are the tools and libraries that belong in every serious enterprise C#
project in 2026.

Testing
xUnit: Unit testing framework — clean, extensible, parallel by default

NSubstitute: Mocking — fluent API, no Setup/Verify boilerplate

FluentAssertions: Assertion library — readable test failures

Testcontainers: Real containers in tests — PostgreSQL, Redis, RabbitMQ

BenchmarkDotNet: Micro-benchmarking — the only trustworthy way to
measure


Observability
OpenTelemetry .NET: Vendor-agnostic traces, metrics, logs — use this
everywhere

Serilog: Structured logging — JSON output to any sink

Polly: Resilience: retry, circuit breaker, rate limiter


Data Access
Entity Framework Core: Primary ORM for relational databases

Dapper: Lightweight micro-ORM for raw SQL performance-critical paths

MassTransit: Messaging abstraction over RabbitMQ, Azure Service Bus, etc.


HTTP & APIs
Refit: Type-safe REST client — no boilerplate HttpClient code

```
- 178 -
```


<a id='p179'></a>
<!-- Página 179 -->

```
C# 2026: Enterprise Mastery


```

Carter: Minimal API module pattern — organises endpoint classes

FastEndpoints: Fast, clean Minimal API alternative with built-in validation


Security
Duende IdentityServer: OpenID Connect/OAuth2 server for custom auth

Azure.Identity: Managed identity — no secrets in code


Developer Experience
.NET Aspire: Local development orchestration for distributed applications

Bogus: Fake data generation for tests and demos

Scrutor: Assembly scanning for DI registration — no manual wiring


Deep Dive: BenchmarkDotNet in Production
Pipelines
Benchmark-driven development means running BenchmarkDotNet in
your CI pipeline and failing the build when a performance regression is
detected. This elevates performance from a reactive concern to a
first-class quality gate.


// Supplement/PerfBenchmarks.cs
[MemoryDiagnoser]
[SimpleJob]
public class StringProcessingBenchmarks
{
```
private const string Input = "The quick brown fox jumps
```

over the lazy dog";

```
[Benchmark(Baseline = true)]
public string StringConcat()
{
var result = "";
foreach (var word in Input.Split(' '))
result += word.ToUpper() + " ";
return result.TrimEnd();

- 179 -
```


<a id='p180'></a>
<!-- Página 180 -->

```
C# 2026: Enterprise Mastery


}

[Benchmark]
public string StringBuilder()
{
var sb = new StringBuilder();
foreach (var word in Input.Split(' '))
sb.Append(word.ToUpper()).Append(' ');
if (sb.Length > 0) sb.Length--;
return sb.ToString();
}

[Benchmark]
public string StringCreate()
{
var words = Input.Split(' ');
var totalLen = Input.Length;
return string.Create(totalLen, words, (span, ws) =>
{
int pos = 0;
foreach (var w in ws)
{

```

w.ToUpperInvariant().AsSpan().CopyTo(span[pos..]);
```
pos += w.Length;
if (pos < span.Length) span[pos++] = ' ';
}
});
}

[Benchmark]
public string SpanProcessing()
{
Span<char> buffer = stackalloc char[Input.Length];
Input.AsSpan().CopyTo(buffer);
for (int i = 0; i < buffer.Length; i++)
if (buffer[i] != ' ') buffer[i] =
```

char.ToUpper(buffer[i]);
```
return buffer.ToString();
}
```

}

// Relative results (run BenchmarkDotNet yourself for
// absolute numbers —

```
- 180 -
```


<a id='p181'></a>
<!-- Página 181 -->

```
C# 2026: Enterprise Mastery


```

// they depend on CPU, runtime version, dataset, and JIT
// warmup):
//
// | Method | Relative speed | Allocations |
//
|----------------|----------------|----------------------|
// | StringConcat | baseline (1x) | highest — grows O(n) |
// | StringBuilder | several x | moderate |
// | StringCreate | faster still | low |
// | SpanProcessing | fastest | zero heap |
//
// The ranking is stable across hardware; the magnitudes
// are not.
// What matters: each step down this list removes
// allocation pressure.




Object Pooling for Expensive Resources
Object pools amortise the cost of expensive object creation across many
requests. In high-throughput systems, even 'cheap' allocations add GC
pressure. The ObjectPool<T> in Microsoft.Extensions.ObjectPool is the
right tool for most scenarios.


// Supplement/ObjectPooling.cs
using Microsoft.Extensions.ObjectPool;

// 1. Register a pool in DI
builder.Services.AddSingleton<ObjectPool<StringBuilder>>(sp
=>
{
```
var provider = new DefaultObjectPoolProvider();
return
```

provider.CreateStringBuilderPool(initialCapacity: 256,
maximumRetainedCapacity: 4096);
});

// 2. Use the pool in a service
public class ReportFormatter
{
```
private readonly ObjectPool<StringBuilder> _pool;

- 181 -
```


<a id='p182'></a>
<!-- Página 182 -->

```
C# 2026: Enterprise Mastery




public ReportFormatter(ObjectPool<StringBuilder> pool)
```

=> _pool = pool;

```
public string Format(IEnumerable<ReportLine> lines)
{
var sb = _pool.Get();
try
{
foreach (var line in lines)
{
sb.Append(line.Date.ToString("yyyy-MM-dd"))
.Append(' ')
.AppendLine(line.Description);
}
return sb.ToString();
}
finally
{
// Always return — use try/finally
_pool.Return(sb);
}
}
```

}

// 3. Custom pooled object — implement IResettable for
// auto-reset
public class ParseContext : IResettable
{
```
public List<Token> Tokens { get; } = new(64);
public Dictionary<string, object> Variables { get; } =
```

new(16);
```
public int Position { get; set; }

public bool TryReset()
{
Tokens.Clear();
Variables.Clear();
Position = 0;
// Return false to discard the object instead of
// pooling it
return true;
}
```

}

```
- 182 -
```


<a id='p183'></a>
<!-- Página 183 -->

```
C# 2026: Enterprise Mastery




```

builder.Services.AddSingleton(
```
new DefaultObjectPool<ParseContext>(new
```

DefaultPooledObjectPolicy<ParseContext>()));




Reducing Allocations with Struct Enumerators
LINQ's IEnumerable<T> chains heap-allocate enumerator objects. For
performance-critical inner loops you can write struct enumerators that
give the same ergonomics with zero allocation.


// Supplement/StructEnumerator.cs
// Custom struct enumerator: zero allocation,
// foreach-compatible
public readonly struct RangeEnumerable
{
```
private readonly int _start;
private readonly int _end;
private readonly int _step;

public RangeEnumerable(int start, int end, int step =
```

1)
```
{
_start = start;
_end = end;
_step = step;
}

public Enumerator GetEnumerator() => new
```

Enumerator(_start, _end, _step);

```
public struct Enumerator
{
private int _current;
private readonly int _end;
private readonly int _step;

internal Enumerator(int start, int end, int step)
{
_current = start - step;

- 183 -
```


<a id='p184'></a>
<!-- Página 184 -->

```
C# 2026: Enterprise Mastery


_end = end;
_step = step;
}

public int Current => _current;

public bool MoveNext()
{
_current += _step;
return _current < _end;
}
}
```

}

// Usage — identical to foreach over IEnumerable<int> but
// zero allocs
foreach (var i in new RangeEnumerable(0, 1_000_000, 2))
{
```
Process(i);
```

}

// The compiler uses duck typing: GetEnumerator() returning
// a struct
// with Current/MoveNext is sufficient — no IEnumerable
// needed




Efficient JSON Processing at Scale
System.Text.Json is the high-performance JSON library in .NET. For
maximum throughput, use source generation to avoid runtime reflection
and Utf8JsonReader/Utf8JsonWriter for streaming document processing.


// Supplement/JsonPerformance.cs
// 1. Source-generated serialiser — no reflection,
// AOT-compatible
[JsonSerializable(typeof(Order))]
[JsonSerializable(typeof(Order[]))]
[JsonSerializable(typeof(List<Order>))]
[JsonSourceGenerationOptions(
```
PropertyNamingPolicy = JsonKnownNamingPolicy.CamelCase,

- 184 -
```


<a id='p185'></a>
<!-- Página 185 -->

```
C# 2026: Enterprise Mastery


WriteIndented = false)]
```

public partial class AppJsonContext : JsonSerializerContext
{ }

// Register in DI
builder.Services.ConfigureHttpJsonOptions(opts =>
```
opts.SerializerOptions.AddContext<AppJsonContext>());

```

// Serialise without reflection
```
var json = JsonSerializer.Serialize(order,
```

AppJsonContext.Default.Order);
```
var order = JsonSerializer.Deserialize(json,
```

AppJsonContext.Default.Order);

// 2. Low-allocation response writing with Utf8JsonWriter
app.MapGet("/orders/bulk", async (IOrderRepository repo,
HttpResponse response) =>
{
```
response.ContentType = "application/json";
await using var writer = new
```

Utf8JsonWriter(response.Body,
```
new JsonWriterOptions { Encoder =
```

JavaScriptEncoder.UnsafeRelaxedJsonEscaping });

```
writer.WriteStartArray();
await foreach (var order in repo.StreamAsync())
{
writer.WriteStartObject();
writer.WriteNumber("id"u8, order.Id);
writer.WriteString("status"u8,
```

order.Status.ToString());
```
writer.WriteNumber("amount"u8, order.Amount);
writer.WriteEndObject();
}
writer.WriteEndArray();
await writer.FlushAsync();
```

});
// Note: "status"u8 creates a UTF-8 literal — avoids
// encoding on every call




```
- 185 -
```


<a id='p186'></a>
<!-- Página 186 -->

```
C# 2026: Enterprise Mastery



```

Deep Dive: Pipelines and Dataflow
System.IO.Pipelines is the high-performance I/O API for processing
network data without copying. TPL Dataflow provides block-based
pipelines for CPU-bound parallel processing. Both complement async
streams for different workloads.


// Supplement/PipelineProcessing.cs
// System.IO.Pipelines: process a stream of
// newline-delimited JSON without buffering
public async Task ProcessJsonStreamAsync(Stream input,
CancellationToken ct)
{
```
var reader = PipeReader.Create(input);

while (true)
{
var result = await reader.ReadAsync(ct);
var buffer = result.Buffer;

while (TryReadLine(ref buffer, out var line))
{
var order =
```

JsonSerializer.Deserialize<Order>(line.ToArray());
```
await ProcessOrderAsync(order!);
}

reader.AdvanceTo(buffer.Start, buffer.End);

if (result.IsCompleted) break;
}

await reader.CompleteAsync();
```

}

private static bool TryReadLine(ref ReadOnlySequence<byte>
buffer,
```
out ReadOnlySequence<byte> line)
```

{
```
var reader = new SequenceReader<byte>(buffer);
if (reader.TryReadTo(out line, (byte)'
```

', advancePastDelimiter: true))

```
- 186 -
```


<a id='p187'></a>
<!-- Página 187 -->

```
C# 2026: Enterprise Mastery


{
buffer = buffer.Slice(reader.Position);
return true;
}
line = default;
return false;
```

}

// TPL Dataflow: parallel CPU-bound processing pipeline
public async Task
ProcessWithDataflowAsync(IAsyncEnumerable<Order> orders)
{
```
var validateBlock = new TransformBlock<Order, Order>(
async order => { await ValidateAsync(order); return
```

order; },
```
new ExecutionDataflowBlockOptions
```

{ MaxDegreeOfParallelism = 4 });

```
var enrichBlock = new TransformBlock<Order,
```

EnrichedOrder>(
```
async order => await EnrichAsync(order),
new ExecutionDataflowBlockOptions
```

{ MaxDegreeOfParallelism = 8 });

```
var saveBlock = new ActionBlock<EnrichedOrder>(
async order => await SaveAsync(order),
new ExecutionDataflowBlockOptions
```

{ MaxDegreeOfParallelism = 2 });

```
validateBlock.LinkTo(enrichBlock, new
```

DataflowLinkOptions { PropagateCompletion = true });
```
enrichBlock.LinkTo(saveBlock, new DataflowLinkOptions {
```

PropagateCompletion = true });

```
await foreach (var order in orders)
await validateBlock.SendAsync(order);

validateBlock.Complete();
await saveBlock.Completion;
```

}




```
- 187 -
```


<a id='p188'></a>
<!-- Página 188 -->

```
C# 2026: Enterprise Mastery



```

IAsyncEnumerable: Streaming from Database to
Client
IAsyncEnumerable<T> allows data to flow from a database cursor
through your application layers to the HTTP response without ever
materialising the entire dataset in memory. For large reports, this is the
difference between a 2 GB RAM spike and a flat memory profile.


// Supplement/AsyncStreaming.cs
// Repository: stream directly from EF Core's async cursor
public class OrderRepository
{
```
public IAsyncEnumerable<Order> StreamLargeExportAsync(
DateRange range, CancellationToken ct)
{
return _db.Orders
.Where(o => o.CreatedAt >= range.Start &&
```

o.CreatedAt <= range.End)
```
.OrderBy(o => o.CreatedAt)
.AsAsyncEnumerable()
.WithCancellation(ct);
}
```

}

// Service: transform while streaming — no ToList()
public class ExportService
{
```
public async IAsyncEnumerable<CsvRow> StreamCsvAsync(
DateRange range,
[EnumeratorCancellation] CancellationToken ct =
```

default)
```
{
await foreach (var order in
```

_repo.StreamLargeExportAsync(range, ct))
```
{
yield return new CsvRow(
order.Id, order.CreatedAt, order.Amount,
```

order.Status);
```
}
}
```

}


```
- 188 -
```


<a id='p189'></a>
<!-- Página 189 -->

```
C# 2026: Enterprise Mastery




```

// API: stream directly to HTTP response
app.MapGet("/export/csv", async (
```
DateRange range, ExportService svc,
HttpResponse response, CancellationToken ct) =>
```

{
```
response.ContentType = "text/csv";
response.Headers.Append("Content-Disposition",
```

"attachment; filename=orders.csv");

```
await response.WriteAsync("Id,Date,Amount,Status
```

", ct);
```
await foreach (var row in svc.StreamCsvAsync(range,
```

ct))
```
{
await response.WriteAsync(
$"{row.Id},{row.Date:yyyy-MM-dd},{row.Amount},
```

{row.Status}
", ct);
```
}
```

});
// Memory use is constant regardless of how many rows the
// query returns




Semaphore Patterns for Rate-Limiting

// Supplement/SemaphorePatterns.cs
// SemaphoreSlim: limit concurrent external API calls
public class ThirdPartyApiClient
{
```
// max 20 concurrent
private readonly SemaphoreSlim _throttle = new(20, 20);
private readonly HttpClient _http;

public async Task<T> GetAsync<T>(string path,
```

CancellationToken ct = default)
```
{
await _throttle.WaitAsync(ct);
try
{

- 189 -
```


<a id='p190'></a>
<!-- Página 190 -->

```
C# 2026: Enterprise Mastery


var response = await _http.GetAsync(path, ct);
response.EnsureSuccessStatusCode();
return await
```

response.Content.ReadFromJsonAsync<T>(ct) ?? default!;
```
}
finally
{
_throttle.Release();
}
}

// Batch with bounded concurrency
public async Task<TResult[]> BatchAsync<TItem,
```

TResult>(
```
IEnumerable<TItem> items,
Func<TItem, Task<TResult>> process,
int concurrency = 10)
{
var semaphore = new SemaphoreSlim(concurrency,
```

concurrency);
```
var tasks = items.Select(async item =>
{
await semaphore.WaitAsync();
try { return await process(item); }
finally { semaphore.Release(); }
});
return await Task.WhenAll(tasks);
}
```

}




```
- 190 -
```


<a id='p191'></a>
<!-- Página 191 -->

```
C# 2026: Enterprise Mastery



```

Deep Dive: CQRS with Mediatr and Clean
Architecture
CQRS (Command Query Responsibility Segregation) separates reads from
writes. In .NET the pattern is most cleanly implemented with MediatR's
request/handler pattern inside a Clean Architecture structure. The result
is application logic that is trivially testable and infinitely composable
through pipeline behaviours.


// Supplement/CqrsCleanArch.cs
// -- Commands
//
-----------------------------------------------------------
---
public record PlaceOrderCommand(
```
Guid CustomerId,
List<OrderLineDto> Lines) : IRequest<Result<Guid>>;

```

public class PlaceOrderHandler :
IRequestHandler<PlaceOrderCommand, Result<Guid>>
{
```
private readonly IOrderRepository _orders;
private readonly IInventoryService _inventory;
private readonly IEventBus _events;
private readonly IUnitOfWork _uow;

public PlaceOrderHandler(IOrderRepository orders,
```

IInventoryService inventory,
```
IEventBus events, IUnitOfWork uow)
{
_orders = orders;
_inventory = inventory;
_events = events;
_uow = uow;
}

public async Task<Result<Guid>>
```

Handle(PlaceOrderCommand cmd, CancellationToken ct)
```
{
// Domain logic — no HTTP, no EF, just pure
// business rules

- 191 -
```


<a id='p192'></a>
<!-- Página 192 -->

```
C# 2026: Enterprise Mastery


var order = Order.Create(cmd.CustomerId,
```

cmd.Lines.Select(LineItem.From));
```
if (order.IsFailure) return
```

Result.Failure<Guid>(order.Error);

```
var reserved = await
```

_inventory.ReserveAsync(order.Value.Lines, ct);
```
if (!reserved) return
```

Result.Failure<Guid>("Insufficient inventory");

```
await _orders.AddAsync(order.Value, ct);
await _events.PublishAsync(new
```

OrderPlaced(order.Value.Id), ct);
```
await _uow.CommitAsync(ct);

return Result.Success(order.Value.Id);
}
```

}

// -- Queries
//
-----------------------------------------------------------
----
public record GetOrderQuery(Guid OrderId) :
IRequest<Result<OrderDto>>;

public class GetOrderHandler :
IRequestHandler<GetOrderQuery, Result<OrderDto>>
{
```
// Separate read model — optimised
private readonly IReadDbContext _read;

public GetOrderHandler(IReadDbContext read) => _read =
```

read;

```
public async Task<Result<OrderDto>>
```

Handle(GetOrderQuery q, CancellationToken ct)
```
{
var dto = await _read.Orders
.Where(o => o.Id == q.OrderId)
.Select(o => new OrderDto(o.Id, o.Status,
```

o.TotalAmount, o.CreatedAt))
```
.FirstOrDefaultAsync(ct);


- 192 -
```


<a id='p193'></a>
<!-- Página 193 -->

```
C# 2026: Enterprise Mastery


return dto is not null
? Result.Success(dto)
: Result.Failure<OrderDto>("Order not found");
}
```

}

// -- Pipeline Behaviours
// ---------------------------------------------------
public class ValidationBehaviour<TRequest, TResponse>
```
: IPipelineBehavior<TRequest, TResponse>
where TRequest : IRequest<TResponse>
```

{
```
private readonly IEnumerable<IValidator<TRequest>>
```

_validators;

```
public
```

ValidationBehaviour(IEnumerable<IValidator<TRequest>>
validators)
```
=> _validators = validators;

public async Task<TResponse> Handle(TRequest request,
RequestHandlerDelegate<TResponse> next,
```

CancellationToken ct)
```
{
if (!_validators.Any()) return await next();

var context = new
```

ValidationContext<TRequest>(request);
```
var failures = _validators
.Select(v => v.Validate(context))
.SelectMany(r => r.Errors)
.Where(f => f is not null)
.ToList();

if (failures.Count > 0) throw new
```

ValidationException(failures);
```
return await next();
}
```

}




```
- 193 -
```


<a id='p194'></a>
<!-- Página 194 -->

```
C# 2026: Enterprise Mastery



```

Outbox Pattern Implementation Details
The outbox pattern guarantees that domain events are published exactly
once, even if the application crashes mid-transaction. The message is
saved in the same database transaction as the business data, then a
background worker reads and publishes pending messages.


// Supplement/OutboxDetail.cs
// Outbox table entity
public class OutboxMessage
{
```
public Guid Id { get; init; } = Guid.NewGuid();
public string EventType { get; init; } = string.Empty;
public string Payload { get; init; } = string.Empty;
public DateTimeOffset CreatedAt { get; init; } =
```

DateTimeOffset.UtcNow;
```
public DateTimeOffset? ProcessedAt { get; set; }
public int RetryCount { get; set; }
public string? Error { get; set; }
```

}

// Write to outbox in the same transaction as domain data
public class PlaceOrderHandler :
IRequestHandler<PlaceOrderCommand, Guid>
{
```
public async Task<Guid> Handle(PlaceOrderCommand cmd,
```

CancellationToken ct)
```
{
var order = Order.Create(cmd);
_db.Orders.Add(order);

// Same transaction — both succeed or both fail
_db.OutboxMessages.Add(new OutboxMessage
{
EventType = nameof(OrderPlaced),
Payload = JsonSerializer.Serialize(new
```

OrderPlaced(order.Id, order.CustomerId))
```
});

await _db.SaveChangesAsync(ct); // One transaction
return order.Id;
}

- 194 -
```


<a id='p195'></a>
<!-- Página 195 -->

```
C# 2026: Enterprise Mastery


```

}

// Background processor — reads and publishes pending
// messages
public class OutboxProcessor : BackgroundService
{
```
protected override async Task
```

ExecuteAsync(CancellationToken ct)
```
{
while (!ct.IsCancellationRequested)
{
await ProcessBatchAsync(ct);
await Task.Delay(TimeSpan.FromSeconds(5), ct);
}
}

private async Task ProcessBatchAsync(CancellationToken
```

ct)
```
{
// SELECT ... FOR UPDATE SKIP LOCKED — handles
// multiple instances safely
var messages = await _db.OutboxMessages
.Where(m => m.ProcessedAt == null &&
```

m.RetryCount < 5)
```
.OrderBy(m => m.CreatedAt)
.Take(50)
.ToListAsync(ct);

foreach (var msg in messages)
{
try
{
var eventType =
```

Type.GetType(msg.EventType)!;
```
var @event =
```

JsonSerializer.Deserialize(msg.Payload, eventType)!;
```
await _bus.PublishAsync(@event, ct);
msg.ProcessedAt = DateTimeOffset.UtcNow;
}
catch (Exception ex)
{
msg.RetryCount++;
msg.Error = ex.Message;


- 195 -
```


<a id='p196'></a>
<!-- Página 196 -->

```
C# 2026: Enterprise Mastery


_logger.LogWarning(ex, "Outbox message {Id}
```

failed", msg.Id);
```
}
}

await _db.SaveChangesAsync(ct);
}
```

}




```
- 196 -
```


<a id='p197'></a>
<!-- Página 197 -->

```
C# 2026: Enterprise Mastery



```

Deep Dive: Property-Based Testing with FsCheck
Unit tests verify specific examples. Property-based tests verify invariants
that must hold for all valid inputs. FsCheck generates hundreds of random
inputs and finds edge cases that you would never think to write manually.


// Supplement/PropertyBasedTests.cs
using FsCheck;
using FsCheck.Xunit;

public class OrderCalculatorProperties
{
```
// Property: total is always the sum of line totals
[Property]
public Property TotalEqualsSumOfLines(List<(decimal
```

Price, int Qty)> lines)
```
{
var orderLines = lines
.Where(l => l.Price > 0 && l.Qty > 0)
.Select(l => new OrderLine(l.Price, l.Qty))
.ToList();

var order = new Order(orderLines);

var expected = orderLines.Sum(l => l.Price *
```

l.Qty);
```
return (order.Total == expected)
.Label($"Expected {expected}, got
```

{order.Total}");
```
}

// Property: applying a discount never increases the
// total
[Property]
public Property DiscountNeverIncreasesTotal(
PositiveInt amount,
NonNegativeInt discountPercent)
{
var pct = discountPercent.Get % 101; // 0..100
var order = new Order { Amount = amount.Get };
var discounted = order.ApplyDiscount(pct);



- 197 -
```


<a id='p198'></a>
<!-- Página 198 -->

```
C# 2026: Enterprise Mastery


return (discounted.Amount <= order.Amount)
.Label($"Discount {pct}%: {order.Amount} ->
```

{discounted.Amount}");
```
}

// Property: serialise/deserialise round-trip preserves
// equality
[Property]
public Property SerialiseRoundTrip(Order order)
{
var json = JsonSerializer.Serialize(order);
var restored =
```

JsonSerializer.Deserialize<Order>(json);
```
return (order == restored)
.Label($"Round trip failed for {json}");
}
```

}




Architecture Tests with NetArchTest
Architecture tests enforce structural rules that cannot be expressed in C#
access modifiers. They run in CI and fail immediately when a developer
accidentally introduces a dependency that violates the layering rules.


// Supplement/ArchitectureTests.cs
using NetArchTest.Rules;

public class ArchitectureTests
{
```
private const string DomainNs = "MyApp.Domain";
private const string AppNs = "MyApp.Application";
private const string InfrastructureNs =
```

"MyApp.Infrastructure";

```
[Fact]
public void Domain_Should_Not_Depend_On_Application()
{
var result =
```

Types.InAssembly(typeof(Domain.Order).Assembly)
```
.Should().NotHaveDependencyOn(AppNs)

- 198 -
```


<a id='p199'></a>
<!-- Página 199 -->

```
C# 2026: Enterprise Mastery


.GetResult();

Assert.True(result.IsSuccessful,
string.Join('
```

', result.FailingTypeNames ?? []));
```
}

[Fact]
public void
```

Application_Should_Not_Depend_On_Infrastructure()
```
{
var result =
```

Types.InAssembly(typeof(Application.PlaceOrderCommand).Asse
mbly)
```
.Should().NotHaveDependencyOn(InfrastructureNs)
.GetResult();

Assert.True(result.IsSuccessful,
string.Join('
```

', result.FailingTypeNames ?? []));
```
}

[Fact]
public void Handlers_Should_Be_Sealed()
{
// MediatR handlers should not be inherited
var result =
```

Types.InAssembly(typeof(Application.PlaceOrderCommand).Asse
mbly)
```
.That().ImplementInterface(typeof(IRequestHandl
```

er<,>))
```
.Should().BeSealed()
.GetResult();

Assert.True(result.IsSuccessful,
string.Join('
```

', result.FailingTypeNames ?? []));
```
}

[Fact]
public void
```

Controllers_Should_Not_Contain_Business_Logic()
```
{
// Controllers should not depend on repositories

- 199 -
```


<a id='p200'></a>
<!-- Página 200 -->

```
C# 2026: Enterprise Mastery


// directly
var result =
```

Types.InAssembly(typeof(WebApi.OrdersController).Assembly)
```
.That().Inherit(typeof(ControllerBase))
.Should().NotHaveDependencyOn(InfrastructureNs)
.GetResult();

Assert.True(result.IsSuccessful,
string.Join('
```

', result.FailingTypeNames ?? []));
```
}
```

}




Chaos Engineering with Polly and Simmy
Simmy is the chaos extension for Polly. It injects faults — delays,
exceptions, bad results — into your production resilience pipelines to
verify that your application degrades gracefully when dependencies
misbehave.


// Supplement/ChaosEngineering.cs
using Polly.Simmy;

// Register chaos policies in DI (enable only in
// non-production environments)
builder.Services.AddResiliencePipeline("payment-service",
(pipeline, context) =>
{
```
pipeline
.AddRetry(new RetryStrategyOptions
```

{ MaxRetryAttempts = 3 })
```
.AddCircuitBreaker(new
```

CircuitBreakerStrategyOptions
```
{
FailureRatio = 0.5,
SamplingDuration = TimeSpan.FromSeconds(30)
});

// Chaos — enable via config


- 200 -
```


<a id='p201'></a>
<!-- Página 201 -->

```
C# 2026: Enterprise Mastery


if
```

(context.ServiceProvider.GetRequiredService<IConfiguration>
()
```
.GetValue<bool>("Chaos:Enabled"))
{
pipeline
// Inject latency: 30% of calls delayed by 2-5
// seconds
.AddChaosLatency(new
```

ChaosLatencyStrategyOptions
```
{
EnabledGenerator = _ =>
```

ValueTask.FromResult(true),
```
InjectionRateGenerator = _ =>
```

ValueTask.FromResult(0.3),
```
LatencyGenerator = _ =>
```

ValueTask.FromResult(

TimeSpan.FromSeconds(Random.Shared.Next(2, 5)))
```
})
// Inject faults: 10% of calls throw
.AddChaosFault(new ChaosFaultStrategyOptions
{
InjectionRateGenerator = _ =>
```

ValueTask.FromResult(0.1),
```
FaultGenerator = _ =>
```

ValueTask.FromResult<Exception?>(
```
new HttpRequestException("Chaos fault
```

injected"))
```
});
}
```

});

// Use in tests to verify resilience
public class PaymentServiceChaosTests
{
```
[Fact]
public async Task CircuitBreaker_Opens_After_Failures()
{
var pipeline = new ResiliencePipelineBuilder()
.AddCircuitBreaker(new
```

CircuitBreakerStrategyOptions
```
{
FailureRatio = 0.5,

- 201 -
```


<a id='p202'></a>
<!-- Página 202 -->

```
C# 2026: Enterprise Mastery


MinimumThroughput = 5
})
.AddChaosFault(1.0, () => new Exception("Always
```

fails"))
```
.Build();

// After enough failures, circuit should open
for (int i = 0; i < 5; i++)
{
try { await pipeline.ExecuteAsync(_ =>
```

CallPaymentApiAsync()); }
```
catch { /* expected */ }
}

await Assert.ThrowsAsync<BrokenCircuitException>(
() => pipeline.ExecuteAsync(_ =>
```

CallPaymentApiAsync()));
```
}
```

}




```
- 202 -
```


<a id='p203'></a>
<!-- Página 203 -->

```
C# 2026: Enterprise Mastery



```

Deep Dive: Zero-Trust API Security
Zero-trust architecture assumes that any request — internal or external
— must be authenticated, authorised, and validated. For APIs this means
combining JWT validation, resource-based authorisation, input validation,
and rate limiting into a coherent security pipeline.


// Supplement/ZeroTrustApi.cs
// 1. JWT validation with audience and scope checking
builder.Services.AddAuthentication(JwtBearerDefaults.Authen
ticationScheme)
```
.AddJwtBearer(options =>
{
options.Authority =
```

builder.Configuration["Auth:Authority"];
```
options.Audience =
```

builder.Configuration["Auth:Audience"];
```
options.TokenValidationParameters = new
```

TokenValidationParameters
```
{
ValidateIssuerSigningKey = true,
ValidateAudience = true,
ValidateIssuer = true,
ValidateLifetime = true,
// Tighten from the 5-min default
ClockSkew = TimeSpan.FromSeconds(30)
};
});

```

// 2. Resource-based authorisation
public class OrderAuthorizationHandler
```
: AuthorizationHandler<SameOwnerRequirement, Order>
```

{
```
protected override Task HandleRequirementAsync(
AuthorizationHandlerContext ctx,
SameOwnerRequirement requirement,
Order order)
{
var userId =
```

ctx.User.FindFirstValue(ClaimTypes.NameIdentifier);
```
if (order.CustomerId.ToString() == userId)
ctx.Succeed(requirement);

- 203 -
```


<a id='p204'></a>
<!-- Página 204 -->

```
C# 2026: Enterprise Mastery


return Task.CompletedTask;
}
```

}

// 3. Input validation with FluentValidation
public class UpdateOrderValidator :
AbstractValidator<UpdateOrderRequest>
{
```
public UpdateOrderValidator()
{
RuleFor(x => x.Amount)
.GreaterThan(0).WithMessage("Amount must be
```

positive")
```
.LessThanOrEqualTo(1_000_000).WithMessage("Amou
```

nt exceeds limit");

```
RuleFor(x => x.Notes)
.MaximumLength(500)
.Matches(@"^[\w\
```

s\.,\-!?]*$").WithMessage("Notes contain invalid
characters");

```
RuleFor(x => x.DeliveryAddress)
.NotEmpty()
.SetValidator(new AddressValidator());
}
```

}

// 4. Endpoint combining auth, validation, and rate
// limiting
app.MapPut("/orders/{id}", async (
```
Guid id,
UpdateOrderRequest request,
IValidator<UpdateOrderRequest> validator,
IAuthorizationService auth,
IOrderService orders,
ClaimsPrincipal user,
CancellationToken ct) =>
```

{
```
var validation = await validator.ValidateAsync(request,
```

ct);
```
if (!validation.IsValid) return
```

Results.ValidationProblem(validation.ToDictionary());


```
- 204 -
```


<a id='p205'></a>
<!-- Página 205 -->

```
C# 2026: Enterprise Mastery


var order = await orders.GetAsync(id, ct);
if (order is null) return Results.NotFound();

var authResult = await auth.AuthorizeAsync(user, order,
```

"SameOwner");
```
if (!authResult.Succeeded) return Results.Forbid();

await orders.UpdateAsync(id, request, ct);
return Results.NoContent();
```

})
.RequireAuthorization()
.RequireRateLimiting("api");




Secrets Management — Never Put Secrets in Code

// Supplement/SecretsManagement.cs
// 1. Local development: use dotnet user-secrets
// dotnet user-secrets set "Database:Password"
// "devpassword"

// 2. Production: Azure Key Vault with Managed Identity
builder.Configuration.AddAzureKeyVault(
```
new
```

Uri($"https://{builder.Configuration["KeyVault:Name"]}.vaul
t.azure.net/"),
```
// Uses Managed Identity in Azure, dev credentials
// locally
new DefaultAzureCredential());

```

// 3. Kubernetes: mount secrets as environment variables,
// never ConfigMaps
// kubectl create secret generic db-creds
// --from-literal=password=secret
// In deployment.yaml:
// env:
// - name: DATABASE__PASSWORD
// valueFrom:
// secretKeyRef:
// name: db-creds
// key: password

```
- 205 -
```


<a id='p206'></a>
<!-- Página 206 -->

```
C# 2026: Enterprise Mastery




```

// 4. Connection string builder — construct from separate
// secret pieces
public class DatabaseConnectionFactory
{
```
private readonly IConfiguration _config;

public string BuildConnectionString() =>
new NpgsqlConnectionStringBuilder
{
Host = _config["Database:Host"],
Database = _config["Database:Name"],
Username = _config["Database:Username"],
// From Key Vault or secret
Password = _config["Database:Password"],
SslMode = SslMode.Require,
TrustServerCertificate = false
}.ConnectionString;
```

}




```
- 206 -
```


<a id='p207'></a>
<!-- Página 207 -->

```
C# 2026: Enterprise Mastery



```

Deep Dive: Custom Metrics with
System.Diagnostics.Metrics
The System.Diagnostics.Metrics API (the successor to EventCounters) is
the idiomatic way to emit custom metrics in .NET. Metrics are
automatically picked up by OpenTelemetry and exported to Prometheus,
Azure Monitor, or any other compatible backend.


// Supplement/CustomMetrics.cs
// Define meters in a static class — meters are expensive
// to create
public static class AppMetrics
{
```
private static readonly Meter _meter = new("MyApp",
```

"1.0");

```
// Counters: count things that only go up
public static readonly Counter<long> OrdersPlaced =
_meter.CreateCounter<long>("orders.placed",
```

"orders",
```
"Total number of orders placed");

public static readonly Counter<long> OrdersFailed =
_meter.CreateCounter<long>("orders.failed",
```

"orders",
```
"Total number of failed order placements");

// Histograms: measure distributions (latency, payload
// size)
public static readonly Histogram<double>
```

OrderProcessingDuration =

_meter.CreateHistogram<double>("orders.processing.duration"
, "ms",
```
"Time to process an order from placement to
```

confirmation");

```
public static readonly Histogram<long> OrderAmount =
_meter.CreateHistogram<long>("orders.amount",
```

"cents",
```
"Distribution of order amounts");


- 207 -
```


<a id='p208'></a>
<!-- Página 208 -->

```
C# 2026: Enterprise Mastery




// Gauges: snapshot values (queue depth, connection
// pool, active users)
public static readonly ObservableGauge<int>
```

PendingOrders =
```
_meter.CreateObservableGauge("orders.pending", ()
```

=>
```
OrderQueue.CurrentDepth,
"orders", "Number of orders pending
```

processing");
}

// Use metrics in business logic
public class OrderService
{
```
public async Task<Guid>
```

PlaceOrderAsync(PlaceOrderCommand cmd, CancellationToken
ct)
```
{
var sw = Stopwatch.StartNew();
try
{
var orderId = await ProcessInternalAsync(cmd,
```

ct);

```
AppMetrics.OrdersPlaced.Add(1,
new TagList
{
{ "customer.tier", cmd.CustomerTier },
{ "channel", cmd.Channel }
});

AppMetrics.OrderAmount.Record((long)
```

(cmd.TotalAmount * 100));
```
return orderId;
}
catch (Exception)
{
AppMetrics.OrdersFailed.Add(1,
new TagList { { "reason", "exception" } });
throw;
}
finally
{

- 208 -
```


<a id='p209'></a>
<!-- Página 209 -->

```
C# 2026: Enterprise Mastery




```

AppMetrics.OrderProcessingDuration.Record(sw.Elapsed.TotalM
illiseconds);
```
}
}
```

}




Distributed Tracing: Linking Spans Across
Services

// Supplement/DistributedTracing.cs
// Create an ActivitySource — one per library/service
public static class Telemetry
{
```
public static readonly ActivitySource Source =
new("MyApp.OrderService", "1.0.0");
```

}

// Add a custom span with semantic conventions
public class OrderFulfillmentService
{
```
public async Task FulfillAsync(Guid orderId,
```

CancellationToken ct)
```
{
using var activity =
```

Telemetry.Source.StartActivity(
```
"order.fulfill", ActivityKind.Internal);

activity?.SetTag("order.id", orderId);
activity?.SetTag("service.name", "fulfillment");

try
{
// Child spans are created automatically for
// outbound HTTP/DB calls
// because ASP.NET Core and EF Core instruments
// are registered
var order = await _db.Orders.FindAsync(orderId,
```

ct);


```
- 209 -
```


<a id='p210'></a>
<!-- Página 210 -->

```
C# 2026: Enterprise Mastery


activity?.SetTag("order.customer_id",
```

order?.CustomerId);
```
activity?.SetTag("order.amount",
```

order?.Amount);

```
await _warehouse.ReserveAsync(orderId, ct);

activity?.SetStatus(ActivityStatusCode.Ok);
}
catch (Exception ex)
{
activity?.SetStatus(ActivityStatusCode.Error,
```

ex.Message);
```
activity?.RecordException(ex);
throw;
}
}
```

}

// Register ActivitySource with OpenTelemetry so spans are
// exported
builder.Services.AddOpenTelemetry()
```
.WithTracing(t => t
// All ActivitySources matching this prefix
.AddSource("MyApp.*")
.AddAspNetCoreInstrumentation()
.AddEntityFrameworkCoreInstrumentation()
.AddHttpClientInstrumentation()
.AddOtlpExporter(o => o.Endpoint = new
```

Uri("http://otel-collector:4317")));




```
- 210 -
```


<a id='p211'></a>
<!-- Página 211 -->

```
C# 2026: Enterprise Mastery



```

Deep Dive: Value Objects and Domain Primitives
Primitive obsession — using string for email addresses, int for money,
Guid for IDs — is one of the most common sources of bugs in enterprise
systems. Value objects encapsulate validation and domain semantics in a
type that is impossible to misuse.


// Supplement/ValueObjects.cs
// Domain primitive: Email — impossible to pass an invalid
// email
public readonly record struct Email
{
```
private static readonly Regex _pattern =
new(@"^[^@\s]+@[^@\s]+\.[^@\s]+$",
```

RegexOptions.Compiled);

```
public string Value { get; }

private Email(string value) => Value = value;

public static Result<Email> Create(string? raw)
{
if (string.IsNullOrWhiteSpace(raw))
return Result.Failure<Email>("Email cannot be
```

empty");
```
var normalised = raw.Trim().ToLowerInvariant();
if (!_pattern.IsMatch(normalised))
return Result.Failure<Email>($"'{raw}' is not a
```

valid email");
```
return Result.Success(new Email(normalised));
}

public static implicit operator string(Email e) =>
```

e.Value;
```
public override string ToString() => Value;
```

}

// Typed ID: prevents passing the wrong ID to the wrong
// method
public readonly record struct OrderId(Guid Value)
{
```
public static OrderId New() => new(Guid.NewGuid());

- 211 -
```


<a id='p212'></a>
<!-- Página 212 -->

```
C# 2026: Enterprise Mastery


public static OrderId Parse(string s) =>
```

new(Guid.Parse(s));
```
public override string ToString() => Value.ToString();
```

}

// Money: encapsulates currency and arithmetic rules
public readonly record struct Money(decimal Amount, string
Currency)
{
```
public static Money Zero(string currency) => new(0,
```

currency);

```
public Money Add(Money other)
{
if (Currency != other.Currency)
throw new InvalidOperationException(
$"Cannot add {Currency} and
```

{other.Currency}");
```
return this with { Amount = Amount +
```

other.Amount };
```
}

public Money Multiply(decimal factor) => this with
```

{ Amount = Amount * factor };
```
public Money ApplyDiscount(decimal pct) => Multiply(1 -
```

pct / 100);
}

// Now your Order is self-documenting and safe:
public class Order
{
```
public OrderId Id { get; } = OrderId.New();
// Cannot be invalid
public Email CustomerEmail { get; }
// Cannot mix currencies
public Money Total { get; private set; }
```

}




```
- 212 -
```


<a id='p213'></a>
<!-- Página 213 -->

```
C# 2026: Enterprise Mastery



```

The Result Pattern — Explicit Error Handling
Exceptions are for exceptional conditions — unexpected failures, bugs,
infrastructure failures. Business validation failures are not exceptional;
they are expected. The Result pattern models success and failure as
first-class values.


// Supplement/ResultPattern.cs
public class Result<T>
{
```
public T? Value { get; }
public string? Error { get; }
public bool IsSuccess { get; }
public bool IsFailure => !IsSuccess;

private Result(T value) { Value = value; IsSuccess =
```

true; }
```
private Result(string error) { Error = error; IsSuccess
```

= false; }

```
public static Result<T> Success(T value) => new(value);
public static Result<T> Failure(string error) =>
```

new(error);

```
// Functional chaining
public Result<TNext> Map<TNext>(Func<T, TNext> fn) =>
IsSuccess ? Result<TNext>.Success(fn(Value!)) :
```

Result<TNext>.Failure(Error!);

```
public async Task<Result<TNext>>
```

MapAsync<TNext>(Func<T, Task<TNext>> fn) =>
```
IsSuccess ? Result<TNext>.Success(await fn(Value!))
```

: Result<TNext>.Failure(Error!);

```
public Result<T> OnFailure(Action<string> action)
{
if (IsFailure) action(Error!);
return this;
}
```

}

// Usage: readable, no exceptions for flow control

```
- 213 -
```


<a id='p214'></a>
<!-- Página 214 -->

```
C# 2026: Enterprise Mastery


```

public async Task<IActionResult>
PlaceOrder(PlaceOrderRequest request)
{
```
var emailResult = Email.Create(request.CustomerEmail);
if (emailResult.IsFailure) return
```

BadRequest(emailResult.Error);

```
var commandResult = await _mediator.Send(new
```

PlaceOrderCommand(emailResult.Value!));

```
return commandResult.IsSuccess
? CreatedAtAction(nameof(GetOrder), new { id =
```

commandResult.Value }, null)
```
: commandResult.Error!.Contains("inventory")
? Conflict(commandResult.Error)
: BadRequest(commandResult.Error);
```

}




```
- 214 -
```


<a id='p215'></a>
<!-- Página 215 -->

```
C# 2026: Enterprise Mastery



```

Deep Dive: Organising Minimal APIs at
Enterprise Scale
A single Program.cs with hundreds of MapGet/MapPost calls becomes
unmanageable. The solution is to group endpoints into modules — classes
that encapsulate all endpoints for a feature area.


// Supplement/EndpointModules.cs
// IEndpointModule: convention for all endpoint groups
public interface IEndpointModule
{
```
void MapEndpoints(IEndpointRouteBuilder app);
```

}

// OrdersModule: all order endpoints in one cohesive class
public class OrdersModule : IEndpointModule
{
```
public void MapEndpoints(IEndpointRouteBuilder app)
{
var orders = app.MapGroup("/api/orders")
.RequireAuthorization()
.RequireRateLimiting("api")
.WithTags("Orders")
.WithOpenApi();

orders.MapGet("", GetOrders).WithName("GetOrders");
orders.MapGet("{id:guid}",
```

GetOrder).WithName("GetOrder");
```
orders.MapPost("",
```

PlaceOrder).WithName("PlaceOrder");
```
orders.MapPut("{id:guid}",
```

UpdateOrder).WithName("UpdateOrder");
```
orders.MapDelete("{id:guid}",
```

CancelOrder).WithName("CancelOrder");
```
}

private static async Task<IResult> GetOrders(
[AsParameters] OrderFilterParams filter,
ISender mediator,
CancellationToken ct)
{


- 215 -
```


<a id='p216'></a>
<!-- Página 216 -->

```
C# 2026: Enterprise Mastery


var result = await mediator.Send(new
```

GetOrdersQuery(filter), ct);
```
return Results.Ok(result);
}

private static async Task<IResult> PlaceOrder(
PlaceOrderRequest request,
IValidator<PlaceOrderRequest> validator,
ISender mediator,
CancellationToken ct)
{
var validation = await
```

validator.ValidateAsync(request, ct);
```
if (!validation.IsValid) return
```

Results.ValidationProblem(validation.ToDictionary());

```
var result = await
```

mediator.Send(request.ToCommand(), ct);
```
return result.IsSuccess
? Results.CreatedAtRoute("GetOrder", new { id =
```

result.Value })
```
: Results.BadRequest(result.Error);
}

// Other endpoint handlers...
```

}

// Program.cs: register all modules by assembly scanning
builder.Services.AddEndpointModules(typeof(Program).Assembl
y);
app.MapEndpointModules();

// Extension methods for clean registration
public static class EndpointExtensions
{
```
public static IServiceCollection AddEndpointModules(
this IServiceCollection services, Assembly
```

assembly)
```
{
var moduleTypes = assembly.GetTypes()
.Where(t =>
```

typeof(IEndpointModule).IsAssignableFrom(t) && !
t.IsAbstract);
```
foreach (var type in moduleTypes)

- 216 -
```


<a id='p217'></a>
<!-- Página 217 -->

```
C# 2026: Enterprise Mastery


services.AddSingleton(typeof(IEndpointModule),
```

type);
```
return services;
}

public static void MapEndpointModules(this
```

WebApplication app)
```
{
foreach (var module in
```

app.Services.GetServices<IEndpointModule>())
```
module.MapEndpoints(app);
}
```

}




OpenAPI and API Versioning

// Supplement/ApiVersioning.cs
// Register API versioning
builder.Services.AddApiVersioning(options =>
{
```
options.DefaultApiVersion = new ApiVersion(1);
options.AssumeDefaultVersionWhenUnspecified = true;
options.ApiVersionReader = ApiVersionReader.Combine(
new UrlSegmentApiVersionReader(),
new HeaderApiVersionReader("X-API-Version"),
new QueryStringApiVersionReader("api-version"));
```

});

builder.Services.AddVersionedApiExplorer(options =>
{
```
options.GroupNameFormat = "'v'VVV";
options.SubstituteApiVersionInUrl = true;
```

});

// Versioned endpoint group
```
var v1 = app.NewVersionedApi();
var v1Orders =
```

v1.MapGroup("/api/v{version:apiVersion}/orders").HasApiVers
ion(1);



```
- 217 -
```


<a id='p218'></a>
<!-- Página 218 -->

```
C# 2026: Enterprise Mastery


var v2Orders =
```

v1.MapGroup("/api/v{version:apiVersion}/orders").HasApiVers
ion(2);

v1Orders.MapGet("", GetOrdersV1).WithName("GetOrders-v1");
v2Orders.MapGet("", GetOrdersV2).WithName("GetOrders-v2");
// V2 might return enriched DTOs, different pagination,
// etc.

// Swagger UI for each version
builder.Services.AddSwaggerGen(c =>
{
```
c.SwaggerDoc("v1", new OpenApiInfo { Title = "Orders
```

API", Version = "v1" });
```
c.SwaggerDoc("v2", new OpenApiInfo { Title = "Orders
```

API", Version = "v2" });
```
c.AddSecurityDefinition("Bearer", new
```

OpenApiSecurityScheme
```
{
Type = SecuritySchemeType.Http, Scheme = "bearer"
});
```

});




```
- 218 -
```


<a id='p219'></a>
<!-- Página 219 -->

```
C# 2026: Enterprise Mastery



```

Deep Dive: Query Splitting and Performance
Tuning
EF Core generates SQL on your behalf, and that SQL can be
catastrophically inefficient if you don't understand how it maps to
queries. These patterns address the most common EF Core performance
pitfalls in enterprise systems.


// Supplement/EfCoreAdvanced.cs
// 1. Query splitting: prevents cartesian explosion on
// multi-collection includes
// Without splitting: Orders JOIN Lines JOIN Products JOIN
// Tags = huge cartesian product
```
var orders = await _db.Orders
// Executes separate queries, joins in memory
.AsSplitQuery()
.Include(o => o.Lines)
.ThenInclude(l => l.Product)
.Include(o => o.Tags)
.Where(o => o.CustomerId == customerId)
.ToListAsync();

```

// 2. No-tracking queries for read-only scenarios
// (noticeably faster - EF skips snapshotting)
```
var summaries = await _db.Orders
.AsNoTracking() // EF won't snapshot these entities
.Where(o => o.Status == OrderStatus.Pending)
.Select(o => new OrderSummary(o.Id, o.CreatedAt,
```

o.Total))
```
.ToListAsync();

```

// 3. Compiled queries: reuse the LINQ->SQL translation
// (significant savings at scale)
private static readonly Func<AppDbContext, Guid,
Task<Order?>> _getOrderById =
```
EF.CompileAsyncQuery((AppDbContext db, Guid id) =>
db.Orders.FirstOrDefault(o => o.Id == id));

```

// Usage — zero LINQ compilation overhead
```
var order = await _getOrderById(_db, orderId);



- 219 -
```


<a id='p220'></a>
<!-- Página 220 -->

```
C# 2026: Enterprise Mastery


```

// 4. Raw SQL for complex queries EF can't optimise
```
var leaderboard = await _db.Database
.SqlQueryRaw<CustomerLeaderboard>(@"
SELECT c.Id, c.Name,
COUNT(o.Id) AS OrderCount,
SUM(o.Amount) AS TotalSpend,
RANK() OVER (ORDER BY SUM(o.Amount) DESC) AS
```

Rank
```
FROM Customers c
JOIN Orders o ON o.CustomerId = c.Id
WHERE o.CreatedAt >= @start
GROUP BY c.Id, c.Name
ORDER BY Rank
LIMIT @take
"",
new NpgsqlParameter("start",
```

DateTimeOffset.UtcNow.AddMonths(-1)),
```
new NpgsqlParameter("take", 100))
.ToListAsync();

```

// 5. ExecuteUpdateAsync / ExecuteDeleteAsync: bulk ops
// without loading entities
// Before (.NET 6 and earlier): load 10k entities, modify,
// SaveChanges
// After (.NET 7+): single UPDATE statement
```
var updated = await _db.Orders
.Where(o => o.Status == OrderStatus.PendingPayment
&& o.CreatedAt < DateTime.UtcNow.AddDays(-
```

7))
```
.ExecuteUpdateAsync(s => s.SetProperty(o => o.Status,
```

OrderStatus.Expired));

_logger.LogInformation("Expired {Count} orders", updated);




Global Query Filters and Soft Delete

// Supplement/SoftDelete.cs
// Soft delete: mark as deleted, filter automatically
// everywhere
public interface ISoftDeletable

```
- 220 -
```


<a id='p221'></a>
<!-- Página 221 -->

```
C# 2026: Enterprise Mastery


```

{
```
bool IsDeleted { get; set; }
DateTimeOffset? DeletedAt { get; set; }
```

}

public class Order : ISoftDeletable
{
```
public Guid Id { get; set; }
// ... other properties
public bool IsDeleted { get; set; }
public DateTimeOffset? DeletedAt { get; set; }
```

}

// Configure global filter in DbContext
protected override void OnModelCreating(ModelBuilder model)
{
```
// Apply to all types that implement ISoftDeletable
foreach (var entityType in
```

model.Model.GetEntityTypes())
```
{
if (!
```

typeof(ISoftDeletable).IsAssignableFrom(entityType.ClrType)
) continue;
```
model.Entity(entityType.ClrType)
.HasQueryFilter(BuildSoftDeleteFilter(entityTy
```

pe.ClrType));
```
}
```

}

private static LambdaExpression BuildSoftDeleteFilter(Type
type)
{
```
// Generates: entity => !entity.IsDeleted
var param = Expression.Parameter(type, "e");
var prop = Expression.Property(param,
```

nameof(ISoftDeletable.IsDeleted));
```
var body = Expression.Not(prop);
return Expression.Lambda(body, param);
```

}

// Override SaveChangesAsync to intercept hard deletes
public override async Task<int>
SaveChangesAsync(CancellationToken ct = default)
{

```
- 221 -
```


<a id='p222'></a>
<!-- Página 222 -->

```
C# 2026: Enterprise Mastery


foreach (var entry in
```

ChangeTracker.Entries<ISoftDeletable>()
```
.Where(e => e.State == EntityState.Deleted))
{
entry.State = EntityState.Modified;
entry.Entity.IsDeleted = true;
entry.Entity.DeletedAt = DateTimeOffset.UtcNow;
}
return await base.SaveChangesAsync(ct);
```

}

// Bypass filter when needed (admin, audit, restore)
```
var deletedOrders = await _db.Orders.IgnoreQueryFilters()
.Where(o => o.IsDeleted && o.DeletedAt > oneWeekAgo)
.ToListAsync();




- 222 -
```


<a id='p223'></a>
<!-- Página 223 -->

```
C# 2026: Enterprise Mastery



```

Deep Dive: Cache Invalidation Strategies
Cache invalidation is one of the hardest problems in distributed systems.
There are three broad strategies: TTL-based expiry (simple, stale),
event-driven invalidation (fresh, complex), and cache-aside with
versioning (balanced). Enterprise systems usually combine all three.


// Supplement/CacheInvalidation.cs
// 1. Event-driven invalidation via MediatR notification
public record OrderUpdated(Guid OrderId) : INotification;

public class OrderCacheInvalidator :
INotificationHandler<OrderUpdated>
{
```
private readonly IDistributedCache _cache;

public OrderCacheInvalidator(IDistributedCache cache)
```

=> _cache = cache;

```
public async Task Handle(OrderUpdated notification,
```

CancellationToken ct)
```
{
// Remove all cache keys related to this order
var keys = new[]
{
$"order:{notification.OrderId}",
$"order-summary:{notification.OrderId}",
$"customer-orders:
```

{GetCustomerIdForOrder(notification.OrderId)}",
```
};
foreach (var key in keys)
await _cache.RemoveAsync(key, ct);
}
```

}

// 2. Versioned cache keys — never stale, never need
// explicit invalidation
public class VersionedCache
{
```
private readonly IDistributedCache _cache;
private readonly IEntityVersionStore _versions;


- 223 -
```


<a id='p224'></a>
<!-- Página 224 -->

```
C# 2026: Enterprise Mastery


public async Task<T?> GetAsync<T>(string entityType,
```

Guid id, CancellationToken ct)
```
{
var version = await
```

_versions.GetVersionAsync(entityType, id, ct);
```
var key = $"{entityType}:{id}:v{version}";
var json = await _cache.GetStringAsync(key, ct);
return json is null ? default :
```

JsonSerializer.Deserialize<T>(json);
```
}

public async Task SetAsync<T>(string entityType, Guid
```

id, T value, CancellationToken ct)
```
{
var version = await
```

_versions.IncrementAsync(entityType, id, ct);
```
var key = $"{entityType}:{id}:v{version}";
await _cache.SetStringAsync(key,
```

JsonSerializer.Serialize(value),
```
new DistributedCacheEntryOptions
{
SlidingExpiration =
```

TimeSpan.FromMinutes(10)
```
}, ct);
}
```

}

// 3. Write-through cache: update cache atomically with the
// database
public class OrderService
{
```
public async Task UpdateOrderAsync(Guid id,
```

UpdateOrderDto dto, CancellationToken ct)
```
{
var order = await _db.Orders.FindAsync(id, ct);
order!.UpdateFrom(dto);
await _db.SaveChangesAsync(ct);

// Update cache immediately — read-after-write
// consistency
var cacheKey = $"order:{id}";
await _cache.SetStringAsync(cacheKey,
JsonSerializer.Serialize(OrderDto.From(order)),


- 224 -
```


<a id='p225'></a>
<!-- Página 225 -->

```
C# 2026: Enterprise Mastery


new DistributedCacheEntryOptions
```

{ SlidingExpiration = TimeSpan.FromMinutes(5) },
```
ct);
}
```

}




Response Caching and Output Caching

// Supplement/OutputCaching.cs
// Output caching: cache the entire HTTP response at the
// framework level
builder.Services.AddOutputCache(options =>
{
```
options.AddBasePolicy(b =>
```

b.Expire(TimeSpan.FromSeconds(10)));

```
options.AddPolicy("products", b => b
.Expire(TimeSpan.FromMinutes(5))
.SetVaryByQuery("category", "page")
.Tag("products"));

options.AddPolicy("user-specific", b => b
.Expire(TimeSpan.FromSeconds(30))
.SetVaryByHeader("Authorization")
.SetVaryByClaim(ClaimTypes.NameIdentifier));
```

});

// Apply to endpoints
app.MapGet("/products", GetProducts)
```
.CacheOutput("products");

```

app.MapGet("/me/orders", GetMyOrders)
```
.CacheOutput("user-specific");

```

// Invalidate by tag after data changes
app.MapPost("/products", async (ProductDto dto,
IOutputCacheStore cache, CancellationToken ct) =>
{
```
await SaveProductAsync(dto);
// All product cache entries cleared

- 225 -
```


<a id='p226'></a>
<!-- Página 226 -->

```
C# 2026: Enterprise Mastery


await cache.EvictByTagAsync("products", ct);
return Results.Created();
```

});

// Vary by custom key — e.g. tenant in multi-tenant apps
public class TenantCachePolicy : IOutputCachePolicy
{
```
public ValueTask CacheRequestAsync(OutputCacheContext
```

ctx, CancellationToken ct)
```
{
var tenant =
```

ctx.HttpContext.User.FindFirstValue("tenant_id") ??
"default";
```
ctx.CacheVaryByValues.Add("tenant", tenant);
return ValueTask.CompletedTask;
}

public ValueTask ServeFromCacheAsync(OutputCacheContext
```

ctx, CancellationToken ct)
```
=> ValueTask.CompletedTask;

public ValueTask ServeResponseAsync(OutputCacheContext
```

ctx, CancellationToken ct)
```
=> ValueTask.CompletedTask;
```

}




```
- 226 -
```


<a id='p227'></a>
<!-- Página 227 -->

```
C# 2026: Enterprise Mastery



```

Deep Dive: gRPC Bidirectional Streaming
Bidirectional streaming lets the client and server send messages
independently. This is ideal for real-time collaboration features, telemetry
ingestion, and live data feeds.


// Supplement/GrpcBidirectional.cs
// Proto definition
syntax = "proto3";
service OrderTracker {
```
rpc TrackOrders (stream TrackRequest) returns (stream
```

OrderUpdate);
}

// Server implementation
public class OrderTrackerService :
OrderTracker.OrderTrackerBase
{
```
private readonly IOrderEventStream _events;

public override async Task TrackOrders(
IAsyncStreamReader<TrackRequest> requestStream,
IServerStreamWriter<OrderUpdate> responseStream,
ServerCallContext context)
{
var trackedIds = new ConcurrentHashSet<Guid>();

// Background: receive subscription changes from
// client
var receiveTask = Task.Run(async () =>
{
await foreach (var request in
```

requestStream.ReadAllAsync(context.CancellationToken))
```
{
if (request.Subscribe)

```

trackedIds.Add(Guid.Parse(request.OrderId));
```
else

```

trackedIds.TryRemove(Guid.Parse(request.OrderId));
```
}
}, context.CancellationToken);

- 227 -
```


<a id='p228'></a>
<!-- Página 228 -->

```
C# 2026: Enterprise Mastery




// Foreground: stream order events to client
await foreach (var @event in
```

_events.StreamAsync(context.CancellationToken))
```
{
if (trackedIds.Contains(@event.OrderId))
{
await responseStream.WriteAsync(new
```

OrderUpdate
```
{
OrderId = @event.OrderId.ToString(),
Status = @event.NewStatus,
Timestamp =
```

Timestamp.FromDateTimeOffset(@event.OccurredAt)
```
});
}
}

await receiveTask;
}
```

}




SignalR at Scale: Backplane Configuration

// Supplement/SignalRScale.cs
// Scale SignalR across multiple servers with Redis
// backplane
builder.Services.AddSignalR()
```
.AddStackExchangeRedis(

```

builder.Configuration.GetConnectionString("Redis")!,
```
options =>
{
options.Configuration.ChannelPrefix =
```

RedisChannel.Literal("signalr:");
```
});

```

// Strongly-typed hub
public interface IOrderClient
{

```
- 228 -
```


<a id='p229'></a>
<!-- Página 229 -->

```
C# 2026: Enterprise Mastery


Task OrderStatusChanged(OrderStatusUpdate update);
Task NewOrderAlert(NewOrderNotification notification);
```

}

public class OrderHub : Hub<IOrderClient>
{
```
public async Task SubscribeToOrder(string orderId)
{
await Groups.AddToGroupAsync(Context.ConnectionId,
```

$"order:{orderId}");
```
}

public async Task UnsubscribeFromOrder(string orderId)
{
await
```

Groups.RemoveFromGroupAsync(Context.ConnectionId, $"order:
{orderId}");
```
}
```

}

// Push updates from a domain event handler
public class OrderStatusEventHandler :
INotificationHandler<OrderStatusChanged>
{
```
private readonly IHubContext<OrderHub, IOrderClient>
```

_hub;

```
public OrderStatusEventHandler(IHubContext<OrderHub,
```

IOrderClient> hub)
```
=> _hub = hub;

public async Task Handle(OrderStatusChanged
```

notification, CancellationToken ct)
```
{
// Push to all clients tracking this order
await _hub.Clients
.Group($"order:{notification.OrderId}")
.OrderStatusChanged(new OrderStatusUpdate
{
OrderId = notification.OrderId,
NewStatus = notification.NewStatus,
UpdatedAt = notification.OccurredAt
});
}

- 229 -
```


<a id='p230'></a>
<!-- Página 230 -->

```
C# 2026: Enterprise Mastery


```

}




```
- 230 -
```


<a id='p231'></a>
<!-- Página 231 -->

```
C# 2026: Enterprise Mastery



```

Deep Dive: Decorator Pattern with DI
The decorator pattern adds cross-cutting concerns — logging, caching,
validation, retry — to any interface without modifying the
implementation. In .NET the Scrutor library makes decorator registration
clean.


// Supplement/DecoratorPattern.cs
// Base interface and implementation
public interface IOrderRepository
{
```
Task<Order?> GetAsync(Guid id, CancellationToken ct =
```

default);
```
Task SaveAsync(Order order, CancellationToken ct =
```

default);
}

// Decorator 1: Caching
public class CachingOrderRepository : IOrderRepository
{
```
private readonly IOrderRepository _inner;
private readonly IDistributedCache _cache;

public CachingOrderRepository(IOrderRepository inner,
```

IDistributedCache cache)
```
{
_inner = inner;
_cache = cache;
}

public async Task<Order?> GetAsync(Guid id,
```

CancellationToken ct = default)
```
{
var key = $"order:{id}";
var cached = await _cache.GetStringAsync(key, ct);
if (cached is not null) return
```

JsonSerializer.Deserialize<Order>(cached);

```
var order = await _inner.GetAsync(id, ct);
if (order is not null)
await _cache.SetStringAsync(key,
```

JsonSerializer.Serialize(order),

```
- 231 -
```


<a id='p232'></a>
<!-- Página 232 -->

```
C# 2026: Enterprise Mastery


new DistributedCacheEntryOptions
```

{ SlidingExpiration = TimeSpan.FromMinutes(5) }, ct);
```
return order;
}

public Task SaveAsync(Order order, CancellationToken ct
```

= default)
```
=> _inner.SaveAsync(order, ct);
```

}

// Decorator 2: Logging
public class LoggingOrderRepository : IOrderRepository
{
```
private readonly IOrderRepository _inner;
private readonly ILogger<LoggingOrderRepository>
```

_logger;

```
public LoggingOrderRepository(IOrderRepository inner,
ILogger<LoggingOrderRepository> logger)
{
_inner = inner;
_logger = logger;
}

public async Task<Order?> GetAsync(Guid id,
```

CancellationToken ct = default)
```
{
_logger.LogDebug("Fetching order {OrderId}", id);
var sw = Stopwatch.StartNew();
var result = await _inner.GetAsync(id, ct);
_logger.LogDebug("Fetched order {OrderId} in {Ms}ms
```

(found={Found})",
```
id, sw.ElapsedMilliseconds, result is not
```

null);
```
return result;
}

public async Task SaveAsync(Order order,
```

CancellationToken ct = default)
```
{
_logger.LogInformation("Saving order {OrderId}",
```

order.Id);
```
await _inner.SaveAsync(order, ct);
}

- 232 -
```


<a id='p233'></a>
<!-- Página 233 -->

```
C# 2026: Enterprise Mastery


```

}

// Registration with Scrutor — order matters (outermost
// first)
builder.Services.AddScoped<IOrderRepository,
EfCoreOrderRepository>();
builder.Services.Decorate<IOrderRepository,
CachingOrderRepository>();
builder.Services.Decorate<IOrderRepository,
LoggingOrderRepository>();
// Resolution chain: Logging -> Caching -> EfCore




Keyed Services for Multi-Tenant DI

// Supplement/KeyedServices.cs
// .NET 8+ keyed services: different implementations by
// named key
public interface IPaymentGateway
{
```
Task<PaymentResult> ChargeAsync(PaymentRequest request,
```

CancellationToken ct);
}

// Register multiple implementations with keys
builder.Services.AddKeyedScoped<IPaymentGateway,
StripeGateway>("stripe");
builder.Services.AddKeyedScoped<IPaymentGateway,
PayPalGateway>("paypal");
builder.Services.AddKeyedScoped<IPaymentGateway,
BraintreeGateway>("braintree");

// Resolve by key at runtime — no factory pattern needed
public class PaymentService
{
```
private readonly IServiceProvider _sp;

public async Task<PaymentResult> ProcessAsync(Order
```

order, string gatewayId)
```
{



- 233 -
```


<a id='p234'></a>
<!-- Página 234 -->

```
C# 2026: Enterprise Mastery


var gateway =
```

_sp.GetRequiredKeyedService<IPaymentGateway>(gatewayId);
```
return await
```

gateway.ChargeAsync(PaymentRequest.From(order));
```
}
```

}

// Or inject directly with [FromKeyedServices] attribute
public class CheckoutService
{
```
public CheckoutService(
[FromKeyedServices("stripe")] IPaymentGateway
```

stripeGateway,
```
[FromKeyedServices("paypal")] IPaymentGateway
```

paypalGateway)
```
{
// Both injected at construction time
}
```

}

// Tenant-based gateway selection
public class TenantPaymentService
{
```
private readonly IServiceProvider _sp;
private readonly ITenantContext _tenant;

public async Task<PaymentResult> ProcessAsync(Order
```

order, CancellationToken ct)
```
{
// "stripe", "paypal", etc.
var gatewayId = _tenant.Current.PaymentGateway;
var gateway =
```

_sp.GetRequiredKeyedService<IPaymentGateway>(gatewayId);
```
return await
```

gateway.ChargeAsync(PaymentRequest.From(order), ct);
```
}
```

}




```
- 234 -
```


<a id='p235'></a>
<!-- Página 235 -->

```
C# 2026: Enterprise Mastery



```

Deep Dive: Health Checks for Production
Readiness
Health checks are the bridge between your application and the
infrastructure that manages it. Kubernetes, load balancers, and service
meshes all rely on health endpoints to make routing and scheduling
decisions.


// Supplement/HealthChecks.cs
builder.Services.AddHealthChecks()
```
// Database: verifies the connection and can run a test
// query
.AddNpgsql(

```

builder.Configuration.GetConnectionString("Postgres")!,
```
name: "postgres",
tags: ["ready", "database"])

// Redis: verifies connectivity
.AddRedis(

```

builder.Configuration.GetConnectionString("Redis")!,
```
name: "redis",
tags: ["ready", "cache"])

// Custom health check: verifies business-critical data
// is available
.AddCheck<OrderQueueHealthCheck>("order-queue",
failureStatus: HealthStatus.Degraded,
tags: ["ready"])

// External dependency: HTTP-based check
.AddUrlGroup(
new
```

Uri(builder.Configuration["PaymentService:HealthUrl"]!),
```
name: "payment-service",
failureStatus: HealthStatus.Degraded,
tags: ["ready"]);

```

// Custom health check implementation
public class OrderQueueHealthCheck : IHealthCheck


```
- 235 -
```


<a id='p236'></a>
<!-- Página 236 -->

```
C# 2026: Enterprise Mastery


```

{
```
private readonly IOrderQueue _queue;

public OrderQueueHealthCheck(IOrderQueue queue) =>
```

_queue = queue;

```
public async Task<HealthCheckResult> CheckHealthAsync(
HealthCheckContext context, CancellationToken ct)
{
try
{
var depth = await _queue.GetDepthAsync(ct);
var data = new Dictionary<string, object>
```

{ ["queue_depth"] = depth };

```
return depth switch
{
< 1000 => HealthCheckResult.Healthy("Queue
```

is healthy", data),
```
< 5000 => HealthCheckResult.Degraded("Queue
```

is building up", data),
```
_ => HealthCheckResult.Unhealthy("Queue is
```

overloaded", data: data)
```
};
}
catch (Exception ex)
{
return HealthCheckResult.Unhealthy("Queue check
```

failed", ex);
```
}
}
```

}




Configuration Hot-Reload in Kubernetes

// Supplement/ConfigHotReload.cs
// IOptionsMonitor: responds to configuration changes at
// runtime
public class FeatureFlagService
{

```
- 236 -
```


<a id='p237'></a>
<!-- Página 237 -->

```
C# 2026: Enterprise Mastery


private readonly IOptionsMonitor<FeatureFlags> _flags;
private readonly ILogger<FeatureFlagService> _logger;

public FeatureFlagService(IOptionsMonitor<FeatureFlags>
```

flags,
```
ILogger<FeatureFlagService> logger)
{
_flags = flags;
// Subscribe to changes — executed when config file
// is updated
_flags.OnChange(newFlags =>
{
_logger.LogInformation("Feature flags updated:
```

{Flags}",
```
JsonSerializer.Serialize(newFlags));
});
}

public bool IsEnabled(string featureName)
=> _flags.CurrentValue.IsEnabled(featureName);
```

}

// In Kubernetes: ConfigMap mounted as a file +
// IConfiguration file watcher
// When you apply: kubectl apply -f configmap.yaml
// The file changes, IConfiguration detects it,
// IOptionsMonitor fires

// appsettings configuration provider (automatic in ASP.NET
// Core):
builder.Configuration.AddJsonFile("appsettings.json",
optional: false, reloadOnChange: true);
builder.Configuration.AddJsonFile(
```
$"appsettings.{env.EnvironmentName}.json", optional:
```

true, reloadOnChange: true);

// For Azure App Configuration with real-time push:
builder.Configuration.AddAzureAppConfiguration(options =>
{

options.Connect(builder.Configuration["AzureAppConfig:Conne
ctionString"])
```
.UseFeatureFlags(ff => ff.CacheExpirationInterval =
```

TimeSpan.FromSeconds(30))

```
- 237 -
```


<a id='p238'></a>
<!-- Página 238 -->

```
C# 2026: Enterprise Mastery


.ConfigureRefresh(refresh =>
{
refresh.Register("Sentinel", refreshAll: true)
.SetCacheExpiration(TimeSpan.FromSeconds
```

(30));
```
});
```

});
builder.Services.AddAzureAppConfiguration();
// Registers middleware to poll for changes
app.UseAzureAppConfiguration();




```
- 238 -
```


<a id='p239'></a>
<!-- Página 239 -->

```
C# 2026: Enterprise Mastery



```

Deep Dive: API Gateway Patterns with YARP
YARP (Yet Another Reverse Proxy) is Microsoft's production-grade
reverse proxy library for .NET. It powers Azure, and it is the right tool for
API Gateway scenarios that require custom .NET middleware,
authentication orchestration, or request transformation.


// Supplement/YarpGateway.cs
builder.Services.AddReverseProxy()
```
.LoadFromConfig(builder.Configuration.GetSection("Rever
```

seProxy"))
```
.AddTransforms(transformBuilder =>
{
// Add correlation ID to all proxied requests
transformBuilder.AddRequestTransform(async
```

transform =>
```
{
var correlationId =
```

transform.HttpContext.TraceIdentifier;

transform.ProxyRequest.Headers.TryAddWithoutValidation(
```
"X-Correlation-ID", correlationId);
await Task.CompletedTask;
});

// Strip internal headers before forwarding to
// backends
transformBuilder.AddRequestHeaderRemove("X-
```

Internal-Secret");
```
});

```

// Custom YARP middleware: JWT -> backend token exchange
app.UseAuthentication();
app.UseAuthorization();

app.MapReverseProxy(pipeline =>
{
```
pipeline.Use(async (context, next) =>
{
// Exchange user JWT for a service-to-service token
if (context.User.Identity?.IsAuthenticated == true)
{

- 239 -
```


<a id='p240'></a>
<!-- Página 240 -->

```
C# 2026: Enterprise Mastery


var token = await
```

TokenExchangeService.GetBackendTokenAsync(context.User);
```
context.Request.Headers["X-Service-Token"] =
```

token;
```
}
await next(context);
});
```

});

// appsettings.json routes
// "ReverseProxy": {
// "Routes": {
// "orders": {
// "ClusterId": "orders-cluster",
// "Match": { "Path": "/api/orders/{**catch-all}" }
// }
// },
// "Clusters": {
// "orders-cluster": {
// "Destinations": {
// "orders-primary": { "Address":
// "http://orders-service:8080/" }
// }
// }
// }
// }




Saga Pattern for Distributed Transactions

// Supplement/SagaPattern.cs
// Choreography-based saga: each service publishes events
// and reacts to others
// No central coordinator — looser coupling, harder to
// debug

// Order service publishes OrderCreated
public class CreateOrderHandler :
IRequestHandler<CreateOrderCommand>
{



```
- 240 -
```


<a id='p241'></a>
<!-- Página 241 -->

```
C# 2026: Enterprise Mastery


public async Task Handle(CreateOrderCommand cmd,
```

CancellationToken ct)
```
{
var order = new Order(cmd);
await _db.Orders.AddAsync(order, ct);
await _db.SaveChangesAsync(ct);
await _bus.PublishAsync(new OrderCreated(order.Id,
```

order.Lines), ct);
```
}
```

}

// Inventory service reacts to OrderCreated
public class ReserveInventoryConsumer :
IConsumer<OrderCreated>
{
```
public async Task Consume(ConsumeContext<OrderCreated>
```

context)
```
{
var success = await
```

_inventory.TryReserveAsync(context.Message.Lines);
```
if (success)
await context.Publish(new
```

InventoryReserved(context.Message.OrderId));
```
else
await context.Publish(new
```

InventoryReservationFailed(context.Message.OrderId));
```
}
```

}

// Payment service reacts to InventoryReserved
public class ChargePaymentConsumer :
IConsumer<InventoryReserved>
{
```
public async Task
```

Consume(ConsumeContext<InventoryReserved> context)
```
{
var result = await
```

_payment.ChargeAsync(context.Message.OrderId);
```
if (result.Success)
await context.Publish(new
```

PaymentCharged(context.Message.OrderId));
```
else
await context.Publish(new
```

PaymentFailed(context.Message.OrderId));

```
- 241 -
```


<a id='p242'></a>
<!-- Página 242 -->

```
C# 2026: Enterprise Mastery


}
```

}

// Compensating transaction on failure: release reserved
// inventory
public class PaymentFailedConsumer :
IConsumer<PaymentFailed>
{
```
public async Task Consume(ConsumeContext<PaymentFailed>
```

context)
```
{
await
```

_inventory.ReleaseReservationAsync(context.Message.OrderId)
;
```
await
```

_orders.MarkFailedAsync(context.Message.OrderId);
```
// Notify customer of failure
}
```

}




```
- 242 -
```


<a id='p243'></a>
<!-- Página 243 -->

```
C# 2026: Enterprise Mastery



```

Deep Dive: LINQ Internals and Custom Operators
Understanding how LINQ works internally lets you write better queries
and build your own operators that compose cleanly with the built-in set.
The key insight is that LINQ is lazy: nothing executes until you
enumerate.


// Supplement/LinqDeep.cs
// 1. Custom LINQ operator: Batch — splits a sequence into
// chunks
public static IEnumerable<IReadOnlyList<T>> Batch<T>(
```
this IEnumerable<T> source, int batchSize)
```

{
```
ArgumentNullException.ThrowIfNull(source);

```

ArgumentOutOfRangeException.ThrowIfNegativeOrZero(batchSize
);

```
return Core(source, batchSize);

static IEnumerable<IReadOnlyList<T>>
```

Core(IEnumerable<T> src, int size)
```
{
var batch = new List<T>(size);
foreach (var item in src)
{
batch.Add(item);
if (batch.Count == size)
{
yield return batch;
batch = new List<T>(size);
}
}
if (batch.Count > 0) yield return batch;
}
```

}

// Usage: process large datasets in chunks without loading
// everything
await foreach (var batch in
allOrderIds.Batch(100).ToAsyncEnumerable())
{

```
- 243 -
```


<a id='p244'></a>
<!-- Página 244 -->

```
C# 2026: Enterprise Mastery


var orders = await _db.Orders.Where(o =>
```

batch.Contains(o.Id)).ToListAsync();
```
await ProcessBatchAsync(orders);
```

}

// 2. Custom aggregation: weighted average
public static double WeightedAverage<T>(
```
this IEnumerable<T> source,
Func<T, double> value,
Func<T, double> weight)
```

{
```
var totalWeight = 0.0;
var weightedSum = 0.0;
foreach (var item in source)
{
var w = weight(item);
totalWeight += w;
weightedSum += value(item) * w;
}
return totalWeight == 0 ? 0 : weightedSum /
```

totalWeight;
}

// 3. Defer expensive computation with lazy LINQ
```
var expensive = source
.Where(x => x.IsEligible) // Not yet evaluated
.OrderByDescending(x => x.Score) // Not yet evaluated
.Take(10); // Not yet evaluated

```

// Everything evaluates here — once
foreach (var item in expensive) Process(item);

// 4. Short-circuiting with Any() and All()
// BAD: evaluates all 1M items
```
var hasHigh = orders.Where(o => o.Amount > 10_000).Any();

```

// GOOD: stops at first match — potentially evaluates 1
// item
```
var hasHigh = orders.Any(o => o.Amount > 10_000);




- 244 -
```


<a id='p245'></a>
<!-- Página 245 -->

```
C# 2026: Enterprise Mastery



```

Expression Trees: Dynamic Queries at Runtime
Expression trees let you build LINQ queries programmatically at runtime
— for dynamic filtering, sorting, and projection. Entity Framework
translates expression trees to SQL, so runtime-built expressions get the
same query optimisation as hand-written LINQ.


// Supplement/ExpressionTrees.cs
// Build a dynamic filter from user-provided criteria
public static Expression<Func<Order, bool>>
BuildFilter(OrderSearchCriteria criteria)
{
```
var param = Expression.Parameter(typeof(Order), "o");
Expression? body = null;

if (criteria.MinAmount.HasValue)
{
var prop = Expression.Property(param,
```

nameof(Order.Amount));
```
var constant =
```

Expression.Constant(criteria.MinAmount.Value);
```
var comparison =
```

Expression.GreaterThanOrEqual(prop, constant);
```
body = body is null ? comparison :
```

Expression.AndAlso(body, comparison);
```
}

if (criteria.Status.HasValue)
{
var prop = Expression.Property(param,
```

nameof(Order.Status));
```
var constant =
```

Expression.Constant(criteria.Status.Value);
```
var comparison = Expression.Equal(prop, constant);
body = body is null ? comparison :
```

Expression.AndAlso(body, comparison);
```
}

if (criteria.CustomerId.HasValue)
{
var prop = Expression.Property(param,
```

nameof(Order.CustomerId));

```
- 245 -
```


<a id='p246'></a>
<!-- Página 246 -->

```
C# 2026: Enterprise Mastery


var constant =
```

Expression.Constant(criteria.CustomerId.Value);
```
var comparison = Expression.Equal(prop, constant);
body = body is null ? comparison :
```

Expression.AndAlso(body, comparison);
```
}

// Default: match everything
body ??= Expression.Constant(true);
return Expression.Lambda<Func<Order, bool>>(body,
```

param);
}

// Use in EF Core — translated to optimal SQL
public async Task<List<Order>>
SearchAsync(OrderSearchCriteria criteria, CancellationToken
ct)
{
```
var filter = BuildFilter(criteria);
return await _db.Orders.Where(filter).ToListAsync(ct);
```

}

// Dynamic sorting
public static IQueryable<T> OrderByDynamic<T>(this
IQueryable<T> source,
```
string propertyName, bool descending = false)
```

{
```
var param = Expression.Parameter(typeof(T), "x");
var property = Expression.Property(param,
```

propertyName);
```
var selector = Expression.Lambda(property, param);

var method = descending ? "OrderByDescending" :
```

"OrderBy";
```
var call = Expression.Call(typeof(Queryable), method,
[typeof(T), property.Type],
source.Expression, selector);

return source.Provider.CreateQuery<T>(call);
```

}

// Usage: sort column from UI
```
var sorted = orders.OrderByDynamic(sortColumn, descending:
```

true);

```
- 246 -
```


<a id='p247'></a>
<!-- Página 247 -->

```
C# 2026: Enterprise Mastery




```

- 247 -

<a id='p248'></a>
<!-- Página 248 -->

```
C# 2026: Enterprise Mastery



```

Deep Dive: Specification Pattern
The Specification pattern encapsulates query predicates as first-class
objects that can be combined, reused, and named. This eliminates
duplicate query logic scattered across repositories and application
services.


// Supplement/SpecificationPattern.cs
// Base specification
public abstract class Specification<T>
{
```
public abstract Expression<Func<T, bool>>
```

ToExpression();

```
public bool IsSatisfiedBy(T entity) =>
```

ToExpression().Compile()(entity);

```
public Specification<T> And(Specification<T> other) =>
new AndSpecification<T>(this, other);

public Specification<T> Or(Specification<T> other) =>
new OrSpecification<T>(this, other);

public Specification<T> Not() => new
```

NotSpecification<T>(this);
}

// Concrete specifications — named business rules
public class PendingOrderSpec : Specification<Order>
{
```
public override Expression<Func<Order, bool>>
```

ToExpression() =>
```
o => o.Status == OrderStatus.Pending;
```

}

public class LargeOrderSpec : Specification<Order>
{
```
private readonly decimal _threshold;
public LargeOrderSpec(decimal threshold) => _threshold
```

= threshold;




```
- 248 -
```


<a id='p249'></a>
<!-- Página 249 -->

```
C# 2026: Enterprise Mastery


public override Expression<Func<Order, bool>>
```

ToExpression() =>
```
o => o.Amount >= _threshold;
```

}

public class OrderForCustomerSpec : Specification<Order>
{
```
private readonly Guid _customerId;
public OrderForCustomerSpec(Guid id) => _customerId =
```

id;

```
public override Expression<Func<Order, bool>>
```

ToExpression() =>
```
o => o.CustomerId == _customerId;
```

}

// Composite specifications
public class AndSpecification<T> : Specification<T>
{
```
private readonly Specification<T> _left, _right;

public AndSpecification(Specification<T> left,
```

Specification<T> right)
```
{
_left = left;
_right = right;
}

public override Expression<Func<T, bool>>
```

ToExpression()
```
{
var left = _left.ToExpression();
var right = _right.ToExpression();
var param = left.Parameters[0];
var body = Expression.AndAlso(left.Body,
Expression.Invoke(right, param));
return Expression.Lambda<Func<T, bool>>(body,
```

param);
```
}
```

}

// Repository using specifications
public class OrderRepository
{

```
- 249 -
```


<a id='p250'></a>
<!-- Página 250 -->

```
C# 2026: Enterprise Mastery


public async Task<List<Order>>
```

FindAsync(Specification<Order> spec,
```
CancellationToken ct = default)
{
return await
```

_db.Orders.Where(spec.ToExpression()).ToListAsync(ct);
```
}
```

}

// Usage — composable, readable, reusable
```
var spec = new PendingOrderSpec()
.And(new LargeOrderSpec(1000))
.And(new OrderForCustomerSpec(customerId));

var orders = await _repo.FindAsync(spec);




```

Factory and Builder Patterns in Domain Models

// Supplement/FactoryBuilder.cs
// Factory method: enforce invariants at creation time
public class Order
{
```
// Private constructor — must use factory
private Order() { }

public Guid Id { get; private set; }
public Guid CustomerId { get; private set; }
public OrderStatus Status { get; private set; }
public List<OrderLine> Lines { get; private set; } =
```

new();
```
public decimal Total => Lines.Sum(l => l.Amount);

// Factory: validates and constructs, returns Result
public static Result<Order> Create(Guid customerId,
```

IEnumerable<OrderLine> lines)
```
{
if (customerId == Guid.Empty)
return Result.Failure<Order>("Customer ID
```

cannot be empty");



```
- 250 -
```


<a id='p251'></a>
<!-- Página 251 -->

```
C# 2026: Enterprise Mastery


var lineList = lines.ToList();
if (lineList.Count == 0)
return Result.Failure<Order>("Order must have
```

at least one line");

```
if (lineList.Any(l => l.Quantity <= 0))
return Result.Failure<Order>("All line
```

quantities must be positive");

```
return Result.Success(new Order
{
Id = Guid.NewGuid(),
CustomerId = customerId,
Status = OrderStatus.Draft,
Lines = lineList
});
}
```

}

// Fluent builder for complex test data construction
public class OrderBuilder
{
```
private Guid _customerId = Guid.NewGuid();
private OrderStatus _status = OrderStatus.Pending;
private readonly List<OrderLine> _lines = [];

public OrderBuilder ForCustomer(Guid id) { _customerId
```

= id; return this; }
```
public OrderBuilder WithStatus(OrderStatus s) { _status
```

= s; return this; }

```
public OrderBuilder WithLine(string sku, int qty,
```

decimal price)
```
{
_lines.Add(new OrderLine(sku, qty, price));
return this;
}

public Order Build() => new()
{
Id = Guid.NewGuid(),
CustomerId = _customerId,
Status = _status,
Lines = _lines

- 251 -
```


<a id='p252'></a>
<!-- Página 252 -->

```
C# 2026: Enterprise Mastery


};
```

}

// In tests: readable, intention-revealing
```
var order = new OrderBuilder()
.ForCustomer(customer.Id)
.WithStatus(OrderStatus.Pending)
.WithLine("SKU-001", qty: 2, price: 49.99m)
.WithLine("SKU-002", qty: 1, price: 99.99m)
.Build();




- 252 -
```


<a id='p253'></a>
<!-- Página 253 -->

```
C# 2026: Enterprise Mastery



```

Deep Dive: Resilience Pipelines with Polly v8
Polly v8 introduced a unified ResiliencePipeline API that replaces the
older Policy-based approach. Pipelines compose strategies — retry, circuit
breaker, timeout, rate limiter, hedging — into a single, ordered execution
chain.


// Supplement/PollyResilience.cs
// Build a reusable resilience pipeline
```
var pipeline = new
```

ResiliencePipelineBuilder<HttpResponseMessage>()
```
// 1. Total timeout for the entire operation
.AddTimeout(TimeSpan.FromSeconds(10))

// 2. Retry with exponential back-off and jitter
.AddRetry(new RetryStrategyOptions<HttpResponseMessage>
{
MaxRetryAttempts = 3,
BackoffType = DelayBackoffType.Exponential,
UseJitter = true,
Delay = TimeSpan.FromMilliseconds(200),
ShouldHandle = new
```

PredicateBuilder<HttpResponseMessage>()
```
.Handle<HttpRequestException>()
.HandleResult(r => r.StatusCode ==
```

HttpStatusCode.ServiceUnavailable
```
|| r.StatusCode ==
```

HttpStatusCode.TooManyRequests),
```
OnRetry = args =>
{
_logger.LogWarning("Retry {Attempt} after
```

{Delay}",
```
args.AttemptNumber, args.RetryDelay);
return ValueTask.CompletedTask;
}
})

// 3. Circuit breaker — opens after 50% failure rate
.AddCircuitBreaker(new
```

CircuitBreakerStrategyOptions<HttpResponseMessage>
```
{
FailureRatio = 0.5,

- 253 -
```


<a id='p254'></a>
<!-- Página 254 -->

```
C# 2026: Enterprise Mastery


SamplingDuration = TimeSpan.FromSeconds(30),
MinimumThroughput = 10,
BreakDuration = TimeSpan.FromSeconds(30),
OnOpened = args =>
{
_logger.LogError("Circuit opened: {Reason}",
```

args.Outcome.Exception?.Message);
```
return ValueTask.CompletedTask;
}
})

// 4. Per-attempt timeout (prevents a single slow call
// from blocking retries)
.AddTimeout(TimeSpan.FromSeconds(3))

.Build();

```

// Register named pipelines in DI
builder.Services.AddResiliencePipeline<string,
HttpResponseMessage>(
```
"payment-service", (builder, _) =>
{
builder
.AddRetry(new
```

RetryStrategyOptions<HttpResponseMessage>
```
{
MaxRetryAttempts = 2,
Delay = TimeSpan.FromMilliseconds(500)
})
.AddCircuitBreaker(new
```

CircuitBreakerStrategyOptions<HttpResponseMessage>
```
{
FailureRatio = 0.3,
SamplingDuration = TimeSpan.FromSeconds(60)
});
});

```

// Inject and use
public class PaymentGatewayClient
{
```
private readonly
```

ResiliencePipeline<HttpResponseMessage> _pipeline;




```
- 254 -
```


<a id='p255'></a>
<!-- Página 255 -->

```
C# 2026: Enterprise Mastery


public
```

PaymentGatewayClient(ResiliencePipelineProvider<string>
provider)
```
{
_pipeline =
```

provider.GetPipeline<HttpResponseMessage>("paymentservice");
```
}

public async Task<PaymentResult>
```

ChargeAsync(ChargeRequest request, CancellationToken ct)
```
{
var response = await _pipeline.ExecuteAsync(
async token => await
```

_http.PostAsJsonAsync("/charge", request, token),
```
ct);

response.EnsureSuccessStatusCode();
return await
```

response.Content.ReadFromJsonAsync<PaymentResult>(ct) ??
default!;
```
}
```

}




Hedging: Parallel Requests for Low-Latency APIs
Hedging fires a second request if the first doesn't respond within a
threshold. Used judiciously on read-only endpoints, it reduces tail latency
at the cost of extra backend load.


// Supplement/HedgingStrategy.cs
// Hedging: if first call doesn't respond in 200ms, fire a
// second in parallel
```
var pipeline = new ResiliencePipelineBuilder<string>()
.AddHedging(new HedgingStrategyOptions<string>
{
MaxHedgedAttempts = 2,
Delay = TimeSpan.FromMilliseconds(200),
// Only hedge on slow responses, not failures
ShouldHandle = new PredicateBuilder<string>()

- 255 -
```


<a id='p256'></a>
<!-- Página 256 -->

```
C# 2026: Enterprise Mastery


// Only hedge on delay, not result
.HandleResult(_ => false),
ActionGenerator = args =>
{
// Try a different replica for the hedged
// request
return () =>
```

GetFromReplicaAsync(args.AttemptNumber,
args.ActionContext.CancellationToken);
```
}
})
.Build();

```

// P99 latency improves dramatically because the second
// attempt often returns
// before the first slow one finishes. The faster response
// wins.
// Caution: only use on idempotent read endpoints.




```
- 256 -
```


<a id='p257'></a>
<!-- Página 257 -->

```
C# 2026: Enterprise Mastery



```

Deep Dive: Span<T> Cookbook
Span<T> is the Swiss Army knife of zero-allocation .NET programming.
These recipes cover the most common patterns you will encounter when
optimising hot paths in enterprise applications.


// Supplement/SpanCookbook.cs
// 1. Parse CSV line without allocating strings for each
// field
public static void ParseCsvLine(ReadOnlySpan<char> line,
```
Action<ReadOnlySpan<char>, int> fieldCallback)
```

{
```
int fieldIndex = 0;
while (!line.IsEmpty)
{
int commaPos = line.IndexOf(',');
var field = commaPos >= 0 ? line[..commaPos] :
```

line;
```
fieldCallback(field.Trim(), fieldIndex++);
line = commaPos >= 0 ? line[(commaPos + 1)..] :
```

ReadOnlySpan<char>.Empty;
```
}
```

}

// 2. Parse integers from a span without ToString()
public static bool TryParseInt(ReadOnlySpan<char> span, out
int result)
```
=> int.TryParse(span, out result);

```

// 3. Efficient string splitting (no array allocation)
public static void SplitOnFirst(ReadOnlySpan<char> input,
char delimiter,
```
out ReadOnlySpan<char> left, out ReadOnlySpan<char>
```

right)
{
```
int idx = input.IndexOf(delimiter);
if (idx < 0) { left = input; right =
```

ReadOnlySpan<char>.Empty; return; }
```
left = input[..idx];
right = input[(idx + 1)..];
```

}



```
- 257 -
```


<a id='p258'></a>
<!-- Página 258 -->

```
C# 2026: Enterprise Mastery


```

// 4. Reuse buffer for multiple format operations
Span<char> buffer = stackalloc char[64];
if (orderId.TryFormat(buffer, out int written))
{
```
// Zero-allocation span view
var formatted = buffer[..written];
logger.LogDebug("Processing {OrderId}",
```

formatted.ToString());
}

// 5. Binary protocol parsing
public static OrderHeader ParseHeader(ReadOnlySpan<byte>
data)
{
```
// BinaryPrimitives: reads integers from byte spans
// without unsafe code
var version =
```

BinaryPrimitives.ReadUInt16BigEndian(data[..2]);
```
var messageType =
```

BinaryPrimitives.ReadUInt16BigEndian(data[2..4]);
```
var payloadLength =
```

BinaryPrimitives.ReadInt32BigEndian(data[4..8]);
```
return new OrderHeader(version, messageType,
```

payloadLength);
}

// 6. Memory<T> for async scenarios (Span<T> cannot cross
// await boundaries)
public async Task<int> ProcessChunkAsync(Memory<byte>
buffer, CancellationToken ct)
{
```
// Memory<T> can be passed across await points
int bytesRead = await _stream.ReadAsync(buffer, ct);
// Slice the memory for processing
// Span view for sync processing
ProcessBytes(buffer.Span[..bytesRead]);
return bytesRead;
```

}




```
- 258 -
```


<a id='p259'></a>
<!-- Página 259 -->

```
C# 2026: Enterprise Mastery



```

MemoryMarshal and Unsafe: When
Zero-Allocation Isn't Enough

// Supplement/MemoryMarshal.cs
// Cast span types without copying — use with extreme care
public static ReadOnlySpan<float>
AsFloats(ReadOnlySpan<byte> bytes)
{
```
// MemoryMarshal.Cast: reinterprets bytes as floats (no
// copy)
// Precondition: bytes.Length must be divisible by
// sizeof(float)
return MemoryMarshal.Cast<byte, float>(bytes);
```

}

// Read a struct from a byte span (e.g., from a network
// packet)
[StructLayout(LayoutKind.Sequential, Pack = 1)]
public struct PacketHeader
{
```
public ushort Version;
public ushort Type;
public int PayloadLength;
public long Timestamp;
```

}

public static ref readonly PacketHeader
ReadHeader(ReadOnlySpan<byte> data)
{
```
if (data.Length < Unsafe.SizeOf<PacketHeader>())
throw new ArgumentException("Buffer too small");
return ref MemoryMarshal.AsRef<PacketHeader>(data);
```

}

// Write struct to span for network transmission
public static int WriteHeader(Span<byte> destination, in
PacketHeader header)
{
```
MemoryMarshal.Write(destination, in header);
return Unsafe.SizeOf<PacketHeader>();
```

}


```
- 259 -
```


<a id='p260'></a>
<!-- Página 260 -->

```
C# 2026: Enterprise Mastery


```


## // IMPORTANT SAFETY NOTES:

// - MemoryMarshal.Cast assumes correct alignment;
// misaligned reads are UB on some architectures
// - These operations bypass type safety — test on all
// target platforms
// - Only use in hot paths where profiling proves
// allocation is the bottleneck
// - Document why unsafe is justified with a comment at
// each use site




```
- 260 -
```


<a id='p261'></a>
<!-- Página 261 -->

```
C# 2026: Enterprise Mastery



```

Deep Dive: Aggregate Roots and Domain Events
In Domain-Driven Design, the Aggregate Root is the only entry point for
modifying a cluster of related entities. It enforces invariants and
publishes domain events when significant things happen. This pattern is
the backbone of event-driven architectures.


// Supplement/AggregateRoot.cs
// Base class for all aggregate roots
public abstract class AggregateRoot
{
```
private readonly List<IDomainEvent> _events = [];

public IReadOnlyList<IDomainEvent> DomainEvents =>
```

_events.AsReadOnly();

```
protected void Raise(IDomainEvent @event) =>
```

_events.Add(@event);

```
public void ClearDomainEvents() => _events.Clear();
```

}

// Domain events — what happened, past tense
public record OrderPlaced(Guid OrderId, Guid CustomerId,
decimal Amount,
```
DateTimeOffset OccurredAt) : IDomainEvent;

```

public record OrderCancelled(Guid OrderId, string Reason,
```
DateTimeOffset OccurredAt) : IDomainEvent;

```

public record OrderShipped(Guid OrderId, string
TrackingNumber,
```
DateTimeOffset OccurredAt) : IDomainEvent;

```

// Aggregate root: Order
public class Order : AggregateRoot
{
```
// EF Core needs parameterless constructor
private Order() { }

public Guid Id { get; private set; }
public Guid CustomerId { get; private set; }

- 261 -
```


<a id='p262'></a>
<!-- Página 262 -->

```
C# 2026: Enterprise Mastery


public OrderStatus Status { get; private set; }
public Money Total { get; private set; }
private readonly List<OrderLine> _lines = [];
public IReadOnlyList<OrderLine> Lines =>
```

_lines.AsReadOnly();

```
public static Order Place(Guid customerId,
```

IEnumerable<OrderLine> lines)
```
{
var lineList = lines.ToList();
if (lineList.Count == 0) throw new
```

DomainException("Order must have lines");

```
var order = new Order
{
Id = Guid.NewGuid(),
CustomerId = customerId,
Status = OrderStatus.Pending,
};
order._lines.AddRange(lineList);
order.Total = Money.Sum(lineList.Select(l =>
```

l.LineTotal));

```
order.Raise(new OrderPlaced(order.Id, customerId,
```

order.Total.Amount,
```
DateTimeOffset.UtcNow));

return order;
}

public void Cancel(string reason)
{
if (Status == OrderStatus.Shipped)
throw new DomainException("Cannot cancel a
```

shipped order");

```
Status = OrderStatus.Cancelled;
Raise(new OrderCancelled(Id, reason,
```

DateTimeOffset.UtcNow));
```
}

public void MarkShipped(string trackingNumber)
{
if (Status != OrderStatus.Confirmed)

- 262 -
```


<a id='p263'></a>
<!-- Página 263 -->

```
C# 2026: Enterprise Mastery


throw new DomainException("Only confirmed
```

orders can be shipped");

```
Status = OrderStatus.Shipped;
Raise(new OrderShipped(Id, trackingNumber,
```

DateTimeOffset.UtcNow));
```
}
```

}

// Dispatch domain events after saving (via EF Core
// interceptor)
public class DomainEventDispatcher : SaveChangesInterceptor
{
```
private readonly IMediator _mediator;

public override async ValueTask<int> SavedChangesAsync(
SaveChangesCompletedEventData eventData, int
```

result, CancellationToken ct)
```
{
var aggregates = eventData.Context!.ChangeTracker
.Entries<AggregateRoot>()
.Select(e => e.Entity)
.Where(a => a.DomainEvents.Count > 0)
.ToList();

foreach (var aggregate in aggregates)
{
foreach (var domainEvent in
```

aggregate.DomainEvents)
```
await _mediator.Publish(domainEvent, ct);
aggregate.ClearDomainEvents();
}

return result;
}
```

}




```
- 263 -
```


<a id='p264'></a>
<!-- Página 264 -->

```
C# 2026: Enterprise Mastery



```

Enterprise C# Quick Reference
This reference section collects the most important patterns and idioms
```
from across this book into concise, copy-paste-ready snippets. Each
```

section corresponds to a common enterprise task.

Middleware Pipeline Reference

// Reference/MiddlewarePipeline.cs
// Correct middleware order for enterprise ASP.NET Core
// apps
```
var app = builder.Build();

```

// 1. Exception handling — must be first to catch all
// errors
app.UseExceptionHandler("/error");
// In development: app.UseDeveloperExceptionPage();

// 2. HSTS (only in production HTTPS)
if (!app.Environment.IsDevelopment())
```
app.UseHsts();

```

// 3. HTTPS redirection
app.UseHttpsRedirection();

// 4. Static files (before routing — short-circuits the
// pipeline)
app.UseStaticFiles();

// 5. Routing
app.UseRouting();

// 6. Rate limiting
app.UseRateLimiter();

// 7. CORS (after routing so CORS policy can match routes)
app.UseCors();

// 8. Authentication
app.UseAuthentication();


```
- 264 -
```


<a id='p265'></a>
<!-- Página 265 -->

```
C# 2026: Enterprise Mastery




```

// 9. Authorization (after authentication — needs identity
// context)
app.UseAuthorization();

// 10. Output caching (after auth — cache per-user
// responses correctly)
app.UseOutputCache();

// 11. Custom business middleware
app.UseMiddleware<TenantResolutionMiddleware>();
app.UseMiddleware<AuditLoggingMiddleware>();

// 12. Endpoint mapping — last
app.MapControllers();
app.MapEndpointModules();
app.MapHealthChecks("/health");




DI Registration Patterns Reference

// Reference/DiRegistration.cs
// Lifetime reference:
// Transient: new instance every time — for stateless
// services
// Scoped: new instance per HTTP request — for most
// services, DbContext
// Singleton: one instance for app lifetime — for caches,
// config, IHttpClientFactory

// Correct EF Core registration (Scoped — one context per
// request)
builder.Services.AddDbContext<AppDbContext>(opts =>
```
opts.UseNpgsql(connectionString)
.EnableSensitiveDataLogging(builder.Environment.IsD
```

evelopment())
```
.UseQueryTrackingBehavior(QueryTrackingBehavior.NoT
```

rackingWithIdentityResolution));

// HttpClient — always use IHttpClientFactory, never new
// HttpClient()

```
- 265 -
```


<a id='p266'></a>
<!-- Página 266 -->

```
C# 2026: Enterprise Mastery


```

builder.Services.AddHttpClient<OrderServiceClient>(client
=>
{
```
client.BaseAddress = new
```

Uri(builder.Configuration["Services:Orders"]!);
```
client.Timeout = TimeSpan.FromSeconds(30);
client.DefaultRequestHeaders.Add("Accept",
```

"application/json");
})
// Polly retry + circuit breaker
.AddStandardResilienceHandler();

// Assembly scanning with Scrutor
builder.Services.Scan(scan => scan
```
.FromAssemblyOf<Program>()
.AddClasses(c =>
```

c.AssignableTo<IValidator>()).AsImplementedInterfaces().Wit
hTransientLifetime()
```
.AddClasses(c =>
```

c.AssignableTo<ICommandHandler>()).AsImplementedInterfaces(
).WithScopedLifetime()
```
.AddClasses(c =>
```

c.AssignableTo<IQueryHandler>()).AsImplementedInterfaces().
WithScopedLifetime());

// Options pattern — strongly typed config
builder.Services.AddOptions<DatabaseOptions>()
```
.Bind(builder.Configuration.GetSection("Database"))
.ValidateDataAnnotations()
.ValidateOnStart();




```

Async Best Practices Reference

// Reference/AsyncBestPractices.cs

// RULE 1: ConfigureAwait(false) in library code, not in
// app code
// Library code — avoids capturing the sync context:
public async Task<T> LibraryMethodAsync<T>(...)
{

```
- 266 -
```


<a id='p267'></a>
<!-- Página 267 -->

```
C# 2026: Enterprise Mastery


var result = await SomeIOAsync().ConfigureAwait(false);
return Transform(result);
```

}
// Application code (ASP.NET Core, WPF) — no ConfigureAwait
// needed,
// ASP.NET Core has no synchronisation context by default

// RULE 2: Never block on async code
// WRONG — causes deadlock in contexts with sync context:
```
var result = task.Result;
var result = task.GetAwaiter().GetResult();
```

// RIGHT — await all the way up:
```
var result = await task;

```

// RULE 3: CancellationToken everywhere
public async Task ProcessAsync(int id, CancellationToken ct
= default)
{
```
var data = await _repo.GetAsync(id, ct);
await _processor.HandleAsync(data, ct);
```

}

// RULE 4: ValueTask for hot paths that often complete
// synchronously
// Returns ValueTask when result is often available
// immediately (e.g. from cache)
public ValueTask<Order?> GetFromCacheAsync(Guid id)
{
```
if (_cache.TryGet(id, out var order))
// No allocation
return ValueTask.FromResult<Order?>(order);
// Allocates Task
return new ValueTask<Order?>(_repo.GetAsync(id));
```

}

// RULE 5: Parallel.ForEachAsync for CPU+IO hybrid
// workloads
await Parallel.ForEachAsync(orderIds,
```
new ParallelOptions { MaxDegreeOfParallelism = 4,
```

CancellationToken = ct },
```
async (id, token) =>
{
var order = await _repo.GetAsync(id, token);
await ProcessAsync(order, token);

- 267 -
```


<a id='p268'></a>
<!-- Página 268 -->

```
C# 2026: Enterprise Mastery


});




```

Exception Handling Reference

// Reference/ExceptionHandling.cs
// Define exception hierarchy for your domain
public abstract class DomainException : Exception
{
```
protected DomainException(string message) :
```

base(message) { }
}

public class EntityNotFoundException : DomainException
{
```
public EntityNotFoundException(string entity, object
```

id)
```
: base($"{entity} with id {id} was not found") { }
```

}

public class BusinessRuleViolationException :
DomainException
{
```
public string RuleName { get; }
public BusinessRuleViolationException(string rule,
```

string message)
```
: base(message) => RuleName = rule;
```

}

// Global exception handler (catches everything unhandled)
app.UseExceptionHandler(handler =>
{
```
handler.Run(async context =>
{
var feature =
```

context.Features.Get<IExceptionHandlerFeature>();
```
var ex = feature?.Error;

(int status, string title) = ex switch
{
EntityNotFoundException => (404, "Not Found"),

- 268 -
```


<a id='p269'></a>
<!-- Página 269 -->

```
C# 2026: Enterprise Mastery


BusinessRuleViolationException => (422,
```

"Business Rule Violation"),
```
ValidationException => (400, "Validation
```

Failed"),
```
UnauthorizedAccessException => (403,
```

"Forbidden"),
```
_ => (500, "Internal Server Error")
};

if (status == 500)
logger.LogError(ex, "Unhandled exception on
```

{Path}", context.Request.Path);
```
else
logger.LogWarning(ex, "Domain error {Status} on
```

{Path}", status, context.Request.Path);

```
context.Response.StatusCode = status;
await context.Response.WriteAsJsonAsync(new
```

ProblemDetails
```
{
Status = status,
Title = title,
Detail = app.Environment.IsDevelopment() ?
```

ex?.Message : null,
```
Instance = context.Request.Path
});
});
```

});




EF Core Configuration Reference

// Reference/EfCoreConfig.cs
// IEntityTypeConfiguration — keep entity configuration out
// of DbContext
public class OrderConfiguration :
IEntityTypeConfiguration<Order>
{
```
public void Configure(EntityTypeBuilder<Order> builder)
{
builder.ToTable("Orders");

- 269 -
```


<a id='p270'></a>
<!-- Página 270 -->

```
C# 2026: Enterprise Mastery


builder.HasKey(o => o.Id);
// Domain generates IDs
builder.Property(o => o.Id).ValueGeneratedNever();

builder.Property(o => o.Status)
// Store as string, not integer
.HasConversion<string>()
.HasMaxLength(50);

builder.Property(o => o.Amount)
.HasPrecision(18, 2);

// Value object as owned entity
builder.OwnsOne(o => o.ShippingAddress, addr =>
{
addr.Property(a => a.Street).HasMaxLength(200);
addr.Property(a => a.City).HasMaxLength(100);
addr.Property(a =>
```

a.PostalCode).HasMaxLength(20);
```
});

// One-to-many: eager loading
builder.HasMany(o => o.Lines)
.WithOne()
.HasForeignKey(l => l.OrderId)
.OnDelete(DeleteBehavior.Cascade);

// Indexes for common query patterns
builder.HasIndex(o => o.CustomerId);
builder.HasIndex(o => new { o.Status,
```

o.CreatedAt });
```
builder.HasIndex(o => o.CreatedAt);

// Row version for optimistic concurrency
builder.Property<byte[]>("RowVersion")
.IsRowVersion()
.IsConcurrencyToken();
}
```

}

// DbContext: apply all configurations from assembly
protected override void OnModelCreating(ModelBuilder model)
{


```
- 270 -
```


<a id='p271'></a>
<!-- Página 271 -->

```
C# 2026: Enterprise Mastery




```

model.ApplyConfigurationsFromAssembly(typeof(AppDbContext).
Assembly);

```
// Convention: all string properties default to
// varchar(255) not nvarchar(max)
foreach (var prop in model.Model.GetEntityTypes()
.SelectMany(e => e.GetProperties())
.Where(p => p.ClrType == typeof(string)))
{
if (prop.GetMaxLength() == null)
prop.SetMaxLength(255);
}
```

}




```
- 271 -
```


<a id='p272'></a>
<!-- Página 272 -->

```
C# 2026: Enterprise Mastery



```

Performance Checklist
Use this checklist when reviewing a pull request or auditing a service for
performance.

Database
• All LINQ queries have been profiled — no N+1 problems
• Read-only queries use AsNoTracking()
• Frequently queried columns have database indexes
• Bulk operations use ExecuteUpdateAsync/ExecuteDeleteAsync
• Connection string includes connection pooling settings (MinPoolSize,
MaxPoolSize)

Memory
• Hot paths use ArrayPool<T> or MemoryPool<T> instead of new T[]
• String operations on hot paths use Span<T> or StringBuilder
• No boxing of value types on hot paths
• Large collections are pre-sized with known capacity
• IAsyncEnumerable used for streaming — no ToList() on large result
sets


## HTTP

• HttpClient registered via IHttpClientFactory (never new HttpClient())
• Response compression enabled (UseResponseCompression)
• Output caching configured for appropriate read endpoints
• HTTP/2 enabled for gRPC and high-throughput APIs
• Request/response payloads use System.Text.Json source generation

Async
• No .Result or .GetAwaiter().GetResult() calls
• No async void methods (except UI event handlers)
• CancellationToken accepted and forwarded on all async public
methods

```
- 272 -
```


<a id='p273'></a>
<!-- Página 273 -->

```
C# 2026: Enterprise Mastery


```

• ValueTask used for frequently-called async methods with sync
fast-paths
• Parallel work uses Parallel.ForEachAsync, not Task.WhenAll with
unbounded concurrency




```
- 273 -
```


<a id='p274'></a>
<!-- Página 274 -->

```
C# 2026: Enterprise Mastery



```

Security Checklist
Minimum security requirements before any enterprise API goes to
production.

Authentication & Authorization
• All endpoints require authentication except explicitly public ones
• Authorisation is resource-based, not just role-based
• JWTs have a short expiry (15 min–1 hour) with refresh token rotation
• Token validation includes audience, issuer, and signature verification
• No sensitive data (passwords, tokens) in URLs or logs

Input Validation
• All external inputs validated with FluentValidation or Data
Annotations
• String length limits applied to all string inputs
• File uploads have type validation, size limits, and are scanned
• SQL is parameterized — no string concatenation in queries
• Regex patterns use timeouts to prevent ReDoS attacks

Secrets and Con g
• No secrets in source code, appsettings.json, or environment variables
in plain text
• Secrets sourced from Key Vault or equivalent secrets manager
• Connection strings do not include passwords for production databases
• Managed Identity used for Azure service authentication
• API keys rotated on schedule and on suspected compromise

Transport
• HTTPS enforced in production (HSTS enabled)
• TLS 1.2+ only (TLS 1.0/1.1 disabled)
• Security headers set: X-Content-Type-Options, X-Frame-Options, CSP
• CORS policy is restrictive — not AllowAnyOrigin() in production

```
- 274 -
```


<a id='p275'></a>
<!-- Página 275 -->

```
C# 2026: Enterprise Mastery


```

• Rate limiting applied to all public-facing endpoints




```
- 275 -
```


<a id='p276'></a>
<!-- Página 276 -->

```
C# 2026: Enterprise Mastery



```

Code Review Guide for Senior Engineers
A great code review is not a grammar check. It is a transfer of
architectural knowledge and business context. This section outlines the
lens a senior C# engineer should apply when reviewing a pull request in
an enterprise codebase.

What to Look for First
Before reading a single line of implementation, check the pull request
description and tests. A PR without tests is a PR that will break in
production. A PR without a description is a PR that will break in the
future when someone needs to understand why this change was made.

Architecture Concerns
• Does this change belong in the layer it was placed in? (Infrastructure
logic in domain, UI logic in services — these are red flags.)
• Does this introduce a new dependency from a higher-level layer to a
lower-level one? (Application depending on Infrastructure — needs
an interface.)
• Is a new service being created that duplicates an existing one? (Check
for hidden duplication before approving new abstractions.)
• Does this change make the system harder to test or require more
mocking? (More mocks = more brittle tests = more future pain.)
• Is the new code doing one thing? (If you cannot summarise a class or
method in one sentence, it needs splitting.)

Performance Concerns
• Any LINQ over a DbSet without a Where clause (potential full table
scan).
• Any foreach loop that makes a DB or HTTP call (N+1).
• String concatenation in loops (use StringBuilder or Span<char>).
• new HttpClient() instead of IHttpClientFactory.
• Task.WhenAll with an unbounded list (can exhaust thread pool or
connection pool).
• Any synchronous I/O in an async method (blocks a thread).
```
- 276 -
```


<a id='p277'></a>
<!-- Página 277 -->

```
C# 2026: Enterprise Mastery


```

Security Concerns
• Any user-controlled input used in a SQL query without
parameterization.
• Authorization checks missing on new endpoints.
• Secrets hardcoded in configuration or code.
• Sensitive data (passwords, tokens, PII) logged.
• File upload endpoints without content-type and size validation.

Feedback That Improves Codebases
The goal of code review is not to be right — it is to make the codebase
better without demoralising the author. Separate blocking issues from
suggestions. Label comments clearly: 'Blocking: this will cause a
deadlock', 'Suggestion: consider using ObjectPool here for performance',
'Nit: variable name could be more descriptive'. Ask questions before
making accusations: 'Is there a reason we're not using async here?' is
better than 'This should be async'.




```
- 277 -
```


<a id='p278'></a>
<!-- Página 278 -->

```
C# 2026: Enterprise Mastery



```

Advanced C# Interview Questions and Answers
The following questions test deep understanding of C# and .NET
internals. They are the kind of questions that distinguish engineers who
have used the platform from those who understand it.

Q: What is the difference between Task and ValueTask, and when should
you use each?

A: Task is a reference type that always heap-allocates. ValueTask is a struct that
can avoid allocation when the result is available synchronously (from a cache, for
example). Use ValueTask for hot-path async methods that frequently complete
synchronously. Avoid ValueTask when the result is almost always async — the
overhead of checking the state adds complexity without benefit. Never await a
ValueTask more than once.

Q: Explain the difference between IEnumerable<T> and
IAsyncEnumerable<T>.

A: IEnumerable<T> is synchronous and blocking — it cannot yield from async
operations. IAsyncEnumerable<T> allows each MoveNextAsync() to be awaited,
enabling streaming of results from async sources like databases or network
streams. Use IAsyncEnumerable when processing large datasets to avoid
materialising all results in memory. EF Core returns IAsyncEnumerable via
AsAsyncEnumerable().

Q: What causes a deadlock in async code and how do you prevent it?

A: Deadlocks occur when you call .Result or .GetAwaiter().GetResult() on a Task
in a context that has a synchronisation context (ASP.NET classic, WPF,
WinForms). The awaited task tries to marshal back to the same thread that is
blocked waiting for it. Prevention: never block on async code. Async should
propagate all the way up the call stack. If you must call async from sync code (e.g.
constructor), use ConfigureAwait(false) in the async code and be aware of the
risk.

Q: What is the difference between struct and class in terms of memory
layout?

A: Structs are value types stored inline. A struct local that is not captured or
boxed typically lives on the stack; a struct field lives inside its containing object,
which may be on the heap. Classes are reference types — a reference (pointer) is
```
- 278 -
```


<a id='p279'></a>
<!-- Página 279 -->

```
C# 2026: Enterprise Mastery


```

stored, and the object itself is on the heap. Structs copy on assignment; classes
share a reference. Large structs are more expensive to copy than small ones, so
the guidance is to prefer structs for small, immutable, frequently-created values
(Point, Money, Guid). Value-type data that the GC does not have to trace as a
separate heap object reduces collection work.

Q: How does the garbage collector's generational model affect allocation
patterns?

A: The GC divides the heap into Gen 0 (newest, collected most often), Gen 1
(survivors from Gen 0), and Gen 2 (long-lived objects). Objects that die young
(most request-scoped objects) are collected cheaply in Gen 0 with minimal pause.
Objects that survive long enough reach Gen 2, which is collected infrequently but
with a longer pause. The goal is to either (a) avoid allocation entirely using
pooling or Span<T>, or (b) make objects short-lived so they die in Gen 0. Objects
that linger in Gen 1 are the worst case — they eventually promote to Gen 2 and
increase GC pressure.

Q: What is the difference between Func<T> and Expression<Func<T>>?

A: Func<T> is a compiled delegate — a pointer to executable code.
Expression<Func<T>> is a data structure that describes the delegate as an
abstract syntax tree. You can inspect and transform an Expression at runtime.
Entity Framework uses Expression<Func<T, bool>> in .Where() precisely
because it can read the expression tree and translate it to SQL. If you pass a Func,
EF must load all records and filter in memory. Always use Expression in
repository methods that will be translated to database queries.




```
- 279 -
```


<a id='p280'></a>
<!-- Página 280 -->

```
C# 2026: Enterprise Mastery



```

Closing Thoughts
Software engineering is a craft practised over a career, not a skill acquired
```
from a single book. The patterns and practices in these pages are tools —
```

powerful ones — but tools without judgment are dangerous.

The most important thing I want you to take from this book is not a code
pattern but a habit of mind: always ask why. Why is this service slow?
Profile it before optimising. Why is this code hard to change? Trace the
dependency that makes it rigid. Why did this bug reach production? Fix
the process, not just the code.

The C# and .NET platform in 2026 is extraordinary. The performance
characteristics of modern .NET rival C++ for many workloads. The
language features are expressive without being clever. The ecosystem is
mature and well-supported. You have excellent tools. Use them
thoughtfully.

Build systems that your colleagues — including your future self — can
understand, extend, and trust. Write code that reads like a description of
the problem it solves. And measure everything, because intuition about
performance is almost always wrong.

The companion code repository is listed on the copyright page and at the
end of this book. Pull requests with improvements, corrections, and new
examples are welcome. Good luck, and write great software.




```
- 280 -
```


<a id='p281'></a>
<!-- Página 281 -->

```
C# 2026: Enterprise Mastery



```

Deep Dive: .NET 10 Runtime Improvements
.NET 10 brought significant improvements to the JIT compiler, GC, and the
threading model. Understanding these changes helps you write code that
takes advantage of them, and explains performance characteristics you
may have observed in earlier versions.

JIT Compiler: Dynamic PGO in Production
Dynamic Profile-Guided Optimisation (PGO) was introduced in .NET 6 and
matured significantly in .NET 9 and 10. The JIT observes which code paths
are actually taken at runtime and recompiles hot methods with that
knowledge. The result is JIT-compiled code that approaches AOT quality
without the deployment complexity of NativeAOT.


// Reference/DynamicPgo.cs
// Dynamic PGO is enabled by default in .NET 8+
// To observe PGO effects in your application:

// 1. Check if tiered compilation is active (it enables

## // PGO)

// Set DOTNET_TC_QuickJitForLoops=0 to disable for
// comparison benchmarks

// 2. Profile before and after warmup — PGO improves after
// the JIT observes patterns
// A benchmark run needs adequate warmup iterations to see
// PGO benefits:
[GlobalSetup]
public async Task Setup()
{
```
// Warm up the JIT — first 100 iterations compile to
// Tier 0
// Iterations 101+ use Tier 1 (PGO-optimised)
// compilation
for (int i = 0; i < 200; i++)
await ProcessOrderAsync(GetSampleOrder());
```

}

// 3. NativeAOT for startup-critical workloads (Lambda, CLI
// tools)


```
- 281 -
```


<a id='p282'></a>
<!-- Página 282 -->

```
C# 2026: Enterprise Mastery


```

// Publish with: dotnet publish -r linux-x64
// -p:PublishAot=true
// Tradeoffs: faster cold start, no dynamic code
// generation, larger binary

// 4. ReadyToRun (R2R): pre-compiled managed code for
// faster startup
// Publish with: dotnet publish -p:PublishReadyToRun=true
// Better startup than JIT, worse peak throughput than PGO
// after warmup




GC: Server GC Tuning for High-Throughput Services

// Reference/GcTuning.cs
// runtimeconfig.json for server GC tuning
// {
// "configProperties": {
// "System.GC.Server": true, // One GC heap per CPU core
// "System.GC.HeapHardLimit": 2147483648, // 2GB hard
// memory limit
// "System.GC.HighMemoryPercent": 90, // Trigger GC at 90%
// of HeapHardLimit
// "System.GC.ConserveMemory": 0 // 0=off, 1-9=increasingly
// aggressive
// }
// }

// Monitoring GC in production
public static class GcMetricsReporter
{
```
public static void LogGcStats(ILogger logger)
{
var info = GC.GetGCMemoryInfo();
logger.LogInformation(
"GC: Gen0={Gen0} Gen1={Gen1} Gen2={Gen2} " +
"HeapSizeBytes={Heap:N0}
```

FragmentedBytes={Frag:N0} " +
```
"PauseDuration={Pause}ms",
GC.CollectionCount(0),
GC.CollectionCount(1),
GC.CollectionCount(2),

- 282 -
```


<a id='p283'></a>
<!-- Página 283 -->

```
C# 2026: Enterprise Mastery


info.HeapSizeBytes,
info.FragmentedBytes,

```

info.PauseDurations.LastOrDefault().TotalMilliseconds);
```
}
```

}

// Suppress GC during a critical section (use with extreme
// caution)
public static void ProcessCriticalBatch(Span<Order> orders)
{
```
// Prevent GC from interrupting this batch — guarantees
// low latency
// Only use for very short operations (<10ms); GC debt
// accrues
GC.TryStartNoGCRegion(16 * 1024 * 1024); // 16MB budget
try
{
foreach (ref var order in orders)
ProcessOrder(ref order);
}
finally
{
GC.EndNoGCRegion();
}
```

}




Thread Pool and Task Scheduler Internals

// Reference/ThreadPoolInternals.cs
// The .NET thread pool uses a work-stealing algorithm:
// Each CPU core has its own queue; idle threads steal from
// busy ones.
// This gives excellent locality and minimal contention.

// Monitor thread pool saturation — a leading indicator of
// performance problems
public class ThreadPoolMonitor : BackgroundService
{
```
protected override async Task
```

ExecuteAsync(CancellationToken ct)

```
- 283 -
```


<a id='p284'></a>
<!-- Página 284 -->

```
C# 2026: Enterprise Mastery


{
while (!ct.IsCancellationRequested)
{
ThreadPool.GetAvailableThreads(out int
```

availWorker, out int availIO);
```
ThreadPool.GetMaxThreads(out int maxWorker, out
```

int maxIO);
```
ThreadPool.GetMinThreads(out int minWorker, out
```

int minIO);

```
var workerUtil = (maxWorker - availWorker) *
```

100.0 / maxWorker;
```
var ioUtil = (maxIO - availIO) * 100.0 / maxIO;

if (workerUtil > 80)
_logger.LogWarning(
"Thread pool worker utilisation:
```

{Pct:F0}% ({Used}/{Max})",
```
workerUtil, maxWorker - availWorker,
```

maxWorker);



_metrics.RecordThreadPoolUtilisation(workerUtil, ioUtil);
```
await Task.Delay(TimeSpan.FromSeconds(10), ct);
}
}
```

}

// Avoid thread pool starvation:
// - Never block a thread pool thread synchronously (no
// .Result, no Thread.Sleep)
// - Limit unbounded parallelism (use SemaphoreSlim or
// Parallel.ForEachAsync)
// - Prefer async I/O over synchronous I/O in all hot paths
// - Consider increasing min threads for burst workloads:
ThreadPool.SetMinThreads(workerThreads: 100,
completionPortThreads: 100);
// But: more threads = more context switching overhead;
// profile first




```
- 284 -
```


<a id='p285'></a>
<!-- Página 285 -->

```
C# 2026: Enterprise Mastery


```

Interoperability: P/Invoke and Native Libraries

// Reference/PInvoke.cs
// Modern P/Invoke with LibraryImport (source-generated,
// AOT-compatible)
// Replaces DllImport for .NET 7+

[LibraryImport("libsodium", EntryPoint =
"crypto_secretbox_easy")]
[UnmanagedCallConv(CallConvs = [typeof(CallConvCdecl)])]
private static partial int CryptoSecretboxEasy(
```
Span<byte> ciphertext,
ReadOnlySpan<byte> message,
long messageLen,
ReadOnlySpan<byte> nonce,
ReadOnlySpan<byte> key);

```

// Safer wrapper with proper error handling
public static byte[] Encrypt(ReadOnlySpan<byte> message,
ReadOnlySpan<byte> key)
{
```
Span<byte> nonce = stackalloc byte[24];
RandomNumberGenerator.Fill(nonce);

var ciphertext = new byte[message.Length + 16 +
```

nonce.Length];
```
nonce.CopyTo(ciphertext);

int result = CryptoSecretboxEasy(
ciphertext.AsSpan(nonce.Length),
message, message.Length, nonce, key);

if (result != 0) throw new
```

CryptographicException("Encryption failed");
```
return ciphertext;
```

}

// For high-performance interop: use unsafe code + fixed to
// avoid marshalling
public static unsafe void FastMemCopy(
```
ReadOnlySpan<byte> source, Span<byte> destination)
```

{
```
fixed (byte* src = source)

- 285 -
```


<a id='p286'></a>
<!-- Página 286 -->

```
C# 2026: Enterprise Mastery


fixed (byte* dst = destination)
{
Buffer.MemoryCopy(src, dst, destination.Length,
```

source.Length);
```
}
```

}




```
- 286 -
```


<a id='p287'></a>
<!-- Página 287 -->

```
C# 2026: Enterprise Mastery



```

Building for Production: Deployment Checklist
Before deploying a new .NET 10 service to production, verify each item in
this checklist. Discovered issues cost ten times less before deployment
than after.

Container & Runtime
• Docker image uses mcr.microsoft.com/dotnet/aspnet (not SDK) as
base image
• Container runs as non-root user
• Health check endpoints are defined and return correct status codes
• Environment-specific configuration is sourced from environment
variables or secrets
• .NET runtime is set to invariant mode if culture-specific behaviour is
not needed (DOTNET_SYSTEM_GLOBALIZATION_INVARIANT=1 saves
~1MB memory)
• Container has CPU and memory limits set (not just requests)

Observability
• OpenTelemetry configured with traces, metrics, and structured logs
• Trace sampling rate set appropriately (100% in staging, sampled in
prod)
• Custom metrics defined for key business operations
• Alerts configured for: error rate, P95 latency, memory usage, GC
pressure
• Log level set to Information in production (not Debug)
• Correlation IDs propagated across service boundaries

Performance
• Response compression enabled for text-based endpoints
• Connection pooling configured for all external dependencies
• EF Core lazy loading disabled in production (can cause N+1 silently)
• LINQ queries checked with EF Core logging at Debug level before
go-live
```
- 287 -
```


<a id='p288'></a>
<!-- Página 288 -->

```
C# 2026: Enterprise Mastery


```

• Load test run against staging with realistic concurrency profile
• Baseline benchmark recorded for future regression detection

Security
• Swagger/OpenAPI UI disabled in production
• Developer exception page disabled in production
• All endpoints have explicit authorisation policies
• Rate limiting configured for public-facing endpoints
• Dependency vulnerability scan passed (dotnet list package --
vulnerable)
• Container image scanned for OS-level CVEs




```
- 288 -
```


<a id='p289'></a>
<!-- Página 289 -->

```
C# 2026: Enterprise Mastery



```

Deep Dive: Event Sourcing Fundamentals
Event sourcing stores the history of state changes as an immutable
sequence of events, rather than storing current state. The current state is
derived by replaying events. This gives you a complete audit trail, the
ability to replay history, and natural support for event-driven
architectures.


// Supplement/EventSourcing.cs
// Event store interface
public interface IEventStore
{
```
Task AppendAsync(string streamId,
```

IEnumerable<IDomainEvent> events,
```
long expectedVersion, CancellationToken ct =
```

default);
```
IAsyncEnumerable<IDomainEvent> ReadAsync(string
```

streamId,
```
long fromVersion = 0, CancellationToken ct =
```

default);
}

// Event-sourced aggregate
public abstract class EventSourcedAggregate
{
```
private readonly List<IDomainEvent> _uncommittedEvents
```

= [];
```
public long Version { get; private set; } = -1;

public IReadOnlyList<IDomainEvent> UncommittedEvents =>
```

_uncommittedEvents;

```
protected void Apply(IDomainEvent @event)
{
When(@event); // Update state
_uncommittedEvents.Add(@event);
Version++;
}

public void Rehydrate(IEnumerable<IDomainEvent> events)
{
foreach (var @event in events)

- 289 -
```


<a id='p290'></a>
<!-- Página 290 -->

```
C# 2026: Enterprise Mastery


{
// Replay — no uncommitted tracking
When(@event);
Version++;
}
}

public void ClearUncommittedEvents() =>
```

_uncommittedEvents.Clear();

```
protected abstract void When(IDomainEvent @event);
```

}

// Event-sourced Order aggregate
public class OrderAggregate : EventSourcedAggregate
{
```
public Guid Id { get; private set; }
public OrderStatus Status { get; private set; }
public decimal Total { get; private set; }

public static OrderAggregate Place(Guid customerId,
```

decimal amount)
```
{
var order = new OrderAggregate();
order.Apply(new OrderPlaced(Guid.NewGuid(),
```

customerId, amount,
```
DateTimeOffset.UtcNow));
return order;
}

public void Ship(string trackingNumber)
{
if (Status != OrderStatus.Confirmed)
throw new DomainException("Can only ship
```

confirmed orders");
```
Apply(new OrderShipped(Id, trackingNumber,
```

DateTimeOffset.UtcNow));
```
}

protected override void When(IDomainEvent @event)
{
switch (@event)
{
case OrderPlaced e:

- 290 -
```


<a id='p291'></a>
<!-- Página 291 -->

```
C# 2026: Enterprise Mastery


Id = e.OrderId;
Status = OrderStatus.Pending;
Total = e.Amount;
break;
case OrderConfirmed:
Status = OrderStatus.Confirmed;
break;
case OrderShipped:
Status = OrderStatus.Shipped;
break;
case OrderCancelled:
Status = OrderStatus.Cancelled;
break;
}
}
```

}

// Repository for event-sourced aggregates
public class EventSourcedOrderRepository
{
```
private readonly IEventStore _store;

public async Task SaveAsync(OrderAggregate order,
```

CancellationToken ct)
```
{
var streamId = $"order-{order.Id}";
await _store.AppendAsync(streamId,
```

order.UncommittedEvents,
```
order.Version - order.UncommittedEvents.Count,
```

ct);
```
order.ClearUncommittedEvents();
}

public async Task<OrderAggregate?> LoadAsync(Guid id,
```

CancellationToken ct)
```
{
var streamId = $"order-{id}";
var events = new List<IDomainEvent>();
await foreach (var @event in
```

_store.ReadAsync(streamId, ct: ct))
```
events.Add(@event);

if (events.Count == 0) return null;


- 291 -
```


<a id='p292'></a>
<!-- Página 292 -->

```
C# 2026: Enterprise Mastery


var order = new OrderAggregate();
order.Rehydrate(events);
return order;
}
```

}




Read Model Projections for Event Sourcing
Event sourcing stores everything you need to rebuild any read model.
Projections subscribe to the event stream and maintain denormalised
read models optimised for specific queries.


// Supplement/Projections.cs
// Projection: maintain a real-time order summary read
// model
public class OrderSummaryProjection :
```
INotificationHandler<OrderPlaced>,
INotificationHandler<OrderConfirmed>,
INotificationHandler<OrderShipped>,
INotificationHandler<OrderCancelled>
```

{
```
private readonly IReadDbContext _read;

public async Task Handle(OrderPlaced e,
```

CancellationToken ct)
```
{
_read.OrderSummaries.Add(new OrderSummaryReadModel
{
Id = e.OrderId,
CustomerId = e.CustomerId,
Status = "Pending",
Amount = e.Amount,
PlacedAt = e.OccurredAt
});
await _read.SaveChangesAsync(ct);
}

public async Task Handle(OrderShipped e,
```

CancellationToken ct)
```
{


- 292 -
```


<a id='p293'></a>
<!-- Página 293 -->

```
C# 2026: Enterprise Mastery


var summary = await
```

_read.OrderSummaries.FindAsync(e.OrderId, ct);
```
if (summary is not null)
{
summary.Status = "Shipped";
summary.TrackingNumber = e.TrackingNumber;
summary.ShippedAt = e.OccurredAt;
await _read.SaveChangesAsync(ct);
}
}
// ... other handlers
```

}




```
- 293 -
```


<a id='p294'></a>
<!-- Página 294 -->

```
C# 2026: Enterprise Mastery



```

Ten Habits That Separate Good from Great C#
Engineers
1. Profile Before Optimising

Every performance problem starts with a measurement. Run
BenchmarkDotNet, attach a profiler (dotnet-trace, PerfView, Rider's
profiler), or add OpenTelemetry metrics. Intuition about what is slow is
wrong far more often than it is right. The code you optimise without
profiling is almost never the bottleneck.

2. Read the Source Code

The .NET runtime, ASP.NET Core, Entity Framework Core, and every
major library used in enterprise .NET development is open source at
github.com/dotnet. When a behaviour surprises you — an exception, a
performance result, an edge case — read the source. It gives you
understanding that no documentation can.

3. Design for Testability First

If a class is hard to test, it is hard to change. Write the test before the
implementation. Design classes so their dependencies can be injected.
Keep side effects at the edges of the system. The test suite is the second
most important documentation in a codebase, after the domain model.

4. Understand Your Allocations

In .NET, allocation is not free. Every object on the heap is a future GC
event. In high-throughput systems, allocation pressure is often the
limiting factor, not CPU. Use the memory allocation columns in
BenchmarkDotNet and dotMemory snapshots to understand what your
hot paths actually allocate.

5. Make Illegal States Unrepresentable

Use the type system to prevent invalid states at compile time. A
non-nullable reference type is better than a null check. An enum is better
than a string for a bounded set of values. A value object is better than a

```
- 294 -
```


<a id='p295'></a>
<!-- Página 295 -->

```
C# 2026: Enterprise Mastery


```

primitive for a domain concept with invariants. The goal is code where
the bug cannot be written, not code where the bug is caught at runtime.

6. Treat Configuration as Code

Configuration that can be wrong is a bug waiting to happen. Validate
configuration at startup (ValidateOnStart in the options framework). Use
strongly-typed options classes. Document every configuration value with
its type, valid range, default, and effect. Prefer convention over
configuration — sensible defaults reduce mistakes.

7. Log What Matters, Not What is Easy

Every log line has a cost: storage, ingestion, and human attention. Log
decisions, state transitions, and errors with structured context. Do not log
entry and exit of every method. Use Debug level for developer diagnostics,
Information for business events, Warning for expected failures, Error for
unexpected failures.

8. Automate the Boring Parts

Code formatting, import organisation, naming conventions, and
architectural rules should be enforced automatically. Use .editorconfig,
Roslyn analysers (SonarAnalyzer, StyleCop,
Microsoft.CodeAnalysis.NetAnalyzers), and architecture tests in CI. Save
code review capacity for the things that actually need human judgment.

9. Version Your APIs

Any API that external clients depend on will need to change. Build
versioning in from the start. URL versioning (/v1/, /v2/) is simple and
discoverable. Deprecate old versions with clear timelines and helpful
error messages. Never remove a version without notifying every client.

10. Write Code for the Next Engineer

The most read code is code written six months ago by someone who no
longer remembers the context. Write names that explain intent, not
implementation. Write comments that explain why, not what. Leave the


```
- 295 -
```


<a id='p296'></a>
<!-- Página 296 -->

```
C# 2026: Enterprise Mastery


```

codebase better than you found it — every PR is an opportunity to
improve a name, remove a TODO, or add a missing test.




```
- 296 -
```


<a id='p297'></a>
<!-- Página 297 -->

```
C# 2026: Enterprise Mastery



```

Glossary of Key Terms
Aggregate Root: An entity that controls access to a cluster of related domain
objects and enforces invariants across them.

CQRS: Command Query Responsibility Segregation: separating read and write
models into distinct code paths.

Domain Event: A record of something significant that happened in the domain,
expressed in past tense.

Event Sourcing: Storing state changes as an immutable sequence of events
rather than current state.

Idempotent: An operation that produces the same result regardless of how
many times it is applied.

IAsyncEnumerable: A .NET interface for async streaming of sequences without
materialising all elements.

Mediator: A pattern where components communicate through a central
coordinator rather than directly.

Outbox Pattern: Publishing domain events reliably by saving them in the same
database transaction as business data.

PGO: Profile-Guided Optimisation: JIT compiler optimisations based on observed
runtime behaviour.

RAG: Retrieval-Augmented Generation: grounding AI responses in specific
document context.

Resilience Pipeline: A composable set of fault-handling strategies (retry, circuit
breaker, timeout) for a specific operation.

Saga: A pattern for coordinating a distributed transaction through a sequence of
local transactions and compensating actions.

Span<T>: A ref struct that provides a view over contiguous memory (an array, a
stack buffer, or native memory) without copying or allocating a heap object.

Strangler Fig: A migration pattern that incrementally replaces a legacy system
by routing requests to a new implementation alongside the old one.

ValueTask: A struct-based alternative to Task that avoids heap allocation when
a result is available synchronously.
```
- 297 -
```


<a id='p298'></a>
<!-- Página 298 -->

```
C# 2026: Enterprise Mastery


```

Zero-Trust: Security architecture that authenticates and authorises every
request regardless of network origin.




```
- 298 -
```


<a id='p299'></a>
<!-- Página 299 -->

```
C# 2026: Enterprise Mastery




```

- 299 -

<a id='p300'></a>
<!-- Página 300 -->

```
C# 2026: Enterprise Mastery



About the Author
```

Victor Mihailov is a software architect and engineer focused on
high-throughput distributed systems. His work spans enterprise-grade
APIs, cloud-native architectures, and performance-critical .NET
applications. He writes, speaks, and builds — and believes that clean code
is not an aesthetic preference but a practical advantage that compounds
over the life of a system.



```
Companion code repository
github.com/MrMeHighLove/CSharp2026-Enterprise-Mastery




- 300 -
```