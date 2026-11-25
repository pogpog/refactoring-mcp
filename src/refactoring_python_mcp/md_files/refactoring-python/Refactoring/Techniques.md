---
tags: [refactoring]
date_created: 2026-05-20
status: seed
---

# Refactoring Techniques

 ![image](#) 
### Composing Methods
 Much of refactoring is devoted to correctly composing methods. In most cases, excessively long methods are the root of all evil. The vagaries of code inside these methods conceal the execution logic and make the method extremely hard to understand—and even harder to change. The refactoring techniques in this group streamline methods, remove code duplication, and pave the way for future improvements. - [Extract Method](../Extract%20Method.md) - [Inline Method](../Inline%20Method.md) - [Extract Variable](../Extract%20Variable.md) - [Inline Temp](../Inline%20Temp.md) - [Replace Temp with Query](../Replace%20Temp%20With%20Query.md) - [Split Temporary Variable](../Split%20Temporary%20Variable.md) - [Remove Assignments to Parameters](../Remove%20Assignments%20To%20Parameters.md) - [Replace Method with Method Object](../Replace%20Method%20With%20Method%20Object.md) - [Substitute Algorithm](../Substitute%20Algorithm.md) ![image](#) 
### Moving Features between Objects
 Even if you have distributed functionality among different classes in a less-than-perfect way, there is still hope. These refactoring techniques show how to safely move functionality between classes, create new classes, and hide implementation details from public access. - [Move Method](../Move%20Method.md) - [Move Field](../Move%20Field.md) - [Extract Class](../Extract%20Class.md) - [Inline Class](../Inline%20Class.md) - [Hide Delegate](../Hide%20Delegate.md) - [Remove Middle Man](../Remove%20Middle%20Man.md) - [Introduce Foreign Method](../Introduce%20Foreign%20Method.md) - [Introduce Local Extension](../Introduce%20Local%20Extension.md) ![image](#) 
### Organizing Data
 These refactoring techniques help with data handling, replacing primitives with rich class functionality. Another important result is untangling of class associations, which makes classes more portable and reusable. - [Change Value to Reference](../Change%20Value%20To%20Reference.md) - [Change Reference to Value](../Change%20Reference%20To%20Value.md) - [Duplicate Observed Data](../Duplicate%20Observed%20Data.md) - [Self Encapsulate Field](../Self%20Encapsulate%20Field.md) - [Replace Data Value with Object](../Replace%20Data%20Value%20With%20Object.md) - [Replace Array with Object](../Replace%20Array%20With%20Object.md) - [Change Unidirectional Association to Bidirectional](../Change%20Unidirectional%20Association%20To%20Bidirectional.md) - [Change Bidirectional Association to Unidirectional](../Change%20Bidirectional%20Association%20To%20Unidirectional.md) - [Encapsulate Field](../Encapsulate%20Field.md) - [Encapsulate Collection](../Encapsulate%20Collection.md) - [Replace Magic Number with Symbolic Constant](../Replace%20Magic%20Number%20With%20Symbolic%20Constant.md) - [Replace Type Code with Class](../Replace%20Type%20Code%20With%20Class.md) - [Replace Type Code with Subclasses](../Replace%20Type%20Code%20With%20Subclasses.md) - [Replace Type Code with State/Strategy](../Replace%20Type%20Code%20With%20State%20Strategy.md) - [Replace Subclass with Fields](../Replace%20Subclass%20With%20Fields.md) ![image](#) 
### Simplifying Conditional Expressions
 Conditionals tend to get more and more complicated in their logic over time, and there are yet more techniques to combat this as well. - [Consolidate Conditional Expression](../Consolidate%20Conditional%20Expression.md) - [Consolidate Duplicate Conditional Fragments](../Consolidate%20Duplicate%20Conditional%20Fragments.md) - [Decompose Conditional](../Decompose%20Conditional.md) - [Replace Conditional with Polymorphism](../Replace%20Conditional%20With%20Polymorphism.md) - [Remove Control Flag](../Remove%20Control%20Flag.md) - [Replace Nested Conditional with Guard Clauses](../Replace%20Nested%20Conditional%20With%20Guard%20Clauses.md) - [Introduce Null Object](../Introduce%20Null%20Object.md) - [Introduce Assertion](../Introduce%20Assertion.md) ![image](#) 
### Simplifying Method Calls
 These techniques make method calls simpler and easier to understand. This, in turn, simplifies the interfaces for interaction between classes. - [Add Parameter](../Add%20Parameter.md) - [Remove Parameter](../Remove%20Parameter.md) - [Rename Method](../Rename%20Method.md) - [Separate Query from Modifier](../Separate%20Query%20From%20Modifier.md) - [Parameterize Method](../Parameterize%20Method.md) - [Introduce Parameter Object](../Introduce%20Parameter%20Object.md) - [Preserve Whole Object](../Preserve%20Whole%20Object.md) - [Remove Setting Method](../Remove%20Setting%20Method.md) - [Replace Parameter with Explicit Methods](../Replace%20Parameter%20With%20Explicit%20Methods.md) - [Replace Parameter with Method Call](../Replace%20Parameter%20With%20Method%20Call.md) - [Hide Method](../Hide%20Method.md) - [Replace Constructor with Factory Method](../Replace%20Constructor%20With%20Factory%20Method.md) - [Replace Error Code with Exception](../Replace%20Error%20Code%20With%20Exception.md) - [Replace Exception with Test](../Replace%20Exception%20With%20Test.md) ![image](#) 
### Dealing with Generalization
 Abstraction has its own group of refactoring techniques, primarily associated with moving functionality along the class inheritance hierarchy, creating new classes and interfaces, and replacing inheritance with delegation and vice versa. - [Pull Up Field](../Pull%20Up%20Field.md) - [Pull Up Method](../Pull%20Up%20Method.md) - [Pull Up Constructor Body](../Pull%20Up%20Constructor%20Body.md) - [Push Down Field](../Push%20Down%20Field.md) - [Push Down Method](../Push%20Down%20Method.md) - [Extract Subclass](../Extract%20Subclass.md) - [Extract Superclass](../Extract%20Superclass.md) - [Extract Interface](../Extract%20Interface.md) - [Collapse Hierarchy](../Collapse%20Hierarchy.md) - [Form Template Method](../Form%20Template%20Method.md) - [Replace Inheritance with Delegation](../Replace%20Inheritance%20With%20Delegation.md) - [Replace Delegation with Inheritance](../Replace%20Delegation%20With%20Inheritance.md)

## Related

- [[Composing Methods]]
- [[Moving Features Between Objects]]
- [[Organizing Data]]
- [[Simplifying Conditional Expressions]]
- [[Simplifying Method Calls]]
- [[Dealing With Generalization]]
- [[Refactoring/Smells|Code Smells]]

