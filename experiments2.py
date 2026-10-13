!pip install -q google-genai
--------------------------------------------
from google.colab import userdata
from google import genai

api_key = userdata.get("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in Colab Secrets.")

client = genai.Client(api_key=api_key)

print("✅ Gemini API connected successfully!")

baseline_prompt = "What is recursion?"
-----------------------------------------------
print("Baseline prompt defined:")
print(baseline_prompt)
------------------------------------
enhanced_prompt = (
    "You are a computer science professor. "
    "Explain recursion to a beginner using a simple real-world analogy. "
    "Write exactly two paragraphs in simple English."
)

print("Enhanced prompt defined:")
print(enhanced_prompt)
------------------------------------------
def send_prompt(prompt):
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )
    return response.text
  ------------------------------------------
try:
    baseline_response = send_prompt(baseline_prompt)

    print("=== BASELINE PROMPT ===")
    print(baseline_prompt)

    print("\n=== BASELINE RESPONSE ===")
    print(baseline_response)

except Exception as e:
    print("❌ API Error:", e)
  ---------------------------------------------------
try:
    enhanced_response = send_prompt(enhanced_prompt)

    print("=== ENHANCED PROMPT ===")
    print(enhanced_prompt)

    print("\n=== ENHANCED RESPONSE ===")
    print(enhanced_response)

except Exception as e:
    print("❌ API Error:", e)
  ----------------------------------------------
print("===== PROMPT COMPARISON =====")

print("\nBaseline response length:",
      len(baseline_response.split()), "words")

print("Enhanced response length:",
      len(enhanced_response.split()), "words")

print("\nBaseline prompt length:",
      len(baseline_prompt), "characters")

print("Enhanced prompt length:",
      len(enhanced_prompt), "characters")

print("\nAnalysis:")
print("- Baseline prompt gives a general explanation.")
print("- Enhanced prompt specifies a role, audience, analogy, and format.")
print("- Compare both answers for clarity, simplicity, and usefulness.")
