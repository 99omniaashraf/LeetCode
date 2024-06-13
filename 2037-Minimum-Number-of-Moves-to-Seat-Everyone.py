class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        # Sort the seats and students arrays
        seats.sort()
        students.sort()
        
        # Initialize moves to track total moves
        moves = 0
        
        # Iterate through each student
        for i in range(len(students)):
            # Find the closest seat that is not occupied
            seat = seats[i]
            student = students[i]
            
            # Update student position and increment moves
            moves += abs(seat - student)
        
        # Return the total moves
        return moves        