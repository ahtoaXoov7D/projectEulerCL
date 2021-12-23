#ifndef __TEST_STRUCT_H_
#define __TEST_STRUCT_H_

/** Test structure to test data structures */

struct test_struct {
	int tsi;
	char tsc;
};

int compareIntKey (void *obj1, int idx1, void *obj2, int idx2);
int compareCharKey (void *obj1, int idx1, void *obj2, int idx2);
int compareStruct (void *obj1, int idx1, void *obj2, int idx2);

#endif  /** __TEST_STRUCT_H_ */

