#include <cstdlib>
#include <cstdio>
#include <ctime>
#include <random>

/**
 * Instrumented bubble sort code. For given array size n, executes bubble sort
 * in the best / worst / average situation, counts the number of operations 
 * executed, and repeats for k trials. Ultimately outputs n, k, and avg. number
 * of operations required to sort.
 */

// global PRNG object
std::mt19937_64 prng(time(0));

/**
 * @brief Instrumented bubble sort. 
 * 
 * @param pArr array to sort.
 * @param n size of the array.
 * @return Number of operations executed during the algorithm.
 */
size_t bubbleSort(size_t *pArr, size_t n) {
    size_t numOps = 0;
    size_t t;
    bool swapped;
    do {
        swapped = false;
        numOps += 2;
        for(size_t i = 1; i < n; i++) {
            numOps++;
            if(pArr[i - 1] > pArr[i]) {
                t = pArr[i - 1];
                pArr[i - 1] = pArr[i];
                pArr[i] = t;
                swapped = true;
                numOps += 5;
            } else {
                numOps++;
            }
            numOps++;
        }
        numOps++;
    } while(swapped);

    return numOps;
}

/**
 * @brief Randomly shuffle an array.
 *
 * @param pArr array to shuffle.
 * @param n size of the array.
 */
void shuffle(size_t *pArr, size_t n) {
    std::uniform_int_distribution<size_t> dist(0, n - 1);
    for(size_t i = 0; i < n; i++) {
        size_t j = dist(prng);
        std::swap(pArr[i], pArr[j]);
    }
}

/**
 * @brief Fill array with best-case data for bubble sort.
 *
 * Fills the array with strictly increasing values, for the best-case situation
 * with our bubble sort.
 * 
 * @param pArr array to fill
 * @param n size of the array
 */
void bestCase(size_t *pArr, size_t n) {
    for(size_t i = 0; i < n; i++) {
        pArr[i] = i;
    }
}

/**
 * @brief Fill array with worst-case data for bubble sort.
 * 
 * Fills the array with strictly decreasing values, for the worst-case situation
 * with our bubble sort. 
 *
 * @param pArr arry to file
 * @param n size of the array
 */
void worstCase(size_t *pArr, size_t n) {
    for(size_t i = 0; i < n; i++) {
        pArr[i] = n - i - 1;
    }
}

/**
 * @brief Usage message for command-line arguments.
 */
void usage() {
    fprintf(stderr, "Usage: ./IBS <A|B|W> n k\n");
    fprintf(stderr, "\tFor A)verage, B)est, or W)orst case,\n");
    fprintf(stderr, "\tn is array size and k is number of trials.\n");
}

/**
 * Application entry point. Usage:
 *  ./IBS <A|B|W> n k
 *
 * for A)verage, B)est, or W)orst case, with array size n and k trials.
 */
int main(int argC, char** ppArgv) {
    // sanity check on command-line arguments
    if(argC != 4) {
        usage();
        return EXIT_FAILURE;
    }

    // convert numeric parameters
    size_t n = atoi(ppArgv[2]);
    size_t k = atoi(ppArgv[3]);

    // create and initiall fill array
    size_t* pArr = new size_t[n];
    for(size_t i = 0; i < n; i++) {
        pArr[i] = i;
    }

    size_t numOps = 0;

    // perform k trials
    for(size_t trial = 0; trial < k; trial++) {
        // prepare array for A|B|W case
        switch(ppArgv[1][0]) {
            case 'A':
                shuffle(pArr, n);
                break;
            case 'B':
                bestCase(pArr, n);
                break;
            case 'W':
                worstCase(pArr, n);
                break;
            default:
                usage();
                delete [] pArr;
                return EXIT_FAILURE;
        }

        // count how many ops we took
        numOps += bubbleSort(pArr, n);
    }

    // report average number of ops taken
    long double avgNumOps = numOps / (long double)k;
    printf("%lu\t%0.6Lf\n", n, avgNumOps);

    // exit gracefully
    delete [] pArr;
    return EXIT_SUCCESS;
}