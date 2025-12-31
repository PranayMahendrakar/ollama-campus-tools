"""Tool 13: Time Management Consultant - Master your time in college."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are a time management expert for college students.

Techniques:
- Time blocking
- Pomodoro technique
- Priority matrices
- Calendar management
- Deadline planning
- Procrastination strategies"""

def run():
    console.print("[bold cyan]⏰ Time Management Consultant[/bold cyan]")
    console.print("[dim]Master your time management skills[/dim]\n")
    
    mode = Prompt.ask(
        "[green]What would you like?[/green]",
        choices=["create-system", "beat-procrastination", "weekly-planning", "productivity-audit"],
        default="weekly-planning"
    )
    
    if mode == "create-system":
        console.print("\n[yellow]Describe your current challenges:[/yellow]")
        challenges = get_multiline_input("Enter challenges (type 'END' when done):")
        
        prompt = f"""Create time management system:

Challenges: {challenges}

Provide:
1. 📋 SYSTEM OVERVIEW
   - Core principles
   - Tools needed

2. 📅 DAILY STRUCTURE
   - Morning routine
   - Study blocks
   - Evening wind-down

3. 📊 WEEKLY PLANNING
   - Planning ritual
   - Review process

4. 🎯 PRIORITIZATION
   - Framework to use
   - Decision criteria

5. 🛠️ TOOLS
   - Apps and planners
   - Setup guide"""

    elif mode == "beat-procrastination":
        task = Prompt.ask("[green]What are you procrastinating?[/green]")
        
        prompt = f"""Beat procrastination on: {task}

Provide:
1. 🧠 UNDERSTAND IT
   - Why you're stuck
   - Root causes

2. 🚀 START STRATEGIES
   - 2-minute rule
   - Smallest first step

3. 🔄 MOMENTUM BUILDERS
   - Keep going techniques

4. 🛡️ ENVIRONMENT
   - Remove obstacles
   - Enable success

5. 🎯 ACCOUNTABILITY
   - Track progress
   - Rewards"""

    elif mode == "weekly-planning":
        console.print("\n[yellow]List this week's commitments:[/yellow]")
        commitments = get_multiline_input("Enter commitments (type 'END' when done):")
        
        prompt = f"""Plan the week:

Commitments: {commitments}

Provide:
1. 📅 WEEKLY OVERVIEW
   - Day-by-day plan
   - Major blocks

2. 🎯 TOP PRIORITIES
   - Must accomplish
   - Nice to have

3. 📚 STUDY SCHEDULE
   - When and what
   - Exam prep

4. ⚖️ BALANCE CHECK
   - Work, life, health
   - Adjustments needed

5. 💡 FLEXIBILITY
   - Buffer time
   - Plan B"""

    else:  # productivity-audit
        console.print("\n[yellow]Describe a typical day:[/yellow]")
        typical_day = get_multiline_input("Enter your day (type 'END' when done):")
        
        prompt = f"""Audit your productivity:

Typical day: {typical_day}

Provide:
1. 📊 TIME ANALYSIS
   - Where time goes
   - Productive hours

2. 🕳️ TIME LEAKS
   - Wasted time
   - Distractions

3. ⚡ ENERGY PATTERNS
   - Peak times
   - Low times

4. 🔧 IMPROVEMENTS
   - Quick fixes
   - System changes

5. 📈 OPTIMIZATION
   - Better scheduling"""

    console.print("\n[yellow]Planning...[/yellow]\n")
    result = chat(prompt, SYSTEM_PROMPT)
    display_result("⏰ Time Management", result, "cyan")

if __name__ == "__main__":
    run()
