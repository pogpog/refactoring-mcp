---
tags: [code-smells]
date_created: 2026-05-20
status: seed
---

# Message Chains

 
### Signs and Symptoms
 In code you see a series of calls resembling `$a->b()->c()->d()` ![image](#) 
### Reasons for the Problem
 A message chain occurs when a client requests another object, that object requests yet another one, and so on. These chains mean that the client is dependent on navigation along the class structure. Any changes in these relationships require modifying the client. 
### Treatment
 - To delete a message chain, use [Hide Delegate](../Hide%20Delegate.md) . - Sometimes it’s better to think of why the end object is being used. Perhaps it would make sense to use [Extract Method](../Extract%20Method.md) for this functionality and move it to the beginning of the chain, by using [Move Method](../Move%20Method.md) . ![image](#) 
### Payoff
 - Reduces dependencies between classes of a chain. - Reduces the amount of bloated code. ![image](#) 
### When to Ignore
 - Overly aggressive delegate hiding can cause code in which it’s hard to see where the functionality is actually occurring. Which is another way of saying, avoid the [Middle Man](Middle%20Man.md) smell as well. 

## Related

- [[Hide Delegate]]
- [[Extract Method]]
- [[Middle Man]]
- [[Inappropriate Intimacy]]
- [[Feature Envy]]
- [[Couplers]]

