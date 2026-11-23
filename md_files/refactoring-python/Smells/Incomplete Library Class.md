---
tags: [code-smells]
date_created: 2026-05-20
status: seed
---

# Incomplete Library Class

 
### Signs and Symptoms
 Sooner or later, [libraries](https://en.wikipedia.org/wiki/Library_(computing)) stop meeting user needs. The only solution to the problem—changing the library—is often impossible since the library is read-only. ![image](#) 
### Reasons for the Problem
 The author of the library hasn’t provided the features you need or has refused to implement them. 
### Treatment
 - To introduce a few methods to a library class, use [Introduce Foreign Method](../Introduce%20Foreign%20Method.md) . - For big changes in a class library, use [Introduce Local Extension](../Introduce%20Local%20Extension.md) . 
### Payoff
 - Reduces code duplication (instead of creating your own library from scratch, you can still piggy-back off an existing one). ![image](#) 
### When to Ignore
 - Extending a library can generate additional work if the changes to the library involve changes in code. 

## Related

- [[Introduce Foreign Method]]
- [[Introduce Local Extension]]
- [[Couplers]]

