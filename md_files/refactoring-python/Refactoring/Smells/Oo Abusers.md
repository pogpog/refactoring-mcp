---
tags: [refactoring]
date_created: 2026-05-20
status: seed
---

# Object-Orientation Abusers

 All these smells are incomplete or incorrect application of object-oriented programming principles. [Switch Statements](../../Smells/Switch%20Statements.md) You have a complex `switch` operator or sequence of `if` statements. [Temporary Field](../../Smells/Temporary%20Field.md) Temporary fields get their values (and thus are needed by objects) only under certain circumstances. Outside of these circumstances, they’re empty. [Refused Bequest](../../Smells/Refused%20Bequest.md) If a subclass uses only some of the methods and properties inherited from its parents, the hierarchy is off-kilter. The unneeded methods may simply go unused or be redefined and give off exceptions. [Alternative Classes with Different Interfaces](../../Smells/Alternative%20Classes%20With%20Different%20Interfaces.md) Two classes perform identical functions but have different method names.

## Related

- [[Alternative Classes With Different Interfaces]]
- [[Refused Bequest]]
- [[Switch Statements]]
- [[Temporary Field]]
- [[Bloaters]]
- [[Change Preventers]]
- [[Dispensables]]
- [[Couplers]]
- [[Refactoring/Smells|Code Smells Overview]]

