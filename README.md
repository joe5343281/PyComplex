# PyComplex

- - -

## Introduction
It's a simple complex number module to calculate complex number eq:add, sub, mul, div, conj...

## How to Use
Clone/Download this repository.

Put pycomplex.py which the place you want.

Open .py file in  the same folder to write ``import pycomplex``.

## Class attributes

* ``r`` represents real number 
* ``i`` represents imaginary number  
   
## Function Examples

**``pycomplex.Complex(a, b)``** (Constructor)
   * Comstruct a pycomplex.Complex object to represent acomplex number
      * Example
         * ``comp = pycomplex.Complex(1, 1)``, ``comp`` represents  ``1 + i``
      * if constructor without arguments given 
         * costrutor will use default value, pycomplex.Complex(0, 0).
      
 - - -

**``pycomplex.Complex().__add__(pycomplex.Complex Object)``**  (Magic method)
   * Operator ``+`` with plus ability to add a pycomplex.Complex Object.
      * Return a pycomplex.Complex object
   * Example
    
         comp = pycomplex.Complex(1, 1) + pycomplex.Complex(2, 2)
      * ``comp`` represents ``pycomplex.Complex(3, 3)``
   
   * Other
      
         c1 = pycomplex.Complex(1, 1)
         c2 = pycomplex.Complex(2, 2)
         c3 = c1 + c2 
    
      * ``c3`` also represents ``pycomplex.Complex(3, 3)``
         
 - - -

**``pycomplex.Complex().__sub__(pycomplex.Complex Object)``** (Magic method)
   * Operator ``-`` with plus ability to subtract a pycomplex.Complex Object.
      * Return a pycomplex.Complex object
   * Example

         comp = pycomplex.Complex(3, 3) - pycomplex.Complex(2, 2)      
      * ``comp`` represents ``pycomplex.Complex(1, 1)``
   
   * Other
            
         c1 = pycomplex.Complex(3, 3)                 
         c2 = pycomplex.Complex(2, 2)
         c3 = c1 - c2
      * ``c3`` also represents ``pycomplex.Complex(1, 1)``
   
- - -

**``pycomplex.Complex().__mul__(pycomplex.Complex Object)``** (Magic method)
   * Operator ``*`` with plus ability to multiply a pycomplex.Complex Object.
      * Return a pycomplex.Complex object
   * Example

         comp = pycomplex.Complex(1, 1) * pycomplex.Complex(2, 2)      
      * ``comp`` represents ``pycomplex.Complex(0, 4)``
   
   * Other
            
         c1 = pycomplex.Complex(1, 1)                 
         c2 = pycomplex.Complex(2, 2)
         c3 = c1 * c2
      * ``c3`` also represents ``pycomplex.Complex(0, 4)``

- - -

**``pycomplex.Complex().__mul__(pycomplex.Complex Object)``** (Magic method)
   * Operator ``*`` with plus ability to multiply a pycomplex.Complex Object.
      * Return a pycomplex.Complex object
   * Example

         comp = pycomplex.Complex(2, 2) * pycomplex.Complex(1, 1)      
      * ``comp`` represents ``pycomplex.Complex(2, 0)``
   
   * Other
            
         c1 = pycomplex.Complex(2, 2)                 
         c2 = pycomplex.Complex(1, 1)
         c3 = c1 * c2
      * ``c3`` also represents ``pycomplex.Complex(2, 0)``

- - -  

**``pycomplex.Complex().conj(pycomplex.Complex Object)``** (Function)
   * Return a pycomplex.Complex object
   * Example
   
         comp = pycomplex.Complex().conj(1, 1)
      * ``comp`` represents ``pycomplex.Complex(1, -1)``
   
   * Other    
         
         c1 = pycomplex.Complex(1, 1)
         c1.conj()
      * ``comp`` also represents ``pycomplex.Complex(1, -1)``

- - -

**``pycomplex.Complex().ln(pycomplex.Complex Object)``** (Function) 
   * Return a pycomplex.Complex object
   * Example
   
         comp = pycomplex.Complex(1, 1).ln()
   
   * Other    
         
         c1 = pycomplex.Complex(1, 1)
         c1.ln()
         
- - -

**``pycomplex.Complex().exp(pycomplex.Complex Object)``** (Function) 
   * Return a pycomplex.Complex object
   * Example
   
         comp = pycomplex.Complex(1, 1).exp()
   
   * Other    
         
         c1 = pycomplex.Complex(1, 1)
         c1.exp()
         
- - -

**``pycomplex.Complex().rad()``** (Function) 
   * Return a value of rad
   * Example
   
         comp = pycomplex.Complex(1, 1).rad()
   
   * Other    
         
         c1 = pycomplex.Complex(1, 1)
         c1.rad()
      
- - -

**``pycomplex.Complex().parser(string)``** (Function)
