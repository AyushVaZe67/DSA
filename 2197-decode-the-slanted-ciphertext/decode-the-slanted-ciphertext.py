class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText
        
        n = len(encodedText)
        cols = n // rows
        
        # Create matrix and fill row by row
        matrix = []
        for i in range(rows):
            row = list(encodedText[i * cols : (i + 1) * cols])
            matrix.append(row)
        
        # Read diagonally
        result = []
        for start_col in range(cols):
            r, c = 0, start_col
            while r < rows and c < cols:
                result.append(matrix[r][c])
                r += 1
                c += 1
        
        # Join and remove trailing spaces
        return ''.join(result).rstrip()