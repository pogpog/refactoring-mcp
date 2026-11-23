---
tags: [code-smells]
date_created: 2026-05-20
status: seed
---

# Dead Code

 
### Signs and Symptoms
 A variable, parameter, field, method or class is no longer used (usually because it’s obsolete). ![image](#) 
### Reasons for the Problem
 When requirements for the software have changed or corrections have been made, nobody had time to clean up the old code. Such code could also be found in complex conditionals, when one of the branches becomes unreachable (due to error or other circumstances). 
### Treatment
 The quickest way to find dead code is to use a good [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment) . - Delete unused code and unneeded files. - In the case of an unnecessary class, [Inline Class](../Inline%20Class.md) or [Collapse Hierarchy](../Collapse%20Hierarchy.md) can be applied if a subclass or superclass is used. - To remove unneeded parameters, use [Remove Parameter](../Remove%20Parameter.md) . ![image](#) 
### Payoff
 - Reduced code size. - Simpler support. 

## Related

- [[Speculative Generality]]
- [[Lazy Class]]
- [[Inline Class]]
- [[Collapse Hierarchy]]
- [[Dispensables]]

