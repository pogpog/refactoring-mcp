---
tags: [code-smells]
date_created: 2026-05-20
status: seed
---

# Inappropriate Intimacy

 
### Signs and Symptoms
 One class uses the internal fields and methods of another class. ![image](#) 
### Reasons for the Problem
 Keep a close eye on classes that spend too much time together. Good classes should know as little about each other as possible. Such classes are easier to maintain and reuse. 
### Treatment
 - The simplest solution is to use [Move Method](../Move%20Method.md) and [Move Field](../Move%20Field.md) to move parts of one class to the class in which those parts are used. But this works only if the first class truly doesn’t need these parts. ![image](#) - Another solution is to use [Extract Class](../Extract%20Class.md) and [Hide Delegate](../Hide%20Delegate.md) on the class to make the code relations “official”. - If the classes are mutually interdependent, you should use [Change Bidirectional Association to Unidirectional](../Change%20Bidirectional%20Association%20To%20Unidirectional.md) . - If this “intimacy” is between a subclass and the superclass, consider [Replace Delegation with Inheritance](../Replace%20Delegation%20With%20Inheritance.md) . ![image](#) 
### Payoff
 - Improves code organization. - Simplifies support and code reuse. 

## Related

- [[Move Method]]
- [[Move Field]]
- [[Change Bidirectional Association To Unidirectional]]
- [[Extract Class]]
- [[Hide Delegate]]
- [[Replace Delegation With Inheritance]]
- [[Feature Envy]]
- [[Message Chains]]
- [[Middle Man]]
- [[Couplers]]

