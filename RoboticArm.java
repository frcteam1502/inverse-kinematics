class RoboticArm{
    int[] origin;
    int[] armPosition = {0,0};
    int[] foreArmPosition = {0,0};
    int armLength = 300;
    int foreArmLength = 200;
    int min = armLength - foreArmLength;
    int max = armLength + foreArmLength;
    public RoboticArm(int[] origin) {
        this.origin = origin;
    }

    public void run(int[] pos) {
        int distance = Math.sqrt(endPosition[0] * endPosition[0] + endPosition[1] * endPosition[1]);
        int distMultiple;
        if (distace > max) distMultiplier = max / distance;
        if (distace < min) distMultiplier = min / distance;
        distance *= distMultiple;
        int[] endPosition = {pos[0] * distMultiple, pos[1] * distMultiple};
        try {
            int a1 = Math.atan2(endPosition[1], endPosition[0]);
            int secondAngle = Math.asin((endPosition[1] * endPosition[1] + endPosition[0] * endPosition[0] - armLength * armLength - foreArmLength * foreArmLength) / 2 / armLength / foreArmLength);
            int a2 = Math.asin(foreArmLength * Math.cos(secondAngle) / distance);
            int firstAngle = a1 + a2;
            int[] elbow = {armLength * Math.cos(firstAngle), armLength * Math.sin(firstAngle)};
        }
        catch(ArithmeticException e) {
            System.out.print(e);
        }
        System.out.print(firstAngle + ", " + secondAngle);
    }
}
