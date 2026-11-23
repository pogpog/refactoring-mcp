---
tags: [refactoring]
date_created: 2026-05-20
status: seed
---

# Simplifying Conditional Expressions

 Conditionals tend to get more and more complicated in their logic over time, and there are yet more techniques to combat this as well. [Decompose Conditional](../../Decompose%20Conditional.md) **Problem:** You have a complex conditional ( `if-then` / `else` or `switch` ). **Solution:** Decompose the complicated parts of the conditional into separate methods: the condition, `then` and `else` . [Consolidate Conditional Expression](../../Consolidate%20Conditional%20Expression.md) **Problem:** You have multiple conditionals that lead to the same result or action. **Solution:** Consolidate all these conditionals in a single expression. [Consolidate Duplicate Conditional Fragments](../../Consolidate%20Duplicate%20Conditional%20Fragments.md) **Problem:** Identical code can be found in all branches of a conditional. **Solution:** Move the code outside of the conditional. [Remove Control Flag](../../Remove%20Control%20Flag.md) **Problem:** You have a boolean variable that acts as a control flag for multiple boolean expressions. **Solution:** Instead of the variable, use `break` , `continue` and `return` . [Replace Nested Conditional with Guard Clauses](../../Replace%20Nested%20Conditional%20With%20Guard%20Clauses.md) **Problem:** You have a group of nested conditionals and it’s hard to determine the normal flow of code execution. **Solution:** Isolate all special checks and edge cases into separate clauses and place them before the main checks. Ideally, you should have a “flat” list of conditionals, one after the other. [Replace Conditional with Polymorphism](../../Replace%20Conditional%20With%20Polymorphism.md) **Problem:** You have a conditional that performs various actions depending on object type or properties. **Solution:** Create subclasses matching the branches of the conditional. In them, create a shared method and move code from the corresponding branch of the conditional to it. Then replace the conditional with the relevant method call. The result is that the proper implementation will be attained via polymorphism depending on the object class. [Introduce Null Object](../../Introduce%20Null%20Object.md) **Problem:** Since some methods return `null` instead of real objects, you have many checks for `null` in your code. **Solution:** Instead of `null` , return a null object that exhibits the default behavior. [Introduce Assertion](../../Introduce%20Assertion.md) **Problem:** For a portion of code to work correctly, certain conditions or values must be true. **Solution:** Replace these assumptions with specific assertion checks.

## Related

- [[Decompose Conditional]]
- [[Consolidate Conditional Expression]]
- [[Consolidate Duplicate Conditional Fragments]]
- [[Remove Control Flag]]
- [[Replace Nested Conditional With Guard Clauses]]
- [[Replace Conditional With Polymorphism]]
- [[Introduce Assertion]]
- [[Composing Methods]]
- [[Refactoring/Techniques|Techniques Overview]]

