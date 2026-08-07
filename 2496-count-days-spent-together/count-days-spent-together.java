class Solution {
    public int countDaysTogether(String arriveAlice, String leaveAlice, String arriveBob, String leaveBob) {
        int[] daysInMonth = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

        // Convert all dates to absolute day numbers of the year (1 - 365)
        int startA = dateToDayOfYear(arriveAlice, daysInMonth);
        int endA = dateToDayOfYear(leaveAlice, daysInMonth);
        int startB = dateToDayOfYear(arriveBob, daysInMonth);
        int endB = dateToDayOfYear(leaveBob, daysInMonth);

        // Overlap starts at the latest arrival and ends at the earliest departure
        int overlapStart = Math.max(startA, startB);
        int overlapEnd = Math.min(endA, endB);

        // If end date is before start date, there is no overlap
        return Math.max(0, overlapEnd - overlapStart + 1);
    }

    private int dateToDayOfYear(String dateStr, int[] daysInMonth) {
        int month = Integer.parseInt(dateStr.substring(0, 2));
        int day = Integer.parseInt(dateStr.substring(3, 5));
        
        int dayCount = 0;
        for (int i = 0; i < month - 1; i++) {
            dayCount += daysInMonth[i];
        }
        return dayCount + day;
    }
}