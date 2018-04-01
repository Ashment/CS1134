import ArrayQueue

q = ArrayQueue.BoostQueue();
q.enqueue(1);
q.enqueue(2);
print(q)
q.enqueue(3);
q.enqueue(4);
print(q)
q.enqueue(5);
q.enqueue(6);
print(q)


# Deque Testing #########
#print(q.first());
#print(q.last());

#q.add_first(100);
#q.add_last(1000);
#print(q)

#########################

## Boost Queue ##########
q.enqueue(100);
print(q)
q.boost(3);
print(q);
q.boost(7);