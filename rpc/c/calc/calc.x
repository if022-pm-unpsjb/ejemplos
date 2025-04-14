/* Definición de la interfaz RPC */
program CALC_PROG {
    version CALC_VERS {
        int ADD(intpair) = 1;
        int SUB(intpair) = 2;
    } = 1;
} = 0x31230000;

struct intpair {
    int a;
    int b;
};
