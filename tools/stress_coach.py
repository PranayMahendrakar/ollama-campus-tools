"""Tool 6: Stress Management Coach - Manage academic and life stress."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are a supportive stress management coach for students.

Approaches:
- Cognitive techniques
- Physical wellness
- Time management
- Social support
- Mindfulness
- Professional resources

Always encourage seeking professional help for serious concerns."""

def run():
    console.print("[bold cyan]🧘 Stress Management Coach[/bold cyan]")
    console.print("[dim]Manage academic and life stress effectively[/dim]\n")
    
    mode = Prompt.ask(
        "[green]What would you like?[/green]",
        choices=["assess-stress", "coping-strategies", "exam-stress", "daily-wellness"],
        default="coping-strategies"
    )
    
    if mode == "assess-stress":
        console.print("\n[yellow]Describe what's causing stress:[/yellow]")
        stressors = get_multiline_input("Enter info (type 'END' when done):")
        
        prompt = f"""Assess stress levels:

Stressors: {stressors}

Provide:
1. 📊 STRESS ANALYSIS
   - Primary sources
   - Intensity levels

2. 🎯 PRIORITY AREAS
   - What to address first
   - Quick wins available

3. 🔧 PERSONALIZED STRATEGIES
   - For each stressor
   - Practical techniques

4. 🏥 PROFESSIONAL SUPPORT
   - When to seek help
   - Campus resources

5. 💪 BUILDING RESILIENCE
   - Long-term strategies"""

    elif mode == "coping-strategies":
        stress_type = Prompt.ask("[green]Type of stress[/green]",
                                choices=["academic", "social", "financial", "personal", "general"],
                                default="academic")
        
        prompt = f"""Coping strategies for {stress_type} stress:

Provide:
1. 🚀 IMMEDIATE RELIEF
   - 5-minute techniques
   - Grounding exercises

2. 📅 DAILY PRACTICES
   - Morning routines
   - Evening wind-down

3. 🧠 COGNITIVE TECHNIQUES
   - Reframing thoughts
   - Managing worry

4. 🤸 PHYSICAL STRATEGIES
   - Movement and exercise
   - Sleep optimization

5. 👥 SOCIAL SUPPORT
   - Reaching out
   - Building connections

6. 📱 TOOLS & APPS
   - Helpful resources"""

    elif mode == "exam-stress":
        exam_situation = Prompt.ask("[green]Exam situation[/green]", default="finals week")
        
        prompt = f"""Manage exam stress:

Situation: {exam_situation}

Provide:
1. 📅 PRE-EXAM
   - Study planning
   - Avoiding cramming

2. 😰 TEST ANXIETY
   - Before the exam
   - During the exam

3. 🧠 COGNITIVE PREP
   - Positive self-talk
   - Visualization

4. 🤸 PHYSICAL PREP
   - Sleep
   - Nutrition
   - Exercise

5. ⏰ DAY-OF ROUTINE
   - Morning routine
   - Arrival strategy

6. 🎉 AFTER EXAMS
   - Healthy celebration
   - Recovery"""

    else:  # daily-wellness
        prompt = """Daily wellness routine for students:

1. 🌅 MORNING ROUTINE
   - Wake-up practices
   - Setting intentions

2. 📚 DURING CLASSES
   - Staying present
   - Managing overwhelm

3. 🍽️ MEALS & NUTRITION
   - Brain food
   - Stress-eating alternatives

4. 🌙 EVENING ROUTINE
   - Winding down
   - Sleep preparation

5. 🧘 MINDFULNESS PRACTICES
   - Simple techniques
   - Building habits

6. 📱 DIGITAL WELLNESS
   - Screen breaks
   - Social media balance"""

    console.print("\n[yellow]Processing...[/yellow]\n")
    result = chat(prompt, SYSTEM_PROMPT)
    display_result("🧘 Stress Management", result, "green")

if __name__ == "__main__":
    run()
