import os
import sql.sql_backend as sql

# For persistence
import numpy as np
from gtda.homology import VietorisRipsPersistence

# For barcode
import matplotlib.pyplot as plt
import gudhi

import numpy as np


##
#
# FUNCTION: persistence_diagram
#
# DESCRIPTION: Función que imprime el diagrama de persistencia del complejo simplicial representado
#              por los usuarios y sus interaccionesdb_engine, 
#
# PARAM: dist_mat - Matriz de distancias (completa o triangular inferior)
#        plot - Booleano para imprimir el diagrama de persistencia
#        filename - Nombre del archivo donde se guardará el diagrama
#
# RETURN: diagram - lista de tuplas conteniento el número de beti de la barra correspondiente y una
#         tupla indicanto el nacimiento y muerte de cada barra del diagrama
#
##
def persistence_diagram(dist_mat, plot = False, filename = 'persistence.png'):

    # Cambiamos la matriz de distancias de triangular inferior a una completa
    for i in range(len(dist_mat)):
        for j in range(len(dist_mat[i])):
            dist_mat[i][j] = dist_mat[j][i]
    
    # Create Rips complex
    VR = VietorisRipsPersistence(metric='precomputed', homology_dimensions=[0,1,2])
    diagram = VR.fit_transform(np.asarray([dist_mat]))

    # Plot persistence diagram
    plot = VR.plot(diagram, sample=0)

    #!! Show plot (to manipulate it and see data)
    #plot.show()

    # Save plot
    if plot:
        file = os.path.realpath(__file__)
        file = '/'.join(file.split('/')[:-3])
        file += '/output/diagrams/' + filename
        plot.write_image(file, format='png')
    
    ret_diagram = []
    for i in range(len(diagram[0])-1, -1, -1):
        ret_diagram.append((int(diagram[0][i][2]), (diagram[0][i][0], diagram[0][i][1])))
    
    return ret_diagram


##
#
# FUNCTION: barcode_diagram
#
# DESCRIPTION: Función que imprime el diagrama de barras del complejo simplicial representado
#              por los usuarios y sus interacciones
#
# PARAM: dist_mat - Matriz de distancias (completa o triangular inferior)
#        plot - Booleano para imprimir el diagrama de barras
#        filename - Nombre del archivo donde se guardará el diagrama
#
# RETURN: diagram - lista de tuplas conteniento el número de beti de la barra correspondiente y una
#         tupla indicanto el nacimiento y muerte de cada barra del diagrama
#
##
def barcode_diagram(dist_mat, plot = False, filename = 'barcode.png'):
    # Create Rips complex
    graph = gudhi.RipsComplex(distance_matrix=dist_mat)

    # Compute simplex tree
    st = graph.create_simplex_tree(max_dimension=3)

    # Plot persistence diagram
    diagram = st.persistence()

    if plot:
        gudhi.plot_persistence_barcode(diagram)

        #!! Show plot (to manipulate it and see data)
        #plt.show()

        # Save plot
        file = os.path.realpath(__file__)
        file = '/'.join(file.split('/')[:-3])
        file += '/output/diagrams/' + filename
        plt.savefig(file)
        plt.close()
    
    return diagram