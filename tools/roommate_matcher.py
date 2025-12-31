"""Tool 10: Dormitory Compatibility Matcher - Find compatible roommates."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are a residential life expert helping students find compatible roommates.

Compatibility factors:
- Sleep schedules
- Study habits
- Cleanliness standards
- Social preferences
- Noise tolerance
- Guest policies
- Shared space usage"""

def run():
    console.print("[bold cyan]🏠 Dormitory Compatibility Matcher[/bold cyan]")
    console.print("[dim]Find compatible roommates and living arrangements[/dim]\n")
    
    mode = Prompt.ask(
        "[green]What would you like?[/green]",
        choices=["assess-compatibility", "roommate-profile", "conflict-resolution", "living-agreement"],
        default="roommate-profile"
    )
    
    if mode == "assess-compatibility":
        console.print("\n[yellow]Describe yourself and potential roommate:[/yellow]")
        profiles = get_multiline_input("Enter info (type 'END' when done):")
        
        prompt = f"""Assess roommate compatibility:

{profiles}

Provide:
1. 📊 COMPATIBILITY SCORE
   - Overall compatibility
   - Key matches
   - Potential conflicts

2. ✅ ALIGNED AREAS
   - Where you match
   - Strengths

3. ⚠️ POTENTIAL ISSUES
   - Differences to discuss
   - Compromise areas

4. 💬 CONVERSATION TOPICS
   - What to discuss before deciding
   - Questions to ask

5. 💡 MAKING IT WORK
   - Tips for success"""

    elif mode == "roommate-profile":
        prompt = """Create your roommate profile:

Answer these questions:

1. 😴 SLEEP HABITS
   - Typical bedtime?
   - Morning person or night owl?
   - Light/noise sensitivity?

2. 📚 STUDY HABITS
   - Where do you study?
   - Music/silence preference?
   - Study schedule?

3. 🧹 CLEANLINESS
   - Organization level?
   - Cleaning expectations?
   - Shared vs personal items?

4. 👥 SOCIAL PREFERENCES
   - Guests frequency?
   - Quiet time needs?
   - Party atmosphere?

5. 🎯 DEAL BREAKERS
   - What's non-negotiable?

Based on responses, I'll suggest:
- Ideal roommate traits
- What to look for
- Red flags to avoid"""

    elif mode == "conflict-resolution":
        console.print("\n[yellow]Describe the roommate conflict:[/yellow]")
        conflict = get_multiline_input("Enter situation (type 'END' when done):")
        
        prompt = f"""Resolve roommate conflict:

Situation: {conflict}

Provide:
1. 🔍 CONFLICT ANALYSIS
   - Root cause
   - Both perspectives

2. 💬 CONVERSATION GUIDE
   - How to bring it up
   - Non-confrontational approach

3. 🤝 SOLUTIONS
   - Compromise options
   - Win-win possibilities

4. 📋 AGREEMENTS
   - Clear expectations
   - Follow-up plans

5. 🆘 ESCALATION
   - When to involve RA
   - Room change options"""

    else:  # living-agreement
        prompt = """Create roommate living agreement:

📋 ROOMMATE AGREEMENT

1. SLEEP
   - Quiet hours: ___
   - Wake-up courtesy: ___

2. STUDYING
   - In-room study times: ___
   - Noise levels: ___

3. CLEANLINESS
   - Cleaning schedule: ___
   - Shared vs personal items: ___

4. GUESTS
   - Notice required: ___
   - Overnight guests: ___

5. SHARED ITEMS
   - What's shared: ___
   - Replacement policy: ___

6. COMMUNICATION
   - How to address issues: ___

7. CONFLICT RESOLUTION
   - Steps to follow: ___

Signatures:
_______________  _______________"""

    console.print("\n[yellow]Processing...[/yellow]\n")
    result = chat(prompt, SYSTEM_PROMPT)
    display_result("🏠 Roommate Compatibility", result, "blue")

if __name__ == "__main__":
    run()
