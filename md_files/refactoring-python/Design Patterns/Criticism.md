---
tags: [design-patterns]
date_created: 2026-05-20
status: seed
---

# Criticism of patterns

 It seems like only lazy people haven’t criticized design patterns yet. Let’s take a look at the most typical arguments against using patterns. 
#### Kludges for a weak programming languageThis point of view was first expressed by Paul Graham in the essayRevenge of the Nerds. Read more about this on thisWiki page
 Usually the need for patterns arises when people choose a programming language or a technology that lacks the necessary level of abstraction. In this case, patterns become a kludge that gives the language much-needed super-abilities. For example, the [Strategy](Strategy.md) pattern can be implemented with a simple anonymous (lambda) function in most modern programming languages. 
#### Inefficient solutions
 Patterns try to systematize approaches that are already widely used. This unification is viewed by many as a dogma, and they implement patterns “to the letter”, without adapting them to the context of their project. 
#### Unjustified use
 > If all you have is a hammer, everything looks like a nail. This is the problem that haunts many novices who have just familiarized themselves with patterns. Having learned about patterns, they try to apply them everywhere, even in situations where simpler code would do just fine.

