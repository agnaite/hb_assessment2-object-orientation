# hb_assessment2-object-orientation

## Part 1: Discussion

### 1. What are the three main design advantages that object orientation can provide? Explain each concept.
Abstraction: Hiding all but the relevant data about an object in order to reduce complexity and increase efficiency.

Encapsulation: Pairing data and functions to keep everything together.

Polymorphism: The ability to process objects differently depending on their data type or class.
   
### 2. What is a class?
It's a template for creating objects, i.e. a type of thing (like an Integer or File).

### 3. What is an instance attribute?
A piece of data set directly on the object (and not the class itself).

### 4. What is a method?
A function defined for a class.

### 5. What is an instance in object orientation?
An individual instance of a class (e.g. a particular file).

### 6. How is a class attribute different than an instance attribute? Give an example of when you might use each.
A class attribute is data set on the class itself, and not an instance of a class. 

For example:

If you have a class `Shoes` and know that the majority of the `Shoes` instances will have the attribute `material = 'leather'`, then it would make sense to set a class attribute, so that all the `Shoes` instances will have the material set at `__init__`. 

On the other hand, if `Shoes` contained all types of shoes with different materials, it would make more sense to set the attribute on each instance individually.
