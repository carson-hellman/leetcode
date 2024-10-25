"""
Remove Sub-Folders from the Filesystem (Medium)
Solved in O(n log n) time complexity and O(n) space complexity
"""

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        output = [folder[0]]
        for path in folder[1:]:
            # check if not subfolder
            if not path.startswith(output[-1]+"/"):
                output.append(path)

        return output
