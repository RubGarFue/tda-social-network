import sql.sql_backend as sql
import src.distance.distances as dj
import distance.pagerank as pr
import persistence.diagrams as di
import similarity.similarity as sim
import time


def main():
    # Barcode of prueba_db
    prueba_engine = sql.get_engine('prueba')
    prueba_bar = di.barcode_diagram(prueba_engine, True, 'new_barcode_prueba.png')
    print('Barcode printed as barcode_prueba.png\n')
    
    # Graph and barcode of test_high_index
    hindex_engine = sql.get_engine('test_high_index')
    hindex_bar = di.barcode_diagram(hindex_engine, True, 'new_barcode_high_index.png')
    print('Barcode printed as barcode_high_index.png\n')

    # Graph and barcode of test_low_index
    lindex_engine = sql.get_engine('test_low_index')
    lindex_bar = di.barcode_diagram(lindex_engine, True, 'new_barcode_low_index.png')
    print('Barcode printed as barcode_low_index.png\n\n')

    # Print similarity
    print('Similarity between prueba_db and test_high_index: ' + str(sim.similarity(prueba_bar, hindex_bar)))
    print('Similarity between prueba_db and test_low_index: ' + str(sim.similarity(prueba_bar, lindex_bar)))

    print('Similarity between prueba_db and prueba_db: ' + str(sim.similarity(prueba_bar, prueba_bar)))
    print('Similarity between test_low_index and test_low_index: ' + str(sim.similarity(lindex_bar, lindex_bar)))
    print('Similarity between test_high_index and test_high_index: ' + str(sim.similarity(hindex_bar, hindex_bar)))

    # Barcode of phpmyadmin
    #phpmyadmin_bar = di.barcode_diagram(phpmyadmin_engine, True, 'barcode_phpmyadmin.png')


if __name__ == '__main__':
    main()