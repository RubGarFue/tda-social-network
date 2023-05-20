import sql.sql_backend as sql
import persistence.diagrams as di
import time


def main():

    repeat = 20

    # Times for prueba_db
    prueba_engine = sql.get_engine('prueba')

    times = []
    for _ in range(repeat):
        start = time.time()
        di.adjacency_matrix(prueba_engine)
        end = time.time()
        times.append(end - start)
    
    print('Time adjacency_matrix for prueba: ', sum(times)/len(times))

    times = []
    for _ in range(repeat):
        start = time.time()
        di.fast_adjacency_matrix(prueba_engine)
        end = time.time()
        times.append(end - start)

    print('Time fast_adjacency_matrix for prueba: ', sum(times)/len(times))

    times = []
    for _ in range(repeat):
        start = time.time()
        di.lower_adjacency_matrix(prueba_engine)
        end = time.time()
        times.append(end - start)
    
    print('Time lower_adjacency_matrix for prueba: ', sum(times)/len(times))
    print('')
    
    # Times for test_high_index
    hindex_engine = sql.get_engine('test_high_index')

    times = []
    for _ in range(repeat):
        start = time.time()
        di.adjacency_matrix(hindex_engine)
        end = time.time()
        times.append(end - start)
    
    print('Time adjacency_matrix for test_high_index: ', sum(times)/len(times))

    times = []
    for _ in range(repeat):
        start = time.time()
        di.fast_adjacency_matrix(hindex_engine)
        end = time.time()
        times.append(end - start)

    print('Time fast_adjacency_matrix for test_high_index: ', sum(times)/len(times))

    times = []
    for _ in range(repeat):
        start = time.time()
        di.lower_adjacency_matrix(hindex_engine)
        end = time.time()
        times.append(end - start)

    print('Time lower_adjacency_matrix for test_high_index: ', sum(times)/len(times))
    print('')

    # Times for test_low_index
    lindex_engine = sql.get_engine('test_low_index')

    times = []
    for _ in range(repeat):
        start = time.time()
        di.adjacency_matrix(lindex_engine)
        end = time.time()
        times.append(end - start)

    print('Time adjacency_matrix for test_low_index: ', sum(times)/len(times))

    times = []
    for _ in range(repeat):
        start = time.time()
        di.fast_adjacency_matrix(lindex_engine)
        end = time.time()
        times.append(end - start)

    print('Time fast_adjacency_matrix for test_low_index: ', sum(times)/len(times))

    times = []
    for _ in range(repeat):
        start = time.time()
        di.lower_adjacency_matrix(lindex_engine)
        end = time.time()
        times.append(end - start)

    print('Time lower_adjacency_matrix for test_low_index: ', sum(times)/len(times))


if __name__ == '__main__':
    main()