##
#
# MODULE: similarity
#
# DESCRIPTION: Módulo que contiene las funciones necesarias para calcular la similitud entre dos
#              diagramas de persistencia
#
##

import numpy as np

##
#
# FUNCTION: similarity
#
# DESCRIPTION: Función que calcula la similitud entre dos diagramas de persistencia a través del
# índice de Jaccard
#
# PARAMS: A - Diagrama de persistencia A
#         B - Diagrama de persistencia B
#
# RETURN: sim - Similitud entre los diagramas
#
##
def similarity(A, B):

    A_0, A_1, A_2 = [], [], []
    B_0, B_1, B_2 = [], [], []

    for a in A:
        if a[0] == 0:
            A_0.append(a[1])
        elif a[0] == 1:
            A_1.append(a[1])
        else:
            A_2.append(a[1])
    
    for b in B:
        if b[0] == 0:
            B_0.append(b[1])
        elif b[0] == 1:
            B_1.append(b[1])
        else:
            B_2.append(b[1])
    
    dim_0 = dim_similarity(A_0, B_0)
    dim_1 = dim_similarity(A_1, B_1)
    dim_2 = dim_similarity(A_2, B_2)

    print(dim_0, dim_1, dim_2)

    sim = (dim_0 + dim_1 + dim_2) / 3

    return sim


##
#
# FUNCTION: dim_similarity
#
# DESCRIPTION: Función que calcula la similitud entre dos códigos de barras de un diagrama de
# persistencia con la misma dimensión
#
# PARAMS: A - Código de barras A
#         B - Código de barras B
#
# RETURN: sim - Similitud entre los códigos de barras
#
##
def dim_similarity(A, B):
    sim = 0

    if len(A) == 0 or len(B) == 0:
        if len(A) == 0 and len(B) == 0:
            return 1
        else:
            return 0
    
    for a in A:
        sup_b = 0
        for b in B:
            aux = index(a, b)
            
            if aux > sup_b:
                sup_b = aux

        sim += sup_b
    
    for b in B:
        sup_a = 0
        for a in A:
            aux = index(a, b)

            if aux > sup_a:
                sup_a = aux

        sim += sup_a
    
    sim *= 1 /(len(A) + len(B))

    return sim


##
#
# FUNCTION: index
#
# DESCRIPTION: Función que calcula el índice de Jaccard entre dos intervalos (barras)
#
# PARAMS: a - Barra a
#         b - Barra b
#
# RETURN: aux - Índice de Jaccard
#
##
def index(a, b):
    a_cap_b = 0
    a_cup_b = 0

    if a[1] < b[0] or a[0] > b[1]:
        return 0

    if a[1] > b[1]:
        a_cap_b = b[1]
        a_cup_b = a[1]
    else:
        a_cap_b = a[1]
        a_cup_b = b[1]
    if a[0] < b[0]:
        a_cap_b -= b[0]
        a_cup_b -= a[0]
    else:
        a_cap_b -= a[0]
        a_cup_b -= b[0]
    
    if np.isinf(a_cap_b) and np.isinf(a_cup_b):
        return 1
    else:
        return a_cap_b / a_cup_b