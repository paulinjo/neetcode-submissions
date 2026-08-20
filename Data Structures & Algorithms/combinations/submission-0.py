class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        def compute(i: int, current_combination: list[int]):
            nonlocal results

            if len(current_combination) == k:
                results.append(current_combination)
                return

            for j in range(i+1, n+1):
                print(f"{i=} | {j=}")
                compute(j, current_combination + [j])
        
        compute(0, [])
        return results