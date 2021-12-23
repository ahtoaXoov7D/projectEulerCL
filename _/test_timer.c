#include <threaded_timer.h>

void threaded_timer_fn(void *args)
{
	static int i = 1;

	int currtime = time(NULL);
	printf("%d Timer: %d\n", currtime, i++);
}

int main(void)
{
	/** Recur thrice at intervals of 10s */
	threaded_timer_t *timer = set_timer(10, 1, 3, 5, threaded_timer_fn, (void *)1);

	start_timer(timer);

	pthread_join(timer->thread, NULL);

	printf("Exiting\n");

	return 0;
}
