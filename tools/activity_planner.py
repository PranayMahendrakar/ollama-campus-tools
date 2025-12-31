"""Tool 8: Extracurricular Activity Planner - Plan meaningful activities."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are an extracurricular planning expert for college students.

Consider:
- Academic commitments
- Career goals
- Personal interests
- Time constraints
- Skill development
- Resume building
- Social connections"""

def run():
    console.print("[bold cyan]🎯 Extracurricular Activity Planner[/bold cyan]")
    console.print("[dim]Plan meaningful extracurricular involvement[/dim]\n")
    
    mode = Prompt.ask(
        "[green]What would you like?[/green]",
        choices=["plan-activities", "prioritize", "leadership-path", "resume-builder"],
        default="plan-activities"
    )
    
    if mode == "plan-activities":
        goals = Prompt.ask("[green]Your goals (career, personal, social)[/green]")
        available_hours = Prompt.ask("[green]Hours available per week[/green]", default="5-10")
        
        prompt = f"""Plan extracurricular activities:

Goals: {goals}
Available time: {available_hours} hours/week

Provide:
1. 📋 RECOMMENDED ACTIVITIES
   For each (4-5):
   - Activity type
   - Time commitment
   - Benefits

2. ⚖️ BALANCED PORTFOLIO
   - Academic enrichment
   - Community service
   - Personal interests
   - Professional development

3. 📅 SCHEDULING
   - How to fit it all in
   - Seasonal considerations

4. 📈 PROGRESSION
   - Year-by-year growth
   - Deepening involvement"""

    elif mode == "prioritize":
        console.print("\n[yellow]List your current/potential activities:[/yellow]")
        activities = get_multiline_input("Enter activities (type 'END' when done):")
        
        prompt = f"""Prioritize activities:

Activities: {activities}

Provide:
1. 📊 PRIORITY RANKING
   - Tier 1 (must keep)
   - Tier 2 (valuable)
   - Tier 3 (optional)

2. 🎯 CRITERIA USED
   - Goal alignment
   - Time ROI

3. 💡 RECOMMENDATIONS
   - What to commit to
   - What to drop/reduce"""

    elif mode == "leadership-path":
        current = Prompt.ask("[green]Current involvement level[/green]")
        
        prompt = f"""Create leadership path:

Current: {current}

Provide:
1. 📈 LEADERSHIP LADDER
   - Year 1: Member
   - Year 2: Committee
   - Year 3: Officer
   - Year 4: Executive

2. 🎯 SKILLS TO DEVELOP
   - Each stage

3. 💼 OPPORTUNITIES
   - How to stand out"""

    else:  # resume-builder
        major = Prompt.ask("[green]Your major[/green]")
        career = Prompt.ask("[green]Target career[/green]")
        
        prompt = f"""Build resume through activities:

Major: {major}
Career: {career}

Provide:
1. 🎯 HIGH-IMPACT ACTIVITIES
   - Best for your field

2. 📝 SKILLS TO HIGHLIGHT
   - From each activity

3. 💼 TALKING POINTS
   - For interviews"""

    console.print("\n[yellow]Planning...[/yellow]\n")
    result = chat(prompt, SYSTEM_PROMPT)
    display_result("🎯 Activity Plan", result, "magenta")

if __name__ == "__main__":
    run()
