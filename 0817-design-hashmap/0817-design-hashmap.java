class MyHashMap {
    private static final int SIZE = 1000;
    private LinkedList<Entry>[] buckets;

    public MyHashMap() {
        this.buckets = new LinkedList[SIZE];
        for(int i = 0; i < SIZE; i++){
            buckets[i] = new LinkedList<Entry>();
        }
    }
    
    public void put(int key, int value) {
        int index = hash(key);
        LinkedList<Entry> bucket = buckets[index];

        for(Entry entry : bucket){
            if(key == entry.key){
                entry.value = value;
                return;
            }
        }
        bucket.add(new Entry(key, value));

    }
    
    public int get(int key) {
        int index = hash(key);
        LinkedList<Entry> bucket = buckets[index];

        for(Entry entry : bucket){
            if(key == entry.key){
                return entry.value;
            }
        }
        return -1;
    }
    
    public void remove(int key) {
        int index = hash(key);
        LinkedList<Entry> bucket = buckets[index];

        for(Entry entry : bucket){
            if(key == entry.key){
                bucket.remove(entry);
                return ;
            }
        }
    }

    private int hash(int key){
        return key % SIZE;
    }
}

class Entry{
    int key;
    int value;

    public Entry(int key, int value){
        this.key = key;
        this.value = value;
    }

}
/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */