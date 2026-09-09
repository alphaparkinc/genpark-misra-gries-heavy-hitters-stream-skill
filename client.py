class MisraGriesSketch:
    """Misra-Gries frequency estimator."""
    def find_heavy_hitters(self, stream: list[str], k: int) -> dict:
        counters = {}
        for item in stream:
            if item in counters:
                counters[item] += 1
            elif len(counters) < k - 1:
                counters[item] = 1
            else:
                for key in list(counters.keys()):
                    counters[key] -= 1
                    if counters[key] == 0:
                        del counters[key]

        return {
            "k_threshold": k,
            "heavy_hitters": counters
        }
