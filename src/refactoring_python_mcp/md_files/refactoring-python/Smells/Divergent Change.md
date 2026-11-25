---
tags: [code-smells]
date_created: 2026-05-20
status: seed
---
# Divergent Change

 > Divergent ChangeresemblesShotgun Surgerybut is actually the opposite smell.Divergent Changeis when many changes are made to a single class.Shotgun Surgeryrefers to when a single change is made to multiple classes simultaneously. 
### Signs and Symptoms
 You find yourself having to change many unrelated methods when you make changes to a class. For example, when adding a new product type you have to change the methods for finding, displaying, and ordering products. ![image](#) 
### Reasons for the Problem
 Often these divergent modifications are due to poor program structure or "copypasta programming”. 
### Treatment
 - Split up the behavior of the class via [Extract Class](../Extract%20Class.md) . - If different classes have the same behavior, you may want to combine the classes through inheritance ( [Extract Superclass](../Extract%20Superclass.md) and [Extract Subclass](../Extract%20Subclass.md) ). ![image](#) 
### Payoff
 - Improves code organization. - Reduces code duplication. - Simplifies support. 

## Related

- [[Extract Class]]
- [[Shotgun Surgery]]
- [[Parallel Inheritance Hierarchies]]
- [[Change Preventers]]

