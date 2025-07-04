import google.generativeai as genai
genai.configure(api_key="AIzaSyCBABdQso755CYVU1jdV-18sCcDHTsv-kw")  
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")
def build_prompt_basic(genre, theme, character):
    return f"Give me a short story idea based on the genre: {genre}, the theme: {theme}, and a main character who is {character}."

def build_prompt_elaborate(genre, theme, character):
    return (
        f"Imagine you are a master storyteller. Generate a unique and creative story idea with these elements:\n"
        f"- Genre: {genre}\n"
        f"- Theme: {theme}\n"
        f"- Main character: {character}\n"
        f"Include conflict, setting, and a possible twist."
    )

def build_prompt_constraint(genre, theme, character):
    openings = [
        "The last candle flickered out...",
        "Everyone had forgotten her name...",
        "It was the last summer before the war...",
        "They shouldn't have opened that door.",
        "The lights flickered one last time..."
    ]
    import random
    opening = random.choice(openings)
    return (
        f"Write a story idea that begins with: '{opening}', falls under the {genre} genre, and explores the theme of {theme}. "
        f"The protagonist is {character}."
    )
def generate_story(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f" Error: {e}"


def main():
    print("\n Welcome to the Story Idea Generator (Powered by Gemini AI)\n")

    genre = input("Enter a genre (e.g., Fantasy, Sci-Fi, Romance): ")
    theme = input("Enter a theme (e.g., Betrayal, Redemption): ")
    character = input("Describe a main character (e.g., a lonely robot): ")

    print("\nChoose a prompt style:")
    print("1. Basic")
    print("2. Elaborate")
    print("3. Constraint (with random opening line)")

    choice = input("Select (1/2/3): ").strip()

    if choice == '1':
        prompt = build_prompt_basic(genre, theme, character)
    elif choice == '2':
        prompt = build_prompt_elaborate(genre, theme, character)
    elif choice == '3':
        prompt = build_prompt_constraint(genre, theme, character)
    else:
        print(" Invalid choice. Using basic prompt.")
        prompt = build_prompt_basic(genre, theme, character)

    print("\n Generating your story idea...\n")
    story_idea = generate_story(prompt)
    print(" Here's your story idea:\n")
    print(story_idea)

    feedback = input("\n💬 Was this idea helpful? (yes/no): ")
    print("Thank you for your feedback!")

if __name__ == "__main__":
    main()
