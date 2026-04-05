from fastapi import FastAPI

app = FastAPI()

@app.get("/info")
def get_info(topic: str):

    return {
        "topic": topic,
        "content": f"{topic} is an important concept used in real-world applications and technology.",
        "points": [
        f"What is {topic}?",
        f"Key Ideas Behind {topic}",
        f"How {topic} Works",
        f"Where {topic} is Used",
        f"Benefits of {topic}",
        f"Challenges of {topic}"
        ]
    }