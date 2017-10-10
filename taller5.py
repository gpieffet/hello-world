# Punto 1
def chequear_fermat(a, b, c, n):
    if a**n + b**n == c**n:
        print 'Oye, Fermat estaba equivocado'
    else:
        print 'No, la igualdad no funciona.'
        print '%d^%d + %d^%d != %d^%d' % (a, n, b, n, c, n)
        print '%d != %d' %(a**n+b**n, c**n)

def obtener_valores():
    """Obtener 4 valores del usuario"""
    print 'a^n + b^n = c^n'
    a = raw_input('Valor de a: ')
    b = raw_input('Valor de b: ')
    c = raw_input('Valor de c: ')
    d = raw_input('Valor de n: ')
    chequear_fermat(int(a), int(b), int(c), int(d))

# a, b, c, n = 1, 2, 4, 5
# chequear_fermat(a, b, c, n)
obtener_valores()



# Punto 2.a
def es_triangulo(a, b, c):
    """Determina si tres longitudes forman un triangulo"""
    if (a > c + b) or (b > a + c) or (c > a + b):
        print 'No'
    else:
        print 'Si'

# es_triangulo(1, 2, 4)
# es_triangulo(1, 2.5, 3)
# es_triangulo(5, 2, 4)
# es_triangulo(1, 2, 3)

# Punto 2.b
def es_triangulo(a, b, c):
    """Determina si tres longitudes forman un triangulo"""
    if (a > c + b) or (b > a + c) or (c > a + b):
        print 'No'
    else:
        if (a == c + b) or (b == a + c) or (c == a + b):
            print 'Si, pero degenerado: ', c, '=', a+b
        else:
            print 'Si'

# es_triangulo(1, 2, 4)
# es_triangulo(1, 2.5, 3)
# es_triangulo(5, 2, 4)
# es_triangulo(1, 2, 3)



# Punto 2.c
def es_triangulo(a, b, c):
    """Determina si tres longitudes forman un triangulo"""
    if (a > c + b) or (b > a + c) or (c > a + b):
        print 'No'
    else:
        if (a != c + b) and (b != a + c) and (c != a + b):
            print 'Si: '
        else:
            print 'Si, pero degenerado: ', c, '=', a+b 

# es_triangulo(1, 2, 4)
# es_triangulo(1, 2.5, 3)
# es_triangulo(5, 2, 4)
# es_triangulo(1, 2, 3)
