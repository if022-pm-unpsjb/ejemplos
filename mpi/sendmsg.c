#include <stdio.h>
#include <mpi.h>

int main(int argc, char** argv) {
    int rank, size;
    char message[100];
    MPI_Status status;

    // Initialize the MPI environment
    MPI_Init(&argc, &argv);

    // Get the number of processes
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    // Get the rank of the process
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    // Each process prints a message
    sprintf(message, "Hello from process %d of %d", rank, size);
    printf("%s\n", message);

    // The root process (rank 0) receives messages from all others
    if (rank == 0) {
        printf("\nRoot process (rank 0) is receiving messages...\n");
        for (int i = 1; i < size; i++) {
            MPI_Recv(message, 100, MPI_CHAR, i, 0, MPI_COMM_WORLD, &status);
            printf("Received: %s\n", message);
        }
    } else {
        // Other processes send their message to the root
        MPI_Send(message, 100, MPI_CHAR, 0, 0, MPI_COMM_WORLD);
    }

    // Finalize the MPI environment
    MPI_Finalize();

    return 0;
}
