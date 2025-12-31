"""Tool 3: Course Schedule Optimizer - Build the perfect class schedule."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are an academic scheduling expert helping students optimize their course schedules.

Consider:
- Course requirements and prerequisites
- Time preferences (morning/afternoon/evening)
- Energy levels throughout the day
- Buffer time between classes
- Work/extracurricular commitments
- Study time needs
- Workload balance"""

def run():
    console.print("[bold cyan]📅 Course Schedule Optimizer[/bold cyan]")
    console.print("[dim]Build the perfect class schedule[/dim]\n")
    
    mode = Prompt.ask(
        "[green]What would you like?[/green]",
        choices=["optimize-schedule", "balance-workload", "time-preferences", "backup-plan"],
        default="optimize-schedule"
    )
    
    if mode == "optimize-schedule":
        console.print("\n[yellow]List courses you need to take:[/yellow]")
        courses = get_multiline_input("Enter courses (type 'END' when done):")
        
        preference = Prompt.ask("[green]Time preference[/green]",
                               choices=["early-bird", "mid-day", "afternoon", "flexible"],
                               default="flexible")
        
        commitments = Prompt.ask("[green]Other commitments (work, sports, etc.)[/green]", default="none")
        
        prompt = f"""Optimize course schedule:

Courses needed: {courses}
Time preference: {preference}
Other commitments: {commitments}

Provide:
1. 📅 OPTIMAL SCHEDULE
   - Recommended time blocks
   - Day-by-day layout

2. ⚡ ENERGY OPTIMIZATION
   - Difficult courses when alert
   - Lighter courses when tired

3. 🔄 BUFFER TIME
   - Between classes
   - For meals and breaks

4. 📚 STUDY BLOCKS
   - Recommended study times
   - Course-specific prep

5. 💡 ALTERNATIVES
   - Backup options
   - What to adjust if needed

6. ⚠️ WATCH OUT FOR
   - Potential conflicts
   - Heavy days"""

    elif mode == "balance-workload":
        console.print("\n[yellow]Describe your courses and their demands:[/yellow]")
        workload = get_multiline_input("Enter course info (type 'END' when done):")
        
        prompt = f"""Balance course workload:

Courses: {workload}

Provide:
1. 📊 WORKLOAD ANALYSIS
   - Heavy vs light courses
   - Time requirements

2. ⚖️ BALANCE RECOMMENDATIONS
   - Distribution across week
   - Avoiding overload days

3. 📅 ASSIGNMENT PLANNING
   - When to work on what
   - Avoiding deadline clusters

4. 💡 SURVIVAL TIPS
   - Managing heavy weeks
   - Getting ahead strategies"""

    elif mode == "time-preferences":
        prompt = """Help determine optimal class times:

1. 🌅 EARLY MORNING (8-10am)
   - Pros and cons
   - Best for what types

2. ☀️ MID-MORNING (10am-12pm)
   - Pros and cons
   - Best for what types

3. 🌤️ AFTERNOON (1-4pm)
   - Pros and cons
   - Best for what types

4. 🌙 EVENING (4pm+)
   - Pros and cons
   - Best for what types

5. 💡 PERSONALIZATION
   - Questions to ask yourself
   - Finding your pattern"""

    else:  # backup-plan
        console.print("\n[yellow]Describe your ideal schedule and constraints:[/yellow]")
        constraints = get_multiline_input("Enter info (type 'END' when done):")
        
        prompt = f"""Create schedule backup plans:

Constraints: {constraints}

Provide:
1. 📋 PLAN A (Ideal)
   - Best case scenario

2. 📋 PLAN B (Good Alternative)
   - If some courses unavailable

3. 📋 PLAN C (Fallback)
   - Minimum viable schedule

4. 🔄 FLEXIBILITY POINTS
   - What can be moved
   - What's fixed

5. 💡 REGISTRATION STRATEGY
   - Priority order
   - Backup sections"""

    console.print("\n[yellow]Optimizing...[/yellow]\n")
    result = chat(prompt, SYSTEM_PROMPT)
    display_result("📅 Schedule Optimization", result, "blue")

if __name__ == "__main__":
    run()
