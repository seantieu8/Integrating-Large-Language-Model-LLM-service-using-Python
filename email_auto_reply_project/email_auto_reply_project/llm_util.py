from google import genai
from .settings import GEMINI_API_KEY

def extract_sender_and_receiver_names(email_content: str):

    client = genai.Client(api_key=GEMINI_API_KEY)
    prompt = generate_prompt(email_content)
    print(email_content)


    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt)
    content = response.text

    result = str(content).strip().split("\n")
    print(f" ### ### ### Gemini response: {result=}")

    try:
        sender_name = result[0].split(":")[1].strip()

        receiver_name = result[1].split(":")[1].strip()
    except Exception as e:
        print(f"Error extracting names from Gemini response: {e}")
        sender_name = None
        receiver_name = None
    print(sender_name)
    print(receiver_name)

    try:
        inquiry_questions = [line.strip() for line in result[3:-1]]
        print(f" ### ### ### Extracted questions: {inquiry_questions=}")
    except Exception as e:
        print(f"Error extracting questions from Gemini response: {e}")
        inquiry_questions = []

    return sender_name, receiver_name, inquiry_questions


def generate_prompt(email_content):
    prompt = f"""
    Extract the sender and receiver names from the following email.

    Email Content:
    "{email_content}"

    Respond with exactly the following format:
    Sender Name: [Sender Name]
    Receiver Name: [Receiver Name]
    Inquiry Questions: [
        [First inquiry question]
        [Second inquiry question]
        ...
    ]



    Do not include any additional text, explanations, or formatting.
    If there is no name, send back "N/A".
    For names, capitalize the first letter.

    Ensure:
    - The "inquiry_questions" list contains only the extracted questions.
    - If there are no questions, return an empty list: '"inquiry_questions": []'.
    - Capitalize the first letter of the question and capitalize when needed.
    """
    return prompt
