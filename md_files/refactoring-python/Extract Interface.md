---
tags: []
date_created: 2026-05-20
status: seed
---

# Extract Interface

 
### Problem
 Multiple clients are using the same part of a class interface. Another case: part of the interface in two classes is the same. 
### Solution
 Move this identical portion to its own interface. Before ![Extract Interface - Before](#) After ![Extract Interface - After](#) 
### Why Refactor
 2. Interfaces are very apropos when classes play special roles in different situations. Use [Extract Interface](#) to explicitly indicate which role. 4. Another convenient case arises when you need to describe the operations that a class performs on its server. If it’s planned to eventually allow use of servers of multiple types, all servers must implement the interface. 
### Good to Know
 There’s a certain resemblance between [Extract Superclass](Extract%20Superclass.md) and [Extract Interface](#) . Extracting an interface allows isolating only common interfaces, not common code. In other words, if classes contain [Duplicate Code](Smells/Duplicate%20Code.md) , extracting the interface won’t help you to deduplicate. All the same, this problem can be mitigated by applying [Extract Class](Extract%20Class.md) to move the behavior that contains the duplication to a separate component and delegating all the work to it. If the common behavior is large in size, you can always use [Extract Superclass](Extract%20Superclass.md) . This is even easier, of course, but remember that if you take this path you will get only one parent class. 
### How to Refactor
 2. Create an empty interface. 4. Declare common operations in the interface. 6. Declare the necessary classes as implementing the interface. 8. Change type declarations in the client code to use the new interface. 

## Related

- [[Extract Superclass]]
- [[Extract Subclass]]
- [[Alternative Classes With Different Interfaces]]
- [[Dealing With Generalization]]

