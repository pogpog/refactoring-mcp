---
tags: [refactoring]
date_created: 2026-05-20
status: seed
---

# Simplifying Method Calls

 These techniques make method calls simpler and easier to understand. This, in turn, simplifies the interfaces for interaction between classes. [Rename Method](../../Rename%20Method.md) **Problem:** The name of a method doesn’t explain what the method does. **Solution:** Rename the method. [Add Parameter](../../Add%20Parameter.md) **Problem:** A method doesn’t have enough data to perform certain actions. **Solution:** Create a new parameter to pass the necessary data. [Remove Parameter](../../Remove%20Parameter.md) **Problem:** A parameter isn’t used in the body of a method. **Solution:** Remove the unused parameter. [Separate Query from Modifier](../../Separate%20Query%20From%20Modifier.md) **Problem:** Do you have a method that returns a value but also changes something inside an object? **Solution:** Split the method into two separate methods. As you would expect, one of them should return the value and the other one modifies the object. [Parameterize Method](../../Parameterize%20Method.md) **Problem:** Multiple methods perform similar actions that are different only in their internal values, numbers or operations. **Solution:** Combine these methods by using a parameter that will pass the necessary special value. [Replace Parameter with Explicit Methods](../../Replace%20Parameter%20With%20Explicit%20Methods.md) **Problem:** A method is split into parts, each of which is run depending on the value of a parameter. **Solution:** Extract the individual parts of the method into their own methods and call them instead of the original method. [Preserve Whole Object](../../Preserve%20Whole%20Object.md) **Problem:** You get several values from an object and then pass them as parameters to a method. **Solution:** Instead, try passing the whole object. [Replace Parameter with Method Call](../../Replace%20Parameter%20With%20Method%20Call.md) **Problem:** Calling a query method and passing its results as the parameters of another method, while that method could call the query directly. **Solution:** Instead of passing the value through a parameter, try placing a query call inside the method body. [Introduce Parameter Object](../../Introduce%20Parameter%20Object.md) **Problem:** Your methods contain a repeating group of parameters. **Solution:** Replace these parameters with an object. [Remove Setting Method](../../Remove%20Setting%20Method.md) **Problem:** The value of a field should be set only when it’s created, and not change at any time after that. **Solution:** So remove methods that set the field’s value. [Hide Method](../../Hide%20Method.md) **Problem:** A method isn’t used by other classes or is used only inside its own class hierarchy. **Solution:** Make the method private or protected. [Replace Constructor with Factory Method](../../Replace%20Constructor%20With%20Factory%20Method.md) **Problem:** You have a complex constructor that does something more than just setting parameter values in object fields. **Solution:** Create a factory method and use it to replace constructor calls. [Replace Error Code with Exception](../../Replace%20Error%20Code%20With%20Exception.md) **Problem:** A method returns a special value that indicates an error? **Solution:** Throw an exception instead. [Replace Exception with Test](../../Replace%20Exception%20With%20Test.md) **Problem:** You throw an exception in a place where a simple test would do the job? **Solution:** Replace the exception with a condition test.

## Related

- [[Rename Method]]
- [[Add Parameter]]
- [[Remove Parameter]]
- [[Separate Query From Modifier]]
- [[Parameterize Method]]
- [[Replace Parameter With Explicit Methods]]
- [[Preserve Whole Object]]
- [[Replace Parameter With Method Call]]
- [[Introduce Parameter Object]]
- [[Remove Setting Method]]
- [[Hide Method]]
- [[Replace Constructor With Factory Method]]
- [[Replace Error Code With Exception]]
- [[Replace Exception With Test]]
- [[Refactoring/Techniques|Techniques Overview]]

