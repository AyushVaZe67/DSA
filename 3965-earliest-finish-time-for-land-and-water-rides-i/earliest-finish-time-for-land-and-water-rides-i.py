from typing import List

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], 
                          waterStartTime: List[int], waterDuration: List[int]) -> int:
        earliest_time = float('inf')
        
        # Try all combinations of land and water rides
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                # Order 1: Land first, then water
                land_ride_finish = max(landStartTime[i], 0) + landDuration[i]
                water_ride_finish = max(waterStartTime[j], land_ride_finish) + waterDuration[j]
                earliest_time = min(earliest_time, water_ride_finish)
                
                # Order 2: Water first, then land
                water_ride_finish = max(waterStartTime[j], 0) + waterDuration[j]
                land_ride_finish = max(landStartTime[i], water_ride_finish) + landDuration[i]
                earliest_time = min(earliest_time, land_ride_finish)
        
        return earliest_time