---
tags: []
date_created: 2026-05-20
status: seed
---

# Pull Up Field

 
### Problem
 Two classes have the same field. 
### Solution
 Remove the field from subclasses and move it to the superclass. Before ![Pull Up Field - Before](#) After ![Pull Up Field - After](#) 
### Why Refactor
 Subclasses grew and developed separately, causing identical (or nearly identical) fields and methods to appear. 
### Benefits
 - Eliminates duplication of fields in subclasses. - Eases subsequent relocation of duplicate methods, if they exist, from subclasses to a superclass. 
### How to Refactor
 2. Make sure that the fields are used for the same needs in subclasses. 4. If the fields have different names, give them the same name and replace all references to the fields in existing code. 6. Create a field with the same name in the superclass. Note that if the fields were private, the superclass field should be protected. 8. Remove the fields from the subclasses. 10. You may want to consider using [Self Encapsulate Field](Self%20Encapsulate%20Field.md) for the new field, in order to hide it behind access methods. 

## Related

- [[Pull Up Method]]
- [[Pull Up Constructor Body]]
- [[Push Down Field]]
- [[Duplicate Code]]
- [[Dealing With Generalization]]

