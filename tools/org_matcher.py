"""Tool 1: Student Organization Matching System - Find the right clubs and organizations."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are an expert student life advisor helping students find organizations.

Consider:
- Academic interests and major
- Career goals
- Personal hobbies
- Time availability
- Social preferences
- Leadership aspirations
- Skill development goals"""

def run():
    console.print("[bold cyan]🎓 Student Organization Matching System[/bold cyan]")
    console.print("[dim]Find clubs and organizations that match your interests[/dim]\n")
    
    mode = Prompt.ask(
        "[green]What would you like?[/green]",
        choices=["find-matches", "explore-types", "evaluate-fit", "involvement-plan"],
        default="find-matches"
    )
    
    if mode == "find-matches":
        major = Prompt.ask("[green]Your major/field of study[/green]")
        
        console.print("\n[yellow]Describe your interests and goals:[/yellow]")
        interests = get_multiline_input("Enter interests (type 'END' when done):")
        
        time_available = Prompt.ask("[green]Hours per week available[/green]",
                                   choices=["1-3", "4-6", "7-10", "10+"],
                                   default="4-6")
        
        prompt = f"""Match student to organizations:

Major: {major}
Interests/Goals: {interests}
Time Available: {time_available} hours/week

Provide:
1. 🎯 TOP MATCHES
   For each recommendation (5-7):
   - Organization type
   - Why it's a good match
   - Time commitment
   - Benefits

2. 📊 MATCH CATEGORIES
   - Academic/Professional orgs
   - Social/Interest clubs
   - Service organizations
   - Leadership opportunities

3. 💡 HIDDEN GEMS
   - Lesser-known options
   - Unique opportunities

4. 🔗 SKILL ALIGNMENT
   - Skills you'll develop
   - Career connections

5. 📋 NEXT STEPS
   - How to get involved
   - Questions to ask"""

    elif mode == "explore-types":
        prompt = """Explore types of student organizations:

1. 📚 ACADEMIC & PROFESSIONAL
   - Honor societies
   - Major-specific clubs
   - Pre-professional orgs

2. 🎭 ARTS & CULTURE
   - Performance groups
   - Cultural organizations
   - Creative clubs

3. 🤝 SERVICE & VOLUNTEERING
   - Community service
   - Advocacy groups
   - Mentorship programs

4. 🏃 RECREATION & SPORTS
   - Club sports
   - Intramurals
   - Outdoor clubs

5. 💼 LEADERSHIP
   - Student government
   - Peer leadership
   - Residential life

6. 🎯 SPECIAL INTEREST
   - Hobby clubs
   - Gaming groups
   - Media organizations

For each: typical activities, time commitment, benefits"""

    elif mode == "evaluate-fit":
        org_name = Prompt.ask("[green]Organization you're considering[/green]")
        
        console.print("\n[dim]What do you know about this org?[/dim]")
        org_info = get_multiline_input("Enter info (type 'END' when done):")
        
        prompt = f"""Evaluate fit for: {org_name}

Info: {org_info}

Provide:
1. ✅ POTENTIAL BENEFITS
   - Skills development
   - Networking
   - Experience

2. ⏰ TIME CONSIDERATIONS
   - Typical commitment
   - Peak busy times

3. ❓ QUESTIONS TO ASK
   - Before joining
   - At first meeting

4. 🎯 FIT ASSESSMENT
   - Good fit if...
   - Maybe not ideal if...

5. 💡 MAXIMIZING VALUE
   - How to get the most out of it"""

    else:  # involvement-plan
        console.print("\n[yellow]Describe your current situation:[/yellow]")
        situation = get_multiline_input("Enter situation (type 'END' when done):")
        
        prompt = f"""Create involvement plan:

Situation: {situation}

Provide:
1. 📅 SEMESTER PLAN
   - Recommended involvement level
   - Balanced approach

2. 🎯 PRIORITY SETTING
   - Primary organization
   - Secondary involvements

3. ⏰ TIME MANAGEMENT
   - Scheduling tips
   - Avoiding overcommitment

4. 📈 PROGRESSION PATH
   - Year 1 → Year 4 plan
   - Leadership trajectory

5. 💡 BALANCE TIPS
   - Academics + activities
   - Self-care integration"""

    console.print("\n[yellow]Finding matches...[/yellow]\n")
    result = chat(prompt, SYSTEM_PROMPT)
    display_result("🎓 Organization Matches", result, "cyan")

if __name__ == "__main__":
    run()
