#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

#define N 4 // Tamaño de las matrices (N x N)

void print_matrix(int matrix[N][N], const char* name) {
    printf("Matriz %s:\n", name);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%d\t", matrix[i][j]);
        }
        printf("\n");
    }
}

int main(int argc, char** argv) {
    int rank, size;
    int a[N][N], b[N][N], c[N][N];
    int rows_per_proc, start_row, end_row;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    if (N % size != 0) {
        if (rank == 0) {
            printf("Error: El número de procesos debe dividir N.\n");
        }
        MPI_Finalize();
        return 1;
    }

    rows_per_proc = N / size;
    start_row = rank * rows_per_proc;
    end_row = start_row + rows_per_proc;

    // Inicializar matrices A y B solo en el proceso raíz
    if (rank == 0) {
        printf("Inicializando matrices...\n");
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                a[i][j] = i + j;
                b[i][j] = i + j;
                c[i][j] = 0;
            }
        }
        print_matrix(a, "A");
        print_matrix(b, "B");
    }

    // Distribuir filas de la matriz A
    MPI_Bcast(b, N * N, MPI_INT, 0, MPI_COMM_WORLD);
    MPI_Scatter(a, N * rows_per_proc, MPI_INT, a[start_row], N * rows_per_proc, MPI_INT, 0, MPI_COMM_WORLD);

    // Cada proceso calcula su parte del resultado
    for (int i = start_row; i < end_row; i++) {
        for (int j = 0; j < N; j++) {
            c[i][j] = 0;
            for (int k = 0; k < N; k++) {
                c[i][j] += a[i][k] * b[k][j];
            }
        }
    }

    // Recolectar resultados en el proceso raíz
    MPI_Gather(c[start_row], N * rows_per_proc, MPI_INT, c, N * rows_per_proc, MPI_INT, 0, MPI_COMM_WORLD);

    if (rank == 0) {
        printf("\nResultado de la multiplicación de matrices:\n");
        print_matrix(c, "C");
    }

    MPI_Finalize();
    return 0;
}
