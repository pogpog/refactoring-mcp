---
tags: []
date_created: 2026-05-20
status: seed
---

# Remove Setting Method

 
### Problem
 The value of a field should be set only when it’s created, and not change at any time after that. 
### Solution
 So remove methods that set the field’s value. Before ![Remove Setting Method - Before](#) After ![Remove Setting Method - After](#) 
### Why Refactor
 You want to prevent any changes to the value of a field. 
### How to Refactor
 2. The value of a field should be changeable only in the constructor. If the constructor doesn’t contain a parameter for setting the value, add one. 4. Find all setter calls. - If a setter call is located right after a call for the constructor of the current class, move its argument to the constructor call and remove the setter. - Replace setter calls in the constructor with direct access to the field. 6. Delete the setter. 

## Related

- [[Encapsulate Field]]
- [[Data Class]]
- [[Simplifying Method Calls]]

