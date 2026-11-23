---
tags: [code-smells]
date_created: 2026-05-20
status: seed
---

# Parallel Inheritance Hierarchies

 
### Signs and Symptoms
 Whenever you create a subclass for a class, you find yourself needing to create a subclass for another class. ![image](#) 
### Reasons for the Problem
 All was well as long as the hierarchy stayed small. But with new classes being added, making changes has become harder and harder. 
### Treatment
 - You may de-duplicate parallel class hierarchies in two steps. First, make instances of one hierarchy refer to instances of another hierarchy. Then, remove the hierarchy in the referred class, by using [Move Method](../Move%20Method.md) and [Move Field](../Move%20Field.md) . 
### Payoff
 - Reduces code duplication. - Can improve organization of code. ![image](#) 
### When to Ignore
 - Sometimes having parallel class hierarchies is just a way to avoid even bigger mess with program architecture. If you find that your attempts to de-duplicate hierarchies produce even uglier code, just step out, revert all of your changes and get used to that code. 

## Related

- [[Move Method]]
- [[Move Field]]
- [[Divergent Change]]
- [[Shotgun Surgery]]
- [[Change Preventers]]

