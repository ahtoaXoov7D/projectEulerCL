#include <sll.h>


/** Return an initialized object so the user can avoid calling
 *  sll_init() himself and instead initialize by copying 
 *  from an already initialized object
 */
sll_t
sll_lib_initialized_object(void)
{
	static int _initialized = 0;

	/** 
	 * Perform initialization only on the first run
	 * Subsequent runs, just return a copy of the already initialized object 
	 */
	if (!_initialized) {
		_initialized = 1;
		sll_init(&_sll_lib_initialized_sll_object);
	}

	return _sll_lib_initialized_sll_object;
}

/** Initialize Singly Linked List */
void 
sll_init (sll_t *sll)
{
	if (!sll)
		return;

	sll->head = sll->tail = NULL;
	sll->_size = 0;
}


/** Return size of the SLL */
int 
sll_length (sll_t *sll)
{
	if (!sll)
		return -1;

	return sll->_size;
}



