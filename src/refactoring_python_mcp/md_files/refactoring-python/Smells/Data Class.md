---
tags: [code-smells]
date_created: 2026-05-20
status: seed
---

# Data Class

 
### Signs and Symptoms
 A data class refers to a class that contains only fields and crude methods for accessing them (getters and setters). These are simply containers for data used by other classes. These classes don’t contain any additional functionality and can’t independently operate on the data that they own. ![image](#) 
### Reasons for the Problem
 It’s a normal thing when a newly created class contains only a few public fields (and maybe even a handful of getters/setters). But the true power of objects is that they can contain behavior types or operations on their data. 
### Treatment
 - If a class contains public fields, use [Encapsulate Field](../Encapsulate%20Field.md) to hide them from direct access and require that access be performed via getters and setters only. - Use [Encapsulate Collection](../Encapsulate%20Collection.md) for data stored in collections (such as arrays). - Review the client code that uses the class. In it, you may find functionality that would be better located in the data class itself. If this is the case, use [Move Method](../Move%20Method.md) and [Extract Method](../Extract%20Method.md) to migrate this functionality to the data class. - After the class has been filled with well thought-out methods, you may want to get rid of old methods for data access that give overly broad access to the class data. For this, [Remove Setting Method](../Remove%20Setting%20Method.md) and [Hide Method](../Hide%20Method.md) may be helpful. ![image](#) 
### Payoff
 - Improves understanding and organization of code. Operations on particular data are now gathered in a single place, instead of haphazardly throughout the code. - Helps you to spot duplication of client code. 

## Related

- [[Encapsulate Field]]
- [[Encapsulate Collection]]
- [[Remove Setting Method]]
- [[Hide Method]]
- [[Extract Class]]
- [[Move Method]]
- [[Feature Envy]]
- [[Dispensables]]

