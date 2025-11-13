# boundary_coach.py
# Lumina AI MVP: Unapologetic 'No' Simulator (Updated for "Era")

import random

# --- 1. CONFIGURATION: Keywords for Weakening Boundaries ---
# The AI checks the user's response for these words, which indicate apologizing or backing down.
WEAK_KEYWORDS = ["sorry", "maybe", "next time", "but i can", "if you want", "i guess", "i apologize"]

# --- 2. THE SIMULATION SCENARIO ---
def run_simulation():
    """Sets up the scenario and manages the conversational flow."""

    print("\n--- LUMINA AI: Boundary Setting Coach ---")
    # UPDATED LINE HERE:
    print("Welcome to your **Unapologetic No Era!**")
    print("Scenario: You have established plans with a friend tonight, but your partner is pressuring you to cancel, exploiting your empathy.")
    print("Goal: Set and maintain your boundary clearly and without apologizing, justifying, or seeking compromise.")

    # Partner's initial manipulative pressure
    print("\n[Partner]: 'Are you really going out? I had a tough day, and you know I get lonely when you're gone. I really *need* you here tonight. Please cancel your friend.'")

    # --- 3. GET USER RESPONSE ---
    user_response = input("Your Response (Type your firm boundary statement): ").lower()

    # --- 4. AI ANALYSIS (Boundary Strength Check) ---
    score, feedback = analyze_response(user_response)

    # --- 5. AI RESPONSE & OUTCOME ---
    if score >= 2:
        # Strong boundary: The AI Partner backs down
        print("\n--- COACH FEEDBACK: Success! (Boundary Maintained) ---")
        print(f"**Score: {score}/3** - {feedback}")
        print("\n[Partner]: (Sighs, frustrated) 'Fine. Whatever. I'll just find something to do here myself.'")
        print("COACH NOTE: You maintained clarity and refused to accept responsibility for their emotional state. Excellent work! **You were not selfish, you were self-respecting.**")
    else:
        # Weak boundary: The AI Partner escalates the manipulation
        print("\n--- COACH FEEDBACK: Opportunity for Growth (Weakened Boundary) ---")
        print(f"**Score: {score}/3** - {feedback}")
        print("\n[Partner]: 'See? That's what I mean. You always choose your friends over me! I guess I know where I stand in your life.'")
        print("COACH NOTE: The Partner escalated because they sensed weakness. Practice removing 'weakening' keywords and stick to a simple, unyielding 'No' that honors your existing plans. Try again!")

# --- 6. CORE AI FUNCTION: NLP Logic (Basic Keyword Check) ---
def analyze_response(text):
    """Analyzes the text for signs of a weak, apologetic, or unclear boundary."""

    score = 3 # Start with a perfect score (firm and clear)
    weak_words_found = []
    feedback = []

    # Check for keywords that undermine the boundary (based on the WEAK_KEYWORDS list)
    for keyword in WEAK_KEYWORDS:
        if keyword in text:
            score -= 1
            weak_words_found.append(f"'{keyword}'")

    if not text:
        score = 0
        feedback.append("You said nothing. A clear boundary must be stated and verbalized.")

    # Apply score constraints
    if score <= 0:
        score = 0
        feedback.append("The response was unclear or completely apologetic/missing.")
    elif score < 3:
        # The user was clear but used some weak language
        feedback.append(f"Your boundary was stated, but the words {', '.join(weak_words_found)} weakened it. Avoid apologizing for your plans or justifying your decision.")
    else:
        # Perfect score
        feedback.append("Your response was clear, firm, and unapologetic. You did not justify or minimize your decision, reinforcing your self-worth.")

    return score, ' '.join(feedback)

# --- EXECUTION ---
if __name__ == "__main__":
    run_simulation()
    