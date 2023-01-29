import openai

# API key
openai.api_key = "API KEY"

def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5
    )

    message = completions.choices[0].text
    return message

# TEST
prompts = ["Name some restaurants in DC", "Repeat the list with the cuisine of each restaurant", "Add the location of each restaurant"]

for prompt in prompts:
    print(prompt + "\n")
    resp = generate_response(prompt)
    print(resp + "\n\n")









