"""Tool 5: Work-Study Balance Advisor - Balance academics, work, and life."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are an expert in student work-life balance and time management.

Consider:
- Academic demands and deadlines
- Work schedules and requirements
- Personal well-being
- Social connections
- Sleep and health
- Financial needs"""

def run():
    console.print("[bold cyan]⚖️ Work-Study Balance Advisor[/bold cyan]")
    console.print("[dim]Balance academics, work, and life[/dim]\n")
    
    mode = Prompt.ask(
        "[green]What would you like?[/green]",
        choices=["assess-balance", "create-plan", "reduce-stress", "set-boundaries"],
        default="assess-balance"
    )
    
    if mode == "assess-balance":
        console.print("\n[yellow]Describe your current schedule and commitments:[/yellow]")
        schedule = get_multiline_input("Enter info (type 'END' when done):")
        
        prompt = f"""Assess work-study balance:

Current situation: {schedule}

Provide:
1. 📊 BALANCE ASSESSMENT
   - Current distribution
   - Areas of concern
   - Sustainability rating

2. ⚠️ RED FLAGS
   - Burnout indicators
   - Unsustainable patterns

3. ✅ WHAT'S WORKING
   - Positive patterns

4. 🔧 RECOMMENDATIONS
   - Immediate adjustments
   - Long-term changes

5. 💡 PRIORITIZATION GUIDE
   - What matters most
   - What can flex"""

    elif mode == "create-plan":
        hours_work = Prompt.ask("[green]Work hours per week[/green]")
        credits = Prompt.ask("[green]Credit hours this semester[/green]")
        
        prompt = f"""Create balanced schedule:

Work: {hours_work} hours/week
Credits: {credits}

Provide:
1. 📅 WEEKLY TEMPLATE
   - Block schedule
   - Protected times

2. 📚 STUDY ALLOCATION
   - Hours needed
   - When to schedule

3. 💼 WORK INTEGRATION
   - Optimal shifts
   - Avoiding conflicts

4. 🧘 SELF-CARE TIME
   - Non-negotiables
   - Recovery periods

5. 🔄 FLEXIBILITY BUFFER
   - Handling surprises"""

    elif mode == "reduce-stress":
        console.print("\n[yellow]Describe your stress points:[/yellow]")
        stressors = get_multiline_input("Enter info (type 'END' when done):")
        
        prompt = f"""Reduce work-study stress:

Stressors: {stressors}

Provide:
1. 🎯 QUICK WINS
   - Immediate relief
   - Simple changes

2. 🔧 STRUCTURAL FIXES
   - Schedule changes
   - Commitment adjustments

3. 💬 CONVERSATIONS TO HAVE
   - With employer
   - With professors

4. 🧘 COPING STRATEGIES
   - Daily practices
   - Emergency techniques"""

    else:  # set-boundaries
        prompt = """Guide for setting boundaries:

1. 💼 WORK BOUNDARIES
   - Saying no to extra shifts
   - Protecting study time

2. 📚 ACADEMIC BOUNDARIES
   - Realistic goals
   - Asking for extensions

3. 👥 SOCIAL BOUNDARIES
   - Quality over quantity
   - FOMO management

4. 💬 COMMUNICATION SCRIPTS
   - How to say no
   - Negotiating flexibility"""

    console.print("\n[yellow]Analyzing...[/yellow]\n")
    result = chat(prompt, SYSTEM_PROMPT)
    display_result("⚖️ Balance Advice", result, "yellow")

if __name__ == "__main__":
    run()
