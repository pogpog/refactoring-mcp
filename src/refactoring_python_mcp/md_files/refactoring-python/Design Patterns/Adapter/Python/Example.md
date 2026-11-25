---
tags: [design-patterns]
date_created: 2026-05-20
status: seed
---

# Adapterin Python

 **Adapter** is a structural design pattern, which allows incompatible objects to collaborate. The Adapter acts as a wrapper between two objects. It catches calls for one object and transforms them to format and interface recognizable by the second object. [Learn more about Adapter](../../Adapter.md) Navigation [Intro](#) [Conceptual Example (via inheritance)](#) [main](#) [Output](#) [Conceptual Example (via object composition)](#) [main](#) [Output](#) **Complexity:** **Popularity:** **Usage examples:** The Adapter pattern is pretty common in Python code. It’s very often used in systems based on some legacy code. In such cases, Adapters make legacy code work with modern classes. **Identification:** Adapter is recognizable by a constructor which takes an instance of a different abstract/interface type. When the adapter receives a call to any of its methods, it translates parameters to the appropriate format and then directs the call to one or several methods of the wrapped object. 
## Conceptual Example (via inheritance)
 This example illustrates the structure of the **Adapter** design pattern. It focuses on answering these questions: - What classes does it consist of? - What roles do these classes play? - In what way the elements of the pattern are related? 
#### main.py:Conceptual example
 
```
class Target:
 """
 The Target defines the domain-specific interface used by the client code.
 """

 def request(self) -> str:
 return "Target: The default target's behavior."

class Adaptee:
 """
 The Adaptee contains some useful behavior, but its interface is incompatible
 with the existing client code. The Adaptee needs some adaptation before the
 client code can use it.
 """

 def specific_request(self) -> str:
 return ".eetpadA eht fo roivaheb laicepS"

class Adapter(Target, Adaptee):
 """
 The Adapter makes the Adaptee's interface compatible with the Target's
 interface via multiple inheritance.
 """

 def request(self) -> str:
 return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"

def client_code(target: "Target") -> None:
 """
 The client code supports all classes that follow the Target interface.
 """

 print(target.request(), end="")

if __name__ == "__main__":
 print("Client: I can work just fine with the Target objects:")
 target = Target()
 client_code(target)
 print("\n")

 adaptee = Adaptee()
 print("Client: The Adaptee class has a weird interface. "
 "See, I don't understand it:")
 print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

 print("Client: But I can work with it via the Adapter:")
 adapter = Adapter()
 client_code(adapter)
```
 
#### Output.txt:Execution result
 
```
Client: I can work just fine with the Target objects:
Target: The default target's behavior.

Client: The Adaptee class has a weird interface. See, I don't understand it:
Adaptee: .eetpadA eht fo roivaheb laicepS

Client: But I can work with it via the Adapter:
Adapter: (TRANSLATED) Special behavior of the Adaptee.
```
 
## Conceptual Example (via object composition)
 This example illustrates the structure of the **Adapter** design pattern. It focuses on answering these questions: - What classes does it consist of? - What roles do these classes play? - In what way the elements of the pattern are related? 
#### main.py:Conceptual example
 
```
class Target:
 """
 The Target defines the domain-specific interface used by the client code.
 """

 def request(self) -> str:
 return "Target: The default target's behavior."

class Adaptee:
 """
 The Adaptee contains some useful behavior, but its interface is incompatible
 with the existing client code. The Adaptee needs some adaptation before the
 client code can use it.
 """

 def specific_request(self) -> str:
 return ".eetpadA eht fo roivaheb laicepS"

class Adapter(Target):
 """
 The Adapter makes the Adaptee's interface compatible with the Target's
 interface via composition.
 """

 def __init__(self, adaptee: Adaptee) -> None:
 self.adaptee = adaptee

 def request(self) -> str:
 return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"

def client_code(target: Target) -> None:
 """
 The client code supports all classes that follow the Target interface.
 """

 print(target.request(), end="")

if __name__ == "__main__":
 print("Client: I can work just fine with the Target objects:")
 target = Target()
 client_code(target)
 print("\n")

 adaptee = Adaptee()
 print("Client: The Adaptee class has a weird interface. "
 "See, I don't understand it:")
 print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

 print("Client: But I can work with it via the Adapter:")
 adapter = Adapter(adaptee)
 client_code(adapter)
```
 
#### Output.txt:Execution result
 
```
Client: I can work just fine with the Target objects:
Target: The default target's behavior.

Client: The Adaptee class has a weird interface. See, I don't understand it:
Adaptee: .eetpadA eht fo roivaheb laicepS

Client: But I can work with it via the Adapter:
Adapter: (TRANSLATED) Special behavior of the Adaptee.
```

