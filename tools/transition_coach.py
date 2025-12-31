"""Tool 14: College Life Transition Coach - Navigate college transitions."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are a college transition coach helping students navigate major life changes.

Transitions:
- High school to college
- Living away from home
- Making new friends
- Academic adjustment
- Year-to-year progression
- Preparing for post-graduation"""

def run():
    console.print("[bold cyan]🎓 College Life Transition Coach[/bold cyan]")
    console.print("[dim]Navigate college transitions successfully[/dim]\n")
    
    mode = Prompt.ask(
        "[green]What transition are you facing?[/green]",
        choices=["freshman-year", "upperclassman", "homesickness", "graduation-prep"],
        default="freshman-year"
    )
    
    if mode == "freshman-year":
        concerns = Prompt.ask("[green]Main concerns[/green]", default="general adjustment")
        
        prompt = f"""First-year transition guide:

Concerns: {concerns}

Provide:
1. 📚 ACADEMIC TRANSITION
   - Differences from high school
   - Study strategies
   - Professor relationships

2. 👥 SOCIAL ADJUSTMENT
   - Making friends
   - Finding your people
   - Dealing with loneliness

3. 🏠 INDEPENDENT LIVING
   - Self-care basics
   - Managing responsibilities

4. 🧭 FINDING YOUR WAY
   - Getting involved
   - Exploring interests

5. 💪 RESILIENCE
   - Common challenges
   - Coping strategies

6. 📅 FIRST SEMESTER MILESTONES
   - Week by week guidance"""

    elif mode == "upperclassman":
        year = Prompt.ask("[green]Entering which year?[/green]",
                         choices=["sophomore", "junior", "senior"],
                         default="junior")
        
        prompt = f"""Transition to {year} year:

Provide:
1. 🎯 KEY FOCUS AREAS
   - This year's priorities

2. 📚 ACADEMIC
   - Course expectations
   - Major/career planning

3. 💼 CAREER PREP
   - What to do now
   - Timeline

4. 👥 RELATIONSHIPS
   - Evolving friendships
   - Networking

5. 🌱 PERSONAL GROWTH
   - This stage of development

6. ⚠️ COMMON PITFALLS
   - What to avoid"""

    elif mode == "homesickness":
        console.print("\n[dim]Describe what you're experiencing:[/dim]")
        feelings = get_multiline_input("Enter feelings (type 'END' when done):")
        
        prompt = f"""Address homesickness:

Feelings: {feelings}

Provide:
1. 💚 VALIDATE FEELINGS
   - This is normal
   - It gets better

2. 🔗 STAY CONNECTED
   - Healthy contact with home
   - Boundaries

3. 🌱 BUILD NEW CONNECTIONS
   - Making friends
   - Creating community

4. 🏠 CREATE COMFORT
   - Making your space home
   - Routines

5. 🆘 WHEN TO SEEK HELP
   - Warning signs
   - Resources"""

    else:  # graduation-prep
        months_left = Prompt.ask("[green]Months until graduation[/green]", default="6")
        
        prompt = f"""Prepare for graduation:

Time left: {months_left} months

Provide:
1. 📋 CHECKLIST
   - Academic requirements
   - Administrative tasks

2. 💼 CAREER PREPARATION
   - Job search timeline
   - Applications and networking

3. 💰 FINANCIAL PREP
   - Student loans
   - Budgeting for after

4. 👋 SOCIAL TRANSITION
   - Maintaining friendships
   - Saying goodbye

5. 🧠 EMOTIONAL PREP
   - Mixed feelings
   - Managing uncertainty

6. 📅 MONTH-BY-MONTH
   - What to do when"""

    console.print("\n[yellow]Processing...[/yellow]\n")
    result = chat(prompt, SYSTEM_PROMPT)
    display_result("🎓 Transition Guidance", result, "blue")

if __name__ == "__main__":
    run()
