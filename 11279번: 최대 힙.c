#include <stdio.h>
#include <stdlib.h>
#define MAX_ELEMENT 100005

typedef struct
{
    int key;
} element;

typedef struct {
    element heap[MAX_ELEMENT];
    int heap_size;
} HeapType;

HeapType* create()
{
    return (HeapType*)malloc(sizeof(HeapType));
}

void init(HeapType *h)
{
    h->heap_size = 0;
}

void insert_heap (HeapType *h, element item)
{
    int index = ++(h->heap_size);

    while((index != 1) && (item.key > h->heap[index / 2].key))
    {
        h->heap[index] = h->heap[index / 2];
        index /= 2;
    }
    h->heap[index] = item;
}

element delete_heap(HeapType *h)
{
    int parent, child;
    element item, temp;

    if(!h->heap_size)
    {
        item.key = 0;
        return item;
    }

    item = h->heap[1];
    temp = h->heap[(h->heap_size)--];
    parent = 1; child = 2;

    while(child <= h->heap_size)
    {
        if((child < h->heap_size) && (h->heap[child].key) < h->heap[child + 1].key)
            child++;
        if(temp.key >= h->heap[child].key)
            break;
        h->heap[parent] = h->heap[child];
        parent = child;
        child *= 2;
    }

    h->heap[parent] = temp;
    return item;
}

int main()
{
    HeapType* heap;
    heap = create();
    init(heap);

    element item;
    element temp;

    int N; scanf("%d", &N);


    for(int i = 0; i < N; i++)
    {
        scanf("%d", &item.key);
        if(item.key)
            insert_heap(heap, item);
        else
        {
            temp = delete_heap(heap);
            printf("%d\n", temp.key);
        }
    }

    return 0;
}
