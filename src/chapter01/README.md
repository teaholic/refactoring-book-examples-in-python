# The theatrical company loyalty program

Here below, some quotes from [Refactoring](https://martinfowler.com/books/refactoring.html), Chapter 1 (2nd edition) that I find useful to practice refactoring with the code in `src/chapter01/main.py`.

> Frankly, it is not worth the effort to do all the refactoring that I’m going to show you on the small program I will be using. But **if the code I’m showing you is part of a larger system, then the refactoring becomes important**. Just look at my example and imagine it in the context of a much larger system.

> Image a company of theatrical players who go out to various events performing plays. Typically, a customer will request a few plays and the company charges them based on the size of the audience and the kind of play they perform. There are currently two kinds of plays that the company performs: tragedies and comedies. As well as providing a bill for the performance, the company gives its customers “volume credits” which they can use for discounts on future performances—think of it as a customer loyalty mechanism.

## How could this functionality change?

> First, they want a **statement printed in HTML**. Consider what impact this change would have. I’m faced with adding conditional statements around every statement that adds a string to the result. That will add a host of complexity to the function. Faced with that, most people prefer to copy the method and change it to emit HTML. Making a copy may not seem too onerous a task, but it sets up all sorts of problems for the future. Any changes to the charging logic would force me to update both methods—and to ensure they are updated consistently.

> The players are looking to perform **more kinds of plays**: they hope to add history, pastoral, pastoral-comical, historical-pastoral, tragical-historical, tragical-comical-historical-pastoral, scene individable, and poem unlimited to their repertoire. They **haven’t exactly decided yet** what they want to do and when. This change will affect both the way their plays are charged for and the way volume credits are calculated.

## Why refactoring?

> Let me stress that **it’s these changes that drive the need** to perform refactoring.

> As is often the case with refactoring, the early stages were mostly driven by trying to **understand** what was going on. 

## How to refactor?

1. Add tests
> **I need to ensure I have a solid set of tests** for that section of code. The tests are essential because even though I will follow refactorings structured to avoid most of the opportunities for introducing bugs, I’m still human and still make mistakes. The larger a program, the more likely it is that my changes will cause something to break inadvertently—in the digital age, frailty’s name is software.

> A common sequence is: Read the code, gain some insight, and **use refactoring to move that insight from your head back into the code**. The clearer code then makes it easier to understand it, leading to deeper insights and a beneficial positive feedback loop. There are still some improvements I could make, but I feel I’ve done enough to pass my test of leaving the code significantly better than how I found it.
