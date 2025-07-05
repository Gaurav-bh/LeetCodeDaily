class Solution {
    HashSet<Integer> isTravelNeeded = new HashSet<>();

    private int solve(int[] dp, int lastDay, int[] costs, int currDay) {
        // If we have iterated over travel days, return 0.
        if (currDay > lastDay) {
            return 0;
        }

        // If we don't need to travel on this day, move on to next day.
        if (!isTravelNeeded.contains(currDay)) {
            return solve(dp, lastDay, costs, currDay + 1);
        }

        // If already calculated, return from here with the stored answer.
        if (dp[currDay] != -1) {
            return dp[currDay];
        }

        int oneDay = costs[0] + solve(dp, lastDay, costs, currDay + 1);
        int sevenDay = costs[1] + solve(dp, lastDay, costs, currDay + 7);
        int thirtyDay = costs[2] + solve(dp, lastDay, costs, currDay + 30);

        // Store the cost with the minimum of the three options.
        return dp[currDay] = Math.min(oneDay, Math.min(sevenDay, thirtyDay));
    }

    public int mincostTickets(int[] days, int[] costs) {
        // The last day on which we need to travel.
        int lastDay = days[days.length - 1];
        int dp[] = new int[lastDay + 1];
        Arrays.fill(dp, -1);

        // Mark the days on which we need to travel.
        for (int day : days) {
            isTravelNeeded.add(day);
        }

        return solve(dp, lastDay, costs, 1);
    }
}