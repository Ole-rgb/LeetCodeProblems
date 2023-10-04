class MyHashMap {
    private List<Entry> entries;

    public MyHashMap() {
        this.entries = new ArrayList<>();
    }
    
    public void put(int key, int value) {
        for(Entry entry : entries){
            if(key == entry.key){
                entry.value = value;
                return;
            }
        }
        entries.add(new Entry(key, value));

    }
    
    public int get(int key) {
        for(Entry entry : entries){
            if(key == entry.key){
                return entry.value;
            }
        }
        return -1;
    }
    
    public void remove(int key) {
        for(Entry entry : entries){
            if(key == entry.key){
                entries.remove(entry);
                return ;
            }
        }
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