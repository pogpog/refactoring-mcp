---
tags: [refactoring]
date_created: 2026-05-20
status: seed
---

# Moving Features between Objects

 Even if you have distributed functionality among different classes in a less-than-perfect way, there’s still hope. These refactoring techniques show how to safely move functionality between classes, create new classes, and hide implementation details from public access. [Move Method](../../Move%20Method.md) **Problem:** A method is used more in another class than in its own class. **Solution:** Create a new method in the class that uses the method the most, then move code from the old method to there. Turn the code of the original method into a reference to the new method in the other class or else remove it entirely. [Move Field](../../Move%20Field.md) **Problem:** A field is used more in another class than in its own class. **Solution:** Create a field in a new class and redirect all users of the old field to it. [Extract Class](../../Extract%20Class.md) **Problem:** When one class does the work of two, awkwardness results. **Solution:** Instead, create a new class and place the fields and methods responsible for the relevant functionality in it. [Inline Class](../../Inline%20Class.md) **Problem:** A class does almost nothing and isn’t responsible for anything, and no additional responsibilities are planned for it. **Solution:** Move all features from the class to another one. [Hide Delegate](../../Hide%20Delegate.md) **Problem:** The client gets object B from a field or method of object А. Then the client calls a method of object B. **Solution:** Create a new method in class A that delegates the call to object B. Now the client doesn’t know about, or depend on, class B. [Remove Middle Man](../../Remove%20Middle%20Man.md) **Problem:** A class has too many methods that simply delegate to other objects. **Solution:** Delete these methods and force the client to call the end methods directly. [Introduce Foreign Method](../../Introduce%20Foreign%20Method.md) **Problem:** A utility class doesn’t contain the method that you need and you can’t add the method to the class. **Solution:** Add the method to a client class and pass an object of the utility class to it as an argument. [Introduce Local Extension](../../Introduce%20Local%20Extension.md) **Problem:** A utility class doesn’t contain some methods that you need. But you can’t add these methods to the class. **Solution:** Create a new class containing the methods and make it either the child or wrapper of the utility class.

## Related

- [[Move Method]]
- [[Move Field]]
- [[Extract Class]]
- [[Inline Class]]
- [[Hide Delegate]]
- [[Remove Middle Man]]
- [[Introduce Foreign Method]]
- [[Introduce Local Extension]]
- [[Composing Methods]]
- [[Dealing With Generalization]]
- [[Refactoring/Techniques|Techniques Overview]]

