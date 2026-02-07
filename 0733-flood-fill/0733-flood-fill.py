class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:
            return []

        rows, cols = len(image), len(image[0])

        def dfs(r, c, Scolor):
            if r >= rows or r < 0 or c >= cols or c < 0 or image[r][c] == color or image[r][c] != Scolor:
                return
            image[r][c] = color
            dfs(r,c-1, Scolor)
            dfs(r-1,c, Scolor)
            dfs(r,c+1, Scolor)
            dfs(r+1,c, Scolor)

        if image[sr][sc] == color:
            return image
        storeColor = image[sr][sc]
        dfs(sr, sc, storeColor)
        return image
        