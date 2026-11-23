---
tags: [refactoring]
date_created: 2026-05-20
status: seed
---

# Code Smells

 — What? How can code "smell"?? 
 — Well it doesn't have a nose... but it definitely can stink! ![image](#) 
### Bloaters
 Bloaters are code, methods and classes that have increased to such gargantuan proportions that they are hard to work with. Usually these smells do not crop up right away, rather they accumulate over time as the program evolves (and especially when nobody makes an effort to eradicate them). - [Long Method](../Smells/Long%20Method.md) - [Large Class](../Smells/Large%20Class.md) - [Primitive Obsession](../Smells/Primitive%20Obsession.md) - [Long Parameter List](../Smells/Long%20Parameter%20List.md) - [Data Clumps](../Smells/Data%20Clumps.md) ![image](#) 
### Object-Orientation Abusers
 All these smells are incomplete or incorrect application of object-oriented programming principles. - [Alternative Classes with Different Interfaces](../Smells/Alternative%20Classes%20With%20Different%20Interfaces.md) - [Refused Bequest](../Smells/Refused%20Bequest.md) - [Switch Statements](../Smells/Switch%20Statements.md) - [Temporary Field](../Smells/Temporary%20Field.md) ![image](#) 
### Change Preventers
 These smells mean that if you need to change something in one place in your code, you have to make many changes in other places too. Program development becomes much more complicated and expensive as a result. - [Divergent Change](../Smells/Divergent%20Change.md) - [Parallel Inheritance Hierarchies](../Smells/Parallel%20Inheritance%20Hierarchies.md) - [Shotgun Surgery](../Smells/Shotgun%20Surgery.md) ![image](#) 
### Dispensables
 A dispensable is something pointless and unneeded whose absence would make the code cleaner, more efficient and easier to understand. - [Comments](../Smells/Comments.md) - [Duplicate Code](../Smells/Duplicate%20Code.md) - [Data Class](../Smells/Data%20Class.md) - [Dead Code](../Smells/Dead%20Code.md) - [Lazy Class](../Smells/Lazy%20Class.md) - [Speculative Generality](../Smells/Speculative%20Generality.md) ![image](#) 
### Couplers
 All the smells in this group contribute to excessive coupling between classes or show what happens if coupling is replaced by excessive delegation. - [Feature Envy](../Smells/Feature%20Envy.md) - [Inappropriate Intimacy](../Smells/Inappropriate%20Intimacy.md) - [Incomplete Library Class](../Smells/Incomplete%20Library%20Class.md) - [Message Chains](../Smells/Message%20Chains.md) - [Middle Man](../Smells/Middle%20Man.md)

## Related

- [[Bloaters]]
- [[Oo Abusers]]
- [[Change Preventers]]
- [[Dispensables]]
- [[Couplers]]
- [[Refactoring/Techniques|Techniques]]

