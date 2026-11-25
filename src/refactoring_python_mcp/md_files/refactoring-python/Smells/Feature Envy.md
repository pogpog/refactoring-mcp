---
tags: [code-smells]
date_created: 2026-05-20
status: seed
---

# Feature Envy

 
### Signs and Symptoms
 A method accesses the data of another object more than its own data. ![image](#) 
### Reasons for the Problem
 This smell may occur after fields are moved to a data class. If this is the case, you may want to move the operations on data to this class as well. 
### Treatment
 As a basic rule, if things change at the same time, you should keep them in the same place. Usually data and functions that use this data are changed together (although exceptions are possible). - If a method clearly should be moved to another place, use [Move Method](../Move%20Method.md) . - If only part of a method accesses the data of another object, use [Extract Method](../Extract%20Method.md) to move the part in question. - If a method uses functions from several other classes, first determine which class contains most of the data used. Then place the method in this class along with the other data. Alternatively, use [Extract Method](../Extract%20Method.md) to split the method into several parts that can be placed in different places in different classes. ![image](#) 
### Payoff
 - Less code duplication (if the data handling code is put in a central place). - Better code organization (methods for handling data are next to the actual data). ![image](#) 
### When to Ignore
 - Sometimes behavior is purposefully kept separate from the class that holds the data. The usual advantage of this is the ability to dynamically change the behavior (see [Strategy](../Design%20Patterns/Strategy.md) , [Visitor](../Design%20Patterns/Visitor.md) and other patterns). 

## Related

- [[Move Method]]
- [[Move Field]]
- [[Extract Method]]
- [[Data Class]]
- [[Inappropriate Intimacy]]
- [[Message Chains]]
- [[Couplers]]

