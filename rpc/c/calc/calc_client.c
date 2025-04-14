#include "calc.h"

void calc_prog_1(char *host, int a, int b) {
    CLIENT *clnt;
    intpair pair;
    int *result;

    clnt = clnt_create(host, CALC_PROG, CALC_VERS, "udp");
    if (clnt == NULL) {
        clnt_pcreateerror(host);
        exit(1);
    }

    pair.a = a;
    pair.b = b;

    // Llamada RPC para suma
    result = add_1(&pair, clnt);
    if (result == NULL) {
        clnt_perror(clnt, "Error en la llamada RPC");
    } else {
        printf("Resultado de ADD(%d, %d): %d\n", a, b, *result);
    }

    // Llamada RPC para resta
    result = sub_1(&pair, clnt);
    if (result == NULL) {
        clnt_perror(clnt, "Error en la llamada RPC");
    } else {
        printf("Resultado de SUB(%d, %d): %d\n", a, b, *result);
    }

    clnt_destroy(clnt);
}

int main(int argc, char *argv[]) {
    char *host;

    if (argc < 2) {
        printf("Uso: %s <hostname> operando1 operando2\n", argv[0]);
        exit(1);
    }
    host = argv[1];
    calc_prog_1(host, atoi(argv[2]), atoi(argv[3]));
    exit(0);
}
