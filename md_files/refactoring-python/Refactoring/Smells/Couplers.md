---
tags: [refactoring]
date_created: 2026-05-20
status: seed
---

# Couplers

 All the smells in this group contribute to excessive coupling between classes or show what happens if coupling is replaced by excessive delegation. [Feature Envy](../../Smells/Feature%20Envy.md) A method accesses the data of another object more than its own data. [Inappropriate Intimacy](../../Smells/Inappropriate%20Intimacy.md) One class uses the internal fields and methods of another class. [Message Chains](../../Smells/Message%20Chains.md) In code you see a series of calls resembling `$a->b()->c()->d()` [Middle Man](../../Smells/Middle%20Man.md) If a class performs only one action, delegating work to another class, why does it exist at all?

## Related

- [[Feature Envy]]
- [[Inappropriate Intimacy]]
- [[Incomplete Library Class]]
- [[Message Chains]]
- [[Middle Man]]
- [[Bloaters]]
- [[Oo Abusers]]
- [[Change Preventers]]
- [[Dispensables]]
- [[Refactoring/Smells|Code Smells Overview]]

