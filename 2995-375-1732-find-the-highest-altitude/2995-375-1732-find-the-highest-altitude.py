class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = [0]

        for i in range(0, len(gain)):
            curr_alti = altitude[i] + gain[i]
            altitude.append(curr_alti)
        
        return max(altitude)