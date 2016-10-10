# PyComplex

- - -

## Introduction
It's a simple complex number module to calculate complex number eq:add, sub, mul, div, conj...

## How to Use
Clone/Download this repository.

Put PyComplex.py which the place you want.

Open .py file in  the same folder to write ``import PyComplex``.

## Class attributes

*   
   
         r represents real number 
         i represents imaginary number  
   
## Function Examples

* **``PyComplex.Complex(a, b)``** (Constructor)
   * Example
      * ``comp = PyComplex.Complex(1, 1)``, ``comp`` represents  ``1 + i``
      * if constructor without arguments given 
         * costrutor will use default value, PyComplex.Complex(0, 0).
      
 - - -

**``PyComplex.Complex.__add__(PyComplex.Complex Object)``**  (Magic method)
   * Operator ``+`` with plus ability to add a PyComplex.Complex Object.
   * Example
    
         comp = PyComplex.Complex(1, 1) + PyComplex.Complex(2, 2)
   * ``comp`` represents ``PyComplex.Complex(3, 3)``
   
   * Other
      
         c1 = PyComplex.Complex(1, 1)
         c2 = PyComplex.Complex(2, 2)
         c3 = c1 + c2 
   ``c3`` also represents ``PyComplex.Complex(3, 3)``
         
 - - -

**``PyComplex.Complex.__sub__(PyComplex.Complex Object)``** (Magic method)
   * Operator ``-`` with plus ability to subtract a PyComplex.Complex Object.
   * Example

         comp = PyComplex.Complex(3, 3) - PyComplex.Complex(2, 2)      
   ``comp`` represents ``PyComplex.Complex(1, 1)``
   
   * Other
            
         c1 = PyComplex.Complex(3, 3)                 
         c2 = PyComplex.Complex(2, 2)
         c3 = c1 - c2
   ``c3`` also represents ``PyComplex.Complex(1, 1)``
   
