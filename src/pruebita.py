import sql.sql_backend as sql
import distance.matrix as mat
import persistence.diagrams as di


def main():
    reduced_db_engine = sql.get_engine('reduced_db')

    # Obtención de la matriz de adyacencia

    #adj_mat = mat.adjacency_matrix(reduced_db_engine, True)

    # Obtención de la matriz de distancias

    #dist_mat = mat.distance_matrix(adj_mat, True)

    dist_mat = []
    with open('/home/rubgarfue/Escritorio/TFG-Informatica/matrix/dist_mat.csv') as f:
        lines = f.readlines()

    for line in lines:
        dist_mat.append([float(x) for x in line.split(',')])          

    # Cálculo del diagrama de barras

    persistence = di.persistence_diagram(dist_mat)

    with open('/home/rubgarfue/Escritorio/TFG-Informatica/output/persistence/persistence.txt', 'w') as f:
        for p in persistence:
            f.write(str(p) + '\n')
    
    '''
    users = sql.users(reduced_db_engine)
    for i in range(104,len(users)+1):
        print('Diagram: ' + str(i) + '/' + str(len(users)))
        with open('/home/rubgarfue/Escritorio/TFG-Informatica/matrix/dist_mat.csv') as f:
            lines = f.readlines()
        dist_mat_1 = []
        for j in range(i):
            dist_mat_1.append([float(x) for x in lines[j].split(',')[:i]])
            dist_mat_2 = [vector[:j+1] for vector in dist_mat[:i]]
        barcode = di.barcode_diagram(dist_mat_1, True, 'reduced_b_' + str(i) + '.png')
        persistence = di.persistence_diagram(dist_mat_2, True, 'reduced_p_' + str(i) + '.png')
    '''
    
    '''
    barcode = di.barcode_diagram(reduced_db_engine, None, True, 'phpmyadmin.png')

    bar_0 = []
    bar_1 = []
    bar_2 = []

    for b in barcode:
        if b[0] == 0:
            bar_0.append(b[1])
        elif b[0] == 1:
            bar_1.append(b[1])
        elif b[0] == 2:
            bar_2.append(b[1])
    
    with open('barcode_phpmyadmin.txt', 'w') as f:
        f.write("Dimension 0:\n")
        for bar in bar_0:
            f.write("\t" + str(bar) + '\n')
        f.write("Dimension 1:\n")
        for bar in bar_1:
            f.write("\t" + str(bar) + '\n')
        f.write("Dimension 2:\n")
        for bar in bar_2:
            f.write("\t" + str(bar) + '\n')
    '''

if __name__ == '__main__':
    main()