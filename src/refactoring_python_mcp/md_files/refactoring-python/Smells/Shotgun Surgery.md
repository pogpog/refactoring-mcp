---
tags: [code-smells]
date_created: 2026-05-20
status: seed
---

# Shotgun Surgery

 > Shotgun SurgeryresemblesDivergent Changebut is actually the opposite smell.Divergent Changeis when many changes are made to a single class.Shotgun Surgeryrefers to when a single change is made to multiple classes simultaneously. 
### Signs and Symptoms
 Making any modifications requires that you make many small changes to many different classes. ![image](#) 
### Reasons for the Problem
 A single responsibility has been split up among a large number of classes. This can happen after overzealous application of [Divergent Change](Divergent%20Change.md) . ![image](#) 
### Treatment
 - Use [Move Method](../Move%20Method.md) and [Move Field](../Move%20Field.md) to move existing class behaviors into a single class. If there’s no class appropriate for this, create a new one. - If moving code to the same class leaves the original classes almost empty, try to get rid of these now-redundant classes via [Inline Class](../Inline%20Class.md) . ![image](#) 
### Payoff
 - Better organization. - Less code duplication. - Easier maintenance. 

## Related

- [[Move Method]]
- [[Move Field]]
- [[Inline Class]]
- [[Divergent Change]]
- [[Parallel Inheritance Hierarchies]]
- [[Change Preventers]]

