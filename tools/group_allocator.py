"""Tool 4: Group Project Role Allocator - Optimize team roles and responsibilities."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are an expert in team dynamics and project management for student groups.

Consider:
- Individual strengths and skills
- Workload equity
- Learning opportunities
- Communication styles
- Schedule compatibility
- Project requirements"""

def run():
    console.print("[bold cyan]👥 Group Project Role Allocator[/bold cyan]")
    console.print("[dim]Optimize team roles and responsibilities[/dim]\n")
    
    mode = Prompt.ask(
        "[green]What would you like?[/green]",
        choices=["allocate-roles", "resolve-conflict", "balance-work", "team-contract"],
        default="allocate-roles"
    )
    
    if mode == "allocate-roles":
        console.print("\n[yellow]Describe team members and their strengths:[/yellow]")
        members = get_multiline_input("Enter member info (type 'END' when done):")
        
        project = Prompt.ask("[green]Project type[/green]")
        
        prompt = f"""Allocate roles for group project:

Project: {project}
Team: {members}

Provide:
1. 👤 ROLE ASSIGNMENTS
   For each member:
   - Assigned role
   - Responsibilities
   - Why this fits

2. 📊 TASK BREAKDOWN
   - Major tasks
   - Who owns what

3. 🔗 COLLABORATION POINTS
   - Where members interact
   - Handoff points

4. 📅 TIMELINE SUGGESTIONS
   - Milestone assignments
   - Check-in schedule

5. 💡 SUCCESS TIPS
   - Working together effectively"""

    elif mode == "resolve-conflict":
        console.print("\n[yellow]Describe the team conflict:[/yellow]")
        conflict = get_multiline_input("Enter situation (type 'END' when done):")
        
        prompt = f"""Resolve team conflict:

Situation: {conflict}

Provide:
1. 🔍 ANALYSIS
   - Root cause
   - Perspectives involved

2. 🤝 RESOLUTION STRATEGIES
   - Immediate steps
   - Long-term solutions

3. 💬 CONVERSATION GUIDE
   - How to discuss
   - Key talking points

4. 📋 AGREEMENTS TO MAKE
   - Moving forward
   - Preventing recurrence"""

    elif mode == "balance-work":
        console.print("\n[yellow]Describe current work distribution:[/yellow]")
        distribution = get_multiline_input("Enter info (type 'END' when done):")
        
        prompt = f"""Balance project workload:

Current situation: {distribution}

Provide:
1. 📊 WORKLOAD ANALYSIS
   - Current distribution
   - Imbalances identified

2. ⚖️ REBALANCING PLAN
   - Task redistribution
   - Fair allocation

3. 💬 DISCUSSION APPROACH
   - How to bring this up
   - Maintaining harmony"""

    else:  # team-contract
        project = Prompt.ask("[green]Project description[/green]")
        
        prompt = f"""Create team contract:

Project: {project}

Provide:
1. 📋 TEAM CONTRACT TEMPLATE

   ROLES & RESPONSIBILITIES:
   [Section]

   COMMUNICATION:
   - How we'll communicate
   - Response expectations

   MEETINGS:
   - Schedule
   - Attendance expectations

   WORK STANDARDS:
   - Quality expectations
   - Deadlines

   CONFLICT RESOLUTION:
   - Process

   SIGNATURES:
   [Lines for each member]"""

    console.print("\n[yellow]Processing...[/yellow]\n")
    result = chat(prompt, SYSTEM_PROMPT)
    display_result("👥 Team Allocation", result, "green")

if __name__ == "__main__":
    run()
