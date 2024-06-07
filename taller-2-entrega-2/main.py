import sqlite3
import numpy as np
from marine_predators_algorithm import MarinePredatorsAlgorithm
from cec2013_functions import CEC2013LSGO

def main():
    # Parámetros de optimización
    dim = 1000
    population_size = 50
    max_iter = 5000
    lower_bound = -100
    upper_bound = 100
    num_executions = 31

    # Crear instancia de las funciones CEC2013
    cec2013 = CEC2013LSGO(dim)

    # Lista de funciones de prueba
    functions = [
        cec2013.shifted_bent_cigar,
        cec2013.shifted_sum_of_different_power,
        cec2013.shifted_zakharov,
        cec2013.shifted_rosenbrock,
        cec2013.shifted_rotated_rosenbrock,
        cec2013.shifted_rastrigin,
        cec2013.shifted_rotated_rastrigin,
        cec2013.shifted_non_continuous_rastrigin,
        cec2013.shifted_schwefel,
        cec2013.shifted_rotated_schwefel,
        cec2013.shifted_elliptic,
        cec2013.shifted_rotated_elliptic,
        cec2013.shifted_ackley,
        cec2013.shifted_rotated_ackley,
        cec2013.shifted_schwefel_1_2
    ]

    # Conectar a la base de datos (ajustar la ruta según tu sistema)
    conn = sqlite3.connect(r'C:\Users\rorov\PycharmProjects\taller-2-entrega-2\bd_ddyaadaa.db')
    cursor = conn.cursor()

    for func_index, func in enumerate(functions, start=1):
        print(f"\nRunning MPA on Function f{func_index}")
        for exec_index in range(num_executions):
            print(f"Execution {exec_index+1}")
            mpa = MarinePredatorsAlgorithm(func, dim, population_size, max_iter, lower_bound, upper_bound)
            best_solution, best_fitness = mpa.optimize()
            print(f"Best Solution for f{func_index} - Execution {exec_index+1}: {best_solution}")
            print(f"Best Fitness for f{func_index} - Execution {exec_index+1}: {best_fitness}")

            # Insertar resultados en la base de datos
    cursor.execute('''
      INSERT INTO registros_mh_ceclsgo (
         id_grupo, mh_nombre, num_ejecucion, num_iteracion, num_soluciones, seed, fitness, tiempo_ms,
            cec_funcion, cec_bks, cec_upper, cec_lower, cec_dimension, mh_param_1, mh_param_1_des,
         mh_param_2, mh_param_2_des, mh_param_3, mh_param_3_des, mh_param_4, mh_param_4_des,
         mh_param_5, mh_param_5_des, mh_param_6, mh_param_6_des, mh_param_7, mh_param_7_des,
              mh_param_8, mh_param_8_des
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', (
    11, 'Marine Predators Algorithm', exec_index + 1, max_iter, population_size, np.random.randint(0, 1000000),
    best_fitness, '1000', func_index, 0.0, upper_bound, lower_bound, dim, 0.5, 'Parametro 1',
    0.5, 'Parametro 2', None, None, None, None, None, None, None, None, None, None, None, None
))
    conn.commit()


# Cerrar la conexión a la base de datos
    conn.close()

if __name__ == "__main__":
    main()
