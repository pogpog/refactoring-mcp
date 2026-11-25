---
tags: [refactoring]
date_created: 2026-05-20
status: seed
---

# Composing Methods

 Much of refactoring is devoted to correctly composing methods. In most cases, excessively long methods are the root of all evil. The vagaries of code inside these methods conceal the execution logic and make the method extremely hard to understand—and even harder to change. The refactoring techniques in this group streamline methods, remove code duplication, and pave the way for future improvements. [Extract Method](../../Extract%20Method.md) **Problem:** You have a code fragment that can be grouped together. **Solution:** Move this code to a separate new method (or function) and replace the old code with a call to the method. [Inline Method](../../Inline%20Method.md) **Problem:** When a method body is more obvious than the method itself, use this technique. **Solution:** Replace calls to the method with the method’s content and delete the method itself. [Extract Variable](../../Extract%20Variable.md) **Problem:** You have an expression that’s hard to understand. **Solution:** Place the result of the expression or its parts in separate variables that are self-explanatory. [Inline Temp](../../Inline%20Temp.md) **Problem:** You have a temporary variable that’s assigned the result of a simple expression and nothing more. **Solution:** Replace the references to the variable with the expression itself. [Replace Temp with Query](../../Replace%20Temp%20With%20Query.md) **Problem:** You place the result of an expression in a local variable for later use in your code. **Solution:** Move the entire expression to a separate method and return the result from it. Query the method instead of using a variable. Incorporate the new method in other methods, if necessary. [Split Temporary Variable](../../Split%20Temporary%20Variable.md) **Problem:** You have a local variable that’s used to store various intermediate values inside a method (except for cycle variables). **Solution:** Use different variables for different values. Each variable should be responsible for only one particular thing. [Remove Assignments to Parameters](../../Remove%20Assignments%20To%20Parameters.md) **Problem:** Some value is assigned to a parameter inside method’s body. **Solution:** Use a local variable instead of a parameter. [Replace Method with Method Object](../../Replace%20Method%20With%20Method%20Object.md) **Problem:** You have a long method in which the local variables are so intertwined that you can’t apply *Extract Method* . **Solution:** Transform the method into a separate class so that the local variables become fields of the class. Then you can split the method into several methods within the same class. [Substitute Algorithm](../../Substitute%20Algorithm.md) **Problem:** So you want to replace an existing algorithm with a new one? **Solution:** Replace the body of the method that implements the algorithm with a new algorithm.

## Related

- [[Extract Method]]
- [[Inline Method]]
- [[Extract Variable]]
- [[Inline Temp]]
- [[Replace Temp With Query]]
- [[Split Temporary Variable]]
- [[Remove Assignments To Parameters]]
- [[Replace Method With Method Object]]
- [[Substitute Algorithm]]
- [[Moving Features Between Objects]]
- [[Refactoring/Techniques|Techniques Overview]]

