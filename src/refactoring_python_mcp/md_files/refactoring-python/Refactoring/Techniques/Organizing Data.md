---
tags: [refactoring]
date_created: 2026-05-20
status: seed
---

# Organizing Data

 These refactoring techniques help with data handling, replacing primitives with rich class functionality. Another important result is untangling of class associations, which makes classes more portable and reusable. [Self Encapsulate Field](../../Self%20Encapsulate%20Field.md) **Problem:** You use direct access to private fields inside a class. **Solution:** Create a getter and setter for the field, and use only them for accessing the field. [Replace Data Value with Object](../../Replace%20Data%20Value%20With%20Object.md) **Problem:** A class (or group of classes) contains a data field. The field has its own behavior and associated data. **Solution:** Create a new class, place the old field and its behavior in the class, and store the object of the class in the original class. [Change Value to Reference](../../Change%20Value%20To%20Reference.md) **Problem:** So you have many identical instances of a single class that you need to replace with a single object. **Solution:** Convert the identical objects to a single reference object. [Change Reference to Value](../../Change%20Reference%20To%20Value.md) **Problem:** You have a reference object that’s too small and infrequently changed to justify managing its life cycle. **Solution:** Turn it into a value object. [Replace Array with Object](../../Replace%20Array%20With%20Object.md) **Problem:** You have an array that contains various types of data. **Solution:** Replace the array with an object that will have separate fields for each element. [Duplicate Observed Data](../../Duplicate%20Observed%20Data.md) **Problem:** Is domain data stored in classes responsible for the GUI? **Solution:** Then it’s a good idea to separate the data into separate classes, ensuring connection and synchronization between the domain class and the GUI. [Change Unidirectional Association to Bidirectional](../../Change%20Unidirectional%20Association%20To%20Bidirectional.md) **Problem:** You have two classes that each need to use the features of the other, but the association between them is only unidirectional. **Solution:** Add the missing association to the class that needs it. [Change Bidirectional Association to Unidirectional](../../Change%20Bidirectional%20Association%20To%20Unidirectional.md) **Problem:** You have a bidirectional association between classes, but one of the classes doesn’t use the other’s features. **Solution:** Remove the unused association. [Replace Magic Number with Symbolic Constant](../../Replace%20Magic%20Number%20With%20Symbolic%20Constant.md) **Problem:** Your code uses a number that has a certain meaning to it. **Solution:** Replace this number with a constant that has a human-readable name explaining the meaning of the number. [Encapsulate Field](../../Encapsulate%20Field.md) **Problem:** You have a public field. **Solution:** Make the field private and create access methods for it. [Encapsulate Collection](../../Encapsulate%20Collection.md) **Problem:** A class contains a collection field and a simple getter and setter for working with the collection. **Solution:** Make the getter-returned value read-only and create methods for adding/deleting elements of the collection. [Replace Type Code with Class](../../Replace%20Type%20Code%20With%20Class.md) **Problem:** A class has a field that contains type code. The values of this type aren’t used in operator conditions and don’t affect the behavior of the program. **Solution:** Create a new class and use its objects instead of the type code values. [Replace Type Code with Subclasses](../../Replace%20Type%20Code%20With%20Subclasses.md) **Problem:** You have a coded type that directly affects program behavior (values of this field trigger various code in conditionals). **Solution:** Create subclasses for each value of the coded type. Then extract the relevant behaviors from the original class to these subclasses. Replace the control flow code with polymorphism. [Replace Type Code with State/Strategy](../../Replace%20Type%20Code%20With%20State%20Strategy.md) **Problem:** You have a coded type that affects behavior but you can’t use subclasses to get rid of it. **Solution:** Replace type code with a state object. If it’s necessary to replace a field value with type code, another state object is “plugged in”. [Replace Subclass with Fields](../../Replace%20Subclass%20With%20Fields.md) **Problem:** You have subclasses differing only in their (constant-returning) methods. **Solution:** Replace the methods with fields in the parent class and delete the subclasses.

## Related

- [[Self Encapsulate Field]]
- [[Replace Data Value With Object]]
- [[Change Value To Reference]]
- [[Change Reference To Value]]
- [[Replace Array With Object]]
- [[Duplicate Observed Data]]
- [[Change Unidirectional Association To Bidirectional]]
- [[Change Bidirectional Association To Unidirectional]]
- [[Replace Magic Number With Symbolic Constant]]
- [[Encapsulate Field]]
- [[Encapsulate Collection]]
- [[Replace Type Code With Class]]
- [[Replace Type Code With Subclasses]]
- [[Replace Type Code With State Strategy]]
- [[Replace Subclass With Fields]]
- [[Refactoring/Techniques|Techniques Overview]]

