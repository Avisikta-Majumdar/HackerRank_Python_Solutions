import cmath
m=complex(input())
print(abs(complex(m.real,m.imag)),'\n',cmath.phase(complex(m.real,m.imag)))
