---
tags: [code-smells]
date_created: 2026-05-20
status: seed
---

# Switch Statements

 
### Signs and Symptoms
 You have a complex `switch` operator or sequence of `if` statements. ![image](#) 
### Reasons for the Problem
 Relatively rare use of `switch` and `case` operators is one of the hallmarks of object-oriented code. Often code for a single `switch` can be scattered in different places in the program. When a new condition is added, you have to find all the `switch` code and modify it. As a rule of thumb, when you see `switch` you should think of polymorphism. 
### Treatment
 - To isolate `switch` and put it in the right class, you may need [Extract Method](../Extract%20Method.md) and then [Move Method](../Move%20Method.md) . - If a `switch` is based on type code, such as when the program’s runtime mode is switched, use [Replace Type Code with Subclasses](../Replace%20Type%20Code%20With%20Subclasses.md) or [Replace Type Code with State/Strategy](../Replace%20Type%20Code%20With%20State%20Strategy.md) . - After specifying the inheritance structure, use [Replace Conditional with Polymorphism](../Replace%20Conditional%20With%20Polymorphism.md) . - If there aren’t too many conditions in the operator and they all call same method with different parameters, polymorphism will be superfluous. If this case, you can break that method into multiple smaller methods with [Replace Parameter with Explicit Methods](../Replace%20Parameter%20With%20Explicit%20Methods.md) and change the `switch` accordingly. - If one of the conditional options is `null` , use [Introduce Null Object](../Introduce%20Null%20Object.md) . 
### Payoff
 - Improved code organization. ![image](#) 
### When to Ignore
 - When a `switch` operator performs simple actions, there’s no reason to make code changes. - Often `switch` operators are used by factory design patterns ( [Factory Method](../Design%20Patterns/Factory%20Method.md) or [Abstract Factory](../Design%20Patterns/Abstract%20Factory.md) ) to select a created class. 

## Related

- [[Replace Type Code With Subclasses]]
- [[Replace Type Code With State Strategy]]
- [[Replace Conditional With Polymorphism]]
- [[Extract Method]]
- [[Replace Parameter With Explicit Methods]]
- [[Primitive Obsession]]
- [[Oo Abusers]]

