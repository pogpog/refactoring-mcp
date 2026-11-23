---
tags: [code-smells]
date_created: 2026-05-20
status: seed
---

# Duplicate Code

 
### Signs and Symptoms
 Two code fragments look almost identical. ![image](#) 
### Reasons for the Problem
 Duplication usually occurs when multiple programmers are working on different parts of the same program at the same time. Since they’re working on different tasks, they may be unaware their colleague has already written similar code that could be repurposed for their own needs. There’s also more subtle duplication, when specific parts of code look different but actually perform the same job. This kind of duplication can be hard to find and fix. Sometimes duplication is purposeful. When rushing to meet deadlines and the existing code is “almost right” for the job, novice programmers may not be able to resist the temptation of copying and pasting the relevant code. And in some cases, the programmer is simply too lazy to de-clutter. 
### Treatment
 - If the same code is found in two or more methods in the same class: use [Extract Method](../Extract%20Method.md) and place calls for the new method in both places. ![image](#) - If the same code is found in two subclasses of the same level: - Use [Extract Method](../Extract%20Method.md) for both classes, followed by [Pull Up Field](../Pull%20Up%20Field.md) for the fields used in the method that you’re pulling up. - If the duplicate code is inside a constructor, use [Pull Up Constructor Body](../Pull%20Up%20Constructor%20Body.md) . - If the duplicate code is similar but not completely identical, use [Form Template Method](../Form%20Template%20Method.md) . - If two methods do the same thing but use different algorithms, select the best algorithm and apply [Substitute Algorithm](../Substitute%20Algorithm.md) . - If duplicate code is found in two different classes: - If the classes aren’t part of a hierarchy, use [Extract Superclass](../Extract%20Superclass.md) in order to create a single superclass for these classes that maintains all the previous functionality. - If it’s difficult or impossible to create a superclass, use [Extract Class](../Extract%20Class.md) in one class and use the new component in the other. - If a large number of conditional expressions are present and perform the same code (differing only in their conditions), merge these operators into a single condition using [Consolidate Conditional Expression](../Consolidate%20Conditional%20Expression.md) and use [Extract Method](../Extract%20Method.md) to place the condition in a separate method with an easy-to-understand name. - If the same code is performed in all branches of a conditional expression: place the identical code outside of the condition tree by using [Consolidate Duplicate Conditional Fragments](../Consolidate%20Duplicate%20Conditional%20Fragments.md) . 
### Payoff
 - Merging duplicate code simplifies the structure of your code and makes it shorter. - Simplification + shortness = code that’s easier to simplify and cheaper to support. ![image](#) 
### When to Ignore
 - In very rare cases, merging two identical fragments of code can make the code less intuitive and obvious. 

## Related

- [[Extract Method]]
- [[Extract Superclass]]
- [[Extract Class]]
- [[Form Template Method]]
- [[Substitute Algorithm]]
- [[Pull Up Constructor Body]]
- [[Consolidate Conditional Expression]]
- [[Consolidate Duplicate Conditional Fragments]]
- [[Alternative Classes With Different Interfaces]]
- [[Dispensables]]

