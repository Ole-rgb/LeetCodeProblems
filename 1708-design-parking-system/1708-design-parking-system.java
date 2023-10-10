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
        if((carType == 1  & freeBig==0)|| (carType == 2  & freeMedium==0)||(carType == 3 & freeSmall == 0)){
            return false;
        }

        if(carType == 1) freeBig--;
        if(carType == 2) freeMedium--;
        if(carType == 3) freeSmall--;
        return true;
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem obj = new ParkingSystem(big, medium, small);
 * boolean param_1 = obj.addCar(carType);
 */