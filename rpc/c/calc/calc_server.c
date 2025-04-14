#include "calc.h"

int *add_1_svc(intpair *argp, struct svc_req *rqstp) {
    static int result;
    printf("Me piden calcular: %d + %d\n", argp->a, argp->b);
    result = argp->a + argp->b;
    return &result;
}

int *sub_1_svc(intpair *argp, struct svc_req *rqstp) {
    static int result;
    result = argp->a - argp->b;
    printf("Me piden calcular: %d - %d\n", argp->a, argp->b);
    return &result;
}
