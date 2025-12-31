"""Tool 11: Digital Wellness Guide - Maintain healthy tech habits."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are a digital wellness expert for students.

Focus areas:
- Screen time management
- Social media balance
- Digital distraction reduction
- Online safety and privacy
- Tech-life boundaries
- Sleep and blue light
- Mindful technology use"""

def run():
    console.print("[bold cyan]📱 Digital Wellness Guide[/bold cyan]")
    console.print("[dim]Maintain healthy technology habits[/dim]\n")
    
    mode = Prompt.ask(
        "[green]What would you like?[/green]",
        choices=["assess-habits", "reduce-distractions", "social-media", "digital-detox"],
        default="reduce-distractions"
    )
    
    if mode == "assess-habits":
        console.print("\n[yellow]Describe your digital habits:[/yellow]")
        habits = get_multiline_input("Enter info (type 'END' when done):")
        
        prompt = f"""Assess digital wellness:

Habits: {habits}

Provide:
1. 📊 USAGE ANALYSIS
   - Patterns identified
   - Time allocation

2. ✅ HEALTHY HABITS
   - What's working

3. ⚠️ CONCERNS
   - Problem areas
   - Impact on wellbeing

4. 🔧 RECOMMENDATIONS
   - Priority changes
   - Tools to help

5. 📅 ACTION PLAN
   - Weekly goals"""

    elif mode == "reduce-distractions":
        prompt = """Reduce digital distractions:

1. 📵 PHONE STRATEGIES
   - Do Not Disturb settings
   - App limits
   - Phone-free zones

2. 💻 COMPUTER FOCUS
   - Website blockers
   - Focus modes
   - Tab management

3. 🔔 NOTIFICATION CONTROL
   - What to allow
   - Batching notifications

4. 📚 STUDY ENVIRONMENT
   - Digital-free study
   - Focus techniques

5. 🛠️ TOOLS & APPS
   - Recommended apps
   - Browser extensions"""

    elif mode == "social-media":
        platforms = Prompt.ask("[green]Platforms you use[/green]", default="Instagram, TikTok")
        
        prompt = f"""Balance social media use:

Platforms: {platforms}

Provide:
1. 📊 HEALTHY LIMITS
   - Time recommendations
   - Usage patterns

2. 🧠 MENTAL HEALTH
   - Comparison trap
   - FOMO management

3. 🛠️ PRACTICAL TOOLS
   - Time limits
   - Content curation

4. 🔄 HEALTHY HABITS
   - Mindful scrolling
   - Intentional posting

5. 💡 ALTERNATIVES
   - Real-world connections"""

    else:  # digital-detox
        duration = Prompt.ask("[green]Detox duration[/green]",
                             choices=["1-day", "weekend", "week", "ongoing"],
                             default="weekend")
        
        prompt = f"""Plan {duration} digital detox:

Provide:
1. 📋 PREPARATION
   - Before starting
   - Necessary notifications

2. 📵 DETOX RULES
   - What to avoid
   - What's allowed

3. 🎯 ACTIVITIES
   - What to do instead
   - Reconnecting offline

4. 😰 MANAGING URGES
   - Coping strategies

5. 🔄 REINTEGRATION
   - Coming back mindfully
   - New boundaries"""

    console.print("\n[yellow]Processing...[/yellow]\n")
    result = chat(prompt, SYSTEM_PROMPT)
    display_result("📱 Digital Wellness", result, "green")

if __name__ == "__main__":
    run()
