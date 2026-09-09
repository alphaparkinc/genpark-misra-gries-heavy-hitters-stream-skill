from client import MisraGriesSketch

def main():
    print("=== Misra-Gries Heavy Hitters Sketch ===")
    sketch = MisraGriesSketch()
    data = ["alpha"] * 60 + ["beta"] * 30 + ["gamma"] * 5 + ["delta"] * 2
    res = sketch.find_heavy_hitters(data, k=3)
    print("Heavy Hitters Output:", res)
    assert "alpha" in res["heavy_hitters"]

    print("Misra-Gries Sketch verified successfully!")

if __name__ == "__main__":
    main()
