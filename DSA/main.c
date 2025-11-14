#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "include/delivery.h"

void clear(void) { system("clear||cls"); }
void pause(void) { printf("Press Enter to continue..."); getchar(); }

static int randu(int min, int max) {
    return min + rand() % (max - min + 1);
}

void findAR(Platform *p) {
    if (!p || !p->in_transit || !p->in_transit->root) {
        printf("No deliveries in transit.\n");
        return;
    }
    int eta = p->in_transit->root->data.eta;
    int eta2=randu(10,100);
    printf("path One ETA: %d min\n", eta);
    printf("path Two ETA: %d min\n", eta2);
    if(eta<eta2){
      printf("Path One is form fast");
    }
    else {
      printf("Path Two is form fast"); 
    }
}
int main(void) {
    Platform *plat = init_platform();
    if (!plat) { perror("init"); return EXIT_FAILURE; }

    int choice;
    do {
        clear();
        printf("\033[1;36m=== Food Delivery Platform ===\033[0m\n");
        printf("1. Place Order\n");
        printf("2. Prepare Next Order\n");
        printf("3. Assign Delivery Agent\n");
        printf("4. Track Order\n");
        printf("5. Generate Report\n");
        printf("0. Exit\n");
        printf("> ");
        if (scanf("%d", &choice) != 1) { while(getchar()!='\n'); choice = -1; }
        while(getchar()!='\n'); /* flush */

        switch (choice) {
            case 1: {
                char rest[32], cust[32];
                int  mins;
                printf("Restaurant: "); fgets(rest, sizeof(rest), stdin); rest[strcspn(rest,"\n")] = 0;
                printf("Customer:   "); fgets(cust, sizeof(cust), stdin); cust[strcspn(cust,"\n")] = 0;
                printf("Prep time (min): "); scanf("%d", &mins);
                place_order(plat, rest, cust, mins);
                break;
            }
            case 2: prepareOrder(plat);           break;
            case 3: assignDeliveryAgent(plat);    break;
            case 6: findAR(plat);
            case 4: {
                      int id;
                      printf("Order ID: ");
                      if (scanf("%d", &id) != 1) {      // handle invalid input
                        printf("Invalid ID!\n");
                        while(getchar()!='\n');       // clear buffer
                        break;
                      }
    while(getchar()!='\n');           // flush leftover '\n'
    trackOrder(plat, id);
    break;
}
            case 5: generateReport(plat);         break;
            case 0: printf("Good-bye!\n");        break;
            default: printf("Invalid option.\n"); break;
        }
        if (choice != 0) pause();
    } while (choice != 0);

    destroy_platform(plat);
    return EXIT_SUCCESS;
}
