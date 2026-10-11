
# AI Writing Assistant
# Using Groq API

from groq import generate_response


def get_essay_details():
    print("\n=== AI Writing Assistant ===\n")

    topic = input("What is the topic of your essay? ").strip()
    essay_type = input("What type of essay are you writing? ").strip()

    lengths = ["300 words", "900 words", "1200 words", "2000 words"]

    print("Select essay word count:")
    for i, length in enumerate(lengths, 1):
        print(f"{i}) {length}")

    try:
        choice = int(input("> ").strip())
        if 1 <= choice <= len(lengths):
            length = lengths[choice - 1]
        else:
            length = "300 words"
    except ValueError:
        length = "300 words"

    target_audience = input(
        "Target audience (e.g., High school students): "
    ).strip()

    return {
        "topic": topic,
        "essay_type": essay_type,
        "length": length,
        "target_audience": target_audience
    }


def generate_essay_content(details):
    try:
        temperature = float(
            input("Enter temperature (0.1 structured, 0.7 creative): ")
        )

        if not 0.0 <= temperature <= 1.0:
            raise ValueError

    except ValueError:
        print("Invalid temperature. Using 0.3.")
        temperature = 0.3

    topic = details["topic"]
    essay_type = details["essay_type"]
    length = details["length"]
    audience = details["target_audience"]

    # Generate introduction
    intro_prompt = (
        f"Write an introduction for a {essay_type} essay "
        f"about {topic}. The target audience is {audience}. "
        f"The complete essay length should be approximately {length}. "
        "Write only the introduction."
    )

    intro = generate_response(
        intro_prompt,
        temperature=temperature,
        max_tokens=1024
    )

    print("\n=== Generated Introduction ===\n")
    print(intro)

    # Choose body writing style
    print("\nWould you like the body written as a full draft or step-by-step?")
    print("1) Full draft")
    print("2) Step-by-step")

    choice = input("> ").strip()

    if choice == "1":
        body_prompt = (
            f"Write the body of a {essay_type} essay about {topic}. "
            f"Target audience: {audience}. "
            f"Complete essay length: approximately {length}. "
            "Include arguments, examples, and reasoning. "
            "Write only the body, not the introduction or conclusion."
        )
        heading = "Generated Full Body"

    else:
        body_prompt = (
            f"Create step-by-step arguments for a {essay_type} essay "
            f"about {topic}. Target audience: {audience}. "
            "Give clear arguments, examples, and reasoning."
        )
        heading = "Generated Step-by-Step Body"

    body = generate_response(
        body_prompt,
        temperature=temperature,
        max_tokens=2048
    )

    print(f"\n=== {heading} ===\n")
    print(body)

    # Generate conclusion
    conclusion_prompt = (
        f"Write a conclusion for a {essay_type} essay about {topic}. "
        f"Target audience: {audience}. "
        "Summarize the main arguments and end with a strong final thought. "
        "Write only the conclusion."
    )

    conclusion = generate_response(
        conclusion_prompt,
        temperature=temperature,
        max_tokens=1024
    )

    print("\n=== Generated Conclusion ===\n")
    print(conclusion)


def feedback_and_refinement():
    try:
        rating = int(input("\nRate satisfaction (1-5): ").strip())

        if rating < 1 or rating > 5:
            raise ValueError

    except ValueError:
        print("Invalid rating. Using 3.")
        rating = 3

    if rating != 5:
        feedback = input(
            "Provide feedback (tone, structure, etc.): "
        ).strip()

        print(f"\nThank you for your feedback: {feedback}")

    else:
        print("\nThank you! The essay looks good.")


def run_activity():
    print("\nWelcome to the AI Writing Assistant!")

    details = get_essay_details()

    if not details["topic"] or not details["essay_type"]:
        print("Please provide a topic and essay type to continue.")
        return

    generate_essay_content(details)
    feedback_and_refinement()


if __name__ == "__main__":
    run_activity()
