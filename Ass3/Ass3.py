import multiprocessing

# Function to calculate dot product of a row and a column
def matrix_multiply_mapper(row, column):
    result = 0
    for i in range(len(row)):
        result = result+ row[i] * column[i]
        print("Row:", row, "Column:", column, "Result:", result)
        print("End of iteration")
    return result

# Worker function for multiprocessing
def matrix_multiply_worker(arguments):
    row_index = arguments[0]
    row = arguments[1]
    all_columns = arguments[2]

    row_result = []
    for column_index in range(len(all_columns)):
        column = all_columns[column_index]
        value = matrix_multiply_mapper(row, column)
        row_result.append((row_index, column_index, value))
    
    return row_result

# Reducer function to combine all results into a final matrix
def matrix_multiply_reduce(results):
    final_result = {}
    for item in results:
        row_index = item[0]
        column_index = item[1]
        value = item[2]

        if row_index not in final_result:
            final_result[row_index] = {}
        
        final_result[row_index][column_index] = value
    
    return final_result

# Main function that runs the map-reduce matrix multiplication
def map_reduce_matrix_multiply(matrix1, matrix2):
    number_of_cpus = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=number_of_cpus)

    # Transpose matrix2 so we can access its columns as rows
    transposed_matrix2 = []
    print("Transposing matrix2", matrix2)
    for j in range(len(matrix2[0])):
        column = []
        for i in range(len(matrix2)):
            column.append(matrix2[i][j])
        transposed_matrix2.append(column)
    print("Transposed matrix2", transposed_matrix2)
    # Print the transposed matrix2
    # Prepare arguments for each row
    args = []
    #len(matrixx1) will give number of rows in matrix1
    for i in range(len(matrix1)):
        row = matrix1[i]
        args.append((i, row, transposed_matrix2))
    print("Arguments for worker function", args)

    # Run worker function in parallel
    intermediate_results = pool.map(matrix_multiply_worker, args)
    print("Intermediate results from worker function", intermediate_results)

    pool.close()
    pool.join()

    # Flatten the list of lists into a single list
    flat_results = []
    for sublist in intermediate_results:
        for item in sublist:
            flat_results.append(item)

    # Reduce phase to construct final matrix
    final_result = matrix_multiply_reduce(flat_results)

    return final_result

# Main execution block
if __name__ == '__main__':
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        
    ]

    matrix2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    result = map_reduce_matrix_multiply(matrix1, matrix2)

    # Display final matrix
    for row_index in sorted(result.keys()):
        row_data = result[row_index]
        row_output = []
        for column_index in sorted(row_data.keys()):
            row_output.append(row_data[column_index])
        print(row_output)
