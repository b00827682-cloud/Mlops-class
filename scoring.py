

def score(x: float) -> dict:
    y = 2 * x + 1
    return {"input": x, "score": y}

if __name__ == "__main__":
    print(score(3))
