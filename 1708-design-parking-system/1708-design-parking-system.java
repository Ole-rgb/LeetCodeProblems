class ParkingSystem {
    private int freeBig;
    private int freeMedium;
    private int freeSmall;
    

    public ParkingSystem(int big, int medium, int small) {
        this.freeBig = big;
        this.freeMedium = medium;
        this.freeSmall = small;
    }
    
    public boolean addCar(int carType) {
        if(carType == 3){
            //small car
            if(freeSmall -1 >= 0){
                freeSmall = freeSmall- 1;
                return true;
            }
        }
        else if(carType == 2){
            //medium car
            if(freeMedium -1 >= 0){
                freeMedium = freeMedium - 1;
                return true;
            }
        }
        else if(carType == 1){
            //big car
            if(freeBig -1 >= 0){
                freeBig = freeBig - 1;
                return true;
            }
        }
        return false;
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem obj = new ParkingSystem(big, medium, small);
 * boolean param_1 = obj.addCar(carType);
 */