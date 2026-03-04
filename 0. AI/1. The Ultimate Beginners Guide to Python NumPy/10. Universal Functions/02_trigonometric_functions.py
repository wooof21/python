
import numpy as np

'''
### Trigonometric functions

They return the corresponding trigonometric operation in the values of the array. 
The values are interpreted as radians:

    - `np.sin`: sine
    - `np.cos`: cosine
    - `np.tan`: tangent
    - `np.hypot`: hypotenuse
    - `np.arc*`: arc-sine, consine or tangent, ex: `np.arcsin`
    - `np.*h`: hyperbolic sine, cosine or tangent, ex: `np.sinh`
    - `np.arc*h`: hyperbolic arc-sine, cosine or tangent, ex: `np.arcsinh`
    - `np.degrees`, `np.rad2deg`: converts angles from radians to degrees
    - `np.radians`, `np.deg2rad`: converts angles from degrees to radians
'''

pi = np.radians(180)
print(pi) # 3.141592653589793

sin = np.sin(pi)
print(sin) # 1.2246467991473532e-16

cos = np.cos(pi)
print(cos) # -1.0