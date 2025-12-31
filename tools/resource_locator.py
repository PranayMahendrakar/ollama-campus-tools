"""Tool 7: Campus Resource Locator - Find the right campus resources."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are a campus resource expert helping students navigate university services.

Resource categories:
- Academic support (tutoring, writing centers, advising)
- Health & wellness (counseling, health center, recreation)
- Financial (financial aid, scholarships, emergency funds)
- Career (career services, internships, job boards)
- Technology (IT help, computer labs, software)
- Student life (housing, dining, transportation)"""

def run():
    console.print("[bold cyan]🏫 Campus Resource Locator[/bold cyan]")
    console.print("[dim]Find the right campus resources for your needs[/dim]\n")
    
    mode = Prompt.ask(
        "[green]What would you like?[/green]",
        choices=["find-resource", "emergency-help", "academic-support", "all-resources"],
        default="find-resource"
    )
    
    if mode == "find-resource":
        need = Prompt.ask("[green]What do you need help with?[/green]")
        
        prompt = f"""Find campus resources for: {need}

Provide:
1. 🎯 PRIMARY RESOURCES
   - Most relevant services
   - What they offer
   - How to access

2. 🔗 RELATED RESOURCES
   - Additional support
   - Complementary services

3. 📞 CONTACT INFO
   - Typical contact methods
   - Best times to reach out

4. 💡 TIPS
   - How to get the most help
   - What to prepare"""

    elif mode == "emergency-help":
        prompt = """Emergency campus resources:

1. 🆘 IMMEDIATE CRISIS
   - Campus security/police
   - Crisis hotlines
   - Emergency services

2. 🏥 HEALTH EMERGENCIES
   - Health center
   - After-hours care
   - Mental health crisis

3. 💰 FINANCIAL EMERGENCIES
   - Emergency funds
   - Food pantries
   - Housing assistance

4. 📚 ACADEMIC EMERGENCIES
   - Dean of students
   - Incomplete policies
   - Medical withdrawals

5. 🔒 SAFETY RESOURCES
   - Safe walk/ride
   - Reporting concerns"""

    elif mode == "academic-support":
        subject = Prompt.ask("[green]Subject or area[/green]", default="general")
        
        prompt = f"""Academic support resources for {subject}:

1. 📚 TUTORING
   - Available services
   - How to schedule

2. ✍️ WRITING SUPPORT
   - Writing center
   - Online resources

3. 🧮 SUBJECT-SPECIFIC
   - Math/Science centers
   - Language labs

4. 📖 STUDY RESOURCES
   - Study groups
   - Library services

5. 👨‍🏫 INSTRUCTOR HELP
   - Office hours
   - TA support

6. 💻 ONLINE TOOLS
   - Learning platforms
   - Practice resources"""

    else:  # all-resources
        prompt = """Comprehensive campus resource guide:

1. 📚 ACADEMIC
   - Tutoring, advising, libraries

2. 🏥 HEALTH & WELLNESS
   - Health center, counseling, recreation

3. 💰 FINANCIAL
   - Financial aid, scholarships, jobs

4. 💼 CAREER
   - Career services, internships

5. 🏠 STUDENT LIFE
   - Housing, dining, transportation

6. 💻 TECHNOLOGY
   - IT help, labs, software

7. 🌍 DIVERSITY & INCLUSION
   - Cultural centers, support groups

8. ⚖️ ADVOCACY
   - Ombudsman, student rights"""

    console.print("\n[yellow]Finding resources...[/yellow]\n")
    result = chat(prompt, SYSTEM_PROMPT)
    display_result("🏫 Campus Resources", result, "cyan")

if __name__ == "__main__":
    run()
