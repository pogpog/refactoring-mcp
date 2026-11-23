---
tags: []
date_created: 2026-05-20
status: seed
---

# Inline Class

 
### Problem
 A class does almost nothing and isn’t responsible for anything, and no additional responsibilities are planned for it. 
### Solution
 Move all features from the class to another one. Before ![Inline Class - Before](#) After ![Inline Class - After](#) 
### Why Refactor
 - Often this technique is needed after the features of one class are “transplanted” to other classes, leaving that class with little to do. 
### Benefits
 - Eliminating needless classes frees up operating memory on the computer—and bandwidth in your head. 
### How to Refactor
 2. In the recipient class, create the public fields and methods present in the donor class. Methods should refer to the equivalent methods of the donor class. 4. Replace all references to the donor class with references to the fields and methods of the recipient class. 6. Now test the program and make sure that no errors have been added. If tests show that everything is working A-OK, start using [Move Method](Move%20Method.md) and [Move Field](Move%20Field.md) to completely transplant all functionality to the recipient class from the original one. Continue doing so until the original class is completely empty. 8. Delete the original class. 

## Related

- [[Extract Class]]
- [[Collapse Hierarchy]]
- [[Lazy Class]]
- [[Shotgun Surgery]]
- [[Moving Features Between Objects]]

