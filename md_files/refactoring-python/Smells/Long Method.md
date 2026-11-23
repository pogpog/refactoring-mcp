---
tags: [code-smells]
date_created: 2026-05-20
status: seed
---

# Long Method

 
### Signs and Symptoms
 A method contains too many lines of code. Generally, any method longer than ten lines should make you start asking questions. ![image](#) 
### Reasons for the Problem
 Like the Hotel California, something is always being added to a method but nothing is ever taken out. Since it’s easier to write code than to read it, this “smell” remains unnoticed until the method turns into an ugly, oversized beast. Mentally, it’s often harder to create a new method than to add to an existing one: “But it’s just two lines, there’s no use in creating a whole method just for that...” Which means that another line is added and then yet another, giving birth to a tangle of spaghetti code. 
### Treatment
 As a rule of thumb, if you feel the need to comment on something inside a method, you should take this code and put it in a new method. Even a single line can and should be split off into a separate method, if it requires explanations. And if the method has a descriptive name, nobody will need to look at the code to see what it does. ![image](#) - To reduce the length of a method body, use [Extract Method](../Extract%20Method.md) . - If local variables and parameters interfere with extracting a method, use [Replace Temp with Query](../Replace%20Temp%20With%20Query.md) , [Introduce Parameter Object](../Introduce%20Parameter%20Object.md) or [Preserve Whole Object](../Preserve%20Whole%20Object.md) . - If none of the previous recipes help, try moving the entire method to a separate object via [Replace Method with Method Object](../Replace%20Method%20With%20Method%20Object.md) . - Conditional operators and loops are a good clue that code can be moved to a separate method. For conditionals, use [Decompose Conditional](../Decompose%20Conditional.md) . If loops are in the way, try [Extract Method](../Extract%20Method.md) . 
### Payoff
 - Among all types of object-oriented code, classes with short methods live longest. The longer a method or function is, the harder it becomes to understand and maintain it. - In addition, long methods offer the perfect hiding place for unwanted duplicate code. ![image](#) 
### Performance
 Does an increase in the number of methods hurt performance, as many people claim? In almost all cases the impact is so negligible that it’s not even worth worrying about. Plus, now that you have clear and understandable code, you’re more likely to find truly effective methods for restructuring code and getting real performance gains if the need ever arises. 

## Related

- [[Extract Method]]
- [[Replace Temp With Query]]
- [[Introduce Parameter Object]]
- [[Preserve Whole Object]]
- [[Replace Method With Method Object]]
- [[Decompose Conditional]]
- [[Large Class]]
- [[Bloaters]]

